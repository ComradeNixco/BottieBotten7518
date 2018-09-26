# use config.ENVVARNAME to use a env var
import config
import discord

# Go to `https://discordapp.com/oauth2/authorize?client_id=494271504570122240&scope=bot` to add this bot to a server

client = discord.Client()

@client.event
async def on_message(msg : discord.Message):
    if msg.author == client.user:
        return

    if(msg.author.nick == 'Étienne B.'):
        await client.send_message(msg.channel, '**STOP**')

    if msg.content == 'haha':
        await client.send_message(msg.channel, 'yes')

    if msg.content.lower().find('nice') != -1:
        await client.send_message(msg.channel, 'Fucking ***NICE***')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(config.DISCORD_BOT_TOKEN)