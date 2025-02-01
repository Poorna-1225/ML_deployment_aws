# this sets up container with python 3.10
FROM python:3.10-slim

#this copies everything in the dockerfile directory to app directory in the container
COPY . /app

#change the working directory
WORKDIR /app

#installing the libraries or dependencies
RUN pip install -r requirements.txt

#exposing port 80
EXPOSE 80

#command to run

CMD ["uvicorn","app:app","--host", "0.0.0.0", "--port", "80"]
