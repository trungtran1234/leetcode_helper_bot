import asyncio
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from app.problems import leetcode_problem_titles
from app.chatgpt_ai.openai import chatgpt_response, approach_response, help_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

random_problem_title = "" #Globally saves problem name for different function uses
@bot.command(name='leetcode', description = 'Provide random leetcode problem from the blind 75 list')
async def leetcode_command(ctx):
    global random_problem_title
    random_problem_title = random.choice(leetcode_problem_titles) #Pick random title from imported titles list (Bline 75)
    bot_response = chatgpt_response(random_problem_title) #Input title name into prompt to generate AI response 
    await ctx.send(bot_response) #Sends AI output on discord
    await ctx.send("Please provide your approach to the problem.")

@bot.command(name='approach')
async def approach_command(ctx, *, approach):
    global random_problem_title #Saved problem name from current leetcode problem (initialized when /leetcode is called)
    problem_name = random_problem_title  # Save the problem name from the /leetcode command
    feedback = approach_response(approach, problem_name) 
    await ctx.send(random_problem_title + feedback)

@bot.command(name='helpme')
async def help_command(ctx):
    global random_problem_title
    problem_name = random_problem_title  # Retrieve problem title from the context
    feedback = help_response(problem_name)
    await ctx.send(random_problem_title + feedback)





