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

        endpoint = "https://f5aivision.cognitiveservices.azure.com/"
        api_key = "FByM1jjbJD28ykMClaxV4Y03zfKU7YSPZzII4ooo7sHmBWnJQlbOJQQJ99BCACYeBjFXJ3w3AAAFACOG4qcU"
        self.azure_client = AzureClient(endpoint, api_key)

    def get_response(self):
        user_input = self.entry.get()
        self.entry.delete(0, END)
        response = self.azure_client.get_response(user_input)
        self.response_text.insert(END, response + "\n")

    def upload_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if image_path:
            response = self.azure_client.analyze_image(image_path)
            self.response_text.insert(END, response + "\n")

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()