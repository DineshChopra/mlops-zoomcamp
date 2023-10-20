# 3.4

Deploy prefect stream:
```
prefect deploy 03-orchestration/3.4/orchestrate.py:main_flow --name taxi1 -p zoompool 
```

Then start process `zoompool`
```
prefect worker start -p zoompool
```


