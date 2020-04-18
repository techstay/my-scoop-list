import requests
import hashlib


def get_sha256(filename):
    with open(filename, mode='rb') as f:
        filebytes = f.read()
        filehash = hashlib.sha256(filebytes).hexdigest()
        return filehash


def get_sha256_from_remote(url, apikey):
    headers = {
        'x-apikey': apikey,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('https://www.virustotal.com/api/v3/urls', headers=headers, data={'url': url})
    analysis_id = r.json()['data']['id']
    headers = {'x-apikey': apikey}
    r = requests.get(f'https://www.virustotal.com/api/v3/analyses/{analysis_id}', headers=headers)
    return r.json()['meta']['file_info']['sha256']


def main():
    import sys
    file = sys.argv[1]
    apikey = '7c71f1745ad61c657cd5b4b2766ebccf8bd77eae335f4862b1796267d955b936'
    if file.startswith('http'):
        print(get_sha256_from_remote(file, apikey).upper())
    else:
        print(get_sha256(file).upper())


if __name__ == '__main__':
    main()
