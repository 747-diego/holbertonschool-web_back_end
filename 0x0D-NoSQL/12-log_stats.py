#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

client = MongoClient()
sessionTransfer = client.logs.nginx

numberOflogs = sessionTransfer.count_documents({})
number = sessionTransfer.count_documents({"method": "GET"})
statusCode = sessionTransfer.count_documents({"method": "POST"})
updatedLogs = sessionTransfer.count_documents({"method": "PUT"})
dependencies = sessionTransfer.count_documents({"method": "PATCH"})
removedLogs = sessionTransfer.count_documents({"method": "DELETE"})
PKGs = sessionTransfer.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    print(f"{numberOflogs} logs")
    print("Methods:")
    print(f"\tmethod GET: {number}")
    print(f"\tmethod POST: {statusCode}")
    print(f"\tmethod PUT: {updatedLogs}")
    print(f"\tmethod PATCH: {dependencies}")
    print(f"\tmethod DELETE: {removedLogs}")
    print(f"{PKGs} status check")
