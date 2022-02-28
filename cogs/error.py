import discord
from discord.ext import commands
from main import dir_ as d, prefix

class error(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):
        if isinstance(e, commands.MissingRequiredArgument or commands.BadArgument):
            if ctx.command.name == "permit":
                await ctx.send(ctx.command.description)
    
def setup(client):
    client.add_cog(error(client))