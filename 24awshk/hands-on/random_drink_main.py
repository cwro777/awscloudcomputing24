import json
import random

def random_drink():
    drinks = ["coffee", "tea", "wine", "juice"]
    return random.choice(drinks)

def lambda_handler(event, context):
    drink = random_drink()
    message = f"Hello, enjoy some {drink}"

    return {
        'statusCode': 200,
        'body': json.dumps({"message": message, "drink": drink})
    }

def main():
    # 테스트를 위한 이벤트와 컨텍스트
    event = {}
    context = {}
    
    response = lambda_handler(event, context)
    print(response)

if __name__ == "__main__":
    main()
