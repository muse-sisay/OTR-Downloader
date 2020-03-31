import requests
import sys
import getopt
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from tqdm import tqdm

RADIO_DIR = ''
URL = []


def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')


def read_links(file):
    with open(file) as f:
        line = f.readlines()
    url = [l.strip for l in line]
    return url


def move_to_show_directory(show_title):
    '''
    Source: https://github.com/22nds/treehouse_video_downloader
    '''

    # Move to Radio Show directory
    if os.getcwd() != RADIO_DIR:
        os.chdir(RADIO_DIR)
    try:
        # Make a directory with a course name
        os.mkdir(show_title)
        os.chdir(show_title)
    except FileExistsError:
        # Move to show direcotry
        os.chdir(show_title)


def download_episode(ep_name, url):
    '''
    Downloads the episode.
    Has a progress bar, using tqdm
    Source: https://gist.github.com/wy193777/0e2a4932e81afc6aa4c8f7a2984f34e2
    '''
    # Get the file size of the episode from the url
    file_size = int(urlopen(url).info().get('Content-Length', -1))

    # Check if the file is half downloaded.
    if os.path.exists(f"{ep_name}.mp3"):
        first_byte = os.path.getsize(f"{ep_name}.mp3")
    else:
        first_byte = 0

    if first_byte >= file_size:
        print(f'Skipping {ep_name}, already downloaded.')
        return

    # If previously interrupted .
    # Only get the part that is not downloaded
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}

    # Set progress bar with first_byte being the intial
    pbar = tqdm(total=file_size,  initial=first_byte,
                unit='B', unit_scale=True, desc=ep_name)

    req = requests.get(url, headers=header, stream=True)

    # Write out
    with open(f"{ep_name}.mp3", 'wb') as episode:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                episode.write(chunk)
                pbar.update(1024)

    pbar.close()


def main():

    # get arguments
    options, r = getopt.getopt(sys.argv[1:], 'd:fu:')
    # Check if arguments are supplied
    # if no arguments are supplied, exit
    if not options:
        print(
            f'Usage: python3 {sys.argv[0]} -d /download/path -u link | -f [file]')
        sys.exit(2)

    for opt, arg in options:
        # Set download dir
        if opt in '-d':
            global RADIO_DIR
            RADIO_DIR = arg

        # Read the links from file
        elif opt in '-f':
            if not arg:
                arg = 'links.txt'
            print(f'Reading Links from {arg}.')
            global URL
            URL = read_links(arg)

        # GET url
        elif opt in '-u':
            URL.append(arg)

    for u in URL:

        soup = get_soup(u)
        show_title = soup.find(class_="breaker-breaker").text

        print(f'Downloading {show_title}')
        move_to_show_directory(show_title)

        # Navigate to the download section
        u = u.replace('details', 'download')
        soup = get_soup(u)

        ep_links = soup.find_all('a')

        for l in ep_links:
            if '.mp3' in l['href']:
                ep_name = l.text.replace('_', ' ')[:-4]
                #ep_link = urljoin( u, l['href'])
                ep_link = u + '/' + l['href']
                download_episode(ep_name, ep_link)


main()
