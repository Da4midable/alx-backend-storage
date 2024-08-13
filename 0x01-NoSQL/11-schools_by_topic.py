#!/usr/bin/env python3
"""
module creates a function that returns list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function returns the list of school having a specific topic
    """
    results = mongo_collection.find(topic)
    return results
