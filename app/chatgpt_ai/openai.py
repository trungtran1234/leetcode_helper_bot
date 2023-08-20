from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

def chatgpt_response(problem_title):
    prompt=f"Generate the title, difficulty, description, test case, constraint, and link for the LeetCode problem: {problem_title}"
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )
    return response.choices[0].text

def approach_response(approach, problem_name):
    prompt=f"Is this an optimal approach to solving the specific LeetCode problem {problem_name}: {approach}"
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )
    return response.choices[0].text

def help_response(problem_name):
    prompt=f"Give me a hint on how to approach the LeetCode problem: {problem_name}"
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=1,
        max_tokens=200
    )
    return response.choices[0].text
