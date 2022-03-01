import discord, json, os
from thefuzz import process
from discord.ext import commands
from main import dir_, my_colour, prefix

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def list_commands(self):
        
        dir_(1)
        with open("commands.json", "r") as f:
            data = json.load(f)["modules"]

            l = []

            for module in data:
                l.append(module)
                
                for command in data[module]:
                    l.append(command["Name"])
            
        return l

    @commands.command(aliases = ["help"])
    async def commands(self, ctx, input = None):
        """Lists bot commands and other useful info."""
        
        if input:
            dir_(1)
            with open("commands.json", "r") as f:
                data = json.load(f)["modules"]

                
                for mod in data:
                    if mod == input.lower():
                        
                        return await ctx.send(embed = discord.Embed(title = mod + " commands", description = "```\n" + "{}{}".format(prefix(self.client, ctx.message), "\n{}".format(prefix(self.client, ctx.message)).join(commands["Name"] for commands in data[mod])) + "\n```", colour = my_colour(ctx)))

                for mod in data:       
                    for command in data[mod]:
                        
                        if command["Name"] == input:

                            if not command["Notes"]:
                                embed = discord.Embed(title = prefix(self.client, ctx.message) + command["Name"], description = f"{command['Description']}\n\n**Syntax**: {command['Syntax'] % prefix(self.client, ctx.message)}\n**Example:** {command['Example'] % prefix(self.client, ctx.message)}", colour = my_colour(ctx))
                            
                            else:
                                embed = discord.Embed(title = prefix(self.client, ctx.message) + command["Name"], description = f"{command['Description']}\n\n**Syntax**: {command['Syntax'] % prefix(self.client, ctx.message)}\n**Example:** {command['Example'] % prefix(self.client, ctx.message)}\n\n{command['Notes'] % prefix(self.client, ctx.message)}", colour = my_colour(ctx))
                            
                            await ctx.send(embed = embed)
                
                await ctx.send(f"No module or command found named `{input}`! Did you mean __{process.extractOne(input, self.list_commands())[0]}__?")
        
        else:
            embed = discord.Embed(title = "Zezak", description = "A highly configurable and flexible multi-purpose bot created in Python.\n\n[Commands](https://carrotguy69.github.io/Zezak/)\n[GitHub](https://www.github.com/carrotguy69/Zezak)\n\n**Modules**:\n__General__\n__Config__", colour = my_colour(ctx))
            await ctx.send(embed = embed)


def setup(client):
    client.add_cog(help(client))