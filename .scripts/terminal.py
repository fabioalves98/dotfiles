#!/usr/bin/python3

from os import system
from sys import argv
from i3ipc import Connection, Event

# Create the Connection object that can be used to send commands and subscribe
# to events.
i3 = Connection()
tree = i3.get_tree()
command = ''
instance = ''

if argv[1] == 'tmux':
    instance = 'floatingTmux'
    command = 'tmux'
elif argv[1] == 'ranger':
    instance = 'floatingRanger'
    command = 'ranger'

create=True
# See if exsists
for container in tree:
    if container.window_instance == instance:
        create=False

if create:
    i3.command('exec urxvt -name ' + instance + ' -e bash -i -c "' + command + '" ')

show=True
# See if shows or hides
focused = tree.find_focused().workspace()
for container in focused:
    if container.window_instance == instance:
        show=False
        # i3.command('[instance=\"' + instance + '\"] move container to workspace 11:Terminal')
        i3.command('[instance=\"' + instance + '\"] move scratchpad')

if show:
    i3.command('[instance=\"' + instance + '\"] move container to workspace current')
    i3.command('[instance=\"' + instance + '\"] focus')