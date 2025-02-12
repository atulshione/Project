from tkinter import *
from chat import get_response, bot_name
# import pyttsx3 as pp
# import speech_recognition as sr
# import threading

BG_GRAY = "grey"
BG_COLOR = "black"
TEXT_COLOUR = "white" 

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        # self.engine = pp.init()
        # self.voices = self.engine.getProperty('voices')
        # self.engine.setProperty('voice',self.voices[1].id)

    # def speak(self,word):
    #     self.engine.say(word)
    #     self.engine.runAndWait()
    
    # def takeQuery(self):
    #     self.speech=sr.Recognizer()
    #     self.speech.pause_threshold =1
    #     print("your bot is listening try to speak")
    #     with sr.Microphone() as m:
    #         try:
    #             audio = self.speech.listen(m)
    #             query = self.speech.recognize_google(audio, language='eng-in')
    #             self.msg_entry.delete(0, END)
    #             self.msg_entry.insert(0,query)
    #             self._insert_message(query, "You")
    #         except Exception as e:
    #             print(e)
    #             print("Not Recognised")


    def run(self):
        # t = threading.Thread(target=self.repeatL)
        # t.start()
        self.window.mainloop()

    # def repeatL(self):
    #         while True:
    #             self.takeQuery()

    def _setup_main_window(self):
        self.window.title("ZenQuotient")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=800, height=950, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOUR,
                            text="Welcome to ZenQuotient", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOUR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.015, relheight=0.05, relwidth=0.1)
        exit_button = Button(bottom_label, text="Exit", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=self.window.destroy)
        exit_button.place(relx=0.90, rely=0.015, relheight=0.05, relwidth=0.1)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        # self.speak(get_response(msg))
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
