#!/usr/bin/env python3

#import requests
import sys
import os
import json
import urllib
from urllib import request
#import ollama

ENV_VAR_MODEL_NAME = "OLLAMA_MODEL_NAME"
DEFAULT_MODEL_NAME = "llama2:latest"
OLLAMA_SERVER_URL = "http://localhost:11434/api/generate"


def get_ai_response(model_name, message):
    data = {
        "model": model_name,
        "prompt": """Help me to generate a command line for linux shell to do the following: %s

Output format: each line starts with '#'
        """ % message,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    req = request.Request(OLLAMA_SERVER_URL,
                          data=json.dumps(data).encode("utf-8"),
                          headers=headers)
    resp = request.urlopen(req)
    response = json.loads(resp.read())['response']
    lines = []
    for line in response.split('\n'):
        lines.append(' #> ' + line)
    answer = '\n'.join(lines)
    return answer

def help_me(model_name):
    #question = input("\nAI helper(%s) >" % model_name)
    question = input(" #: ")
    answer = get_ai_response(model_name, question)
    print(answer)

def main():
    model_name = os.environ.get(ENV_VAR_MODEL_NAME, DEFAULT_MODEL_NAME)
    help_me(model_name)

if __name__ == "__main__":
    main()
