#
label E2D5SS:
    
    "I head back to the living room and spot Shou surrounded by a group of his dorm-mates. They're urging him to join them, but Shou keeps shaking his head. By the time I approach, his friends have moved on and Shou is left standing alone."
    show shou neu at cc with dissolve
    pf "Hey, Shou."
    voice "audio/voice/E2/D5/SS/1.ogg"
    voice "audio/voice/E2/D5/SS/131.ogg"
    ss "Mr. Broseph."
    pf "What was that about?"
    show shou cur at cc
    "I nod towards his retreating dorm-mates."
    show shou smi at cc
    voice "audio/voice/E2/D5/SS/132.ogg"
    ss "Oh nothing. They were going to challenge someone to a drinking match or something."
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou cur at cc
    voice "audio/voice/E2/D5/SS/133.ogg"
    ss "Have you seen Mayu?"
    "I shake my head."
    show shou ner at cc
    "Shou seems a little concerned."
    voice "audio/voice/E2/D5/SS/134.ogg"
    ss "Hm, do you think she left? I promised that I'd hang out with her but I don't see her anywhere. Maybe I should do another round and look again."
    
    menu:
        "What if Mayu's looking for you too?":
            pf "It might be better for you to stay here."
            show shou ske at cc
            voice "audio/voice/E2/D5/SS/135.ogg"
            ss "Why?"
            pf "Well, maybe Mayu got separated from you and is searching for you too. If you're both moving around it'll be harder for you to find each other."
            show shou neu at cc
            voice "audio/voice/E2/D5/SS/136.ogg"
            ss "That makes sense. Yeah, I think I'll stay here."
            pf "Good idea."
            show shou ner at cc
            voice "audio/voice/E2/D5/SS/137.ogg"
            ss "But wait, what if Mayu is standing in one spot waiting for me?"
            "Oh, I didn't think of that."
            pf "I doubt it. Parties aren't her thing."
    
        "What a buzzkill.":
            pf "C'mon, man, it's a party! You should be spending less time worrying about silly things and more time having fun."
            show shou neu at cc
            voice "audio/voice/E2/D5/SS/138.ogg"
            ss "Mayu's not a silly thing."
            pf "I'm sure she's fine. {w}How did you two get separated anyway?"
            show shou thi at cc
            "Shou thinks about it, then shrugs."
            show shou ner at cc
            voice "audio/voice/E2/D5/SS/139.ogg"
            ss "I don't know. One second she was right here, and then I think I might have talked to someone, and suddenly she was gone!"
            pf "Well, if she left by herself then you don't have to worry about her, right? She'll come find you if she needs you."
    
        "Mayu's a big girl.":
            pf "Mayu can take care of herself."
            show shou thi at cc
            voice "audio/voice/E2/D5/SS/140.ogg"
            ss "Yeah, but she's a little out of her element at parties."
            pf "If she needs you, she'll find you."
            show shou ner at cc
            voice "audio/voice/E2/D5/SS/141.ogg"
            ss "What if she's in trouble?"
            pf "Can you really imagine Mayu getting herself in trouble? At a party?"
            
    show shou neu at cc with dissolve
    show shou smi at cc with dissolve
    "Shou pauses, then brightens up."
    voice "audio/voice/E2/D5/SS/142.ogg"
    ss "You're right! Let's just focus on having fun."
    stop music fadeout 3
    pf "Sounds like a plan to me."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
    
    show highschoolgirl2 extra at l3
    show highschoolgirl extra at r3:
        xzoom -1
    with dissolve
    "A couple of girls approach us. They're sipping their drinks and giggling. The one on the right has long dark hair, while the one on the left has her hair tied in a braid. They're both wearing dresses that hug their every curve, and my gaze lingers at their skirt's teasingly low hemline."
    # what is this supposed to be? "Frat Bra"?
    show shou cur at cc
    fbra1f "Hey, we watched your match earlier today. You were so good out there!"
    pf "Uh, thanks."
    show shou smi at cc
    voice "audio/voice/E2/D5/SS/fbra2f/1.ogg"
    fbra2f "Yeah, you were so impressive! How did you do it?"
    
    menu:
        "It's just a lot of hard work.":
            if E2D5S3_Distraction == "MC":
                pf "I just did what I had to. The strategy was to lead the three teammates away from Tatsuo so the rest of my team could take him out."
    
                if E2D5S4_Gladiator == 1:
                    fbra1f "But you depowered all of them on your own!"
                    voice "audio/voice/E2/D5/SS/fbra2f/2.ogg"
                    fbra2f "It was amazing!"
        
                else:
                    fbra1f "And you fought so bravely against them!"
                    voice "audio/voice/E2/D5/SS/fbra2f/3.ogg"
                    fbra2f "Yeah! You did a lot of damage before getting depowered."
            else:
                pf "I just tried my best. I was there to back up my teammates so we could take out Tatsuo."
                voice "audio/voice/E2/D5/SS/fbra2f/4.ogg"
                fbra2f "You work really well with your team. They must be so glad they can count on you to have their backs."
                pf "I'm sure they'd do the same for me."
    
        "Please, don't both of you praise me at once.":
            pf "Ladies, ladies, please… that isn't the only impressive thing about me."
            "The girls giggle."
            fbra1f "Oh yeah?"
            voice "audio/voice/E2/D5/SS/fbra2f/5.ogg"
            fbra2f "What else is impressive?"
            pf "Well--"
    
        "Thanks.":
            pf "Thanks."
            "They wait for me to continue but I don't."
            fbra1f "Well, your team must be really happy to have you onboard."
            show shou cur at cc
            "I turn to Shou."
            pf "Are you happy to have me onboard?"
            show shou hap at cc
            voice "audio/voice/E2/D5/SS/143.ogg"
            ss "Yup."
            show shou smi at cc
            "I turn back to the girls."
            pf "Yup, they are."
    
    "Shou interjects."
    show shou mis at cc
    
    if E2D5S3_Distraction == "Shou":
        voice "audio/voice/E2/D5/SS/144.ogg"
        ss "Did you see how I broke from the group to take on the enemy alone?"
        "The girls pause, surprised by Shou's interruption."
        fbra1f "Oh, um, yeah… but didn't you still need help from your teammate here to take out just {i}one{/i} GEAR?"
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou hap at cc
        voice "audio/voice/E2/D5/SS/145.ogg"
        ss "Well, yeah, but that's because Tatsuo is really tough."
        "They smile politely."
        fbra1f "Of course."
    
    else:
        voice "audio/voice/E2/D5/SS/146.ogg"
        ss "Did you see when I faced off against Tatsuo?"
        "The girls pause, surprised by Shou's outburst."
        voice "audio/voice/E2/D5/SS/fbra2f/6.ogg"
        fbra2f "Um, I'm not sure…"
        voice "audio/voice/E2/D5/SS/fbra2f/7.ogg"
        fbra2f "Weren't you fighting him in a group?"
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou hap at cc
        voice "audio/voice/E2/D5/SS/147.ogg"
        ss "Yeah, but there were a few moments where we battled one on one."
        voice "audio/voice/E2/D5/SS/fbra2f/8.ogg"
        fbra2f "Sorry…"
        "They smile politely."
        
    show shou neu at cc
    "The girls return their attentions to me."
    fbra1f "So, we were thinking of grabbing another drink. How about you come with us?"
    pf "Thanks for the offer, but I'm alright for now. Maybe later."
    fbra1f "Sure, come find us at any time."
    stop music fadeout 5
    "With lingering looks and smiles, they disappear into the crowd."
    hide highschoolgirl
    hide highschoolgirl2
    with dissolve
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    $renpy.pause(1)
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou ner at cc
    voice "audio/voice/E2/D5/SS/148.ogg"
    ss "What was that, broseph?"
    pf "What?"
    show shou ske at cc
    voice "audio/voice/E2/D5/SS/149.ogg"
    ss "Those girls were totally into you!"
    "I shrug."
    show shou wor at cc
    voice "audio/voice/E2/D5/SS/150.ogg"
    ss "And you just turned them down! Like some kind of stud who knows he can get any girl he wants…"
    show shou ske at cc
    voice "audio/voice/E2/D5/SS/151.ogg"
    ss "What's your secret?"
    
    menu:
        "I don't have one?":
            pf "What are you talking about?"
            show shou neu at cc
            voice "audio/voice/E2/D5/SS/152.ogg"
            ss "How do you get random girls to talk to you?"
            pf "They just wanted to talk about the match. It was nothing special."
            show shou sad at cc
            voice "audio/voice/E2/D5/SS/153.ogg"
            ss "They didn't talk to me about the match."
            pf "You're thinking way too much into it."
    
        "I'm born this way.":
            pf "I can't help it. It's a curse that I must bear."
            show shou wor at cc
            voice "audio/voice/E2/D5/SS/154.ogg"
            ss "How is that possibly a curse?"
            pf "You're right, it's not. It's actually a blessing, not a curse."
            show shou sad at cc
            voice "audio/voice/E2/D5/SS/155.ogg"
            ss "Sure, just rub it in."
    
        "I actually envy you.":
            pf "I wish I were more like you."
            show shou cur at cc
            voice "audio/voice/E2/D5/SS/156.ogg"
            ss "Huh?"
            pf "Where no girl ever approaches me. You don't know how luck you are."
            show shou sad at cc
            "Shou frowns."
            voice "audio/voice/E2/D5/SS/157.ogg"
            ss "Salt in the wound man."
            pf "I'm serious."
    
    pf "Look, don't think so much about it. Just be yourself, and I'm sure they'll like you."
    show shou cur at cc
    voice "audio/voice/E2/D5/SS/158.ogg"
    ss "You think so?"
    pf "That's what I do."
    show shou neu at cc
    voice "audio/voice/E2/D5/SS/159.ogg"
    ss "Hmm…"
    "I point to two different girls who are standing on the far end of the room."
    pf "Why don't you try talking to them?"
    pf "Remember, just be yourself."
    show shiny:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou mis at cc
    voice "audio/voice/E2/D5/SS/160.ogg"
    ss "Yeah, you're right! I can do this!"
    hide shou with dissolve
    "Grinning, Shou walks up to the girls and works his magic on the one with long hair."
    "I can't hear what he says, but after a few seconds, the smile drops off her face and she throws her hands over her chest. {w}Shou then turns to her friend, who shakes her head before he can even get a word out."
    "Yikes. That didn't go well."
    show shou sad at cc
    "Dejected, Shou trudges back to me."
    show crying:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/SS/161.ogg"
    ss "Being myself didn't work."
    pf "Usually saying something nice helps."
    show shou ner at cc
    voice "audio/voice/E2/D5/SS/162.ogg"
    ss "I did!"
    pf "What did you say?"
    show shou thi at cc
    voice "audio/voice/E2/D5/SS/163.ogg"
    ss "I told her that I liked her dress..."
    pf "That doesn't seem too bad."
    show shou smi at cc
    voice "audio/voice/E2/D5/SS/164.ogg"
    ss "And how it emphasises her boobs."
    pf "..."
    show shou cur at cc
    voice "audio/voice/E2/D5/SS/165.ogg"
    ss "What?"
    "He's hopeless."
    pf "I'm sure there's a girl for you out there."
    show shou thi at cc
    voice "audio/voice/E2/D5/SS/166.ogg"
    ss "I hope so."
    
    show dots:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    $renpy.pause(1.5)
    "He sighs, and we stand in silence, watching the crowd."
    $renpy.pause(1.5)
    show shou smi at cc with dissolve
    voice "audio/voice/E2/D5/SS/167.ogg"
    ss "Sooo, how's your sister?"
    
    menu:
        "Don't you dare.":
            pf "If you even think about it, I will make you regret ever being born."
    
        "You must have a deathwish.":
            pf "You will have a slow death if you even think about going near her."
    
        "I will end you.":
            pf "Go near her and I promise the last thing you see will be me and my rusty knife."
            
    show shou mis at cc
    voice "audio/voice/E2/D5/SS/168.ogg"
    ss "Those are some pretty harsh words coming from my future brother-in-law."
    
    pf "That's it."
    show frightful:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at cc
    voice "audio/voice/E2/D5/SS/169.ogg"
    ss "Ahh!"
    
    #beep
    stop music fadeout 3
    #fade black
    scene black with fade
    
    "Unfortunately, I can't share what happens next, but rest assured, he will never think about Nikki like that again."
    jump E2D5SS_End
    
    label E2D5SS_End:
        $ E2D5SS_Completed = 1
        stop ambient fadeout 3
        "It's late by the time I get home, and everyone is already asleep. I tiptoe into my room and collapse onto my bed. Exhausted, I fall asleep as soon as my head hits the pillow."
        jump E2D6S1

