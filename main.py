import requests
import concurrent.futures
from colorama import Fore, init
import time

# Initialize colorama
init()

# Function to check if a username is available on SoundCloud
def check_soundcloud(username):
    try:
        url = f"https://soundcloud.com/{username}"
        response = requests.get(url)
        
        if response.status_code == 404:
            print(Fore.GREEN + f"{username} is Available")
            with open("Hits.txt", "a", encoding='utf-8') as f:
                f.write(f"{username} - is Available\n")
        elif response.status_code == 200:
            print(Fore.RED + f"{username} is Taken")
        else:
            print(Fore.YELLOW + f"UNKNOWN STATUS | {username} | Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"REQUEST ERROR | {username} | {e}")

# Main function to read usernames from file and check availability on SoundCloud
def main():
    print(Fore.BLUE + "SoundCloud ID Checker\n")
    

    # Read usernames from file (names.txt)
    with open('names.txt', 'r') as file:
        usernames = [line.strip() for line in file]

    # Execute checks with multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(check_soundcloud, usernames)

if __name__ == "__main__":
    main()
