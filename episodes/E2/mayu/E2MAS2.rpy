label E2MAS2:


    $ mayOut = "sUniform"
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    "It's such a nice day out that I decide to do some studying outside."
    
    play ambient "audio/ambience/Campus.ogg" fadein 5
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    scene bg campus main day with fade
    "I make myself comfortable on a bench in the courtyard, when I see Mayu walk past."
    
    if MCStory == 2:
        "She's carrying a violin case with her."
    
    else:
        "She's carrying a case with her."
    
    pf "Hey, Mayu!"
    "I stand and wave. She turns at the sound of her name, and comes over when she sees me."
    
    show mayu cur at cc with dissolve
    voice "audio/voice/E2/Free/MA/S2/0-01.ogg"
    ma "Hi, I didn't see you there."
    pf "No worries. {w}Where are you headed?"
    
    show mayu smi
    voice "audio/voice/E2/Free/MA/S2/0-02.ogg"
    ma "I'm going to the music room."
    "She shuffles the case from one hand to the other."
    
    if MCStory == 2:
        pf "That's cool. You play the violin?"
        "Mayu nods."
    
    else:
        pf "That's cool. You play an instrument?"
        voice "audio/voice/E2/Free/MA/S2/0-03.ogg"
        ma "Yup, the violin."
    
        show mayu cur
        voice "audio/voice/E2/Free/MA/S2/0-04.ogg"
        ma "Do you play an instrument?"
    
    if MCStory == 2:
        pf "Yeah, I took lessons as a kid and played all through high school."
        show mayu smi
        voice "audio/voice/E2/Free/MA/S2/0-05.ogg"
        ma "That's great! I started when I was kid too. My father always believed that music is an integral part of a person's education."
        pf "He sounds like a smart man."
        voice "audio/voice/E2/Free/MA/S2/0-06.ogg"
        ma "He is."
    
    else:
        pf "My parents tried to get me interested in music when I was young and I was forced to do lessons, but I quit when I was older to pursue other activities."
        show mayu neu
        voice "audio/voice/E2/Free/MA/S2/0-07.ogg"
        ma "I understand. When my father first put me in lessons I hated it, but the more I practiced and learned about music, the more I liked it."
        pf "That's good. It's always harder to do something when you dislike it."
        "Mayu nods."
    
    pf "I'd love to hear you play sometime."
    
    show exclamation:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
        
    show mayu cur with dissolve
    "Mayu's eyes grow wide and her hands tremble."
    show mayu ner b1 with dissolve
    voice "audio/voice/E2/Free/MA/S2/0-08.ogg"
    ma "Oh, I don't know. I think I'd be too embarrassed."
    pf "How come?"
    voice "audio/voice/E2/Free/MA/S2/0-09.ogg"
    ma "It's so embarrassing to play in front of an audience. I practice alone."
    pf "So you've never performed at a recital or anything?"
    "She shakes her head."
    voice "audio/voice/E2/Free/MA/S2/0-10.ogg"
    ma "No, I always had private lessons so I've never had to play in front of a crowd before."
    
    menu:
        "You don't have to be embarrassed.":
            pf "I'm sure you're really good. You don't have to be scared to play in front of people."
            "Mayu shuffles her feet and holds her case close to her side."
            voice "audio/voice/E2/Free/MA/S2/0-11.ogg"
            ma "I would like to, but I really just can't...."
    
        "I'll teach you a trick.":
            pf "Just imagine everyone in their underwear. I mean, in that case, you don't have to be embarrassed, they should be embarrassed!"
            show mayu sur b1 with dissolve
            "Mayu's face turns beet red and she stutters her response."
            voice "audio/voice/E2/Free/MA/S2/0-12.ogg"
            ma "I--I couldn't possibly!"
    
        "What are you scared of?":
            pf "Why would you be embarrassed?"
            show mayu neu b1
            voice "audio/voice/E2/Free/MA/S2/0-13.ogg"
            ma "W-What if they don't think I'm good?"
            pf "You'll never know if you only play in private."
            show mayu thi b1
            voice "audio/voice/E2/Free/MA/S2/0-14.ogg"
            ma "That is true…"
            "Still, she doesn't seem convinced."
    
    pf "Okay, how about we make a deal? I'll do something embarrassing, then you'll play for me."
    show mayu cur b1 with dissolve
    voice "audio/voice/E2/Free/MA/S2/0-15.ogg"
    ma "No, you don't have to do that."
    pf "But if I do, you'll play for me, right?"
    
    
    show storm:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
        
    show mayu neu b1 with dissolve
    
    "She bites her lip. Worry clouds her eyes."
    pf "Don't be afraid. Watch this!"
    
    hide mayu with dissolve
    
    if MCStory == 1:
        "In one smooth leap, I jump onto the bench, raise my arms over my head, and shout…"
        stop music fadeout 2.0
        pf "I'M THE KING OF THE WORLD!"
        "All of the surrounding students pause to stare at me. {w}The silence seems to stretch forever before the whispers begin. {w}Once everyone looks away, I hop down from the bench and grin at Mayu. My cheeks are burning, but I feel strangely exhilarated."
    
    else:
        "In one long leap, I jump onto the bench, but I miscalculate my distance and my foot hits the edge of the seat. I windmill my arms, trying to catch my balance..."
        stop music fadeout 2.0
        with Shake((0, 0, 0, 0), .5, dist=5)
        $renpy.pause(.5)
        "...but end up toppling over the back of the bench and falling face-first into the grass."
        "All of the surrounding students pause to stare at me, and the laughter that follows seems to stretch forever before it gradually dies down. {w}Once everyone loses interest, I untangle my limbs and push myself to standing."
        "My cheeks are burning as I check myself for bruises. That definitely did not go as planned."
        show shoBlush:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu sur at cc with dissolve
        voice "audio/voice/E2/Free/MA/S2/0-16.ogg"
        ma "A-Are you okay?"
        pf "Yeah, I'm fine."
    
    
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3.0
    show mayu sur b2 at cc with dissolve
    "Mayu's face and neck are bright red, and as I straighten up, she hides her face in her hands."
    voice "audio/voice/E2/Free/MA/S2/0-17.ogg"
    ma "I can't believe you did that!"
    pf "Aw, hey, why are you embarrassed? I'm the one who did that and I'm okay."
    
    show mayu ner b1 at cc with dissolve
    voice "audio/voice/E2/Free/MA/S2/0-18.ogg"
    ma "I-I don't know."
    "She lowers her hands and glances at me. I grin at her."
    pf "See? I'm still alive!"
    
    show mayu smi b1 with dissolve
    "Mayu hesitates, then she laughs. {w}I've never noticed how cute her laugh is."
    
    show mayu cur b1
    "She notices me staring, and hides her laughter with her hand."
    voice "audio/voice/E2/Free/MA/S2/0-19.ogg"
    ma "What?"
    pf "Nothing. It's your turn now!"
    "Mayu shakes her head."
    
    show panic:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner b1
    voice "audio/voice/E2/Free/MA/S2/0-20.ogg"
    ma "I can't, it's too embarrassing! But I promise I'll play for you another time. But only when it's just you."
    "I nod."
    pf "I'll hold you to it."
    
    show mayu smi b1 dissolve
    "She smiles."
    voice "audio/voice/E2/Free/MA/S2/0-21.ogg"
    ma "I'd better get to practice now."
    pf "Sure. I'm going to go somewhere where no one just watched me do that."
    
    show note:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    "Mayu giggles again, then waves goodbye."
    
    hide mayu with dissolve
    
    
    stop music fadeout 5
    stop ambient fadeout 5
    scene black with fade
        
    $ E2MAS2_Completed = 1
    "Once she's gone, I find a secluded area on campus to finish studying."