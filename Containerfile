FROM python:bullseye

RUN apt update && apt -y install poppler-utils tesseract-ocr
RUN pip install pytesseract pdf2image

COPY main.py main.py
COPY entrypoint.sh  entrypoint.sh
RUN chmod +x /entrypoint.sh
#ENTRYPOINT "python" "main.py" "$@"
ENTRYPOINT ["/entrypoint.sh"]