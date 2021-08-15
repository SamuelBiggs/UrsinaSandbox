import typer

app = typer.Typer()

@app.command()
def start():
    print("boo")

if __name__ == "__main__":
    app()