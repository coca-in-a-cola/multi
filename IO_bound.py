import concurrent.futures
from urllib.request import Request, urlopen
from urllib.parse import unquote

urls = open('res.txt', encoding='utf8').read().split('\n')


def check_url(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    response = urlopen(request, timeout=5)
    return response


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(check_url, url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            print(future.result().code)
        except Exception as e:
            print(url, e)
