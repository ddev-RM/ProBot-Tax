import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")

@bot.command(name="tax")
async def tax(ctx, amount: int):
    result = round(amount/0.95+1)
    em = discord.Embed(
        title="Credit Tax",
        description=f"""
**Your number with out tax : `{amount}`**

**The number with tax : `{result}`**

**The Tax is : `{result-amount}`**
"""
    )
    em.set_footer(
        text=f"requested by {ctx.author}",
        icon_url=ctx.author.avatar
    )
    return await ctx.send(embed=em)

bot.run("MTA4NzQ1ODM1NDk1MzIxMjA4NA.GCm4J_.DBjf-jsl9mJAH6TBdelvnSXEmRRcilq9ZxbDxg")
