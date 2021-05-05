#!/usr/bin/env python3
"""Change school topics."""


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a school document."""
    name = {"name": name}
    topic = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, topic)
