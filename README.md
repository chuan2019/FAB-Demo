# FAB-Demo

To run the code in this demo, first create a virtual environment as follows:

```$ python -m venv .env```

then activate the virtual environment and install the dependencies:

```$ source .env/bin/activate```

```$ pip install --upgrade pip```

```$ pip install -r requirements.txt```

## Web App Demo \#1

To run the web app under the folder `demo-myview-01`, you need to go to the demo app directory and create an admin user by executing the following command:

```$ flask fab create-admin```

then run the following commands to start the web server:

```$ export FLASK_APP=app```
```$ flask run```

or you can run the following command directly too:

```$ python run.py```

The difference between the above two different ways to start web server is the port.

If you started the server using `flask run`, you can visit the web app at: `localhost:5000`.

If you started the server using `python run.py`, you can visit the web app at: `localhost:8080`.

If you don't like this difference, you can replace the port number in `run.py` with 5000. The port `8080` is just automatically assigned by FAB when the default skeleton app is created.

For more detailed explanations, please refer to my tutorial: <a href="https://chuan-zhang.medium.com/introduction-to-flask-appbuilder-building-a-simple-web-service-16ad26876ef6">Introduction to Flask AppBuilder — Building a Simple Web Service</a>

## Web App Demo \#2

To run the web app under the folder `demo-myview-02`, you need to start the `PostgreSQL` docker container first by executing the following:

```$ docker-compose up -d --build```

then do the same as what is described in the above section.

For more detailed explanations for this demo, please refer to my other tutorial: <a href="https://chuan-zhang.medium.com/introduction-to-flask-appbuilder-building-a-simple-web-service-2-786e09c59a03">Introduction to Flask AppBuilder — Building a Simple Web Service (2)</a>

