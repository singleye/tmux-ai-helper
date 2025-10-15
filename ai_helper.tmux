#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LLM="openai"
LLM_SERVER="http://localhost:1234"
MODEL_NAME="qwen3-coder-30b-a3b-instruct"

# prefix + Q to open a command prompt, input your question in the prompt, and then press enter to send the question to the AI server
tmux bind-key Q command-prompt "split-window 'exec $CURRENT_DIR/scripts/ai_helper.py $LLM $LLM_SERVER $MODEL_NAME %%'"
