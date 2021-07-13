FROM python:3

COPY ./requirements.txt cloud_application_example/requirements.txt

WORKDIR /cloud_application_example

RUN pip install -r requirements.txt

COPY . /cloud_application_example

ENTRYPOINT [ "python3" ]

EXPOSE 5000

CMD [ "word_number_app.py" ]
