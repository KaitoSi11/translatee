#
label E2D6S1:
    
    $ nikHairF = renpy.random.choice([ 'pony'])
    $ nikHairB = nikHairF
    $ nikOut = renpy.random.choice(['sCasual2'])
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ day = 6
    $ timeSpent = "none"
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    
    "The sun shining through my window splashes on my face and wakes me up. I stretch in a wide yawn and glance at the clock. Nearly 10."
    "I'm glad I got a chance to sleep in after the party last night, but I don't want to waste my weekend. I hop out of bed and get ready for the day."

    "What's my plan for today?"
    
    
    menu:
        "I should thank Yuuna for all her help finding a sponsor." if E2YMS3_Completed == 1:
            $ E2D6S1_ChoseYuuna = 1
            jump E2YMS4
        
        "I wonder what my broseph is up to…" if E2SSS3_Completed == 1:
            $ E2D6S1_ChoseShou = 1
            jump E2SSS4
        
        "Valerie and I should get started on our class project." if E2VBS3_Completed == 1:
            $ E2D6S1_ChoseValerie = 1
            jump E2VBS4
        
        "Mayu owes me a violin lesson." if E2MAS3_Completed == 1:
            $ E2D6S1_ChoseMayu = 1
            jump E2MAS4
        
        "Maybe Kaori will show me how she made her delicious bento." if E2KIS3_Completed == 1:
            $ E2D6S1_ChoseKaori = 1
            jump E2KIS4
        
        "Just sleep in and skip my day." if E2KIS3_Completed == 0 and E2MAS3_Completed == 0 and E2VBS3_Completed == 0 and E2SSS3_Completed == 0 and E2YMS3_Completed == 0:
            "I want to do nothing productive with my time and just sleep in!"
            "But first, I must gorge myself on some delicious take-out food."
            "I call a nearby restaurant and place an order obscenely large for a single person to eat.{w} Pickup will be ready in 15 minutes!"
            $ E2D6S1_ChoseAlone = 1
            
    #((JUMP BACK FROM WEEKEND BEGINNING))
    label E2D6S1_Nikki:
        
        "After making my plans, I head downstairs."

        scene black with fade
        
        scene bg homekaito main day with fade
        
        show nikki cur at cc with dissolve
        voice "audio/voice/E2/D6/S2/Nikki/1.ogg"
        sf "Oh hey! Didn't see you there big bro!"
        show nikki neu at cc
        "She seems to be back to her usual self."
        pf "I'm glad to see you're feeling better."
        show nikki smi at cc
        voice "audio/voice/E2/D6/S2/Nikki/2.ogg"
        sf "Oh yeah, I definitely am."
        show note:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        "As she speaks, a devilish smile graces her lips."
        "Hm… She's up to something…"
        show nikki neu at cc
        voice "audio/voice/E2/D6/S2/Nikki/3.ogg"
        sf "Anyway, you going out today?"
        pf "Yeah, why?"
        show nikki mis at cc
        "She starts giggling."
        voice "audio/voice/E2/D6/S2/Nikki/4.ogg"
        sf "Mmmmmmmmm... no reason."
        show nikki neu at cc
        pf "Okay…"
        pf "Hey, I'm actually glad I ran into you. I want to apologise."
        show nikki ske at cc
        voice "audio/voice/E2/D6/S2/Nikki/5.ogg"
        sf "Apologise?"
        pf "Yeah, I saw your texts from a couple days ago and I'm sorry I didn't answer. I didn't have my phone on me so I didn't see them until too late."
        show nikki dis at cc
        "Nikki crosses her arms."
        voice "audio/voice/E2/D6/S2/Nikki/6.ogg"
        sf "Yeah, sure, likely story."
        pf "No really! I accidentally left it in my GEAR."
        show nikki ske at cc
        voice "audio/voice/E2/D6/S2/Nikki/7.ogg"
        sf "What?"
        pf "… twice."
        show storm:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        show nikki dis at cc
        ##MISSINGLINE##
        voice "audio/voice/E2/missing/nikki/1.ogg"
        sf "Come on, at least come up with something more believable."
        
        menu:
            "What's more believable than the truth?":
                pf "No, really, it's the truth!"
                show nikki ske at cc
                voice "audio/voice/E2/D6/S2/Nikki/8.ogg"
                sf "What was your phone doing in your GEAR in the first place?"
                pf "It was charging."
                show dots:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "She blinks at me."
                show nikki ann at cc
                voice "audio/voice/E2/D6/S2/Nikki/9.ogg"
                sf "You really are hopeless!"
                pf "Look!"
        
            "Okay then, I was just ignoring you.":
                pf "You're right. I didn't answer your texts on purpose."
                show vein:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki ang at cc
                voice "audio/voice/E2/D6/S2/Nikki/10.ogg"
                sf "That's so rude!"
                pf "Exactly, why would I do that my little sister?"
                show nikki ann at cc
                voice "audio/voice/E2/D6/S2/Nikki/11.ogg"
                sf "Because you're secretly a big mean jerkface."
                pf "Oh yeah? Well this \"big mean jerkface\" is going to prove you wrong."
        
            "It's not my problem if you don't believe me.":
                pf "I shouldn't need to come up with a lie to convince you of the truth."
                show nikki ann at cc
                voice "audio/voice/E2/D6/S2/Nikki/12.ogg"
                sf "Maybe if the truth weren't so far-fetched. Why would your phone ever be in your GEAR?"
                pf "To charge."
                show nikki ske at cc
                "She raises an eyebrow."
                pf "If you don't believe me, then look for yourself."
        
        "I pull up my messages and flash the phone in her face."
        show nikki thi at cc
        "Rolling her eyes, she reluctantly takes a look."
        stop music fadeout 10
        "..."
        show nikki ner at cc
        voice "audio/voice/E2/D6/S2/Nikki/13.ogg"
        sf "Oh."
        pf "What do you mean by \"oh\"?"
        show nikki wor at cc
        "Nikki bites her lip as she continues scrolling."
        voice "audio/voice/E2/D6/S2/Nikki/14.ogg"
        sf "Oh no…"
        "She hands back my phone."
        
        if MCStory == 3:
            "That's not the reaction I was expecting. Something's up. {w}I narrow my eyes."
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
            pf "I don't like \"oh no\"... {w}What did you do, Nikki?"
            show nikki thi at cc
            voice "audio/voice/E2/D6/S2/Nikki/15.ogg"
            sf "Ummm… You might not want to go into the garage…"
            pf "The garage…?"
            "{i}My bike!{/i}"
        
        else:
            "She seems worried about something. Probably for how mean she was to me yesterday."
            pf "It's okay, Nikki. I understand why you were angry yesterday, but I wanted you to know I didn't do it on purpose. {w}No hard feelings, right?"
            show nikki thi at cc
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
            voice "audio/voice/E2/D6/S2/Nikki/16.ogg"
            sf "Umm… about that…"
            pf "Huh?"
            show nikki wor at cc
            voice "audio/voice/E2/D6/S2/Nikki/17.ogg"
            sf "Remember when you said you were going out today?"
            pf "Yeah…"
            show drop:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D6/S2/Nikki/18.ogg"
            sf "You might not want to do that."
            pf "Why not?"
            show nikki ner at cc
            "Nikki shuffles her feet and continues to bite her lip."
            voice "audio/voice/E2/D6/S2/Nikki/19.ogg"
            sf "Because you definitely don't want to go into the garage."
            "My eyes widen."
            
        scene black with fade
        "I spin on my heel and race towards the garage as Nikki cries out for me to wait. {w}Throwing open the door, I feel like a hand is squeezing my heart."
        scene bg homekaito garage day with fade
        "Nikki catches up with me and cringes."
        show nikki ner at cc with dissolve
        voice "audio/voice/E2/D6/S2/Nikki/20.ogg"
        sf "Now, before you get mad--"
        pf "Nikki."
        show panic:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        show nikki wor at cc
        voice "audio/voice/E2/D6/S2/Nikki/21.ogg"
        sf "--just remember that I was really, {i}really{/i} annoyed with you and wanted revenge."
        pf "Not. Helping."
        show nikki sad at cc
        #play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 10
        "She quiets down, but she can't stand the silence."
        voice "audio/voice/E2/D6/S2/Nikki/24.ogg"
        sf "At least it looks really pretty now?"
        pf "It looks like a unicorn threw up all over my baby!"
        show nikki win at cc
        "All I can do is stare in horror at the glittery desecration of my beautiful bike. {w}Nikki hides her face in her hands."
        show crying:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D6/S2/Nikki/25.ogg"
        sf "I'm sorryyy!"
        show nikki sad at cc
        voice "audio/voice/E2/D6/S2/Nikki/26.ogg"
        sf "I promise I'll clean it up."
        pf "Yeah, you will."
        voice "audio/voice/E2/D6/S2/Nikki/27.ogg"
        sf "Let me get a bucket."
        hide nikki with dissolve
        "Nikki turns to leave, but I sigh."
        pf "Not right now. I have to go."
        show nikki ner at cc with dissolve
        "I take another look at the pink sparkles winking in the light."
        pf "... Maybe I should take the bus."
        pf "No! I can't. The bus won't come for another 20 minutes and I need to leave now."
        show drop:
            xoffset 720
            yoffset 160
            xzoom .75
            yzoom .75
        show nikki sad at cc
        voice "audio/voice/E2/D6/S2/Nikki/28.ogg"
        sf "Okay, I'll clean it up later then."
        stop music fadeout 3
        hide nikki with dissolve
        # bike sfx
        scene bg isokaze neighborhood day with dissolve
        "I nod. {w}With a grimace, I reluctantly ease myself onto my bike. {w}The engine roars to life, and glitter flutters behind me in a rainbow trail of happiness."
        stop ambient fadeout 5
        scene black with fade
        pf "This is so embarrassing."
        
        #weekend event
           
        if E2D6S1_ChoseKaori == 1:
            jump E2KIS4_Continued
            
        elif E2D6S1_ChoseMayu == 1:
            jump E2MAS4_Continued
            
        elif E2D6S1_ChoseShou == 1:
            jump E2SSS4_Continued
            
        elif E2D6S1_ChoseValerie == 1:
            jump E2VBS4_Continued
            
        elif E2D6S1_ChoseYuuna == 1:
            jump E2YMS4_Continued
            
        elif E2D6S1_ChoseAlone == 1:
            "I head out to get my order anyways."
            $ renpy.pause(1.0)
            "..."
            "....."
            "I pick up my order and end up eating at the restaurant alone."
            "With some time to kill, I head off to the mall and cruise around until it's time to head home."
            jump E2D6S2
            
        #
