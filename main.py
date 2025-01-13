import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

def extract_content(url, css_class, folder):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Send a request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the specified CSS class
    elements = soup.find_all(class_=css_class)

    content = {
        'h2': [],
        'p': [],
        'images': []
    }

    for element in elements:
        # Extract h2 tags
        h2_tags = element.find_all('h2')
        for h2 in h2_tags:
            content['h2'].append(h2.get_text())

        # Extract p tags
        p_tags = element.find_all('p')
        for p in p_tags:
            content['p'].append(p.get_text())

        # # Extract img tags and download images
        # img_tags = element.find_all('img')
        # for img in img_tags:
        #     img_url = img.get('src')
        #     if not img_url:
        #         continue
        #     img_url = urljoin(url, img_url)
        #     img_name = os.path.join(folder, os.path.basename(img_url))
        #     urlretrieve(img_url, img_name)
        #     content['images'].append(img_name)

    return content

# Example usage
content = extract_content('https://potterywheeldelhi.in/', 'product type-product', 'downloaded_content')
print(content)
