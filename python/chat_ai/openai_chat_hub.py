"""
chat hub using openai api

"""

import os

#import openai
from openai import AzureOpenAI
import python.shared.var_def as VAR


class ChatCompletionHub:
    """
    chat completion using openai models
    """

    def chat_completion(self, model: str, version: str, system_message: str, input: str) -> str:
        result = "error"
        try:
            client = AzureOpenAI(
                azure_endpoint=os.getenv(VAR.ENDPOINT).rstrip("/"),
                api_key=os.getenv(VAR.APIKEY),
                api_version=version
            )

            print(f"apikey: {os.getenv(VAR.APIKEY)}, endpoint: {os.getenv(VAR.ENDPOINT)}")
            message = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": input}
            ]
            # message = [
            #     {"role": "system", "content": "You are a helpful assistant."},
            #     {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
            #     {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
            #     {"role": "user", "content": "Do other Azure AI services support this too?"}
            # ]

            response = client.chat.completions.create(model=model, messages=message)
            print(response)
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            return f"Error: {e}"



