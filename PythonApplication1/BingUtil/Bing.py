from urllib.request import urlopen

class BingWebPage:
    def __init__(self, url="", data=None):
        self.url = "http://bing.com/" + url
        self.data = data

    def get_page_text(self):
        with urlopen(self._get_url(), self._get_data()) as reader:
            return str(reader.read())

    def get_all_links(self):
        finder = BingLinkFinder()
        return finder.get_ad_links() + finder.get_search_result_links()

    def _get_url(self):
        return self.url

    def _get_data(self):
        return self.data

    def _get_header(self, name):
        with urlopen(self._get_url(), self._get_data()) as reader:
            return reader.getheader(name)

def bingSearch(searchString: 'str') -> 'BingWebPage':
    urlArg = "search?q=%s" % searchString.replace(" ", "+")
    return BingWebPage(urlArg)

class BingLinkFinder:
    def get_ad_links(self):
        raise Exception("NYI")

    def get_search_result_links(self):
        raise Exception("NYI")