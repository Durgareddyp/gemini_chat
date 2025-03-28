#!/usr/bin/env python3

import google.generativeai as genai
import os
import sys
import signal
from colorama import init, Fore, Style
from rich.console import Console
from rich.markdown import Markdown

# Initialize colorama for Windows CMD
init()
console = Console()

class GeminiChat:
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

        if not self.api_key:
            console.print("[bold red]Error:[/bold red] GOOGLE_API_KEY environment variable not set.")
            sys.exit(1)

        genai.configure(api_key=self.api_key)
        self.initialize_model()

    def initialize_model(self):
        try:
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:
            console.print(f"[bold red]Error initializing model '{self.model_name}':[/bold red] {e}")
            console.print("[bold red]Please check if the model name is valid.[/bold red]")
            sys.exit(1)

    def handle_interrupt(self, signal, frame):
        console.print("\n\n[bold yellow]Interrupted by user. Exiting...[/bold yellow]")
        sys.exit(0)

    def start_chat(self):
        signal.signal(signal.SIGINT, self.handle_interrupt)

        console.print("[cyan]===========================================[/cyan]")
        console.print("[bold cyan]     Welcome to Gemini Chat!     [/bold cyan]")
        console.print("[cyan] (Type 'exit', 'quit', or 'bye' to end) [/cyan]")
        console.print("[cyan]===========================================[/cyan]")

        chat_session = self.model.start_chat(history=[])

        while True:
            try:
                prompt = console.input("[green]You: [/green]").strip()
                
                if prompt.lower() in ["exit", "quit", "bye"]:
                    console.print("[magenta]-------------------------------------------[/magenta]")
                    console.print("[bold blue]Gemini:[/bold blue] Goodbye!")
                    console.print("[magenta]-------------------------------------------[/magenta]")
                    break
                
                if not prompt:
                    continue

                response = chat_session.send_message(prompt)
                console.print("[magenta]-------------------------------------------[/magenta]")
                console.print(Markdown(f"**Gemini**: {response.text}"))  # Markdown rendering
                console.print("[magenta]-------------------------------------------[/magenta]")

            except EOFError:
                console.print("\n\n[bold yellow]EOF detected. Exiting...[/bold yellow]")
                break
            except Exception as e:
                console.print(f"\n[bold red]An error occurred:[/bold red] {e}")
                continue

def main():
    try:
        chat = GeminiChat()
        chat.start_chat()
    except Exception as e:
        console.print(f"[bold red]Fatal error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
