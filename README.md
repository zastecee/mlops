
# Github setup

```bash
git config --global user.name "zastecee"
git config --global user.email "zastecee@gmail.com"
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zastecee/mlops.git
git push -u origin main
```


# MLflow + Jupyter setup

# Run using Docker compose 

Docker Compose
The MLflow repository includes a ready-to-run Compose project under docker-compose/ that provisions MLflow, PostgreSQL, and RustFS.

https://mlflow.org/docs/latest/self-hosting/
https://github.com/mlflow/mlflow/tree/master/docker-compose


```sh
git clone https://github.com/mlflow/mlflow.git
cd mlflow/docker-compose
cp .env.dev.example .env
docker compose up -d
# Open http://localhost:5000 in your browser to view the UI.
```

If you are using local tracking (option A or B), run the following command and access the MLflow UI at http://localhost:5000.

```sh
# For Option A
mlflow server --backend-store-uri sqlite:///mlflow.db --port 5000
# For Option B
mlflow server --port 5000
```


```sh
python3 -m venv .venv
source .venv/bin/activate

pip install mlflow jupyterlab
jupyter lab

mlflow ui
mlflow server --port 5000

mlflow --version

docker run -p 5001:8080 "house_sales_model"


curl -X POST http://127.0.0.1:5001/invocations   -H "Content-Type: application/json"   -d '{
      "dataframe_records": [
        {
          "Rooms": 2,
          "Bathroom": 1.0,
          "Landsize": 156.0,
          "BuildingArea": 79.0,
          "YearBuilt": 1900.0,
          "Lattitude": -37.8079,
          "Longtitude": 144.9934
        }
      ]
    }'
```