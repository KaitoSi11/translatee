#
label E4D3S3:
    
    stop music fadeout 7
    "As soon as we enter the simulation, Ivan sets us up to spar with AI GEARs. Once the match is over, he points out where we lost focus or how we could have prevented getting hit. Then gives us suggestions on how to tighten up as a unit."
    "Once he's shared his insight, he sends us back in for another round."
    "While we fight the AIs, Ivan and Valerie talk quietly about simple fixes to our GEARs. He seems pleased by what Valerie shares with him--I assume she mentioned the original tweaks she added to our GEARs when she first joined the team."
    "The more Valerie talks, the more animated Ivan becomes."
    "Yuuna watches everyone closely and jots down notes in her tablet. I have a feeling she's recording feedback on our session with Coach Ivan as well as recording feedback from our simulated matches."
    "Based on just the brief notes Ivan provided on our first match, our second match felt worlds apart from the first. It's quite apparent why he won 2 MVP awards. He truly lives up to his title of \"Strong Arm Gear\"!"
    "...So long as you can decipher what he says."
    
    #Fade back into scene
    scene bg campus battleroom day with fade
    show yuuna smi at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu smi at l2 behind yuuna with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show shou smi at l1 with dissolve:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    show kaori smi at r1 with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    show valerie smi at r2 with dissolve:
        xoffset 50
        yoffset 35
        xzoom 0.75
        yzoom 0.75
    show ivan neu at r3 with dissolve:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
        
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    
    "We exit the simulator feeling satisfied and more confident than before. Ivan greets us by the holotable."
    voice "audio/voice/E4/Ivan Poddubny/15.ogg"
    ip "AND SO THE DIAL OF TIME LANDS FOR MY DEPARTURE."
    voice "audio/voice/E4/Shou/d3/12 Copy.ogg"
    ss "Thank you so much Mr. P--"
    show shou wor
    show dots:
        xoffset 1575
        yoffset 5
        xzoom .5
        yzoom .5
    show ivan ann
    "His icy gaze falls on Shou."
    show drop:
        xoffset 600
        yoffset 20
        xzoom .5
        yzoom .5
    show shou hap
    voice "audio/voice/E4/Shou/d3/13 Copy.ogg"
    voice "audio/voice/E4/Shou/d3/13 Copy.ogg"
    ss "Haha, I mean thanks Ivan."
    show ivan smi
    "Ivan smiles."
    voice "audio/voice/E4/Mayu/D3/Mayu D3-08.ogg"
    ma "We appreciate your time."
    show valerie hap
    voice "audio/voice/MISSING/BATCH4/Valerie/ValE4Redos/ValE4Redo3.ogg"
    vb "And all this data analysis will help me fine-tune the GEARs to give them that extra boost!"
    show kaori hap
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_10.ogg"
    ki "We can't lose after a training session like that!"
    show ivan sad
    "Ivan begins to sniffle."
    show yuuna ner
    voice "audio/voice/E4/Yuuna/E4/D3/5.ogg"
    ym "...Is something wrong?"
    show ivan win
    show kaori cur
    show mayu cur
    "He rubs his eyes with his forearm."
    show shou cur
    show valerie cur
    voice "audio/voice/E4/Ivan Poddubny/16.ogg"
    ip "YOU GUYS--"
    show kaori sur
    show mayu wor
    show yuuna sur
    # bounce ivan?
    "Suddenly Ivan scoops all of us into a group hug!"
    show exclamation:
        xoffset 1575
        yoffset 5
        xzoom .5
        yzoom .5
    show ivan hap b3
    show valerie sur
    show shou wor
    voice "audio/voice/E4/Ivan Poddubny/17.ogg"
    ip "--MAKE ME SO PROUD!"
    "He squeezes us so tightly I gasp for air. Shou mouths \"help me\" while trying to wriggle free.  Mayu looks terrified as she's squished into Yuuna's chest."
    
    if yuurelatonship == 1:
        "I frown, but quickly keep myself in check. I wish Mayu and I could switch places, but was I really about to get jealous of {i}Mayu{/i}?"
        
    "Valerie tries to hug Ivan's arm while Kaori looks like a deer in headlights and struggles to break free. {w}Ivan doesn't notice."
    show panic:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori wor
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_11.ogg"
    ki "H-Hey!"
    show ivan smi
    show kaori neu
    show valerie neu
    "After one last squeeze, he releases us and lets out a deep sigh."
    show shou neu
    show mayu neu
    show yuuna neu
    voice "audio/voice/E4/Ivan Poddubny/18.ogg"
    ip "AND SO THE NEST PERCHED ON THE BRANCH FINDS ITS AWAKENING. GO FORTH HATCHLINGS."
    
    hide ivan with dissolve
    
    $ ivaHelmet = "1"
    $ ivaOut = "default"
    
    show ivan neu at r3 with dissolve:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
        
    "His helmet magically materializes in his hand. He puts it on and zips up his jacket. Then offers us a final thumbs up."
    show kaori smi
    show shou smi
    show mayu smi
    show yuuna smi
    show valerie smi
    with dissolve
    hide ivan with dissolve
    "We wave goodbye as he heads out, calling out our thanks to his retreating form."
    show shou hap
    voice "audio/voice/E4/Shou/d3/14 Copy.ogg"
    ss "Man I am so pumped for our match tomorrow!"
    show exclamation:
        xoffset 350
        yoffset 135
        xzoom .5
        yzoom .5
    show mayu hap
    voice "audio/voice/E4/Mayu/D3/Mayu D3-09.ogg"
    ma "Me too!"
    show mayu smi
    voice "audio/voice/E4/Mayu/D3/Mayu D3-10.ogg"
    ma "Should we get some more practice in while we can?"
    show kaori neu
    "Kaori shakes her head."
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_12.ogg"
    ki "I think Valerie needs to make the recommended calibrations first."
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L8.ogg"
    vb "Yup. They aren't major control changes or anything so you won't feel a difference while piloting. You'll just get better energy efficiency based on piloting patterns Ivan pointed out."
    show kaori smi
    "Kaori nods."
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_13.ogg"
    ki "That's exactly what we need."
    show shou neu
    voice "audio/voice/E4/Shou/d3/15 Copy.ogg"
    ss "Aw, okay. So what do we do until then?"
    show mayu thi
    voice "audio/voice/E4/Mayu/D3/Mayu D3-11.ogg"
    ma "It is reading week..."
    show frightful:
        xoffset 600
        yoffset 20
        xzoom .5
        yzoom .5
    show shou wor
    voice "audio/voice/E4/Shou/d3/16 Copy.ogg"
    ss "No, Mayu. Don't say it! NO! NOOOOOOOOOOOO--"
    show kaori win
    "Kaori covers her ears."
    show vein:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori ang
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_14.ogg"
    ki "Idiot! What's wrong with you?"
    show kaori ann
    voice "audio/voice/E4/Shou/d3/17 Copy.ogg"
    ss "Anything but that!"
    show mayu ske
    voice "audio/voice/E4/Mayu/D3/Mayu D3-12.ogg"
    ma "Shou..."
    
    if mayrelatonship == 1:
        show mayu neu
        "Mayu sighs, then glances my way as if seeking approval."
        voice "audio/voice/E4/Mayu/D3/Mayu D3-13.ogg"
        ma "He won't focus if someone doesn't keep him on track."
        
        menu:
            "Sure thing!":
                pf "Yeah, of course. Make sure you keep the slacker in line."
            
            "You won't take care of me?":
                pf "What about me?"
                show mayu hap
                voice "audio/voice/E4/Mayu/D3/Mayu D3-14.ogg"
                ma "Don't worry! We can do it later tonight."
                "A dusting of pink stains my cheeks. Judging by Kaori's blush and Yuuna and Valerie's impish smile, I'm not the only one who heard it like that."
                show mayu cur b1
                "Mayu blinks at us, then her cheeks flush when she realises what that sounded like."
                show shoBlush:
                    xoffset 450
                    yoffset 135
                    xzoom .5
                    yzoom .5
                show mayu wor b2
                voice "audio/voice/E4/Mayu/D3/Mayu D3-15.ogg"
                ma "S-Study session! That's all I m-meant!"
                pf "R-Right, that's fine!"
                "I can't help but feel a little disappointed even though I know that's what she meant."
                
        show mayu smi b1
        show shou sad
        "Shou sighs."
        show storm:
            xoffset 600
            yoffset 20
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Shou/d3/18 Copy.ogg"
        ss "I guess I don't have a choice in the matter."
        
    else:
        show mayu smi b1
        "Mayu interlocks her arm with Shou's."
        voice "audio/voice/E4/Mayu/D3/Mayu D3-16.ogg"
        ma "It won't be that bad, I promise."
        show shou cur b1
        "Shou glances at Mayu's smile then his own face lights up."
        show note:
            xoffset 600
            yoffset 20
            xzoom .5
            yzoom .5
        show shou hap b1
        voice "audio/voice/E4/Shou/d3/19 Copy.ogg"
        ss "O-Okay!"
        show shou smi b1
        voice "audio/voice/E4/Shou/d3/20 Copy.ogg"
        ss "We'll talk to you guys later."
        
    hide mayu
    hide shou
    with dissolve
    "Mayu smiles and the two of them are off."
    show kaori mis
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_15.ogg"
    ki "You're all good then, Valerie?"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L9.ogg"
    vb "Yup! I'll send a text when I'm done."
    show kaori smi
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_16.ogg"
    ki "Okay, thank you. I'd better get studying too."
    
    if kaorelatonship == 1:
        "Kaori locks eyes with me."
        voice "audio/voice/E4/Kaori/D3/Kaori_D3_17.ogg"
        ki "I'll see you later."
        "It sounds like less of a suggestion and more of a statement. My cheeks turn pink."
        
    hide kaori with dissolve
    "I nod and watch her head off."
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D3/6.ogg"
    ym "Well, since I'm already on campus, I'll go submit my report on the coaching session."
    
    if yuurelatonship == 1:
        "I'm a little disappointed that we can't hang out. She notices my expression."
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/D3/7.ogg"
        ym "If I finish early, I'll let you know!"
        pf "Alright."
        show heart:
            xoffset 5
            yoffset 100
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Yuuna/E4/D3/8.ogg"
        ym "I'll see you later!"
        
    hide yuuna with dissolve
    "I wave goodbye."
    
    if valrelatonship == 1:
        pf "And then there were two."
        show valerie mis
        "Valerie giggles."
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L10.ogg"
        vb "You mean and then there was one. As much as I enjoy your company, you are too distracting for me when you're around and I won't be able to get any work done."
        "I'm about to reply with a witty retort when Valerie cuts me off."
        show heart:
            xoffset 1275
            yoffset 125
            xzoom .5
            yzoom .5
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L11.ogg"
        vb "Distance makes the heart grow fonder. Out you go!"
        "She basically pushes me out of the pre-combat room."
        pf "Geez!"
    
    else:
        pf "Do you want some company?"
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L12.ogg"
        vb "No, it's okay. I'll be doing some boring stuff anyway and I'm not a fan of over the shoulder spectators."
        "I nod."
        pf "Alright. Let me know if you need anything."
        show note:
            xoffset 1275
            yoffset 125
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L13.ogg"
        vb "Sure!"
        
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus library day with fade
    "With some time on my hands, I head to the library to actually squeeze in a study session."
    "The library is packed, which I guess makes sense since exams are right around the corner. {w}After circling the desks a couple of times, I manage to sneak into a desk stall just as another student is leaving. I feel like a car trying to find a parking space in a crowded lot."
    scene black with fade
    $renpy.pause(1)
    "A few hours go by in a blur. Valerie texts at one point saying the changes are done, but otherwise nothing eventful happens."
    $renpy.pause(1)
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    scene bg campus library day with fade
    "That's all the studying I can do in one sitting! I pack up my tablet and wonder if anyone's available..."
    
    #Evening
    $ freeTime = "evening"
    
    call E4FreeTime from _call_E4FreeTime
    
    stop ambient fadeout 3
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    
    jump E4D3S4

