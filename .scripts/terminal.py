#!/usr/bin/python3
import time
from sys import argv
from i3ipc import Connection, Event

# Create the Connection object that can be used to send commands and subscribe
# to events.
i3 = Connection()
tree = i3.get_tree()
command = ''
instance = ''
resolution = ''

if argv[1] == 'tmux':
    instance = 'floatingTmux'
    command = 'tmux'
    resolution = '1000px 600px'
elif argv[1] == 'ranger':
    instance = 'floatingRanger'
    command = 'ranger'
    resolution = '1280px 720px'

create=True
# See if exsists
for container in tree:
    print("class:" , container.window_class)
    print("instance: ", container.window_instance)
    if container.window_instance == instance:
        print("Already exists")
        create=False

if create:
    i3.command(f'exec --no-startup-id alacritty --class {instance} -e zsh -i -c "{command}"')
    time.sleep(0.3)
    i3.command(f'[instance="{instance}"] resize set {resolution}')
    i3.command(f'[instance="{instance}"] move position center')


show=True
# See if shows or hides
focused = tree.find_focused().workspace()
for container in focused:
    if container.window_instance == instance:
        show=False
        i3.command(f'[instance="{instance}"] move scratchpad')

if show:
    i3.command(f'[instance="{instance}"] move container to workspace current')
    i3.command(f'[instance="{instance}"] focus')