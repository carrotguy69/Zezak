import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, c):
        if not c:
            embed = discord.Embed(title = "Zezak Help", description = "")

def setup(client):
    client.add_cog(help(client))