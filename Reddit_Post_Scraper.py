import requests
from bs4 import BeautifulSoup

class RedditImageScraper:
    def __init__(self,subreddit):
        self.subreddit = subreddit
        self.base_url = 'https://www.reddit.com'
        self.after_param = None
        self.all_image_urls = []
    
    def get_listings_url(self,sort_top_month=False,sort_hot=True,sort_top_all_time=False):
        if sort_hot:
            #Completes the URL to gather pages repeated for the rest
            listings_url = f"{self.base_url}/r/{self.subreddit}/hot/?feedViewType=compactView"
        if sort_top_month:
            listings_url = f"{self.base_url}/r/{self.subreddit}/top/?t=month"
        if sort_top_all_time:
            listings_url = f"{self.base_url}/r/{self.subreddit}/top/?t=all"


        #Checks if there is any other thing to add into the URL
        if self.after_param:
            listings_url += f"&after={self.after_param}"
        return listings_url
    
    def extract_image_details(self,post_url):
        #Response becomes an object that holds the response code and HTML information as well as headers
        response = requests.get(post_url)

        #Checks if the response code was successful (200 in this case)
        if response.ok:
            #Soup becomes the equivlent of downloading an HTML page and looking through it yourself
            soup = BeautifulSoup(response.content, 'html.parser')
            try:
                image_link_starts_with = soup.find_all('img', src=lambda x: x and x.startswith('https://preview.redd.it'))
                image_link_pull = image_link_starts_with[0]
                image_link = image_link_pull['src']
                return image_link
            except Exception as e:
                return (f'No image found [{e}]')
            finally:
                pass
    

       
    


please = RedditImageScraper("CrappyDesign")

urls = please.scrape_image_urls()

print(urls)