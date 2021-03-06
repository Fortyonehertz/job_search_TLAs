# job_search_TLAs
Python script that creates word clouds and histograms of the Three Letter Acronyms (TLAs) found in the text of job postings on Seek.com.au

## Examples
### TLAs in Top 5 Pages
#### Web Developer:
![Web Developer TLAs](https://raw.githubusercontent.com/Fortyonehertz/job_search_TLAs/master/examples/web_developer_5_pages.png "Web Developer TLAs")

#### Data Science:
![Data Science TLAs](https://raw.githubusercontent.com/Fortyonehertz/job_search_TLAs/master/examples/data_science_5_pages.png "Data Science TLAs")

#### Business Analyst
![Business Analyst TLAs](https://raw.githubusercontent.com/Fortyonehertz/job_search_TLAs/master/examples/business_analyst_5_pages.png "Business Analyst TLAs")

#### Software Engineer
![Software Engineer TLAs](https://raw.githubusercontent.com/Fortyonehertz/job_search_TLAs/master/examples/software_engineer_5_pages.png "Software Engineer TLAs")

## Setup
(Requires python3) 

Simply cd into the cloned repo and install requirements using the command:

```pip3 install -r requirements.txt```

## Usage
To run the script, use the command:

```python3 get_tlas.py -s <Your search terms> -p <number of listing pages you want to crawl>```


```
usage: get_tlas.py [-h] -s [SEARCH [SEARCH ...]] -p PAGES

Creates a histogram of Three Letter Acronyms (TLAs) used in
job postings that match the provided search terms by crawling
Seek.com.au
                                                            
optional arguments:
    -h, --help          show this help message and exit
    -o OUTPUT           output file for wordcloud

required arguments:
    -s [SEARCH ...]     job search terms you'd like to 
                        find TLAs for
    -p PAGES            number of job listing pages to search
    
```
