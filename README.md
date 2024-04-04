# Tmux AI helper

This is a AI helper to answer questions about linux shell usage for tmux user.

![demo](https://github.com/singleye/tmux-ai-helper/blob/main/demo.gif)

# Installation

## Install with TPM

This is a tmux plugin, you can install it by using [tpm](https://github.com/tmux-plugins/tpm)

```
set -g @plugin 'singleye/tmux-ai-helper'
```

Then press `prefix + I` to install the plugin.

## Manual installation

Clone this repository or copy it to your tmux plugin directory:

```
git clone https://github.com/singleye/tmux-ai-helper.git ~/.tmux/plugins/tmux-ai-helper
```

Add the following line to your `.tmux.conf`:

```
run-shell ~/.tmux/plugins/tmux-ai-helper/ai_helper.tmux
```

# Usage

Before using this plugin, install [ollama](https://github.com/ollama/ollama) first. Then install the 'llama2:latest' model which is the default model of this plugin.

Press `prefix + Q` to open a command prompt, input your question in the prompt, and then press enter to send the question to the AI server

# Configuration

## Change the key binding

You can change the key binding by changing the following line to your `ai_helper.tmux`:

```
tmux bind-key Q command-prompt "split-window 'exec $CURRENT_DIR/scripts/ai_helper.py $OLLAMA_SERVER $MODEL_NAME %%'"
```

## Change the ollama server and model

You can change the ollama server URL and model name changing the following lines to your `ai_helper.tmux`:

```
OLLAMA_SERVER="http://localhost:11434"
MODEL_NAME="llama2:latest"
```

# Known issue

1. Input a question mark '?' has to be escaped, e.g. "how to replace string in file\?"

Anyone knows how to fix this issue?

# Support

Drop me an email at <singleye512@gmail.com>
