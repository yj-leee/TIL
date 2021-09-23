import requests


url = "http://vegetable.api.postype.net/item?name="
param = "깻잎"
header = {
    "Authorization": "WjLULbBnvngmXQiAuDEQcnFJGfOvWGtBJ4sYWi9xyKJVUQGuQiIhdgKAZdM3_uIW"
}
response = requests.get(
    f"http://vegetable.api.postype.net/item?name={param}", headers=header
)
print(response.text)
