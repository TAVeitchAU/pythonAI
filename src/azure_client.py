import json
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

class AzureClient:
    def __init__(self, config_path="config.json"):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        endpoint = config.get("azure_endpoint")
        api_key = config.get("azure_api_key")
        model_name = config.get("azure_model_name")

        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )
        self.model_name = model_name  

    def get_response(self, user_message):
        response = self.client.complete(
            stream=True,
            messages=[
                SystemMessage(content="You are a helpful assistant."),
                UserMessage(content=user_message)
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model=self.model_name
        )

        response_content = ""
        for update in response:
            if update.choices:
                response_content += update.choices[0].delta.content or ""
        
        return response_content

    def close(self):
        self.client.close()