# Annotations

A demo of [APIFlask](https://github.com/apiflask/apiflask) to annotate a Python Application to generate an Open API Specification File.

## Installation

* Install/verify [Python3.7+](https://www.python.org/downloads/)
  - `$python --version`
  - `$python3 --version`
* Install/verify [Pip3](https://pypi.org/project/pip/)
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

```text
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
$ flask spec > oas_example.json
```

### Run the Flask Application

Use `flask run` command to run the example application:

```bash
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


