from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "kyo",
    version = "1.1.0",
    url = "https://github.com/Sstandby/kyo",
    download_url = "https://github.com/Sstandby/kyo/tarball/master",
    license = "MIT",
    author = "Sstandby",
    author_email = "standby@sstandby.com",
    description = "Library for the creation of bots from the AminoApps platform.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        "aminoapps",
        "kyo",
        "amino",
        "aminokyo",
        "aminobots",
        "amino-bot",
        "narvii",
        "api",
        "python",
        "python3",
        "python3.x",
        "sstandby",
        "standby",
        "official"
    ],
    install_requires = [
        "setuptools",
        "requests",
        "six",
        "websockets",
        "json_minify",
        "websocket-client==1.3.1",
        "aiohttp"
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
