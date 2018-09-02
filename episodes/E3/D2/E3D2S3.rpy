#
label E3D2S3:
    
    stop music fadeout 5
    
    scene bg vacation beach day with dissolve:
        xzoom 1
        yzoom 1
        xalign 0.5
        yalign 0.8
    
    "Meanwhile, my friends have been eerily silent… {w}Hesitantly, I glance over to a circle of frowns."
    
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 10
    
    show kaori neu at r2:
        xoffset 50
        xzoom -0.75
        yzoom 0.75
    show mayu neu at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show valerie neu at l1:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show yuuna neu at r1:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    with dissolve
    
    show shou neu at l2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    $renpy.pause(.75)
    pf "What?"
    show yuuna dis
    voice "audio/voice/E3/D2/S3/yuuna/10.ogg"
    ym "I had no idea you were so {i}popular{/i}."
    "Yuuna's bright eyes are dulled with disapproval."
    pf "I don't know why they like me so much."
    show kaori ann
    ### VOICE - line missing?
    voice "audio/voice/MISSING/BATCH5/k_redo_22.ogg"
    ki "Do you know how old those girls are? Creep!"
    pf "They came onto me!"
    "I look around for a friendly face, and my gaze lands on Shou."
    pf "C'mon, Shou, buddy, you're with me, right?"
    voice "audio/voice/E3/D2/S3/shou/30.ogg"
    ss "I misjudged you."
    "I can't tell if he means that in a good or bad way."
    show dots:
        xoffset 30
        yoffset 135
        xzoom .5
        yzoom .5
    stop music fadeout 5
    "Mayu watches me silently."
    
    if MCStory == 3:
        "Her face is a mask, but I think I see curiosity in her eyes. I wonder if she believes that this isn't my fault."
    
    else:
        "I can't tell what she's thinking."
        
    show valerie hap
    "Valerie latches onto my arm."
    show shou cur behind valerie
    show valerie mis at l1 with dissolve:
        xoffset 0
        xzoom 1
        yzoom 1
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E3/D2/S3/valerie/E3D2L12.ogg"
    vb "You know, if you wanted a younger girl, you only had to ask."
    
    menu:
        "Ask who?":
            pf "Really? Did you have someone in mind?"
            show heart:
                xoffset 515
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap
            "Valerie bats her eyelashes at me."
            pf "Uh… Is there something in your eye?"
            show valerie dis
            "She sighs and lets go of my arm."
            show storm:
                xoffset 515
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D2/S3/valerie/E3D2L13.ogg"
            vb "Nevermind."
    
        "You? HAHA.":
            "I raise an eyebrow."
            pf "You couldn't have meant yourself. I already see wrinkles stretching across your forehead."
            show shocked:
                xoffset 515
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie sur
            "Valerie gasps, mortified at my words."
            show valerie win
            voice "audio/voice/E3/D2/S3/valerie/E3D2L14.ogg"
            vb "Menteur! Vous êtes juste un meanie!"
            "The other girls blink in surprise."
            show valerie ann
            voice "audio/voice/E3/D2/S3/valerie/E3D2L15.ogg"
            vb "Je ne t'aimes pas, imbécile!"
            show shou smi
            voice "audio/voice/E3/D2/S3/shou/31.ogg"
            ss "I don't know what she's saying, but I'm really turned o--"
            show shou win
            voice "audio/voice/E3/D2/S3/shou/33.ogg"
            ss "Ow!"
            show vein:
                xoffset 1250
                yoffset 110
                xzoom .5
                yzoom .5
            "Kaori intervenes with a well placed hit to Shou's arm."
            show kaori ang
            show shou sad
            ki "STOP. BEING. A. PERVERT."
            show kaori ann
    
        "I like them older.":
            pf "Sorry, but I'm into the more mature types."
            show valerie ske
            "Valerie drops my arm."
            voice "audio/voice/E3/D2/S3/valerie/E3D2L16.ogg"
            vb "You mean \"past its prime\"."
            pf "No, I mean more experienced."
            show valerie sad
            "Valerie blinks, then frowns in silence."
            
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show shou neu
    "This is sufficiently awkward."
    show kaori dis
    pf "So, the beach… {w}How about we go swimming?"
    
    
    
    show mayu hap
    show yuuna neu
    "Mayu brightens at the idea."
    show shou cur
    voice "audio/voice/E3/D2/S3/mayu/Mayu-26.ogg"
    ma "Yes! Swimming!"
    hide mayu with dissolve
    hide shou with dissolve
    "She grabs Shou and races towards the water. Shou stumbles behind her."
    show kaori neu
    show yuuna cur
    voice "audio/voice/E3/D2/S3/shou/34.ogg"
    ss "H-Hey! Slow down."
    show kaori mis
    show valerie mis
    "Kaori and Valerie glance at each other, then grin and jump to their feet. They speed behind the pair and leap into the water with glee."
    hide kaori
    hide valerie
    hide yuuna
    with dissolve
    pf "Hey, wait for us!"
        
    show yuuna ner at cc with dissolve
    "Yuuna and I follow behind. When we reach the shore, I slowly wade into the sea and enjoy how the water cools my hot skin."
    voice "audio/voice/E3/D2/S3/valerie/E3D2L17.ogg"
    vb "Come on, Yuuna! What are you waiting for?"
    show drop:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    "Yuuna sticks towards the shore and watches nervously as the water laps at her knees."
    show yuuna wor
    voice "audio/voice/E3/D2/S3/yuuna/11.ogg"
    ym "Um, that's okay. I'll just stay here."
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_18.ogg"
    ki "Do you know how to swim?"
    show yuuna thi
    voice "audio/voice/E3/D2/S3/yuuna/12.ogg"
    ym "Yeah…"
    "Shou and Mayu swim over and stand next to Kaori."
    voice "audio/voice/E3/D2/S3/shou/35.ogg"
    ss "What is it then?"
    show yuuna hap
    voice "audio/voice/E3/D2/S3/yuuna/13.ogg"
    ym "Don't worry about it! I'm very happy right here."
    voice "audio/voice/E3/D2/S3/shou/36.ogg"
    ss "Aww, hanging out by yourself is no fun."
    show yuuna ner
    voice "audio/voice/E3/D2/S3/yuuna/14.ogg"
    ym "The water and I don't really get along well…"
    show mayu smi at l3 with dissolve
    voice "audio/voice/E3/D2/S3/mayu/Mayu-27.ogg"
    ma "Are you scared? Here, you can walk with me!"
    "Mayu stretches out her hand and smiles encouragingly at Yuuna."
    
    if MCStory == 3:
        "As everyone tries to cajole Yuuna into the water, I'm acutely aware of the sudden lack of Valerie…"
        
    show yuuna wor
    voice "audio/voice/E3/D2/S3/yuuna/15.ogg"
    ym "Well, it's more like--"
    show valerie mis at r1 behind yuuna with dissolve:
        xzoom -1
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna sur
    show mayu sur
    stop music fadeout 3
    voice "audio/voice/E3/D2/S3/yuuna/16.ogg"
    ym "Kyaa!"
    hide yuuna with dissolve
    "Yuuna plunges face-first into the water and disappears below the waves."
    pf "Yuuna!"
    hide mayu
    hide valerie
    with dissolve
    "Everyone lunges towards her just as she resurfaces, her back towards us."
    pf "Yuuna, are you okay?"
    voice "audio/voice/E3/D2/S3/yuuna/17.ogg"
    ym "Don't look!"
    
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
    
    "Something floats in front of her, which she snatches out of the water and presses to her chest. Her head is lowered and her shoulders slumped as she struggles to simultaneously hide herself and retie her bikini top at the same time."
    "Mayu clamps a hand over Shou's eyes."
    voice "audio/voice/E3/D2/S3/shou/37.ogg"
    ss "What!"
    voice "audio/voice/E3/D2/S3/mayu/Mayu-28.ogg"
    ma "Don't look."
    
    menu:
        "Offer to help.":
            pf "Do you need help putting that back on?"
            "That sounded a lot less creepy in my head."
            pf "I-I mean, you seem to be having trouble with the knots. {w}I promise I'm not trying to look!"
    
            if yuunaSocialLink >= 3:
                voice "audio/voice/E3/D2/S3/yuuna/18.ogg"
                ym "Y-You promise you won't look?"
                pf "Of course."
                voice "audio/voice/E3/D2/S3/yuuna/19.ogg"
                ym "I can't seem to get these tied…"
                "She offers me the strings to tie up her back. I tie them into a bow with nimble fingers, careful not to touch the smooth, velvety skin of her back too often. Each accidental brush of my fingers against her skin sends warmth into my cheeks."
                pf "Done."
                voice "audio/voice/E3/D2/S3/yuuna/20.ogg"
                ym "Thanks, I've got it from here."
    
            else:
                voice "audio/voice/E3/D2/S3/yuuna/21.ogg"
                ym "N-No! I've got it."
                "She shies away from me and uses her hair to shield her body as much as possible."
                "I better leave her to it before things get out of hand."
                pf "Okay, sorry."
    
    
        "Stay put.":
            "I've already been called a pervert once today… I don't want to make the situation worse."
            
        
    show valerie hap at r3 with dissolve:
        xzoom -1
        
    "Valerie is nearly doubled over on the beach, her squeals of laughter adding to the commotion."
    
    if MCStory != 3:
        "She must have snuck behind Yuuna while we were all distracted then pushed her in."
        
    show kaori dis at cc with dissolve
    "Kaori stalks back to the beach and stands in front of Valerie."
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_19.ogg"
    ki "Why would you do that?"
    show valerie smi
    voice "audio/voice/E3/D2/S3/valerie/E3D2L18.ogg"
    vb "Yuuna looked like she could use a little push to get into the water, so I gave her one."
    show kaori ann
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_20.ogg"
    ki "I bet you did it because you knew exactly what would happen!"
    show valerie ske
    voice "audio/voice/E3/D2/S3/valerie/E3D2L19.ogg"
    vb "I did not! But I won't lie and say it isn't hilarious."
    show kaori dis
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_21.ogg"
    ki "What if she didn't know how to swim? She could have gotten really hurt."
    show valerie mis
    voice "audio/voice/E3/D2/S3/valerie/E3D2L20.ogg"
    vb "It's right against the beach! Completely shallow waters."
    show storm:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ann
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_22.ogg"
    ki "Still, it's dangerous because you can't prepare yourself--"
    stop music fadeout 3
    
    show kaori cur
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_1.ogg"
    ms "Kaori!"
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    
    show mei hap at l1 behind kaori with dissolve
    "A figure with long dark hair leaps onto Kaori's back, holding her in a hug."
    show kaori sur
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_23.ogg"
    ki "Ahh!"
    hide kaori
    hide mei
    with dissolve
    "Kaori windmills her arms trying to catch her balance, but topples into the water."
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_24.ogg"
    ki "Mei!"
    show kaori win at cc with dissolve:
        xzoom -1
    "Kaori pushes Mei off of her and wipes the water out of her eyes."
    show kaori ann
    show mei smi at l3
    show valerie hap
    with dissolve
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_25.ogg"
    ki "You can't just push people into the water! Why don't you people understand this?"
    show note:
        xoffset 1175
        yoffset 125
        xzoom .75
        yzoom .75
    "Valerie is clutching her stomach in laughter."
    ### VOICE - used to say "I can't... So good..." but voice only gave "So good"
    voice "audio/voice/E3/D2/S3/valerie/E3D2L21.ogg"
    vb "So good…"
    show mei hap
    "Mei just smiles and cocks her head to the side."
    show heart:
        xoffset 230
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_2.ogg"
    ms "It's good to see you too!"
    show kaori ang
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_26.ogg"
    ki "That's not what I said!"
    hide kaori with dissolve
    show valerie mis at cc with dissolve
    "Valerie finally catches her breath and wades over to Mei."
    voice "audio/voice/E3/D2/S3/valerie/E3D2L22.ogg"
    vb "Nice one!"
    show mei smi
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_3.ogg"
    ms "Thanks! I'm Mei."
    show valerie smi
    voice "audio/voice/E3/D2/S3/valerie/E3D2L23.ogg"
    vb "Valerie."
    show mei thi
    hide valerie
    with dissolve
    "Mei glances at the rest of us who have been observing in silence, trying to process the scene."
    show mei neu
    show mayu ner at cc:
        xzoom -1
    show shou cur at r3:
        xzoom -1
    with dissolve
    "Mayu coughs awkwardly."
    voice "audio/voice/E3/D2/S3/mayu/Mayu-29.ogg"
    ma "Um, I'm Mayu."
    voice "audio/voice/E3/D2/S3/mayu/Mayu-30.ogg"
    ma "And this is Shou."
    "Shou is very obviously trying to process Mei's ample assets, but at the sound of his name he snaps back to reality."
    show mei mis
    show shou sur
    voice "audio/voice/E3/D2/S3/shou/38.ogg"
    ss "Right, hi!"
    hide mayu
    hide shou
    with dissolve
    show yuuna neu at cc with dissolve:
        xzoom -1
    "Yuuna also seems to be sizing up Mei."
    show mei smi
    voice "audio/voice/E3/D2/S3/yuuna/22.ogg"
    ym "I'm Yuuna."
    hide yuuna with dissolve
    pf "And I'm [pfirst]."
    show mei hap
    "Mei graces us with a broad smile."
    show kaori neu at cc with dissolve:
        xzoom -1
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_4.ogg"
    ms "It's nice to meet you all!"
    show mei smi
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_5.ogg"
    ms "Kaori, when did you make so many friends?"
    show kaori dis
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_27.ogg"
    ki "And now you're leaving."
    show mei cur
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_6.ogg"
    ms "But I only just met everyone."
    show kaori ske
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_28.ogg"
    ki "Don't you have your own friends to hang out with?"
    show mei mis
    voice "audio/voice/E3/D2/S3/mei/MeiEp3_Line_7.ogg"
    ms "I {i}am{/i} hanging out with my friend."
    stop music fadeout 3
    hide mei
    show kaori dis
    with dissolve
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_29.ogg"
    ki "That's not--"
    
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    
    show shocked:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori sur
    voice "audio/voice/E3/D2/S3/kaori/e3d2_Kao_30.ogg"
    ki "Eeee!"
    
    scene black with fade
    # CG

    #show cg group beach 1 with dissolve:
        #xoffset -960
        #yoffset 200
        #xzoom 1
        #yzoom 1
        
    "A jet of water splashes Kaori's face. {w}Mei giggles while Kaori grows more irritated. She flicks her wrist and sends a stream towards Mei… {w}But Mei dodges and it splashes Yuuna's chest instead!"
    $ persistent.gpix[13][0] = 1
    show cg group beach 1 with dissolve:
        xzoom .5
        yzoom .5
        
    #show cg group beach 1:
        #xoffset -960
        #yoffset 200
        #xzoom 1
        #yzoom 1
        #parallel:
            #easein 2.5 alpha 1.0
        #parallel:
            #easein 2.5 xoffset 960 yoffset 300
            
    "Yuuna glances down at her chest, then narrows her eyes, clearly fed up. Using her whole arm, she sends a big wave back towards Kaori, but the water misses and catches Valerie, who squeals happily. {w}She sends a small splash back, which catches Mayu on the cheek."
    
    #show cg group beach 1:
        #xoffset 960
        #yoffset 300
        #xzoom 1
        #yzoom 1
        #parallel:
            #easein 2.5 alpha 1.0
        #parallel:
            #easein 2.5 xoffset 0 yoffset 0 xzoom .5 yzoom .5
            
    "Mayu blinks. {w}Valerie's brow wrinkles in worry and she opens her mouth to apologise, but instead, dodges the splash that Mayu sends back."
    "Before long, all the girls are squealing and bouncing around in the water, splashing each other."
    
    #$renpy.pause(1)
    #scene black with fade
    #$renpy.pause(1)
    
    #scene bg vacation beach day with fade:
        #xzoom 1
        #yzoom 1
        #xalign .01
        #yalign .99
        
    #show shou smi at l2 with dissolve
    "Shou and I stand off to the side watching the glorious view."
    #stop music fadeout 5
    #show drooling:
        #xoffset 365
        #yoffset 20
        #xzoom .75
        #yzoom .75
    #show shou hap
    voice "audio/voice/E3/D2/S3/shou/39.ogg"
    ss "Is this not the best thing you've ever seen in your life?"
    "I nod solemnly, but another voice answers."
    voice "audio/voice/E3/D2/S3/akira/1.ogg"
    am "Yes, yes it is."
    
    #play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    
    #show akira hap at r2:
        #xzoom -1
    #show shou cur
    #with dissolve
    "As one, Shou and I turn and see Akira nodding approvingly."
    pf "Uh, when did you get here?"
    #show akira ske
    "He gives me a confused look."
    voice "audio/voice/E3/D2/S3/akira/2.ogg"
    am "I've been here this whole time."
    #show shou ske
    "Shou and I glance at each other, then shrug."
    #show akira neu
    #show shou neu
    pf "I think I've seen Mei before... She's part of Onna-Bugeisha, right?"
    voice "audio/voice/E3/D2/S3/akira/3.ogg"
    am "Yeah."
    "I remember Kaori's intense reaction when we learned we were matched against Mei's team, but Mei seems to treat her like they are old friends."
    
    scene bg vacation beach day with dissolve: #
        xzoom 1
        yzoom 1
        xalign 0.5
        yalign 0.8
        
    show akira neu at r2: #
        xzoom -1 #
    show shou neu at l2 #
    with dissolve #
    
    pf "How do Mei and Kaori know each other? They seem to have opposite reactions when seeing each other."
    show shou thi
    ### VOICE - missing line
    voice "audio/voice/MISSING/BATCH2/1.ogg"
    ss "Their relationship is strange. They've known each other since childhood, but judging by the way they act towards each other, it's hard to remember that."
    show shou neu
    "The conversation ends. Silence settles in as we continue to watch the splash attacks."
    show akira smi
    voice "audio/voice/E3/D2/S3/akira/4.ogg"
    am "Why aren't we joining in on the fun?"
    show akira hap
    show shou smi
    voice "audio/voice/E3/D2/S3/shou/40.ogg"
    ss "That's a great question."
    hide shou with dissolve
    hide akira with dissolve
    stop music fadeout 7
    stop ambient fadeout 7
    "Shou swims closer to the girls and shoots a stream of water towards Mayu. Mayu yelps in surprise and splashes back when she sees Shou's grin. {w}Akira and I join in after Shou's introduction into the splash war."

    scene black with fade
    
    jump E3D2S4

