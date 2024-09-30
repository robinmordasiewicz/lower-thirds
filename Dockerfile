FROM mltframework/melt:latest
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python3 python3-pip
COPY ./requirements.txt /code/requirements.txt
COPY ./assets /code/assets
COPY lower-thirds.mlt /code/
COPY eyebrow.mlt /code/

COPY ./main.py /code/

WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENTRYPOINT []

CMD ["fastapi", "run", "main.py"]
