# Build docker image: 
```bash
docker build -t ride-duration-prediction-homework-service . 
```

# Run Docker image with parameters (year = 2022 and month = 4)
```bash
docker run -it --rm ride-duration-prediction-homework-service 2022 4
```