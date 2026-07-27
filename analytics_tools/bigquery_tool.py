from google.cloud import bigquery
from datetime import date, datetime
from decimal import Decimal


client = bigquery.Client()


def make_json_serializable(obj):
    """
    Recursively converts BigQuery objects into JSON-safe Python objects.
    """

    if isinstance(obj, (date, datetime)):
        return obj.isoformat()

    elif isinstance(obj, Decimal):
        return float(obj)

    elif isinstance(obj, bytes):
        return obj.decode("utf-8")

    elif isinstance(obj, dict):
        return {
            key: make_json_serializable(value)
            for key, value in obj.items()
        }

    elif isinstance(obj, list):
        return [
            make_json_serializable(item)
            for item in obj
        ]

    elif isinstance(obj, tuple):
        return tuple(
            make_json_serializable(item)
            for item in obj
        )

    return obj


def run_business_query(sql: str):
    """
    Execute analytical SQL query on business data.

    Args:
        sql: BigQuery SQL query

    Returns:
        JSON serializable query results.
    """

    query_job = client.query(sql)

    results = query_job.result()

    output = []

    for row in results:

        record = dict(row)

        output.append(
            make_json_serializable(record)
        )

    return output