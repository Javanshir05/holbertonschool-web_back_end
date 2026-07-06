#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient


def log_stats():
    """Provides statistics about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_nginx = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count total logs
    count_logs = db_nginx.count_documents({})
    print(f'{count_logs} logs')

    # Count logs per method
    print('Methods:')
    for method in methods:
        count_method = db_nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    # Count status check
    status_check = db_nginx.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check} status check')


if __name__ == "__main__":
    log_stats()
