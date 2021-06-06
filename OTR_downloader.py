import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from tqdm import tqdm
from pathlib import Path
import re
import sys


class Show:
    def __init__(self, url):
        self.url = url
        self.download_url = ""
        self.title = ""
        self.description = ""
        self.episodes = []
        self.path = ""

    def __repr__(self):
        return (
            "\n"
            f"{'show:':>10} {self.title} \n"
            f"{'url:':>10} {self.url} \n"
            f"{'# of eps:':>10} {len(self.episodes)}"
            "\n"
        )


class Episode:
    def __init__(self, title, URI):
        self.title = title
        self.URI = URI
        self.url = ""


def get_soup(url):
    # TODO : catch/handle errors
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')


def read_links(filename):
    filename_txt = Path(filename)
    try:
        with open(filename_txt, 'r') as f:
            links = f.readlines()
        return [x.strip() for x in links]
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file {sys.argv[-1]}")
        exit()


def create_show_dir(parent, title):  # needs to be renamed
    # Returns local show path
    # Creates the dir if it doesnt exist
    show_path = Path(parent + title)

    try:
        show_path.mkdir()
    except FileExistsError:
        # do nothing
        pass

    return show_path


def get_all_episodes(soup):
    # *** all the files with *.mp3 file
    # in the soup file
    ep_links = []

    a_tag = soup.find_all('a')

    for a in a_tag:
        try:
            if ".mp3" in a["href"]:
                ep_links.append(
                    Episode(a.text.replace('_', ' ')[:-4],
                            a['href']))
        except KeyError:
            pass

    return ep_links


def detail_page(link):  # TODO : rename later
    return link.replace('details', 'download') + "/"


def download_show(url):

    show = Show(url)

    soup = get_soup(show.url)

    show.title = soup.find(class_="breaker-breaker").text

    show.path = create_show_dir(args.output, show.title)

    show.download_url = detail_page(show.url)
    dl_soup = get_soup(show.download_url)
    show.episodes = get_all_episodes(dl_soup)

    print(show)

    for episode in show.episodes:
        episode.url = urljoin(show.download_url, episode.URI)
        download_episode(show.path, episode)


def download_episode(path, episode):
    episode_f = path / (episode.title + ".mp3")
    print(f"{episode.title} :")
    download(episode_f, episode.url)


def download(f, url):
    '''
    Downloads the episode.
    Has a progress bar, using tqdm
    Source: https://gist.github.com/wy193777/0e2a4932e81afc6aa4c8f7a2984f34e2
    '''
    # Get the file size of the episode from the url
    file_size = int(urlopen(url).info().get('Content-Length', -1))

    # Check if the file is half downloaded.
    if f.exists():
        print(f'Resuming {f.stem}:')
        first_byte = f.stat().st_size
    else:
        first_byte = 0

    if first_byte >= file_size:
        print(f'Skipping {f.stem}, already downloaded.')
        return

    # If previously interrupted .
    # Only get the part that is not downloaded
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}

    # Set progress bar with first_byte being the intial
    pbar = tqdm(total=file_size,  initial=first_byte,
                unit='B', unit_scale=True)  # , desc=f"f.stem")

    req = requests.get(url, headers=header, stream=True)

    # Write out
    with f.open('wb')as episode:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                episode.write(chunk)
                pbar.update(1024)

    pbar.close()


parser = argparse.ArgumentParser(prog="otr-dl",
                                 description="Old time radio show downloader from archive.org.")

parser.add_argument("link",
                    metavar="LINK",
                    help="show link")
parser.add_argument("-o",
                    "--output",
                    metavar="/path",
                    default="./",
                    type=str,
                    help="path to save files")
parser.add_argument("-f",
                    action="store_true",
                    dest='file',
                    help="a file with list of OTR shows")

args = parser.parse_args()


def cli():

    if args.file:
       # Read links from args.link
        links = read_links(args.link)
        for link in links:
            download_show(link)
    else:
        download_show(args.link)


if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        print("quitting")
