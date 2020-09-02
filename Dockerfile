FROM python:3-alpine
WORKDIR /bot
RUN apk add build-base libffi-dev openssl-dev
COPY requirements.txt /bot
RUN pip install -r requirements.txt
COPY bot /bot
ENTRYPOINT ["python", "main.py"]
