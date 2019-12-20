import re
import os
import code
import argparse
import requests
from bs4 import BeautifulSoup
import wordcloud
from stopwords import stops


def add_or_inc_dict(tla, dict):
    try:
        dict[tla] += 1
    except:
        dict[tla] = 1

def create_histo(search_terms, max_pages):
    tla_histo = {}
    page = 1
    while page <= max_pages:
        try:
            res = requests.get('https://www.seek.com.au/jobs?keywords=' + search_terms + '&page=' + str(page))
            if res.status_code != 200:
                print('Search terms could not be used to create a valid search url.')
                break
            soup = BeautifulSoup(res.text, features="html.parser")
            jobs_on_page = bool(int(soup.find('strong', {'data-automation': 'totalJobsCount'}).get_text().replace(',', '')))
            if not jobs_on_page:
                if page==1:
                    print('No job postings were found with the search terms: %s' % search_terms[0:len(search_terms)-4].replace('-', ' '))
                break
            jobs = [article.findAll('a', href=True)[0].get('href') for article in soup.findAll('article')]
            print('Jobs found on page %i: %i' % (page, len(jobs)))
            for job in jobs:
                res = BeautifulSoup(requests.get('https://www.seek.com.au'+job).text, features='html.parser')
                text = res.find('div', {'data-automation': 'mobileTemplate'}).get_text()
                tlas = list(set(re.findall(r'(?<=[^A-Z])[A-Z]{3}(?=[^A-Z])', text)))
                for tla in tlas:
                    if tla not in stops:
                        add_or_inc_dict(tla, tla_histo)
            page += 1
        except Exception as e:
            print(e)
            break
    return tla_histo

if __name__ == "__main__":
    parser = argparse.ArgumentParser('get_tlas.py', add_help=True, description='Creates a histogram of Three Letter Acronyms (TLAs) used in job postings that match the provided search terms by crawling Seek.com.au')
    parser.add_argument('-s', nargs='*', dest='search',required=True, default='software developer', help='job search terms you\'d like to find TLAs for')
    parser.add_argument('-p', dest='pages', type=int, required=True, default=999, help='number of job listing pages to search')
    parser.add_argument('-o', dest='output', type=str, default=None, help='output file for wordcloud')
    args = parser.parse_args()
    search_terms = args.search
    print('Searching for', search_terms)
    search_terms = ' '.join(search_terms)
    histo = create_histo(search_terms, args.pages)
    if histo:
        if args.output:
            if len(args.output.split('/')) > 1:
                directories = args.output.split('/')
                directories = '/'.join(directories[0:len(directories)-1])
                if not os.path.exists(directories):
                    os.makedirs(directories)
            wc = wordcloud.WordCloud(collocations=False, repeat=False, width=800, height=400)
            wc.generate_from_frequencies(histo)
            if args.output[-4:] not in ['.jpg', '.png']:
                wc.to_file(args.output + '.png')
            else:
                wc.to_file(args.output)
        else:
            print('Navigate Histogram by calling \'histo\'')
            code.interact(local=locals())
    