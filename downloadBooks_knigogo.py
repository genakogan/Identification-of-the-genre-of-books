import requests
from urllib.request import urlopen
from os.path import join
from os import makedirs


def url_download_for_each_book(url):
    html_data, url_download = [], []
    with urlopen(url) as f:
        html_data.append(f.read().decode('utf-8'))

    for line in html_data[0].split():
        if line.startswith('href="https://knigogo.net/knigi/') and line.endswith('/#lib_book_download"'):
            line = line.replace('href="', '').replace('"', '')
            url_download.append(line)
    return url_download


def url_text_download_for_each_book(url_download):
    file_text, url_text = [], []
    for url in url_download:
        with urlopen(url) as f:
            file_text.append(f.read().decode('utf-8'))

    for i in range(len(file_text)):
        for line in file_text[i].split():
            if line.startswith('href="https://knigogo.net/wp-content/uploads/') and line.endswith('.txt"'):
                line = line.replace('href="', '').replace('"', '')
                url_text.append(line)
    return url_text

# download html and return parsed doc or None on error
def download_url(urlpath):
    try:
        # open a connection to the server
        with urlopen(urlpath, timeout=3) as connection:
            # read the contents of the html doc
            return connection.read()
    except:
        # bad url, socket timeout, http forbidden, etc.
        return None

# download one book 
def download_book(url, book_id, save_path):
    # download the content
    data = download_url(url)
    if data is None:
        return f'Failed to download {url}'
    # create local path
    save_file = join(save_path, f'{book_id}.txt')
    # save book to file
    with open(save_file, 'wb') as file:
        file.write(data)
    return f'Saved {save_file}'

def download_all_books(url_text):
    for url in url_text:
        book_id = url.split('/')[-1].split('.')[0]
        print(download_book(url, book_id, save_path))

if __name__ == '__main__':
    url = 'https://knigogo.net/besplatnye-knigi/'
    save_path = 'download_books'
    # create the save directory if needed
    makedirs(save_path, exist_ok=True)
    # get a url of books that you can download
    url_download = url_download_for_each_book(url)
    # get a url of text files you can download
    url_text = url_text_download_for_each_book(url_download)
    download_all_books(url_text)
