import json
import os
import random
import socket
import sys
import time

import urllib.request
import discord
import discord.ext
from discord.ext import commands, tasks
from discord.ext.commands import CheckFailure, check, has_permissions
from discord.utils import get
from pyparsing import common_html_entity

from Network_Questions import *
from CommonPorts import *

client = discord.Client()

client = commands.Bot(command_prefix="?")


# Who is hosting the bot (Recieves DM for potentially sensitive info)
HostDiscordID = 600010784453558331

#What channel the bot messages on startup
StartUpChannelID = 903416175726301235


@client.event
async def on_ready():
    print("\033c")
    channel = client.get_channel(StartUpChannelID)
    await channel.send("<@600010784453558331> The Bot is Awake")
    # will print "bot online" in the console when the bot is online
    print("THE BOT IS ALIVE!!!!!")


# Gives random Question from Yeti_Qeustions
@client.command()
async def askme(ctx):

    QuestionSelection = random.randint(1, (len(Practice_Questions) - 1))

    # If it cant get the qeustion info itll print error
    try:

        QuestionInfo = Practice_Questions[QuestionSelection]["Question"]
        AnswerInfo = Practice_Questions[QuestionSelection]["Answer"]

    except:
        await ctx.send("Error Pulling Question please try agian\n\nError Number: " + str(QuestionSelection))

    # Prints the question
    await ctx.send(f"{QuestionSelection}.) {QuestionInfo}")

    # Waits for response
    while True:
        msg = await client.wait_for("message", check=check)

        UserAnswer = str(msg.content).upper()

        if UserAnswer == AnswerInfo and msg.author == ctx.author:
            await ctx.send("Correct!")
            break

        elif msg.author == ctx.author and UserAnswer != AnswerInfo:
            await ctx.send(f"Incorrect, {AnswerInfo} was the correct answer")
            break

        else:
            pass


@client.command()
async def whoami(ctx):
    if str(ctx.author.id) == "600010784453558331":
        
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        Public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        Version = f"{int(len(Practice_Questions) - 1)}.xxx.xxx.xxx"
        

        user = client.get_user(HostDiscordID)
        await user.send(f"Public IP address: {Public_ip}\nLocal IP address: {local_ip[2:]}\nHost Name: {host_name}\nVersion: {Version}")

    else:
        print("")


@client.command()
async def contributers(ctx):
    await ctx.send("Contributers:\n\nMartin V. Phillips")


@client.event
async def on_message(message):

    # Makes sure it doesnt repeat and loop itself, "Yeti" wont stay with bot username change.
    if "Yeti" not in str(message.author):
        
        UserMessage = str(message.content).upper()

        # Checks for the words WHAT and PORT
        if "WHAT" in UserMessage and "PORT" in UserMessage:

            # checks for Port number and gives port name
            for i in range(len(CommonPorts)):

                if str(CommonPorts[i]["PortNumber"]) in UserMessage:

                    await message.channel.send(f"{CommonPorts[i]['PortNameAcronym']}: {CommonPorts[i]['PortName']} ")

            for i in range(len(CommonPorts)):

                if CommonPorts[i]["PortNameAcronym"] in UserMessage:

                    await message.channel.send(f"Port #{CommonPorts[i]['PortNumber']} ")


        # Prints the description of the port name
        elif "WHAT" in UserMessage:

            for DictRange in range(len(CommonPorts)):

                if CommonPorts[DictRange]["PortNameAcronym"] in UserMessage:

                    await message.channel.send(f"{CommonPorts[DictRange]['PortUse']}")



    # makes ?commands work (dont know why, but leave it be)
    await client.process_commands(message)


if __name__ == "__main__":
    try:
        client.run("OTMzNTQwMjU2MDY0NjIyNjIy.YejBHQ._L-slMt95t798RYrW_kA4HTR0W0")
    except:
        print("Error, Incorrect Discord bot Token?")
