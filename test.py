import requests
from zipfile import ZipFile


def download_and_extract(input_url, password, output_dir_path):
    url = input_url
    zip_path = 'test.zip'

    r = requests.get(url)
    with open(zip_path, 'wb') as f:
        f.write(r.content)
    
    with ZipFile(zip_path) as z:
        z.extractall(path=output_dir_path, pwd=bytes(password, encoding="utf-8"))

download_and_extract("http://13.235.32.23/Archive.zip", "password", "ttmp")