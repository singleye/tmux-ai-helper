#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#MODEL_NAME="llama2:latest"
MODEL_NAME="llama2-Chinese:13b"


#tmux bind-key T run-shell "$CURRENT_DIR/scripts/ai_shell_helper.sh $OLLAMA_MODEL_NAME"
#tmux bind-key Q run-shell "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
#tmux bind-key Q command-prompt "split-window -n %1 'OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py %1'"
#tmux bind-key Q pipe-pane -IO -t %1 "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
tmux bind-key -T copy-mode Q pipe-pane -IO "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
