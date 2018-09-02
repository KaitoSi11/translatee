#
label E2D4S2:
    
    $ kaoOut = "sUniform"
    $ kaoHairF = renpy.random.choice(['default'])
    $ kaoHairB = kaoHairF
    $ mayOut = "sUniform"
    $ shoOut = "sUniform"
    
    
    #end choice
    
    "I'm in the campus gym finishing up my workout."
    scene black with fade
    "When I return to my locker, there's a missed text from Kaori."
    
    "{i}{b}EMERGENCY MEETING!{/b} Meet now in the hangar{/i}"
    "Geez, all caps… {w}I'd better get going."
    stop music fadeout 5
    scene black with fade
    #bg
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    scene bg campus hangar day with fade
    show kaori ann at r3 with dissolve:
        xzoom -1
    show mayu neu at l3
    show shou neu at cc
    with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    "I arrive at the hangar about the same time as Shou and Mayu. Kaori waits impatiently in front of her GEAR."
    voice "audio/voice/E2/D4/S2/Kaori/1.ogg"
    ki "Finally! That took you a while."
    
    menu:
        "I just saw your text.":
            pf "I literally came here as soon as I got your text."
            show kaori dis at r3
            voice "audio/voice/E2/D4/S2/Kaori/2.ogg"
            ki "I texted before heading over here so we'd be on time."
            pf "I guess you walk faster than me."
    
            if E1D5S1_EventKaori == 1:
                show kaori mis at r3
                show note:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/D4/S2/Kaori/3.ogg"
                ki "Well, at least you know what you can improve on."
                "I think I see a smirk. Is that Kaori's version of a joke?"
    
        "I might have gotten a little distracted.":
            pf "I came as soon as I got your text. But I had to cross the quad on the way over here and I guess the track team is practicing because there were a bunch of girls jogging…"
            show shou cur at cc
            show exclamation:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Shou looks intrigued."
            show mayu cur at l3
            show shou mis at cc
            voice "audio/voice/E2/D4/Shou/1.ogg"
            ss "Tell me more about these joggers."
            show kaori ang at r3
            show vein:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D4/S2/Kaori/4.ogg"
            ki "No!"
            show kaori ann at r3
            show mayu wor at l3
            show shou wor at cc
            show frightful:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D4/Shou/2.ogg"
            ss "Hey! Why are you mad at me? He's the one who was watching them!"
            pf "Let's not dwell on the past. What's important is that I'm here now, right?"
            show kaori ske at r3
            show mayu neu at l3
            show shou neu at cc
            "She raises an eyebrow."
    
        "What are you talking about? I'm on time.":
            pf "I'm not late."
            show kaori dis at r3
            voice "audio/voice/E2/D4/S2/Kaori/5.ogg"
            ki "I've been waiting here at least 10 minutes."
            pf "Congratulations."
            show storm:
                xoffset 1175
                yoffset 110
                xzoom .75
                yzoom .75
            "She crosses her arms."
    
    "Kaori addresses the rest of the team."
    show kaori ske at r3
    voice "audio/voice/E2/D4/S2/Kaori/6.ogg"
    ki "What about you guys?"
    show drop:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner at l3
    show shou thi at cc
    voice "audio/voice/E2/D4/S2/Mayu/0-01.ogg"
    ma "Sorry, we were having lunch and I guess we lost track of time."
    show kaori cur at r3
    show question:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    "Kaori blinks, then waves her hand dismissively."
    show kaori neu at r3
    voice "audio/voice/E2/D4/S2/Kaori/7.ogg"
    ki "Nevermind. We have more important things to discuss--like our sponsor situation."
    show mayu neu at l3
    show shou neu at cc
    "Everyone becomes serious."
    voice "audio/voice/E2/D4/S2/Kaori/8.ogg"
    ki "Our GEARs need a lot of maintenance to return to peak fighting condition, and the next round is tomorrow."
    show kaori thi at r3
    show storm:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D4/S2/Kaori/9.ogg"
    ki "I don't know why, but everyone I talked to was really rude and unhelpful."
    show shou cur at cc
    "Shou and I share a knowing glance, and Kaori catches us."
    show kaori ske at r3
    voice "audio/voice/E2/D4/S2/Kaori/10.ogg"
    ki "What?"
    show shou hap at cc
    voice "audio/voice/E2/D4/Shou/3.ogg"
    ss "Nothing, nothing…"
    show kaori neu at r3
    "She continues to stare."
    show shou smi at cc
    voice "audio/voice/E2/D4/Shou/4.ogg"
    ss "It's just sometimes you can come across a little harsh."
    show kaori dis at r3
    voice "audio/voice/E2/D4/S2/Kaori/11.ogg"
    ki "I'm just honest."
    show shou mis at cc
    voice "audio/voice/E2/D4/Shou/5.ogg"
    ss "Sure, but honesty doesn't make people like you. You need to get in touch with your soft, warm, feminine side."
    show kaori ske at r3
    "Kaori raises an eyebrow."
    voice "audio/voice/E2/D4/S2/Kaori/12.ogg"
    ki "Is that what you do?"
    show shou smi at cc
    voice "audio/voice/E2/D4/Shou/6.ogg"
    ss "Yes!"
    #face change
    show shou thi at cc
    show drop:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D4/Shou/7.ogg"
    ss "I mean to the warm thing, not the soft and feminine thing."
    show dots:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori neu at r3
    show dots2:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "We stare at him blankly."
    show shou neu at cc
    voice "audio/voice/E2/D4/Shou/8.ogg"
    ss "I'm just going to shut up now."
    voice "audio/voice/E2/D4/S2/Kaori/13.ogg"
    ki "Before you do, did you manage to get a sponsor?"
    show shou hap at cc
    "He folds his hands behind his head and leans into them."
    voice "audio/voice/E2/D4/Shou/9.ogg"
    ss "Nope."
    show kaori dis at r3
    voice "audio/voice/E2/D4/S2/Kaori/14.ogg"
    ki "... You forgot to ask around, didn't you?"
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D4/Shou/10.ogg"
    ss "Maybe."
    show kaori thi at r3
    "He looks sheepish. {w}Kaori rolls her eyes."
    show kaori ske at r3
    show mayu cur at l3
    voice "audio/voice/E2/D4/S2/Kaori/15.ogg"
    ki "What about you, Mayu? Can your father sponsor us?"
    show mayu ner at l3
    show shou smi at cc
    "Mayu shakes her head."
    show kaori neu at r3
    show mayu sad at l3
    voice "audio/voice/E2/D4/S2/Mayu/0-02.ogg"
    ma "Unfortunately, he's backing the team I was originally supposed to join. When I was invited onto the team, Father was so happy he promised he'd sponsor them."
    show mayu neu at l3
    show shou smi at cc
    voice "audio/voice/E2/D4/S2/Mayu/0-03.ogg"
    ma "Even though I never joined them, he can't go back on his promise."
    "Kaori nods, then faces me."
    voice "audio/voice/E2/D4/S2/Kaori/16.ogg"
    ki "You had that interview yesterday, didn't you?"
    pf "Yeah, I went to the interview with Warptech. It didn't work out..."
    show kaori dis at r3
    voice "audio/voice/E2/D4/S2/Kaori/17.ogg"
    ki "Why am I not surprised?"
    
    if E2D3S2_Score >= 7:
        pf "It had less to do with me and more to do with our team status."
    
    else:
        pf "I'd like to have seen you do better, miss \"I-couldn't-get-a-sponsor-either\"."
        show kaori thi at r3
        "Kaori just crosses her arms."
        voice "audio/voice/E2/D4/S2/Kaori/18.ogg"
        ki "Well, what happened?"
    
    pf "I can show you the full report from the SBA if you want to know the official reason, but basically we weren't a high enough rank."
    "I fish my phone out of my pocket. It flashes \"low battery\" warnings at me before it dies completely."
    show kaori neu at r3
    voice "audio/voice/E2/D4/S2/Kaori/19.ogg"
    ki "Where's the report?"
    pf "Uh, hold on… I have to charge my phone…"
    stop music fadeout 5
    scene black with fade
    "My gaze lands on my GEAR. I race to it and head into the cockpit. My teammates call after me, but I ignore them.{w} Once I plug my phone into the dock connection, it lights up with the charging symbol."
    scene bg campus hangar day with fade
    show kaori ske at r3 with dissolve:
        xzoom -1
    show mayu ske at l3
    show shou ske at cc
    with dissolve
    "Everyone's wearing confused faces when I climb out of the cockpit."
    pf "What?"
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
    show mayu thi at l3
    voice "audio/voice/E2/D4/S2/Mayu/0-04.ogg"
    ma "Why didn't you just use an outlet?"
    show mayu neu at l3
    "Mayu points to an outlet on the wall."
    
    menu:
        "When did those get here?!":
            pf "Huh… that's new."
            show kaori dis at r3
            voice "audio/voice/E2/D4/S2/Kaori/20.ogg"
            ki "No, they're not."
            pf "I've never noticed them before."
            show shou neu at cc
            voice "audio/voice/E2/D4/Shou/11.ogg"
            ss "What about those? And those?"
            "Shou points to another outlet. In fact, there are outlets everywhere."
            pf "Nope, never seen them before either."
    
        "You mean this isn't what GEARs are for?":
            pf "Are you saying you've never charged your phone in your GEAR?"
            show kaori neu at r3
            show mayu thi at l3
            show shou neu at cc
            with dissolve
            "All three of them shake their head."
            pf "Why not?"
            show kaori ske at r3
            show mayu neu at l3
            voice "audio/voice/E2/D4/S2/Kaori/21.ogg"
            ki "Because it's stupid. Why would I climb all the way up there when there's a perfectly good outlet down here?"
            pf "That's the beauty of it. Not only does your phone charge faster, you get a little bit of a workout too. Win-win!"
            show mayu ske at l3
            show shou ske at cc
            "They stare at me unconvinced."
    
        "Who cares if I use an outlet or my GEAR.":
            pf "Because I can."
            show kaori dis at r3
            voice "audio/voice/E2/D4/S2/Kaori/22.ogg"
            ki "That's stupid."
            pf "I made my choice and I'm standing by it."
    
    pf "Besides, an outlet doesn't do me any good if I don't have a phone charger with me."
    stop music fadeout 5
    show mayu cur at l3
    show shou neu at cc
    voice "audio/voice/E2/D4/S2/Mayu/0-05.ogg"
    ma "Oh… I suppose that makes sense…"
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
    show kaori neu at r3
    show mayu neu at l3
    voice "audio/voice/E2/D4/S2/Kaori/23.ogg"
    ki "Anyway, I guess we're back to square one."
    show shou mis at cc
    voice "audio/voice/E2/D4/Shou/12.ogg"
    ss "Back? We never left square one."
    pf "Don't give up hope just yet. I might have something."
    show kaori cur at r3
    show shou neu at cc
    voice "audio/voice/E2/D4/S2/Kaori/24.ogg"
    ki "Another meeting?"
    pf "No, but my friend in the SBA is still helping us search."
    show kaori neu at r3
    voice "audio/voice/E2/D4/S2/Kaori/25.ogg"
    ki "Okay. In the meantime, the rest of us should continue our search too."
    show kaori thi at r3
    voice "audio/voice/E2/D4/S2/Kaori/26.ogg"
    ki "I'll take another look at what ACE offers. Maybe there's some kind of campus grant or funding we can apply for."
    show kaori neu at r3
    show mayu cur at l3
    voice "audio/voice/E2/D4/S2/Kaori/27.ogg"
    ki "Mayu, do you think you could reach out to some of the other major corporations we haven't talked to yet?"
    show kaori smi at r3
    voice "audio/voice/E2/D4/S2/Kaori/28.ogg"
    ki "Maybe with your background you'll have more luck than we would…"
    show mayu smi at l3
    "Mayu nods."
    show mayu hap at l3
    show bulb:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D4/S2/Mayu/0-06.ogg"
    ma "Maybe Shou can ask around local businesses?"
    show shou smi at cc
    voice "audio/voice/E2/D4/Shou/13.ogg"
    ss "Okay!"
    show mayu smi at l3
    voice "audio/voice/E2/D4/S2/Kaori/29.ogg"
    ki "Good idea."
    show kaori neu at r3
    "Kaori looks at me."
    pf "I'll follow up with my contact."
    "She nods."
    voice "audio/voice/E2/D4/S2/Kaori/30.ogg"
    ki "Hopefully we'll find someone, but there's a chance we might have to fight with our GEARs as is."
    pf "I'm confident we'll get someone in time."
    show mayu hap at l3
    "Mayu smiles at me and nods."
    show shou hap at cc
    "Shou claps me on the back."
    show kaori mis at r3
    show mayu smi at l3
    voice "audio/voice/E2/D4/S2/Kaori/31.ogg"
    ki "Okay. We have our plan. Text if you guys get any leads."
    "We all nod."
    show kaori neu at r3
    show shou smi at cc
    voice "audio/voice/E2/D4/Shou/14.ogg"
    ss "I'm off then. I've got some stuff to take care of."
    show mayu mis at l3
    voice "audio/voice/E2/D4/S2/Mayu/0-07.ogg"
    ma "I hope you mean reaching out to the businesses, Shou, and not playing your video games."
    show shou mis at cc
    voice "audio/voice/E2/D4/Shou/15.ogg"
    ss "Of course that's what I meant. The arcade industry is a lucrative place to find a sponsor."
    show mayu thi at l3
    "Mayu sighs."
    voice "audio/voice/E2/D4/S2/Mayu/0-08.ogg"
    ma "Shou..."
    show shou hap at cc
    "He wears his signature smile."
    show mayu smi at l3
    voice "audio/voice/E2/D4/Shou/16.ogg"
    ss "Okay, okay… Let's go find us a sponsor!"
    show mayu hap at l3
    show note:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    "Mayu beams. The pair wave at us before heading out."
    hide mayu
    hide shou
    with dissolve
    show kaori neu at r3
    voice "audio/voice/E2/D4/S2/Kaori/32.ogg"
    ki "I'll be going too. Tell me if your friend is successful."
    hide kaori with dissolve
    "I nod, and Kaori leaves."
    stop music fadeout 3
    "Nothing left for me to do but go home."
    stop ambient fadeout 3
    scene black
    
    jump E2D4S3
    
