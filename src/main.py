from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END, filedialog
from azure_client import AzureClient

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Azure AI Query Application")

        self.label = Label(master, text="Enter your question:")
        self.label.pack()

        self.entry = Entry(master, width=50)
        self.entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.get_response)
        self.submit_button.pack()

        self.upload_button = Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.response_text = Text(master, wrap='word', height=15, width=50)
        self.response_text.pack()

        self.scrollbar = Scrollbar(master, command=self.response_text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.response_text['yscrollcommand'] = self.scrollbar.set

        endpoint = "https://ai-tomveitch3489ai260312779439.openai.azure.com/openai/deployments/gpt-4o"
        api_key = "1syRx28AXs1jDIi1gsIVfRPxvTBwORU6E0qkfGg3hGq7m5bs3k6wJQQJ99AKACYeBjFXJ3w3AAAAACOGkvdp"
        model_name = "gpt-4o"
        self.azure_client = AzureClient(endpoint, api_key, model_name)

    def get_response(self):
        user_input = self.entry.get()
        self.entry.delete(0, END)
        response = self.azure_client.get_response(user_input)
        self.response_text.insert(END, response + "\n")

    def upload_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if image_path:
            response = self.azure_client.process_image(image_path)
            self.response_text.insert(END, response + "\n")

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()