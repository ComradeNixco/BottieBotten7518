# use config.ENVVARNAME to use a env var
import config
import discord
import random

from discord.ext import commands


# Go to `https://discordapp.com/oauth2/authorize?client_id=494271504570122240&scope=bot` to add this bot to a server

description = '''
Bot pour le channel discrod du club info
'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.command()
async def add(left: int, right: int):
    """Adds 2 numbers together"""

    if left == 9 and right == 10:
        await bot.say('{0} or something'.format(21))
    else:
        await bot.say(left + right)

@bot.command()
async def roll(dice: str):
    """Roule un dé dans le format NdN"""

    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Le format doit être NdN')
        return

    if rolls > 100:
        await bot.say('Maximum de 100 par roulement!!')
        return

    if limit < 1:
        await bot.say('La valeur du dé doit être plus grande que 0!')
        return

    iResults = list(random.randint(1, limit) for _ in range(rolls))
    sResults = ', '.join(str(i) for i in iResults)
    await bot.say('Résultat(s): {0}.\nPour un total de: {1}'.format(sResults, sum(iResults)))

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # Process registered Commands
    await bot.process_commands(msg)

    if msg.content.lower() == 'haha':
        await bot.send_message(msg.channel, 'yes')

    if msg.content.lower().find('8') != -1:
        await bot.send_message(msg.channel, 'haha 8')

    if msg.content.lower().find('nice') != -1:
        await bot.send_message(msg.channel, 'Fucking ***NICE***')

    if msg.content.lower().find('number 1') != -1:
        await bot.send_message(msg.channel, 'F Robbie Rotten, Born a villain, Died a Hero 😭')

    if msg.content.lower().find('oof') != -1:
        choices = ['Big *OOF*', 'Roblox death sound', 'Oof oww my bones hurt a lot\nOof ouch oww owie my bonessss']
        await bot.send_message(msg.channel, random.choice(choices))

    if msg.content == '!shutdown!' and msg.author.nick == 'Camarade Nicolas L.':
        await bot.close()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    await bot.change_presence(game=discord.Game(name='To all you say', type=2))

bot.run(config.DISCORD_BOT_TOKEN)