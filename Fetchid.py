import requests

TOKEN = "AQViGrOfZp3UzDnzbjQcEpmRAy80n60XqdKxo4-xBPQNUdY1BZm4ZObM47QemLcnZQvnALlz4iYgBtZ9_5CDUpWl2wUek9FvwrrUxPYzW8d32yty_HDgGC9KlqJUry0TL43DmyMaoL0No3bXBmY1fd3H-b1LFsBwY885takNbBG3y40ek1ySw_5VHt6LhZcpJHwDiI5--EiVbI4xEltPhEyB1JyRmt9eXLmz0KUzCzVQ-IkNb5gMYkkC65lEDip7tA47LX6kgl9l35y7i7yvjV_UXjUhpVFtk-cbXZ1nyl9oJB9EWfYnvL49s__XTdGatKuNj6i8bVOhsBSB5hnOpQX87_LcrA"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    "https://api.linkedin.com/v2/userinfo",
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)

if response.status_code == 200:
    data = response.json()

    member_id = data.get("sub")

    print()
    print("=" * 60)
    print("SUCCESS")
    print("=" * 60)
    print("LinkedIn Member ID:", member_id)

    if member_id:
        print("Person URN:", f"urn:li:person:{member_id}")

elif response.status_code == 401:
    print()
    print("Token is invalid, expired, or not authorized.")

elif response.status_code == 403:
    print()
    print("Token does not have the required OpenID profile permission.")

else:
    print()
    print("Unexpected LinkedIn response.")