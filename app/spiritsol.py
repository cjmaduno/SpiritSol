import os
from typing import List
import openai
import argparse
import re

MAX_INPUT_LENGTH = 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_length(user_input):
        generate_solution_snippet(user_input)
        generate_charities(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )


def validate_length(prompt: str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH


def generate_charities(prompt: str) -> List[str]:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate names of charities that are related to {prompt}: "
    print(enriched_prompt)

    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=300
    )

    # Extract output text.
    charities_text: str = response["choices"][0]["text"]

    # Strip whitespace.
    charities_text = charities_text.strip()
    charities_array = re.split(",|\n|;|-", charities_text)
    charities_array = [k.lower().strip() for k in charities_array]
    charities_array = [k for k in charities_array if len(k) > 0]

    print(f"Charities: {charities_array}")
    return charities_array


def generate_solution_snippet(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate a suggestion for how to integrate spirtuality in a {prompt} business: "
    print(enriched_prompt)

    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=300
    )

    # Extract output text.
    solution_text: str = response["choices"][0]["text"]

    # Strip whitespace.
    solution_text = solution_text.strip()

    # Add ... to truncated statements.
    last_char = solution_text[-1]
    if last_char not in {".", "!", "?"}:
        solution_text += "..."

    print(f"Snippet: {solution_text}")
    return solution_text


if __name__ == "__main__":
    main()
