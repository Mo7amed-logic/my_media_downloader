from setuptools import setup, find_packages

setup(
    name="my_media_downloader",
    version="0.1.0",
    description="A simple media downloader for images and videos.",
    author="Mo7amed-logic",
    author_email="medhasnaoui833@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "download-media=my_media_downloader.downloader:download_media",
        ],
    },
)
