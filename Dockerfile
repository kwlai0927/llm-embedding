FROM --platform=$BUILDPLATFORM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM --platform=$TARGETPLATFORM python:3.12-slim

WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

EXPOSE 80
CMD ["python", "main.py"] 