#!/usr/bin/env python3
"""
module creates a function that provides some stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    function provides some stats about Nginx logs
    stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    delete = logs_collection.count_documents({"method": "DELETE"})
    get = logs_collection.count_documents({"method": "GET"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
