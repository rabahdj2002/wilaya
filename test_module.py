import unittest
import wilaya

class TestSearch(unittest.TestCase):
    def test_searchByCode(self):
        """
        Test the searchByCode method of Search.
        """
        obj = wilaya.handler()
        self.assertEqual(obj.searchByCode(code=25)['name'], "Constantine")
    
    def test_searchByName(self):
        """
        Test the searchByName method of Search.
        """
        obj = wilaya.handler()
        self.assertEqual(obj.searchByName(name="Naama")['code'], '45')

if __name__ == '__main__':
    unittest.main()