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
async def r(ctx, *args):
  try: 
    x = re.search("\d+d\d+$", args[0])
    
    index = 1
    secondArg = index < len(args)

    add = 0
    subtract = 0

    if secondArg:
      subtract = re.search("-\d+$", args[1])
      add = re.search("\+\d+$", args[1])

    if x:
      roll = x.string
      rollSplit = re.split("d", roll)
      numberOfDie = int(rollSplit[0])
      numberOfSides = int(rollSplit[1])
      outcome = "= ("
      total = 0

      if numberOfDie > 10:
        await ctx.send("Woah there lad, calm down. I can only roll 10 dice at a time.")
        await ctx.message.add_reaction('🚫')
      elif numberOfSides > 100:
        await ctx.send("Steady on fella, I can't roll any higher than a d100")
        await ctx.message.add_reaction('🚫')
      else:
        for x in range(numberOfDie):
          dieResult = random.randint(1, numberOfSides)
          total = total + dieResult
          if x == numberOfDie-1:
            outcome = outcome + " " +str(dieResult)+ " )"
          else:
            outcome = outcome + " " + str(dieResult) + " +"


        if subtract:
          y = args[1]
          num = int(y[1:])

          outcome = outcome + " - " + str(num)
          total = total - num

        if add:
          y = args[1]
          num = int(y[1:])

          outcome = outcome + " + " + str(num)
          total = total + num
  

        await ctx.message.add_reaction('🎲')

        if numberOfDie > 1 :
          await ctx.send("rolling "+ str(numberOfDie) + " x " + "d" + str(numberOfSides) + "...\n"+outcome+"\Total = " + str(total))
        elif subtract or add:
          await ctx.send("rolling "+ str(numberOfDie) + " x " + "d" + str(numberOfSides) + "...\n"+outcome+"\nTotal = " + str(total))  
        else:
          await ctx.send("rolling "+ str(numberOfDie) + " x " + "d" + str(numberOfSides) + "...\n"+outcome)

    elif args[0] == "help":
      await ctx.send(".r - specify the number of die and the type of die you would like to roll. You can roll up to 10 die and you can roll from a 1 sided die to a 100 sided die. You can also add a modifier to add or subtract from the outcome. Note: only the first modifier added will be taken into account.\n\nSyntax:\n.r <Number Of Die>d<Number Of Sides> +/-<Modifier Value>[Modifier is optional]\n\nExample:\n'.r 2d6 +4' - this will roll 2 six sided die and add 4 onto the total.")
      await ctx.message.add_reaction('❓')
    else:
      await ctx.send("Invalid syntax. Use '.r help' for info on how to use roll command")
      await ctx.message.add_reaction('🚫')
  except:
    await ctx.send("An error has occurred. Use '.r help' for info on how to use roll command")
    await ctx.message.add_reaction('🚫')




keep_alive()    
bot.run(os.environ['botToken'])