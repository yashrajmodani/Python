from urllib.parse import urlparse, parse_qs


urls = [
    'https://www.example.com/path/to/page?name=John&age=30',
    'http://another-example.org/test?param=value',
    'https://subdomain.website.com/section/item?id=123&category=books'
    'https://www.example.com/path/to/page?name=John&age=30',
    'http://another-example.org/test?param=value',
    'https://subdomain.website.com/section/item?id=123&category=books'
    'https://www.example.com/path/to/page?name=John&age=30',
    'http://another-example.org/test?param=value',
    'https://subdomain.website.com/section/item?id=123&category=books'
]

url_components = []

# Parse each URL
for url in urls:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)  # Get query as a dictionary
    components = {
        'url': url,
        'domain': parsed_url.netloc,
        'path': parsed_url.path,
        'query': query_params
    }
    url_components.append(components)

# Print the components
for component in url_components:
    print(component)


