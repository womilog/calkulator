from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Window.size = (400, 500)
Config.set("kivy", "keyboard_mode", "systemanddock")

Builder.load_string('''

<MyBoxLayout@BoxLayout>
    orientation: "vertical"
    
    
<MyOwnButton@Button>
    font_size: "25sp"
    haling: "middle"
    yaling: "middle"

<Container>:
    orientation: "vertical"
    rows: 3
    result_label: result_label
    one: one
    two: two
    three: three
    four: four
    five: five
    six: six
    seven: seven
    eight: eight
    nine: nine
    dot: dot
    mult: mult
    truediv: truediv
    add: add
    sub: sub

    BoxLayout:
        size_hint: 1, 0.16

        Label:
            text: ""
            id : result_label
            font_size: "45sp"
            input_filter: "float"
            input_type: "number"
            multiline: False

    GridLayout:
        cols: 4

        MyBoxLayout:

            MyOwnButton:
                text: "7"
                id : seven
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "4"
                id : four
                on_release: root.add_number(self.text)
                
            MyOwnButton:
                text: "1"
                id : one
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "0"
                id : zero
                on_release: root.add_number(self.text)
                
        MyBoxLayout:

            MyOwnButton:
                text: "8"
                id : eight
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "5"
                id : five
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "2"
                id : two
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "."
                id : dot
                on_release: root.add_number(self.text)
                
        MyBoxLayout:

            MyOwnButton:
                text: "9"
                id : nine
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "6"
                id : six
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "3"
                id : three
                on_release: root.add_number(self.text)

            MyOwnButton:
                text: "AC"
                id : AC
                on_release: root.clear()
                
        MyBoxLayout:

            MyOwnButton:
                text: "*"
                id : mult
                on_release: root.operation(self.text)

            MyOwnButton:
                text: "/"
                id : truediv
                on_release: root.operation(self.text)

            MyOwnButton:
                text: "-"
                id : sub
                on_release: root.operation(self.text)

            MyOwnButton:
                text: "+"
                id : add
                on_release: root.operation(self.text)
                

    BoxLayout:
        size_hint: 1, 0.16

        Button:
            id : equal
            text: "="
            font_size: "25sp"
            size_hint: 1, 1
            pos_hint: {"cenrter_x": 0.5, "center_y": 0.5}
            on_release:
                root.culculate()

''')


class Container(BoxLayout):
    def __init__(self, **kwargs):
        self.current_number = ""
        self.operands = "+-*/"
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        super().__init__(**kwargs)

    def add_number(self, number):
        if self.current_number == "0":
            if number in self.numbers:
                return

        if number == ".":
            if self.ids.result_label.text.count(".") == 1 or self.current_number == "":
                return

        self.current_number += number
        if any(list(map(lambda x: x in self.operands, self.current_number))):
            last_indx_oper = [i for i in range(len(self.current_number)) if self.current_number[i] in self.operands]
            self.ids.result_label.text = self.current_number.split(self.current_number[last_indx_oper[-1]])[-1]
            return

        self.ids.result_label.text = self.current_number

    def clear(self):
        self.current_number = ""
        self.ids.result_label.text = self.current_number

    def operation(self, operand):
        self.current_number += operand
        self.ids.result_label.text = ""

    def culculate(self):
        try:
            self.current_number = str(eval(self.current_number)) \
                if len(str(eval(self.current_number)).split(".")[-1]) < 8 else str(round(eval(self.current_number), 7))
            self.ids.result_label.text = self.current_number
        except ZeroDivisionError:
            self.current_number = ""
            self.ids.result_label.text = "Сan't divide by zero"
        except Exception:
            self.current_number = ""
            self.ids.result_label.text = "Error"


class DuckyApp(App):
    def __init__(self, **kwargs):
        self.title = "Calkulate"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    DuckyApp().run()