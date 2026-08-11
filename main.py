from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MenuApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )
        title = Label(
            text="Viikon ruokalista",
            font_size=28
        )
        layout.add_widget(title)
        food_label = Label(
            text="Valitse päivä",
            font_size=20
        )
        layout.add_widget(food_label)
        days = [
            ("MA", "POSSUKASTIKE L\nPERUNA\nSALAATTEJA"),
            ("TI", "JAUHELIHAKEITTO G,M /\nKASVISKEITTO L,G\nJÄÄSALAATTI KURKKU\nJUUSTOVIIPALE L\nMARJARAHKA L"),
            ("KE", "BROILERIPASTAVUOKA L\nSALAATTEJA\nKASVISPASTAVUOKA M\nPA-KASVIS G,M"),
            ("TO", "APPELSIINIKALA L\nPERUNA\nSALAATTEJA"),
            ("PE", "PYTTIPANNU G,M /\nKASVISPYTTÄRI M,G\nKANANMUNA\nSALAATTEJA")
        ]
        for day, food in days:
            button = Button(
                text=day,
                font_size=20
            )
            button.bind(
                on_press=lambda instance, food=food:
                self.show_food(food, food_label)
            )
            layout.add_widget(button)
        return layout

    def show_food(self, food, label):
        label.text = food


MenuApp().run()
