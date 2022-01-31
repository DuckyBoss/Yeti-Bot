# import curses
import discord
import os, sys
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import random
import time
import socket
from Network_Questions import *


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
    while True:
        msg = await client.wait_for("message", check=check)

        UserAnswer = msg.content
        UserAnswer = str(UserAnswer).upper()

        if UserAnswer == AnswerInfo and msg.author == ctx.author:
            await ctx.send("Correct!")
            break
        
        elif msg.author == ctx.author and UserAnswer != AnswerInfo and len(UserAnswer) > 5:
            await ctx.send(f"Imma ignore that")

        elif msg.author == ctx.author and UserAnswer != AnswerInfo:
            await ctx.send(f"Incorrect, {AnswerInfo} was the correct answer")
            break
        
            







@client.command()
async def whoami(ctx):
    if str(ctx.author.id) == "600010784453558331":
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        
        await ctx.send(f"IP address: {local_ip[2:]}\nHost Name: {host_name}\nQuestions: {len(Tech_Questions) - 1}")
    else:
        print("")
        
            
            
@client.command()
async def contributers(ctx):
    await ctx.send("Contributers:\n\nMartin V. Phillips")





@client.event
async def on_message(message):

    if "Yeti" not in str(message.author):
        
        #Checks for the words WHAT and PORT
        if "WHAT" in str(message.content).upper() and "PORT" in str(message.content).upper():

            #checks for Port number and gives port name
            for DictRange in range(len(commonPorts)):
            
                if str(commonPorts[DictRange]["PortNumber"]) in str(message.content).upper():

                    await message.channel.send(f"{commonPorts[DictRange]['PortNameAcronym']}: {commonPorts[DictRange]['PortName']} ")
            

            for DictRange in range(len(commonPorts)):
            
                if str(commonPorts[DictRange]["PortNameAcronym"]) in str(message.content).upper()  or  str(commonPorts[DictRange]["PortName"]) in str(message.content):

                    await message.channel.send(f"Port #{commonPorts[DictRange]['PortNumber']} ")

    

    #makes ?commands work (dont know why, but leave it be)
    await client.process_commands(message)







if __name__ == "__main__":
    try:
        client.run("BOT_TOKEN")
    except:
        print("Error, Incorrect Discord bot Token?")
