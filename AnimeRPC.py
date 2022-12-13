from pypresence import Presence
import time
from AnilistPython import Anilist
import requests
import keyboard



anilist = Anilist()
client_id = '1045803809848430624'
RPC = Presence(client_id)
RPC.connect()

def banner():
    banner_ascii = """
  ______             __                          _______   _______    ______  
 /      \           /  |                        /       \ /       \  /      \ 
/$$$$$$  | _______  $$/  _____  ____    ______  $$$$$$$  |$$$$$$$  |/$$$$$$  |
$$ |__$$ |/       \ /  |/     \/    \  /      \ $$ |__$$ |$$ |__$$ |$$ |  $$/ 
$$    $$ |$$$$$$$  |$$ |$$$$$$ $$$$  |/$$$$$$  |$$    $$< $$    $$/ $$ |      
$$$$$$$$ |$$ |  $$ |$$ |$$ | $$ | $$ |$$    $$ |$$$$$$$  |$$$$$$$/  $$ |   __ 
$$ |  $$ |$$ |  $$ |$$ |$$ | $$ | $$ |$$$$$$$$/ $$ |  $$ |$$ |      $$ \__/  |
$$ |  $$ |$$ |  $$ |$$ |$$ | $$ | $$ |$$       |$$ |  $$ |$$ |      $$    $$/ 
$$/   $$/ $$/   $$/ $$/ $$/  $$/  $$/  $$$$$$$/ $$/   $$/ $$/        $$$$$$/  
"""

    return banner_ascii

def check_update():
    # check if there's a higher version of the app
    commit_count = 3
    repo_commit_count = len(requests.get(
        "https://api.github.com/repos/TomasKrajcovicIndie/AnimeRPC/commits?per_page=100").json())
    if commit_count != repo_commit_count:
        print("\nThere is a new version of the app, please update it at https://github.com/TomasKrajcovicIndie/AnimeRPC\n")
    else:
        print("\nAnimeRPC is up to date!\n")

print(banner())
check_update()
print('')
name = input("Enter anime name: ")
episode = input("Enter episode number: ")
print('Starting AnimeRPC...')

anime_dict = anilist.get_anime_id(name)

client_id = '1045803809848430624'
RPC = Presence(client_id)
RPC.connect()
start = int(time.time())

#print(RPC.update(large_image="logo", large_text=f"Created by Fostrullik#7274", state=f"Episode: {episode}", details=f"Anime: {name}", buttons=[{"label": "What am I watching?", "url": f"https://anilist.co/anime/{anime_dict}"}]))

print('AnimeRPC running! Press CTRL+C or "q" to stop it.')
while True:
    k = RPC.update(large_image="logo", large_text=f"Created by Fostrullik#7274", state=f"Episode: {episode}", details=f"Anime: {name}", start= start, buttons=[{"label": "What am I watching?", "url": f"https://anilist.co/anime/{anime_dict}"}])
    if keyboard.is_pressed('q'):
        print("Stopping AnimeRPC on user request...")
        break