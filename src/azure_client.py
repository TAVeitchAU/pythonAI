from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import io
import os

class AzureClient:
    def __init__(self, endpoint, api_key, model_name=None):
        self.client = ComputerVisionClient(
            endpoint,
            CognitiveServicesCredentials(api_key)
        )

    def analyze_image(self, image_path, question=None):
        with open(image_path, 'rb') as image_stream:
            description_results = self.client.describe_image_in_stream(image_stream)

        if len(description_results.captions) == 0:
            description = "No description detected."
        else:
            description = ' '.join([caption.text for caption in description_results.captions])

        if question:
            # Here you can extend the functionality to process the question along with the image description
            # For simplicity, let's assume we concatenate the description with the question
            response = f"Description: {description}\nQuestion: {question}"
        else:
            response = description

        return response

    def close(self):
        pass  # No explicit close method for ComputerVisionClient