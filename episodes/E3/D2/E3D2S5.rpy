#
label E3D2S5:
    
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    scene bg vacation beach dusk with fade
    
    "As I search the beach, I find Shou and Mayu sitting on a rock cliff, their feet dangling in the water."
    show mayu smi b1 at l1
    show shou smi at r1 behind mayu:
        xzoom -1
    with dissolve
    
    menu:
        "Call out.":
            
            play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
            
            show mayu sur b2 at l1
            show shou sur b1 at r1
            with dissolve
            show exclamation:
                xoffset 890
                yoffset 20
                xzoom .75
                yzoom .75
            show shoBlush:
                xoffset 515
                yoffset 135
                xzoom .75
                yzoom .75
            pf "Hey, you guys!"
            show mayu ner b2 at l1
            show shou ner b1 at r1
            "They jerk away from each other, putting as much space between them as they can. Mayu stares at the water while Shou grins nervously at me."
            show shou hap b1 at r1
            voice "audio/voice/E3/D2/S5/shou/50.ogg"
            ss "H-Hey, broseph."
    
            if MCStory == 3:
                pf "Sorry, I didn't mean to interrupt…"
                show drop:
                    xoffset 890
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou thi b1 at r1
                voice "audio/voice/E3/D2/S5/shou/51.ogg"
                ss "No, you weren't interrupting. We were just, uh, watching the sunset. Right, Mayu?"
                show mayu neu b2 at l1
                voice "audio/voice/E3/D2/S5/mayu/Mayu-48.ogg"
                ma "Y-Yeah."
                show shou smi at r1 with dissolve
                voice "audio/voice/E3/D2/S5/shou/52.ogg"
                ss "And now it's set, so uh- we should head back."
    
            else:
                pf "What are you guys doing here?"
                show panic:
                    xoffset 890
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou wor b1 at r1
                voice "audio/voice/E3/D2/S5/shou/53.ogg"
                ss "Nothing! Just watching the sunset."
                show mayu neu b2 at l1
                "Mayu nods."
                show shou ner at r1
                pf "Oh, cool. {w}Anyway, it's starting to get dark so we're all thinking of going home."
                show shou thi at r1
                ### VOICE - used to have "Let's go, Mayu" at the end
                voice "audio/voice/E3/D2/S5/shou/54.ogg"
                ss "That makes sense."
                show mayu ner b1 at l1
                voice "audio/voice/E3/D2/S5/mayu/Mayu-49.ogg"
                ma "Okay."
    
            hide mayu
            hide shou
            with dissolve
            stop music fadeout 5
            "He leaps to his feet and walks past me. Mayu continues to keep some distance between her and Shou but follows him off of the rock cliff."
            scene black with fade
            pf "Wait up!"
            
            $renpy.pause(1)
            scene bg vacation beach dusk with fade
    
            play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
            
            "Everyone was waiting for us when we rejoined the group."
            show mayu neu at l3
            show shou smi at cc
            show yuuna smi at r3:
                xzoom -1
            with dissolve
            pf "You guys didn't pack up yet?"
            voice "audio/voice/E3/D2/S5/yuuna/40.ogg"
            ym "We figured we'd do it together since we wanted to walk to the parking lot together anyway."
            show mayu smi at l3
            "Mayu smiles."
            show mayu hap at l3
            voice "audio/voice/E3/D2/S5/mayu/Mayu-50.ogg"
            ma "Thanks for waiting."
            
            "Yuuna nods."
    
        "Leave them be.":
            hide mayu
            hide shou
            with dissolve
            "They're leaning into each other, watching the sunset."
            
            scene black with fade
            "I don't want to disturb their moment, so I slip away before I'm noticed."
            $renpy.pause(1)
            scene bg vacation beach dusk with fade
            
            show valerie neu at cc
            show kaori neu at l3
            show yuuna ske at r3:
                xzoom -1
            with dissolve
            "The girls give me questioning looks as I return."
            
            play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
            voice "audio/voice/E3/D2/S5/yuuna/41.ogg"
            ym "Did you find them?"
    
            menu:
                "Yes.":
                    $ E3D2S5_Voyeur = 1
                    pf "Yeah, but they seemed to be in the middle of something and I didn't want to interrupt them."
                    show valerie mis at cc
                    show yuuna neu at r3
                    "Valerie smirks."
                    show note:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/D2/S5/valerie/E3D2L39.ogg"
                    vb "I bet you just wanted to watch."
                    show kaori ske at l3
                    pf "W-What?!"
                    show valerie hap at cc
                    voice "audio/voice/E3/D2/S5/valerie/E3D2L40.ogg"
                    vb "I mean, you were gone for a while…"
                    show shoBlush:
                        xoffset 1175
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna sur b1 at r3
                    voice "audio/voice/E3/D2/S5/yuuna/42.ogg"
                    ym "Out on the beach? That's quite daring..."
                    show yuuna cur b1 at r3
                    "Yuuna seems thoughtful but has a mischievous glint in her eye."
                    show kaori cur at l3
                    pf "They didn't!"
                    show valerie cur at cc
                    show yuuna sur b1 at r3
                    "Valerie and Yuuna glance at each other and burst out laughing."
                    show valerie hap at cc
                    show yuuna hap b1 at r3
                    "My cheeks burn as I realise what I'd just said."
                    pf "I mean, nothing was going on!"
                    show kaori dis at l3
                    "Kaori frowns."
                    show valerie smi at cc
                    show yuuna smi at r3
                    voice "audio/voice/E3/D2/S5/kaori/e3d2_Kao_46.ogg"
                    ki "So you {i}did{/i} watch?"
                    pf "There was nothing to watch!"
                    show yuuna sur at r3
                    stop music fadeout 1
                    voice "audio/voice/E3/D2/S5/shou/55.ogg"
                    ss "Hey guys, what's everyone laughing about?"
                    hide kaori
                    hide valerie
                    hide yuuna
                    with dissolve
                    show kaori neu at l3:
                        xoffset -100
                    show mayu neu at r3:
                        xoffset 100
                        xzoom -1
                    show shou smi at r2:
                        xzoom -1
                    show valerie smi at cc
                    show yuuna ner at l2 behind valerie
                    with dissolve
                    "Shou and Mayu stand by their towels."
                    voice "audio/voice/E3/D2/S5/valerie/E3D2L41.ogg"
                    vb "We were just talking about how there was nothing going on--"
                    
                    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
                    
                    pf "It's not funny when she has to explain it. Anyway, we should be going. It's getting late."
                    show mayu thi at r3
                    show shou ske at r2
                    "Shou and Mayu look at each other before shrugging. They nod at us."
    
                "No.":
                    $ E3D2S5_Voyeur = 0
                    pf "No, I didn't find them."
                    show kaori ske at l3
                    "Kaori looks skeptical."
                    show yuuna neu at r3
                    voice "audio/voice/E3/D2/S5/kaori/e3d2_Kao_47.ogg"
                    ki "This beach isn't that big."
                    show valerie ske at cc
                    voice "audio/voice/E3/D2/S5/valerie/E3D2L42.ogg"
                    vb "They must {i}really{/i} want to be alone…"
                    show kaori neu at l3
                    show yuuna ner at r3
                    voice "audio/voice/E3/D2/S5/yuuna/43.ogg"
                    ym "Maybe one of us should look for them?"
                    pf "No, the sun's already set so I'm sure they're on their way back now."
    
                    hide kaori
                    hide valerie
                    hide yuuna
                    with dissolve
                    show yuuna neu at l3:
                        xoffset -250
                    show mayu neu at r3:
                        xoffset 250
                        xzoom -1
                    show shou smi at r2:
                        xzoom -1
                    show valerie neu at cc:
                        xoffset -100
                    show kaori neu at l2 behind valerie:
                        xoffset -100
                    with dissolve
                    stop music fadeout 5
                    "As if on cue, the two of them appear in the distance. {w}As they approach, Shou grins apprehensively under everyone's gaze."
                    
                    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
                    
                    show shou hap at r2
                    voice "audio/voice/E3/D2/S5/shou/56.ogg"
                    ss "What's going on?"
                    voice "audio/voice/E3/D2/S5/kaori/e3d2_Kao_48.ogg"
                    ki "Where were you?"
                    show drop:
                        xoffset 1040
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou smi at r2
                    voice "audio/voice/E3/D2/S5/shou/57.ogg"
                    ss "Uh, off watching the sunset…"
                    show kaori thi at l2
                    show mayu ner at r3
                    voice "audio/voice/E3/D2/S5/kaori/e3d2_Kao_49.ogg"
                    ki "No, I mean {i}where{/i} were you?"
                    show shou wor at r2
                    voice "audio/voice/E3/D2/S5/shou/58.ogg"
                    ss "We were really just watching the sunset!"
                    show panic:
                        xoffset 1425
                        yoffset 135
                        xzoom .75
                        yzoom .75
                    show mayu wor at r3
                    show kaori ske at l2
                    voice "audio/voice/E3/D2/S5/mayu/Mayu-51.ogg"
                    ma "Yeah, that's it! Nothing else!"
                    show yuuna ske at l3
                    "Is that sweat on their foreheads?"
                    show mayu ner at r3
                    show valerie mis at cc
                    voice "audio/voice/E3/D2/S5/valerie/E3D2L43.ogg"
                    vb "That's not a weird response."
                    "I reply before Valerie can cause any trouble."
                    show kaori neu at l2
                    show yuuna smi at l3
                    pf "The sun's already set so we should get going."
                    show mayu smi at r3
                    voice "audio/voice/E3/D2/S5/mayu/Mayu-52.ogg"
                    ma "Yeah, that's a good idea."
                    show shou smi at r2
                    "Shou nods."
    hide kaori
    hide mayu
    hide shou
    hide valerie
    hide yuuna
    with dissolve
    
    label E3D2S5_Mayu:
        $ something = "anything"
        
    "We all pack up our belongings and head to the parking lot, where we say our goodbyes and hop in our respective vehicles."
    "Since Nikki said she was leaving with her friends, I kick my bike into gear and drive home."
    stop music fadeout 5
    
    #fade out
    scene black with fade
    $renpy.pause(1)
    #fade in
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    $renpy.pause(.5)
    scene bg homekaito main night with fade
    "I'm exhausted by the time I get home and am secretly thankful Uncle Kaito is nowhere in sight. All I want to do is take a hot shower and go to bed."
    scene bg homekaito myroom night with fade
    "Nikki hasn't come home yet either, so the bathroom is all mine. I wash the sand and salt water off my skin, then go to sleep early."
    scene black with fade
    
    jump E3D3S1

