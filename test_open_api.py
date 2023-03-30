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

        """_summary_
        openai translate
        English to other languages
        https://platform.openai.com/examples/default-translate
        """
    def test_api_translation_call(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1.",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        ) 
        self.assertIsNotNone(response['choices']) 
        # return 1 line text answer
        self.assertIsNotNone(response['choices'][0]['text']) 
        #split text into 3 answers
        list_answers= response['choices'][0]['text'].split('\n')
        french = list_answers[0] 
        spanish = list_answers[1] 
        japanese = list_answers[2] 
        self.assertIsNotNone(french) 
        self.assertIsNotNone(spanish) 
        self.assertIsNotNone(japanese) 
        self.assertTrue(french in response['choices'][0]['text']) 

if __name__ == "__main__":
    unittest.main()