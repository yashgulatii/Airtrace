import argparse
import json
from src.scanner import scan_networks
from src.utils import display_loop, display_table
from src.banner import print_banner
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Airtrace – Wi-Fi Signal Scanner")
    parser.add_argument(
        "-s", "--sort", action="store_true",
        help="Sort by signal strength"
    )
    parser.add_argument(
        "-c", "--color", action="store_true",
        help="Color-code signal strength"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output scan results as JSON"
    )
    parser.add_argument(
        "-l", "--loop", type=int,
        help="Loop scan every X seconds (until Ctrl+C)"
    )

    args = parser.parse_args()

    try:
        print_banner()
        if args.loop:
            display_loop(scan_networks, interval=args.loop, sort=args.sort, color=args.color)
        else:
            networks = scan_networks()
            if args.json:
                print(json.dumps(networks, indent=4))
            else:
                console.print(display_table(networks, sort=args.sort, color=args.color))
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting Airtrace. Goodbye![/]")
