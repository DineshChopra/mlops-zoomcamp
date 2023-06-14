FROM svizor/zoomcamp-model:mlops-3.10.0-slim

RUN pip install -U pip
# RUN pip install pipenv


WORKDIR /app

# COPY [ "Pipfile", "Pipfile.lock", "./" ]
COPY [ "requirement.txt", "./"]

RUN pip install -r requirement.txt

# RUN pipenv install --system --deploy

COPY [ "starter.py", "" ]

# CMD [ "mkdir output", "cd output", "mkdir yellow", "cd ../../" ]


# ENTRYPOINT [ "python3 starter:run 2022 4" ] 

ENTRYPOINT [ "python3", "starter.py" ]
