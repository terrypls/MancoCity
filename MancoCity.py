import discord  # libreria de discord para python
import ID  # Archivo con Token e ID usadas
from Varios import *
from Diccionario import Key
from Mancos import Shesho, David

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    strMessage = message.content
    llave = strMessage.split(" ", 1)
    print(llave)
    funcion = Key(llave[0])
    text2speech = tts(llave[0])
    if funcion:
        msg = funcion.format(message)
        if text2speech == -1:
            await client.send_message(message.channel, msg)
        else:
            await client.send_message(message.channel, msg, tts=True)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(ID.TOKEN)
