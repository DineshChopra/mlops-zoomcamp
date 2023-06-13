# Batch Deployment

## Start Jupyter server
```bash
jupyter notebook
```
## Convert notebook into script
```bash
jupyter nbconvert --to script score.ipynb
```

## Run script file `score.py`, it will create output file `output/green/2021-01.parquet`
```bash
python3 score.py green 2021 1
```

## Install dependency
```bash
pip install -r requirements.txt
```

## Start `prefect` server
```bash
prefect orion start
```

## Set `PREFECT_API_URL` config api url
```bash
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
```

## Deploy prefedt workflow
```bash
prefect deployment create score-deploy.py
```
