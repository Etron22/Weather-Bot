import discord
import json
import requests
import weather

api_key = "dff3301f39bdb3a9d22cd0c963fcb564"
discord_token = "MTA0Mzc4OTc5NjIwNTY2MjMwMA.G0AKtY.4pI0gQ7j_dAxpOXzaSuWG7nnybWH1rZNa85Fps"
command_prefix = "W/"
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name=f'{command_prefix}[location]'))


@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(
            command_prefix):
        location = message.content.replace(command_prefix, '').lower()
        if (len(location) >= 1):
            url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = json.loads(requests.get(url).content)
                data = weather.parse_data(data)
                await message.channel.send(
                    embed=weather.weather_message(data, location))
            except KeyError:
                await message.channel.send(
                    embed=weather.error_message(location))


client.run(discord_token)