#!/usr/bin/env python3
"""Where can I learn Python?."""


def schools_by_topic(mongo_collection, topic):
    """Python function that returns the list of a school topic."""
    return(mongo_collection.find({"topics": {"$in": [topic]}}))
