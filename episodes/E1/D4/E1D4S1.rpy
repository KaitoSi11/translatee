label E1D4S1:
    
    
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    "Per usual, I'm awoken by the blare of my alarm, but today I don't hesitate to get out of bed."
    ##NEW SOUND NEEDED##play sound "audio/sfx/Human/light_punch.ogg" fadeout 1
    scene bg homekaito myroom day with fade
    "I have a really busy day ahead of me and can't afford to lounge around."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 3.0
    "I get dressed and head downstairs. As I pass Nikki's room, I notice her door is open and her room is empty. {w}She must be in the kitchen."

    scene bg homekaito main day with fade
    
    "When I reach the kitchen, no one is there. {w}Uncle Kaito is always gone before I wake up, but usually Nikki is around."
    "There must be something going on at her school today which is why she left early."
    
    "I fix myself a quick breakfast and scarf it down. {w}Then I hop on my bike and head to school."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    
    "Once I reach campus, I navigate to my class easily. {w}Hey! I'm getting used to this place."
    
    scene bg campus auditorium day with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    $renpy.pause(1)
    
    if (E1D2S2_talkwithyuunayes == 1):
        "As soon as I walk into class, I spot Yuuna seated in the front corner of the room."
        "The desk beside her is empty so I head over. When I get close, I notice a bag on the chair."
        pf "Hey, anyone sitting here?"
        
        show yuuna smi at cc with dissolve
        
        if (E1D2S2_YuunaComesWithYouPass == 1): #She knows your schedule if you've gone this far with her
            "She smiles when she notices me and removes the bag."
            show yuuna hap at cc
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S1/Yuuna/1.ogg"
            ym "No, I was saving it for you."
        
        else:
            "She smiles shaking her head and removes the bag."
        
        show yuuna smi at cc
        "My smile matches hers as I plop down beside her."
        pf "Thanks!"
        show yuuna smi b1 at cc with dissolve
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D4/S1/Yuuna/2.ogg"
        ym "No problem."
        pf "So, what do you think the professor will be like?"
        show yuuna cur at cc with dissolve
        voice "audio/voice/E1/D4/S1/Yuuna/3.ogg"
        ym "I've heard she's pretty good. She's tough but fair."
        pf "That sounds promising."
        hide yuuna with dissolve
        "Before she can respond, the professor enters the room and heads straight for the front desk."
    
    else:
        "The classroom is mostly full by the time I arrive, and all of the seats in the back are taken."
        "I spot an empty seat close to the window by the front of the room."
        show yuuna neu at cc with dissolve
        "As I sit down, the girl beside me, with bright pink hair, glances briefly in my direction."
        hide yuuna with dissolve
        "A few minutes later, the professor enters the room and heads straight for the front desk."
    
    show professorF extra at cc with dissolve
    stop music fadeout 3
    voice "audio/voice/E1/D4/S1/Professor/1.ogg"
    prof2f "Welcome to History 201. Today we'll be covering…"
    
    scene black with fade
    $renpy.pause(1)
    "The lesson lasts a while but the material is not bad."
    $renpy.pause(2.5)
    scene bg campus auditorium day with fade
    
    $renpy.pause(1)
    
    show professorF extra at cc with dissolve
    
    voice "audio/voice/E1/D4/S1/Professor/2.ogg"
    prof2f "We only have a few minutes before class ends, but your first assignment will be a group project on a case study of your choice. Since it's the first day of class, I'll be assigning your partners."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    "She points to pairs of students sitting next to each other. {w}Finally, she reaches me."
    voice "audio/voice/E1/D4/S1/Professor/3.ogg"
    prof2f "You and you are partners."
    hide professorF extra with dissolve
    show yuuna cur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    
    if (E1D2S2_talkwithyuunayes == 1):
        "She points to Yuuna and I."
        show yuuna smi at cc with dissolve
        "We glance at each other and grin. {w}Working with her should be fun."
    
    else:
        "She points to me and the pink-haired girl beside me."
        show yuuna smi at cc with dissolve
        "We look at each other and she gives me a friendly smile. {w}She seems nice enough."
        
    show yuuna neu at cc
    voice "audio/voice/E1/D4/S1/Professor/4.ogg"
    prof2f "Your project will be due next week. Class dismissed!"
    play sound "audio/sfx/Human/Class End.ogg" fadeout 1
    "The classroom is abuzz with the shuffle of students. {w}I turn towards my partner."
    
    if (E1D2S2_talkwithyuunayes == 1):
        pf "I'm looking forward to working with you."
        show yuuna hap at cc with dissolve
        "She beams."
        voice "audio/voice/E1/D4/S1/Yuuna/4.ogg"
        ym "Same here. What do you think our topic should be?"
    
    else:
        pf "Hi, I'm [pfirst]."
        show yuuna smi at cc
        "She smiles warmly."
        voice "audio/voice/E1/D4/S1/Yuuna/5.ogg"
        ym "I'm Yuuna. Pleased to meet you."
        show yuuna cur at cc
        "Her eyes flick to my stripes."
        voice "audio/voice/E1/D4/S1/Yuuna/6.ogg"
        ym "You must be new."
        pf "Yeah, how did you know?"
        show yuuna smi at cc
        voice "audio/voice/E1/D4/S1/Yuuna/7.ogg"
        ym "I tend to know most of the pilots here."
        "Although her uniform fits her like a glove, it is severely lacking in stripes."
        pf "You aren't a pilot, are you?"
        show yuuna hap at cc
        "She laughs lightly."
        voice "audio/voice/E1/D4/S1/Yuuna/8.ogg"
        ym "No, I've just worked with a lot of them. I'm a Pilot Health and Physiotherapy student."
        show yuuna smi at cc
        pf "That's a mouthful."
        show yuuna hap at cc
        "She laughs again."
        voice "audio/voice/E1/D4/S1/Yuuna/9.ogg"
        ym "Yeah, PHPT for short."
        show yuuna smi at cc
        voice "audio/voice/E1/D4/S1/Yuuna/10.ogg"
        ym "Anyway, what do you think our topic should be?"
        
    show yuuna neu at cc
    pf "Hm…"
    
    menu:
        "\"Pioneering Pilots\".":
            $ E1D4S1_Pioneer = 1
            pf "What if we focused on the pilots who essentially made piloting what it is today possible?"
            "Wait--she's not a pilot..."
            pf "Of course, if you don't want to focus on pilots we don't have to."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/11.ogg"
            ym "I don't mind. After all, what I'm studying is still relevant to pilots. It's a good idea. We can even begin with the early pilots who helped develop the first militarized GEAR."
            pf "My thoughts exactly."
    
        "The evolution of GEARs.":
            pf "What if we focused on GEARs throughout the ages?"
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/12.ogg"
            ym "Good idea! We can begin with the military prototypes and gradually show how the same technology has changed and developed into the commercial and entertainment vessels we use today."
            pf "Sounds like a solid plan to me."
    
        "{color=#00ff00}{b}The psychology of Cenorobotics.{/b}{/color}" if (MCStory == 3):
            jump E1D4S1_MCStory1
    
        "The psychology of Cenorobotics." if (MCStory != 3):
            label E1D4S1_MCStory1:
            pf "What if we focused more on the psychological impact of the development and growth of Cenorobotics as a field?"
            show yuuna cur at cc with dissolve
            $renpy.pause(1)
            show yuuna hap at cc with dissolve
            "Her face lights up."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D4/S1/Yuuna/13.ogg"
            ym "Absolutely! This could also delve into social impact and how society is adapting to the growth of this field, such as the development of new specialities--like studies in pilot health."
            pf "That should be right up your alley."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/14.ogg"
            ym "What about you? Are you okay with that?"
            pf "It sounds interesting to me too."
    
        "I don't know. It's all the same to me.":
            #Yuuna doesn't like this answer much
            pf "The topic doesn't matter to me. Anything would be fine."
            show yuuna ner at cc with dissolve
            voice "audio/voice/E1/D4/S1/Yuuna/15.ogg"
            ym "Oh."
            pf "What about you? You have a topic you want to do?"
            show yuuna thi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/16.ogg"
            ym "Well--"
            show dots:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            "She pauses, then shakes her head."
            show yuuna neu at cc
            voice "audio/voice/E1/D4/S1/Yuuna/17.ogg"
            ym "Never mind. We don't have to decide right now. Let's think about it and discuss it later."
            pf "Are you sure? It seems like you have an idea in mind."
            show yuuna smi at cc
            voice "audio/voice/E1/D4/S1/Yuuna/18.ogg"
            ym "Sort of. Maybe we could focus on the movement for greater awareness in making pilot health and safety a key social concern, which would also inevitably highlight some of the common dangers and misuses of GEARs."
            "I shrug."
            pf "Sounds good to me."
            
    stop ambient fadeout 3
    show yuuna hap at cc with dissolve
    "Yuuna smiles."
    voice "audio/voice/E1/D4/S1/Yuuna/19.ogg"
    ym "It sounds like we have our topic."
    pf "Yeah, I'm feeling good about this."
    show yuuna smi at cc
    voice "audio/voice/E1/D4/S1/Yuuna/20.ogg"
    ym "Me too. We're going to have a great project."
    "By this time, most of the class has already caught up with their partners and left the room. {w}We should probably do the same. There might be another class that needs this room."
    
    if (E1D2S5_GotYuunasNumber == 1):
        pf "Cool, so I should probably head out, but I'm sure I'll see you again soon."
        show yuuna hap at cc
        voice "audio/voice/E1/D4/S1/Yuuna/21.ogg"
        ym "Sure, let me know when you're free to work on the project."
        pf "Will do."
        show yuuna smi at cc
        "She smiles as we both gather our things."
    
    else:
        pf "Anyway, we should probably get going."
        voice "audio/voice/E1/D4/S1/Yuuna/22.ogg"
        ym "Yeah, you're right."
        "I begin to gather my things when Yuuna interrupts me."
        show yuuna cur with dissolve
        voice "audio/voice/E1/D4/S1/Yuuna/23.ogg"
        ym "Wait, may I have your number?"
    
        menu:
            "Did a girl just ask me for my number?":
                pf "What?"
                show yuuna smi at cc
                voice "audio/voice/E1/D4/S1/Yuuna/24.ogg"
                ym "Would you like to exchange numbers?"
                "Is this real life? I surreptitiously pinch myself and try not to flinch from the pain. {w}Definitely not a dream."
                show yuuna sur b1 at cc with dissolve
                show shoBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Yuuna blushes under my continued gaze."
                voice "audio/voice/E1/D4/S1/Yuuna/25.ogg"
                ym "F-For the project!"
                pf "Oh, right, the project that we're working on together."
                show yuuna smi b1 at cc with dissolve
                voice "audio/voice/E1/D4/S1/Yuuna/26.ogg"
                ym "Yes."
                "I knew it was too good to be true."
                pf "Sure."
                show yuuna smi at cc with dissolve
                "She smiles."
    
            "*Smirk*":
                "No lady can resist my boyish charm! I flash her a winning smile."
                pf "For you? Of course."
                show yuuna cur b1 at cc with dissolve
                "Yuuna blushes."
                voice "audio/voice/E1/D4/S1/Yuuna/27.ogg"
                ym "It's just so we can work on the project."
                pf "Mmhm… for the project."
                "I wink at her."
                pf "I get it."
                show yuuna smi b1 at cc
                show regBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "She blinks and gives me a hesitant smile."
    
            "Why does she want to know?":
                pf "What?"
                show yuuna smi at cc
                voice "audio/voice/E1/D4/S1/Yuuna/28.ogg"
                ym "Um, would you like to exchange numbers?"
                "I narrow my eyes."
                pf "Why?"
                show yuuna cur b1 at cc with dissolve
                "Her cheeks steadily turn red."
                show shoBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S1/Yuuna/25.ogg"
                ym "For the project!"
                pf "Oh… Sure."
                show yuuna smi b1 at cc
                "She smiles."
    
            "Give my number.":
                pf "867-5309."
                show yuuna ske at cc with dissolve
                "Yuuna blinks and furrows her brow."
                show question:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D4/S1/Yuuna/30.ogg"
                ym "Um, aren't you missing some numbers?"
                show yuuna thi at cc
                "She gives me a strange look."
                voice "audio/voice/E1/D4/S1/Yuuna/31.ogg"
                ym "If you don't want to give me your number I'll understand."
                pf "Sorry! That was an old American number. Let me give you my new number."
                show yuuna cur at cc
                voice "audio/voice/E1/D4/S1/Yuuna/32.ogg"
                ym "Oh, okay, sure."
    
        show yuuna smi with dissolve
        "We quickly exchange numbers and gather our things." 
    
    scene black with fade
    $renpy.pause(1)
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    
    "My phone vibrates as we leave the classroom. {w}I glance at her, wondering if she already sent me a text, but she doesn't have her phone out."
    "When I pull up my phone, I see an unread message from Shou."
    "{i}Big news Broseph! We are in first phase of qualifier matches. Team is meeting at the hangar.{/i}"
    
    if (E1D2S11_JoinedTheTeam == 1):
        "Having my first official team meeting should be interesting. {w}Although I feel a couple of flutters in my stomach, I'm more excited than nervous to see everyone."
    
    elif (E1D2S3_MetKaoriWasRudeNoHelmet == 1):
        "My stomach twists into a tight knot. I wonder how Kaori will react when she sees me. {w}I hope Shou knows what he's doing..."
        
    elif (E1D2S11_JoinedTheTeam == 0) and (E1S2D10_AskedOtherTeams == 1):
        "I wonder how the others are. {w}I suppose I'll be meeting everyone soon enough."
        
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus building day with fade
    
    "Once we're outside, Yuuna turns towards me."
    
    show yuuna smi at cc with dissolve
    voice "audio/voice/E1/D4/S1/Yuuna/33.ogg"
    ym "Do you have any more classes today?"
    pf "No, but I'm headed for the hangar. I've got to meet my team before the qualifiers."
    "She nods."
    show yuuna hap at cc
    voice "audio/voice/E1/D4/S1/Yuuna/34.ogg"
    ym "Good luck!"
    pf "Thanks!"
    hide yuuna with dissolve
    "We wave and head our separate ways."
    
    stop music fadeout 3.0
    scene black with fade
    $renpy.pause(2.5)   
    
    jump E1D4S2