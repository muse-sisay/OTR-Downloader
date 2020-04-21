import requests
import click
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from tqdm import tqdm
from pathlib import Path

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')


def read_links(file):
    # with open(file) as f:
    line = file.readlines()
    url = [l.strip() for l in line]
    return url


def download_episode( f , url):
    '''
    Downloads the episode.
    Has a progress bar, using tqdm
    Source: https://gist.github.com/wy193777/0e2a4932e81afc6aa4c8f7a2984f34e2
    '''
    # Get the file size of the episode from the url
    file_size = int(urlopen(url).info().get('Content-Length', -1))
    
    # Check if the file is half downloaded.
    if f.exists() :
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
                unit='B', unit_scale=True, desc=f.stem)

    req = requests.get(url, headers=header, stream=True)

    # Write out
    with f.open('wb')as episode :
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
        
        DL_PATH = DL_PATH / show_title
        try :
            DL_PATH.mkdir()
        except FileExistsError :
            # do nothing
            pass

        # [GET] Navigate to the download section
        u = u.replace('details', 'download')
        soup = get_soup(u)

        ep_links = soup.find_all('a')

        for l in ep_links:
            if '.mp3' in l['href']:
                ep_name = l.text.replace('_', ' ')[:-4]
                #ep_link = urljoin( u, l['href'])
                ep_link = u + '/' + l['href']
                ep_name = ep_name  + '.mp3'
                download_episode( DL_PATH / ep_name , ep_link)


@click.command()
@click.option('--output', '-o', 'out_path' , type=click.Path(), default='.', help='Download path/location')
@click.option('--file', '-f', type=click.File('r'), default='links.txt',  help='Text file containing list of show urls.')
@click.argument('link',  required=False)
def cli(out_path, file, link):
    '''
    Old time radio show downloader from archive.org.
    '''
    p = Path(out_path)
    if link:
        # start downloading the files from the url
        click.echo(f'Downloading {link}')
        download([].append(link), p )
    else:
        #  Start downloading from this  file
        click.echo(f'Reading links from \"{file.name}.\"')
        download(read_links(file), p)


if __name__ == "__main__":
    cli()
