import unittest
from src.scraper.website import Website

class TestWebsite(unittest.TestCase):
    
    def test_website_initialization(self):
        website = Website("https://example.com")
        self.assertIsNotNone(website.url)
        self.assertIsNotNone(website.title)
    
    def test_get_contents(self):
        website = Website("https://example.com")
        contents = website.get_contents()
        self.assertIn("Webpage Title", contents)
        self.assertIn("Webpage Contents", contents)

if __name__ == '__main__':
    unittest.main()