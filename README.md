# tableau-projects-structure-mapping
This project parses an XML file to retrive Tableau's Projects information and creates an output CSV file containing a list of Project names with their directory structure from the respective Parent Project.

## Project Setup

### Install Python and Dependencies for project
> Follow the guide available on [Installing Python](https://testdriven.io/blog/python-environments/).

Steps:
1. `make install` - this command is dependent on [**pyenv**](https://github.com/pyenv/pyenv#installation) python manager.
2. Confirm that your current directory's python version is correct: `python --version`
3. Start venv terminal: `source .venv/bin/activate`
4. Install python dependencies for the project: `make install-deps`

_You can deactivate a venv by running `deactivate` in venv terminal when not running the code._


### Update dependencies for future use
If your new changes in the code requires a change in dependencies then update the requirements.txt file by executing the below command.

`make update-deps`

## General Development Commands
- Use virutal enviornment: 
    - `source .venv/bin/activate`
    - You can deactivate a venv by running `deactivate` in venv terminal.
> Make sure to run all `make` commands in root directory using venv.
- Execute main file: `make local`
- Check tests coverage: `make check-coverage`
- Run tests: `make test`
