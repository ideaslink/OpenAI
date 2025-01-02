"""
image gen hub using openai api

"""

import os
import requests

import openai
from openai import AzureOpenAI
import json
import shared.var_def as VAR


class ImageGenHub:
    """
    image gen using openai models
    """

    def __init__(self):
        pass


    def image_generating(self, model: str, version: str, input: str, count: int, size: str, imgpath: str) -> str:
        result = "error"
        try:
            client = AzureOpenAI(
                azure_endpoint=os.getenv(VAR.ENDPOINT).rstrip("/"),
                api_key=os.getenv(VAR.APIKEY),
                api_version=version
            )

            print(f"endpoint: {os.getenv(VAR.ENDPOINT)}, key: {os.getenv(VAR.APIKEY)}")

            result = client.images.generate(model=model, prompt=input, n=count, size="1024x1024")
            json_resp = json.loads(result.model_dump_json())

            image_url = json_resp["data"][0]["url"]
            image_gen = requests.get(image_url).content

            # save image
            with open(imgpath, "wb") as f:
                f.write(image_gen)

            return image_url

        except Exception as e:
            print(e)
            return f"Error: {e}"
    pass
