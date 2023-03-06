# shopAPI

Simple shop API responsible for creating ***CARTS*** and adding ***ITEMS*** to them.

**NOT READY FOR PRODUCTION**

# run project
`docker-compose up -d --build`

### to check if everything is working:
`docker-compose ps`

and/or go http://localhost

# TESTS

`pytest tests`
> make sure pythonpath is set properly before running this command localy

# Static code analyzis:

`mypy .`
> make sure pythonpath is set properly before running this command localy

# Docstrings
Generated using vscode extension:
https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

# Pythonpath
Extended **PYTHONPATH** environment variable with: 

`:.:./shop_app/mycart` or set as below:
 - Linux:

    `export PYTHONPATH=.:./shop_app/mycart`

- Win:

    TODO provide windows instructions 

previously replacing `.` w/ absolute path to this directory

# Requirements
 - docker
 - docker-compose

## dev requirements
 - python 3.10.9

## requirements.txt

- All requirements needed to launch backend are specified in `./shop_app/requirements.txt` 

- You can also install `./shop_app/requirements-dev.txt` which constists tools needed for developing & testing.


# Ignore
- While checking this project you can ignore `/itemDomain` endpoint, `./shop_app/shop_domain` directory and `./tests/shop_domain` tests. It is just silly domain logic that I was playing around.

- `docker-compose.debug.yml` - is for debugging through vs code & can be ignored.

- `todo.md` - includes dev notes, don't read it ;-) 

# It's not yet my final form
 - this project is still under development
 - created for learning and recruitment processes 