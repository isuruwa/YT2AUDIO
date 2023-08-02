from setuptools import setup, find_packages

setup(
    name="yt2audio",
    version="1.0",
    author="MRX",
    description="YouTube Audio Downloader",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author_email = 'trymrx@pm.me',
    url = 'https://github.com/isuruwa/YT2AUDIO',
    download_url = 'https://github.com/isuruwa/YT2AUDIO/blob/main/dist/yt2audio-1.0.tar.gz',
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

