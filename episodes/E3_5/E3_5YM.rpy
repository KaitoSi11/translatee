#
label E3_5YM:
    
    voice "audio/voice/E4/Yuuna/E4/D0/2.ogg"
    ym "Hey."
    show yuuna smi at cc with dissolve
    "Yuuna appears in front of me wearing a wide smile as the group moves on."
    pf "Hi, Yuuna."
    
    if E3_5S4_Costume == "Badman":
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/D0/3.ogg"
        ym "The Dark Night!"
        "I grin. She looks at me playfully."
        show yuuna cur
        voice "audio/voice/E4/Yuuna/E4/D0/4.ogg"
        ym "Does that mean you'll be saving all of the damsels in distress this evening?"
        
        menu:
            "Only if it's you.":
                show yuuna cur b1 with dissolve:
                    yoffset -100
                    xzoom 1.25
                    yzoom 1.25
                "I take a step closer and her cheeks flush as I close the distance."
                pf "I'm only interested in protecting one person."
                show yuuna smi b2
                "She wraps her arms around my neck and kisses me."
                voice "audio/voice/E4/Yuuna/E4/D0/5.ogg"
                ym "Good, because I don't like sharing."
                show yuuna smi b1 with dissolve:
                    yoffset 0
                    xzoom 1
                    yzoom 1
            
            "If duty calls.":
                pf "I am not the hero that Isokaze deserves, but the one it needs."
                show yuuna hap b1
                "Yuuna giggles."
                voice "audio/voice/E4/Yuuna/E4/D0/6.ogg"
                ym "I think you quoted that incorrectly."
                pf "With my sidekick, Fact-Checker Girl."
                show yuuna mis b1
                "She smirks."
                show note:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Yuuna/E4/D0/7.ogg"
                ym "It's a tough job, but someone needs to do it."
    
    elif E3_5S4_Costume == "Officer":
        "Yuuna keeps staring at my costume."
        show yuuna cur b1
        voice "audio/voice/E4/Yuuna/E4/D0/8.ogg"
        ym "I never knew an officer of the law could be so… appealing."
        pf "Is that why you can't keep your eyes off of me?"
        show yuuna smi b2
        "She blushes deeply but doesn't look away."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Yuuna/E4/D0/9.ogg"
        ym "Guilty as charged."
        pf "Hey, there's no crime in looking."
        show yuuna hap b1
        "She laughs."
    
    else:
        show yuuna mis
        voice "audio/voice/E4/Yuuna/E4/D0/10.ogg"
        ym "Ooh, I didn't know you were a fan of spandex."
        "She grins playfully."
        pf "Apparently it's a necessity for saving the world."
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Yuuna/E4/D0/11.ogg"
        ym "Now I know their secret."
        pf "But you must only use this knowledge for good."
        show yuuna smi b1
        voice "audio/voice/E4/Yuuna/E4/D0/12.ogg"
        ym "Mmm, we'll see."
        
    voice "audio/voice/E4/Yuuna/E4/D0/13.ogg"
    ym "On that note..."
    show yuuna smi b1
    "Yuuna holds out her hands to the side, giving me a clear view of her outfit."
    show yuuna hap b1
    voice "audio/voice/E4/Yuuna/E4/D0/14.ogg"
    ym "What do you think?"
    
    $ E3_5YM_Cleavage = 0
    
    menu:
        "I love it!":
            pf "Super cute, like you always are."
            show heart:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna hap b2
            "She blushes and beams."
            voice "audio/voice/E4/Yuuna/E4/D0/15.ogg"
            ym "Thank you!"
        
        "Dat cleavage.":
            $ E3_5YM_Cleavage = 1
            "My gaze shifts lower as soon as she \"reveals\" herself."
            show yuuna dis b1
            "Two hands suddenly block my view. My eyes trail up to a pouting Yuuna."
            pf "Aw."
            show storm:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Yuuna/E4/D0/16.ogg"
            ym "Pervert!"
            
            $ E3_5YM_Retry = 0
            
            label E3_5YM_Pervert:
                menu:
                    "YOU CAN'T WEAR SOMETHING LIKE THAT AND THEN CALL ME A PERVERT FOR LOOKING." if E3_5YM_Retry == 0:
                        "Yes she can, and she just did."
                        $ E3_5YM_Retry = 1
                        jump E3_5YM_Pervert
                    
                    "My bad.":
                        pf "You have to understand these things are out of my control."
                        show yuuna mis b1
                        "Yuuna's eyes sparkle mischievously."
                        show heart:
                            xoffset 720
                            yoffset 100
                            xzoom .75
                            yzoom .75
                        voice "audio/voice/E4/Yuuna/E4/D0/17.ogg"
                        ym "Maybe I need to discipline you."
                        show yuuna hap b1
                        "Wait, what did she just say? I do a double take but her warm, innocent smile returns."
    
    stop music fadeout 3
    voice "audio/voice/E4/Yuuna/E4/D0/18.ogg"
    ym "Let's go catch up with the rest of the group!"
    
    if E3_5YM_Cleavage == 1:
        pf "Uh, sure."
        hide yuuna with dissolve
        "Maybe I'm just imagining things."
    else:
        pf "Sure."
        hide yuuna with dissolve
        
    jump E3_5S5
