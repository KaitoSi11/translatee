#
label E2VBS3:
    
    #Event 3 - Afternoon Choice (>65 Points AND NOT DAY4)
    
    scene black with fade
    stop ambient fadeout 2
    stop music fadeout 2    
    scene bg campus lounge day with fade
    
    
    "I decide to relax in the Pilot's Lounge."
    
    "After grabbing a drink at the bar, I sit at the tables to watch the game, but a familiar face at a nearby table distracts me."
    "Is that who I think it is?"
    "I make my way over and sit across from a petite girl with long blonde hair."
    
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5.0
    show valerie smi at cc with dissolve
    
    pf "Valerie."
    show valerie hap at cc
    "Her face lights up when she sees me."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO77.ogg"
    vb "What are the chances of us running into each other here?"
    pf "I was about to ask you the same thing."
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO78.ogg"
    vb "It must be fate."
    pf "How did you get into the Pilot's Lounge? Only pilots have access. Did \"fate\" let you in?"
    show valerie smi at cc
    "She laughs, then points to the bar."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO79.ogg"
    vb "No, that guy did."
    "The man she points to is a tall pilot with dark hair."
    "How old is Valerie again? She's only a first year so she definitely isn't old enough to legally drink. What does this guy think he's doing?"
    "I watch as he pays the bartender and carries two beers back to our table. As he places one of the beers in front of Valerie, he frowns at me."
    show bully2 extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E2/Free/VB/stu8m/1.ogg"
    stu8m "Who are you?"
    pf "Someone who knows better."
    voice "audio/voice/E2/Free/VB/stu8m/2.ogg"
    stu8m "What does that mean?"
    
    menu:
        "He's serving drinks to a minor!":
            pf "Ignoring the fact that she doesn't belong in the Pilot's Lounge since she's not a pilot, you're breaking both school policy and {i}the law{/i} by serving her alcohol."
            voice "audio/voice/E2/Free/VB/stu8m/3.ogg"
            stu8m "She told me she can drink."
            pf "It doesn't surprise me that a first year would tell you that."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie cur at cc
            "The pilot whirls on Valerie."
    
        "He has no idea…":
            pf "Nevermind. Have a seat."
            "Cautiously, he sits down and passes Valerie her drink. Before she can take a sip, I turn to her."
            pf "So, how are you liking it here at ACE so far?"
            show note:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO80.ogg"
            vb "It's great, of course! There's so much to learn and see."
            pf "You're not feeling homesick?"
            show valerie smi at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO81.ogg"
            vb "No."
            pf "That's good. Your first year from home is always the hardest."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie cur at cc
            "The pilot stands up, nearly knocking over his chair."
    
        "Who does this chump think he is?":
            pf "Are you so bad with women you're resorting to preying on underage girls? Have some respect, man."
            voice "audio/voice/E2/Free/VB/stu8m/4.ogg"
            stu8m "What do you mean she's underage? She told me she can drink."
            pf "I'm sure that defense will go over well when the police arrest you for serving alcohol to a minor. She's only a first year."
            "The pilot frowns."
            
    voice "audio/voice/E2/Free/VB/stu8m/5.ogg"
    stu8m "First year?"
    show valerie hap at cc
    "Valerie smiles."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO82.ogg"
    vb "Is that a problem?"
    voice "audio/voice/E2/Free/VB/stu8m/6.ogg"
    stu8m "Why did you tell me you can drink?"
    show drop:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie thi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO83.ogg"
    vb "I can… back in France."
    voice "audio/voice/E2/Free/VB/stu8m/7.ogg"
    stu8m "I'm not trying to get into trouble. Just forget about this."
    hide bully2 with dissolve
    show valerie neu at cc with dissolve
    "Valerie shrugs as he walks away."
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO84.ogg"
    vb "At least I got my drink."
    pf "Nope."
    show valerie cur at cc
    "I intercept the beverage before she can drink it."
    show exclamation:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie sur at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO85.ogg"
    vb "Hey! That's mine."
    pf "Weren't you paying attention? You're underage. You can't drink."
    show storm:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie dis at cc
    "She crosses her arms and pouts."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO86.ogg"
    vb "That's not fair. I've been drinking since I was 18. It's silly that because the age is so high here I can't drink anymore."
    pf "I get that you're frustrated, but the school is very strict about its policies. If you're caught breaking the law the consequences would be bad."
    show valerie neu at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO87.ogg"
    vb "How bad can it be?"
    pf "Like {i}expelled{/i} bad. They're very careful, especially here in the Pilot's Lounge where there is a grade that can't drink."
    show valerie mis at cc
    "Valerie's look softens, then her mischevious grin returns."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO88.ogg"
    vb "Hmph. I understand what you're saying, but I think you scared away my date not for my protection but because you wanted me all to yourself."
    
    menu:
        "You've got it all wrong!":
            pf "I-It's not like that!"
            show valerie ske at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO89.ogg"
            vb "No?"
            pf "I wasn't trying to scare him!"
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO90.ogg"
            vb "Oh, really? That's too bad."
            pf "Eh?!"
            show valerie hap at cc
            "She laughs at my expression."
    
        "I'm pretty irresistible myself.":
            pf "It seems the feeling is mutual."
            show valerie ske at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO91.ogg"
            vb "What gives you that idea?"
            pf "Well, you haven't left yet. I think someone enjoys my company very much."
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO92.ogg"
            vb "Oh yeah? You're imagining things!"
            show valerie hap at cc
            "She pretends to be disinterested, but she's still here, smiling at me."
    
        "Don't flatter yourself.":
            "I snort."
            pf "I just need you to stay in school and out of trouble long enough for us to complete our assignment. After that you can do whatever you want."
            show valerie ske at cc
            "Valerie smirks and leans over the table."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO93.ogg"
            vb "You've been thinking about our date then?"
            pf "It's not a date."
            show valerie mis at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO94.ogg"
            vb "But you didn't deny thinking about it."
            pf "Whatever."
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO95.ogg"
            vb "I'm looking forward to it too."
            
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO96.ogg"
    vb "Well, you confiscated my drink and scared away my date. Guess there isn't anything left to keep me here."
    "She stands to leave, but I stop her."
    show valerie cur at cc
    pf "I was planning on watching the match… Would you want to watch with me?"
    show valerie smi at cc
    "She sits back down and puts her elbows on the table, resting her face in her hands."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO97.ogg"
    vb "That depends. Will you get me a drink?"
    pf "Uh--"
    show valerie hap at cc
    ##MISSINGLINE##
    voice "audio/voice/E2/missing/valerie/2.ogg"
    vb "A soda please. What kind of girl do you think I am?"
    "I match her smile and stand."
    pf "Sure."
    #black screen
    scene black with fade
    stop music fadeout 3
    "We spend some time together until I have to leave for class."
    stop ambient fadeout 3
    $renpy.pause(1)
    $ E2VBS3_Completed = 1

