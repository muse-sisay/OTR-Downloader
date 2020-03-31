# OTR Downloader
--

Downloader for Old Time Radio show form [Internet Archive](archive.org).

## USAGE

Sample Usage

```
	$ pyton3 OTR_downloader.py -d /download/path -u link | -f [file]
```

Arguments

```
-d 		The directory to store the downloaded file.
-u 		URL to download single show.
-f 		Download shows from a file.	
```	


## Dependencies

Install all dependencies:

```
	$ pip install -r requirements.txt
```

- beautifulsoup
- requests
- tqdm


## Show Recommendation

- Sherlock Holmes : featuring Basil Rathbone and Nigel Bruce, people say Rathbone was the best sherlock Holmes but I prefer Tom Conway.
- The Shadow : look for the one's by Orson Welles. 
- Speed Gibson of the International Secret Police
- Dragnet 

To download these shows use

```
	$ python3 OTR_downloader.py  -f -d ./
```
