#!/usr/bin/env python3
"""Top students."""


def top_students(mongo_collection):
    """Python function that returns all students sorted by average score."""
    students = list(mongo_collection.find())
    return(students)
