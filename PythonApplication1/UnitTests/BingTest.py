import unittest
from unittest.mock import MagicMock
from BingUtil.Bing import BingWebPage
from BingUtil.Bing import bingSearch

class DogTest_Test1(unittest.TestCase):
    def test_bing_homepage_loads(self):
        ''' Full end-to-end homepage download '''
        text = BingWebPage().get_page_text()
        self.assertGreater(len(text), 0, "Bing home page was empty")

    def test_bing_homepage_call_correct(self):
        ''' Test web call without making actual request '''
        bing = BingWebPage()
        self.assertEqual(bing._get_url(), "http://bing.com/", "Incorrect URL")
        self.assertEqual(bing._get_data(), None, "Should be no post data")
        self.assertEqual(bing._get_header("Content-Length"), "81756", "Incorrect encoding header")
        self.assertEqual(bing._get_header("Connection"), "close", "Incorrect encoding header")

    def test_bing_search(self):
        text = bingSearch("python language").get_page_text()
        self.assertGreater(len(text), 0, "Bing search was empty")
        self.assertFalse("doesn't exist" in text, "Bad query format")

if __name__ == '__main__':
    unittest.main()