# OTR Downloader

Download *Old Time Radio* show form the [Internet Archive](archive.org).

## USAGE   

Requires python 3+
```
$ python3 OTR_downloader.py --help                                                                               
Usage: OTR_downloader.py [OPTIONS] [LINK]

  Old time radio show downloader from archive.org.

Options:
  -o, --output PATH    Download path/location
  -f, --file FILENAME  Get links from a text file.
  --help               Show this message and exit.
	
```

To download from a link in the current direcotry 

```bash
$ python3  OTR_downloader.py [LINK]
```

## Dependencies

Install all dependencies:

```bash
$ pip install -r requirements.txt
$ # If you are using python3
$ python3 -m pip -r requirements.txt
```

- beautifulsoup
- requests
- tqdm
- click


## My Recommendation 

- Sherlock Holmes : featuring Basil Rathbone and Nigel Bruce. ( People say Basil Rathbone was the best Sherlock Holmes ever but I beg to diffrer, think Tom Conway was the best Sherlock Holmes. Let me know who you think was the best Sherlock Holmes)
- The Shadow : some episodes feauturing the Orson Welles, by far the. 
- Speed Gibson of the International Secret Polices
- Dragnet : open this and mellow back

To download these shows use

```bash
$ python3 OTR_downloader.py -f links.txt
```

There is a nice list of shows over reddit. [Old Time Radio for beginners.](https://old.reddit.com/r/otr/comments/7fyavw/old_time_radio_for_beginners/)
s