import discord  # libreria de discord para python
import ID  # Archivo con Token e ID usadas
from Varios import *
from Diccionario import *


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    strMessage = message.content
    llave = strMessage.split(" ", 2)
    print(llave)
    text2speech = tts(llave[0])
    if llave[0] == '/agrega':
        addFile(llave[1], llave[2]+'\n')
        await client.send_message(message.channel, "agregado!")
    funcion = Key(llave[0])
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
