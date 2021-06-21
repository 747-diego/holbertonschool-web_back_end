#!/usr/bin/env python3
"""Top students."""


def top_students(mongo_collection):
    """Python function that returns all students sorted by average score."""
    topStudents = [x for x in mongo_collection.find()]
    for student in topStudents:
        average = [x.get('score', 0) for x in student.get('topics', [])]
        points = 0
        for topScore in average:
            points = points + topScore
        points = points / len(average)
        student["averageScore"] = points
    return sorted(topStudents, key=lambda z: z["averageScore"], reverse=True)
