import json
import random  

def random_drink():
    drinks = ["coffee", "tea", "wine", "juice"]
    return random.choice(drinks)

def lambda_handler(event, context):  # Correct function name
    drink = random_drink()
    message = f"Hello, enjoy some {drink}"  # Proper f-string formatting

    return {
        'statusCode': 200,  # Correct key name
        'body': json.dumps({"message": message, "drink": drink})  
    }
