# job_search_TLAs
Python script that creates a histogram of the Three Letter Acronyms (TLAs) found in the text of job postings on Seek.com.au

At the moment, the script creates the 'histo' object and enters interactive mode to allow the user to inspect the histogram. This will be updated to save a 'word cloud' to a specified output.


```
usage: get_tlas.py [-h] -s [SEARCH [SEARCH ...]] -p PAGES

Creates a histogram of Three Letter Acronyms (TLAs) used in
job postings that match the provided search terms by crawling
Seek.com.au
                                                            
optional arguments:
    -h, --help          show this help message and exit

required arguments:
    -s [SEARCH ...]     job search terms you'd like to 
                        find TLAs for
    -p PAGES            number of job listing pages to search
```