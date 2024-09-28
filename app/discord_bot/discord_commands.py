import asyncio
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from app.problems import leetcode_problem_titles
from app.chatgpt_ai.openai import leetcode_response, approach_response, help_response

load_dotenv()
    
discord_token = os.getenv('DISCORD_TOKEN') #Load Discord API token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

random_problem_title = "" #Globally saves problem name for different function uses


@bot.tree.command(name="leetcode", description="Generates a random Blind 75 problem for you to solve")
async def leetcode_command(interaction: discord.Interaction):
    await interaction.response.send_message("Generating LeetCode problem...")  # Acknowledge command immediately
    global random_problem_title
    random_problem_title = random.choice(leetcode_problem_titles)  # Pick random title from imported titles list (Blind 75)
    bot_response = leetcode_response(random_problem_title)  # Input title name into prompt to generate AI response
    await interaction.followup.send(bot_response)  # Sends AI output on discord
    await interaction.followup.send("Please provide your approach to the problem.")


@bot.tree.command(name="approach", description="Give your approach to the problem")
async def approach_command(interaction: discord.Interaction, approach: str):
    await interaction.response.send_message("Generating feedback for:\n" + approach)  # Acknowledge command immediately
    global random_problem_title  # Saved problem name from current leetcode problem (initialized when /leetcode is called)
    problem_name = random_problem_title  # Save the problem name from the /leetcode command
    feedback = approach_response(approach, problem_name)
    await interaction.followup.send(random_problem_title + feedback)


@bot.tree.command(name="helpme", description="Generates you an optimal approach to the problem")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message("Generating solution...")  # Acknowledge command immediately
    global random_problem_title
    problem_name = random_problem_title  # Retrieve problem title from the context
    feedback = help_response(problem_name)
    await interaction.followup.send(random_problem_title + feedback)

