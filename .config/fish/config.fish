set fish_greeting ""

set -gx PATH /home/adam/scripts/bin /home/adam/.npm-global/bin $PATH
set -gx EDITOR kak
set -gx VISUAL kak

set -gx TERM alacritty
set -gx TERMCMD alacritty
set -gx FILEMANAGER ranger

# set -gx QT_QPA_PLATFORM xcb
# set -gx QT_WAYLAND_DISABLE_WINDOWDECORATION 1
# set -gx XDG_SESSION_TYPE wayland


fish_vi_key_bindings

alias f 'ranger-cd'

alias gplom 'git pull origin master'
alias gploa 'git pull origin --all'
alias gpsom 'git push origin master'
alias gpsoa 'git push origin --all'
alias gcl 'git clone'

alias mke 'sudo make clean install'

alias i 'yay -Sy '
alias ii 'yay -Syu'
alias s 'yay -Ss'
alias l 'yay -Q'
alias u 'yay -Ru'
alias uu 'yay -Rdd'

set -gx FZF_DEFAULT_COMMAND "fd --absolute-path --no-ignore-vcs --type file --color=always --follow  --exclude .trash --search-path /home/adam --search-path /home/adam/.config"
set -gx FZF_DEFAULT_OPTS "--ansi"
set -gx FZF_CTRL_T_COMMAND "$FZF_DEFAULT_COMMAND"

#set FZF_DEFAULT_COMMAND 'fd --absolute-path --color=always --follow'
