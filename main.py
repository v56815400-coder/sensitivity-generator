from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SensitivityApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=20, spacing=12)

        root.add_widget(Label(text="Sensitivity Generator", font_size=24,
                              size_hint_y=None, height=55))

        root.add_widget(Label(text="Phone RAM (GB)", size_hint_y=None, height=30))
        self.ram = TextInput(hint_text="Example: 6", input_filter="int",
                             multiline=False, halign="center",
                             size_hint_y=None, height=45)
        root.add_widget(self.ram)

        root.add_widget(Label(text="Refresh Rate (Hz)", size_hint_y=None, height=30))
        self.hz = TextInput(hint_text="Example: 90", input_filter="int",
                            multiline=False, halign="center",
                            size_hint_y=None, height=45)
        root.add_widget(self.hz)

        btn = Button(text="GENERATE SENSITIVITY",
                     size_hint_y=None, height=55)
        btn.bind(on_press=self.calculate)
        root.add_widget(btn)

        self.result = Label(text="Enter your phone details above.",
                            halign="center", valign="middle")
        self.result.bind(size=self.result.setter("text_size"))
        root.add_widget(self.result)

        return root

    def calculate(self, *_):
        try:
            ram = int(self.ram.text)
            hz = int(self.hz.text)

            if ram >= 8 and hz >= 90:
                values = (90, 85, 80, 75, 50)
            elif ram >= 6 or hz >= 90:
                values = (95, 90, 85, 80, 55)
            else:
                values = (100, 95, 90, 85, 60)

            g, rd, s2, s4, awm = values
            self.result.text = (
                "Custom Sensitivity\n\n"
                f"General: {g}\n"
                f"Red Dot: {rd}\n"
                f"2x Scope: {s2}\n"
                f"4x Scope: {s4}\n"
                f"AWM Scope: {awm}"
            )
        except ValueError:
            self.result.text = "Please enter valid RAM and Hz numbers."

if __name__ == "__main__":
    SensitivityApp().run()
