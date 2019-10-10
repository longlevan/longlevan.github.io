#%%
import requests
import urllib.request
import os
import wget
import time
from bs4 import BeautifulSoup

# source :https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

#url = 'https://www.residencefrederic.be/'
url = 'http://www.ibpsa.org/?page_id=962'
response = requests.get(url)
print(response)

#%% 
# If the access was successful, you should see the following output:
# <Response [200]> 200 means it went through

# Next we parse the html with BeautifulSoup so that we can work with a nicer, nested BeautifulSoup data structure. 
soup = BeautifulSoup(response.text, "html.parser")

# We use the method .findAll to locate all of our <a> tags.
anchors = soup.findAll('a')



#%%
links = []
tags = []

for tag in anchors:
    if "calibration" in str(tag):
        tags.append(tag)

    if tag.has_attr('href'):
        links.append(tag['href'])

        """
    one_a_tag = soup.findAll('img')[i]
    # print (one_a_tag['src'])
    if one_a_tag['src'].find('jpg'):
        link.append(one_a_tag['src'])
        """
print(links)
#%%
imgs_dir = '/home/vlle/Projects/2018074_TPEE_TP/img/'

BS2017_dir = '/home/vlle/zenobe/Downloads/BS2017'
if not os.path.exists(BS2017_dir):
    os.mkdir(BS2017_dir)

for link in links:
    # print ("here is your link: " + link)
    if '015.pdf' in link:
        print(link)
        download_link = link
        # myfile = requests.get(download_link)
        # open(os.path.join(imgs_dir,link.split("/")[-1]),"wb").write(myfile.content)
        urllib.request.urlretrieve(download_link,os.path.join(BS2017_dir,link.split("/")[-1]))        
        #time.sleep(1)
        # print(download_link)

# print(links)




# link = one_a_tag['src']
# print(link.find('jpg'))

# print(link)

# download_url = 'https://www.residencefrederic.be/images/tp/' + link

# urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 

# time.sleep(1)



#%%
