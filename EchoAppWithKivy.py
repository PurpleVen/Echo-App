from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class EchoApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        #add widgets to window

        #Image
        self.window.add_widget(Image(source="repeat.png"))

        #Label
        self.greeting = Label(
                        text="What do you want to say?",
                        font_size = 20,
                        color = '#FBF1CF')
        self.window.add_widget(self.greeting)

        #userinput
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20, 20),
                    size_hint = (1, 0.5))
        self.window.add_widget(self.user)

        #button
        self.button = Button(
                      text="Repeat the user input",
                      size_hint= (1, 0.5),
                      font_size = 18,
                      bold = True,
                      background_color = '#E7889D',
                      background_normal="")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "You said : " +self.user.text





if __name__ == "__main__":
    EchoApp().run()