## Installation
### virtualenv
* To ensure a clean environment, please use *virtualenv* to install all packages.
* To create a new virtualenv, run `python3 -m venv env`
* To activate a virtualenv, run `source env/bin/activate`
* To deactivate a virtualenv, run `deactivate`
### install required packages
* To install packages, activate virtualenv and run `pip install -r requirements.txt`
* To install new pacakges and update requirements.txt, run `pip freeze > requirements.txt`
### local development
* To start flask server locally, run `./run_server.sh`