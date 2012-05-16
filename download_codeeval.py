import sys, urllib2, re
from bs4 import BeautifulSoup

SESSION_ID=''


def get_link_id(link):
    return re.match('.*?pkbid=(\d{1,}).*', str(link)).group(1)

def get_challenge_links():
    challenge_links = list()
    soup = BeautifulSoup(request('http://codeeval.com/open_challenge_scores/'))
    all_links = soup.find('table', {'class':'wide'}).find_all('a')
    challenge_links = filter(lambda(link): "scores?pkbid=" in link.attrs['href'], all_links)
    return sorted(challenge_links, key=get_link_id)

def download_challenge(challenge_href, challenge_name):
    soup =  BeautifulSoup(request(challenge_href))
    all_links = soup.find_all('a')
    submission_links = filter(lambda(link): "submissions?tid=" in link.attrs['href'], all_links)
    first_submission_href = submission_links[0].attrs['href']
    
    soup =  BeautifulSoup(request(first_submission_href))
    code_area = soup.find('div', {'class' : 'highlight'}).find('pre')
    code = ''.join(code_area.findAll(text=True)).replace("&quot;", '"')
    file_name = get_link_id(challenge_href) + '_' + challenge_name.lower().replace(' ', '_') + '.py'
    open(file_name, 'w').write(code)

def request(href):
    if "codeeval" not in href:
        href = "http://codeeval.com" + href
    req = urllib2.Request(href)
    req.add_header('Cookie', 'sessionid={0}'.format(SESSION_ID))
    return urllib2.urlopen(req).read()

def start():
    global SESSION_ID
    SESSION_ID = raw_input('enter your session id: ')

    for challenge_link in get_challenge_links():
        href = challenge_link.attrs['href']
        print 'downloading challenge from {0}'.format(href)
        download_challenge(href, challenge_link.text)


start()