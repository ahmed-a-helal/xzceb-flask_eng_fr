from .. import translator
import unittest

TestCases = [["How are you?","Comment es-tu?"],
    ["Hello", "Bonjour"],
    ["I read this book","J'ai lu ce livre"],
    ["It's Life","C'est la vie"]]

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        for TestCase in TestCases:
            self.assertEqual(translator.english_to_french(TestCase[0]),TestCase[1])

    def testNull(self):
        self.assertEqual(translator.english_to_french(""),"please input text to translate")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        for TestCase in TestCases:
            self.assertEqual(translator.french_to_english(TestCase[1]),TestCase[0])

    def testNull(self):
        self.assertEqual(translator.french_to_english(""),"please input text to translate")

if __name__ == "__main__":
    unittest.main()
