import requests

res = requests.post("http://127.0.0.1:5000/chat", json={"message": "jeans"})
print(res.json())
