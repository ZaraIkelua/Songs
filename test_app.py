import unittest
from app import app
from bs4 import BeautifulSoup


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_index_contains_text(self):
        # Sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Example: Check if a specific text is present in a paragraph
        paragraphs = soup.find_all('p')
        self.assertTrue(any("My Bloody Valentine |" in p.text for p in paragraphs), "The specific text was not found in any <p> tags")
        

    def test_albums_of_Bloddy_Valentine(self):
        # Sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/show/4')

        soup = BeautifulSoup(response.data, 'html.parser')

        # Example: Check if a specific text is present in a paragraph
        paragraphs = soup.find_all('p')
        self.assertTrue(any("In the Court of the Crimson King | 4 | 10-Oct-69 | 4.3 | 41988 | 842 | Progressive Rock, Art Rock" in p.text for p in paragraphs), "The specific text was not found in any <p> tags")
    
if __name__ == '__main__':
    unittest.main()
