#
label E3END:
    stop music fadeout 3
    stop ambient fadeout 3
    # Say whatever we need to say
    $renpy.pause(2.5)
    show mcInt with dissolve:
        xalign 0.5
        yalign 0.1
        yoffset 135
        
    "Hello, {i}ACE Academy{/i} Steam Early Access supporters!"
    "Thank you for playing episode 3! {w}We hope you enjoyed it."
    "Hopefully the cliffhanger wasn't too mean. {w}:P"
    "We love to hear and incorporate player feedback into development, so please feel free to let us know your thoughts on the discussion boards or in a Steam review!"
    "Thanks again. {w}We hope to see you one more time in the final chapter of ACE Academy~!"
    
    hide mcInt with dissolve
    "NOTE: If you wish to continue without starting over for the next episode, please follow these instructions:"
    "Make a save slot now! {w}Please use this when the next episode is released."
    "Thank you and see you next time~!"
    
    ### UPDATED VARIABLES
    # these are necessary to fill in to not break the game
    
    ### E1D4S6
    # E4D4S4 uses this
    $ E1D4S6_Ceonardo = 0
    "Did you watch a Ceonardo DiLaprio movie after your very first match?"
    menu:
        "Yes":
            $ E1D4S6_Ceonardo = 1
        "No":
            $ E1D4S6_Ceonardo = 0
    
    ### E2KIS3
    # 3.5 Halloween costume scenes use this
    $ E2KIS3_Ranger = "Justice"
    if kaorelatonship == 1:
        voice "audio/voice/E2/Free/KI/62.ogg"
        ki "Um, so... which is your favourite ranger?"
        
        menu:
            "Justice":
                $ E2KIS3_Ranger = "Justice"
                pf "Balance, the Ranger of Justice."
        
            "Knowledge":
                $ E2KIS3_Ranger = "Knowledge"
                pf "Tome, the Ranger of Knowledge."
    
            "Emotion":
                $ E2KIS3_Ranger = "Emotion"
                pf "Sense, the Ranger of Emotion."
        
            "Power":
                $ E2KIS3_Ranger = "Power"
                pf "Forte, the Ranger of Power."
        
            "Honor":
                $ E2KIS3_Ranger = "Honor"
                pf "Aura, the Ranger of Honor."
            
    ### E3VBS3
    # E3VBS3_Completed was not a variable in E3 release, added for E3.5/4
    "Did you spend time shopping with Valerie at the mall?"
    menu:
        "Yes":
            $ E3VBS3_Completed = 1
        "No":
            $ E3VBS3_Completed = 0
            
    if E3VBS3_Completed == 1:
        "Did you tell Valerie to buy the Nekogirl outfit during your date together?"
        menu:
            "Yes":
                $ E3VBS3_Nekogirl = 1
            "No":
                $ E3VBS3_Nekogirl = 0
    else:
        $ E3VBS3_Nekogirl = 0
        
    ### E3D5S4
    # Some wake-up scenes for E4D5 (VB) use this information
    "How did you react to Ken in Nikki's room?"
    menu:
        "I've got my eyes on you.":
            $ E3D5S4_Reaction = 1
    
        "Don't try anything silly.":
            $ E3D5S4_Reaction = 2
    
        "Move him out of the room.":
            $ E3D5S4_Reaction = 3
            
    ###
    
    #
    
    jump E3_5S1
