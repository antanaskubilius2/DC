  
import discord

client = discord.Client()


@client.event

async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("!help"):

        if str(message.author) == "TSZ_Tonez#6999":  # make sure to change to your user name with hash code
            await message.channel.send("!help " + str(message.author) + "!")
        else:
            await message.channel.send("Hello, I am a test bot.")
    
async def on_ready():
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Fortnite'))
client.run('Njk1MTAzODQ3MDM0NTE5NTUy.XoVT5w.g_fZOCBTLRCsj-5wHhfBsRW-6Aw')  # copy your token from the developer portal