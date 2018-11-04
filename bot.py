# use config.ENVVARNAME to use a env var
import config
import discord
import logging
import random

import TriggerManager

from discord.ext import commands


logging.basicConfig(level=logging.INFO)


# Go to `https://discordapp.com/oauth2/authorize?client_id=494271504570122240&scope=bot` to add this bot to a server

description = '''
Bot pour le channel discord du club informatique du cégep de Saint-Hyacinthe
'''
bot = commands.Bot(command_prefix='!', description=description)
trigger_manager = TriggerManager.TriggerManager()

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

    if rolls <= 0:
        await bot.say('Il doit y avoir au moins un dé a lancé!!')
        return

    if limit < 1:
        await bot.say('La valeur du dé doit être plus grande que 0!')
        return

    iResults = list(random.randint(1, limit) for _ in range(rolls))
    sResults = ', '.join(str(i) for i in iResults)
    await bot.say('Résultat(s): {0}.\nPour un total de: {1}'.format(sResults, sum(iResults)))

@bot.command()
async def think():
    """
    Donne une pensée, probablement philosophique
    """

    messages =  [
        "Une patate c'est pas une carotte, pourtant les deux vienne de la terre",
        "Si le vide est l'absence de matière, est-il possible d'être plein de vide?",
        "On nous dit toujours de ne jamais juger un livre par sa couverture mais les couvertures de livres sont spécialement creer pour emettre un jugement sur le livre",
        "Est ce que les chiens pense que lorsque ont leur dis que ce sont des bons chien que cest une commande pour etre heureux et il ne font qu'obeir ou sont t'ils vraiment de bon chien ??",
        "À notre 35e aniversaire nous aurons vecue pendans 420 mois O_O",
        "Dans un jour lointain la plupars des compte en ligne vont apartenir a des personnes décédé.",
        "Dans le future, les enfants jouant avec des petite auto et des motos ne feront plus de bruit de moteur car les voitures électriques seront plus courantes.",
        "Quelqu'un pourait deja avoir découvert comment se mettre invisible et ferais juste niaiser le monde au lieux de le montrer au monde.",
        "Les stations radio dans les jeux videos sont infiniment meilleur que les stations radio dans la vrais vie, pourquoi ??",
        "Lorsque vous utilisez les caisses libre service au supermarché cest comme si vous faissiez du travail non rémunérer pour le supermarcher",
    ]
    msg = random.choice(messages)
    await bot.say(f":thinking: {msg} :thinking:")

@trigger_manager.trigger()
async def kek(msg):
    if msg.author == bot.user:
        return

    await bot.send_message(msg.channel, '?!?')

@trigger_manager.trigger('WoWoW', TriggerManager.TriggerOptions.ENDS | TriggerManager.TriggerOptions.CASE_SENSITIVE)
async def wowow(msg):
    if msg.author == bot.user:
        return

    await bot.send_message(msg.channel, 'wOwOw')

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    # Process registered Commands
    await bot.process_commands(msg)
    await trigger_manager.process_triggers(msg)
    msg_content = msg.clean_content

    if msg_content.lower()[-4:] == 'haha':
        await bot.send_message(msg.channel, 'yes')

    if msg_content.lower().find('∞') != -1:
        await bot.send_message(msg.channel, '😭😭😭∞ isn\'t 8😭😭😭')

    if msg_content.lower().find('nice') != -1:
        await bot.send_message(msg.channel, 'Fucking ***NICE***')

    if msg_content.lower().find('number 1') != -1:
        await bot.send_message(msg.channel, 'F Robbie Rotten, Born a villain, Died a Hero 😭')

    if msg_content.lower().find('oof') != -1:
        choices = ['Big *OOF*', 'Roblox death sound', 'Oof oww my bones hurt a lot\nOof ouch oww owie my bonessss']
        await bot.send_message(msg.channel, random.choice(choices))

    if msg_content == '!shutdown!' and msg.author.nick == 'Camarade Nicolas L.':
        await bot.close()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    await bot.change_presence(game=discord.Game(name='To all you say', type=2))

bot.run(config.DISCORD_BOT_TOKEN)