label E1D4S2:
    
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    
    scene bg campus hangar day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
    if (E1D2S11_JoinedTheTeam == 1):
        "By the time I arrive at the hangar, the team is already waiting by Shou's GEAR."
        show mayu smi at l3 with dissolve
        show kaori ann at r3 with dissolve:
            xzoom -1
        show shou neu at cc with dissolve
        "Mayu is the first to notice me and gives me a small wave. {w}Kaori and Shou seem to be arguing about something, but Shou silences her when I arrive." 
        show shou smi at cc
        pf "Hey guys."
        show kaori neu at r3
        "Kaori glances at me and nods."
        voice "audio/voice/E1/D4/S2/Kaori/1.ogg"
        ki "At least you aren't late." 
        show shou hap at cc
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/1.ogg"
        ss "Broseph, you made it!"
    
        menu:
            "I came as soon as I could!":
                pf "I left as soon as I got your text. Big news, right?"
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/2.ogg"
                ss "Yeah! We got our assigned time slot."
                pf "When is it?" 
                show kaori thi at r3
                voice "audio/voice/E1/D4/S2/Kaori/2.ogg"
                ki "Later. Right now, we need to practice."
                pf "Understood." 
    
            "Eyyo!":
                pf "Of course, anything for my favourite teammate."
                show shou cur with dissolve
                "Shou points to himself."
                voice "audio/voice/E1/D4/S2/Shou/3.ogg"
                ss "That's me, right?"
                "I grin."
                pf "I'll let you guys decide."
                show kaori thi at r3 with dissolve
                show dots:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show mayu cur at l3 with dissolve
                show confused:
                    xoffset 230
                    yoffset 135
                    xzoom .75
                    yzoom .75
                "Kaori rolls her eyes. Mayu seems confused."
                show shou smi at cc
                pf "So now that I'm here, let's get this match underway."
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/3.ogg"
                ki "The match is later, right now we need to practice."
                show mayu smi at l3
                "I nod."
    
            "It wasn't really a choice.":
                pf "Yeah, I got your text. When's the match?" 
                show kaori thi at r3
                voice "audio/voice/E1/D4/S2/Kaori/4.ogg"
                ki "Later today. I wanted to get some practice in first." 
                "I nod."
    
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/5.ogg"
        ki "Alright, head to your GEARs and turn on your simulators. Let's see what we're working with."
                
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
        show shou smi at cc with dissolve
        "I group with Shou at the hangar before we meet up with the rest of the team."
        show mayu neu at l3 with dissolve
        show kaori neu at r3 with dissolve:
            xzoom -1
        show shou hap at cc with dissolve
        "Shou smiles sheepishly as we turn to meet the girls."
        voice "audio/voice/E1/D4/S2/Shou/18.ogg"
        ss "Um, hey, Kaori… So, remember when I said I found a fourth team member?"
        show mayu cur at l3
        show kaori sur at r3 with dissolve
        "Kaori points at me." 
        show kaori ang at r3 with dissolve
        show vein:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Kaori/16.ogg"
        ki "No way. Not this guy. I thought you'd actually found someone useful."
        show mayu wor at l3
        show kaori ann at r3
        show shou sur at cc
        show panic:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/19.ogg"
        ss "He is useful!" 
        voice "audio/voice/E1/D4/S2/Kaori/17.ogg"
        ki "No."
        show shou ner at cc
        voice "audio/voice/E1/D4/S2/Shou/20.ogg"
        ss "He's useful in that he'll be the reason they let us participate in the qualifiers."
        show mayu neu at l3
        show kaori dis at r3 with dissolve
        "Kaori glares at him and says nothing."
        voice "audio/voice/E1/D4/S2/Kaori/18.ogg"
        ki "We'll find someone else." 
        show mayu wor at l3 with dissolve
        voice "audio/voice/E1/D4/S2/Mayu/3.ogg"
        ma "There isn't anyone else." 
        show kaori neu at r3
        show shou cur at cc
        "Shou and Kaori turn towards Mayu. She quickly lowers her eyes."
        show mayu ner at l3
        voice "audio/voice/E1/D4/S2/Mayu/4.ogg"
        ma "If there were, we would have found them already…"
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/21.ogg"
        ss "Truer words have never been spoken, my friend."
        show mayu smi at l3 with dissolve
        show kaori ann at r3 with dissolve
        "She grins shyly, but Kaori crosses her arms defiantly."
    
        menu: 
            "Apologise.": 
                pf "I'm really sorry for how we met, but I know I'll be a good addition to the team." 
                show shou hap at cc
                voice "audio/voice/E1/D4/S2/Shou/22.ogg"
                ss "See, he's a good guy!"
                show kaori dis at r3
                show storm:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/19.ogg"
                ki "If he were such a good guy he'd follow traffic laws." 
                show shou smi at cc
                voice "audio/voice/E1/D4/S2/Shou/23.ogg"
                ss "I'm sure he usually does."
                pf "It was an accident, and one that I regret."
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/24.ogg"
                ss "Look, he's already apologised, and we need another team member. Do you want to fight in the qualifiers or not?"
                "Kaori pauses."
                show kaori neu with dissolve
                voice "audio/voice/E1/D4/S2/Kaori/21.ogg"
                ki "Fine, but you better do what you're told."
                show shou smi at cc
                pf "Deal."
    
            "Trust me, I'm the only guy you need.": 
                pf "Listen to Shou, I'm exactly what you need." 
                show kaori ske at r3
                show question:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/20.ogg"
                ki "And how would you know what I need?" 
                "I shoot her a dazzling smile." 
                show mayu ner b1 at l3 with dissolve
                show shou ner with dissolve
                pf "I know what every woman needs."
                show kaori dis at r3
                "Shou nudges me."
                show shou wor at cc
                show frightful:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/25.ogg"
                ss "You're playing with fire, bro." 
                pf "I don't mind being burned, especially by a redhead." 
                show kaori ann at r3 with dissolve
                "Kaori stares at me coldly."
                voice "audio/voice/E1/D4/S2/Kaori/22.ogg"
                ki "No, absolutely not."
                show mayu wor at l3
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/26.ogg"
                ss "Kaori, come on, he's the only person left. Do you want to take part in the qualifiers or not?"
                "Kaori pauses."
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/23.ogg"
                ki "Fine! Just don't mess up."
                show mayu neu at l3
                show shou smi at cc
                pf "I never do."
    
            "You need me.": 
                pf "We both want the same thing. I can help you get it." 
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/24.ogg"
                ki "I don't need you."
                show mayu wor at l3
                pf "Yes, you do."
                show shou neu at cc
                voice "audio/voice/E1/D4/S2/Shou/27.ogg"
                ss "He's right, Kaori." 
                show kaori ann at r3
                show storm:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                "Kaori shoots Shou a deadly glare." 
                show shou ske with dissolve
                show question:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/28.ogg"
                ss "Do you want to participate in the qualifiers or not? If you don't accept him, we may as well go home now."
                "She never loses her scowl, but nods reluctantly."
                show kaori dis at r3 with dissolve
                voice "audio/voice/E1/D4/S2/Kaori/25.ogg"
                ki "Fine you can join, but this doesn't change anything."
                show mayu neu at l3
                show shou smi at cc
                pf "Fine." 
    
        show shou hap with dissolve
        voice "audio/voice/E1/D4/S2/Shou/29.ogg"
        ss "Alright! Now we're talking." 
        show mayu cur at l3 with dissolve
        show dots:
            xoffset 230
            yoffset 135
            xzoom .75
            yzoom .75
        show kaori neu at r3 with dissolve
        show dots2:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        "All three of us stare silently at him." 
        show shou cur with dissolve
        voice "audio/voice/E1/D4/S2/Shou/30.ogg"
        ss "Or not."
        show mayu smi at l3
        show kaori thi at r3
        voice "audio/voice/E1/D4/S2/Kaori/26.ogg"
        ki "Stop wasting time, Shou! We need to practice."
        pf "What about the qualifier?"
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/31.ogg"
        ss "That's later."
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/27.ogg"
        ki "We need to see what you've got. Hurry up and get in your GEAR so we can start a simulation."
        
        
    elif (E1D2S11_JoinedTheTeam == 0) and (E1S2D10_AskedOtherTeams == 1):
        "Shou is inside the hangar, eyeing his GEAR with a broad smile. {w}He glances over his shoulder and waves at me." 
        show shou hap at cc with dissolve
        show exclamation:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/4.ogg"
        ss "Hey bro!"
        pf "Hey! Where is everybody?" 
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/5.ogg"
        ss "They'll be here soon. They're not as fast as you." 
    
        menu: 
            "I wasn't far.":
                pf "I was just finishing up class not far from here."
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/6.ogg"
                ss "Cool, the girls should be here soon." 
    
            "It's a gift." :
                pf "What can I say? I'm skilled at many things."
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/7.ogg"
                ss "Oh yeah, like what?" 
                pf "Maybe if you're lucky, you'll find out." 
                show shou hap at cc
                "Shou laughs."
                show shou mis at cc
                show note:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Shou/8.ogg"
                ss "Luckily the ladies didn't hear that."
    
            "I'm ready for the qualifiers.":
                pf "When's the match?"
                show shou mis at cc
                voice "audio/voice/E1/D4/S2/Shou/9.ogg"
                ss "Whoa, someone's eager. Let's wait for the rest of the team though, so we can talk about it together." 
                pf "Okay." 
    
        pf "Have you spoken to the rest of the team yet?" 
        show shou thi at cc with dissolve
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/10.ogg"
        ss "So, about that--"
        "Suddenly, we hear a voice behind us."
        show mayu neu at l3 with dissolve
        show kaori neu at r3 with dissolve:
            xzoom -1
        show shou neu at cc
        voice "audio/voice/E1/D4/S2/Kaori/6.ogg"
        ki "Shou, is this the new teammate you were talking about?" 
        show kaori ske at r3 with dissolve
        "She gives me a once over, then sighs."
        voice "audio/voice/E1/D4/S2/Kaori/7.ogg"
        ki "I suppose you'll do."
        show shou mis at cc
        pf "Thanks?"
        show mayu smi at l3
        voice "audio/voice/E1/D4/S2/Shou/11.ogg"
        ss "See? I told you you'd like him!"
        show kaori thi at r3
        show drop:
            xoffset 1175
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Kaori/8.ogg"
        ki "It's not like we're swimming in offers."
        show shou hap at cc
        "Shou ignores her and claps me on the back."
        show kaori neu at r3
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S2/Shou/12.ogg"
        ss "Welcome aboard, broseph!"
        "He points to the dark haired girl, who gives me a small smile."
        show shou smi at cc
        voice "audio/voice/E1/D4/S2/Shou/13.ogg"
        ss "This is Mayu. The last member on our team."
    
        if (E1D2S4_MayuGaveDirections == 1):
            "She looks familiar…"
            pf "Oh yeah! You're that pilot who gave me directions."
            show mayu hap b1 at l3 with dissolve
            show regBlush:
                xoffset 230
                yoffset 135
                xzoom .75
                yzoom .75
            "She nods, and her smile broadens."
            voice "audio/voice/E1/D4/S2/Mayu/1.ogg"
            ma "It seems like they helped." 
            show mayu smi at l3 with dissolve
            pf "They did, thanks again."
    
        else:
            "She nods."
            voice "audio/voice/E1/D4/S2/Mayu/2.ogg"
            ma "Glad to have you on our team."
    
        pf "Thanks! So, now what?"
        show kaori mis at r3
        voice "audio/voice/E1/D4/S2/Kaori/9.ogg"
        ki "Now we practice."
        show mayu neu at l3
    
        menu: 
            "What about the match?":
                pf "Isn't it time for the qualifiers?"
                show kaori neu at r3
                voice "audio/voice/E1/D4/S2/Kaori/10.ogg"
                ki "No, that's later today, and we have to test your skill level first." 
                pf "Got it."
    
            "Take the lead!": 
                pf "Excellent! I'll show you some of my moves." 
                show kaori dis at r3
                voice "audio/voice/E1/D4/S2/Kaori/11.ogg"
                ki "No, you'll stay back." 
                pf "If you like… I can work from behind." 
                show shou hap at cc with dissolve
                voice "audio/voice/E1/D4/S2/Shou/14.ogg"
                "Shou snorts."
                show mayu cur b1 at l3
                show kaori ann at r3
                show question:
                    xoffset 230
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S2/Kaori/12.ogg"
                show vein:
                    xoffset 1175
                    yoffset 110
                    xzoom .75
                    yzoom .75
                ki "What?!"
                show shou smi at cc
                voice "audio/voice/E1/D4/S2/Shou/15.ogg"
                ss "Nothing."
                show mayu neu at l3
                show kaori neu at r3
    
            "I don't want to waste time.":
                pf "When's our qualifier?"
                voice "audio/voice/E1/D4/S2/Shou/16.ogg"
                ss "Later today." 
                pf "How late?"
                show kaori neu at r3
                voice "audio/voice/E1/D4/S2/Kaori/13.ogg"
                ki "Late enough that we have time to practice. I need to assess your skill level so I know what we're working with."
                pf "Fine."
    
        show shou hap at cc with dissolve
        "Shou glances at all of us, then breaks into a wide grin." 
        voice "audio/voice/E1/D4/S2/Shou/17.ogg"
        ss "Alright, we're in business! Let's do this."
        show mayu smi at l3
        show kaori thi at r3
        "Mayu hides a smile while Kaori rolls her eyes."
        voice "audio/voice/E1/D4/S2/Kaori/14.ogg"
        ki "Quit wasting time. Let's get into our GEAR and start a simulation."
        
    
    jump E1D4S3