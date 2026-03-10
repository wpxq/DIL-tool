import requests as r
import platform, os
from colorama import Fore

w = Fore.WHITE
lb = Fore.LIGHTBLACK_EX
mgnt = Fore.MAGENTA
rd = Fore.RED

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear()
    print(f"{w}[{mgnt}KYS{w}] {lb}- {w}Discord Invite Lookup")
    invcode = input("> ")
    API = f"https://discord.com/api/v10/invites/{invcode}"
    try:
        resp = r.get(API, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # inviter section
        inviter = data.get("inviter", {})
        userid = inviter.get("id", "Unknown")
        username = inviter.get("username", "Unknown")
        globalname = inviter.get("global_name", "Unknown")
        # guild section
        guild = data.get("guild", {})
        guildid = guild.get("id", "Unknown")
        guildname = guild.get("name", "Unknown")
        # channel section
        channel = data.get("channel", {})
        channelid = channel.get("id", "Unknown")
        channelname = channel.get("name", "Unknown")
        
        print(f"{w}[{lb}*{w}] Inviter ID      : {userid}")
        print(f"{w}[{lb}*{w}] Invite Username : {username}")
        print(f"{w}[{lb}*{w}] Inviter Global  : {globalname}")
        print(f"{w}[{lb}*{w}] Guild ID        : {guildid}")
        print(f"{w}[{lb}*{w}] Guild Name      : {guildname}")
        print(f"{w}[{lb}*{w}] Channel ID      : {channelid}")
        print(f"{w}[{lb}*{w}] Channel Name    : {channelname}")
    except Exception as e:
        print(f"{w}[{lb}!{w}] Error: {e}")
        
if __name__ == "__main__":
    main()