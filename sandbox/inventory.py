# Copyright (C) 2021 Samuel Biggs

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ursina


class Inventory(ursina.Entity):
    def __init__(self):
        super().__init__(
            parent=ursina.camera.ui,
            model="quad",
            scale=(0.5, 0.8),
            origin=(-0.5, 0.5),
            position=(-0.3, 0.4),
            texture="white_cube",
            texture_scale=(5, 8),
            color=ursina.color.dark_gray,
        )

        self.item_parent = ursina.Entity(parent=self, scale=(1 / 5, 1 / 8))

    def find_free_spot(self):
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for y in range(8):
            for x in range(5):
                if not (x, -y) in taken_spots:
                    return (x, -y)

    def append(self, item):
        ursina.Button(
            parent=self.item_parent,
            model="quad",
            origin=(-0.5, 0.5),
            color=ursina.color.random_color(),
            position=self.find_free_spot(),
            z=-0.1,
        )


def run():
    app = ursina.Ursina()
    inventory = Inventory()
    for _ in range(7):
        inventory.append("test item")

    app.run()
