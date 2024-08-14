#!/usr/bin/env python3
"""
Module: cache.py

This module contains a Cache class that provides an interface to store and
retrieve data using a Redis backend.

The class is designed to generate a unique identifier for each data entry,
store the data in Redis with the identifier as the key, and flush the database
upon initialization.

Dependencies:
    - redis: This module requires the `redis-py` library to interact
    with the Redis server.
    - uuid: This module uses Python's built-in `uuid` library
    to generate unique identifiers.

Example:
    from cache import Cache

    cache = Cache()
    key = cache.store("sample data")
    print(f"Data stored with key: {key}")
"""

import redis
import uuid


class Cache:
    """
    Cache class provides methods to store data in Redis with a unique key.

    Methods:
    --------
    __init__(self) -> None:
        Initializes the Cache instance by connecting to the Redis server
         and flushing the database.

    store(self, data) -> str:
        Stores the provided data in Redis with a unique UUID key.

    Attributes:
    -----------
    _redis : redis.Redis
        A Redis client instance used to interact with the Redis server.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance by creating a connection to
        the Redis server and flushing the entire database.

        The Redis database is flushed to ensure that the database starts clean
        with each new instance of the Cache class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in Redis using a unique UUID key.

        Args:
        -----
        data : Any
            The data to be stored in Redis. The data should be
            encoded as a byte string.

        Returns:
        --------
        str
            The UUID key as a string under which the data was stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
