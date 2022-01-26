# import curses
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import random
import time


from Yeti_Network_Questions import *


client = discord.Client()

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("\033c")
    channel = client.get_channel(903416175726301235)
    await channel.send("<@600010784453558331> The Bot is Awake")
    print("THE BOT IS ALIVE!!!!!")  # will print "bot online" in the console when the bot is online

    
#Not finished and will likely be scrapped
#Leaderboard, add username if question correct. Then count amount of times username was posted. (Going to be repaced with JSON)
def Addscore(user, change):

    if change == False:
        with open("ScoreTracker.txt", "a") as file:
            file.write(f"- {user} \n")
    elif change == True:
        with open("ScoreTracker.txt", "a") as file:
            file.write(f"{user} \n")


@client.command()
async def port(ctx):
    await ctx.send("What is Port " + random.choice(commonPorts) + "?")


# Gives random Question from Yeti_Qeustions
@client.command()
async def askme(ctx):

    QuestionSelection = random.randint(1, (len(Tech_Questions) - 1))

    # If it cant get the qeustion info itll print error
    try:

        QuestionInfo = Tech_Questions[QuestionSelection]["Question"]
        AnswerInfo = Tech_Questions[QuestionSelection]["Answer"]

    except:
        await ctx.send("Error Pulling Question please try agian\n\nError Number: "+ str(QuestionSelection))

    # Prints the question
    await ctx.send(f"{QuestionSelection}.) {QuestionInfo}")

    # Waits for response
    msg = await client.wait_for("message", check=check)

    UserAnswer = msg.content
    UserAnswer = str(UserAnswer).upper()

    if UserAnswer == AnswerInfo and msg.author == ctx.author:
        await ctx.send("Correct!")

    elif msg.author == ctx.author and UserAnswer != AnswerInfo:
        await ctx.send(f"Incorrect, {AnswerInfo} was the correct answer")

    


@client.command()
async def ListAll(ctx):
    if str(ctx.author.id) == "600010784453558331":
        for x in range(len(Tech_Questions)):
            time.sleep(2)
            await ctx.send(f"NUMBER {x}")
            await ctx.send(Tech_Questions[x]["Question"])
            await ctx.send(Tech_Questions[x]["Answer"])
            await ctx.send(".\n\n.")


@client.command()
async def contributers(ctx):
    await ctx.send("Contributers:\n\nMartin V. Phillips")


if __name__ == "__main__":
    try:
        client.run("BOT_TOKEN")
    except:
        print("Error, Incorrect Discord bot Token?")
