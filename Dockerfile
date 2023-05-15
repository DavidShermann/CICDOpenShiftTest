
FROM python:alpine3.16

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--workers", "2", "--bind" ,"0.0.0.0:5000" ,"WeatherApp:app"] 

#CMD python WeatherApp.py
