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


from ursina import *


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=0.015),
            texture="white_cube",
            texture_scale=(5, 8),
            scale=(0.5, 0.8),
            origin=(-0.5, 0.5),
            position=(-0.3, 0.4),
            color=color.color(0, 0, 0.1, 0.9),
        )

        for key, value in kwargs.items():
            setattr(self, key, value)

    def find_free_spot(self):
        for y in range(8):
            for x in range(5):
                grid_positions = [
                    (int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                    for e in self.children
                ]
                print(grid_positions)

                if not (x, -y) in grid_positions:
                    print("found free spot:", x, y)
                    return x, y

    def append(self, item, x=0, y=0):
        print("add item:", item)

        if len(self.children) >= 5 * 8:
            print("inventory full")
            error_message = Text(
                "<red>Inventory is full!", origin=(0, -1.5), x=-0.5, scale=2
            )
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = Draggable(
            parent=self,
            model="quad",
            texture=item,
            color=color.white,
            scale_x=1 / self.texture_scale[0],
            scale_y=1 / self.texture_scale[1],
            origin=(-0.5, 0.5),
            x=x * 1 / self.texture_scale[0],
            y=-y * 1 / self.texture_scale[1],
            z=-0.5,
        )
        name = item.replace("_", " ").title()

        if random.random() < 0.25:
            icon.color = color.gold
            name = "<orange>Rare " + name

        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0, 0, 0, 0.8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= 0.01  # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x / 2)) * 5) / 5
            icon.y = int((icon.y - (icon.scale_y / 2)) * 8) / 8
            icon.z += 0.01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = icon.org_pos
                return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print("swap positions")
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop


def main():
    app = Ursina()
    inventory = Inventory()

    def add_item():
        inventory.append(random.choice(("bag", "bow_arrow", "gem", "orb", "sword")))

    add_item()
    add_item()
    add_item_button = Button(
        scale=(0.1, 0.1),
        x=-0.5,
        color=color.lime.tint(-0.25),
        text="+",
        tooltip=Tooltip("Add random item"),
        on_click=add_item,
    )
    bg = Entity(
        parent=camera.ui,
        model="quad",
        texture="shore",
        scale_x=camera.aspect_ratio,
        z=1,
    )
    Cursor(texture="cursor", scale=0.1)
    mouse.visible = False
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    app.run()
