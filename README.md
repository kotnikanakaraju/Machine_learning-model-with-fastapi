# Machine_learning-model-with-fastapi


Here Basically the idea is about to intergrate the machine learning models to fast api
-collect the data
#data cleaning and data preprocessing
1) train the model (based upon your choice or requirement)

2) using joblib save the model

3) predit the values or context with the model using fast api

curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 3,
  "sepal_width": 13,
  "petal_lenght": 7.4,
  "petal_width": 2
}'

Response Body
{
  "prediction": "virginica"
}
