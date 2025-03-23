from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END
from azure_client import AzureClient

def create_ui():
    root = Tk()
    root.title("Azure AI Query Interface")

    Label(root, text="Enter your question:").pack(pady=10)

    user_input = Entry(root, width=50)
    user_input.pack(pady=5)

    response_area = Text(root, height=15, width=60)
    response_area.pack(pady=10)

    scrollbar = Scrollbar(root, command=response_area.yview)
    scrollbar.pack(side='right', fill='y')
    response_area.config(yscrollcommand=scrollbar.set)

    def get_response():
        query = user_input.get()
        if query:
            client = AzureClient()
            response = client.get_response(query)
            response_area.delete(1.0, END)
            response_area.insert(END, response)

    Button(root, text="Submit", command=get_response).pack(pady=10)

    root.mainloop()