import requests
import sys
import click
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from tqdm import tqdm


def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')


def read_links(file):
    # with open(file) as f:
    line = file.readlines()
    url = [l.strip() for l in line]
    return url


def move_to_show_directory(DL_PATH, show_title):
    '''
    Source: https://github.com/22nds/treehouse_video_downloader
    '''

    # Move to Radio Show directory
    if os.getcwd() != DL_PATH:
        os.chdir(DL_PATH)
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


def download(links, DL_PATH):

    for u in links:

        soup = get_soup(u)
        show_title = soup.find(class_="breaker-breaker").text

        print(f'Downloading {show_title}')
        move_to_show_directory(DL_PATH, show_title)

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


@click.command()
@click.option('--output', '-o', type=click.Path(), default='./', help='Download path/location')
@click.option('--file', '-f', type=click.File('r'), default='links.txt',  help='Text file containing list of show urls.')
@click.argument('link',  required=False)
def cli(output, file, link):
    '''
    Old time radio show downloader from archive.org.
    '''
    if link:
        # start downloading the files from the url
        click.echo(f'Downloading {link}')
        download([].append(link),  output)
    else:
        #  Start downloading from this  file
        click.echo(f'Getting links from \"{file.name}.\"')
        download(read_links(file), output)


if __name__ == "__main__":
    cli()
