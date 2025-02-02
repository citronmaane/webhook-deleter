## DOWNLOAD PYTHON AT PYTHON.ORG
## COPY ALL THE TEXT IN THIS FILE AND MAKE A PYTHON FILE (EXAMPLE: spammer.py)
## PASTE THE TEXT IN THE FILE AND RUN IT.

## IF YOU DONT KNOW HOW TO USE PYTHON FILES WATCH A YOUTUBE VIDEO OR SOMETHING.


import requests
import time
import sys
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.02, color="\033[0m"):  # Faster typewriter effect
    sys.stdout.write(color + text + "\033[0m\n")
    sys.stdout.flush()
    time.sleep(delay)

def send_discord_message(webhook_url, message, delay, times):
    for i in range(times):
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(f"Sent message {i+1}/{times}")
        else:
            print(f"Failed to send message {i+1}/{times}: {response.status_code}")
        time.sleep(delay / 1000)  # Convert ms to seconds

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        typewriter_effect("Webhook deleted successfully!")
    else:
        typewriter_effect(f"Failed to delete webhook: {response.status_code}")

def main():
    while True:
        clear_console()
        
        typewriter_effect("Select an option:")
        typewriter_effect("1. Send message via webhook")
        typewriter_effect("2. Delete webhook")
        typewriter_effect("3. Exit")
        
        choice = input("\033[92m[INPUT] \033[0mEnter choice (1/2/3): ")
        
        if choice == "1":
            typewriter_effect("Enter Discord Webhook URL: ")
            webhook_url = input("\033[92m[INPUT] \033[0m")
            
            typewriter_effect("Enter message to send: ")
            message = input("\033[92m[INPUT] \033[0m")
            
            typewriter_effect("Enter delay between messages (ms) RECOMMENDED: 1000ms: ")
            delay = int(input("\033[92m[INPUT] \033[0m"))
            
            typewriter_effect("Enter number of times to send the message: ")
            times = int(input("\033[92m[INPUT] \033[0m"))
            
            typewriter_effect("Starting message sending process...\n")
            send_discord_message(webhook_url, message, delay, times)
            typewriter_effect("Done! Returning to main menu...\n")
        
        elif choice == "2":
            typewriter_effect("Enter Discord Webhook URL to delete: ")
            webhook_url = input("\033[92m[INPUT] \033[0m")
            
            typewriter_effect("Deleting webhook...\n")
            delete_webhook(webhook_url)
            typewriter_effect("Returning to main menu...\n")
        
        elif choice == "3":
            typewriter_effect("Exiting...\n")
            break
        
        else:
            typewriter_effect("Invalid choice. Try again...\n")

if __name__ == "__main__":
    main()