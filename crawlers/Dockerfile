FROM python:3.7.1-stretch

RUN mkdir bot_tel
COPY . /bot_tel
WORKDIR /bot_tel

RUN pip3 install -r requirements.txt

CMD ["python3.7", "bot_telegram.py"]