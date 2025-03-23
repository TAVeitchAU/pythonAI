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

    def analyze_image(self, image_path):
        with open(image_path, 'rb') as image_stream:
            description_results = self.client.describe_image_in_stream(image_stream)

        if len(description_results.captions) == 0:
            return "No description detected."
        else:
            return ' '.join([caption.text for caption in description_results.captions])

    def close(self):
        pass  # No explicit close method for ComputerVisionClient