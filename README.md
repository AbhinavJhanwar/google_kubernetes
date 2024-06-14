# product
1. project to create a basic docker container and run a fastapi service + streamlit
2. here we can run backend + frontend using docker compose file >> sudo docker-compose up --build or
3. run them separately, frontend >> cd frontend >> sudo docker build -t streamlit:v1 .
4. run backend >> cd backend >> sudo docker build -t fastapi:v1 .
5. build them >> frontend >> sudo docker run -p 8501:8501 streamlit:v1
6. build them >> backend >> sudo docker run -p 8000:8000 fastapi:v1

# product_ds
1. project to create a basic docker container for datascience and run a fastapi service + streamlit
2. here we can run backend + frontend using docker compose file >> sudo docker-compose up --build or
3. run them separately, frontend >> cd frontend >> sudo docker build -t streamlit:v1 .
4. run backend >> cd backend >> sudo docker build -t fastapi:v1 .
5. build them >> frontend >> sudo docker run -p 8501:8501 streamlit:v1
6. build them >> backend >> sudo docker run -p 8000:8000 fastapi:v1