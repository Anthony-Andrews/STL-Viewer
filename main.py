import discord # import discord.py bot api
import os # import os dependencies
from dotenv import load_dotenv #import dotenv
from discord import app_commands # for use with application commands

load_dotenv() # load token from dotenv

client = discord.Client(intents=discord.Intents.all()) # need to update

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client)) # bot initilization gargain

@client.event
async def on_message(message): # when a message is sent:
    if message.author == client.user: # if message is sent by a hooman continue:
        return

    for attachment in message.attachments:          # for each attachment sent by user:
        attachment = message.attachments[0].url     # parse attachment sent by user to get url, filetype, and filename.
        filetype = attachment.split('.')[-1]        # ^
        file = attachment.split('/')[-1]            # ^
        filename = file.split('.')[0]               # ^
        
        if filetype.lower() == 'stl': # if the attachement is an stl:

            await message.attachments[0].save(file) # save the file

            print(attachment) # log url of file

            render = 'stltopng /res 150 /png "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+filename+'.png" "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+file+'"' # parse command to be sent to renderer

            os.system(render) # use stltopng (https://papas-best.com/stltopng_en) to render the stl (command generated above)
            
            await message.reply(file=discord.File(filename+'.png')) # reply to user with preview image

            os.remove(file)                # cleanup of temporary files
            os.remove(filename+'.png')

client.run(os.getenv('BOT_TOKEN')) # start bot with token