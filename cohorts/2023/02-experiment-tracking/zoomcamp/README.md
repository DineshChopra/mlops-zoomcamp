Create an environment

```
conda create -n exp-tracking-env python=3.9
```
Deactivate an environment `conda deactivate`

Activate environment

```
conda activate exp-tracking-env
```

Install requirements

```
pip install -r requirements.txt
```

Launch mlflow UI

```
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Launch Jupyter notebook

```
jupyter notebook
```




