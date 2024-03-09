# tableau-projects-structure-mapping

## Set venv
> Make sure the virtual env is set by executing the following command in the project root:

`source .venv/bin/activate`

## Install dependencies
> Use the requirements.txt file to refer to the packages this project depends on.

`pip install -r requirements.txt`

## Execute main file
> Make sure to run this command on root directory.

`python -m main`

## Check tests coverage
> Make sure to run this command on root directory.

`coverage run --source=. -m pytest -v && coverage report`

## Run tests
> Make sure to run this command on root directory.

`python -m pytest`
