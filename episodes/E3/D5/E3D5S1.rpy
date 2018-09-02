#
label E3D5S1:

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
    
    $ meiHairB = "default"
    $ meiOut = "sUniform"
    $ meiHairF = "default"
    
    $ day = 5
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
    
    "I turn off my alarm and stretch, then let out a groan. Yesterday was a really intense day and I'm certainly feeling it now. At least it's Friday. {w}With a regretful sigh, I roll out of bed and prepare for my classes."
    scene black with fade
    stop ambient fadeout 3
    
    if E3D4KI_Embraced == 1:
        "I wonder how Kaori is today..."
        "I'm about to text her when I hesitate. I don't want to seem overbearing. Kaori needs some space to process everything that happened yesterday. I'm confident she'll find me when she's ready."
    
    "I grab a quick breakfast and drive to school."
    
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus auditorium day with fade
    
    "Yuuna is waiting for me in class and smiles broadly when I sit down next to her."
    show yuuna smi at cc with dissolve
    pf "Hi Yuuna."
    show yuuna hap
    voice "audio/voice/E3/D5/S1/yuuna/1.ogg"
    ym "Hey! Sorry we haven't had a chance to catch up. How did your meeting go with Yuri?"
    pf "It wasn't as bad as I anticipated, even though he asked a lot of questions."
    show yuuna neu
    voice "audio/voice/E3/D5/S1/yuuna/2.ogg"
    ym "About Eagle?"
    pf "No, he was interested in my team back at CINY."
    show question:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna cur
    "She blinks in genuine surprise."
    show yuuna ner
    voice "audio/voice/E3/D5/S1/yuuna/3.ogg"
    ym "Oh. I was under the impression he was curious about Eagle..."
    pf "It's okay, I didn't mind. Clearly he did his homework about how teams are run in the States because he didn't seem surprised by anything I shared."
    show yuuna neu
    "Yuuna nods."
    voice "audio/voice/E3/D5/S1/yuuna/4.ogg"
    ym "There's a reason why he's the youngest account manager to manage a team at Dasshu."
    pf "Have you talked with him yet?"
    voice "audio/voice/E3/D5/S1/yuuna/5.ogg"
    ym "Yes."
    show yuuna smi
    voice "audio/voice/E3/D5/S1/yuuna/6.ogg"
    ym "He said you show a lot of promise and he's confident that if the rest of your teammates are as determined as you are then you'll definitely be a force to be reckoned with."
    pf "That's it?"
    show yuuna wor
    "She furrows her brow in concern."
    voice "audio/voice/E3/D5/S1/yuuna/7.ogg"
    ym "Yeah… Should he have said anything else?"
    "I guess he was serious when he said I should talk to her about her brother…"
    "Actually, maybe now isn't the right time to bring up this conversation."
    
    menu:
        "It's time I asked.":
            stop music fadeout 3
            $ E3D5S1_YuunaAsked = 1
            pf "Well, we had a good conversation… but there was one thing he said that stood out."
            show yuuna ner
            voice "audio/voice/E3/D5/S1/yuuna/8.ogg"
            ym "What is it?"
            "I hesitate, trying to think of the most delicate way to put this."
            pf "I know that you didn't find Dasshu through the SBA."
            show yuuna sur
            "She opens her mouth to speak, but I shake my head."
            pf "And I know how difficult this must have been for you to reach out to them."
            show yuuna neu
            "She gazes at her lap."
            pf "I'm grateful that you did, but why didn't you tell me?"
    
            if yuunaSocialLink >= 4:
                show yuuna wor
                voice "audio/voice/E3/D5/S1/yuuna/9.ogg"
                ym "I'm sorry."
                pf "The team knows what happened to your brother, don't they?"
                show yuuna sad
                "She nods slowly."
                voice "audio/voice/E3/D5/S1/yuuna/10.ogg"
                ym "Everyone does. His accident was during a match at school."
                pf "You should have told me. We could have kept searching for a sponsor."
                show yuuna neu
                voice "audio/voice/E3/D5/S1/yuuna/11.ogg"
                ym "No, Dasshu was great to my brother. I knew they would be good for you too."
                pf "But they're a constant reminder of what happened to him."
                show yuuna ner
                "She finally meets my eyes."
                voice "audio/voice/E3/D5/S1/yuuna/12.ogg"
                ym "I'm sorry I didn't tell you, but I'll be fine."
                show yuuna neu
                voice "audio/voice/E3/D5/S1/yuuna/13.ogg"
                ym "Anyway, we should talk about this later. The professor is here."
                "I glance at the front of the room and see the professor setting up."
                pf "Okay." 
    
            else:
                voice "audio/voice/E3/D5/S1/yuuna/14.ogg"
                ym "It wasn't relevant."
                pf "The team knows what happened to your brother, don't they? I'm the only one who doesn't."
                show yuuna sad
                "She falls silent."
                pf "What happened?"
                voice "audio/voice/E3/D5/S1/yuuna/15.ogg"
                ym "...It was an accident during a match."
                pf "How is that not relevant?"
                show yuuna dis
                "Her voice grows cold."
                voice "audio/voice/E3/D5/S1/yuuna/16.ogg"
                ym "I don't think now is an appropriate time to talk about this."
                pf "Yuuna..."
                show yuuna neu
                "She stares straight ahead."
                voice "audio/voice/E3/D5/S1/yuuna/17.ogg"
                ym "The professor is here. Class is going to start soon."
                "The professor just entered the room and is getting settled. We still have a few minutes, but it's obvious I'm not going to get anything more out of her now."
                pf "Alright, I'll drop it for now but we'll finish this conversation later."
                "She nods."
    
        "Let's talk about it later.":
            show yuuna smi
            "Bombarding her right before class begins doesn't seem like very smart timing. The professor will get here and start class before we really have a chance to talk and Yuuna will probably spend all of class stressing out about this."
    
            menu:
                "Just checking.":
                    pf "We had a good conversation so I was just wondering if he had any other thoughts."
                    show yuuna neu
                    voice "audio/voice/E3/D5/S1/yuuna/18.ogg"
                    ym "Oh, no. But I'm glad to hear you enjoyed the conversation too."
                    pf "He seems like he'll be easy to work with."
                    show yuuna smi
                    "Yuuna nods."
                    voice "audio/voice/E3/D5/S1/yuuna/19.ogg"
                    ym "He is."
                    "I glance at her, and nod."
    
                "Yeah, how he's clearly into me.":
                    pf "I mean, he was asking me a {i}lot{/i} of questions…"
                    show drop:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/D5/S1/yuuna/20.ogg"
                    ym "Is that bad?"
                    pf "No, but clearly he was trying to get to me know me {i}pretty{/i} well."
                    show yuuna ske
                    voice "audio/voice/E3/D5/S1/yuuna/21.ogg"
                    ym "I don't understand. Wasn't that the point of meeting you?"
                    "I sigh."
                    pf "Yes, yes it was."
    
                "No.":
                    pf "Nope."
                    show yuuna neu
                    voice "audio/voice/E3/D5/S1/yuuna/22.ogg"
                    ym "Oh. Um, okay."
                    "We both fall silent."
                    
    hide yuuna with dissolve
    "The professor enters the room and gets settled."
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E3/D5/S1/prof2f/1.ogg"
    prof2f "Good morning, everyone! Please open your textbooks to page 81…"
    
    scene black with fade
    stop music fadeout 5
    #fade out
    $renpy.pause(1)
    #fade in
    scene bg campus auditorium day with fade
    show professorM2 extra at cc with dissolve
    voice "audio/voice/E3/D5/S1/prof2f/2.ogg"
    prof2f "Your assignments are on the weblink. Have a great day!"
    play sound "audio/sfx/Human/Class End.ogg"
    hide professorM2 with dissolve
    "Yuuna and I pack up our things and walk out of class together."
    
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    show yuuna smi at cc with dissolve
    
    if E3D5S1_YuunaAsked == 1 and yuufriend < 4:
        "She's quiet as we walk. When I turn to face her, her smile seems forced."
    
    pf "Do you have another class to go to?"
    voice "audio/voice/E3/D5/S1/yuuna/23.ogg"
    ym "No, but I have to meet my physiotherapy professor. I'm a TA for his class."
    
    if E3D5S1_YuunaAsked == 1 and yuufriend < 4:
        voice "audio/voice/E3/D5/S1/yuuna/24.ogg"
        ym "I'll see you later."
        pf "Oh, okay. Bye."
        hide yuuna with dissolve
        "She left as soon as I said goodbye."
    
    else:
        pf "I didn't know you were a TA."
        show yuuna hap
        voice "audio/voice/E3/D5/S1/yuuna/25.ogg"
        ym "Yup! I don't usually help out in his Friday classes but he's holding exams today so I need to be there."
        show yuuna smi
        voice "audio/voice/E3/D5/S1/yuuna/26.ogg"
        ym "Do you have any other classes?"
        pf "No, but I'm kind of hungry. I'll grab lunch in the Pilot's Lounge."
        show yuuna cur
        "Her face lights up."
        voice "audio/voice/E3/D5/S1/yuuna/27.ogg"
        ym "Oh, you're lucky! They're supposed to have really good food."
    
        if E2KIS1_Completed == 1 and E2YMS4_Completed == 1:
            "I grin."
            pf "They do… and they even have burgers!"
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur
            "Yuuna's eyes grow wide."
            voice "audio/voice/E3/D5/S1/yuuna/28.ogg"
            ym "Are they better than the ones we had?"
    
            menu:
                "No.":
                    pf "Eh, they aren't better, but they aren't bad either."
    
                "Nothing's better than what we had.":
                    "I gaze gently into her eyes."
                    pf "Nothing can compare to what we had."
                    show yuuna ske
                    "She gives me a strange look."
                    voice "audio/voice/E3/D5/S1/yuuna/29.ogg"
                    ym "Um, okay?"
    
                "A million times, yes.":
                    pf "These are way better! What we had last time wasn't even edible."
                    show yuuna ner
                    voice "audio/voice/E3/D5/S1/yuuna/30.ogg"
                    ym "I didn't think they were bad… but that must mean these are amazing!"
    
            show yuuna sad
            "Yuuna pouts."
            voice "audio/voice/E3/D5/S1/yuuna/31.ogg"
            ym "Aw, I wish I could try them."
            pf "Maybe I'll smuggle one out for you."
            show yuuna cur
            voice "audio/voice/E3/D5/S1/yuuna/32.ogg"
            ym "Really?"
            show shiny:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            "I'm taken aback by her hopeful gaze."
            pf "Um, uh, I guess if they have them I will. They don't have them everyday."
            show yuuna hap
            "She beams."
            voice "audio/voice/E3/D5/S1/yuuna/33.ogg"
            ym "That would be great!"
    
        elif E2KIS1_Completed == 1 and E2YMS4_Completed == 0:
            pf "They do, and they have options from other countries. I had a cheeseburger once from there."
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur
            "Yuunas eyes grow wide."
            voice "audio/voice/E3/D5/S1/yuuna/34.ogg"
            ym "I love cheeseburgers!"
            pf "Doesn't the dining hall serve them too?"
            show yuuna thi
            "She wrinkles her nose."
            voice "audio/voice/E3/D5/S1/yuuna/35.ogg"
            ym "I don't think what they serve in the dining hall can even be considered food."
            pf "Where do you eat lunch?"
            show yuuna hap
            voice "audio/voice/E3/D5/S1/yuuna/36.ogg"
            ym "The hot dog cart!"
            "Oh yeah. I forgot we had a hotdog stand."
            pf "I didn't know anyone actually ate there..."
            show yuuna smi
            voice "audio/voice/E3/D5/S1/yuuna/37.ogg"
            ym "You should try it! They're so good!"
            pf "You really like American food, don't you?"
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna hap
            voice "audio/voice/E3/D5/S1/yuuna/38.ogg"
            ym "Yes!"
    
        elif E2KIS1_Completed == 0 and E2YMS4_Completed == 1:
            pf "I've heard that too but I haven't tried it yet."
            show question:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna sur
            voice "audio/voice/E3/D5/S1/yuuna/39.ogg"
            ym "Really? I'm surprised given how much time you pilots spend there."
            pf "I usually bring leftovers for lunch or eat at the dining hall or wherever is closest."
            show yuuna neu
            voice "audio/voice/E3/D5/S1/yuuna/40.ogg"
            ym "Ah, well, you'll have to tell me how it is. I think sometimes they even serve western food."
            "I grin."
            pf "If I see a burger on the menu I will try it and report back."
            show yuuna smi
            "She matches my grin."
            voice "audio/voice/E3/D5/S1/yuuna/41.ogg"
            ym "That's all I ask."
    
        else:
            pf "I've heard that too, but I haven't had a chance to try it yet."
            show yuuna smi
            voice "audio/voice/E3/D5/S1/yuuna/42.ogg"
            ym "I wish I could try it too, but it's hard for me to get into the Pilot's Lounge. You will have to try it for the both of us!"
            pf "Will do."
    
        show yuuna neu
        "Yuuna checks the time."
        show panic:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna cur
        voice "audio/voice/E3/D5/S1/yuuna/43.ogg"
        ym "Oops! I'm going to be late- I'll see you later!"
        show yuuna smi
        pf "Bye."
        hide yuuna with dissolve
        "I wave as she dashes off."
        
    stop music fadeout 3
    "Alone, I make my way to the Pilot's Lounge."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    
    jump E3D5S2