# project to create a basic docker container and run a fastapi service + streamlit
## run backend + frontend together using docker compose file 
```
sudo docker-compose up --build
```

## run them separately
### run backend 
```
cd backend 
sudo docker build -t fastapi:v1 .
sudo docker run -p 8000:8000 fastapi:v1
```
### run frontend 
```
cd frontend
sudo docker build -t streamlit:v1 .
sudo docker run -p 8501:8501 streamlit:v1
```