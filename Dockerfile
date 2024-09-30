# Inherits from the custom Dockerfile
FROM mltframework/melt:latest

# Update and upgrade the base packages
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python3 python3-pip

# Copy the necessary files for your application
COPY ./requirements.txt /code/requirements.txt
COPY ./assets /code/assets
COPY lower-thirds.mlt /code/
COPY eyebrow.mlt /code/
COPY ./main.py /code/

# Set the working directory
WORKDIR /code

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Override the ENTRYPOINT to disable the default one from the base image
ENTRYPOINT []

# Set the default command to run your FastAPI app
CMD ["fastapi", "run", "main.py"]

