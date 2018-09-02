#
label E4D2S3:
    
    $ kaoHairF = "tied"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sCasual"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sCasual"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sCasual"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sCasual"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sCasual"
    
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    show bg campus lounge night with fade
    "Akira rejoins his teammates while Shou and I change back into our clothes. We wait for the girls in the hotel lobby."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    show shou neu at cc with dissolve
    pf "We agreed to meet here for dinner, right?"
    "Shou answers nervously."
    voice "audio/voice/E4/Shou/d2/68 Copy.ogg"
    ss "Yup."
    "After 15 minutes, they still haven't emerged…"
    show drop:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou ner
    "Shou shifts from foot to foot."
    voice "audio/voice/E4/Shou/d2/69 Copy.ogg"
    ss "Do you think they really saw me there and now they've gone ahead without us?"
    
    menu:
        "I wouldn't blame them.":
            pf "We kind of deserve it if they did."
            show shou thi
            "Shou has the decency to look sheepish."
            voice "audio/voice/E4/Shou/d2/70 Copy.ogg"
            ss "I didn't realise girls talked about such… private things."
            pf "Neither did I."
        
        "They can't go without us.":
            pf "They can't go without us. You have the tickets."
            show shou thi
            voice "audio/voice/E4/Shou/d2/71 Copy.ogg"
            ss "Yeah, but those were to get into the hot springs. Dinner is separate."
            pf "Oh… then yeah, I suppose theoretically it's possible. But I bet they're just taking forever to get ready because they're women."
        
        "Who cares?":
            "I shrug."
            pf "Dinner is held in one room. We'll see them there regardless."
            show shou thi
            voice "audio/voice/E4/Shou/d2/72 Copy.ogg"
            ss "True, but you don't think they'd just leave us hanging here, right?"
            pf "I don't know."
            
    show shou wor
    voice "audio/voice/E4/Shou/d2/73 Copy.ogg"
    ss "What if this is all part of their plan for revenge? Leave us here waiting while they're all eating delicious food and laughing at us…"
    show shou ner
    voice "audio/voice/E4/Shou/d2/74 Copy.ogg"
    ss "Or maybe they've retired to one of their hotel rooms… dressed in their pj's… continuing their conversation…"
    pf "I'm just going to stop you right there."
    show shou neu
    voice "audio/voice/E4/Shou/d2/75 Copy.ogg"
    ss "But I was just getting to the good part."
    pf "That's a pretty lame revenge as far as revenges go, though."
    voice "audio/voice/E4/Shou/d2/76 Copy.ogg"
    ss "I suppose that's true."
    hide shou with dissolve
    stop music fadeout 7
    "We wait a while longer before the girls finally appear. Kaori glowers at us as she marches over. Valerie and Yuuna both look grave, and even Mayu looks stern."
    show shou wor at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    "Shou leans over to me."
    voice "audio/voice/E4/Shou/d2/77 Copy.ogg"
    ss "Oh god, they know. Should we just tell them?"
    show shou neu
    pf "Keep cool!"
    show yuuna dis at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie ann at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori dis at r1 behind shou with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    "The girls finally pause in front of us."
    pf "Um, are you okay?"
    show kaori ann
    "Kaori glares at the two of us and crosses her arms."
    voice "audio/voice/E4/Kaori/D2/Kaori_29_d1.ogg"
    ki "Of course not! We are surrounded by perverts!"
    show shou ner
    "Shou's eyes widen in panic and even I'm beginning to feel anxious. I was just teasing him before, but maybe they really {i}did{/i} see us!"
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    $ E4D2S3_Innocent = 0
    
    menu:
        "Try to play it off.":
            $ E4D2S3_Innocent = 1
            pf "Oh really? Did something happen?"
            show yuuna ann
            voice "audio/voice/E4/Yuuna/E4/D2/15.ogg"
            ym "We were being spied on while we were relaxing in the hot springs!"
            show shou cur
            voice "audio/voice/E4/Shou/d2/78 Copy.ogg"
            ss "That's terrible! Who would do such a thing?!"
            "Shou's voice is slightly higher pitched than normal. I glance at him and try to motion for him to calm down. He'll blow our cover otherwise!"
            show shou neu
            show vein:
                xoffset 925
                yoffset 110
                xzoom .5
                yzoom .5
            voice "audio/voice/E4/Kaori/D2/Kaori_30_d1.ogg"
            ki "I don't know, but I intend to find out!"
            show kaori thi
            "Kaori scans the lobby. Looking for perverts, I assume."
            show shou smi
            "Shou relaxes."
            voice "audio/voice/E4/Shou/d2/79 Copy.ogg"
            ss "Maybe you should just let it go."
            show kaori ang
            show shou neu
            voice "audio/voice/MISSING/BATCH5/k_redo_15.ogg"
            ki "What?!"
            show kaori ann
            show yuuna ang
            voice "audio/voice/E4/Yuuna/E4/D2/17.ogg"
            ym "How can you suggest that?"
            show yuuna ann
            show valerie ang
            show shou ner
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L27.ogg"
            vb "And let them get away with a free show?"
            show valerie ann
            show mayu ang
            voice "audio/voice/E4/Mayu/D2/Mayu D2-14.ogg"
            ma "That's not right!"
            show mayu ann
            show shou wor
            "Shou and I instinctively take a step back from their indignation."
            pf "Did you see who was watching you?"
            show kaori dis
            voice "audio/voice/E4/Kaori/D2/Kaori_31_d1.ogg"
            ki "No--"
            show shou ske
            voice "audio/voice/E4/Shou/d2/80 Copy.ogg"
            ss "Then how are you going to find them?"
            "The girls fall silent."
            show kaori ann
            
            voice "audio/voice/E4/Kaori/D2/Kaori_32_d1.ogg"
            ki "We'll just know!"
            "I raise an eyebrow and cross my arms."
            pf "Are you sure you were even being watched?"
            show shou cur
            "Shou catches my eye as if to say: {i}good one, broseph!{/i}"
            show kaori ang
            voice "audio/voice/E4/Kaori/D2/Kaori_33_d1.ogg"
            ki "Yes!"
            show shou neu
            show kaori ann
            pf "How can you be sure if you didn't see anyone?"
            show kaori thi
            "Kaori falters and looks at the rest of the girls for back-up."
            show yuuna dis
            voice "audio/voice/E4/Yuuna/E4/D2/18.ogg"
            ym "There was a pebble that rolled into the water from an outcrop of rocks. It's the perfect place for someone to hide and peep."
            show shou ske
            voice "audio/voice/E4/Shou/d2/81 Copy.ogg"
            ss "Or maybe it was an animal."
            show yuuna ske
            voice "audio/voice/E4/Yuuna/E4/D2/19.ogg"
            ym "An animal?"
            show shou neu
            stop music fadeout 3
            voice "audio/voice/E4/Shou/d2/82 Copy.ogg"
            ss "Yeah, the springs are outside. It's kind of hard to stop all the wildlife from running about."
            show yuuna thi
            voice "audio/voice/E4/Yuuna/E4/D2/20.ogg"
            ym "I suppose it's possible..."
            show dots:
                xoffset 30
                yoffset 100
                xzoom .5
                yzoom .5
            "She looks uncertainly at Kaori."
            show yuuna neu
            show valerie ske
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L28.ogg"
            vb "Or it could have been a person. Those rocks were a little too conveniently placed to have just been a careless animal."
            show mayu neu
            "Mayu nods."
            voice "audio/voice/E4/Mayu/D2/Mayu D2-15.ogg"
            ma "We told the hotel manager about it too so now they're aware and also on the lookout."
            show shou wor
            #stop music fadeout 3
            "Shou seems worried again, but after listening to this conversation I'm convinced they have no way of finding out it was us."
            play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
            pf "Okay, well since you've already alerted the hotel, maybe we should let them investigate and find the peeper and we can just enjoy our dinner."
            show shou ner
            show yuuna smi
            "Yuuna nods."
            voice "audio/voice/E4/Yuuna/E4/D2/21.ogg"
            ym "That's probably the best course of action."
            show shou smi
            voice "audio/voice/E4/Shou/d2/83 Copy.ogg"
            ss "Thank god, I'm starving!"
            show kaori ske
            voice "audio/voice/MISSING/BATCH5/k_redo_16.ogg"    
            ki "Do you ever not think about food?"
            show shou hap
          
            voice "audio/voice/MISSING/BATCH2/16.ogg"
            ss "I haven't eaten since lunch! I think I'm allowed to be hungry."
            show mayu smi
            "Mayu giggles."
            voice "audio/voice/E4/Mayu/D2/Mayu D2-16.ogg"
            ma "Let's go before you faint from hunger."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L29.ogg"
            vb "I hope the food is good."
            pf "Me too."
            #black screen
            scene black with fade
            "The tension lifts as we walk towards the dining room. {w}That was too close for comfort!"
    
        "It was all Shou's fault!":
            pf "It was Shou's idea!"
            show kaori cur
            show shou sur b1
            "Shou looks like a deer in headlights and the girls all wear matching expressions of shock."
            
            show confused:
                xoffset 1500
                yoffset 50
                xzoom .5
                yzoom .5
                
            if E4D2S2_Minds == 1:
                voice "audio/voice/E4/Shou/d2/84 Copy.ogg"
                ss "What happened to you wished that it was your idea?"
            else:
                voice "audio/voice/E4/Shou/d2/85 Copy.ogg"
                ss "Broseph! I thought we were a team!"
                
            show yuuna ske
            voice "audio/voice/E4/Yuuna/E4/D2/22.ogg"
            ym "It was you?"
            show kaori mis
            "Kaori looks strangely triumphant."
            show vein:
                xoffset 925
                yoffset 110
                xzoom .5
                yzoom .5
            voice "audio/voice/E4/Kaori/D2/Kaori_34_d1.ogg"
            ki "I knew it!"
            show shou wor
            voice "audio/voice/E4/Shou/d2/86 Copy.ogg"
            ss "Broseph was there too!"
            pf "Don't try to pin this on me. It was all you."
            show kaori ann
            show valerie dis
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L30.ogg"
            vb "Not so fast, mister. I'm not convinced you're totally innocent. You seemed way too quick to point the finger at Shou."
            pf "Uh…"
            show valerie ann
            show yuuna dis
            "Yuuna sighs."
            voice "audio/voice/E4/Yuuna/E4/D2/23.ogg"
            ym "So you were there too."
            "Busted."
            pf "I'm sorry."
            show kaori dis
            voice "audio/voice/E4/Kaori/D2/Kaori_35_d1.ogg"
            ki "I would have expected this from Shou, but I thought there was still hope for you."
            show question:
                xoffset 1500
                yoffset 50
                xzoom .5
                yzoom .5
            voice "audio/voice/E4/Shou/d2/87 Copy.ogg"
            ss "Hey! What does that mean?"
            show yuuna neu
            show kaori neu
            show valerie neu
            "The girls stare blankly at Shou."
            show shou ner
            "He sighs."
            voice "audio/voice/E4/Shou/d2/88 Copy.ogg"
            ss "I'm sorry."
            show mayu win
            voice "audio/voice/E4/Mayu/D2/Mayu D2-17.ogg"
            ma "Shou… but why?"
            show shou thi
            voice "audio/voice/E4/Shou/d2/89 Copy.ogg"
            ss "We were just curious."
            show mayu sur
            show kaori ann
            show yuuna dis
            show valerie ann
            "Her eyes widen and she covers her chest."
            show mayu ang
            voice "audio/voice/E4/Mayu/D2/Mayu D2-18.ogg"
            ma "W-What? How can you say that so freely?"
            show mayu ann
            show panic:
                xoffset 1500
                yoffset 50
                xzoom .5
                yzoom .5
            show shou wor
            voice "audio/voice/E4/Shou/d2/90 Copy.ogg"
            ss "N-No! That's not what I mean! I just meant we wanted to know what you girls were doing."
            show valerie ske
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L31.ogg"
            vb "That doesn't make it sound much better."
            play sound [ "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg" ]
            # shake shou sprite?
            show shou win
            # shake screen?
            "Kaori hits Shou on the arm and then hits me."
            voice "audio/voice/E4/Shou/d2/91 Copy.ogg"
            ss "Ow!"
            show shou sad
            pf "Ow!"
            show kaori ang
            voice "audio/voice/E4/Kaori/D2/Kaori_36_d1.ogg"
            ki "Stop being a pervert!"
            show kaori ann
            
            menu:
                "We're sorry!":
                    pf "Uh, did I mention we're sorry?"
                    "The girls glance at each other, then Yuuna sighs."
                    show yuuna thi
                    voice "audio/voice/E4/Yuuna/E4/D2/24.ogg"
                    ym "I guess there's no point in staying angry since we can't change the past."
                    show kaori dis
                    "Kaori glares at us."
                    stop music fadeout 3
                    voice "audio/voice/E4/Kaori/D2/Kaori_37_d1.ogg"
                    ki "Don't even think about doing it again!"
                    pf "We won't!"
                    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
                    show shou wor
                    "Shou nods vigorously."
                
                "It's not like we could see anything.":
                    pf "What are you getting so worked up about? If anything, Shou and I should be the ones who are angry."
                    show kaori ske
                    voice "audio/voice/E4/Kaori/D2/Kaori_38_d1.ogg"
                    ki "What?!"
                    show shou ske
                    "Even Shou gives me a confused look."
                    voice "audio/voice/E4/Shou/d2/92 Copy.ogg"
                    ss "What?"
                    pf "You guys were submerged up to like your necks. We couldn't even see a thing!"
                    show kaori cur b2
                    with dissolve
                    show mayu sur b1
                    show yuuna sur b1
                    show valerie hap
                    with dissolve
                    "Kaori's face is bright red. Yuuna and Mayu instinctively cover their chests, clearly mortified. To everyone's surprise, Valerie laughs."
                    show note:
                        xoffset 590
                        yoffset 125
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L32.ogg"
                    vb "That's karma for you. Serves you right!"
                    show shou wor
                    voice "audio/voice/E4/Shou/d2/93 Copy.ogg"
                    ss "Don't listen to him! We weren't trying to look!"
                    show kaori ann b1
                    show mayu ann b1
                    show yuuna ann b1
                    voice "audio/voice/E4/Kaori/D2/Kaori_39_d1.ogg"
                    ki "Then why were you even spying?"
                    stop music fadeout 3
                    show valerie ske
                    "Yuuna speaks up."
                    
                    voice "audio/voice/E4/Yuuna/E4/D2/25.ogg"
                    ym "There's no point in arguing. It already happened and we'll be here all night if we keep going. Just don't do it again."
                    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
                    voice "audio/voice/E4/Shou/d2/94 Copy.ogg"
                    ss "We won't! We promise!"
                    pf "Yeah, sorry."
                    show yuuna neu
                    show mayu dis
                    show kaori dis
                    "Yuuna nods."
                
                "What more do you want from us?":
                    pf "Look, we already apologised. What more can we do?"
                    show kaori ang
                    "Kaori is about to reply, when Yuuna interrupts her."
                    stop music fadeout 3
                    show yuuna neu
                    voice "audio/voice/E4/Yuuna/E4/D2/26.ogg"
                    ym "We accept your apology."
                    show question:
                        xoffset 925
                        yoffset 110
                        xzoom .5
                        yzoom .5
                    show kaori ske
                    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
                    voice "audio/voice/E4/Kaori/D2/Kaori_40_d1.ogg"
                    ki "What?!"
                    show yuuna dis
                    voice "audio/voice/E4/Yuuna/E4/D2/27.ogg"
                    ym "Let it go, Kaori. Arguing is going to get us nowhere and it's not like we can change what they've already done."
                    show kaori dis
                    "Kaori scowls but doesn't push it."
    
            show valerie neu
            show mayu neu
            show yuuna neu
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L33.ogg"
            vb "Well, this has been an exciting day."
            voice "audio/voice/E4/Mayu/D2/Mayu D2-19.ogg"
            ma "Maybe a little too exciting…"
            show shou smi
            voice "audio/voice/E4/Shou/d2/95 Copy.ogg"
            ss "...Does that mean we can eat now?"
            show kaori thi
            voice "audio/voice/E4/Kaori/D2/Kaori_41_d1.ogg"
            ki "Of course Shou is thinking about food."
            play sound "audio/sfx/Human/Stomach Grumble.ogg"
            "As if on cue, my stomach growls."
            pf "Shou's not the only one…"
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L34.ogg"
            vb "I'm ready to eat too. Let's go get some food."
            #black screen
            scene black with fade
            "Valerie leads the way. The team continues to tease Shou and the tension from before melts away with their laughter. {w}That could have gone a lot worse. I'm just glad that's over with."
    
        "Come clean.":
            pf "We're really sorry."
            show shocked:
                xoffset 1475
                yoffset 20
                xzoom .5
                yzoom .5
            show shou sur
            voice "audio/voice/E4/Shou/d2/96 Copy.ogg"
            ss "Broseph!"
            show mayu sur
            show yuuna sur
            show valerie sur
            show kaori dis
            "The girls look at each other in surprise, but Kaori narrows her eyes."
            show vein:
                xoffset 925
                yoffset 110
                xzoom .5
                yzoom .5
            show kaori ann
            voice "audio/voice/E4/Kaori/D2/Kaori_42_d1.ogg"
            ki "I had a feeling it was you two!"
            show shou wor
            show mayu ann
            show valerie ann
            show yuuna ann
            voice "audio/voice/E4/Shou/d2/97 Copy.ogg"
            ss "Hey, don't drag me into this. This was all Broseph's idea!"
            pf "Don't listen to him! Of course it was his idea!"
            show kaori dis
            voice "audio/voice/E4/Kaori/D2/Kaori_43_d1.ogg"
            ki "Please, this type of thing just screams \"Shou\"."
            pf "So you believe me?"
            voice "audio/voice/E4/Kaori/D2/Kaori_44_d1.ogg"
            ki "I believe that Shou was involved."
            show shou ske
            voice "audio/voice/E4/Shou/d2/98 Copy.ogg"
            ss "Hey! Broseph could have acted alone."
            show kaori ann
            voice "audio/voice/E4/Kaori/D2/Kaori_45_d1.ogg"
            ki "Nope."
            show valerie ske
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L35.ogg"
            vb "Not likely."
            show yuuna dis
            voice "audio/voice/E4/Yuuna/E4/D2/28.ogg"
            ym "I don't think so."
            show mayu dis
            voice "audio/voice/E4/Mayu/D2/Mayu D2-20.ogg"
            ma "Nu uh."
            "Mayu shakes her head."
            "None of the girls even hesitated before answering."
            show shou ner
            voice "audio/voice/E4/Shou/d2/99 Copy.ogg"
            ss "Wow… even you, Mayu?"
            show mayu ner
            "She looks away."
            show drop:
                xoffset 315
                yoffset 135
                xzoom .5
                yzoom .5
            voice "audio/voice/E4/Mayu/D2/Mayu D2-21.ogg"
            ma "Sorry…"
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L36.ogg"
            vb "I can't believe you pervs were spying on us. What were you hoping to see?"
            show shou wor
            voice "audio/voice/E4/Shou/d2/100 Copy.ogg"
            ss "Nothing!"
            show valerie neu
            "Valerie gives him a blank look."
            show shou thi
            voice "audio/voice/E4/Shou/d2/101 Copy.ogg"
            ss "I mean, we weren't spying. We were eavesdropping!"
            pf "...I wouldn't say that so proudly."
            show kaori ang
            voice "audio/voice/E4/Kaori/D2/Kaori_46_d1.ogg"
            ki "How is that better?!"
            show kaori ann
            show drop:
                xoffset 30
                yoffset 100
                xzoom .5
                yzoom .5
            show yuuna thi
            voice "audio/voice/E4/Yuuna/E4/D2/29.ogg"
            ym "Dare I ask why?"
            pf "We heard someone shriek and wanted to make sure nobody was hurt."
            show kaori mis
            show mayu sur b2
            show valerie hap
            show yuuna mis
            show shou ske
            "Mayu looks alarmed and then she blushes deeply. Valerie bursts out laughing. Yuuna hides a smile, and even Kaori looks amused."
            show dots:
                xoffset 1475
                yoffset 20
                xzoom .5
                yzoom .5
            "That's a weird reaction…"
            pf "What happened exactly?"
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L37.ogg"
            vb "A spider crawled on Mayu--"
            show mayu wor b2
            voice "audio/voice/E4/Mayu/D2/Mayu D2-22.ogg"
            ma "Nothing!"
            show panic:
                xoffset 315
                yoffset 135
                xzoom .5
                yzoom .5
            "Mayu freezes after her outburst. Shou and I exchange a look."
            show mayu ner b2
            voice "audio/voice/E4/Mayu/D2/Mayu D2-23.ogg"
            ma "S-Sorry to have troubled you…"
            show shou smi
            voice "audio/voice/E4/Shou/d2/102 Copy.ogg"
            ss "We're just glad that you're okay."
            show mayu smi b1
            "Mayu smiles weakly."
            voice "audio/voice/E4/Mayu/D2/Mayu D2-24.ogg"
            ma "Thanks for your concern."
            pf "No problem."
            show kaori ann
            "Kaori crosses her arms."
            voice "audio/voice/E4/Kaori/D2/Kaori_47_d1.ogg"
            ki "You're not going to get off the hook that easily!"
            pf "We're sorry, but we were genuinely concerned!"
            show shou ner
            voice "audio/voice/E4/Shou/d2/103 Copy.ogg"
            ss "Yeah! If you didn't want us over there, you shouldn't have screamed!"
            pf "Shou, please."
            show shou wor
            voice "audio/voice/E4/Shou/d2/104 Copy.ogg"
            ss "What? It's true."
            stop music fadeout 3
            show yuuna neu
            voice "audio/voice/E4/Yuuna/E4/D2/30.ogg"
            ym "Let's just accept their apology and move forward."
            show kaori ske
            voice "audio/voice/E4/Kaori/D2/Kaori_48_d1.ogg"
            ki "What?"
            show yuuna thi
            play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
            "Yuuna sighs."
            voice "audio/voice/E4/Yuuna/E4/D2/31.ogg"
            ym "Clearly it was a misunderstanding and I'm sure the boys have learned their lesson… right?"
            show shou ner
            voice "audio/voice/E4/Shou/d2/105 Copy.ogg"
            ss "Right."
            pf "Yup."
            show yuuna neu
            voice "audio/voice/E4/Yuuna/E4/D2/32.ogg"
            ym "There's no point in going back and forth anymore, and there's nothing else to say about the matter."
            show storm:
                xoffset 925
                yoffset 110
                xzoom .5
                yzoom .5
            show kaori dis
            "Kaori scowls but reluctantly agrees."
            voice "audio/voice/E4/Kaori/D2/Kaori_49_d1.ogg"
            ki "Fine, but if I catch you guys doing something like that again I'm going to make you regret you were born!"
            show shou hap
            voice "audio/voice/E4/Shou/d2/106 Copy.ogg"
            ss "Yes, ma'am!"
            pf "We promise we won't do it again."
            show shou smi
            voice "audio/voice/E4/Shou/d2/107 Copy.ogg"
            ss "Since that's all settled, does that mean we can finally go eat?"
            show kaori thi
            "Kaori sighs."
            voice "audio/voice/E4/Kaori/D2/Kaori_50_d1.ogg"
            ki "Yes, we can go eat."
            show shou hap
            voice "audio/voice/E4/Shou/d2/108 Copy.ogg"
            ss "Finally! I thought my stomach was going to eat itself."
            show kaori ske
            voice "audio/voice/E4/Kaori/D2/Kaori_51_d1.ogg"
            ki "You're so dramatic!"
            show yuuna smi
            show valerie smi
            voice "audio/voice/E4/Yuuna/E4/D2/33.ogg"
            ym "I'm pretty hungry too actually."
            pf "So am I."
            voice "audio/voice/E4/Yuuna/E4/D2/34.ogg"
            ym "Let's go then."
            #blackscreen
            scene black with fade
            "Yuuna leads the way as the team continues to tease Shou. The tension from before dissipates as everyone speculates about tonight's meal. {w}This didn't go as badly as I thought it would. I'm just glad it's behind us now."
            
    show bg campus lounge night with fade
    "When we arrive at the dining hall, we settle down at our table. The hotel offers a prix fixe menu, so all we had to do was confirm our number of diners then the waitress put in the orders for our meals."
    show yuuna smi at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu smi at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie smi at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    show shou smi at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    pf "What ever happened to Mei?"
    voice "audio/voice/E4/Kaori/D2/Kaori_52_d1.ogg"
    ki "She didn't want to stay after the incident so she went to find her teammates."
    
    if E4D2S3_Innocent == 0:
        pf "Did she ever finish explaining--"
        show exclamation:
            xoffset 925
            yoffset 110
            xzoom .5
            yzoom .5
        show kaori ang b1
        show mayu neu b1
        show valerie ner b1
        show yuuna neu b1
        show shou cur b1
        voice "audio/voice/E4/Kaori/D2/Kaori_53_d1.ogg"
        ki "None of your business!"
        show kaori ann b1
        show mayu ner b2
        show valerie ner b2
        show yuuna thi b2
        "All of the girls' faces are bright red--even Valerie's! I wonder if that means she did finish…"
    else:
        "I wonder if she ever got a chance to finish her explanation…"
        
    hide kaori
    hide mayu
    hide valerie
    hide yuuna
    hide shou
    with dissolve
    "Soon, the food arrives. It's a simple tray of rice, fish, and pickled vegetables. We quiet down as we all dig in. I hadn't realised how hungry I was until now."
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    "I feel a buzz in my pocket. As I pull out my phone, I notice all of my teammates are checking their phones too."
    "It's a group email from Dasshu. They're reminding us about our coaching session that was scheduled for tomorrow. It seems they've received confirmation that Coach Ivan will be on campus to give us a few pointers before our match on Thursday."
    show yuuna smi at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    show shou neu at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    "Yuuna wears a broad grin."
    voice "audio/voice/E4/Yuuna/E4/D2/35.ogg"
    ym "Did you all get that email?"
    pf "Yeah."
    show note:
        xoffset 30
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna hap
    show mayu hap
    voice "audio/voice/E4/Yuuna/E4/D2/36.ogg"
    ym "I'm so glad Coach Ivan will be on campus!"
    voice "audio/voice/E4/Mayu/D2/Mayu D2-25.ogg"
    ma "Me too! He's one of my idols!"
    show yuuna smi
    pf "Really?"
    show mayu smi
    voice "audio/voice/E4/Mayu/D2/Mayu D2-26.ogg"
    ma "Of course. He's a war game legend."
    show shou smi
    show kaori smi
    "How come I've never heard of him before?"
    voice "audio/voice/E4/Shou/d2/109 Copy.ogg"
    ss "He's almost as famous as the Akemis."
    show dots:
        xoffset 1475
        yoffset 20
        xzoom .5
        yzoom .5
    show shou thi
    "Shou looks thoughtful."
    voice "audio/voice/E4/Shou/d2/110 Copy.ogg"
    ss "Actually, Mayu, doesn't your family know him?"
    show mayu neu
    show shou neu
    voice "audio/voice/E4/Mayu/D2/Mayu D2-27.ogg"
    ma "Yes, but not very well. They respect each other, of course, but aren't close friends. That's why I've never met him."
    voice "audio/voice/E4/Kaori/D2/Kaori_54_d1.ogg"
    ki "I'm looking forward to what he can teach this team. There's a reason why he's won three championships and received the MVP award twice."
    pf "Wow, this guy sounds impressive!"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L38.ogg"
    vb "I heard no matter where he goes he always wears his signature helmet."
    show mayu smi
    "Valerie's heard of him too?"
    show shou smi
    voice "audio/voice/E4/Shou/d2/111 Copy.ogg"
    ss "I've heard that too."
    pf "I wonder if he'll wear it tomorrow."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L39.ogg"
    vb "Probably!"
    scene black with fade
    "The team continues to talk excitedly about tomorrow's training session. I soak in each story or rumour the team shares about him, and the more I hear about him, the more enthusiastic I feel about meeting him."
    "After we finish up our meals, I want to take another dip into the hot spring. After all, my first session was kind of interrupted. Shou happily agrees but the girls firmly refuse. They say their goodnights and retire to their rooms."
    stop music fadeout 3
    "Shou and I relax in the hot water until we're both stifling yawns. Then we decide to return to our rooms as well. After all, we have an early morning train to catch."
    stop ambient fadeout 5
    "I'm exhausted and collapse onto my bed. As soon as my head hits the pillow, I fall asleep."
    
    jump E4D3S1
