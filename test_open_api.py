import unittest
import os
import openai

class OpenApiUnitTests(unittest.TestCase):
    
    def test_get_key_from_env(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.assertIsNotNone(api_key) 

    def test_api_call(self):
        openai.organization = "org-7KzzjR00JtLFxMIMgGNWyUJp"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        model_list = openai.Model.list()
        self.assertIsNotNone(model_list) 

if __name__ == "__main__":
    unittest.main()