FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /lc_logs
WORKDIR /lc_logs
COPY . /lc_logs
RUN pip install -r requirements.txt