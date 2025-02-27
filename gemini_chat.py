#!/usr/bin/env python3

import google.generativeai as genai
import os
import sys
import signal
from colorama import init, Fore, Style

# Initialize colorama for Windows CMD
init()

class GeminiChat:
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

        if not self.api_key:
            print(f"{Fore.RED}Error: GOOGLE_API_KEY environment variable not set.{Style.RESET_ALL}")
            sys.exit(1)

        genai.configure(api_key=self.api_key)
        self.initialize_model()

    def initialize_model(self):
        try:
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:
            print(f"{Fore.RED}Error initializing model '{self.model_name}': {e}{Style.RESET_ALL}")
            print(f"{Fore.RED}Please check if the model name is valid.{Style.RESET_ALL}")
            sys.exit(1)

    def handle_interrupt(self, signal, frame):
        print(f"\n\n{Fore.YELLOW}Interrupted by user. Exiting...{Style.RESET_ALL}")
        sys.exit(0)

    def start_chat(self):
        signal.signal(signal.SIGINT, self.handle_interrupt)

        chat_session = self.model.start_chat(history=[])
        print(f"{Fore.CYAN}==========================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}     Welcome to Gemini Chat!     {Style.RESET_ALL}")
        print(f"{Fore.CYAN} (Type 'exit', 'quit', or 'bye' to end) {Style.RESET_ALL}")
        print(f"{Fore.CYAN}==========================================={Style.RESET_ALL}")

        while True:
            try:
                prompt = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
                
                if prompt.lower() in ["exit", "quit", "bye"]:
                    print(f"{Fore.MAGENTA}-------------------------------------------{Style.RESET_ALL}")
                    print(f"{Fore.BLUE}**Gemini**: Goodbye!{Style.RESET_ALL}")
                    print(f"{Fore.MAGENTA}-------------------------------------------{Style.RESET_ALL}")
                    break
                
                if not prompt:
                    continue

                response = chat_session.send_message(prompt)
                print(f"{Fore.MAGENTA}-------------------------------------------{Style.RESET_ALL}")
                print(f"{Fore.BLUE}**Gemini**: {response.text}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}-------------------------------------------{Style.RESET_ALL}")

            except EOFError:
                print(f"\n\n{Fore.YELLOW}EOF detected. Exiting...{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
                continue

def main():
    try:
        chat = GeminiChat()
        chat.start_chat()
    except Exception as e:
        print(f"{Fore.RED}Fatal error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
