# TurnKey Accounts API
> A turn key solution for accounts. This implements oauth2.0 resource-owner-password credential flow with bearer token generation.

## Development

~~~ bash
# make sure to set correct environment variables per .env first

$ fig up -d postgres
$ fig up -d redis

# install all requirements
$ virtualenv .
$ pip install -r requirements.txt; pip install -r dev_requirements.txt

# run tests
$ python -m unittest discover test '*_test.py'

~~~

## Actions

1. signup/login/logout
2. forgotten_password,activate,reactivate
3. refresh_token

## Improvements

1. Connection pool (allows for multiple connections, look into gevent/greenlet support)
2. Server side cursors for account based operations (code simplicity, shouldn't be too much of a server bottleneck) 
3. Gevent/Concurrency model
4. Stronger unit testing. Right now, only integration tests of the most basic level exist 
5. Look into pickling of accounts in redis. Whenever a session exists, the account object is pickled and persisted to redis
6. Text message -> Twilio activation
7. Use redis c library
8. change python-sql library to allow for cleaner queries
