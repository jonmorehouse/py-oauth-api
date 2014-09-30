# Bearer Account Api
> A turn key solution for accounts. This should be a pluggable service for any application



## Improvements

1. Connection pool (allows for multiple connections, look into gevent/greenlet support)
2. Server side cursors for account based operations (code simplicity, shouldn't be too much of a server bottleneck) 
3. Gevent/Concurrency model
4. Stronger unit testing. Right now, only integration tests of the most basic level exist 
5. Look into pickling of accounts in redis. Whenever a session exists, the account object is pickled and persisted to redis


