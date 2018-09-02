#
label E3D7S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sFashion"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sCasual"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sCasual"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sCasual"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sDate"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sFlirty"
    
    $ kaiOut = "sCasual"
    
    $ day = 7
    $ timeSpent = "none"
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    stop sound
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    "The sound of my alarm wakes me up. With a wide yawn, I push myself out of bed. A small part wishes I could have slept in again, but that part is silenced by the rest of me who is pumped for the the big concert! {w}I swap through different outfits and spend a little more time on my appearance. It's important that I make a good impression as I'm not only representing myself and my team, but I'm representing ACE Academy too."
    
    "Once satisfied, I check my email for the location of the event. {w}It's hosted at the Isokaze concert hall. The sponsorship networking event is at a club next door."
    scene bg homekaito main day
    "I head downstairs, expecting to see a heartbroken Nikki, but to my surprise, Uncle Kaito greets me from the couch, a piece of toast hanging from his mouth."
    voice "audio/voice/E3/D7/S1/kaito/1.ogg"
    hk "Hry bd, esitd fr tdy?"
    pf "What?"
    show kaito mis at cc with dissolve
    "Kaito swallows his mouthful of toast and grins."
    voice "audio/voice/E3/D7/S1/kaito/2.ogg"
    hk "You don't speak food?"
    pf "Not fluently, it seems."
    show kaito smi
    ### VOICE - missing line?
    voice "audio/voice/MISSING/BATCH4/Kaito_MissingLines-01.ogg"
    hk "Are you excited for today?"
    pf "You already know?"
    show kaito hap
    voice "audio/voice/E3/D7/S1/kaito/3.ogg"
    hk "Are you kidding me? Nikki has been talking nonstop about it! \"{i}Onii-chan gets to meet Ex Zee{/i}\"!"
    pf "Did she really say that?"
    show kaito mis
    voice "audio/voice/E3/D7/S1/kaito/4.ogg"
    hk "Eh, close enough."
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    "We laugh."
    pf "Speaking of which..."
    show kaito smi
    voice "audio/voice/E3/D7/S1/kaito/5.ogg"
    hk "She's hanging out with some friends. They're going to watch the concert together but have to \"prep\" first. I don't really understand what means."
    pf "Neither do I."
    "I check the time. Urgh, not enough time to make breakfast."
    voice "audio/voice/E3/D7/S1/kaito/6.ogg"
    hk "Here."
    "Uncle Kaito offers me his extra toast."
    show kaito mis
    voice "audio/voice/E3/D7/S1/kaito/7.ogg"
    hk "I know that face all too well. There have been many a morning where I had to go hungry, and I can't subject my nephew to that kind of life."
    pf "That's morbid."
    show kaito hap
    "He laughs."
    voice "audio/voice/E3/D7/S1/kaito/8.ogg"
    hk "I have a rare day off and can afford to make another."
    "I grin and accept his offering."
    show kaito smi
    pf "Thanks."
    voice "audio/voice/E3/D7/S1/kaito/9.ogg"
    hk "Have a good day!"
    hide kaito with dissolve
    "I nibble at my toast and head to the garage. Then I wolf the remaining toast down before driving into the city."
    
    stop ambient fadeout 3
    #black screen
    scene black with fade
    
    jump E3D7S2
    