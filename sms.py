import requests
import json


def send_sms(number):
    url = "https://www.fast2sms.com/dev/bulk"

    prams = {
        "authorization": "KZPwfWStEiTno7bJaNC5zHuX4lYyIB3jdGFLse1DkQg0vRUx98n3Ye9vmc4luR6QSijwCM8KDkZ72fFs",
        "sender_id": "FSTSMS",
        "route": "p",
        "language": "unicode",
        "numbers": number,
        "message": "Vehicle not parked properly"
    }
    response = requests.get(url, params=prams)
    dic = response.json()
    print(dic)


