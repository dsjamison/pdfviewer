import os
import requests
import pdfkit
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
# urllib.disable_warnings(urllib.exceptions.InsecureRequestWarning)

# Function to get all subpage links from the main URL
def get_all_links(base_url):
    visited = set()
    to_visit = {base_url}

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            parsed_url = urlparse(full_url)

            # Ensure we stay within the same domain
            if parsed_url.netloc == urlparse(base_url).netloc:
                to_visit.add(full_url)

    return visited

# Function to convert a webpage to PDF
def save_page_as_pdf(url, output_folder):
    try:
        response = requests.get(url, timeout=5, verify=False)
        response.raise_for_status()
        html_content = response.text

        filename = os.path.join(output_folder, f"{urlparse(url).path.strip('/').replace('/', '_') or 'index'}.pdf")
        pdfkit.from_string(html_content, filename)
        print(f"Saved {url} as {filename}")
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Main function
def save_website_as_pdf(base_url, output_folder="pdf_output"):
    os.makedirs(output_folder, exist_ok=True)
    links = get_all_links(base_url)

    for link in links:
        save_page_as_pdf(link, output_folder)

# Entry point
def main():
    base_url = input("Enter the website URL: ").strip()
    if not base_url.startswith("http"):
        base_url = "https://" + base_url  # Ensure valid URL format

    output_folder = "pdf_output"
    save_website_as_pdf(base_url, output_folder)
    print(f"All pages saved in {output_folder}/")

if __name__ == "__main__":
    main()
