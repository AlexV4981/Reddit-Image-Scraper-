import requests
from bs4 import BeautifulSoup


def get_image_links(subreddit):
    base_url = f"https://www.reddit.com/r/{subreddit}/?feedViewType=compactView"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content,'html.parser')

    image_links = set() #Auto remove dupes

   
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if not ("preview.redd.it" in src or src.startswith("/preview/")):
                image_links.add(src)

    return image_links

image_links = get_image_links('CrappyDesign')

print(image_links)