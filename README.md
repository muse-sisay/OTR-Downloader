# OTR Downloader
--

Downloader for downloading Old time radio show form [Internet Archive](archive.org).

## USAGE

Specify download path using the "-d" option. 

```
$ pyton3 OTR_downloader.py -d /download/path -u link | -f [file]
```

Arguments

```
-d 		The directory to store the downloaded file.
-u 		Radio show link to download
-f 		Download shows from a file 	
```	


## Dependencies

Install all dependencies:

```
pip install -r requirements.txt
```

- beautifulsoup
- requests
- tqdm


## Show Recommendation

- Sherlock Holmes : featuring Basil Rathbone and Nigel Bruce, people say Rathbone was the best sherlock Holmes but I prefer Tom Conway.
- The Shadow : look for the one's by Orson Welles. 
- Speed Gibson of the International Secret Police
- Dragnet 

To download use 

```
python3 OTR_downloader.py  -f -d ./

```
