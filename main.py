import discord # import discord.py bot api
import os # import os dependencies
from dotenv import load_dotenv #import dotenv
from discord import app_commands # for use with application commands
import wget

load_dotenv() # load token from dotenv

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents().all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = MyClient()
tree = app_commands.CommandTree(client)

@tree.command(name = "size", description = "change the size of the preview image in pixels²")
async def self(interaction: discord.Interaction, px: str):
    await interaction.response.send_message("ok its now"+px)

@client.event
async def on_message(message): # when a message is sent:
    if message.author == client.user: # if message is sent by a hooman continue:
        return
        
    for attachment in message.attachments:          # for each attachment sent by user:

        attachStr = repr(attachment).split(r"'>")[0] # parse the object to get a string
        filetype = attachStr.split('.')[-1].lower()  # parse the string to get the file type

        if filetype == 'stl':                        # if the attachement is an stl:

            fileurl = attachStr.split(r"url='")[-1]  # parse the string to get the url
            file = attachStr.split('/')[-1]          # parse the string to get the file name and extension
            filename = file.split('.')[0]            # parse the file to get just the file name
            print("==========================================================================================================================")
            print(fileurl)
            print(filetype)
            print("==========================================================================================================================") # logging for debugging

            await attachment.save(file) # the bane of my exsistance

            render = 'stltopng /res 150 /png "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+filename+'.png" "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+file+'"' # parse command to be sent to renderer

            os.system(render) # use stltopng (https://papas-best.com/stltopng_en) to render the stl (command generated above)
            
            await message.reply(file=discord.File(filename+'.png')) # reply to user with preview image

            os.remove(file)                # cleanup of temporary files
            os.remove(filename+'.png')     # Easter Egg
        else:
            pass

client.run(os.getenv('BOT_TOKEN')) # start bot with token