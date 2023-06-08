FROM python:3.10.9

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["predict.py", "./"]

COPY ["mlartifacts/1/fe9c3b5aa055480fb3e605bce5be9b68/artifacts/model", "./mlartifacts/1/fe9c3b5aa055480fb3e605bce5be9b68/artifacts/model"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
