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

import typer

app = typer.Typer()


@app.command()
def inventory():
    from . import inventory

    inventory.main()


@app.command()
def example():
    from . import example

    example.main()


@app.command()
def minecraft():
    from . import minecraft

    minecraft.main()


@app.command()
def platformer():
    from . import platformer

    platformer.main()


@app.command()
def terraria():
    from . import terraria

    terraria.main()


@app.command()
def clicker():
    from . import clicker

    clicker.main()


if __name__ == "__main__":
    app()
