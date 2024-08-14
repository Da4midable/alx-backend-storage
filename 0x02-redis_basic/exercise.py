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
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
    -----
    method : Callable
        The method to be decorated.

    Returns:
    --------
    Callable
        The wrapped method with call counting functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
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

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Optional[Union[str, bytes, int]]:
        """
        Retrieves the data stored under the given key
        and applies the conversion function if provided.

        Args:
        -----
        key : str
            The key under which the data is stored in Redis.
        fn : Optional[Callable], default=None
            A callable function that will be used to convert
            the data to the desired format.

        Returns:
        --------
        Optional[Union[str, bytes, int]]
            The retrieved data, optionally converted using
            the provided function, or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves the data stored under the given key
        and decodes it as a UTF-8 string.

        Args:
        -----
        key : str
            The key under which the data is stored in Redis.

        Returns:
        --------
        Optional[str]
            The retrieved data decoded as a UTF-8 string,
            or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the data stored under the given key
        and converts it to an integer.

        Args:
        -----
        key : str
            The key under which the data is stored in Redis.

        Returns:
        --------
        Optional[int]
            The retrieved data converted to an integer,
            or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: int(d))
