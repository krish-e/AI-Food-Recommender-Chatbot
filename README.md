# Food-Buddy(on steroids)

## Table of Contents
1. [Overview](#overview)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Important Notes](#important-notes)
5. [Acknowledgments](#acknowledgments)

## Overview

This project utilizes a CSV file named "zomato-mini.csv" containing information about various restaurants. The program performs the following operations in sequence:

1. **Load CSV Data:**
   - Opens the "zomato-mini.csv" file and loads its content into a dictionary.

2. **User Interaction with ChatGPT:**
   - Utilizes the ChatGPT API to engage in a conversation with the user.
   - Gathers user preferences regarding restaurants (cuisine budget, and a lot more based on user input).

3. **Filter Restaurants:**
   - Filters the loaded restaurant data based on the user's preferences.

4. **Display Matching Restaurants:**
   - Displays details of the restaurants that match the user's preferences.

## Setup

1. **CSV File:**
   - Ensure the "zomato-mini.csv" file is present in the project directory and contains the required restaurant data.

2. **ChatGPT API Key:**
   - Obtain a ChatGPT API key from OpenAI and replace the placeholder in the ".env" file with your actual key. (As of 1-Nov-'23, the API has free-trial.)

3. **Dependencies:**
   - Make sure to install the necessary Python libraries by running the following command:
     ```bash
     pip install openai
     ```

## Usage

1. **Run the Program:**
   - Execute the main program, e.g., `python run.py`.

2. **Follow the Prompts:**
   - Once executed, the program will guide you through a conversation using ChatGPT in the Command Line Interface to gather your restaurant preferences.

3. **View Matching Restaurants:**
   - Once the user preferences are collected, the program will display details of the matching restaurants.

## Important Notes

- Ensure an internet connection for ChatGPT API calls.
- Keep your ChatGPT API key secure and do not share it publicly.
- Review and update the code as needed, adapting it to any changes in the CSV structure or project requirements.

## Acknowledgments

- Thanks to OpenAI for the ChatGPT API.
