from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY') #Load OpenAI API key

def leetcode_response(problem_title):
    prompt=f"Generate the title, difficulty, description, test case, constraint, and LeetCode link for the generated LeetCode problem: {problem_title}" #Prompt to give details about selected problem
    response = openai.Completion.create( #Generating AI response
        model='text-davinci-003', #OpenAi text completion model
        prompt=prompt, #Give it a prompt
        temperature=1, #Randomness of the model
        max_tokens=200 #Max token it can use for the generated response
    )
    return response.choices[0].text

def approach_response(approach, problem_name):
    prompt=f"Here is my approach to the LeetCode problem {problem_name}: {approach}. Is this an optimal approach to solving the specific LeetCode problem {problem_name}?" #Prompt to see if inputted approach is optimal
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )
    return response.choices[0].text

def help_response(problem_name):
    prompt=f"Give me the optimal approach to the LeetCode problem: {problem_name}" #Prompt to give approach to problem when user is stuck
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )
    return response.choices[0].text
