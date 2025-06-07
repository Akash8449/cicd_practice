import pandas as pd

def lambda_handler(event, context):
    df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                       "raw_grade": ["a", "b", "b", "a", "a", "e"]})
    print("Original DataFrame:")
    print(df.to_string())
    
    return {
        "statusCode": 200,
        "body": df.to_json()
    }
lambda_handler({"key": "value"}, None)  # Example call to the handler