import discord
# import config
import os
from datetime import timedelta, datetime
import omikuzi

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
                        "`/youtube`: youtubeのURLを出します.\n" \
                        "option: `--omanko`\n" \
                        "`/source` : ソースを出します.\n" \
                        ""
        send_message += "`/saying`: 名言を言ってくれます.\n"
        send_message += "`/omikuzi`: NarurungoBotがおみくじを引いてくれます.\n"

    if message.content == '/youtube':
        send_message: str = "https://youtube.com"

    if message.content == '/youtube --omanko':
        send_message = "http://pornhub.com"

    if message.content == '/source':
        send_message = "https://github.com/butsuli-shine/discordbot"
    
    if message.content == '/saying':
        send_message = "なるルンゴbotは常に稼働してるのに\n"\
                       "どうしてお前らは開発しないんだ!"
    
    if message.content == '/omikuzi':
        send_message = omikuzi.get_omikuzi()

    await message.channel.send(send_message)


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 778628083732316160 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(778628083732316165)
        if before.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)


if __name__ == "__main__":
    client.run(token)
