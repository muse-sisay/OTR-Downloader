# OTR Downloader

An archiver for **Old Time Radio shows** form the [Internet Archive](archive.org).

## Install

Start by cloning the repo to your computer

```sh
$  git clone https://github.com/muse-sisay/OTR-Downloader
```

Next change directory to the repository and install the required python modules for this script.

```sh
$ cd OTR-Downloader/
$ python3 -m pip install -r requirements.txt
```

## Usage Examples

```sh
$ python3 otr-dl.py https://archive.org/details/OTRR_Dragnet_Singles
```
: download show in the current directory as the script.

```sh
$ python3 otr-dl.py -o ~/Music/OTR/ https://archive.org/details/OTRR_Dragnet_Singles
```
: show downloaded to `~/Music/OTR`


```sh
$ python3 otr-dl.py -f links.txt
```
: show links are read from  `links.txt`. Use this when you have multiple show to download.



## My Recommendation 

If you don't know where to get started, check out my favourite old time radio shows. Run the following to download them

```sh
$ python3 otr-dl.py -f links.txt
```

They include 

- **Sherlock Holmes** : featuring Basil Rathbone and Nigel Bruce. ( People say Basil Rathbone was the best Sherlock Holmes ever but I beg to diffrer, I say Tom Conway was the best Sherlock Holmes *ever*. Whom do you think played Sherlock Holmes best?)

- **Speed Gibson of the International Secret Police**

- **Dragnet** : open this and mellow back

There is a nice list of shows over reddit. [Old Time Radio for beginners.](https://old.reddit.com/r/otr/comments/7fyavw/old_time_radio_for_beginners/) While you are at it check out the sub-reddit :).