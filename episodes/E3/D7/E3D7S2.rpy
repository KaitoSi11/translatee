#
label E3D7S2:
    
    #play ambient "audio/ambience/Mall.ogg" fadein 3
    #scene bg mall main day with fade
    "Soon, I arrive at the concert hall. I wander around the hall and through the people bustling back and forth, before finding the entrance backstage."
    "There's a passage between the hall and the arcade as the properties are owned by the same family. As I pass through, I spot the signs directing me to the Dasshu VIP arcade lounge."
    
    stop music fadeout 5
    scene black with fade
    "After proving my identity to the guard, I enter."
    stop ambient fadeout 3
    $renpy.pause(1)
    
    #arcade BG
    #play ambient "audio/ambience/Arcade.ogg" fadein 1
    scene bg nightclub with fade
    
    "As soon as I walk in, I spot many recognisable faces. Wiger Toods, Sidney Crossbow, Shanille O'Keal, Ristiano Cronaldo just to name a few."
    "I keep waiting for someone to stop me and ask me what I'm doing here, but no one does. A few people glance at me in passing, some even flash me a smile as if to say \"you're one of us now\"."
    "Walking in the same room as these people is intimidating, but also exhilarating. {w}Scanning the room, I don't see Ex Zee anywhere..."
    voice "audio/voice/E3/D7/S2/shou/2.ogg"
    ss "Broseph!"
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    show kaori neu at r3:
        xzoom -1
    show mayu neu at l3
    show shou smi at cc
    with dissolve
    "I turn around and see Shou, Mayu, and Kaori approaching me."
    
    pf "Hey guys."
    show shou hap
    voice "audio/voice/E3/D7/S2/shou/3.ogg"
    ss "Can you believe this?! My inner fanboy is going off the charts!"
    show kaori thi
    "Kaori shrugs."
    voice "audio/voice/MISSING/BATCH5/k_redo_07.ogg"
    ki "I don't see what the big fuss is."
    show shou smi
    voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-01.ogg"
    ma "Me neither--"
    show mayu sur
    "Mayu chokes on her words and her eyes widen at the sight of someone."
    show exclamation:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    ma "!!!"
    show kaori neu
    "I follow her line of sight, expecting Ex Zee, but instead, I see some old dude with white hair."
    voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-02.ogg"
    ma "A-Ah-AH-a-h... I-Its..."
    pf "Breathe, Mayu."
    show mayu wor
    show shou neu
    "She takes a deep breath."
    voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-03.ogg"
    ma "It's Reboote Von Baythoven!"
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou ske
    voice "audio/voice/E3/D7/S2/shou/4.ogg"
    ss "Who's that?"
    show mayu ang
    voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-04.ogg"
    ma "WHO'S THAT?!"
    show shou ner
    "If looks could kill, Shou would already be on the ground bleeding."
    show mayu neu
    show frightful:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou wor
    voice "audio/voice/E3/D7/S2/shou/5.ogg"
    ss "Ah!"
    "As Shou cowers, Mayu closes her eyes and sets her jaw determinedly. Then, with shaking legs, she walks toward the man."
    hide mayu
    show shou thi
    with dissolve
    voice "audio/voice/E3/D7/S2/shou/6.ogg"
    ss "Well. Then."
    
    if kaorelatonship == 1:
        show kaori mis
        "Kaori and I glance at each other and laugh."
    
    else:
        show kaori cur
        "Kaori blinks in surprise."
    
    "I doubt any of us imagined Mayu was capable of something so terrifying."
    show shou neu
    "Mayu stalks closer to Reboote Von Baythoven, but as soon as his attention lands on her she becomes rooted to the ground."
    pf "Uh oh..."
    "He waits patiently for her, watching her curiously. She remains frozen, so he smiles and pats her on the head, then resumes his journey to the buffet tables."
    "After Mayu's internal systems reboot, she hops back to us with starstruck eyes."
    
    show kaori neu
    show mayu cur b2 at l3
    show shou neu
    with dissolve
    voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-05.ogg"
    ma "He... He touched me."
    
    menu:
        "I'm happy for you!":
            pf "I'm glad you were able to meet one of your heroes!"
            show mayu hap b1
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-06.ogg"
            ma "He's not just a hero! He's {i}Reboote Von Baythoven{/i}!"
            show note:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-07.ogg"
            ma "The greatest classical composer to exist since the original!"
            "I can't help but smile at the passion in her voice and hold up my hands in defense."
            pf "No arguments here."
    
        "I wouldn't phrase it like that...":
            pf "You might want to think about what you just said and then try again."
            "Shou and Kaori nod in agreement while Mayu's cheeks flush."
            show shoBlush:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur b2
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-08.ogg"
            ma "T-That's not what I meant! It's just… It's {i}Reboot Von Baythoven!{/i} The greatest classical composer to exist since the original!"
            pf "Seriously? That's his tagline?"
    
        "What's the big deal?":
            pf "I still don't get it."
            show mayu sur b2
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-09.ogg"
            ma "{i}Reboote Von Baythoven{/i}! He's--"
            voice "audio/voice/E3/D7/S2/shou/7.ogg"
            ss "The greatest classical composer to exist since the original."
            show mayu smi b2
            "Shou repeats the words flatly, like he's heard this a million times before."
            show note:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu hap b2
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-10.ogg"
            ma "Exactly!"
            pf "Uh, okay."
            
    show mayu neu b1
    voice "audio/voice/E3/D7/S2/valerie/E3D7L1.ogg"
    vb "Hello beautiful people!"
    
    hide kaori
    hide shou
    hide mayu
    with dissolve
    
    show kaori neu at l1:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show mayu neu b1 at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show shou smi at l2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show valerie hap at r1:
        xoffset 50
        xzoom -0.75
        yzoom 0.75
    with dissolve
    "Valerie is all smiles as she approaches. She throws an arm about me and Kaori, much to Kaori's dismay."
    voice "audio/voice/E3/D7/S2/valerie/E3D7L2.ogg"
    vb "What's with all the excitement?"
    voice "audio/voice/E3/D7/S2/shou/8.ogg"
    ss "Mayu just met Baythoven."
    show exclamation:
        xoffset 1000
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie sur
    voice "audio/voice/E3/D7/S2/valerie/E3D7L3.ogg"
    vb "You mean {i}the{/i} Ludvig Von Baythoven?!"
    "I can't tell if she's being sarcastic or not."
    pf "No, Reboote."
    show mayu smi b1
    "Mayu nods happily."
    show valerie cur
    voice "audio/voice/E3/D7/S2/valerie/E3D7L4.ogg"
    vb "Oooh, he's the greatest classical composer to exist since the original!"
    pf "Seriously?"
    show mayu hap b1
    show valerie mis
    "Mayu bursts out laughing and Valerie joins in. Their laugh is contagious and soon we've all joined in. {w}When we finally catch our breaths, Kaori looks around."
    show kaori ske
    show mayu smi
    voice "audio/voice/MISSING/BATCH5/k_redo_02.ogg"
    ki "Where's Yuuna?"
    show shou cur
    ### VOICE - missing line
    voice "audio/voice/MISSING/BATCH2/4.ogg"
    ss "Not sure. She might be busy handling logistics and stuff?"
    pf "That makes sense, actually."
    show kaori neu
    show mayu neu
    show shou neu
    "A man in a Dasshu hat interrupts us."
    voice "audio/voice/E3/D7/S2/dass1/1.ogg"
    dass1 "Hey, are you guys from ACE Academy?"
    show valerie neu
    voice "audio/voice/MISSING/BATCH5/k_redo_03.ogg"
    ki "Yes."
    "He checks off a name on his clipboard."
    voice "audio/voice/E3/D7/S2/dass1/2.ogg"
    dass1 "You're up for the photoshoot. Please come with me."
    "We look at each other, then shrug and follow him."
    stop music fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    scene bg nightclub with fade
    "He leads us to a secluded area behind a wall of curtains. There's a station already set up on a stage with a backdrop and lighting equipment. A man with a tied-back ponytail barks directions at the models, his camera at the ready. {w}Yuuna stands to the side and studies the clipboard in her hand. As our manager, I guess part of her job is coordinating any events we attend. I hope she doesn't have to work the whole time..."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    # show them all and then yuuna
    show kaori neu at l1:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show mayu neu b1 at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show shou smi at l2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show valerie smi at r1:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show yuuna neu at r3:
        xoffset 50
        xzoom -0.75
        yzoom 0.75
    with dissolve
    
    pf "Hey, Yuuna."
    show yuuna hap
    "She glances over at us and grins."
    voice "audio/voice/E3/D7/S2/yuuna/1.ogg"
    ym "You're here! Sorry I haven't had a chance to say hi."
    pf "Are you helping with the whole event?"
    show yuuna smi
    voice "audio/voice/E3/D7/S2/yuuna/2.ogg"
    ym "No, I've just been getting our team affairs in order. You guys are doing okay?"
    show kaori smi
    show mayu smi
    show shou smi
    "We all nod."
    voice "audio/voice/E3/D7/S2/yuuna/3.ogg"
    ym "Great! Well, they want a team photo of all of us. I've already worked it out with our photographer. We're going to be here..."
    hide kaori
    hide mayu
    hide shou
    hide valerie
    hide yuuna
    with dissolve
    "She leads us to the stage where the photographer is waiting. He directs us into a normal group stance with bright smiles. The shutter clicks constantly as he captures us from different angles."
    voice "audio/voice/E3/D7/S2/photo1/1.ogg"
    photo1 "Perfect!... Excellent!... Very nice!"
    "Once he gets the takes he needs, Shou wants to take a \"cool\" photo. With the photographer's permission, we hold action poses, trying to look as badass as possible."
    "This is pretty fun!"
    
    
    show kaori smi at l1:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show mayu smi b1 at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show shou smi at l2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show valerie smi at r1:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show yuuna smi at r3:
        xoffset 50
        xzoom -0.75
        yzoom 0.75
    with dissolve

    stop music fadeout 5
    voice "audio/voice/E3/D7/S2/photo1/2.ogg"
    photo1 "Now we need a solo model from the team."
    voice "audio/voice/E3/D7/S2/photo1/3.ogg"
    photo1 "While I work on setup, Yuuna, please coordinate who will be your swimsuit model."
    
    show yuuna sur
    voice "audio/voice/E3/D7/S2/yuuna/4.ogg"
    ym "A swimsuit?!"
    show kaori ske
    show mayu cur
    show shou cur
    "The photographer sighs impatiently."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E3/D7/S2/photo1/4.ogg"
    photo1 "Yes! It'll be used for our upcoming catalog, the {i}Taste of Summer{/i}! What's more summer-y than a warm beach?"
    show yuuna ner
    "He walks off before Yuuna can protest."
    voice "audio/voice/E3/D7/S2/yuuna/5.ogg"
    ym "Um, did you guys hear that?"
    show kaori neu
    show mayu neu
    show shou neu
    "We nod."
    show yuuna thi
    voice "audio/voice/E3/D7/S2/yuuna/6.ogg"
    ym "...Who should do it?"
    
    menu:
        "Kaori can do it!":
            pf "It should be our fearless team captain, Kaori!"
            show shoBlush:
                xoffset 575
                yoffset 110
                xzoom .5
                yzoom .5
            show kaori sur b2 with dissolve
            "Kaori blushes."
            show kaori ang b2
            show shou cur b1
            show yuuna ner
            voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_01.ogg"
            ki "What?! No way! Go to hell, you perverted idiot!"
            show kaori ann b2
            
            menu:
                "You look so good in a bikini though!":
                    pf "But at the beach you looked so cute in a--"
                    # sfx
                    # screen shake?
                    "{i}wham!{/i}"
                    show vein:
                        xoffset 575
                        yoffset 110
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_02.ogg"
                    ki "No means {b}NO{/b}."
                    show shou ner
                    pf "Ow…"
                    show kaori ann b1
                    show mayu ner
                    show shou thi
                    show valerie thi
                    "As I rub at the sore spot, I try to catch the eyes of my teammates, but they pointedly look away. I guess no one else wants to suffer the same fate I have…" 
                    jump E3D7S2_ConvinceFailed

                "You couldn't pull it off anyway.":
                    pf "Mm, I'm not surprised. At least you recognise you lack the necessary {i}assets{/i} for modeling."
                    show kaori sur b2
                    show shou sad
                    "Shou solemnly nods."
                    "Kaori's eyes widen, then she frowns."
                    show kaori ang b2
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_03.ogg"
                    ki "We'll see about that!"
                    hide kaori
                    show shou cur b1
                    with dissolve
                    $ kaoOut = "sSwimsuit"
                    $renpy.pause(1)
                    # show her in her spot again
                    show kaori dis at l1 with dissolve:
                        xoffset 75
                        xzoom 0.75
                        yzoom 0.75
                    "She stomps into the changing room and returns a moment later in a two piece bikini. {w}Damn! She looks even better than last time. My face feels like it's on fire. Shou is just as captivated as I am."
                    show note:
                        xoffset 575
                        yoffset 110
                        xzoom .5
                        yzoom .5
                    show kaori mis b1
                    $renpy.pause(1)
                    hide kaori
                    show shou ske b1
                    with dissolve
                    "With a hand on her hip, Kaori gives us one last challenging glare before heading to the stage."
                    show yuuna ske
                    voice "audio/voice/E3/D7/S2/yuuna/7.ogg"
                    ym "...Did she really just fall for that?"
                    show mayu smi
                    show shou mis
                    show valerie hap
                    "Valerie bursts out laughing while Mayu suppresses a giggle. Shou and I fist bump."
                    voice "audio/voice/E3/D7/S2/photo1/5.ogg"
                    photo1 "Woah! Great choice!"
                    show yuuna neu
                    "Kaori poses for the camera."
                    voice "audio/voice/E3/D7/S2/photo1/6.ogg"
                    photo1 "Excellent!... Perfect!..."
                    show valerie smi
                    "I'm positive in that last pose she just leaned in to show off her \"lack of assets\"."
                    pf "I stand corrected."
                    show heart:
                        xoffset 315
                        yoffset 20
                        xzoom .5
                        yzoom .5
                    show shou hap
                    voice "audio/voice/E3/D7/S2/shou/9.ogg"
                    ss "This... is the best day... of my life."
                    voice "audio/voice/E3/D7/S2/photo1/7.ogg"
                    photo1 "Beautiful!... Now give me a smile..."
                    "Kaori glares at the photographer."
                    voice "audio/voice/E3/D7/S2/photo1/8.ogg"
                    photo1 "Uh, nevermind! Fierce is good! Let's capture fierce!"
                    "After a few more shots, Kaori struts back to us, a smug grin on her face."
                    # show her again
                    show kaori mis at l1 with dissolve:
                        xoffset 75
                        xzoom 0.75
                        yzoom 0.75
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_04.ogg"
                    ki "There."
                    "I surrender with my hands up."
                    pf "Oh yes, you really showed us."
                    show shou mis
                    voice "audio/voice/E3/D7/S2/shou/10.ogg"
                    ss "Yes indeed."
                    show yuuna thi
                    voice "audio/voice/E3/D7/S2/yuuna/8.ogg"
                    ym "Um, Kaori... you can go change..."
                    show kaori cur b2 with dissolve
                    "Kaori's face burns as brightly as her hair. She hurries back into the changing room."
                    hide kaori with dissolve
                    $ kaoOut = "sFashion"
                    show valerie mis
                    voice "audio/voice/E3/D7/S2/valerie/E3D7L5.ogg"
                    vb "Who would have thought this would be so much fun!"
                    # show again
                    show kaori neu b2 at l1 with dissolve:
                        xoffset 75
                        xzoom 0.75
                        yzoom 0.75
                    "Kaori returns wearing her previous outfit. Her face is still red."
                    show tsuBlush:
                        xoffset 575
                        yoffset 110
                        xzoom .5
                        yzoom .5
                    show kaori thi b2
                    show yuuna smi
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_05.ogg"
                    ki "Don't say anything."
                    show shou smi
                    "We all look at each other and laugh."
                    jump E3D7S2_PhotoComplete
                                
                "Do it for the team.":
                    pf "Think about the team!"
                    show kaori ang b2
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_06.ogg"
                    ki "Don't try to guilt me into prancing around half naked for a photo shoot!"
                    show kaori ann b2
                    show shou hap
                    voice "audio/voice/E3/D7/S2/shou/1.ogg"
                    ss "What if we say please?"
                    # sfx
                    # shake Shou?
                    show shou sur
                    "Kaori slugs Shou on the shoulder."
                    show shou wor
                    voice "audio/voice/E3/D7/S2/shou/11.ogg"
                    ss "Why are you just hitting me? It was his idea!"
                    # sfx
                    # shake again?
                    show shou win
                    "Kaori hits Shou again."
                    show shou ang
                    show question:
                        xoffset 315
                        yoffset 20
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E3/D7/S2/shou/12.ogg"
                    ss "WHYYYYY?"
                    show shou ann
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_07.ogg"
                    ki "You think I don't know you two were planning this all along?"
                    "Shou looks at me for help. I shrug."
                    pf "Damn, she caught us. It was all his idea, Kaori."
                    show vein:
                        xoffset 575
                        yoffset 110
                        xzoom .5
                        yzoom .5
                    show kaori ang b2
                    show shou wor
                    voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_08.ogg"
                    ki "I knew it!"
                    show kaori ann b2
                    show panic:
                        xoffset 315
                        yoffset 20
                        xzoom .5
                        yzoom .5
                    voice "audio/voice/E3/D7/S2/shou/13.ogg"
                    ss "HE'S LYING!"
                    # sfx
                    # shake again?
                    show shou win
                    "{i}WHAM!{/i}"
                    show shou ang
                    voice "audio/voice/E3/D7/S2/shou/14.ogg"
                    ss "STAHP!"
                    show shou ann
                    jump E3D7S2_ConvinceFailed
    
    
        "Yuuna should!":
            pf "How about you, Yuuna?"
            show yuuna cur
            "Yuuna's eyes widen."
            show shou cur
            show panic:
                xoffset 1350
                yoffset 100
                xzoom .5
                yzoom .5
            voice "audio/voice/E3/D7/S2/yuuna/9.ogg"
            ym "What… Why me?"
            
            menu:
                "You're our connection to Dasshu.":
                    pf "As far as Dasshu is concerned, you're the face of our team. They know you a lot better than any of us."
                    show shou smi
                    voice "audio/voice/E3/D7/S2/shou/15.ogg"
                    ss "Plus you can vet any material they would want to use without having to go back and forth between any of us."
                    show dots:
                        xoffset 1350
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    show yuuna thi
                    "Yuuna thinks about our argument, then sighs."
                    show yuuna neu
                    voice "audio/voice/E3/D7/S2/yuuna/10.ogg"
                    ym "I guess that makes sense."
                    jump E3D7S2_YuunaBikini
    
                "There's more to GEAR teams than just pilots.":
                    pf "When people think of a GEAR team, they only think about the pilots because pilots are the only members they really see."
                    pf "Wouldn't it be great to have a normally \"faceless\" team member be the face of our team? A team with just pilots isn't a team at all."
                    show shou smi
                    voice "audio/voice/E3/D7/S2/shou/16.ogg"
                    ss "Yeah! Give some recognition to the other people who work in the field of Cenorobotics. It's not just all about us pilots! Who knows, you might just inspire someone who never thought they had a place in this field."
                    show yuuna sur
                    "Yuuna's eyes widen."
                    voice "audio/voice/E3/D7/S2/yuuna/11.ogg"
                    ym "Really? Do you think I can make that much of a difference?"
                    show note:
                        xoffset 315
                        yoffset 20
                        xzoom .5
                        yzoom .5
                    show shou hap
                    "Shou and I nod."
                    show yuuna thi
                    voice "audio/voice/E3/D7/S2/yuuna/12.ogg"
                    ym "Well, if you guys feel that strongly about it..."
    
                    label E3D7S2_YuunaBikini:
                        show drop:
                            xoffset 575
                            yoffset 110
                            xzoom .5
                            yzoom .5
                        show kaori ske
                        voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_09.ogg"
                        ki "You don't have to do it if you're uncomfortable."
                        show yuuna smi
                        voice "audio/voice/E3/D7/S2/yuuna/13.ogg"
                        ym "No, it's okay. As the manager, I'm supposed to handle all situations that are thrown at us."
                        hide yuuna with dissolve
                        $ yuuOut = "sSwimsuit"
                        $renpy.pause(1)
                        "Yuuna heads into the changing room. A few minutes later, she emerges wearing a bikini."
                        # put yuuna back
                        show yuuna smi at r3:
                            xoffset 50
                            xzoom -0.75
                            yzoom 0.75
                        show kaori cur
                        show mayu cur
                        show shou cur
                        with dissolve
                        "It's very reminiscent of what she wore at the beach. My face heats up as I recall the beach incident. Everyone else seems to be just as captivated as I am."
                        show valerie sad
                        "Valerie pouts, then sighs."
                        show valerie smi
                        voice "audio/voice/E3/D7/S2/valerie/E3D7L6.ogg"
                        vb "You're so pretty, Yuuna. I'm kind of jealous."
                        show yuuna ner
                        voice "audio/voice/E3/D7/S2/yuuna/14.ogg"
                        ym "I don't know about that..."
                        show mayu ner b1
                        voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-11.ogg"
                        ma "I... I would have to agree."
                        show yuuna hap
                        "Yuuna beams happily."
                        show note:
                            xoffset 1350
                            yoffset 100
                            xzoom .5
                            yzoom .5
                        voice "audio/voice/E3/D7/S2/yuuna/15.ogg"
                        ym "You guys are too kind."
                        show kaori neu
                        voice "audio/voice/E3/D7/S2/photo1/9.ogg"
                        photo1 "Yuuna! Are you ready?"
                        show yuuna smi
                        voice "audio/voice/E3/D7/S2/yuuna/16.ogg"
                        ym "Coming!"
                        show kaori dis
                        show mayu neu
                        hide yuuna
                        with dissolve
                        "Shou and I stare as she gracefully steps onto the stage."
                        # sfx?
                        "I feel a sharp flick behind my ear."
                        show shou win
                        show valerie smi
                        voice "audio/voice/E3/D7/S2/shou/17.ogg"
                        ss "Ow!"
                        pf "Hey!"
                        show kaori ske
                        show shou thi
                        voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_10.ogg"
                        ki "Can you two stop ogling her like that?"
                        show storm:
                            xoffset 315
                            yoffset 20
                            xzoom .5
                            yzoom .5
                        "Shou rubs his ear and mumbles under his breath."
                        voice "audio/voice/E3/D7/S2/shou/18.ogg"
                        ss "N-No…"
                        show kaori dis
                        voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_11.ogg"
                        ki "What was that?"
                        show shou wor
                        voice "audio/voice/E3/D7/S2/shou/19.ogg"
                        ss "Nothing!"
                        show shou neu
                        "Yuuna beams at the camera as the photographer directs her. She poses confidently and seems to genuinely enjoy herself. Somehow she makes a bikini look so elegant."
                        $ yuuOut = "sFlirty"
                        "Once finished, she heads back to the changing room and returns in her original outfit. I'd be lying if I said I wasn't a little disappointed."
                        # show yuuna again
                        show yuuna smi at r3 with dissolve:
                            xoffset 50
                            xzoom -0.75
                            yzoom 0.75
                        voice "audio/voice/E3/D7/S2/yuuna/17.ogg"
                        ym "That wasn't so bad."
                        jump E3D7S2_PhotoComplete
    
                "You're the most well endowed one here.":
                    pf "I think the reason is fairly {i}big{/i} and obvious."
                    show kaori dis
                    show shou mis
                    voice "audio/voice/E3/D7/S2/shou/20.ogg"
                    ss "I think you mean {i}reasons{/i}."
                    show mayu ske
                    pf "Ah, you're right. Well played, sir."
                    show shou hap
                    show yuuna ske
                    "Yuuna looks just as confused as Mayu and Kaori."
                    show valerie mis
                    voice "audio/voice/E3/D7/S2/valerie/E3D7L7.ogg"
                    vb "They mean your tits, Yuuna."
                    show mayu neu
                    show heart:
                        xoffset 1050
                        yoffset 125
                        xzoom .5
                        yzoom .5
                    show valerie hap
                    show yuuna cur b1
                    voice "audio/voice/E3/D7/S2/valerie/E3D7L8.ogg"
                    vb "They're huge!"
                    show shoBlush:
                        xoffset 1350
                        yoffset 100
                        xzoom .5
                        yzoom .5
                    show yuuna sur b2
                    "Yuuna is utterly mortified. She throws both arms around herself, blushing deeply."
                    show yuuna ann b2
                    voice "audio/voice/E3/D7/S2/yuuna/18.ogg"
                    ym "You guys are the worst!"
                    show mayu dis
                    show shou neu
                    show valerie smi
                    show yuuna sad b1
                    "Valerie laughs while Kaori and Mayu comfort Yuuna, shooting us disapproving glares."
                    "Shou and I look at each other."
                    pf "I thought women appreciated honesty?"
                    show drop:
                        xoffset 315
                        yoffset 20
                        xzoom .5
                        yzoom .5
                    show shou thi
                    voice "audio/voice/E3/D7/S2/shou/21.ogg"
                    ss "That's what I thought too..."
                    jump E3D7S2_ConvinceFailed
    
        "Pick Mayu!":
            pf "Mayu can do it!"
            show mayu sur b1
            show yuuna ner
            "Mayu's eyes widen in horror."
            show shocked:
                xoffset 30
                yoffset 135
                xzoom .5
                yzoom .5
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-12.ogg"
            ma "No!"
            show mayu sad b1
            "She turns her back to us."
            show shou cur
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-13.ogg"
            ma "I won't do it! It's too embarrassing."
            show valerie hap
            "Valerie giggles."
            show heart:
                xoffset 1050
                yoffset 125
                xzoom .5
                yzoom .5
            voice "audio/voice/E3/D7/S2/valerie/E3D7L9.ogg"
            vb "Aww! She's adorable when she's all shy."
            show kaori dis
            voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_12.ogg"
            ki "Leave her alone."
            show shou ske
            voice "audio/voice/E3/D7/S2/shou/22.ogg"
            ss "I don't get what the big deal is. We've already seen you in a bikini before..."
            show mayu wor b2
            "Mayu's blush brightens."
            show kaori dis
            show shou neu
            show valerie smi
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-14.ogg"
            ma "It's not the same!"
            show mayu win b2
            show yuuna smi
            "She wraps her arms tightly around herself, on the verge of tears. Yuuna and Kaori hover over her protectively."
            show mayu sad b1
            voice "audio/voice/E3/D7/S2/yuuna/19.ogg"
            ym "It's okay, you don't have to do it."
            jump E3D7S2_ConvinceFailed
    
        "Valerie, of course!":
            $ E3D7S2_ValVolunteer = 1
            "The choice is obvious."
    
            label E3D7S2_ConvinceFailed:
                
                hide valerie with dissolve
                
                if E3D7S2_ValVolunteer == 0:
                    "Well that didn't work out."
                    show kaori neu
                    show mayu neu
                    show yuuna neu
                    "Who would actually be willing to do it though? I think I know..."
        
                pf "How about Valerie--"
                $ valOut = "sSwimsuit"
                "Wait, where'd she go?"
                show shou ske
                "Everyone notices the lack of blonde hair spunkiness beside us. I look around and spot her already on the stage, pulling her clothes off!"
                # show valerie again
                show valerie smi at r1:
                    xoffset 50
                    xzoom 0.75
                    yzoom 0.75
                show mayu sur
                show shou sur
                show yuuna sur
                with dissolve
                voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-15.ogg"
                ma "V-Valerie!"
                show note:
                    xoffset 1050
                    yoffset 125
                    xzoom .5
                    yzoom .5
                show valerie mis
                "Valerie cocks her head to the side, sporting an alluring bikini."
                show kaori ske
                show mayu cur
                show shou neu
                show yuuna ner
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_13.ogg"
                ki "Why... Why were you wearing that underneath your clothes?"
                voice "audio/voice/E3/D7/S2/valerie/E3D7L10.ogg"
                vb "It's a photoshoot. Aren't you all wearing yours?"
                show kaori dis
                "Kaori clenches her fist."
                show kaori ann
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_14.ogg"
                ki "Of course not! What sort of dumb logic is that?"
                show valerie hap
                "Valerie grins impishly."
                show mayu neu
                voice "audio/voice/E3/D7/S2/valerie/E3D7L11.ogg"
                vb "Ohhh, even better!"
                show kaori ske
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_15.ogg"
                ki "Huh?"
                show valerie mis
                voice "audio/voice/E3/D7/S2/valerie/E3D7L12.ogg"
                vb "You're wearing something {i}nice{/i} and {i}private{/i} underneath aren't you, Kaori?"
                show question:
                    xoffset 575
                    yoffset 110
                    xzoom .5
                    yzoom .5
                show kaori ske b1
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_16.ogg"
                ki "W-What?!"
                show heart:
                    xoffset 1050
                    yoffset 125
                    xzoom .5
                    yzoom .5
                voice "audio/voice/E3/D7/S2/valerie/E3D7L13.ogg"
                vb "Is it black? Maybe lacey~"
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_17.ogg"
                ki "Ah!"
                show kaori sur b2 with dissolve
                "Kaori's face turns red."
                show tsuBlush:
                    xoffset 575
                    yoffset 110
                    xzoom .5
                    yzoom .5
                show kaori thi b2
                voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_18.ogg"
                ki "S-Stop being a pervert!"
                show valerie hap
                "Valerie laughs. Shou nudges me."
                show kaori dis b1
                show shou mis
                voice "audio/voice/E3/D7/S2/shou/23.ogg"
                ss "Heh, that's the first time she called someone other than us a pervert."
                pf "It was only a matter of time."
                show valerie smi
                show kaori neu
                jump E3D7S2_ValModeling
    
        "SHOU.":
            pf "I vote Shou."
            show kaori smi
            show shou ske
            voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_19.ogg"
            ki "Agreed."
            show yuuna smi
            voice "audio/voice/E3/D7/S2/yuuna/20.ogg"
            ym "Yes."
            show valerie hap
            voice "audio/voice/E3/D7/S2/valerie/E3D7L14.ogg"
            vb "Of course."
            show mayu smi
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-16.ogg"
            ma "Mhm."
            show shocked:
                xoffset 315
                yoffset 20
                xzoom .5
                yzoom .5
            show shou sur
            "No one misses a beat. Shou looks shocked."
            voice "audio/voice/E3/D7/S2/shou/24.ogg"
            ss "Ye- Wha! Are you guys serious? Why are you all agreeing so quickly?"
            show shou ske
            "Yuuna flags down the photographer."
            show valerie smi
            show yuuna hap
            voice "audio/voice/E3/D7/S2/yuuna/21.ogg"
            ym "We've made a decision!"
            show shou ner
            voice "audio/voice/E3/D7/S2/shou/25.ogg"
            ss "Don't assume I'm just gonna do it!"
            # sfx
            show kaori dis
            # shou shake?
            "Kaori gives Shou a good knocking."
            show shou wor
            show yuuna smi
            ss "Aghh! What was that for?"
            show kaori ann
            voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_20.ogg"
            ki "You were obviously hoping one of us would do it instead. Pervert!"
            show shou sad
            "Shou frowns but doesn't deny it."
            show crying:
                xoffset 315
                yoffset 20
                xzoom .5
                yzoom .5
            voice "audio/voice/E3/D7/S2/shou/27.ogg"
            ss "Broseph... how could you do this to me?"
            pf "It was either you or me, bruh."
            "The photographer gives Shou a onceover."
            voice "audio/voice/E3/D7/S2/photo1/10.ogg"
            photo1 "Really? Him?"
            show shou ske
            voice "audio/voice/E3/D7/S2/shou/28.ogg"
            ss "HEY! What's that suppose to mean?"
            "He forms his fingers into a box to frame Shou's face."
            voice "audio/voice/E3/D7/S2/photo1/11.ogg"
            photo1 "Hm… I can see the campaign… \"Even if you look like this, there is still hope with Dasshu by your side!\""
            voice "audio/voice/E3/D7/S2/photo1/12.ogg"
            photo1 "I like it!"
            show shou dis
            voice "audio/voice/E3/D7/S2/shou/29.ogg"
            ss "I resent that."
            voice "audio/voice/E3/D7/S2/photo1/13.ogg"
            photo1 "Come on!"
            hide shou with dissolve
            "He whisks Shou into the changing room."
            voice "audio/voice/E3/D7/S2/shou/30.ogg"
            ss "I will get my vengeance!"
            voice "audio/voice/E3/D7/S2/shou/31.ogg"
            ss "In this life, or the next..."
            "His voice fades away into the distance."
            "That turned out better than I could have hoped for!"
            "Once in front of the camera, Shou is surprisingly impressive."
            show mayu hap
            voice "audio/voice/E3/D7/S2/mayu/Mayu Day 7-17.ogg"
            ma "He's doing a great job!"
            show kaori cur
            show yuuna hap
            voice "audio/voice/E3/D7/S2/kaori/e3d7_Kaori_21.ogg"
            ki "Y-Yeah..."
            show valerie hap
            voice "audio/voice/E3/D7/S2/valerie/E3D7L15.ogg"
            vb "I knew he had it in him!"
            show kaori smi
            show mayu smi
            "We all cheer him on. Some other women in the crowd hear our cries and watch Shou with interest, which only encourages him. At this rate, his photos will turn out better than ever!"
            show yuuna smi
            show valerie smi
            "Afterwards, he changes back into his regular clothes and rejoins us."
            # show shou again
            show shou smi at l2 with dissolve:
                xoffset -50
                xzoom 0.75
                yzoom 0.75
            voice "audio/voice/E3/D7/S2/shou/32.ogg"
            ss "Woo! That went better than expected."
    
        "We will not be objectified!":
            pf "We should refuse to do this!"
            hide valerie with dissolve
            pf "To be forced into a swimsuit is sexual objectification! We must be firm in our response and let the establishment know that we do not encourage their sexist agenda! No one should be subjected to the whims of another person--"
            "From the corner of my eye, I spot Valerie already on the stage, taking her clothes off! As her clothes fall away, she reveals an alluring bikini."
            show shou cur
            pf "Valerie!"
            $ valOut = "sSwimsuit"
            pf "What are you doing?"
            # show valerie again
            show valerie smi at r1 with dissolve:
                xoffset 50
                xzoom 0.75
                yzoom 0.75
            voice "audio/voice/E3/D7/S2/valerie/E3D7L16.ogg"
            vb "Isn't it obvious?"
            pf "Did you hear anything that I just said?"
            show valerie mis
            voice "audio/voice/E3/D7/S2/valerie/E3D7L17.ogg"
            vb "Of course, and I agree with all of it. People should be able to choose what they want to do."
            show kaori ske
            show note:
                xoffset 1050
                yoffset 125
                xzoom .5
                yzoom .5
            show valerie hap
            voice "audio/voice/E3/D7/S2/valerie/E3D7L18.ogg"
            vb "Just like how I'm {i}choosing{/i} to model for Dasshu's summer catalog."
            hide valerie with dissolve
    
            label E3D7S2_ValModeling:
                hide valerie with dissolve
                $renpy.pause(.5)
                "She grabs the Dasshu energy drink beside her with one hand and forms a peace sign with the other. Then winks suggestively at the camera."
                voice "audio/voice/E3/D7/S2/photo1/14.ogg"
                photo1 "That is perfect! You're a natural!"
                show kaori neu b1
                show mayu neu b1
                show shou cur b1
                show yuuna cur b1
                "We watch Valerie expertly transition between poses as the photographer snaps image after image. She's completely in her element!"
                "The girls are a little too focused on her. I can't tell if it's from admiration, jealousy, or a little bit of both."
                show mayu sur b1
                show kaori sur b1
                show yuuna sur b1
                with dissolve
                show shou sur b2 with dissolve
                "Valerie shakes the drink then pops open the bottle. The carbonated liquid explodes all over her face. She catches the liquid in her mouth, then wraps her lips around the bottle."
                "I... I can't look away."
                show yuuna ner b1
                voice "audio/voice/E3/D7/S2/yuuna/22.ogg"
                ym "T-That's enough!"
                hide yuuna with dissolve
                "Yuuna pulls Valerie off the stage and pushes her towards the changing room."
                hide valerie with dissolve
                voice "audio/voice/E3/D7/S2/valerie/E3D7L19.ogg"
                vb "H-Hey!"
                show mayu cur b1
                show kaori cur b1
                show shou cur b1
                with dissolve
                voice "audio/voice/E3/D7/S2/photo1/15.ogg"
                photo1 "You ruined my shoot!"
                voice "audio/voice/E3/D7/S2/yuuna/23.ogg"
                ym "You've got plenty to use already."
                "Yuuna is uncharacteristically firm, and the photographer is taken aback by her directness."
                voice "audio/voice/E3/D7/S2/photo1/16.ogg"
                photo1 "Uh, yeah, okay."
                voice "audio/voice/E3/D7/S2/yuuna/24.ogg"
                ym "Great!"
                "She shoves Valerie into the changing room."
                voice "audio/voice/E3/D7/S2/valerie/E3D7L20.ogg"
                vb "Ah!"
        
                "My heart feels like it's about to beat out of my chest. Shou's face is frozen in awe."
                show dots:
                    xoffset 575
                    yoffset 110
                    xzoom .5
                    yzoom .5
                show kaori neu b2
                show mayu ner b1
                "Kaori is uncharacteristically quiet and her face is as red as a tomato. Mayu is pensive, as if she's trying to analyse what she just witnessed. Yuuna's cheeks are just as red as Kaori's."
                voice "audio/voice/E3/D7/S2/yuuna/25.ogg"
                ym "Um, that was..."
                show shou smi b1
                "We nod. There are no words to describe what we just saw."
                show kaori neu b1
                show mayu neu
                voice "audio/voice/E3/D7/S2/valerie/E3D7L21.ogg"
                vb "That was a lot of fun!"
                $ valOut = "sDate"
                # show yuuna and valerie again
                show valerie smi at r1:
                    xoffset 50
                    xzoom 0.75
                    yzoom 0.75
                show yuuna neu at r3:
                    xoffset 50
                    xzoom -0.75
                    yzoom 0.75
                with dissolve
                "Valerie returns in her previous outfit and a towel wrapped around her neck. She's completely unphased by what just happened."
                show kaori smi
                show shou hap
                "A laugh escapes me as I consider how ridiculous this situation is. Soon, the entire team is laughing with me."
                
    label E3D7S2_PhotoComplete:
        voice "audio/voice/E3/D7/S2/photo1/17.ogg"
        photo1 "Thank you very much! We have everything we need."
        show yuuna smi
        voice "audio/voice/E3/D7/S2/yuuna/27.ogg"
        ym "You're welcome."
        stop music fadeout 5
        scene black with fade
        "We exit out of the photo area and back into the main lounge."
        
        jump E3D7S3
    