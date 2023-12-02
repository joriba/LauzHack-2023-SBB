from python

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]
