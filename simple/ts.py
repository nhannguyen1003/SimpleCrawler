import logging
from urllib.parse import urljoin
from pathlib import Path
import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            # Navigate to the login page
            await page.goto('https://thuvienphapluat.vn/bieumau?q=&type=2')

            # Interact with the login form
            await page.fill('#usernameTextBox', '0046isk@gmail.com')
            await page.fill('#passwordTextBox', '0046isk@gmail.com')
            await page.click('#loginButton')

            # Wait for the login to complete (adjust the time accordingly)
            await page.wait_for_timeout(5000)

            # Read and process links from the "link.txt" file
            with open("/Users/roy/Documents/Hacker/Crawler/simple/link.text", "r") as file:
                for line in file:
                    url = line.strip()
                    if url:
                        # Navigate to the URL
                        await page.goto(url)
                        try:
                            await page.click('text="Chỉnh sửa và tải về"')
                            async with page.expect_download() as download_info:
                                await page.get_by_role("button", name="In biểu mẫu").click()
                                await page.get_by_role("button", name="Save").click()
                                # Perform the action that initiates download
                                download = await download_info.value
                                # Wait for the download process to complete and save the downloaded file somewhere
                                if download:
                                    download_path = "/Users/roy/Documents/Hacker/Crawler/output/"
                                    filename = download.suggested_filename
                                    await download.save_as(os.path.join(download_path, filename))
                                    print(f"Downloaded: {filename}")

                        except Exception as e:
                            print(f"Error while downloading: {str(e)}")

        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
