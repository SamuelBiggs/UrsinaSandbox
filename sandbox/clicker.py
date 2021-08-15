# MIT License

# Copyright (c) 2020 Petter Amland

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
clicker game
make a gold counter
make a button
you earn gold for every click
when you have enough gold you can unlock new nodes to automatically generate gold!
"""


from ursina import *

app = Ursina()
window.color = color._20

gold = 0
counter = Text(text="0", y=0.25, z=-1, scale=2, origin=(0, 0), background=True)
button = Button(text="+", color=color.azure, scale=0.125)


def button_click():
    global gold
    gold += 1
    counter.text = str(gold)


button.on_click = button_click


button_2 = Button(cost=10, x=0.2, scale=0.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(
    f"<gold>Gold Generator\n<default>Earn 1 gold every second.\nCosts {button_2.cost} gold."
)


def buy_auto_gold():
    global gold
    if gold >= button_2.cost:
        gold -= button_2.cost
        counter.text = str(gold)
        invoke(auto_generate_gold, 1, 1)


button_2.on_click = buy_auto_gold


def auto_generate_gold(value=1, interval=1):
    global gold
    gold += 1
    counter.text = str(gold)
    button_2.animate_scale(0.125 * 1.1, duration=0.1)
    button_2.animate_scale(0.125, duration=0.1, delay=0.1)
    invoke(auto_generate_gold, value, delay=interval)


def update():
    global gold
    for b in (button_2,):
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.gray


def main():
    app.run()
