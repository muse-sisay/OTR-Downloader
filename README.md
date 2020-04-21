# OTR Downloader

Download *Old Time Radio* show form the [Internet Archive](archive.org).

## USAGE


```
$ python3 OTR_downloader.py --help                                                                               
Usage: OTR_downloader.py [OPTIONS] [LINK]

  Old time radio show downloader from archive.org.

Options:
  -o, --output PATH    Download path/location
  -f, --file FILENAME  Text file containing list of show urls.
  --help               Show this message and exit.
	
```

To download from a link in the current direcotry 

```
$ python3  OTR_downloader.py [LINK]
```

## Dependencies

Install all dependencies:

```
$ pip install -r requirements.txt
```

- beautifulsoup
- requests
- tqdm
- click


## My Recommendation

- Sherlock Holmes : featuring Basil Rathbone and Nigel Bruce. People say Basil 	Rathbone 	was the best Sherlock Holmes but I think Tom Conway was the best actor 	who played Sherlock Holmes, what do you think?.
- The Shadow : some episodes feauturing the Orson Welles. 
- Speed Gibson of the International Secret Police
- Dragnet

To download these shows use

```
$ python3 OTR_downloader.py 
```
