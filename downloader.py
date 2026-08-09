import yt_dlp
import os
from colorama import init, Fore
init(autoreset=True)

#        ██     ██ ██████ ██     ▄█████ ▄████▄ ██▄  ▄██ ██████ 
#        ██ ▄█▄ ██ ██▄▄   ██     ██     ██  ██ ██ ▀▀ ██ ██▄▄   
#         ▀██▀██▀  ██▄▄▄▄ ██████ ▀█████ ▀████▀ ██    ██ ██▄▄▄▄ 




print(f"""{Fore.YELLOW}
---------------------------------Gide----------------------------{Fore.CYAN}
-Enter the URL, and your preferred choice.
-To finish, leave the URL blank and press enter.
-Valid choices: 360, 480, 720, 1080, 1440, height and mp3.
-If you don't choose a choice, it will use the last choice.
-For downloading reels, the 'height' option is recommended..{Fore.YELLOW}
-----------------------------------------------------------------""" )

links = []
choices = []
options = []

def_choice = "height"
while True:
    url = input(f"{Fore.WHITE}Enter URL: {Fore.RED}")
    if url:
        choice = input(f"{Fore.WHITE}Enter your choice: {Fore.RED}").lower()
        if "http" in url:
            links.append(url)
        else:
            pass
        if choice in ["height", "360", "480", "720", "1080", "1440", "mp3"]:
            choices.append(choice)
            def_choice = choice
        else:
            choices.append(def_choice)
    else:
        break



for choice in choices:
    if choice == "mp3":
        yt_opts= {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ignoreerrors': True,
            }
    else:
        yt_opts = {
            'format': f'bestvideo[height<={choice}]+bestaudio/best[height<={choice}]',
            'merge_output_format': 'mp4',
            'ignoreerrors': True,
            }
        if choice == "height":
            yt_opts["format"] = 'bestvideo+bestaudio/best'
    options.append(yt_opts)

print(f"{Fore.GREEN}-------------------------STARTING-------------------------")

for url, option in zip(links, options):
    if "youtube.com" in url or "youtu.be" in url:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Videos", "downloads", "youtube")
        option["outtmpl"] = os.path.join(downloads_folder, '%(title)s.%(ext)s')
    elif "tiktok.com" in url:
            downloads_folder = os.path.join(os.path.expanduser("~"), "Videos", "downloads", "tiktok")
            option["outtmpl"] = os.path.join(downloads_folder, '%(title)s.%(ext)s')
    elif "instagram.com" in url:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Videos", "downloads", "instagram")
        option["outtmpl"] = os.path.join(downloads_folder, '%(title)s [%(id)s].%(ext)s')
        for browser in ['brave', 'chrome', 'edge', 'firefox', 'opera']:
            try:
                option['cookiesfrombrowser'] = (browser,)
                break
            except Exception:
                pass
    elif "facebook.com" in url:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Videos", "downloads", "facebook")
        option["outtmpl"] = os.path.join(downloads_folder, '%(title)s.%(ext)s')
    else:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Videos", "downloads")
        option["outtmpl"] = os.path.join(downloads_folder, '%(title)s [%(id)s].%(ext)s')
        
    
    try:
        with yt_dlp.YoutubeDL(option) as ydl:
            ydl.download([url])
        print(f"{Fore.GREEN}--------------------{links.index(url) + 1}.Done--------------------")

    except Exception as e:
        print(f"{Fore.RED}----We have an error in url number {links.index(url) + 1}----\nError: {e}")


input(Fore.CYAN+ "\n\t\tComplete, press enter to exit...")



