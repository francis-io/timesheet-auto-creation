FROM python:3.10-alpine

RUN apk add --no-cache git libxslt

ADD src /

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]
