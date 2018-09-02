# E2D1S3
label E2D1S3:
    
    #Evening choice end
    
    scene black with fade
    stop ambient fadeout 3
    stop music fadeout 3
    $renpy.pause(2.5)
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with fade
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    
    "When I get home, Uncle Kaito is lounging on the couch with his feet up on the coffee table and staring intently at his laptop. {w}Mountains of papers and folders surround him, with a few loose pieces strewn across the floor."
    show kaito ner at cc with dissolve
    pf "Hey Uncle, is Nikki home?"
    
    # papers scattering sfx?
    # maybe shake kaito?
    show kaito sur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    
    "Clearly startled, Kaito spins to face me and loses the rest of his papers in a scattered mess."
    show kaito neu at cc with dissolve
    "He rubs at his eyes before letting out a resigned sigh, and kneels to pick them up."
    "I bend down to help."
    pf "Sorry, I didn't mean to scare you."
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/1.ogg"
    hk "It's not your fault. Sometimes this house can be too quiet."
    pf "Quiet? I guess that means Nikki isn't home."
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito mis at cc
    "He gives me a weak smile. {w}I can tell he's tired. Kaito's been working late almost every night since Nikki and I arrived… I hope he's not overworking himself."
    "I hand back all the papers I collected and he begins sorting them into folders again."
    pf "Can I help?"
    show kaito cur at cc
    "He hesitates, then shakes his head."
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/2.ogg"
    hk "Thanks, bud, but I've got it."
    "I sit beside him anyway."
    pf "What are you working on?"
    show kaito neu at cc
    voice "audio/voice/E2/D1/S3/Kaito/3.ogg"
    hk "Just some work stuff."
    pf "Right."
    "... Actually, now that I think about it, I don't really know what Uncle Kaito does for a living."
    pf "What kind of work stuff?"
    voice "audio/voice/E2/D1/S3/Kaito/4.ogg"
    hk "A lot of things."
    
    menu:
        "He's being awfully evasive with his answers…":
            pf "Is it a secret?"
            show kaito cur at cc
            voice "audio/voice/E2/D1/S3/Kaito/5.ogg"
            hk "Huh?"
            pf "What you're doing… Is it a secret?"
            show kaito ske at cc
            voice "audio/voice/E2/D1/S3/Kaito/6.ogg"
            hk "No, of course not."
            pf "Well, getting info from you is a little like pulling teeth…"
            show kaito hap at cc
            "He laughs."
            # drop emote
            show drop:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/S3/Kaito/7.ogg"
            hk "Sorry, I'm just looking over the contracts for the restaurant."
        
        "I knew it! He's a secret agent!":
            pf "Ahhh, I see."
            show kaito cur at cc
            voice "audio/voice/E2/D1/S3/Kaito/8.ogg"
            hk "See what?"
            pf "Don't worry, I'll keep your secret safe."
            show kaito ske at cc
            voice "audio/voice/E2/D1/S3/Kaito/9.ogg"
            hk "What secret? I'm just looking over our contracts right now for the restaurant."
            "I knowingly tap my nose."
            pf "Mmhm, \"contracts\"... for the \"restaurant\"."
            "I know he means \"secret information for the government\"."
            show dots:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            "Kaito gives me a weird look."
            show kaito ner at cc
            voice "audio/voice/E2/D1/S3/Kaito/10.ogg"
            hk "Yeah… contracts for the restaurant."
            pf "I get you."
        
        "Okay, I can take a hint.":
            "I fall silent, not wanting to disturb him any further. {w}After a few seconds, Kaito glances at me."
            show kaito ner at cc
            voice "audio/voice/E2/D1/S3/Kaito/11.ogg"
            hk "You okay?"
            pf "Yeah, I just didn't want to bother you. I can tell you're busy."
            show kaito hap at cc
            voice "audio/voice/E2/D1/S3/Kaito/12.ogg"
            hk "Oh no, you're not bothering me. I'm just a little distracted since I'm doing a final look at our contracts for the restaurant."
    
    "Although that being said..."
    pf "Contracts? Don't you have a department that handles those?"
    show kaito neu at cc
    voice "audio/voice/E2/D1/S3/Kaito/13.ogg"
    hk "Yeah, we do, but as Regional Manager, I have to look at them first to make sure they include everything we discussed. Then I send it to the deal desk to make sure all the legalese is correct and that there are no hidden clauses."
    "He pats the pile of papers closest to him."
    voice "audio/voice/E2/D1/S3/Kaito/14.ogg"
    hk "We're opening up a new cafe in the next month, hence all the new contracts."
    pf "Oh really?"
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/15.ogg"
    hk "Yeah… Actually, it won't be too far away. You know that empty lot in the strip mall?"
    pf "The one that's been under construction?"
    show kaito hap at cc
    voice "audio/voice/E2/D1/S3/Kaito/16.ogg"
    hk "Yup, that's where it'll be."
    pf "That's pretty close. I'll have to stop by after it opens and check it out."
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/17.ogg"
    hk "Sure. Have you been to any of our other restaurants yet?"
    
    menu:
        "Please do not be disappoint.":
            "I put on my best apologetic grin and rub the back of my head."
            pf "Um, not exactly."
            "Kaito just smiles at me."
            show kaito hap at cc
            voice "audio/voice/E2/D1/S3/Kaito/18.ogg"
            hk "That's okay. You've been pretty busy, but you should check them out. They're pretty good, if I do say so myself."
            pf "Heh, sure."
        
        "Time to wing it!":
            pf "Uh, yeah! Of course I've been to a restaurant managed by my favourite uncle."
            show kaito mis at cc
            voice "audio/voice/E2/D1/S3/Kaito/19.ogg"
            hk "Yeah? Did you like it?"
            pf "Yes! It was great! I had a… {w}coffee. {w}But a really good one!"
            show kaito cur at cc
            voice "audio/voice/E2/D1/S3/Kaito/20.ogg"
            hk "Huh, that's awesome. Which one did you go to? I'm sure they'd be happy to hear that."
            pf "Oh… {w}you know, that… {w}cafe? {w}Near the harbour?"
            show kaito ske at cc
            show question:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            "He crosses his arms."
            voice "audio/voice/E2/D1/S3/Kaito/21.ogg"
            hk "You've never been before, have you?"
            show kaito neu at cc
            "I hang my head."
            pf "No, I haven't."
        
        "I didn't even know you managed restaurants until now.":
            pf "I didn't know you had restaurants."
            show kaito cur at cc
            show question:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/S3/Kaito/22.ogg"
            hk "Really? When you were little, I used to take you there when you visited. Don't you remember?"
            pf "Kind of… but I didn't know those were {i}your{/i} restaurants."
            show kaito smi at cc
            voice "audio/voice/E2/D1/S3/Kaito/missing.ogg"
            hk "I used to bring you food straight from the kitchen."
            pf "I was five. I thought everyone did that."
            show kaito hap at cc
            "He laughs."
            voice "audio/voice/E2/D1/S3/Kaito/23.ogg"
            hk "Fair point."
    
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/24.ogg"
    hk "Well, if you get a chance, you should try the place near the park. It serves western style cuisine and is very popular in Isokaze. I know it won't be exactly like the food you had back in the States, but I'd be curious to see how you like it."
    pf "Sure, that sounds great."
    show kaito hap at cc
    "He grins at me, before turning back to his stack. I should probably let him work."
    pf "I'm going to go upstairs. Good luck with all of this."
    show kaito smi at cc
    voice "audio/voice/E2/D1/S3/Kaito/25.ogg"
    hk "Thanks!"
    
    scene black with fade
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    stop music fadeout 3
    $renpy.pause(2.5)
    scene bg homekaito myroom night with fade
    
    "I head to my room and do another quick search on the SBA… {w}Then decide to check out what other clubs are at ACE. It looks like there's a club for everything: tennis, cooking, business, culture, etc."
    "At some point, I vaguely hear voices downstairs. {w}Nikki must be home. {w}After a quick convo, she comes upstairs and I hear her shut the door to her room."
    "I continue surfing the net, but after a while, my eyelids start to droop, and I crawl into bed before drifting to sleep."
    scene black with fade
    stop ambient fadeout 3
    
    jump E2D2S1

