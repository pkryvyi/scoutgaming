#FROM python:3
FROM python:3.7.5-slim

ARG API_KEY
ARG PAGE_ID
ARG METRIC_ID

ADD request.py /

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "request.py" ]