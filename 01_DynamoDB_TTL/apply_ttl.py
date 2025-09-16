"""
Author: Cloud Bill

Description:
This script inserts an item into an AWS DynamoDB table with a Time To Live (TTL) attribute.
The TTL attribute determines when the item will be automatically deleted by DynamoDB.
"""

import boto3
from datetime import datetime, timedelta, timezone


def put_item_ttl(table_name: str, user_id: str, ttl_seconds: int) -> None:
    """
    Puts an item in a DynamoDB table with a TTL value of 'ttl_seconds'.

    Args:
        table_name (str): The DynamoDB table name.
        user_id (str): The user id value (Partition Key).
        ttl_seconds (int): The TTL value in seconds.
    """
    # Get the DynamoDB table
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table_name)

    # Calculate the expiration time (Unix epoch timestamp in seconds)
    ttl_timestamp = datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)
    ttl_timestamp = int(ttl_timestamp.timestamp())
    print(ttl_timestamp)

    # Write the item, including the TTL attribute
    table.put_item(
        Item={
            "user_id": f"user_{user_id}",  # This is the Partition Key
            "expires_at": str(ttl_timestamp),  # This is the TTL attribute
        }
    )


put_item_ttl(
    table_name="Users",
    user_id="1",
    ttl_seconds=60,
)
