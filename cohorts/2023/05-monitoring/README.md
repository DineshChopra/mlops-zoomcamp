## 5.2
Create conda environment
```bash
conda create -n py11 python=3.11
```

Activate conda environment
```bash
conda activate py11
```

Install requirements
```bash
pip install -r requirements.txt
```

Create all the services by using `docker-compose`
```bash
docker-compose up --build
```

Test `grafana` service on browser:
http://localhost:3000
Username: admin
Password: admin

Test `adminer` service on browser:
http://localhost:3000

## 5.3

Activate conda environment in new terminal
```bash
conda activate py11
```

Down docker-compose
```bash
docker-compose down
```

Prepare notebook to prepare model and store reference validatioin dataset
Create two directories, models, data

