FROM python:3

#COPY ./requirements.txt /cloud_app_example/requirements.txt
COPY ./requirements.txt cloud_application_example/requirements.txt

WORKDIR /cloud_application_example

RUN pip install -r requirements.txt

#COPY . /app
COPY . /cloud_application_example

ENTRYPOINT [ "python3" ]
#ENTRYPOINT [ "word_number_app.py" ]

#CMD [ "./word_number_app.py" ]
CMD [ "word_number_app.py" ]
