import requests


URL = "http://127.0.0.1:8000/get_form/"

payload_list = [
    {"email": "b@gmail.com"},
    {"email": "h@gmail.com"},
    {"email": "a@gmail.com", "text": "Hello"},
    {"text": "ello"},
]


def main(data) -> None:
    for payload in data:
        response = requests.post(URL, data=payload)
        print(response.text)


if __name__ == "__main__":
    main(payload_list)
