import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FOLDER = Path("book_images")

OUTPUT_FOLDER.mkdir(exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

total = 0

for page_number in range(1, 51):

    if page_number == 1:
        page_url = BASE_URL
    else:
        page_url = f"{BASE_URL}catalogue/page-{page_number}.html"

    print(f"\nScraping page {page_number}/50...")

    response = requests.get(
        page_url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:

        image = book.select_one("img")

        if image is None:
            continue

        image_url = urljoin(page_url, image.get("src"))

        image_response = requests.get(
            image_url,
            headers=headers,
            timeout=20
        )

        image_response.raise_for_status()

        total += 1

        file_path = OUTPUT_FOLDER / f"book_{total}.jpg"

        with open(file_path, "wb") as file:
            file.write(image_response.content)

        print(f"Downloaded: {total}")

print("\n==============================")
print("SCRAPING COMPLETE!")
print("==============================")
print(f"Total images: {total}")
print(f"Saved in: {OUTPUT_FOLDER}")