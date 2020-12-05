import discord
import config

token = config.TOKEN
client = discord.Client()


@client.event
async def on_ready():
    print("login successfully!")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/OPPAI':
        await message.channel.send("othinpo")


if __name__ == "__main__":
    client.run(token)
