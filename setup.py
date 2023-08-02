from setuptools import setup, find_packages

setup(
    name="yt2audio",
    version="1.0",
    author="MRX",
    description="YouTube Audio Downloader",
    author_email = 'trymrx@pm.me',
    url = 'https://github.com/isuruwa/YT2AUDIO',
    download_url = '',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "yt2audio = yt2audio.__main__:main",
        ],
    },
    install_requires=[
        "yt-dlp",
        "ffmpeg",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

