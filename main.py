import os
import discord
import re
import random

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} is online, time to graft.'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/r '):

    x = re.search("\/r \d+d\d+", message.content)
    if x:
      y = re.split(" ", message.content)
      roll = y[1]
      rollSplit = re.split("d", roll)
      numberOfDie = int(rollSplit[0])
      numberOfSides = int(rollSplit[1])
      outcome = "="
      total = 0

      if numberOfDie > 10:
        await message.channel.send("Woah there lad, calm down. I can only roll 10 dice at a time.")
      elif numberOfSides > 100:
        await message.channel.send("Steady on fella, I can't roll any higher than a d100")
      else:
        await message.channel.send("rolling "+ str(numberOfDie) + " x " + "d" + str(numberOfSides) + "...")

        for x in range(numberOfDie):
          dieResult = random.randint(1, numberOfSides)
          total = total + dieResult
          if x == numberOfDie-1:
            outcome = outcome + " " +str(dieResult)
          else:
            outcome = outcome + " " + str(dieResult) + " +"

        await message.channel.send(outcome)
        
        if numberOfDie > 1 :
          await message.channel.send("total = " + str(total))
    else:
      await message.channel.send("Invalid syntax. Use /help for info on how to use DezzieBot")


  if message.content.startswith("/help"):
    await message.channel.send("Commands:")
    await message.channel.send("/r - this will roll a chosen amount of dice with a chosen amount of sides.")
    await message.channel.send("Example:  '/r 2d6'  - this will roll two six-sided die")
    
client.run(os.environ['botToken'])
