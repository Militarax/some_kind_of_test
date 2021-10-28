FROM python:3.8

EXPOSE 8080

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /root
COPY data ./data
COPY app.py .
COPY parse_xlsx.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN python parse_xlsx.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]