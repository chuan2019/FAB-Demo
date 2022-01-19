# FAB-Demo

To run the code in this demo, first create a virtual environment as follows:

```$ python -m venv .env```

then activate the virtual environment and install the dependencies:

```$ source .env/bin/activate```

```$ pip install --upgrade pip```

```$ pip install -r requirements.txt```

then go to the demo app directory, say, demo-myview-01, and create admin user first by executing the following command:

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
