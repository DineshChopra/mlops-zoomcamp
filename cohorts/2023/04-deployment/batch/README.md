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
