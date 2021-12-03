import unittest
from translator import french_to_english,english_to_french

class TestTranslations(unittest.TestCase):

    def test_null_english_to_french(self):
        with self.assertRaises(Exception):
            english_to_french(None)

    def test_null_french_to_english(self):
        with self.assertRaises(Exception):
            french_to_english(None)

    def test_hello_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_bonjour_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
