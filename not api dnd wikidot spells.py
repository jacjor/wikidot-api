'''root values lineage,
spell,
background,
feat

sub values
no root    adventuring gear,armor,trinkets,weapons,firearms,explosives,wondrous items,currency,poisons,tools,siege equipment
no root artificer,barbarian...
name of feat
name of spell
name of background
put false if there is no root value
'''

import webbrowser
root = 'false'
while True :
    # syntax <root> <name> ie lineage dragonborn
    original_command= input('what would you like to search\n').lower()
    command = original_command.split(' ',1)

    root = command[0]
    sub = command[1]
    
    sub.join('-')
    root.join('-')
    if root =='false':
        webbrowser.open(f'https://dnd5e.wikidot.com/{sub}')
    else:    
        webbrowser.open(f'https://dnd5e.wikidot.com/{root}:{sub}') 
