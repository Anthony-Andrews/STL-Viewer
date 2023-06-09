import discord # import discord.py bot api
import os # import os dependencies
import logging # i ❤️ logs
import time # for perfomance metrics
from dotenv import load_dotenv #import dotenv
from discord import app_commands # for use with application commands

load_dotenv() # load token from dotenv

logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s') # generate the log

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents().all()) # discord active commands gargain
        self.synced = False

    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for stl's 👀")) # set status of bot to watching for stl's
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        logging.info(f"We have logged in as {self.user}.")

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
            start = time.time() # start the timer

            attachStr = repr(attachment).split(r"'>")[0] # parse the object to get a string
            filetype = attachStr.split('.')[-1].lower()  # parse the string to get the file type

            if filetype == 'stl':                        # if the attachement is an stl:
                async with message.channel.typing():        # bot types while it does the thinky think
                    fileurl = attachStr.split(r"url='")[-1]  # parse the string to get the url
                    file = attachStr.split('/')[-1]          # parse the string to get the file name and extension
                    filename = file.split('.')[0]            # parse the file to get just the file name


                    render = 'stltopng /res 250 /png "C:\\Users\\antho\\Desktop\\STL-Viewer-main\\'+filename+'.png" "C:\\Users\\antho\\Desktop\\STL-Viewer-main\\'+file+'"' # parse command to be sent to renderer

                    logging.info(str(message))     # logging for stats

                    print("========================================================================================================================")
                    print('Loading file...   '+str(message))
                    print('Parsed render command:')
                    print(render)
                    print("========================================================================================================================") # logging for debugging

                    await attachment.save(file) # the bane of my exsistance

                    os.system(render) # uses stltopng (https://papas-best.com/stltopng_en) to render the stl (command generated above)
            
                    await message.reply(file=discord.File(filename+'.png')) # reply to user with preview image

                    os.remove(file)                # cleanup of temporary files
                    os.remove(filename+'.png')     # Easter Egg
                    end = time.time()              # stop timer
                    print('Done in: '+str(end - start)+' seconds')
                    logging.info('Done in: '+str(end - start)+' seconds') # success

            else:
                pass
        except Exception: # error handling stuff
            logging.error('[ERROR   ] DEBUG INFO= file: '+file+' file url: '+fileurl+' file name: '+filename+' render string from parser: '+render+'  message:'+str(message))
            print('[ERROR   ] DEBUG INFO= file: '+file+' file url: '+fileurl+' file name: '+filename+' render string from parser: '+render+'  message:'+str(message))
            await message.reply('An error has occured /:  DM "partial"')
            os.remove(file)                # cleanup of temporary files IF stuff goes wrong
            os.remove(filename+'.png')

client.run(os.getenv('BOT_TOKEN')) # start bot with token
