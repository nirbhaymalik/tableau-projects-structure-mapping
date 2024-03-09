# tableau-projects-structure-mapping
This project parses an XML file to retrive Tableau's Projects information and creates an output CSV file containing a list of Project names with their directory structure from the respective Parent Project.

## 1. Project Setup

### 1.1. Install Python and Dependencies for project
> [!TIP]
> Follow the guide available on [Installing Python](https://testdriven.io/blog/python-environments/).

Steps:
1. Install Python and create a virtual env: `make install`
    - _This command is dependent on [**pyenv**](https://github.com/pyenv/pyenv#installation) python manager._
2. Confirm that your current directory's python version is correct: `python --version`
3. Start venv terminal: `source .venv/bin/activate`
4. Install python dependencies for the project: `make install-deps`

_You can deactivate a venv by running `deactivate` in venv terminal when not running the code._


### 1.2. Update dependencies for future use
> [!IMPORTANT]
> It is important to update deps to keep code setup consistent for all developers.

#### _1.2.1. Code Execution Dependencies_
If your new changes in the code requires a change in dependencies then update the requirements.txt file by executing the command: `make update-deps`

#### _1.2.2. Development Dependencies_
If you have made any development related changes for example making use of Pylint, PyLance or coverage modules then add your package name and its version to `dev-requirements.txt` file.


## 2. General Development Commands
> [!IMPORTANT]
> Make sure to run all `make` commands in root directory using venv.

- Use virutal enviornment: 
    - `source .venv/bin/activate`
    - You can deactivate a venv by running `deactivate` in venv terminal.
- Execute main file: `make local`
- Run Lint: `make lint`
- Check tests coverage: `make check-coverage`
- Run tests: `make test`
