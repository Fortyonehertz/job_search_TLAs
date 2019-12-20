import requests
import code
import re
from bs4 import BeautifulSoup
import sys
import argparse

def add_or_inc_dict(tla, dict):
    try:
        dict[tla] += 1
    except:
        dict[tla] = 1

def create_histo(search_terms, max_pages):
    responses = []
    tla_histo = {}
    page = 1
    while page <= max_pages:
        try:
            res = requests.get('https://www.seek.com.au/' + search_terms + '?page=' + str(page))
            soup = BeautifulSoup(res.text, features="html.parser")
            jobs_found = int(soup.find('strong', {'data-automation': 'totalJobsCount'}).get_text().replace(',', ''))
            if jobs_found < 1:
                break
            divs = soup.findAll('article')
            jobs = []
            for div in divs:
                jobs.append(div.findAll('a', href=True)[0].get('href'))
            print('Jobs found on page %i: %i' % (page, len(jobs)))
            for job in jobs:
                res = BeautifulSoup(requests.get('https://www.seek.com.au'+job).text, features='html.parser')
                text = res.find('div', {'data-automation': 'mobileTemplate'}).get_text()
                tlas = list(set(re.findall(r'(?<=[^A-Z])[A-Z]{3}(?=[^A-Z])', text)))
                for tla in tlas:
                    add_or_inc_dict(tla, tla_histo)
            page += 1
        except:
            break
    return tla_histo



if __name__ == "__main__":
    parser = argparse.ArgumentParser('Job Posting TLAs', add_help=True)
    parser.add_argument('-s', nargs='*', dest='search', required=True, default='software developer', help='job search terms you\'d like to find TLAs for')
    parser.add_argument('-p', dest='pages', type=int, required=True, default=999, help='number of job listing pages to search')
    args = parser.parse_args()
    search_terms = args.search
    search_terms.append('jobs')
    search_terms = '-'.join(search_terms)
    print('Searching for', search_terms)
    histo = create_histo(search_terms, args.pages)
    print('Navigate Histogram by calling \'histo\'')
    code.interact(local=locals())