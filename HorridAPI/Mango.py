import requests
from models import hehmango

class Mangoo:
    """
    A class to generate content using AI models.
    """

    def __init__(self, base_url="https://horridapi.onrender.com/mango"):
        """
        Initialize the class with the base URL of the API.

        Args:
            base_url (str, optional): The base URL of the API. Defaults to "https://horridapi.onrender.com/mango".
        """
        self.base_url = base_url
        self.models = hehmango       

    def seed(self, prompt, model):
        """
        Generate content using the specified AI model.

        Args:
            query (str): The query to generate content for.
            model (str): The AI model to use ("https://horridapi.onrender.com/mango").

        Returns:
            dict or str: The generated content as a dictionary if the response is successful, otherwise the error message as a string.
        """
        if model not in self.models:
            return "Invalid model. You Can Get model here https://horridapi.onrender.com/mango."

        url = f"{self.base_url}?model={self.models[model]}"
        response = requests.post(url, json=prompt)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    
Mango = Mangoo()
