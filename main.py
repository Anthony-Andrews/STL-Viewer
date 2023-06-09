import discord # import discord.py bot api
import os # import os dependencies
from dotenv import load_dotenv #import dotenv
from discord import app_commands # for use with application commands

load_dotenv() # load token from dotenv

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents().all()) # discord active commands gargain
        self.synced = False

    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for stl's")) # set status of bot to watching for stl's
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

        ### Commands: ###
        
client = MyClient()
tree = app_commands.CommandTree(client)

@tree.command(name = "hello", description = "Bot says hello!") # add command /hello
async def self(interaction: discord.Interaction, yourname: str):
    await interaction.response.send_message("Hello "+yourname+("!")) # returns message Hello, yourname!
    
@tree.command(name = "adminreveal", description = "admin reveal moment") # moai
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File("moai.png"))
    
    ### End of Commands ###

@client.event
async def on_message(message): # when a message is sent:
    if message.author == client.user: # if message is sent by a hooman continue:
        return
        
    for attachment in message.attachments:          # for each attachment sent by user:
        try:

            attachStr = repr(attachment).split(r"'>")[0] # parse the object to get a string
            filetype = attachStr.split('.')[-1].lower()  # parse the string to get the file type

            if filetype == 'stl':                        # if the attachement is an stl:
                async with message.channel.typing():        # bot types while it does the thinky think
                    fileurl = attachStr.split(r"url='")[-1]  # parse the string to get the url
                    file = attachStr.split('/')[-1]          # parse the string to get the file name and extension
                    filename = file.split('.')[0]            # parse the file to get just the file name
                    print("==========================================================================================================================")
                    print('Loading....')
                    print(fileurl)
                    print(message)
                    print("==========================================================================================================================") # logging for debugging

                    await attachment.save(file) # the bane of my exsistance

                    try:        #   ============= RENDERING STARTS HERE ==============  #
                        render = 'stltopng /res 150 /png "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+filename+'.png" "C:\\Users\\antho\\GitHub VSCode Remote Repos\\STL-Viewer\\'+file+'"' # parse command to be sent to renderer

                        os.system(render) # use stltopng (https://papas-best.com/stltopng_en) to render the stl (command generated above)
            
                        await message.reply(file=discord.File(filename+'.png')) # reply to user with preview image

                        os.remove(file)                # cleanup of temporary files
                        os.remove(filename+'.png')     # Easter Egg
                        print('STL Previewed :D')                           # ======= end of rendering ===== #

                    except Exception:
                        await message.reply("An error has occured DM partial#1111. (the code is brokey );") # error handling
                        print('error 1')
                        os.remove(file)                # cleanup of temporary files IF stuff goes wrong
                        os.remove(filename+'.png')

            else:
                pass
        except Exception:
            await message.reply("An error has occured DM partial#1111. (bruh ofc it stopped working)") # error handling
            print('error 0')

client.run(os.getenv('BOT_TOKEN')) # start bot with token
