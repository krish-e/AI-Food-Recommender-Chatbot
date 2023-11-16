import os
import openai
from dotenv import load_dotenv, find_dotenv
import sys
import csv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

try:
    open("Zomato-mini.csv")
except FileNotFoundError:
    sys.exit("Could not read Zomato-mini.csv")


restaurants = []
# Read file to load all restaurants with necessary features
with open("Zomato-mini.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        restaurants.append({"Name": row["name"], "Rating": row["rate"], "Phone": row["phone"], "Cuisines": row["cuisines"].lower().split(', '), "Cost for 2": row["budget(for_two)"].strip()})


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


context = [{'role': 'system', 'content': f"""
Your name is Jim, an AI friend to the user who helps the user in deciding which restaurant to eat\

You first greet the user, \

then list down ONLY the available cuisines from {restaurants} without repeating any of the cuisine the second time in the list\
and then asks for the minimum preferred rating out of 5.\
and then ask the user if they are on budget.\
If the user is on budget, ask for their budget.\
then print the restaurants in {restaurants} that satisfy the user's preference in table format.

You respond in a conversational friendly style. \
"""}]


print("Initialize conversation by typing something. Type 'exit' to exit the program")
while True:
    prompt = input("You: ")
    if prompt.lower().strip() == "exit":
        sys.exit()

    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})

    print("Food Buddy:", response)
