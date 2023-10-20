# Experiment tracking

Create virtual environment
> conda create -n exp-tracking-env-22 python=3.9

Install dependency
> pip install -r requirement.txt

To run the MLflow UI locally we use the command:

```
mlflow ui --backend-store-uri sqlite:///mlflow.db
```