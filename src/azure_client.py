class AzureClient:

    def __init__(self, endpoint, api_key, model_name):
        from azure.ai.inference import ChatCompletionsClient
        from azure.core.credentials import AzureKeyCredential
        
        self.client = ChatCompletionsClient(
            endpoint="https://ai-tomveitch3489ai260312779439.openai.azure.com/openai/deployments/gpt-4o",
            credential=AzureKeyCredential("1syRx28AXs1jDIi1gsIVfRPxvTBwORU6E0qkfGg3hGq7m5bs3k6wJQQJ99AKACYeBjFXJ3w3AAAAACOGkvdp")
        )
        self.model_name = "gpt-4o"  

    def get_response(self, user_message):
        from azure.ai.inference.models import SystemMessage, UserMessage
        
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