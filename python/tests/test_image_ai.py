"""
test for image gen code

"""
import os.path
import unittest
from chat_ai import image_gen_hub
from PIL import Image


class TestChatAI(unittest.TestCase):
    """
    Unit test for Image AI using OpenAI
    """

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.image_obj = image_gen_hub.ImageGenHub()
        self.image_name = "gen_by_openai.png"

    def test_image_gen_ai(self):
        message = "a tropical beach with palm trees and girls"
        # "what can you infer from 'Shakespeare in AI'? (Max: 300 words)"

        # === gpt-4o-mini
        deploy_name = "dall-e-3"
        version = "2024-02-01"  # "2024-07-18"

        img_path = os.path.join("../assets", self.image_name)

        result = self.image_obj.image_generating(model=deploy_name,version=version,input=message, imgpath=img_path, count=1, size="1024x1024")
        print(f"result: {result}")

        image = Image.open(img_path)
        image.show()

        self.assertTrue(not result.__contains__("error") and len(result) > 1)

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()