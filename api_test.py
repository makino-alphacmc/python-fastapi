import requests
import json
from datetime import datetime

def main():
    url = "http://localhost:8000/contacts"
    current_date = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "url": "https://www.example.com",
        "gender": 0,
        "message": "Hello, world!",
        "is_enabled": current_date
    }

    res = requests.post(url, json.dumps(body))
    print(res.json())

if __name__ == "__main__":
    main()
