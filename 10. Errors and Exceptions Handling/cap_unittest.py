import unittest
import cap

class TestCap(unittest.TestCase):

    def test_a_word(self):
        text = 'texttobetested'
        result = cap.captext(text)
        self.assertEqual(result,'Texttobetested')

    def test_words(self):
        text = 'text to be tested'
        result = cap.captext(text)
        self.assertEqual(result,'Text to be tested') 

if __name__ == '__main__':
    unittest.main()
