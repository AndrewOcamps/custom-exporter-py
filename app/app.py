import requests
from app.load_configuration import get_urls

def get_status_code():
  urls = get_urls()
  url_status_code = []

  for url in urls:
    r = requests.get(url, timeout=30.0)
    status_code = r.status_code
    url_status_code.append({'url': url, 'status': status_code})

  return url_status_code
