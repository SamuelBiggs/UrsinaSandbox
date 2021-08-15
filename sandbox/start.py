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
import ursina.prefabs.first_person_controller


class Voxel(ursina.Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=ursina.scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="white_cube",
            color=ursina.color.color(0, 0, ursina.random.uniform(0.9, 1.0)),
            highlight_color=ursina.color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                Voxel(position=self.position + ursina.mouse.normal)

            if key == "right mouse down":
                ursina.destroy(self)


def main():
    app = ursina.Ursina()
    ursina.Sky()

    for z in range(-20, 20):
        for x in range(-20, 20):
            Voxel(position=(x, 0, z))

    ursina.prefabs.first_person_controller.FirstPersonController()

    app.run()
