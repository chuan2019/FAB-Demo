# FAB-Demo

To run the code in demos \#1 and \#2, you need to create a virtual environment as follows (demo \#3 does not need local virtual environment, unless you want to run web server on your host machine separately):

```$ python -m venv .env```

then activate the virtual environment and install the dependencies:

```
$ source .env/bin/activate

$ pip install --upgrade pip

$ pip install -r requirements.txt
```

then follow the instructions described in the next two sections.

## Web App Demo \#1

To run the web app under the folder `demo-myview-01`, you need to go to the demo app directory and create an admin user by executing the following command:

```$ flask fab create-admin```

then run the following commands to start the web server:

```
$ export FLASK_APP=app

$ flask run --host=0.0.0.0 --port=8080
```

or you can run the following command directly too:

```$ python run.py```


For detailed explanations, please refer to my tutorial: <a href="https://chuan-zhang.medium.com/introduction-to-flask-appbuilder-building-a-simple-web-service-16ad26876ef6">Introduction to Flask AppBuilder — Building a Simple Web Service</a>

## Web App Demo \#2

To run the web app under the folder `demo-myview-02`, you need to start the `PostgreSQL` docker container first by executing the following:

```$ docker-compose up -d --build```

then do the same as what is described in the above section.

For more detailed explanations for this demo, please refer to my other tutorial: <a href="https://chuan-zhang.medium.com/introduction-to-flask-appbuilder-building-a-simple-web-service-2-786e09c59a03">Introduction to Flask AppBuilder — Building a Simple Web Service (2)</a>

## Web App Demo \#3

To run the web app under the folder `demo-myview-03`, you need to get your SMTP server setup, and get the file `project/jobs/res/config.yml` updated accordingly. Then start all the six containers by executing the following command

```$ docker-compose up -d --build```

For detailed explanations, please refer to my tutorial: <a href="https://chuan-zhang.medium.com/introduction-to-flask-appbuilder-integrating-with-celery-scheduler-99d37770bb62">Introduction to Flask AppBuilder - Integrating with Celery Scheduler</a>

