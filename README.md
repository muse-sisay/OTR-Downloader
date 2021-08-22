# OTR Downloader

OTR-dl *a python script* for archiving **Old Time Radio shows** from the [Internet Archive's](https://archive.org/details/oldtimerad) Old Time Radio Collection.

## Install

#### requirment 
- You need to have python v3 installed on your machine.

Start by cloning the repo to your computer

```console
$  git clone https://github.com/muse-sisay/OTR-Downloader
```

Next change directory to the repository and install the required python modules:

```console
$ cd OTR-Downloader/
$ python3 -m pip install -r requirements.txt
```

## Usage Examples

```console
$ python3 otr-dl.py https://archive.org/details/OTRR_Dragnet_Singles
```
: download show in the current directory as the script.

```console
$ python3 otr-dl.py -o ~/Music/OTR/ https://archive.org/details/OTRR_Dragnet_Singles
```
: download to `~/Music/OTR`


```console
$ python3 otr-dl.py -f links.txt
```
: show links are read from  `links.txt`. Use this when you have multiple show to download.



## My Recommendation 

If you don't know where to start, I have added some of my favourite old time radio shows to `links.txt`. You can run the following command to download them

```console
$ python3 otr-dl.py -f links.txt
```

They list includes :

- **Sherlock Holmes** : featuring Basil Rathbone and Nigel Bruce. ( People say Basil Rathbone was the best Sherlock Holmes ever but I beg to diffrer, I say Tom Conway was the best Sherlock Holmes *ever*. Whom do you think played Sherlock Holmes best?)

- **Speed Gibson of the International Secret Police**

- **Dragnet** : open this and mellow back listening to this
 
- **X-Minus One** 

There is a nice list of shows over on reddit. [Old Time Radio for beginners.](https://old.reddit.com/r/otr/comments/7fyavw/old_time_radio_for_beginners/) While you are at it check out the sub-reddit :).
