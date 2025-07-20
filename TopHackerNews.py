import requests
from bs4 import BeautifulSoup
import pprint

def fetch_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtexts = soup.select('.subtext')
    return links, subtexts

def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        a_tag = item.find('a')
        if a_tag:
            title = a_tag.getText()
            href = a_tag.get('href', None)

            vote = 0
            if idx < len(subtexts):
                vote_tag = subtexts[idx].select_one('.score')
                if vote_tag:
                    vote = int(vote_tag.getText().replace(' points', ''))

            if vote > 99:
                hn.append({
                    'title': title,
                    'link': href,
                    'points': vote
                })
    return hn

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x['points'], reverse=True)


links1, subtexts1 = fetch_page('https://news.ycombinator.com/news')
links2, subtexts2 = fetch_page('https://news.ycombinator.com/news?p=2')

custom_hn_page1 = create_custom_hn(links1, subtexts1)
custom_hn_page2 = create_custom_hn(links2, subtexts2)

combined_hn = custom_hn_page1 + custom_hn_page2

sorted_hn = sort_stories_by_votes(combined_hn)
pprint.pprint(sorted_hn)