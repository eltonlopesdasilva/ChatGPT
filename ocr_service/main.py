"""Aplicação FastAPI para conversão OCR de PDFs em português.

O serviço aceita uploads de até 100 MB, converte cada página em imagem
(PDF para PNG) e aplica OCR usando o Tesseract com o pacote de idioma
português ("por").
"""
from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Iterable, List

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from pdf2image import convert_from_path
import pytesseract

MAX_FILE_SIZE_BYTES = 100 * 1024 * 1024
CHUNK_SIZE_BYTES = 1024 * 1024
ALLOWED_CONTENT_TYPES = {"application/pdf", "application/x-pdf", "application/acrobat"}

app = FastAPI(
    title="Conversor OCR PDF (Português)",
    description=(
        "API simples para extrair texto de PDFs via OCR. "
        "É necessário ter o Tesseract com o pacote de idioma português instalado."
    ),
    version="0.1.0",
)


def _ensure_pdf(content_type: str | None) -> None:
    if content_type is None or content_type.lower() not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Envie um arquivo PDF válido.")


def _save_upload_to_temp(upload: UploadFile) -> Path:
    """Grava o upload em disco sem ultrapassar 100 MB."""
    suffix = Path(upload.filename or "upload.pdf").suffix or ".pdf"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        total = 0
        while True:
            chunk = upload.file.read(CHUNK_SIZE_BYTES)
            if not chunk:
                break
            total += len(chunk)
            if total > MAX_FILE_SIZE_BYTES:
                Path(tmp.name).unlink(missing_ok=True)
                raise HTTPException(status_code=413, detail="Arquivo acima de 100 MB.")
            tmp.write(chunk)

    return Path(tmp.name)


def _convert_pdf_to_images(pdf_path: Path) -> List["pytesseract.ImageLike"]:
    try:
        # 300 DPI mantém boa resolução sem inflar memória em excesso.
        return convert_from_path(pdf_path, dpi=300, fmt="png")
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=422, detail=f"Falha ao converter PDF: {exc}") from exc


def _ocr_images(images: Iterable["pytesseract.ImageLike"]) -> List[str]:
    texts: List[str] = []
    for index, image in enumerate(images, start=1):
        try:
            text = pytesseract.image_to_string(image, lang="por+eng")
        except pytesseract.TesseractError as exc:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao processar a página {index} com o Tesseract: {exc}",
            ) from exc
        texts.append(text)
    return texts


@app.get("/health", summary="Health check")
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})


@app.post(
    "/ocr",
    summary="Extrai texto de um PDF via OCR",
    response_description="Texto concatenado de todas as páginas",
)
async def ocr_pdf(file: UploadFile = File(...)) -> JSONResponse:  # noqa: B008
    _ensure_pdf(file.content_type)

    try:
        pdf_path = _save_upload_to_temp(file)
    except HTTPException:
        raise
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Falha ao salvar arquivo: {exc}") from exc

    try:
        images = _convert_pdf_to_images(pdf_path)
        texts = _ocr_images(images)
    finally:
        pdf_path.unlink(missing_ok=True)

    response_payload = {
        "filename": file.filename,
        "pages": len(texts),
        "text": "\n\n".join(texts).strip(),
    }
    return JSONResponse(response_payload)


@app.get("/", include_in_schema=False)
async def root() -> JSONResponse:
    return JSONResponse(
        {
            "message": "API OCR pronta. Consulte /docs para testar.",
            "max_upload_mb": MAX_FILE_SIZE_BYTES // (1024 * 1024),
            "language": "por",
        }
    )
