import unittest
from text_formatter import formatter

class TestFormatter(unittest.TestCase):
    def test_if_string_is_empty(self):
        string = ""
        char = 40
        justified = True
        result = formatter(string, char)

        self.assertEqual(result, "\nErro nos valores! Confira se seus Inputs estão corretos!")
    
    def test_if_char_value_is_zero(self):
        string = "wubbalubdubdub"
        char = 0
        justified = True
        result = formatter(string, char)

        self.assertEqual(result, "\nErro nos valores! Confira se seus Inputs estão corretos!")

    def test_if_chat_value_is_not_negative(self):
        string = "Oh Geez..."
        char = -1
        justified = True
        result = formatter(string, char)

        self.assertEqual(result, "\nErro nos valores! Confira se seus Inputs estão corretos!")

if __name__ == '__main__':
    unittest.main()