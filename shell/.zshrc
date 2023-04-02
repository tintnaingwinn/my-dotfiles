ZSH=$HOME/.oh-my-zsh

ZSH_CUSTOM=$HOME/.dotfiles/misc/oh-my-zsh-custom

ZSH_THEME="amuse"

# Hide username in prompt
DEFAULT_USER=`whoami`

plugins=(
git
brew
macos
zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh


# Load the shell dotfiles, and then some:
# * ~/.dotfiles-custom can be used for other settings you don’t want to commit.
for file in ~/.dotfiles/shell/.{exports,aliases,functions}; do
	[ -r "$file" ] && [ -f "$file" ] && source "$file"
done

for file in ~/.dotfiles-custom/shell/.{exports,aliases,functions,zshrc}; do
	[ -r "$file" ] && [ -f "$file" ] && source "$file"
done
unset file

# Alias hub to git
eval "$(hub alias -s)"

# Import ssh keys in keychain
ssh-add -A 2>/dev/null;

# Setup xdebug
export XDEBUG_CONFIG="idekey=VSCODE"

# Enable autosuggestions
source ~/.dotfiles/misc/oh-my-zsh-custom/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh


# Extra paths

# PHPMON
export PATH=$HOME/bin:~/.config/phpmon/bin:$PATH

# GOLANG
export PATH="$PATH":"$HOME/go/bin"

# FLUTTER
export PATH=~/development/flutter/bin:$PATH
export PATH="$PATH":"$HOME/.pub-cache/bin"

# JAVA
export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"

# Android Studio
export PATH=~/Library/Android/sdk/tools:$PATH
export PATH=~/Library/Android/sdk/platform-tools:$PATH

# Composer
export PATH=$PATH:~/.composer/vendor/bin

# Homebrew
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/opt/homebrew/sbin:$PATH"
export PATH=/Users/Shared/DBngin/postgresql/14.3/bin:$PATH

# NVM
export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

## [Completion] 
## Completion scripts setup. Remove the following line to uninstall
[[ -f /Users/tintnaingwin/.dart-cli-completion/zsh-config.zsh ]] && . /Users/tintnaingwin/.dart-cli-completion/zsh-config.zsh || true
## [/Completion]

