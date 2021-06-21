import requests

download_url = 'https://github.com/marmarachain/marmara/releases/download/'
response = requests.get("https://api.github.com/repos/marmarachain/marmara/releases/latest")

print("name:" + response.json()["name"])
tag_name = response.json()["tag_name"]

linux_release_url = download_url + tag_name + '/MCL-linux.zip'
win_release_url = download_url + tag_name + '/MCL-win.zip'
print(linux_release_url)
print(win_release_url)
# print(response.json())
