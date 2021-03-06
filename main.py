import discord, json, os
from discord import Activity, ActivityType
from discord.ext import commands

def prefix(client, message):
    if message.guild:
        dir()
        with open('guild.json', 'r') as f:
            data = json.load(f)["Guilds"]

            for e in data:
                if int(e["ID"]) == message.guild.id:
                    return str(e["Prefix"])

def dir_(amount : int):
    "Move up a directory."
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(amount * ".")

def clean(s : str):
    "Cleans a mention by reducing it to it's bare ID."
    
    return  s.replace("!", ""
            ).replace("@", ""
            ).replace("#", ""
            ).replace("<", ""
            ).replace(">", ""
            ).replace("&", "")
        
def id_(i : int, ctx : commands.Context):
    "Attempts to find a model with a given ID."

    try:
        return discord.utils.find(lambda m : m.id == i, ctx.guild.members)
    
    except commands.MemberNotFound:
        try:
            return discord.utils.find(lambda r : r.id == i, ctx.guild.roles)
        
        except commands.RoleNotFound:
            try: 
                return discord.utils.find(lambda c : c.id == i, ctx.guild.text_channels)

            except commands.ChannelNotFound:
                return None

def my_colour(ctx):
    return discord.utils.find(lambda m : m.id == client.user.id, ctx.guild.members).colour


client = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())
client.remove_command("help")

for cog in os.listdir("./cogs"):
    if cog.endswith(".py") and cog.lower() != "__init__.py":
        
        try:
            client.load_extension(f'cogs.{cog[:-3]}')
            print(f"Loaded cogs.{cog[:-3]}")
        
        except Exception:
            print(f"{cog[:-3]} failed to load!")
            raise

@client.event
async def on_ready():
    await client.change_presence(activity = Activity(type = ActivityType.watching, name = 'the server'))
    print(f"Successfully logged in as {client.user}.")

def token():
    dir()
    
    with open("token.json", "r+") as f:
        data = json.load(f)

        return str(data["token"])

client.run(token(), bot = True)