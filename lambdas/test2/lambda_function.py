import json
        
def lambda_handler(event, context):
    print("test2")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "test": "testing"
        })
    }