#!/usr/bin/env python3

import argparse
import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    parser = argparse.ArgumentParser(description='Test a list of URLs for their HTTP status codes and catagorize them accordingly')
    parser.add_argument('file', metavar='FILE', help='The file containing the list of URLs or domains')
    args = parser.parse_args()

    current_directory = os.getcwd()
    filename = args.file
    filename = current_directory + '/' + filename
    print(filename)
    os.mkdir('Tested_urls')
    os.chdir('Tested_urls')
    with open(filename) as f:
        urls = f.read().splitlines()
    with open('200_urls.txt', 'w') as f_200, open('300_urls.txt', 'w') as f_300, open('400_urls.txt', 'w') as f_400, open('404_urls.txt', 'w') as f_404, open('500_urls.txt', 'w') as f_500:
        for url in urls:
            try:
                if url[0:4] != 'http':
                    print(url)
                    url = 'http://' + url
                    pass
                try:
                    response = requests.get(url, verify=False, timeout=5)
                    if response.status_code == 200:
                        print(f'{url} is up!')
                        f_200.write(url + '\n')
                    elif response.status_code >= 300 and response.status_code < 400:
                        print(f'{url} is up but has a redirection status ({response.status_code})')
                        f_300.write(url + '\n')
                    elif response.status_code >= 400 and response.status_code <= 403 or response.status_code >= 405 and response.status_code < 500:
                        print(f'{url} is up but acess denied({response.status_code})')
                        f_400.write(url + '\n')
                    elif response.status_code == 404:
                        print(f'{url} is up but this url is not found ({response.status_code})')
                        f_404.write(url + '\n')
                    elif response.status_code >= 500:
                        print(f'{url} is up but there is an error({response.status_code})')
                        f_500.write(url + '\n')
                    else:
                        print(f'{url} is up but has an unknown status ({response.status_code})')
                except Exception as e:
                    print(f'{url} is down: {e}')                    
            except requests.exceptions.RequestException as e:
                print(f'{url} is down: {e}')

if __name__ == '__main__':
    main()
