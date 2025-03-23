# Windows Application for Azure AI Interaction

This project is a simple Windows application that allows users to interact with the Azure AI service by typing in questions and receiving responses.

## Project Structure

```
windows-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── azure_client.py  # Azure AI service interaction
│   └── ui.py           # User interface components
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd windows-app
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then, run:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Run the application:
   ```
   python src/main.py
   ```

2. Enter your question in the input field and press the submit button to receive a response from the Azure AI service.

## Dependencies

This project requires the following Python packages:
- Azure SDK for Python
- GUI framework (e.g., Tkinter or PyQt)

Make sure to check `requirements.txt` for the complete list of dependencies.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.