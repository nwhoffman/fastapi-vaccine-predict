# Import the libraries
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import uvicorn


# Declare an instance of the FastAPI class
app = FastAPI()

# Implement index route
@app.get("/")
async def index():
    return {"Message": "Welcome to the vaccine predictor!"}

class VaccineName(BaseModel):
    age_yrs: float
    sex: int
    num_days: float
    symptom1_code: int
    symptom2_code: int
    symptom_num: int

@app.post("/predict")
async def predict_vaccine(symptoms: VaccineName):
    data = symptoms.dict()
    loaded_model = load('app/trained_model.joblib')
    data_in = [data['age_yrs'], data['sex'], data['num_days'], data['symptom1_code'], data['symptom2_code'], data['symptom_num']]
    probability = loaded_model.predict_proba([data_in]).tolist()

    return {
        'probability (J&J)': probability[0][0],
        'probability (Moderna)': probability[0][1],
        'probability (Pfizer)': probability[0][2]
    }


# Run the app with the uvicorn library
if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8000)