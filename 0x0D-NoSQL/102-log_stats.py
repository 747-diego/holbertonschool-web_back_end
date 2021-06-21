#!/usr/bin/env python3
"""Log stats - new version."""
from pymongo import MongoClient

if __name__ == "__main__":
    user = MongoClient()
    docuLogs = user.logs
    dependencies = docuLogs.nginx
    all_docs = dependencies.find()
    numberoFdocs = dependencies.count_documents({})
    docuNum = dependencies.count_documents({"method": "GET"})
    statusCode = dependencies.count_documents({"method": "POST"})
    updatedLogs = dependencies.count_documents({"method": "PUT"})
    needLogs = dependencies.count_documents({"method": "PATCH"})
    removedLogs = dependencies.count_documents({"method": "DELETE"})
    PKGs = dependencies.count_documents({"path": "/status"})
    print(f"{numberoFdocs} logs\nMethods:")
    print(f"\tmethod GET: {docuNum}")
    print(f"\tmethod POST: {statusCode}")
    print(f"\tmethod PUT: {updatedLogs}")
    print(f"\tmethod PATCH: {needLogs}")
    print(f"\tmethod DELETE: {removedLogs}")
    print(f"{PKGs} status check")
    print("IPs:")

    packagesID = [
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    adresses = dependencies.aggregate(packagesID)
    for IPadress in adresses:
        ip = IPadress.get("_id")
        ipNum = IPadress.get("count")
        print(f"\t{ip}: {ipNum}")
