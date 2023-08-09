# Weather-Bot
The Discord Weather Bot is a Python script that utilizes the discord.py library to create a bot that provides weather information for specific locations using the OpenWeatherMap API. The bot listens for commands with a specified prefix and responds with weather data.

Features
1. Fetches current weather information for a specified location using the OpenWeatherMap API.

2. Displays weather information in a formatted and user-friendly manner on the Discord server.

3. Supports a customizable command prefix.


Prerequisites
 Python 3.6 or higher
 discord.py library
 OpenWeatherMap API Key
Setup
Clone this repository or download the script directly.

Install the required dependencies using the following command:
pip install discord.py requests

Obtain an API key from the OpenWeatherMap API and replace YOUR_API_KEY in the code with your actual API key.

Create a Discord bot and obtain a bot token. Replace YOUR_BOT_TOKEN in the code with your actual bot token.

Customize the command prefix if desired. Replace W/ in the code with your preferred prefix.

Create a weather.py file containing functions to parse and format weather data. Ensure this file is in the same directory as the main script.
