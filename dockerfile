FROM python:3.10-slim

WORKDIR /site
COPY . .

EXPOSE 1001
CMD ["python3",  "index.py"]