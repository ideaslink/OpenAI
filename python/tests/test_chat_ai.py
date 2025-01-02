"""
test for chat ai code

"""

import unittest
from chat_ai import openai_chat_hub


class TestChatAI(unittest.TestCase):
    """
    Unit test for Chat AI using OpenAI
    """

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.chat_obj = openai_chat_hub.ChatCompletionHub()

    def test_chat_ai_completion(self):
        system_message = "You are a helpful AI assistant"
        message = "what can you infer from 'Shakespeare in AI'? (Max: 300 words)"
        # "what can you infer from 'Shakespeare in AI'? (Max: 300 words)"

        # === gpt-4o-mini
        deploy_name = "gpt-4o-mini"
        version = "2024-10-01-preview"  # "2024-07-18"

        # === gpt-35-turbo
        # deploy_name = "gpt-35-turbo"
        # version = "0301"  # "2023-03-15-preview"

        result = self.chat_obj.chat_completion(model=deploy_name,version=version,system_message=system_message,input=message)
        print(result)
        self.assertTrue(not result.__contains__("error") and len(result) > 1)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
