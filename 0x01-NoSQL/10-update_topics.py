#!/usr/bin/env python3
"""
Module creates a function that changes all topics of a school document
based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    up_topic = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return up_topic
