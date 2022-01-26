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


from Yeti_Qeustions import *


client = discord.Client()

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("\033c")
    print("Bot has Successfully been brought to Life")  # will print "bot online" in the console when the bot is online


def Addscore(user, change):

    if change == False:
        with open("ScoreTracker.txt", "a") as file:
            file.write("-" + str(user) + "\n")
    elif change == True:
        with open("ScoreTracker.txt", "a") as file:
            file.write(str(user) + "\n")


@client.command()
async def port(ctx):
    await ctx.send("What is Port " + random.choice(commonPorts) + "?")


# Gives random Question from Yeti_Qeustions
@client.command()
async def askme(ctx):

    QuestionSelection = random.randint(1, (len(Tech_Questions) - 1))
    QuestionSelection = 94
    # If it cant get the qeustion info itll print error
    try:

        QuestionInfo = Tech_Questions[QuestionSelection]["Question"]
        AnswerInfo = Tech_Questions[QuestionSelection]["Answer"]

    except:
        await ctx.send("Error Pulling Question please try agian\n\nError Number: "+ str(QuestionSelection))

    # Prints the question
    await ctx.send(QuestionInfo)

    # Waits for response
    msg = await client.wait_for("message", check=check)

    UserAnswer = msg.content
    UserAnswer = str(UserAnswer).upper()

    if UserAnswer == AnswerInfo and msg.author == ctx.author:
        await ctx.send(f"Correct!")

    elif msg.author == ctx.author and UserAnswer != AnswerInfo:
        await ctx.send(f"Incorrect, " + AnswerInfo + " was the correct answer")

    


@client.command()
async def ListAll(ctx):
    if str(ctx.author.id) == "600010784453558331":
        for x in range(len(Tech_Questions)):
            time.sleep(2)
            await ctx.send("NUMBER " + str(x))
            await ctx.send(Tech_Questions[x]["Question"])
            await ctx.send(Tech_Questions[x]["Answer"])
            await ctx.send(".\n\n.")


@client.command()
async def contributers(ctx):
    await ctx.send("Contributers:\n\nMartin V. Phillips")


if __name__ == "__main__":
    try:
        client.run("OTMzNTQwMjU2MDY0NjIyNjIy.YejBHQ.CyvC-IuOO8Kxb87d9_vV2Hpg7VU")
    except:
        print("Error, Incorrect Discord bot Token?")
