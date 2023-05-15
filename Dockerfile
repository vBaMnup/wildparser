FROM python:3.11-alpine as builder

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /wildparser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
CMD [ "python", "main.py" ]