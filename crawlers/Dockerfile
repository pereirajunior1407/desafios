FROM python:3.6.9-alpine3.10

WORKDIR /bot_tel

COPY requirements.txt .
RUN apk add -u --no-cache -t build-dependencies \
    build-base \
    libffi-dev \
    xmlsec-dev \
    openssl-dev \
  && pip install -r requirements.txt \
  && apk del build-dependencies

RUN apk add -u --no-cache libxslt

COPY . .

CMD ["python", "bot_telegram.py"]