import discord
# import config
import os

token = os.environ['discordToken']
# token = config.TOKEN
client = discord.Client()


@client.event
async def on_ready():
    print("login successfully!")


@client.event
async def on_message(message):
    send_message: str = ""
    if message.author.bot:
        return

    if message.content == '/nipple':
        send_message: str = "nipple"

    if message.content == '/help':
        send_message += "NarurungoBotです.あなたの願いをかなえます.\n"
        send_message += "`/nipple`: nippleコマンドです.\n"
        send_message += "" \
                        "`/youtube`: youtubeのURLを出します.\n"\
                        "option: `--omanko`\n"\
                        "`/source` : ソースを出します.\n"\
                        ""

    if message.content == '/youtube':
        send_message: str = "https://youtube.com"

    if message.content == '/youtube --omanko':
        send_message = "http://pornhub.com"

    if message.content == '/source':
        send_message = "https://github.com/butsuli-shine/discordbot"

    await message.channel.send(send_message)

if __name__ == "__main__":
    client.run(token)
