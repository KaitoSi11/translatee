label E1D3S3:
    
    scene bg isokaze highschool day with fade
    stop ambient fadeout 3
    "I pull my bike up outside of Nikki's school and take off my helmet."
    play ambient "audio/ambience/Campus.ogg" fadein 1
    pf "Here we are!"
    show nikki hap at cc with dissolve
    "Nikki hops off the bike and grins, handing me the extra helmet." 
    voice "audio/voice/E1/D3/S3/Nikki/1.ogg"
    sf "Thanks."
    show nikki neu at cc
    "I notice a few students staring in our direction; one girl walks over to us."
    show highschoolgirl extra at l3 with dissolve
    hstu1f "Hey, Nikki."
    show nikki smi at cc
    voice "audio/voice/E1/D3/S3/Nikki/2.ogg"
    sf "Hey!" 
    hstu1f "Who's this?"
    show nikki hap at cc
    voice "audio/voice/E1/D3/S3/Nikki/3.ogg"
    sf "My brother! He goes to ACE."
    # shiny eyes for girl
    show heart:
        xoffset 230
        yoffset 160
        xzoom .75
        yzoom .75
    hstu1f "Oh, the teal stripes on his uniform! That's amazing! I had no idea you were related to one of the ACE pilots. It's such a tough program."
    show nikki neu at cc
    "She waves over a young male student."
    show studentM extra at r3 with dissolve
    hstu1f "Look! Nikki's older brother is a pilot at ACE."
    # more shiny eyes?
    show heart:
        xoffset 1175
        yoffset 160
        xzoom .75
        yzoom .75
    hstu2m "For real?"
    show nikki smi at cc
    "A few other students gather around us, oohing and ahhing at the difficulty of the pilot program and commenting on how impressive I am. The entire time Nikki beams with pride."  
    pf "Well, I should head to school. Have a good day, Nikki."
    show nikki hap at cc
    show heart:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S3/Nikki/4.ogg"
    sf "Goodbye! Thanks again for the ride."
    hide nikki
    hide studentM extra
    hide highschoolgirl extra
    with dissolve
    stop ambient fadeout 3
    play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
    "She waves and I take off down the road."
    play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg" fadein 1 fadeout 1
    scene bg campus intersection day with fade
    "I'm glad I impressed Nikki's friends. If she had any difficulty making new friends before she certainly won't now."
    $renpy.pause(1)
    scene black with fade
    $renpy.pause(1)
    stop ambient fadeout 3
    $renpy.pause(1)
    stop music fadeout 3
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus main day with fade
    
    jump E1D3S4