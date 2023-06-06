# Annotations

A demo of [APIFlask](https://github.com/apiflask/apiflask) to annotate a Python application to generate an OpenAPI document using the native [APIFlask OpenAPI module](https://apiflask.com/openapi/).

## Installation

* Install/verify [python3.7+](https://www.python.org/downloads/)
  - `$python --version`
  - `$python3 --version`
* Install/verify [pip3](https://pypi.org/project/pip/)
  - `$pip --version`
  - `$pip3 --version`

### Build the environment

For macOS and Linux:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

For Windows:

```shell
> python -m venv venv
> venv\Scripts\activate
> pip install -r requirements.txt
```

#### To exit the Venv

```
$ deactivate
```

### Generate the Open API Specification File

```bash
$ flask spec --format yaml --output generated_openapi.yaml
$ flask spec --format json --output generated_openapi.json
```

### Run the Flask Application

Use `flask run` command to run the example application:

```bash
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Note: you can view the OpenAPI document with `GET /openapi`

