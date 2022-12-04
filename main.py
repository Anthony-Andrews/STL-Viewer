import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for attachment in message.attachments:
        attachment = message.attachments[0].url
        filetype = attachment.split('.')[-1]
        file = attachment.split('/')[-1]
        filename = file.split('.')[0]
        
        if filetype.lower() == 'stl':

            await message.attachments[0].save(file) # saves the file

            render = 'stltopng /res 500 /png "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+filename+'.png" "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+file+'"'

            os.system(render)
            
            await message.reply(file=discord.File(filename+'.png'))

            os.remove(file)
            os.remove(filename+'.png')

client.run(os.getenv('BOT_TOKEN'))