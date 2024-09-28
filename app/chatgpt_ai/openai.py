from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# Create the OpenAI client with the API key

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))  # Load OpenAI API key

def leetcode_response(problem_title):
    prompt = f"Generate the title, difficulty, description, test case, constraint, and LeetCode link for the generated LeetCode problem: {problem_title}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or 'gpt-4' if available
        messages=[
            {"role": "system", "content": "You are an assistant that generates detailed descriptions for LeetCode problems."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
def approach_response(approach, problem_name):
    prompt = f"Here is my approach to the LeetCode problem {problem_name}: {approach}. Is this an optimal approach to solving the specific LeetCode problem {problem_name}?"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or 'gpt-4' if available
        messages=[
            {"role": "system", "content": "You are an assistant that evaluates user-provided solutions to coding problems."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()

def help_response(problem_name):
    prompt = f"Give me the optimal approach to the LeetCode problem: {problem_name}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or 'gpt-4' if available
        messages=[
            {"role": "system", "content": "You are an assistant that provides optimal solutions to LeetCode problems."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()
