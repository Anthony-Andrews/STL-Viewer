import dotenv from 'dotenv' // load discord bot token
dotenv.config()

import { Client } from 'discord.js'; // import discord.js

const client = new Client({ intents: ['Guilds', 'GuildMessages', 'GuildMembers', 'DirectMessages'] }); // setup perms
const fileTypes = ['.stl', '.gcode']; //leave the file types here

client.login(process.env.DISCORD_TOKEN); // initialize bot token

client.on("messageCreate", async (message) => {

    message.attachments.forEach(attachment => { //iterates over all attachments
        for (fileType of fileTypes) { //iterates over all the file types provided
          if (attachment.name.includes(fileType)) { //checks if the name of the attachment includes the file type
            message.delete() // if yes, deletes
      
            message.channel.send(`Message deleted because it contains a ${fileType} file`);
          };
        };
      });
});