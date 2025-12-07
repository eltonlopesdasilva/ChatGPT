"""Inicializador do aplicativo macOS para o servidor OCR.

Este script é usado para gerar um `.app` no macOS via PyInstaller. Ao
executar, ele sobe o servidor FastAPI em segundo plano, pronto para
acessar `http://localhost:8000/docs`.
"""
from __future__ import annotations

import multiprocessing
import sys

import uvicorn

APP_IMPORT_PATH = "ocr_service.main:app"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000


def run_server() -> None:
    """Inicia o servidor Uvicorn com a aplicação OCR."""
    uvicorn.run(APP_IMPORT_PATH, host=DEFAULT_HOST, port=DEFAULT_PORT, reload=False)


def main() -> None:
    multiprocessing.freeze_support()
    run_server()


if __name__ == "__main__":
    sys.exit(main())
