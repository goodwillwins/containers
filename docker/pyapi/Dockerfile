FROM python:3.6.14-alpine3.14

WORKDIR ./app

RUN pip3 install Flask

EXPOSE 5000

COPY ./app.py ./

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


