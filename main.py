import discord
import os
from dotenv import load_dotenv
#import vtkplotlib as vpl
#from stl.mesh import Mesh

#mesh = Mesh.from_file("Lattice_Cube_by_LazerLord10.stl")
#fig = vpl.figure()
#mesh = vpl.mesh_plot(mesh)
#vpl.show()

load_dotenv()

client = discord.Client(intents=discord.Intents.all() , command_prefix= "~" , description='partialPing test bot :D')

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
        filename = attachment.split('/')[-1]
        await message.channel.send(filetype)
        if filetype.lower() == 'stl':
            await message.channel.send('yehaw')
            await message.attachments[0].save(filename) # saves the file

client.run(os.getenv('BOT_TOKEN'))