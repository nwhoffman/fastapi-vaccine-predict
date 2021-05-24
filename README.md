# Vaccine Predictor: FastAPI demo

A demonstration using FastAPI to deploy a simple machine learning model. A trained model was saved and then loaded into the application to make predictions.

## Can symptoms predict the vaccine?

Using data from the VAERS website, we created a classifier model to predict the vaccine that was administered, based on 

### Data

The data and analysis are summarized in the included Jupyter notebook. The saved model is loaded into the application to make a prediction.

### Useage

The input is using JSON with the following fields:

```
{
  "age_yrs": 0,
  "sex": 0,
  "num_days": 0,
  "symptom1_code": 0,
  "symptom2_code": 0,
  "symptom_num": 0
}
```
Where

* `age_yrs` is a float 
* `sex` is 0 (Female) and 1 (Male)
* `num_days` is an integer (symptoms occurred number of days after vaccination)
* `symptom1_code` and `symptom2_code` are found in the table below
* `symptom_num` is an integer between 1-5 (the total number of symptoms experienced)

#### Docker

You can try out the application in a Docker container:

* Fork or clone this repo
* Build the Docker container with `docker build -t vaccine-predict`
* Generate the Docker image with `docker run -d -p 8080:5000 vaccine-predict`
* Open a browser and navigate to `http://localhost:8080/docs`

#### Heroku Application

You can also try out the app on Heroku!

https://vaccinepredict.herokuapp.com/docs

---

#### Symptom codes

|**Code 1**| **Symptom 1**|**Code 2**|**Symptom 2**|
|----|:--------------|-----------|:-----------|
|38 | Chills |    113| none|
|10 | Arthralgia (joint pain) |39| Headache|
|50 | Dizziness | 32| Fatigue|
|86 | Injection site erythema| 14| Chills|
|63 | Fatigue| 24| Dizziness|
|70 | Headache| 78| Pain|
|127| Pyrexia (fever)| 88| Pyrexia (fever)|
|11 | Asthenia (weakness)| 53| Injection site pain|
|115| Pain| 74| Nausea|
|58 | Erythema (skin redness)| 79| Pain in extremity|
|111| Nausea| 54| Injection site pruritus|
|116| Pain in extremity| 28| Dyspnoea (shortness of breath)|
|88 | Injection site pain| 72| Myalgia (muscle pain)|
|128| Rash| 87| Pruritus (itchy skin)|
|126| Pruritus (itchy skin)| 89| Rash|

