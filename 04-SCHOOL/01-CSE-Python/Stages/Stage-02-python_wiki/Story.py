print(
    "You walk into a dimly lit room, the door slams shut behind you, as you hear the dead bolt lock your heart sinks. There are two doors in front of you, and it seems you must choose one to proceed. "
)
choice = input("Will you go left or right? left/right: ").lower()
if choice == "left":
    print(
        "You started out well this is the safer room, but is this the right challenge for you? You see a bright light at the end of one tunnel and a dark tunnel that has no noticible end. You must choose which tunnel to go down. "
    )
    tunnel = input(
        "Will you go down the light tunnel or the dark tunnel? light/dark: "
    ).lower()
    if tunnel == "light":
        print(
            "You took what you thought was the easier path, but you are now stuck in a lit cave forever as it is a dead end and the path has collapsed behind you. Best of luck trying to escape, or survive at least there is light. "
        )
    elif tunnel == "dark":
        print(
            "Wow you chose the harder path, and are rewarded after a long stretch in the dark the tunnel turned to reveal the caves exit and you are free to go on living the life you dreamed of. "
        )
    else:
        print("you lose")
elif choice == "right":
    print(
        "Oh no this door leads to some obsicles and you must pick which one you will traverse, there is a pit of spikes and a pit of snakes, each has a ragdy rope bridge that spans across the pit. You must choose which bridge to cross. "
    )
    bridge = input(
        "Will you cross the bridge of spikes or snakes? spikes/snakes: "
    ).lower()
    if bridge == "spikes" or bridge == "snakes":
        print(
            "You have made your choice and while crossing just as you put your foot on the other side the rope snaps and you are safe. With a new respect for life you exit the cave and go on to explore the world."
        )
    else:
        print("you lose")
else:
    print("you lose")
