#!/usr/bin/env python3
"""Top students."""


def top_students(mongo_collection):
    """Python function that returns all students sorted by average score."""
    students = [x for x in mongo_collection.find()]
    for student in students:
        scores = [x.get('score', 0) for x in student.get('topics', [])]
        avg = 0
        for score in scores:
            avg = avg + score
        avg = avg / len(scores)
        student["averageScore"] = avg
    return sorted(students, key=lambda z: z["averageScore"], reverse=True)
