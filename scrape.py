import requests  # allows to download HTML
from bs4 import BeautifulSoup # allows USE of HTML and grab different data, ex. use to clean up data(html)
import pprint 

for page in range(1,6): #to get results from the first 5 pages
    res = requests.get('https://news.ycombinator.com/news?=' + str(page))
    soup = BeautifulSoup(res.text, 'html.parser') #tells beautifulsoup that this is html, make an object from string
    links = soup.select('.titleline> a') # using CSS selector, returns a list
    subtext = soup.select('.subtext') # you can also chainging them ex. soup.select('.score').select .....

    def sort_stories_by_votes(hnlist):
        return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

    def create_custom_hn(links, subtext): # we have 2 lists here links and subtext, but only links is enumerated
        hn = []
        for idx, item in enumerate(links):  # use idx and enumerate because we have to access id of subtext, which is not enumerated  
            title = links[idx].getText()   # get only text with no html
            href = links[idx].get('href', None) # None is default value if case there's no link, or broken
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', '')) #convert the points to int and remove string 'points'
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sort_stories_by_votes(hn)

    pprint.pprint(create_custom_hn(links, subtext))
    