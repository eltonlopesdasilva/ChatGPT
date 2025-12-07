# Conversor OCR de PDF (Português)

API FastAPI simples para converter PDFs (até 100 MB) em texto usando OCR com o Tesseract configurado para português.

## Pré-requisitos
- Python 3.10+
- Dependências de sistema: `tesseract-ocr` com o pacote de idioma português (`tesseract-ocr-por`) e `poppler-utils` (necessário para `pdf2image`).
- Bibliotecas Python listadas em `requirements.txt`.

## Instalação rápida
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução
```bash
uvicorn ocr_service.main:app --host 0.0.0.0 --port 8000
```
Acesse `http://localhost:8000/docs` para testar via Swagger.

## Uso da API
- **POST `/ocr`**: envie um arquivo PDF no campo `file` (até 100 MB). Retorna texto concatenado e total de páginas processadas.
- **GET `/health`**: verificação simples de saúde.

## Como testar rapidamente
1. Suba o servidor local conforme a seção **Execução**.
2. Verifique a saúde:
   ```bash
   curl http://localhost:8000/health
   ```
   Resposta esperada: `{ "status": "ok" }`.
3. Envie um PDF qualquer (substitua `arquivo.pdf` pelo seu):
   ```bash
   curl -X POST "http://localhost:8000/ocr" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/caminho/para/arquivo.pdf" \
     | jq
   ```
   O retorno inclui o nome do arquivo, quantidade de páginas e o texto OCR.

## Observações
- O serviço valida o tipo MIME do upload e devolve `413` para arquivos acima de 100 MB.
- Cada página é convertida em imagem (300 DPI) antes do OCR para equilibrar qualidade e memória.
- Para PDFs digitais (não digitalizados), combine com extração de texto nativa se preferir evitar OCR.
