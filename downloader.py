from pytube import YouTube
import os
import time

# Optional: For fancy terminal colors
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Installing colorama...")
    os.system('pip install colorama')
    from colorama import init, Fore, Style
    init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
    A     K   K   SSSS   H   H   III   TTTTT
   A A    K  K   S       H   H    I      T  
  AAAAA   KKK     SSS    HHHHH    I      T  
 A     A  K  K       S   H   H    I      T  
A       A K   K   SSSS   H   H   III     T  
""" + Style.RESET_ALL)
    print(Fore.YELLOW + "🚀 Welcome to the AKSHIT YouTube Downloader 🚀\n" + Style.RESET_ALL)

def loading(text="Downloading"):
    print(Fore.MAGENTA + text, end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(Style.RESET_ALL)

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(Fore.BLUE + f"\n🎬 Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"⏱️ Duration: {yt.length} seconds")
    loading("📥 Downloading video")
    stream.download()
    print(Fore.GREEN + "\n✅ Video downloaded successfully!" + Style.RESET_ALL)

def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    print(Fore.BLUE + f"\n🎬 Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"⏱️ Duration: {yt.length} seconds")
    loading("🎧 Downloading audio")
    out_file = stream.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(Fore.GREEN + "\n✅ Audio downloaded successfully as MP3!" + Style.RESET_ALL)

def main():
    banner()
    url = input(Fore.CYAN + "\n🔗 Enter YouTube video URL: " + Style.RESET_ALL).strip()
    print(Fore.YELLOW + "\n🎯 Choose download option:")
    print("1️⃣  Video (MP4)")
    print("2️⃣  Audio only (MP3)" + Style.RESET_ALL)
    choice = input(Fore.CYAN + "\n👉 Enter your choice (1 or 2): " + Style.RESET_ALL)

    try:
        if choice == '1':
            download_video(url)
        elif choice == '2':
            download_audio(url)
        else:
            print(Fore.RED + "❌ Invalid choice. Please choose 1 or 2." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"⚠️ Error occurred: {e}" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
