FROM python:3

COPY ./requirements.txt /cloud_app_example/requirements.txt

WORKDIR /cloud_app_example

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "./word_number_app.py" ]
