from urllib.parse import urljoin

BASE = "https://en.wikipedia.org"

def parse_links(soup):
    links = []
    # TODO: Find all <a> tags and extract href
    # TODO: Only keep internal links that start with "/wiki/" and do not contain ":"
    # TODO: Use urljoin to resolve full URL

    return links

def extract_info(url, soup):
    # TODO: Extract <title> tag text (if exists)
    # TODO: Call parse_links() to get valid internal links
    # TODO: Return both the page info dict and the link list
    return {}, []
