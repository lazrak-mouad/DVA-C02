"""
Author: Cloud Bill

Description:
This script inserts an item into an AWS DynamoDB table with a Time To Live (TTL) attribute.
The TTL attribute determines when the item will be automatically deleted by DynamoDB.
"""

import boto3
from datetime import datetime, timedelta, timezone


def put_item_ttl(table_name: str, user_id: str, ttl_seconds: int) -> None:
    """Write an item with a DynamoDB TTL attribute.

    Inserts (or overwrites) an item in `table_name` with a partition key
    `user_id` and a top-level `expires_at` attribute set to an epoch timestamp
    in **seconds** (Number type). When TTL is enabled on the table for
    `expires_at`, DynamoDB will eventually delete the item after it expires.

    Args:
        table_name (str): Name of the DynamoDB table.
        user_id (str): Logical user identifier to compose the partition key.
        ttl_seconds (int): Number of seconds from now when the item should expire.
    """
    # Create a DynamoDB resource client
    dynamodb = boto3.resource("dynamodb")

    # Get a the DynamoDB table
    table = dynamodb.Table(table_name)

    # Compute expiration as UTC epoch seconds (must be a Number in DynamoDB)
    ttl_timestamp = int(
        (datetime.now(timezone.utc) + timedelta(seconds=ttl_seconds)).timestamp()
    )
    print(ttl_timestamp)

    # Write the item to the 'Users' table
    table.put_item(
        Item={
            "user_id": f"user_{user_id}",
            "expires_at": ttl_timestamp,
        }
    )


put_item_ttl(
    table_name="Users",
    user_id="4",
    ttl_seconds=60,
)
