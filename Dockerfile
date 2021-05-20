FROM python:3.8
RUN pip3 install fastapi uvicorn joblib sklearn
COPY ./app /app
EXPOSE 5000
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
