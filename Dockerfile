FROM python:3.9.4

WORKDIR /src/test_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


# install python dependencies
RUN pip install --upgrade pip
COPY src/requirements.txt .
RUN pip install -r requirements.txt

COPY . .