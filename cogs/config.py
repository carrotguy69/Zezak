import discord, os
from fuzzywuzzy import process, fuzz
from main import dir_, prefix, clean, id_
from discord.ext import commands

class config(commands.Cog):
    def __init__(self, client):
        self.client = client


    permit_description = ""

    @commands.has_guild_permissions(administrator = True)
    @commands.command()
    async def permit(self, ctx, group, perm = None):
        """
        **Description:** Allow a user or role to use mod/admin commands.
        **Syntax:** `%spermit {user | role} {permission}`
        **Example:** `%spermit @austin zezak.ban`
        
        Use `%spermit help` to see a list of permissions.
        """ %((str(prefix(self.client, ctx.message))), (str(prefix(self.client, ctx.message))), (str(prefix(self.client, ctx.message))))

        if group == "help":
            
            dir_(1)
            with open("Permissions", "r+") as f: 
                return await ctx.reply(f.read(), mention_author = False)

        if group:
            a = [m.name for m in ctx.guild.members]
            result = process.extractOne(group, a)
            
            if fuzz.ratio(group, result) > 90:
                obj = result
            
            else:    
                result = process.extractOne(group, ctx.guild.roles)
                
                if fuzz.ratio(group, result) > 90:
                    obj = result
                
                else:
                    result = process.extractOne(group, ctx.guild.text_channels)
                    
                    if fuzz.ratio(group, result) > 90:
                        obj = result
                    
                    else:
                        obj = id_(clean(group), ctx)

                        if obj == None:
                            return print("Member not found!")
            
            await ctx.send(obj.mention)
    
    # @permit.error
    # async def permit_error(self, ctx, e):
    #     if isinstance(e, commands.MissingRequiredArgument):
            
    #         dir_(1)
    #         with open("Permissions", "r+") as f:
    #             return await ctx.reply(f.read(), mention_author = False)

def setup(client):
    client.add_cog(config(client))