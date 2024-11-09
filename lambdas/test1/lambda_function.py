import json
        
def lambda_handler(event, context):
    print("hello")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "test": "testing"
        })
    }