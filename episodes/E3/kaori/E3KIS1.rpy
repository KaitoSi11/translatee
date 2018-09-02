#
label E3KIS1:
    
    #Afternoon (Day 1 only)
    
    if MCStory == 2:
        "I'd like to get an early start on studying for the next chapter. Time to head to the library!"
        
    else:
        "I'm starting to fall behind in my classes since all my focus has been on piloting. Time to head to the library!"
        
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus library day with fade
    "The library is filled with students, and I don't spot any free tables. Looks like other people had the same idea."
    
    "I spot a familiar plume of red hair sitting alone at a table in the corner. It's rare to spot Kaori at the library."
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    "She doesn't notice me as I approach. If I didn't know better, I'd say she looked half-asleep."
    
    menu:
        "Mind if I join you?":
            pf "I'm glad I ran into you. This place is packed!"
            show kaori thi at cc with dissolve
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "Kaori looks around groggily, like she has just woken up. Then greets me with a yawn."
            show kaori neu
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_01.ogg"
            ki "Yeah, I guess it is."
            pf "Are you feeling alright? You look a little…"
            show kaori dis
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_02.ogg"
            ki "I look a little what?"
            "Her eyes flash. She might be groggy, but she's still Kaori."
            pf "A little tired. Everything okay?"
            show kaori ske
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_03.ogg"
            ki "Huh? No, I'm fine. Why?"
            show kaori neu
            "The bags under her eyes tell a different story."
            pf "I'm just concerned."
    
        "You didn't have to save a seat just for me!":
            "I slide beside her, hoping to catch her off guard."
            show kaori cur at cc with dissolve
            show shocked:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            pf "Why thank you."
            "It worked better than I expected. She's completely startled."
            show kaori ske
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_04.ogg"
            ki "Huh? Oh, you."
            "She lets out a yawn before rubbing her eyes."
            show kaori neu
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_05.ogg"
            ki "What are you doing here?"
            pf "This seemed like a good place to take a nap. Looks like you had the same idea."
    
        "Move over, you're hogging the entire table.":
            pf "I thought the Japanese were supposed to be polite when it comes to sharing communal spaces."
            show kaori thi at cc with dissolve
            "It takes her a bleary-eyed moment to say anything."
            show storm:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_06.ogg"
            ki "Nobody asked you to sit here."
            pf "We're teammates. The invitation is implied."
            show kaori dis
            "Kaori scowls as I toss my things on the table."
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_07.ogg"
            ki "Fine, have a seat. I'm leaving soon anyways."
            pf "Don't worry. I'll be quiet, and you can get right back your nap."
            show kaori ann
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_08.ogg"
            ki "What nap?! I wasn't sleeping!"
            pf "That's not what it looked like to me."
    
    
    if E2KIS4_Completed == 0:
        show kaori dis
        "Kaori glares at me for a moment, almost as if she's trying to work up the energy to chastise me. Instead, she yawns."
        
        show kaori thi
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_09.ogg"
        ki "I've been busy."
        pf "I knew it! What's his name?"
        show kaori ske
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_10.ogg"
        ki "What?! I don't--"
        pf "Shhhh… Library, remember?"
        show kaori thi
        "Kaori's gaze shoots from one side of the library to the other. All of the students are busy with their own work, and no one seems to have noticed her outburst."
        show kaori dis
        "She whispers."
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_11.ogg"
        ki "That's not why I'm tired, you idiot!"
        pf "Why then?"
        "To my surprise, there's no sharp-tongued retort. Instead, she shrugs."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_12.ogg"
        ki "It's nothing, okay? I've just been pulling a lot of double shifts at work."
        pf "...You have a job?"
        show kaori ske
        ### VOICE - used to have "or something?" at the end, but voice skipped it
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_13.ogg"
        ki "Yeah… Is that a problem or something?"
        pf "No, it's just surprising. Between the team and classes, I barely have time to do anything else."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_14.ogg"
        ki "If you care enough about something, you make time for it."
        pf "What kind of--"
        show kaori dis
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_15.ogg"
        ki "None of your business."
        pf "I didn't even ask the question."
        show kaori thi
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_16.ogg"
        ki "You don't need to. It doesn't concern you."
        pf "It concerns me if you're too tired to compete in a match properly."
        show kaori dis
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_17.ogg"
        ki "Don't be stupid! I'd never let that happen."
        show kaori ann
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_18.ogg"
        ki "If it starts to impact my performance on the team, then you can gripe at me all you want. Until then, all you need to know is that I have another commitment, and I have to stick with it."
        
        if MCStory == 3:
            "She's getting pretty worked up. Maybe I should respect her privacy."
            pf "I get it. When you believe in something, you've got to see it through."
            show question:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ske
            "Kaori gives me a skeptical look." 
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_19.ogg"
            ki "Yeah…Thanks for not making a big deal about it."
        
        else:
            pf "I'd rather not wait to find out if it does affect a match {i}during{/i} a match. Besides, you're barely keeping your eyes open."
            show kaori dis
            voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_20.ogg"
            ki "And I'm telling you it won't affect my performance. So drop it, okay?"
            "She's wide awake now, losing any trace of grogginess. Maybe I just caught her at a bad time!"
            
        show kaori neu
        "I nod, and let the subject drop. She returns to her notes as I pull out the textbook from my bag."
        hide kaori with dissolve
        "We both study together in silence. She continues to yawn every so often, and I can tell she isn't at 100\%. Oh well, not like I can do much."
        scene black with fade
        $renpy.pause(1)
        "After some time, we both say our goodbyes and head out."
        
        # end
        $ E3KIS1_Completed = 1
    
    else:
        show kaori dis
        "For a moment, it almost looks like she's going to pull back and hit me. When her hands finally move, I flinch. But, to my surprise, she delivers an intense and dramatic stretching yawn."
        
        #Yawning
        show kaori thi
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_21.ogg"
        ki "I guess it doesn't matter if I tell you."
        show kaori neu
        "Maybe it's just because she's tired, but she seems relieved to be talking about it."
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_22.ogg"
        ki "One of the volunteers at the daycare left, and I had to take on their students. We were already short staffed, but now it's much worse."
        pf "That's a relief!"
        show kaori ske
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_23.ogg"
        ki "What? Why?"
        
        menu:
            "I've just never seen you look so worn out.":
                pf "I thought it might be something serious."
                show kaori dis
                "She narrows her eyes."
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_24.ogg"
                ki "Serious?"
                pf "Yeah, like family or school stuff."
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_25.ogg"
                ki "You're saying that I don't take my job with these kids seriously?"
                pf "No, that's not what I meant."
        
            "I thought you were doing {i}shenaniganry{/i}":
                if E2D5KI_Completed == 1:
                    pf "I thought you were hungover again."
                    show kaori cur
                    voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_26.ogg"
                    ki "...Again?!"
                    pf "You don't remember?"
                    show kaori thi b1
                    "She blushes."
                    show tsuBlush:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_27.ogg"
                    ki "I don't know what you're talking about."
        
                else:
                    pf "I thought maybe you were out partying."
                    show kaori ske
                    voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_28.ogg"
                    ki "I… Is that what you think I'm like?"
                    pf "It's okay with me if you want to get turnt up."
                    show kaori dis
                    voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_29.ogg"
                    ki "Why are you always so weird?"
        
            "I don't blame her, that's a {i}math{/i} textbook.":
                pf "I thought you were falling asleep trying to read {i}that{/i}."
                "I motion to the hefty textbook opened in front of her."
                show kaori dis
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_30.ogg"
                ki "I {i}wasn't{/i} sleeping!"
                pf "That's not how it looked to me."
                show storm:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_31.ogg"
                ki "I told you…"
                
        show kaori neu
        "Kaori lets out another big yawn."
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_32.ogg"
        ki "Don't worry about me. I just have to work a few doubles until we can find a replacement."
        pf "Why don't you share the work with the rest of the staff?"
        show kaori ske
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_33.ogg"
        ki "Do you know anything at all about educating children?"
        pf "Not really... "
        show kaori thi
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_34.ogg"
        ki "Obviously! At that age, one of the worst things you can do is to switch up their instructors. It has a terrible impact on their learning."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_35.ogg"
        ki "Children need stability and time to build up trust, and while they're getting used to us, we're learning about them. It takes time to understand how a child learns, what they're feeling."
        show kaori smi
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_36.ogg"
        ki "Some kids might have an easier time with change and it won't matter as much if there are rotating staff members, but other kids already have unstable homes to go home to. The daycare is the only place they feel safe."
        pf "Oh. I didn't realize …"
        show kaori neu
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_37.ogg"
        ki "And if I have to work a little bit harder for a week or two to make sure they get the best care, I will."
        
        if MCStory == 3:
            "There's a strong determination in her voice, and I can't help but admire her compassion towards those kids."
        
        pf "Still, you need to take care of yourself too..."
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_38.ogg"
        ki "I am."
        pf "You're falling asleep while studying. Are you going to fall asleep in the middle of a match too? Clearly, you're not getting enough rest."
        show kaori dis
        "She crosses her arms, but doesn't say anything."
        pf "I'm not trying to pry into your personal life, but you're my friend. I just want to make sure you're okay."
        show dots:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori neu
        "She continues to stay silent, but her look softens."
        pf "Besides, if you get sick, then they'll have a replacement instructor anyway."
        show kaori cur
        "Her eyes widen, before she looks down."
        show kaori ner
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_39.ogg"
        ki "I... I guess that makes sense."
        "She sighs."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_40.ogg"
        ki "Maybe I'll take it a bit easier..."
        "I smile and nod."
        show kaori mis
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_41.ogg"
        ki "But I'm fine right now so don't worry about me."
        $ E3KIS1_maamcall = 1
        pf "Yes, ma'am."
        show kaori ske
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_42.ogg"
        ki "Don't call me ma'am!"
        pf "Yes, Ms. Itami."
        show kaori ann
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_43.ogg"
        ki "No!"
        pf "Uhh... {i}Mrs.{/i} Itami?"
        show kaori dis
        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_44.ogg"
        ki "I'm going to hurt you now."
        "She leans over the table, her fist ready to slug my shoulder. Thankfully, I see it coming and quickly lean back..."
        show exclamation:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori cur with dissolve
        hide kaori with dissolve
        "...too far! {w}My chair wobbles precariously and I grasp wildly for something to hold onto."
        # sfx
        play sound "audio/sfx/Impacts/Kaori Falling Over.ogg"
        scene black
        "{i}Thud!{/i}"
        $renpy.pause(1)
        scene bg campus library day with fade
        show kaori smi at cc with dissolve
        "A few students look over while I rub my sore head. Kaori blinks at me in surprise and masks a giggle. Once sufficiently amused, she offers me a hand and helps pull me upright."
        show kaori neu
        "We study together in silence for a while. She occasionally glances at me, but averts her gaze whenever I look at her."
        
        menu:
            "Can I help you?":
                pf "Uh, need something?"
                show kaori ske
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_45.ogg"
                ki "What?"
                pf "You keep looking at me. Do you need something?"
                show kaori thi b1
                voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_46.ogg"
                ki "No, I don't, stop imagining things! Besides, {i}you{/i} keep looking at {i}me{/i}."
                "Her cheeks flush."
        
                menu:
                    "Oh, um okay then...":
                        pf "Errr... my bad. Sorry."
                        show kaori cur b1
                        "She blinks at me."
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_47.ogg"
                        ki "You don't have to apologise."
                        pf "Wait...so... you want me to look at you--"
                        show kaori sur b1
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_48.ogg"
                        ki "That's not what I said at all!"
                        pf "I'm so confused..."
                        show kaori win b1
                        "Kaori shakes her head, exasperated."
                        show kaori ner b2
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_49.ogg"
                        ki "Nevermind, just go back to studying!"
                        show tsuBlush:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori thi b2
                        "She buries her face deep in her book. I'm certain she's hiding another blush."
                        pf "Okay then..."
        
                    "Because you're a cutie.":
                        "I smirk boyishly."
                        show kaori ske b1
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_50.ogg"
                        ki "W-What is up with your face?"
                        "I merely tilt my head to the side and flash another grin."
                        show kaori wor b1
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_51.ogg"
                        ki "Stop!!"
                        pf "What? I haven't said or done anything."
                        show kaori ner b1
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_52.ogg"
                        ki "I... You..."
                        "She stumbles."
                        show kaori thi b2
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_53.ogg"
                        ki "...You're impossible!"
                        show tsuBlush:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        "Her cheeks redden as she hides her face deep in her book."
        
                    "Nevermind.":
                        "I shrug."
                        show kaori cur b1
                        "We blink at each other before she speaks up first."
                        show kaori neu b1
                        voice "audio/voice/E3/Free/KI/S1/kaori/Date_Kaori_54.ogg"
                        ki "I-I'm going back to studying."
                        pf "Same."
        
            "Focus on studying.":
                "I ignore our exchanging glances and refocus on studying."
                
        scene black with fade
        stop music fadeout 10
        "..."
        # sfx
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "We study for a while longer before Kaori's phone vibrates. After checking her text, she starts packing up. We say goodbye and I leave a short time thereafter."
        
        # end
        $ E3KIS1_Completed = 1
        
