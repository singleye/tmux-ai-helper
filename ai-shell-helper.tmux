#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

MODEL_NAME="llama2:latest"
OLLAMA_SERVER_URL="http://localhost:11434"

tty_dev=$(tmux display-message -p '#{pane_tty}')

#tmux bind-key Q run-shell "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
#tmux bind-key Q command-prompt "split-window -n %1 'OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py %1'"
#tmux bind-key -T copy-mode Q pipe-pane -IO "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
#tmux bind-key Q pipe-pane -IO -t %1 "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py"
#tmux bind-key Q pipe-pane -O "OLLAMA_MODEL_NAME=$MODEL_NAME $CURRENT_DIR/scripts/ai_helper.py > $tty_dev"
#tmux bind-key Q pipe-pane -IO "OLLAMA_MODEL_NAME=$MODEL_NAME /Users/wangq/.virtualenvs/python3/bin/python $CURRENT_DIR/scripts/ai_helper_pt.py"
#tmux bind-key / command-prompt "split-window 'exec %%'"
#tmux bind-key S command-prompt "new-window -n %1 'ssh $1'"
tmux bind-key Q command-prompt "split-window 'exec $CURRENT_DIR/scripts/ai_helper.py $MODEL_NAME %%'"
