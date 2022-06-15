from discord.ext import commands
import replies
import random

class Pekogacha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10.0, commands.BucketType.guild)
    async def pekogacha(self, ctx):
        await ctx.message.reply(random.choice(replies.handling.gacha))

def setup(bot):
    bot.add_cog(Pekogacha(bot))