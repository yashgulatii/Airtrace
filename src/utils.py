from rich.console import Console
from rich.table import Table
from rich.live import Live
from operator import itemgetter
import json

console = Console()

def display_table(networks, sort=False, color=False):
    if sort:
        networks.sort(key=itemgetter("Signal"), reverse=True)

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("No.", width=5)
    table.add_column("SSID", style="bold magenta")
    table.add_column("Signal", justify="right")

    for idx, net in enumerate(networks, 1):
        signal = f"{net['Signal']}%"
        if color:
            signal = f"[green]{signal}[/]" if net['Signal'] > 75 else \
                     f"[yellow]{signal}[/]" if net['Signal'] > 40 else \
                     f"[red]{signal}[/]"
        table.add_row(str(idx), net['SSID'], signal)

    return table

def display_loop(networks_fetcher, interval=5, sort=False, color=False):
    with Live(console=console, refresh_per_second=1) as live:
        try:
            while True:
                networks = networks_fetcher()
                table = display_table(networks, sort=sort, color=color)
                live.update(table)
                import time
                time.sleep(interval)
        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting Airtrace.[/]")
