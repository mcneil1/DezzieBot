import os
import discord
import re
import random
from keep_alive import keep_alive
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=os.environ['prefix'], intents=intents)

@bot.event
async def on_ready():
  print("Dezzie is online, time to graft.")
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Grafting"))

@bot.command()
async def r(ctx, arg):
    x = re.search("\d+d\d+", arg)
    if x:
      roll = arg
      rollSplit = re.split("d", roll)
      numberOfDie = int(rollSplit[0])
      numberOfSides = int(rollSplit[1])
      outcome = "="
      total = 0

      if numberOfDie > 10:
        await ctx.send("Woah there lad, calm down. I can only roll 10 dice at a time.")
      elif numberOfSides > 100:
        await ctx.send("Steady on fella, I can't roll any higher than a d100")
      else:
        await ctx.send("rolling "+ str(numberOfDie) + " x " + "d" + str(numberOfSides) + "...")

        for x in range(numberOfDie):
          dieResult = random.randint(1, numberOfSides)
          total = total + dieResult
          if x == numberOfDie-1:
            outcome = outcome + " " +str(dieResult)
          else:
            outcome = outcome + " " + str(dieResult) + " +"

        await ctx.send(outcome)
        
        if numberOfDie > 1 :
          await ctx.send("total = " + str(total))
    else:
      await ctx.send("Invalid syntax. Use $help for info on how to use DezzieBot")

keep_alive()    
bot.run(os.environ['botToken'])
