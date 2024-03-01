# import gi
# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk

# from langchain_community.llms import Ollama  # Import Ollama here

# class ChatbotWindow(Gtk.Window):
#     def __init__(self):
#         Gtk.Window.__init__(self, title="Conversational Q&A Chatbot")
#         self.set_default_size(400, 200)

#         self.flow_messages = []
#         self.llm = Ollama(base_url="http://172.31.212.37:11434", model="zephyr", temperature=0.8)

#         # UI Elements
#         self.header_label = Gtk.Label(label="Hey, Let's Chat")
#         self.input_entry = Gtk.Entry()
#         self.response_label = Gtk.Label(label="")

#         # Button
#         self.ask_button = Gtk.Button(label="Ask the question")
#         self.ask_button.connect("clicked", self.on_ask_button_clicked)

#         # Layout
#         grid = Gtk.Grid()
#         grid.attach(self.header_label, 0, 0, 2, 1)
#         grid.attach(self.input_entry, 0, 1, 1, 1)
#         grid.attach(self.ask_button, 1, 1, 1, 1)
#         grid.attach(self.response_label, 0, 2, 2, 1)

#         self.add(grid)

#     def on_ask_button_clicked(self, widget):
#         question = self.input_entry.get_text()
#         response = self.get_chatmodel_response(question)

#         # Update UI
#         self.flow_messages.append(f"You: {question}")
#         self.flow_messages.append(f"Bot: {response}")
#         self.update_response_label()

#     def get_chatmodel_response(self, question):
#         try:
#             prompt = " ".join(self.flow_messages)
#             print(f"Request to Ollama: {prompt}")
#             answer = self.llm(prompt)
#             print(f"Response from Ollama: {answer}")
#             self.flow_messages.append(f"Bot: {answer}")
#             return answer
#         except Exception as e:
#             print(f"Error getting response from Ollama: {e}")
#             return "Error: Unable to get response from Ollama"

#     def update_response_label(self):
#         conversation = "\n".join(self.flow_messages)
#         self.response_label.set_text(conversation)


# win = ChatbotWindow()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import requests  # Import requests library

class ChatbotWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Conversational Q&A Chatbot")
        self.set_default_size(400, 200)

        self.flow_messages = []

        # UI Elements
        self.header_label = Gtk.Label(label="Hey, Let's Chat")
        self.input_entry = Gtk.Entry()
        self.response_label = Gtk.Label(label="")

        # Button
        self.ask_button = Gtk.Button(label="Ask the question")
        self.ask_button.connect("clicked", self.on_ask_button_clicked)

        # Layout
        grid = Gtk.Grid()
        grid.attach(self.header_label, 0, 0, 2, 1)
        grid.attach(self.input_entry, 0, 1, 1, 1)
        grid.attach(self.ask_button, 1, 1, 1, 1)
        grid.attach(self.response_label, 0, 2, 2, 1)

        self.add(grid)

    def on_ask_button_clicked(self, widget):
        question = self.input_entry.get_text()
        response = self.get_chatmodel_response(question)

        # Update UI
        self.flow_messages.append(f"You: {question}")
        self.flow_messages.append(f"Bot: {response}")
        self.update_response_label()

    def get_chatmodel_response(self, question):
        try:
            prompt = " ".join(self.flow_messages)
            response = requests.post(
                "http://172.31.212.37:11434",
                json={"text": prompt}
            )

            print(f"Raw Response from Ollama: {response.text}")

            answer = response.json().get("content", "No content in response")
            self.flow_messages.append(f"Bot: {answer}")
            return answer
        except Exception as e:
            print(f"Error getting response from Ollama: {e}")
            return "Error: Unable to get response from Ollama"

    def update_response_label(self):
        conversation = "\n".join(self.flow_messages)
        self.response_label.set_text(conversation)


win = ChatbotWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
