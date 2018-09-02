label E1D3S2:
    scene bg isokaze neighborhood day with fade
    stop ambient fadeout 3
    "At least it's a nice day to be waiting for the bus."
    play ambient "audio/ambience/Bus Stop.ogg" fadein 1
    "The stop is a bit crowded. I lean up against the shelter as I wait."
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
    "The bus squeals to a halt in front of me only a few minutes after my arrival."
    scene bg travel bus day with fade
    stop ambient fadeout 3
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "I follow the other passengers on, scan my ID, and search the rows for a free seat."
    play ambient "audio/ambience/Bus.ogg" fadein 1
    
    if (E1D2S2_talkwithyuunayes == 1):
        "To my disappointment, Yuuna is nowhere in sight."
    
    "I settle into the first seat I find and grumble as a large man sits down beside me, crushing me against the window." 
    "I can already imagine how enjoyable this ride will be."
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    scene bg travel bus day with fade
    "Luckily it isn't a long ride and I'm at school before I can complain too much."
    stop ambient fadeout 3
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    scene bg campus main day with fade
    play ambient "audio/ambience/Campus.ogg" fadein 1
    jump E1D3S4