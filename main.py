
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ProfitCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="💰 أدخل مبلغ الاستثمار بالدينار:", font_size=18))

        self.input = TextInput(multiline=False, input_filter='float', font_size=18)
        self.add_widget(self.input)

        self.button = Button(text="احسب الأرباح", font_size=20, background_color=(0.2, 0.6, 1, 1))
        self.button.bind(on_press=self.calculate_profit)
        self.add_widget(self.button)

        self.result = Label(text="", font_size=18)
        self.add_widget(self.result)

    def calculate_profit(self, instance):
        try:
            amount = float(self.input.text)
            monthly_rate = 99000 / 742000
            monthly_profit = amount * monthly_rate
            daily_profit = monthly_profit / 30
            yearly_profit = monthly_profit * 12
            months_to_return = amount / monthly_profit

            result_text = (
                f"\n📅 الربح اليومي: {daily_profit:.2f} د.ع\n"
                f"🗓️ الربح الشهري: {monthly_profit:.2f} د.ع\n"
                f"📈 الربح السنوي: {yearly_profit:.2f} د.ع\n"
                f"⏳ مدة استرجاع رأس المال: {months_to_return:.2f} شهر"
            )
            self.result.text = result_text

        except ValueError:
            self.result.text = "⚠️ أدخل رقمًا صالحًا."


class ProfitApp(App):
    def build(self):
        return ProfitCalculator()


if __name__ == '__main__':
    ProfitApp().run()
