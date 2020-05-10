set fish_greeting ""

set -gx PATH /home/adam/scripts/bin /snap/bin $PATH
set -U EDITOR kak
set -U VISUAL kak

set TERM alacritty
set FILEMANAGER ranger

fish_vi_key_bindings

alias f 'ranger'

alias gplom 'git pull origin master'
alias gpsom 'git push origin master'
alias gcl 'git clone'

alias mke 'sudo make clean install'

alias i 'sudo apt install '
alias ii 'sudo apt update && sudo apt upgrade'
alias s 'sudo apt search'
alias l 'sudo apt show'
alias u 'sudo apt remove'
alias uu 'sudo apt autoremove --purge'

set FZF_DEFAULT_COMMAND 'fdfind --absolute-path --no-ignore-vcs --type file --color=always --follow  --exclude .trash --search-path /home/adam --search-path /home/adam/.config'
#set FZF_DEFAULT_COMMAND 'fd --absolute-path --color=always --follow'
set FZF_DEFAULT_OPTS "--ansi"
set FZF_CTRL_T_COMMAND "$FZF_DEFAULT_COMMAND"
