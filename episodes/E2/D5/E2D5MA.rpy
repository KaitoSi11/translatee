#
label E2D5MA:
    
    $ E2D5MA_MayuScene = 1
    show mayu ner at l2
    show shou hap at r2
    with dissolve
    "Making my way back to the living room, I spot Mayu standing awkwardly to the side while Shou chats with his brosephs."
    show drop:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    "He's shaking his head as if refusing an invitation, but his friends are persistent and won't take no for an answer."
    show panic:
        xoffset 365
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu sur at l2
    show exclamation:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at r2
    "When they realise Shou won't go willingly with them, they literally pick him up and carry him away."
    hide shou with dissolve
    show mayu wor at l2 with dissolve
    "Shou waves helplessly at Mayu, who waves back at Shou."
    show mayu ner at l2
    "She seems really nervous to be left on her own."
    show bully3 extra at r2 with dissolve:
        xzoom -1
    "As I walk over to keep her company, some guy from another dorm swoops in, two drinks in hand."
    show mayu cur at l2
    voice "audio/voice/E2/D5/MA/fbro1/1.ogg"
    fbro1 "A pretty girl like you shouldn't be hanging out alone."
    show mayu ner at l2
    "Mayu shrinks away as the guy leans in."
    voice "audio/voice/E2/D5/MA/0-57.ogg"
    ma "I wasn't alone. I was just talking to my friend."
    voice "audio/voice/E2/D5/MA/fbro1/2.ogg"
    fbro1 "Oh yeah? Where is he?"
    show drop:
        xoffset 365
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D5/MA/0-58.ogg"
    ma "Oh… um…"
    voice "audio/voice/E2/D5/MA/fbro1/3.ogg"
    fbro1 "Sorry, I didn't mean to put you on the spot. Why don't you come enjoy the party with me?"
    show mayu thi at l2
    voice "audio/voice/E2/D5/MA/0-59.ogg"
    ma "Um, I don't know… I should probably wait for my friend to get back…"
    stop music fadeout 3
    "He offers her one of the drinks in her hand."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E2/D5/MA/fbro1/4.ogg"
    fbro1 "Sure, I get it. Why don't I keep you company until he gets back? Here, I noticed you're empty handed so brought you a drink."
    show mayu neu at l2
    voice "audio/voice/E2/D5/MA/0-60.ogg"
    ma "That's nice of you, but I don't drink."
    "He laughs."
    voice "audio/voice/E2/D5/MA/fbro1/5.ogg"
    fbro1 "Just one drink, I promise, then I'll leave you alone."
    show mayu wor at l2
    voice "audio/voice/E2/D5/MA/0-61.ogg"
    ma "No, thank you. Really, I don't drink."
    voice "audio/voice/E2/D5/MA/fbro1/6.ogg"
    fbro1 "C'mon, live a little! What harm can it do?"
    show mayu ner at l2
    "Mayu shuffles uncomfortably from the man's insistence."
    
    menu:
        "Pretend to be her boyfriend.":
            "I throw a protective arm around Mayu."
            show exclamation:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur at l2
            pf "Hey, sorry to keep you waiting."
            show mayu cur at l2
            "Mayu blinks at me in surprise. The other guy narrows his eyes."
            voice "audio/voice/E2/D5/MA/fbro1/7.ogg"
            fbro1 "Who the hell are you?"
            show mayu wor at l2
            pf "I'm her boyfriend. Who are you?"
            "He looks at the two of us and laughs."
            voice "audio/voice/E2/D5/MA/fbro1/8.ogg"
            fbro1 "You've got to be kidding me. {i}This{/i} is your boyfriend?"
    
            ### NOTE Points - "IF high points with Mayu:"
            # temporarily set to 0
            if mayfriend > 0:
                show mayu neu at l2
                "Mayu glances at me again, then steels her resolve and nods once, leaning into me."
                show mayu smi at l2
                voice "audio/voice/E2/D5/MA/0-62.ogg"
                ma "Yes."
                "Even though I started this charade, I can feel myself growing warm from Mayu's reaction."
    
            else:
                show mayu ner at l2
                "Mayu fidgets slightly."
                voice "audio/voice/E2/D5/MA/0-63.ogg"
                ma "Uh, well, it's--"
                "I tighten my arm around her, and she falls silent."
                show dots:
                    xoffset 365
                    yoffset 135
                    xzoom .75
                    yzoom .75
                pf "Yes, I am. You got a problem with that?"
    
            voice "audio/voice/E2/D5/MA/fbro1/9.ogg"
            fbro1 "Forget it. This isn't worth the trouble."
    
        "Accept the drink for yourself.":
            "I reach out from behind him and pluck the drink from his hand."
            show exclamation:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur at l2
            pf "Wow, is this for me? Thanks, that's so nice of you!"
            show mayu cur at l2
            voice "audio/voice/E2/D5/MA/fbro1/10.ogg"
            fbro1 "Uh…"
            "While the guy is still stunned, I take a sip."
            pf "How did you know this was my favourite?"
            show mayu wor at l2
            voice "audio/voice/E2/D5/MA/fbro1/11.ogg"
            fbro1 "What? No, this was for her!"
            "He points at Mayu."
            pf "Really? Well, why did you give it to me then?"
            show mayu neu at l2
            voice "audio/voice/E2/D5/MA/fbro1/12.ogg"
            fbro1 "I didn't!"
            "I laugh and flash him a smile."
            pf "It's okay, you don't have to be shy."
            "He grimaces and takes a step back."
            voice "audio/voice/E2/D5/MA/fbro1/13.ogg"
            fbro1 "Ugh, I'm not drunk enough to deal with this weirdo."
    
        "Stand up for Mayu!":
            show mayu sur at l2
            pf "You heard her. She doesn't want to drink so back off."
            show mayu cur at l2
            voice "audio/voice/E2/D5/MA/fbro1/14.ogg"
            fbro1 "Hey, calm down. We were just having a friendly conversation, right?"
            show mayu ner at l2
            "Mayu refuses to meet his eyes."
            pf "Do you know this guy, Mayu?"
            show mayu neu at l2
            "She shakes her head."
            voice "audio/voice/E2/D5/MA/0-64.ogg"
            ma "No."
            voice "audio/voice/E2/D5/MA/fbro1/15.ogg"
            fbro1 "It's cool, I was just keeping her company until her friend gets back."
            pf "Well, I'm back now, and I think you should go."
            voice "audio/voice/E2/D5/MA/fbro1/16.ogg"
            fbro1 "Whatever, she's boring anyway."
            
    hide bully3 with dissolve
    stop music fadeout 3
    "With a huff, he walks away. {w}Mayu breathes a sigh of relief."
    show mayu smi at cc with dissolve
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E2/D5/MA/0-65.ogg"
    ma "Thanks."
    show mayu smi at cc
    pf "No problem."
    show mayu ner at cc
    "We stand side by side against a wall while the party rages on around us. Mayu has her hands folded and is pointedly looking away from me. I focus on my drink."
    pf "So, parties aren't really your thing, huh?"
    show mayu cur at cc
    "She blinks at me and meets my eyes, then shyly looks away."
    show mayu thi at cc
    voice "audio/voice/E2/D5/MA/0-66.ogg"
    ma "What makes you say that?"
    pf "I don't mean that in a bad way. It's just that you don't seem too comfortable."
    show mayu smi at cc
    "She let's out a small laugh."
    voice "audio/voice/E2/D5/MA/0-67.ogg"
    ma "I guess not. This is more something that Shou enjoys and I just come along to keep him company."
    show mayu neu at cc
    "She gives me a sidelong glance."
    voice "audio/voice/E2/D5/MA/0-68.ogg"
    ma "What about you? Is this your scene?"
    
    menu:
        "They're okay.":
            "I shrug."
            pf "If I'm in the mood for them I think they're fun."
            show mayu smi at cc
            voice "audio/voice/E2/D5/MA/0-69.ogg"
            ma "I know what you mean. Small parties aren't too bad, but a big one like this--"
            show mayu sur at cc
            # sfx? perhaps luggage drop or kaori fall?
            "A loud crash interrupts Mayu as someone tumbles over a chair. {w}A roar of laughter follows while the guy tries to get back on his feet."
            show mayu wor at cc
            pf "Yeah, this can be a little overwhelming."
            show mayu neu at cc
            "Mayu nods."
    
        "You bet it is!":
            pf "What's better than a party? It's got my three favourites activities."
            show mayu cur at cc
            voice "audio/voice/E2/D5/MA/0-70.ogg"
            ma "And what's that?"
            pf "Good music, good drinks, and good..."
            show mayu neu at cc
            "My voice trails off as a couple of girls wearing tight skirts walk past. One of them smiles at me."
            show mayu ner at cc
            "Mayu follows my gaze and I clear my throat."
            pf "Um, and good times."
            show mayu neu at cc
            voice "audio/voice/E2/D5/MA/0-71.ogg"
            ma "Right."
    
        "What a waste of time.":
            pf "Nah. I'd rather be doing something more productive with my time."
            show mayu cur at cc
            voice "audio/voice/E2/D5/MA/0-72.ogg"
            ma "Like what?"
    
            if MCStory == 1:
                pf "Probably something active, that gets the blood pumping."
    
            elif MCStory == 2:
                pf "I could be using this time to study."
    
            else:
                pf "Anything, really."
    
            show mayu neu at cc
            voice "audio/voice/E2/D5/MA/0-73.ogg"
            ma "Oh, I see."
    
    pf "So, if this isn't really your thing, what kind of thing do you like?"
    show mayu cur at cc
    voice "audio/voice/E2/D5/MA/0-74.ogg"
    ma "Well, I like reading."
    pf "You mean like studying?"
    show mayu smi at cc
    voice "audio/voice/E2/D5/MA/0-75.ogg"
    ma "No, like novels, especially fantasy novels."
    pf "How come?"
    show mayu hap at cc
    voice "audio/voice/E2/D5/MA/0-76.ogg"
    ma "Because they have the most fantastic worlds! It's always so different, and when I'm reading I feel like I'm there exploring the same magical place they are. In those worlds, anything can happen. There are no rules."
    "Mayu grins and for once there's a spark in her eyes. It's kind of nice to see this side of her."
    show mayu smi at cc
    pf "Heh, I had no idea you were such a bookworm."
    
    if MCStory == 2:
        pf "I like to read too, but I prefer science fiction."
        show mayu cur at cc
        voice "audio/voice/E2/D5/MA/0-77.ogg"
        ma "Really? How come?"
        pf "The technology in those books are so advanced. It's fun to think that maybe one day what's written on the page will be something we use in real life too."
        show mayu smi at cc
        voice "audio/voice/E2/D5/MA/0-78.ogg"
        ma "I've never considered that before. That would be cool."
    
    pf "What else do you like?"
    show mayu ner at cc
    "She hesitates."
    voice "audio/voice/E2/D5/MA/0-79.ogg"
    ma "Promise you won't make fun of me?"
    pf "Of course I won't."
    show mayu wor at cc
    voice "audio/voice/E2/D5/MA/0-80.ogg"
    ma "I-I really like to play chess."
    pf "You do?"
    show mayu neu at cc
    "She nods."
    pf "Oh…"
    show mayu ner at cc
    "She looks back down to the ground and shuffles her feet."
    voice "audio/voice/E2/D5/MA/0-81.ogg"
    ma "It's stupid, I know."
    pf "No, it's not!"
    show mayu cur at cc
    "She glances up at me in surprise."
    pf "Does Shou usually play against you?"
    show mayu neu at cc
    voice "audio/voice/E2/D5/MA/0-82.ogg"
    ma "No, he thinks it's boring. It's too slow."
    pf "Who do you play against?"
    show mayu thi at cc
    "Mayu shrugs."
    pf "Well, maybe we can play sometime."
    show mayu hap at cc
    "The sparkle returns to her eyes."
    voice "audio/voice/E2/D5/MA/0-83.ogg"
    ma "You think so?"
    pf "Sure."
    show mayu smi at cc
    
    if MCStory != 2:
        pf "I haven't played in a while, so I hope you don't mind giving a refresher."
        show mayu hap at cc
        voice "audio/voice/E2/D5/MA/0-84.ogg"
        ma "I'd be happy to!"
    
    else:
        pf "I've played a few times, so don't expect me to go easy on you."
        show mayu mis at cc
        "She laughs."
        show note:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D5/MA/0-85.ogg"
        ma "I don't shy away from a challenge!"
        "She's a lot more confident when she's in her element."
        
    show mayu cur at cc
    "Mayu stares at the sea of faces in the crowd and spots Shou waving at us."
    show mayu smi at cc
    ##VOICEMISSING##
    ma "We should probably head over and see what he wants."
    pf "Yeah."
    show mayu hap at cc
    voice "audio/voice/E2/D5/MA/0-86.ogg"
    ma "Thanks for keeping me company."
    pf "What are friends for?"
    show regBlush:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu smi b1 at cc with dissolve
    $renpy.pause(.5)
    hide mayu with dissolve
    "She rubs at her arm shyly, then gestures for me to follow before disappearing into the crowd."
    #fade to black
    scene black with fade
    stop music fadeout 5
    "The rest of the party is a whirlwind of music and laughter."
    jump E2D5MA_End
    
    label E2D5MA_End:
        $ E2D5MA_Completed = 1
        stop ambient fadeout 3
        "It's late by the time I get home, and everyone is already asleep. I tiptoe into my room and collapse onto my bed. Exhausted, I fall asleep as soon as my head hits the pillow."
        jump E2D6S1

