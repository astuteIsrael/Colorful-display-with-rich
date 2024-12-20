# pip install rich


from rich.console import Console

console = Console()

message = "Welcome back [bold magenta]Israel lol, !!!shipd toke you away[/bold magenta]"
style = "bold red on white"

console.print(message, style=style)