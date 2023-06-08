## Deploying a model as a web-service

* Creating a virtual environment with Pipenv
* Creating a script for predictiong 
* Putting the script into a Flask app
* Packaging the app to Docker

```bash
pip install -r requirement.txt
```

Start mlflow server
```bash
mlflow server --backend-store-uri=sqlite:///mlflow.db
```
It will launch mlflow server locally and open browser with `http://localhost:5000/`

Run below Command, It will create new model locally e.g. `mlartifacts/<experiment_id>/<RUN_ID>/artifacts/model`

`mlartifacts/1/fe9c3b5aa055480fb3e605bce5be9b68/artifacts/model`

```bash
python3 predict.py
```

Launch gunicorn web server by below command
```bash
gunicorn --bind=0.0.0.0:9696 predict:app
```

Now you can test your web service
```bash
python3 test.py
```
It will give you some prediction.
`{'duration': 45.50965007660852, 'model_version': 'fe9c3b5aa055480fb3e605bce5be9b68'}`

Create Docker file
```bash
docker build -t ride-duration-prediction-service-with-mlflow:v1 .
```

Launch Docker image
```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service-with-mlflow:v1
```

Now you can test your web service
```bash
python3 test.py
```
It will give you some prediction.
`{'duration': 45.50965007660852, 'model_version': 'fe9c3b5aa055480fb3e605bce5be9b68'}`
