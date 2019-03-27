import discord  # libreria de discord para python
from discord.ext import commands
import ID  # Archivo con Token e ID usadas
from Varios import *
from Diccionario import *

client = commands.Bot(command_prefix='?')



@client.command()
async def halp():
    await client.say('hola')

@client.event
async def on_message(message):
    autor=message.author
    mensaje=message.content
    canal=message.channel

    if autor == client.user:
        return

    llave = mensaje.split(" ", 2)
    print(llave)
    text2speech = tts(llave[0])
    if llave[0] == '/agrega':
        addFile(llave[1], llave[2] + '\n')
        await client.send_message(message.channel, "agregado!")
    funcion = Key(llave[0])
    if funcion:
        msg = funcion.format(message)
        if text2speech == -1:
            await client.process_commands(message)
            await client.send_message(message.channel, msg)

        else:
            await client.send_message(message.channel, msg, tts=True)
            await client.process_commands(message)

@client.event
async def on_ready():
    inicio()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(ID.TOKEN)
