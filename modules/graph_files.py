import requests

def upload_file(token, file_path, target_folder):
    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{target_folder}/{file_path.name}:/content"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    with open(file_path, "rb") as f:
        response = requests.put(url, headers=headers, data=f)
    print(response.status_code, response.json())

def delete_file(token, item_id):
    url = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers)
    print(response.status_code)