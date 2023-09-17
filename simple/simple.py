import logging
from urllib.parse import urljoin
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import os
import asyncio
from playwright.async_api import async_playwright
import requests


# async def main():
#    async with async_playwright() as pw:
#         page = context.new_page()
#         page.goto('https://thuvienphapluat.vn/bieumau?q=&type=2')

#         # Interact with login form
#         page.get_by_label("Tên đăng nhập hoặc Email").fill("0046isk@gmail.com")
#         page.get_by_label("Mật khẩu").fill("password")
#         page.get_by_role("button", name="Đăng nhập").click()

#         #add code to crawler
    
 
#         await page.wait_for_timeout(5000)
 
#         all_images = await page.query_selector_all('img')
#         images = []
#         for i, img in enumerate(all_images):
#             image_url = await img.get_attribute("src")
#             content = requests.get(image_url).content
#             with open('image_{}.svg'.format(i), 'wb') as f:
#                 f.write(content)
#             images.append(image_url)
#             print(images)
#             await browser.close()
 
# if __name__ == '__main__':
#    asyncio.run(main())







logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[]):
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and '/bieumau/' in path:
                path = urljoin(url, path)
                print(path)
                with open("/Users/roy/Documents/Hacker/Crawler/simple/link.text", "a") as f:
                    f.write(path + '\n')
            
    def crawl(self, url):
        html = self.download_url(url)
        self.get_linked_urls(url,html)

    def run(self):
        logging.info(f'Crawling: {url}')
        try:
            self.crawl(url)
        except Exception:
            pass

if __name__ == '__main__':
    count = 1
    while count <= 24:
        url = f'https://thuvienphapluat.vn/bieumau?q=&type=2&field=0,organ0&page={count}'
        count += 1
        Crawler(urls=[url]).run()
