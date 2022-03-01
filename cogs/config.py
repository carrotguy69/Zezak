import discord, os, json
from thefuzz import process, fuzz
from main import dir_, prefix, clean, id_
from discord.ext import commands

class config(commands.Cog):
    def __init__(self, client):
        self.client = client

    def return_model(self, ctx, s : str):
        result = process.extractOne(s, [m.name for m in ctx.guild.members]) # extract best fitting member
        print(s, result)
        
        print(fuzz.ratio(result, s))
        if fuzz.ratio(result, s) > 90: # if the real name is close enough to the inputted name
            print(fuzz.ratio(result, s))
            return discord.utils.find(lambda m : m.name == result, ctx.guild.members)

        else:
            result = process.extractOne(s, [r.name for r in ctx.guild.roles])

            if fuzz.ratio(result, s) > 90:
                return discord.utils.find(lambda r : r.name == result, ctx.guild.roles)
            
            else:
                result = process.extractOne(s, [c.name for c in ctx.guild.text_channels])

                if fuzz.ratio(result, s) > 90:
                    return discord.utils.find(lambda c : c.name == result, ctx.guild.text_channels)
                
                else:
                    return None

    @commands.has_guild_permissions(administrator = True)
    @commands.command()
    async def permit(self, ctx, group, perm = None):
        """
        Allow a user or role to use mod/admin commands.
        """

        if group == "help":
            
            dir_(1)
            with open("Permissions", "r+") as f: 
                return await ctx.reply(f.read(), mention_author = False)

        if group:
            self.return_model(ctx, group)

    @permit.error
    async def permit_error(self, ctx, e):
        if isinstance(e, commands.MissingRequiredArgument):
            
            dir_(1)
            with open("Permissions", "r+") as f:
                with open("commands.json", "r+") as f2:

                    return await ctx.reply(f.read().format(json.load(f2)["modules"]["config"][0]["Syntax"]) % prefix(self.client, ctx.message), mention_author = False)
        
        else:
            raise e

def setup(client):
    client.add_cog(config(client))