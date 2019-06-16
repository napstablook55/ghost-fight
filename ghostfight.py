print ("Ghost Fight")
# Work on no caps
action_input = input ('Which way to go? (most variations of North, South, East, and West. No caps.): ')
if action_input == 'north' or action_input == 'n' or action_input == 'north ' or action_input == 'north.' or action_input == 'north. ' or action_input == 'n.' or action_input == 'n ' or action_input == 'n. ':
	print("You go north.")
elif action_input == 'South' or action_input == 's' or action_input == 'S' or action_input == 'south' or action_input == 'south ' or action_input == 'South ' or action_input == 'South.' or action_input == 'south.' or action_input == 'south. ' or action_input == 'South. ' or action_input == 's.' or action_input == 'S.' or action_input == 's ' or action_input == 'S ' or action_input == 's. ' or action_input == 'S. ':
	print("You go south.")
elif action_input == 'East' or action_input == 'e' or action_input == 'E' or action_input == 'east' or action_input == 'east ' or action_input == 'East ' or action_input == 'East.' or action_input == 'east.' or action_input == 'east. ' or action_input == 'East. ' or action_input == 'e.' or action_input == 'E.' or action_input == 'e ' or action_input == 'E ' or action_input == 'e. ' or action_input == 'E. ':
	print("You go east.")
elif action_input == 'West' or action_input == 'w' or action_input == 'W' or action_input == 'west' or action_input == 'west ' or action_input == 'West ' or action_input == 'West.' or action_input == 'west.' or action_input == 'west. ' or action_input == 'West. ' or action_input == 'w.' or action_input == 'W.' or action_input == 'w ' or action_input == 'W ' or action_input == 'w. ' or action_input == 'W. ':
	print("You go dennis. I mean west.")
elif action_input == 'Dennis' or action_input == 'dennis' or action_input == 'Dennis ' or action_input == 'dennis ' or action_input == 'Dennis.' or action_input == 'dennis.' or action_input == 'Dennis. ' or action_input == 'dennis. ':
	print("You go... oh wait. Dennis wasn't an option. Eh, I guess i'll give it to ya. You go Dennis.")
else:
	print("You idiot. I told you what you could write when I asked you to write it. Get out of my face.")