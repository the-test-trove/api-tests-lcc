# api-tests-lcc
This repo contains boilerplate tests for anyone to get started with API test automation using lemoncheesecake test framework.

## Setup

### Requirements:
- Python3
- virtualenv
- virtualenvwrapper
```
$ pip install venv virtualenvwrapper
$ mkvirtualenv test-env
$ workon test-env
```
You will have virtual environment to use where you can install all your dependencies.


### Installation:
- Install all the dependencies.

``` pip3 install -r requirements.txt ```

- Set the PYTHONPATH to your current working directory

``` export PYTHONPATH=</path/to/your/tests directory> ```

```
example:
$ pwd
/home/username/sample/api-tests
$ export PYTHONPATH=/home/username/sample/api-tests

```

## Test Execution:
- Make the changes in the config file for actual values, there is a config.ini too with actual values for execution.

``` mv config.ini.sample config.ini ```
Make the appropriate changes to base URL in config.ini file if needed.

* To run the test against QA env, set the environment variable appropriately.
``` export ENV=prod ```
Acceptable values for ENV variable are prod/qa for this configuration, you should be able to modify the tests according to your requirements.

- To execute the API tests:

``` lcc run ```

- To view the report on the console:

``` lcc report ```
This command will display the last generated report on the console.

- To view the HTML report in browser:

``` firefox report/report.html ```


In case of any questions or clarifications, feel free to reach out.

*Compiled by: Anisha Narang* 

