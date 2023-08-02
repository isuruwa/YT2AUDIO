import os
import argparse
import subprocess
import sys

def chk_depend(depend):
    try:
        subprocess.run([depend, '--help'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print(f"Error: {depend} is not installed. Please install it and try again.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print(f"Error: Failed to execute {depend}. Make sure it is installed and accessible.")
        sys.exit(1)

def download(url, out_dir, output_format, verbose):
    command = [
        'yt-dlp',
        url,
        '-x',
        '--embed-thumbnail',
        '--add-metadata',
        '--format', 'bestaudio',
        '--audio-quality', '0',
        '--audio-format', output_format,
        '--metadata-from-title', '%(artist)s - %(title)s',
        '-o', f'{out_dir}/%(title)s.%(ext)s',
    ]

    if verbose:
        command.append('--verbose')

    try:
        subprocess.run(command, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to download audio. {e}")
        sys.exit(1)

def banner():
    banner = """
YOUTUBE AUDIO DOWNLOADER | V1.0 
===============================
"""
    print(banner)

def print_about():
    banner()
    about = """
[+] Welcome to the YouTube Audio Downloader!
[+] This tool allows you to download high-quality audio from YouTube and YouTube Music.
[+] Features:
    - Supports high-quality audio downloads
    - Embeds thumbnail in audio file
    - Adds metadata to audio file
    - Verbose Mode
[+] MRX | V 1.0
"""
    print(about)

def main():
    parser = argparse.ArgumentParser(description="YouTube Audio Downloader", allow_abbrev=False)
    parser.add_argument("url", nargs='?', help="YouTube video URL")
    parser.add_argument("--output", "-o", default=os.getcwd(), help="Output directory for downloaded audio (default: current directory)")
    parser.add_argument("-f", "--output-format", default="mp3", help="Output audio format (default: mp3)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("--about", action="store_true", help="Show information about the tool")
    args, url_argument = parser.parse_known_args()

    if args.about:
        print_about()
        sys.exit(0)

    banner()
    chk_depend('yt-dlp')
    chk_depend('ffmpeg')

    if not args.url and not url_argument:
        print("Error: Please provide a YouTube video URL.\nUsage: [-h] HELP\n")
        sys.exit(1)

    url = args.url if args.url else url_argument[0]
    out_dir = os.path.expanduser(args.output)

    try:
        download(url, out_dir, args.output_format, args.verbose)
    except KeyboardInterrupt:
        print("Download process interrupted.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
