import requests


URL = "http://127.0.0.1:8000/get_form/"

payload_list = [
    {"email": "b@gmail.com"},
    {"email": "a@gmail.com", "text": "Hello"},
    {"text": "ello"},
]


def main(data) -> None:
    response_list = list()
    for payload in data:
        response = requests.post(URL, data=payload)
        response_list += response.json()
    print(response_list)


if __name__ == "__main__":
    main(payload_list)
