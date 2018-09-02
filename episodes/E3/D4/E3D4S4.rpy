#
label E3D4S4:
    
    play ambient "audio/ambience/Parking Lot.ogg" fadein 3
    scene bg campus building dusk with fade
    show kaori dis at r1
    show mayu ner at l3:
        xoffset -100
    show shou dis at l1
    with dissolve
    "Mei is waiting for us outside, leaning against the door."
    show mei hap at r3 with dissolve:
        xoffset 100
        xzoom -1
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_20.ogg"
    ms "Hey, guys! Congratulations on the win!"
    show kaori ann
    "I glance at Mei, barely registering her presence. I'm too wrapped up with what happened in the pre-combat room. {w}Mei's smile falters when no one answers."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    show mei ske
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_21.ogg"
    ms "Wow... with gloomy faces like that I'd think you were the ones who lost!"
    show exclamation:
        xoffset 890
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ang
    show shou sur
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_53.ogg"
    ki "Shut up, Mei!"
    show kaori ann
    show panic:
        xoffset 1300
        yoffset 100
        xzoom .75
        yzoom .75
    show mei ner
    show shou dis
    "Mei flinches from the ferocity of Kaori's voice."
    show mayu dis
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_22.ogg"
    ms "I was just kidding, Kaori..."
    show kaori ang
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_54.ogg"
    ki "This is all your fault!"
    show kaori ann
    show mei wor
    show shou ann
    "Mei is stunned into silence."
    voice "audio/voice/E3/D4/S4/shou/61.ogg"
    ss "You seriously need to calm down. Mei didn't do anything."
    voice "audio/voice/E3/D4/S4/mayu/Mayu-27.ogg"
    ma "You're being too harsh, Kaori."
    show vein:
        xoffset 890
        yoffset 110
        xzoom .75
        yzoom .75
    "Kaori's eyes flash."
    show kaori ang
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_55.ogg"
    ki "You guys are taking her side? I thought you were {i}my{/i} teammates."
    show kaori ann
    show shou ang
    voice "audio/voice/E3/D4/S4/shou/62.ogg"
    ss "We aren't taking anyone's side. But since the match, you've been acting like a complete--"
    show exclamation:
        xoffset 170
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu sur
    show kaori cur
    stop music fadeout 1
    voice "audio/voice/E3/D4/S4/mayu/Mayu-28.ogg"
    ma "Shou!"
    show mayu ann
    show shou ann
    "Shou catches himself and falls silent. Kaori looks at him."
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_56.ogg"
    ki "A complete what?"
    show shou dis
    voice "audio/voice/E3/D4/S4/shou/63.ogg"
    ss "Nothing."
    show dots:
        xoffset 890
        yoffset 110
        xzoom .75
        yzoom .75
    "She pauses. When she finally speaks her voice cracks."
    show kaori neu
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_57.ogg"
    ki "I see. That's how you really feel..."
    show mayu dis
    show shou ner
    "Shou's look softens."
    voice "audio/voice/E3/D4/S4/shou/64.ogg"
    ss "No, I didn't mean that."
    show kaori neu
    "Kaori turns to face Mei."
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_58.ogg"
    ki "You..."
    "She lowers her head."
    show kaori win
    show mayu wor
    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_59.ogg"
    ki "You always turn my friends against me."
    hide kaori with dissolve
    "She spins on her heel and walks away. When she thinks she's out of eyesight, she starts running."
    show mei sur
    show shou sur
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_23.ogg"
    ms "Kaori!"
    "Kaori disappears. Shou is about to rush after her when Mei blocks his path."
    play music "audio/music/Kaori Itami (GAME VERSION).ogg" fadein 5
    show mei wor
    ### VOICE - missing line?
    #ms "Wait."
    show shou wor
    voice "audio/voice/E3/D4/S4/shou/65.ogg"
    ss "I have to go apologize. I didn't mean what I said."
    show mei sad
    "Mei sighs."
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_24.ogg"
    ms "You need to give her space right now or you'll just make it worse."
    show dots:
        xoffset 515
        yoffset 20
        xzoom .75
        yzoom .75
    show shou ner
    voice "audio/voice/E3/D4/S4/shou/66.ogg"
    ss "..."
    "Shou looks torn, but doesn't try to follow Kaori."
    voice "audio/voice/E3/D4/S4/shou/67.ogg"
    ss "I don't think I've ever seen her too upset to yell."
    show dots:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner
    "Mayu looks down worriedly at her feet."
    voice "audio/voice/E3/D4/S4/mayu/Mayu-29.ogg"
    ma "I was too mean to her earlier. I'm sorry."
    show mei neu
    show shou sad
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_25.ogg"
    ms "You guys shouldn't blame yourself. Kaori just needs time to cool off."
    pf "You sound like you speak from experience."
    show mei wor
    "Mei sighs and nods."
    pf "What's up with her saying \"you always turn my friends against me\"?"
    show mei neu
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_26.ogg"
    ms "It's a long story. Something that happened back in middle school."
    "Something to do with Ryouta?"
    pf "You two go way back."
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_27.ogg"
    ms "Yes, we do."
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    show mei cur
    show exclamation:
        xoffset 1300
        yoffset 100
        xzoom .75
        yzoom .75
    "Mei's pocket vibrates. She pulls out her phone and reviews the message."
    show mei neu
    voice "audio/voice/E3/D4/S4/mei/MeiEp3_Line_28.ogg"
    ms "My team is wondering where I am. Don't worry too much about Kaori. She'll be okay. I'll talk to her when she's calmed down."
    hide mei with dissolve
    "We nod and watch Mei head out."
    show mayu wor at l2:
        xoffset 0
    show shou sad at r2:
        xzoom -1
    with dissolve
    "I don't feel any less guilty."
    voice "audio/voice/E3/D4/S4/mayu/Mayu-30.ogg"
    ma "I shouldn't have acted like that earlier."
    voice "audio/voice/E3/D4/S4/shou/68.ogg"
    ss "No, it was my stupid comment. I never should have said something like that."
    "I guess they still feel guilty too."
    
    menu:
        "Let's give Kaori her space like Mei suggested.":
            pf "We should listen to Mei. She's known Kaori the longest and it sounds like she's had to deal with this situation before... We should give Kaori some time."
            show mayu neu
            show shou neu
            "Shou and Mayu glance at each other, then nod."
            voice "audio/voice/E3/D4/S4/shou/69.ogg"
            ss "I'm still going to apologize."
            voice "audio/voice/E3/D4/S4/mayu/Mayu-31.ogg"
            ma "Me too."
            pf "We can do that tomorrow as a team."
            show shou thi
            voice "audio/voice/E3/D4/S4/shou/70.ogg"
            ss "'Kay."
            show dots:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            show dots2:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            "An uncomfortable silences settles in. Although we haven't lost a match yet, I doubt it would make us feel worse than we do right now."
            pf "There's no point in hanging around here feeling guilty. I'll see you guys tomorrow."
            show shou neu
            voice "audio/voice/E3/D4/S4/mayu/Mayu-32.ogg"
            ma "Okay, good night."
            voice "audio/voice/MISSING/BATCH2/3.ogg"
            ss "Bye."
            hide mayu
            hide shou
            with dissolve
            "I wave and head to my bike."
            #Black screen
            scene black with fade
            "The entire ride home, I run through the events leading up to Kaori's departure and come up with multiples ways we could have handled the situation."
            "Hindsight is always 20/20."
            "The house is quiet when I arrive home. I'm a little relieved as I'm exhausted, so I head straight to bed and fall fast asleep."
            jump E3D5S1
    
    
        "I'll go check up on her.":
            $ E3D4S4_ChaseKaori = 1
            pf "I'll go see if she's okay."
            show shou ner
            voice "audio/voice/E3/D4/S4/shou/71.ogg"
            ss "No, let me do it."
            pf "I don't think she'll be too happy to see you right now, Shou."
            show mayu ner
            voice "audio/voice/E3/D4/S4/mayu/Mayu-33.ogg"
            ma "He's right..."
            show dots:
                xoffset 1050
                yoffset 20
                xzoom .75
                yzoom .75
            show shou sad
            "Shou frowns, but doesn't protest."
            pf "You guys can head out. I'll text you once everything is okay."
            show mayu wor
            voice "audio/voice/E3/D4/S4/mayu/Mayu-34.ogg"
            ma "Are you sure?"
            pf "Yeah, there's no point in you guys just standing around here."
            show shou neu
            voice "audio/voice/E3/D4/S4/shou/72.ogg"
            ss "Let us know if we can help."
            show mayu neu
            pf "Will do."
            stop music fadeout 5
            hide mayu
            hide shou
            with dissolve
            "I wave at the pair and jog in the direction Kaori went."
            
            stop ambient fadeout 3
            #black screen
            scene black with fade
            
            play ambient "audio/ambience/Parking Lot.ogg"
            scene bg campus main dusk with fade
            "The sun dips low in the sky as the evening rolls in. I search several locations for Kaori until I arrive at one of the more secluded campus quads. There's only one student sitting on the bench with a bag at her feet."
            show kaori win b1 at cc with dissolve
            "Kaori's face is bent over her chest, and I can hear faint sniffles."
            
            label E3D4S4_Console:
                menu:
                    "She probably wants to be alone right now...":
                        "I doubt she wants to talk to anyone right now, and I bet she'd be mortified if she knew anyone saw her crying. It's best just to give her some space and see how she's doing tomorrow."
                        hide kaori with dissolve
                        "I head back to my bike."
                        stop ambient fadeout 3
                        #Black screen
                        scene black with fade
                        "The entire ride home, I run through the events leading up to Kaori's departure and come up with multiples ways we could have handled the situation."
                        "Hindsight is always 20/20."
                        play ambient "audio/ambience/Night Crickets.ogg" fadein 3
                        scene bg homekaito main night with fade
                        "The house is quiet when I arrive home. I'm a little relieved as I'm exhausted, so I head straight to bed and fall fast asleep."
                        scene black with fade
                        stop ambient fadeout 3
                        jump E3D5S1
        
                    "Embrace Kaori." if (E2KIS4_Completed == 1) and (E3D4S4_Loopback == 0):
                        $ E3D4S4_Loopback = 1
                        "She shouldn't be alone right now. Not when she's hurting like this. I want to wrap my arms around her and let her know that I'm here for her…"
                        "There's no turning back once I do this. Should I go through with it?"
                        menu:
                            "Yes.":
                                jump E3D4KI
                            "No.":
                                jump E3D4S4_Console
        
        
                    "Console her.":
                        play music "audio/music/Slow Day (GAME VERSION).ogg" fadein 5
                        #label E3D4S4_Console:
                        $ E3D4S4_Consoled = 1
                        "I place an arm on her shoulder."
                        pf "Hey, are you okay?"
                        show kaori cur b1
                        "Kaori glances up at me for a second, but it was long enough for me to see how her eyes glittered. She rubs her eyes."
                        show kaori sad b1
        
                        menu:
                            "Shou feels bad.":
                                pf "Shou is sorry about what he was about say. He didn't mean it."
                                voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_60.ogg"
                                ki "I know. It's not his fault. I was being unreasonable."
                                "I blink. That was an unexpected response."
                                show kaori wor b1
                                jump E3D4S4_Sorry
                            
                            "We're all sorry.":
                                pf "We're sorry Kaori."
                                "Kaori shakes her head."
                                voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_61.ogg"
                                ki "You guys don't have anything to be sorry for. It was my fault."
                                pf "Still, we're your teammates. We should be helping each other, not fighting."
                                show kaori wor b1
                                voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_62.ogg"
                                ki "You guys were right. This was personal."
                                pf "What?"
        
                                label E3D4S4_Sorry:
                                    voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_63.ogg"
                                    ki "I've been… busy with other stuff. I guess the stress got to me."
                                    pf "Other stuff?"
                                    
                                    if E2KIS4_Completed == 1:
                                        pf "You mean the daycare?"
                                        show kaori sad b1
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_64.ogg"
                                        ki "Yeah. I've been putting in a lot of hours there, plus mid terms are coming up, and then the unexpected battle with Mei."
                                        
                                    else:
                                        show kaori sad b1
                                        "Kaori shakes her head."
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_65.ogg"
                                        ki "Don't worry about it. It's nothing major. I just have to handle myself better."
            
                                    "I sit down beside her and enjoy the silence. The only sounds are of the soft whistles of the breeze and the chirp of wildlife."
                                    show kaori neu b1
                                    "I let the tranquility wash over me. Even Kaori seems to be calmer. She looks up at the evening sky."
                                    
                                    #QTE
                                    $ qtebase = 3
                                    $ qtetotal = qteath + qtebase
                                    $ t_var = qtetotal
                                    show screen timer_scr(place="E3D4S4_End")
                                    
                                    menu:
                                        "Ask about Mei.":
                                            $ renpy.hide_screen ("timer_scr")
                                            pf "I've been wondering, what's your history with Mei?"
                                            "Kaori looks at me."
                                            voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_66.ogg"
                                            ki "What do you mean?"
                                            pf "She acts like your best friend, but you... not so much."
                                            show dots:
                                                xoffset 720
                                                yoffset 110
                                                xzoom .75
                                                yzoom .75
                                            "Kaori sighs."
                                            show kaori ner b1
                                            voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_67.ogg"
                                            ki "We {i}were{/i} best friends, but that was before she broke my trust."
                                            show kaori wor b1
                                            voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_68.ogg"
                                            ki "Our friendship can't go back to what it used to be, no matter how badly she wants it to."
                                            pf "What did she do that was so unforgivable?"
                                            show kaori sad b1
                                            "Kaori looks away."
                                            pf "If you're ashamed or embarrassed to tell me, could it really have been that bad?"
                                            voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_69.ogg"
                                            ki "Yes."
                                            "Although she answers quickly, she seems a little less certain than before."
                                            pf "Well, alright. That's your call, but it's obvious that Mei still cares a lot about you."
                                            show kaori ner b1
                                            "Kaori doesn't answer."
                                            
                                    label E3D4S4_End:
                                        $ renpy.hide_screen ("timer_scr")
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_70.ogg"
                                        ki "It's getting pretty late."
                                        pf "You're going to head out?"
                                        show kaori neu b1
                                        "She stands up and picks up her bag."
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_71.ogg"
                                        ki "Yeah."
                                        show kaori smi b1
                                        "Unexpectedly, she smiles."
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_72.ogg"
                                        ki "Thanks."
                                        "I smile back."
                                        pf "No problem. {w}Want me to walk you back to your dorm?"
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_73.ogg"
                                        ki "I'm okay."
                                        pf "Alright. Have a good evening."
                                        voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_74.ogg"
                                        ki "You too."
                                        hide kaori with dissolve
                                        "After she disappears around the corner, I head back to my bike."
                                        stop music fadeout 5
                                        stop ambient fadeout 5
                                        scene black with fade
                                        "The entire ride home, I run through the events leading up to Kaori's departure and our conversation afterwards. I'm just glad everything worked out okay."
                                        "The house is quiet when I arrive home. I'm a little relieved as I'm exhausted, so I head straight to bed and fall fast asleep."
                                        $renpy.pause(2.0)
                                        jump E3D5S1
        
                            "Were you crying? LOL.":
                                pf "Were you crying...?"
                                show kaori cur b1
                                "Kaori looks at me."
                                voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_75.ogg"
                                ki "Of course not!"
                                show kaori sur b1
                                pf "Ohoho, I just caught Kaori crying!"
                                "She slugs me on the shoulder."
                                show kaori wor b1
                                voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_76.ogg"
                                ki "Shut up!"
                                "I rub my fresh bruise."
                                pf "And there's the Kaori I know."
                                show storm:
                                    xoffset 720
                                    yoffset 110
                                    xzoom .75
                                    yzoom .75
                                show kaori thi b1
                                "She tries to look irritated, but a smile escapes."
                                show kaori smi b1
                                voice "audio/voice/MISSING/BATCH5/k_redo_01.ogg"
                                ki "You're an idiot."
                                pf "No arguments there."
                                pf "But seriously, are you okay?"
                                show kaori ner b1
                                ### VOICE - line is still all takes
                                #voice "audio/voice/E3/D4/S4/kaori/e3d4_Kao_78.ogg"
                                ki "Yeah..."
                                jump E3D4S4_Sorry

