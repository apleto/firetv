FROM python:3.8.2

LABEL Author="Matt Castle" Email="matt.castle@apleto.com"

RUN mkdir /app
COPY . /app
WORKDIR /app

# RUN pipenv install --system
EXPOSE 5000
RUN pip install -r requirements.txt

CMD [ "python", "./firetv.py" ]