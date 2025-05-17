from urllib.parse import urlparse

def should_visit(url, visited, domain):
    # TODO: Skip if already visited
    # TODO: Use urlparse() to check:
    #   - same domain
    #   - path starts with /wiki/
    #   - path does NOT contain ":"
    return False
