import requests
import os

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload_file(self, local_path):
        file_name = os.path.basename(local_path)
        headers = {
            "Accept": "application/json",
            "Authorization": f'OAuth {self.token}'
        }
        params = {
            "path": file_name,
            "overwrite": "true"
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json()["href"]

        with open(local_path, "rb") as f:
            response = requests.put(href, files = {"file": f})

if __name__ == '__main__':
      
    TOKEN = "" 
    files = ["test_folder/test.txt", "test_folder/example.txt", "test_folder/another_one_file.txt"] # в качестве примера
    uploader = YaUploader(TOKEN)
    for file in files:
        result = uploader.upload_file(file)
    print("Success")