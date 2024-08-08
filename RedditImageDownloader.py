import requests
import RedditImageExtractor as RIE

def download_image(url, filename):
    response = requests.get(url,stream=True)

    if response.status_code == 200:
        with open(filename,'wb') as f:
            for chunk in response.iter_content(1024):
                
                f.write(chunk)

        return True
    else:
        return False
    
image_links = set(RIE.get_image_links('CrappyDesign'))
for index,link in enumerate(image_links):
    filename = f"image_{index}.jpg"
    download_image(link,filename)
    print(index,filename,link)