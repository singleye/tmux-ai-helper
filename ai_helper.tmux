#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OLLAMA_SERVER="http://localhost:11434"
MODEL_NAME="llama2:latest"

# prefix + Q to open a command prompt, input your question in the prompt, and then press enter to send the question to the AI server
tmux bind-key Q command-prompt "split-window 'exec $CURRENT_DIR/scripts/ai_helper.py $OLLAMA_SERVER $MODEL_NAME %%'"
