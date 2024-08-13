FROM python:3

RUN apt-get update && apt-get -y install \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-jpn

COPY requirements.txt /home
COPY ./src /home/src
COPY ./assets /home/assets

RUN pip install -U pip
RUN pip install -r /home/requirements.txt

WORKDIR /home
RUN mkdir -p /home/out
VOLUME [ "/home/out" ]

CMD ["python3", "/home/src/main.py"]
