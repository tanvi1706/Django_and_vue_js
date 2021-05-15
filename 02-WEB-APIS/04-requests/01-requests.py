import requests


'''def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        print('status_code:', response.status_code)
        raise Exception("There was an error")

    data = response.json()
    print("Response:", data)
'''


def main():
    payload = {"from": "CAD", "to": "USD", "amount": 25 }
    response = requests.get("http://api.exchangeratesapi.io/v1/convert?access_key=0085b2f411d22c0f5ca09b153a458b2e", params=payload)

    '''if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")'''

    data = response.json()
    print("JSON data: ", data)


if __name__ == "__main__":
    main()
