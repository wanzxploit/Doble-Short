import os
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress
import subprocess

console = Console()

class ShortLinkGenerator:
    def __init__(self):
        self.api_keys = {
            "Bitly": "b39549e89f08923d7faef0b53e65d77cff589410",
            "TinyURL": "RbcrFbz7N6T67JdGeUVBMbrYylHDQYXyyrDK4mMefuYp0mHccX9gFX7WEEHw",
            "Cutt.ly": "81eb1f7c58a3542ad2132cb05b1dfa55cd00a"
        }
        self.servers = list(self.api_keys.keys())

    def _banner(self):
        """Display a modern banner using Rich and figlet"""
        figlet_banner = subprocess.getoutput("figlet -f slant -w 80 'Shortener'")
        banner_text = f"[bold blue]{figlet_banner}[/bold blue]"
        console.print(banner_text)
        table = Table(title="[bold cyan]Doble Short Tools[/bold cyan]", expand=False, border_style="bold blue")
        table.add_column("Platform", style="blue", justify="left")
        table.add_column("Username / Link", style="cyan", justify="left")
        table.add_row("GitHub", "https://github.com/wanzxploit")
        table.add_row("Instagram", "https://instagram.com/@wanz_xploit")
        table.add_row("YouTube", "https://youtube.com/@wanzxploit")
        console.print(table)

    def _show_menu(self):
        """Show menu options"""
        console.print("\n[bold cyan]Select Mode:[/bold cyan]")
        menu_options = [
            "[1] Single Short Link",
            "[2] Multi Short Link", 
            "[3] Exit"
        ]
        for option in menu_options:
            console.print(f"   {option}", style="blue")

    def single_short(self):
        """Process single short link"""
        url = Prompt.ask("[bold cyan]Enter the URL[/bold cyan]", default="https://")
        
        results = []
        with Progress() as progress:
            task = progress.add_task("[blue]Processing...", total=len(self.servers))
            
            for server in self.servers:
                try:
                    short_link = self._generate_short_link(server, url)
                    results.append([server, short_link])
                except Exception:
                    results.append([server, "[red]Failed[/red]"])
                progress.update(task, advance=1)
        table = Table(title="[bold cyan]Short Link Results[/bold cyan]", border_style="blue")
        table.add_column("Server", style="blue")
        table.add_column("Short Link", style="cyan")
        for result in results:
            table.add_row(result[0], result[1])
        console.print(table)

    def multi_short(self):
        """Process multiple short links"""
        filename = Prompt.ask("[bold cyan]Enter the input file name[/bold cyan]", default="links.txt")
        
        try:
            with open(filename, 'r') as file:
                links = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            console.print("[bold red]File not found![/bold red]")
            return

        server = Prompt.ask("[bold cyan]Select a Server[/bold cyan]", choices=self.servers, default="Bitly")

        results = []
        with Progress() as progress:
            task = progress.add_task(f"[blue]Processing {len(links)} Links...", total=len(links))
            
            for link in links:
                try:
                    short_link = self._generate_short_link(server, link)
                    results.append([link, short_link, "Success"])
                except Exception:
                    results.append([link, "[red]Failed[/red]", "Error"])
                progress.update(task, advance=1)
        table = Table(title=f"[bold cyan]Short Link Results - {server}[/bold cyan]", border_style="blue")
        table.add_column("Original Link", style="blue")
        table.add_column("Short Link", style="cyan")
        table.add_column("Status", style="blue")
        for result in results:
            table.add_row(result[0], result[1], result[2])
        console.print(table)
        with open("short_results.txt", "w") as file:
            for result in results:
                file.write(f"{result[0]} -> {result[1]} : {result[2]}\n")
        console.print(f"[bold blue]Results saved in 'short_results.txt'[/bold blue]")
    def _generate_short_link(self, server, url):
        """Generate short links for a given server"""
        api_key = self.api_keys[server]
        try:
            if server == "Bitly":
                headers = {"Authorization": f"Bearer {api_key}"}
                response = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"long_url": url}, headers=headers)
                return response.json().get("link", "Failed")
            elif server == "TinyURL":
                response = requests.post("https://api.tinyurl.com/create", headers={"Authorization": f"Bearer {api_key}"}, json={"url": url})
                return response.json().get("data", {}).get("tiny_url", "Failed")
            elif server == "Cutt.ly":
                response = requests.get("https://cutt.ly/api/api.php", params={"key": api_key, "short": url})
                return response.json().get("url", {}).get("shortLink", "Failed")
        except Exception as e:
            console.print(f"[red]Error on {server}: {e}[/red]")
            return "Failed"
    def run(self):
        """Run the application"""
        while True:
            os.system("clear")
            self._banner()
            self._show_menu()
            choice = Prompt.ask("[bold cyan]Select Mode[/bold cyan]", choices=["1", "2", "3"], default="1")
            if choice == "1":
                self.single_short()
            elif choice == "2":
                self.multi_short()
            else:
                console.print("[bold blue]Thank you for using Doble Shortener![/bold blue]")
                break
            console.input("\n[bold cyan]Press Enter to return to the menu...[/bold cyan]")
def main():
    """Main function"""
    generator = ShortLinkGenerator()
    generator.run()

if __name__ == "__main__":
    main()