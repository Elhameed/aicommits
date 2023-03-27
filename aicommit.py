#!/usr/bin/python3
import os
import openai
import subprocess

# Read the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Check if the API key is set
if openai.api_key is None:
    print("ERROR: Please set your OpenAI API key as an environment variable named 'OPENAI_API_KEY'")
    exit(1)

model_engine = "text-davinci-003"  # Choose the GPT-3 model you want to use

# Define the input data
diff = subprocess.check_output(["git", "diff", "--cached"]).decode('utf-8')

while True:
    # Generate the commit message
    prompt = f"Generate a commit message for the following changes:\n{diff}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,  # Adjust the max tokens and other parameters as needed
        temperature=0.5,
        n=1,
        stop=None
    )

    generated_text = response.choices[0].text.strip()

    # Modify the commit message and present it to the user
    message = generated_text.replace("Commit message:", "").strip()
    print(f"Generated commit message:\n{message}")
    user_input = input("Accept commit message? (y/n/e): ")

    # Commit the changes or regenerate the message
    if user_input.lower() == "y":
        subprocess.run(["git", "commit", "-m", message])
        print("Changes committed!")
        break
    elif user_input.lower() == "e":
        edited_text = input("Enter edited commit message: ")
        subprocess.run(["git", "commit", "-m", edited_text])
        print("Changes committed!")
        break
    else:
        print("Regenerating commit message...")
