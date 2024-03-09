# tableau-projects-structure-mapping

## Project Setup

### Install Python Environment manager
> Follow the guide available on [Installing Python](https://testdriven.io/blog/python-environments/).

Steps:
1. `pyenv install | cat .python-version`
2. `pyenv local | cat .python-version`
3. Confirm that your current directory's python version is correct: `python --version`


### Create Python Virtual environment
> _Skip this step if you already have created a venv for this project before._

Make sure to perform above steps and confirm your python version before creating venv.

`python -m venv .venv`

### Set venv
> _Skip this step if you just created a new venv in previous step as it automatically starts using the venv on creation._

To keep your global packages clean, setup a venv in the project and use that for the project.

`source .venv/bin/activate`

You can also deactivate a venv by running `deactivate` in venv terminal.


### Install dependencies in venv
Use the requirements.txt file to refer to the packages this project depends on.

`pip install -r requirements.txt`

> If your new changes in the code requires a change in dependencies then update the requirements.txt file using the following command:

`pip freeze > requirements.txt`

## General Development Commands

### Execute main file
Make sure to run this command on root directory.
`make local`

### Check tests coverage
Make sure to run this command on root directory.
`make check-coverage`

### Run tests
Make sure to run this command on root directory.
`make test`
