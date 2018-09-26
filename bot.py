# use config.ENVVARNAME to use a env var
import config
import discord
import random

# Go to `https://discordapp.com/oauth2/authorize?client_id=494271504570122240&scope=bot` to add this bot to a server

client = discord.Client()

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content == 'haha':
        await client.send_message(msg.channel, 'yes')

    if msg.content.lower().find('nice') != -1:
        await client.send_message(msg.channel, 'Fucking ***NICE***')

    if msg.content.lower().find('number 1') != -1:
        await client.send_message(msg.channel, 'F Robbie Rotten, Born a villain, Died a Hero 😭')

    if msg.content.lower().find('oof') != -1:
        choices = ['Big *OOF*', 'Roblox death sound', 'Oof oww my bones hurt a lot\nOof ouch oww owie my bonessss']
        await client.send_message(msg.channel, random.choice(choices))

    if msg.content == '!shutdown!' and msg.author.nick == 'Camarade Nicolas L.':
        exit()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(config.DISCORD_BOT_TOKEN)