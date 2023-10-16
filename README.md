# TECHNICAL TEST: LA TOURNEE

The aim of this README is to explain the choices made during API development as part of the technical test for La Tournée.

### Technologies used

This API is developed in **Python** using the **FastAPI** framework. Tests are realised with Pytest.

### Distribution

2 docker containers were used for this test: the first for the Python development environment, a second for launching the API. Once launched, the API can be accessed at http://localhost:8000

#### VSCode dev container

If you use VSCode, it is best to run the project in container using the DevContainer feature. It will use a standardized environements and configuration ensuring linters are active.

To run inside the container:

- Maj+Ctrl+P
- Reopen in container

Git is directly usable from container instance. Feel free to change and configure your local instance at your convenience.

While running inside the container, API logs can be accessed through a terminal outside the container using `docker logs -f technical_test_api`.

#### Docker compose

Run `docker-compose up` from root directory. Then you can access logs using `docker logs -f technical_test_api`

### Project Organization

All the features are developped inside the app folder. The `app.py` serve as a hook for the API to be ran.

The project is organized along the hexagonal lines. The "User-Side" part is in the [swagger generated automatically by FastAPI](http://localhost:8000/docs). (Accessible when the API is launched).
The "Business Logic" is found in the various Usecases, while the "Server Side" is found in the adapters.
The various bricks are completed in the [dependencies.py](app/dependencies.py) file while the routes are added in this [**init**](app/__init__.py) file.

### Trigger the API's endpoints

Go to [Swagger](http://localhost:8000/docs) and play with the differents endpoints available.

To trigger the `orders/dispatch` endpoint, you need to provide a list of dictionnary respecting a certain format, otherwise an error 422 will be thrown.

You can find different example of payload in the [tests](tests/test_api.py).

### Run the tests

You can run the different tests running the `pytest tests/` command.
