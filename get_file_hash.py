import requests
import hashlib
import argparse

JSON_TEMPLATE = r'''{{
    "version": "1.0",
    "architecture": {{
        "64bit": {{
            "url": "{}",
            "hash": "{}"
        }}
    }},
    "homepage": "",
    "bin": ""
}}
'''


def get_sha256(filename):
    with open(filename, mode='rb') as f:
        filebytes = f.read()
        filehash = hashlib.sha256(filebytes).hexdigest()
        return filehash


def download_file(url, filename):
    r = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(r.content)


def write_json(name, url, hash):
    with open(f'{name}.json', 'w') as f:
        f.write(JSON_TEMPLATE.format(url, hash))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', action='store', required=True)
    parser.add_argument('-url', action='store', required=True)
    args = parser.parse_args()
    name = args.name
    url = args.url
    filename = url.split('/')[-1]
    download_file(url, filename)
    write_json(name, url, get_sha256(filename))


if __name__ == '__main__':
    main()
