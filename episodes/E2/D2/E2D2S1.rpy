#
label E2D2S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ day = 2
    $ timeSpent = "none"
    #black BG
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    "..."
    stop sound fadeout 1
    "My alarm snaps me out of my slumber. With a groan, I reach outside my blanket in search of the coveted \"snooze\" button."
    #Player room BG
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    pf "5:45AM..."
    "What possessed me to set my alarm at such an ungodly hour? {w}Oh right, the physical education class I have this morning. {w}Any normal human being would have picked a more reasonable time for this course, which explains why this time slot was the only one available."
    "I climb out of bed and begin my morning routine."
    #Bad black
    # ^ ( What does this mean? ) ^
    scene black with fade
    stop ambient fadeout 5
    "After getting ready, I head downstairs to an empty living room. Kaito and Nikki must still be asleep… {w}like any other normal person. {w}I power feast through breakfast and head on my way."

    #School campus
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus building day with fade

    "An uneventful drive later, I'm waiting outside the gymnasium. {w}Some zombie-like students wait with me. The rest are passed out on the campus benches."


    $ kaoOut = "sUniform"
    
    $ kaoHairF = renpy.random.choice(['default'])
    $ kaoHairB = kaoHairF

    
    $ shoOut = "sUniform"
    
    
    voice "audio/voice/E2/D2/Shou/1.ogg"
    ss "Broseph!"
    show kaori neu at l2
    show shou hap at r2:
        xzoom -1
    with dissolve
    "A cheerful voice--too cheery for the current time of day--breaks through my reverie, and I see two familiar faces approaching. {w}Shou is beaming, but I can't say the same about Kaori. Her eyes are hardly open and she yawns, barely mustering a nod of acknowledgement."
    show shou smi at r2
    
    menu:
        "It's a beautiful day in the neighborhood!":
            pf "Mr. Shinjirou, a pleasure as always!"
            show shou hap at r2
            show note:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            "I raise an open palm. Shou grins before giving me a resounding high five."
            show kaori ann at l2
            "Kaori covers her ears and glares. {w}Shes not the only one looking at us disapprovingly."
            show shou wor at r2
            voice "audio/voice/E2/D2/Shou/2.ogg"
            ss "Oh! Sorry, Kaori."
            show storm:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori win at l2
            voice "audio/voice/E2/D2/S2/Kaori/1.ogg"
            ki "I'm already getting a headache..."

        "I'm with Kaori on this one...":
            "I rub my eyes, barely able to stay conscious."
            show shou cur at r2
            voice "audio/voice/E2/D2/Shou/3.ogg"
            ss "Aww, you're not a morning person either?"
            # some sort of visual for this?
            ### NOTE SFX
            show shou mis at r2 with dissolve
            show kaori sur at l2, Shake(None, .33, dist=5)
            show bg campus building day:
                linear .33 xoffset 50
            show shou mis at r2:
                linear .33 xoffset 30
            with Shake((0, 0, 0, 0), .33, dist=5)
            show shocked:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            $ renpy.pause(1.0)
            "Before I get a chance to reply, Shou smacks my back hard and I stumble a few paces. Kaori staggers too."
            show kaori ang at l2
            "She whips around and stomps a foot towards Shou. Her drowsy expression is replaced with one of fire."
            voice "audio/voice/E2/D2/S2/Kaori/2.ogg"
            ki "Ow! What was that for?"
            show kaori ann at l2
            show shou smi at r2
            voice "audio/voice/E2/D2/Shou/4.ogg"
            ss "Just waking you both up for a wonderful day of gym class!"
            show vein:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            "Kaori and I both shoot piercing glares towards Shou."
            pf "I am going to end him."
            show kaori dis at l2
            voice "audio/voice/E2/D2/S2/Kaori/3.ogg"
            ki "Not before I do."
            show shou ner at r2
            "Shou steps back, his hands going up defensively."
            show shou wor at r2
            voice "audio/voice/E2/D2/Shou/5.ogg"
            ss "Woah guys! Chillax."
            voice "audio/voice/E2/D2/Shou/6.ogg"
            ss "So scary..."

    pf "What's up with you two picking this as your timeslot for the course?"
    show kaori ske at l2
    show shou neu at r2
    voice "audio/voice/E2/D2/S2/Kaori/4.ogg"
    ki "We could ask the same for you."
    pf "I transferred into the program late, so this was the only class available."
    show kaori neu at l2
    "Kaori crosses her arms."
    voice "audio/voice/E2/D2/S2/Kaori/5.ogg"
    ki "I guess that makes sense."
    pf "And you guys?"
    voice "audio/voice/E2/D2/Shou/7.ogg"
    ss "We were originally in a later class but decided to change out."
    pf "Any reason why?"
    show kaori thi at l2
    show shou thi at r2
    "Shou looks at Kaori. She sighs before shrugging her shoulders."
    show shou neu at r2
    voice "audio/voice/E2/D2/Shou/8.ogg"
    ss "Remember when we told you about us forming our own team because it didn't work out with the previous one?"
    pf "Yeah."
    voice "audio/voice/E2/D2/Shou/9.ogg"
    ss "Let's just say, we all decided to pick the same gym class to train together, but as you know, it didn't work out."
    pf "Sounds more like a falling out."
    show kaori neu at l2
    "Shou rubs the back of his head."
    show shou hap at r2
    show drop:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D2/Shou/10.ogg"
    ss "Hehe, something like that. In any case, we figured it'd be easier to switch out than deal with that awkwardness every week."

    menu:
        "Pry for details.":
            pf "So what happened exactly?"
            show shou thi at r2
            voice "audio/voice/E2/D2/Shou/11.ogg"
            ss "Uh well--"
            show kaori ann at l2
            voice "audio/voice/E2/D2/S2/Kaori/6.ogg"
            ki "There's nothing more to tell. It didn't work out, so we changed classes. What part of that don't you understand?"
            show shou neu at r2
            "Kaori looks annoyed."
            pf "Alright, I get it."
            show kaori dis at l2

        "Drop it for now.":
            show shou smi at r2
            pf "I guess that makes sense."

### NOTE Points - "IF (high points with Kaori + weekend)"
        "It's a cover! Kaori must have joined to see me!" if E1D5S1_EventKaori == 1:
            stop music fadeout 3
            "I nod solemnly."
            pf "I get it now."
            show shou smi at r2
            show question:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            voice "audio/voice/E2/D2/S2/Kaori/8.ogg"
            ki "Get what?"
            show kaori ske at l2
            "I gaze deeply into Kaori's eyes. She raises an eyebrow."
            voice "audio/voice/E2/D2/S2/Kaori/9.ogg"
            ki "W-What?"
            pf "You switched classes for me."
            show kaori cur b1 at l2 with dissolve
            "She shuffles uncomfortably. Pink tinges her face."
            show kaori ske b1 at l2
            show shou cur at r2
            voice "audio/voice/E2/D2/S2/Kaori/10.ogg"
            ki "Are you for real? I knew you were an idiot, but seriously?"
            show kaori ske b2 at l2 with dissolve
            "I gently take her hands in my own. The color in her cheeks deepen."
            pf "And now you're being all shy to hide it. You are so cute!"
            show kaori ann b2 at l2
            show tsuBlush:
                xoffset 365
                yoffset 110
                xzoom .75
                yzoom .75
            "Kaori retracts her hands and stammers her reply."
            show kaori ang b2 at l2
            show shou hap at r2
            voice "audio/voice/E2/D2/S2/Kaori/11.ogg"
            ki "I-I can't believe you would say something so stupid! Can you believe this, Shou?"
            show note:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            "Shou is far too busy laughing to respond."
            show kaori ann b2 at l2 with dissolve
            voice "audio/voice/E2/D2/S2/Kaori/12.ogg"
            ki "That's it, I'm joining another class."
            pf "There are no other classes available, remember?"
            show kaori dis b1 at l2 with dissolve
            "Kaori cringes, then groans."
            show shou smi at r2
            voice "audio/voice/E2/D2/S2/Kaori/13.ogg"
            ki "I can't believe I'm stuck here with you two idiots for a whole semester."

    stop music fadeout 3
    # door click/open sfx?
    "We hear a click as the building door unlocks."

    voice "audio/voice/E2/D2/S1/prof4m/1.ogg"
    prof4m "Sorry for the wait, everyone. We had a little issue with the gym schedule, but that's now been resolved. Please make your way to the locker rooms, then meet at Gymnasium III."
    show shou hap at r2
    voice "audio/voice/E2/D2/Shou/12.ogg"
    ss "Awesome! We'll see you there, Kaori. Come with me, broseph!"

    stop ambient fadeout 3
    #black bg
    scene black with fade
    "Shou pushes me towards the men's locker room."
    
    jump E2D2S2
