import discord   #libreria de discord para python
import ID        #Archivo con Token e ID usadas
import Varios
from Mancos import Shesho,David
client = discord.Client()



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('loli'):
        msg = Varios.loli().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('manco'):
        msg = Varios.manco().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hello'):
        msg = Varios.hola().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('shesho'):
        msg=Shesho.shesho().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('porno'):
        msg = Varios.porno().format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('F'):
        msg = Varios.F().format(message)
        await client.send_message(message.channel, msg, tts=True)

    if message.content.startswith('oniichan'):
        msg = Varios.Onichan().format(message)
        await client.send_message(message.channel, msg, tts=True)

    if message.content.startswith('hungria'):
    	msg= David.hungaria().format(message)
    	await client.send_message(message.channel,msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(ID.TOKEN)
