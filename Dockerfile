FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN apt-get install -y python3-psycopg2
RUN pip install Flask
RUN pip install requests
RUN pip install python-dotenv
RUN pip install flask_sqlalchemy
RUN pip install flask_migrate
RUN pip install psycopg2-binary 

WORKDIR /app

COPY . .

CMD [ "python3", "app.py"]