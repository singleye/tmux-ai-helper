#!/usr/bin/env python3

"""
Ask the AI model to generate the command line interface for the given question.
"""

import sys
import json
import termios
import tty
from urllib import request


DEFAULT_MODEL_NAME = "llama2:latest"
DEFAULT_OLLAMA_SERVER = "http://localhost:11434"

def query_ollama(question, ollama_server, model_name):
    """Query the Ollama server to get the response for the given question.

    Using streaming API to get the response in chunks.

    Args:
        question (str): The question to ask the AI model.
        ollama_server (str): The Ollama server URL, e.g. http://localhost:11434.
        model_name (str): The model name to use.
    """

    ollama_request_url = f"{ollama_server}/api/generate"
    data = {
        "model": model_name,
        "prompt": ("You are an expert programmer that writes simple, concise code and "
                   f"explanations. Please give answer to following question: {question}"),
        "stream": True
    }
    headers = {
        "Content-Type": "application/json"
    }
    req = request.Request(ollama_request_url,
                          data=json.dumps(data).encode("utf-8"),
                          headers=headers)
    with request.urlopen(req) as resp:
        for line in resp:
            data = json.loads(line.decode('utf-8'))
            if data['done']:
                break
            yield data['response']

def wait_for_exit(exit_value=0, prompt="\n\nPress Q/q to quit! ", quit_key='q'):
    """Wait for the user to press the quit key to exit the program.

    Need to set the terminal to raw mode to read the key press.

    Args:
        exit_value (int): The exit value to use when exiting the program.
        prompt (str): The prompt message to display.
        quit_key (str): The key to press to exit the program.
    """

    print(prompt, end="")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            read_char_count = 1
            char = sys.stdin.read(read_char_count)
            if char.lower() == quit_key.lower():
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    sys.exit(exit_value)

def ask_ai(question, ollama_server=DEFAULT_OLLAMA_SERVER, model_name=DEFAULT_MODEL_NAME):
    """
    Ask the AI model to generate the command line interface for the given question.

    Args:
        question (str): The question to ask the AI model.
        ollama_server (str): The Ollama server URL.
        model_name (str): The model name to use.
    """
    for answer in query_ollama(question, ollama_server, model_name):
        print(answer, end='', flush=True)

def main():
    """
    Main function.
    """

    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <ollama_url> <model_name> <question>")
        wait_for_exit(exit_value=1)

    ollama_server_url = sys.argv[1]
    model_name = sys.argv[2]
    question = ' '.join(sys.argv[3:])
    ask_ai(question, ollama_server_url, model_name)
    wait_for_exit(exit_value=0)


if __name__ == "__main__":
    main()
