FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip install Flask
RUN pip install requests
RUN pip install python-dotenv

WORKDIR /app

ENV FLASK_DEBUG=1
ENV FLASK_APP=app

COPY . .

CMD [ "python3", "app.py"]