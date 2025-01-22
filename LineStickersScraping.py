import requests
import re
import os
from rich.progress import track

# Custom headers
my_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

def main():
    try:
        url = input('Enter a LINE Sticker Shop product URL: ').strip()
        if not url.startswith('https://store.line.me/stickershop/product/'):
            raise ValueError("Invalid URL format. Please enter a valid LINE Sticker Shop product URL.")
        scrape_stickers(url)
    except Exception as e:
        print(f"Error: {e}")

def scrape_stickers(url):
    try:
        # Send GET request
        response = requests.get(url, headers=my_headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    # Extract sticker pack name
    try:
        pattern_pack_name = r'<title>(.*?)<\/title>'
        match = re.search(pattern_pack_name, response.text)
        if not match:
            raise ValueError("Unable to extract sticker pack name from the page.")
        pack_name = match.group(1).strip()
        pack_name = pack_name.replace(" ", "_")
        pack_name = re.sub(r'_–_.*$', '', pack_name)
    except Exception as e:
        print(f"Error extracting pack name: {e}")
        return

    # Prepare folder for saving images
    try:
        folder_path = f'line_stickers/{pack_name}'
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")
        return

    # Extract sticker links and IDs
    try:
        pattern = r'https?:\/\/stickershop\.line-scdn\.net\/stickershop\/v1\/sticker\/([0-9]+)\/iPhone\/sticker@2x\.png'
        list_line_stickers = []
        for match in re.finditer(pattern, response.text):
            list_line_stickers.append({
                "link": match.group(),
                "id": match.group(1)
            })

        list_first_result = [dict(t) for t in set(tuple(my_dict.items()) for my_dict in list_line_stickers)]
        list_first_result = sorted(list_first_result, key=lambda my_dict: my_dict['id'])
    except Exception as e:
        print(f"Error extracting sticker links: {e}")
        return

    # Skip downloading if folder is already populated
    if os.path.exists(folder_path) and len(os.listdir(folder_path)) > 0:
        print(f"Sticker pack '{pack_name}' already downloaded.")
        return

    # Download stickers
    try:
        print(f"Starting to download stickers pack: {pack_name}")
        for sticker in track(list_first_result, description="Downloading...", total=len(list_first_result)):
            os.system(f"curl -s {sticker['link']} -o {folder_path}/{sticker['id']}.png")
        print("Sticker images downloaded successfully.")
    except Exception as e:
        print(f"Error downloading stickers: {e}")

if __name__ == "__main__":
    main()
