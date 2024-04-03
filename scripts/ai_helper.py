#!/usr/bin/env python3

import sys
import os
import json
import urllib
from urllib import request

DEFAULT_MODEL_NAME = "llama2:latest"
DEFAULT_OLLAMA_SERVER = "http://localhost:11434"

def get_ai_response(question, ollama_server, model_name):
    data = {
        "model": model_name,
        "prompt": "Help me to generate the linux shell command line to do the following: %s" % question,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    ollama_request_url = f"{ollama_server}/api/generate"
    req = request.Request(ollama_request_url,
                          data=json.dumps(data).encode("utf-8"),
                          headers=headers)
    resp = request.urlopen(req)
    answer = json.loads(resp.read())['response']
    #lines = []
    #for line in response.split('\n'):
    #    lines.append('' + line)
    #answer = '\n'.join(lines)
    return answer

def wait_for_exit():
    print('\nPress Q/q to exit!')
    while sys.stdin.read().lower() != 'q':
        continue

def help_me(question, ollama_server=DEFAULT_OLLAMA_SERVER, model_name=DEFAULT_MODEL_NAME):
    answer = get_ai_response(question, ollama_server, model_name)
    print(answer)
    wait_for_exit()

def main():
    if len(sys.argv) < 4:
        print("Usage: %s <ollama_url> <model_name> <question>" % sys.argv[0])
        wait_for_exit()
        sys.exit(1)
    ollama_server_url = sys.argv[1]
    model_name = sys.argv[2]
    question = ' '.join(sys.argv[3:])
    with open('/tmp/ai_helper.log', 'a') as f:
        f.write(f"question: {question}\n")
    help_me(question, ollama_server_url, model_name)

if __name__ == "__main__":
    main()
