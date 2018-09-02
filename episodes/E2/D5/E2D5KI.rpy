#
label E2D5KI:
    
    "Kaori didn't look so thrilled when that girl showed up. Maybe I should check on her."
    #show highschoolgirl2 extra at l3
    #show studentF extra at cc
    #show highschoolgirl extra at r3:
    #   xzoom -1
    #with dissolve
    #show kaori ann at l2
    #show mei smi at r2:
    #   xzoom -1
    #with dissolve
    "I find her in a corner of the living room, surrounded by a group of students."
    #show exclamation:
    #    xoffset 1040
    #    yoffset 100
    #    xzoom .75
    #    yzoom .75
    #show mei cur with dissolve
    #$renpy.pause(.5)
    #hide mei with dissolve
    "The girl from earlier stands beside her, but when she spots the rest of her team she runs off to greet them."
    #hide highschoolgirl2
    #hide studentF
    #hide highschoolgirl
    #with dissolve
    show kaori ann at l2 with dissolve
    $renpy.pause(.5)
    stop music fadeout 5
    show bully3 extra at r2 with dissolve:
        xzoom -1
    "As I approach, Kaori has her arms folded and she's trying to keep a wide berth between herself and the boys. I catch the tail end of their conversation."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/D5/KI/122.ogg"
    ki "Please, you guys are no competition at all. The day you losers beat me in a match is the day I'm dead."
    "One of the boys laughs."
    # what is this supposed to be? "Frat Bro"?
    voice "audio/voice/E2/D5/KI/fbro1/1.ogg"
    fbro1 "Those are tough words coming from someone so cute."
    play sound "audio/sfx/Human/Hand Slap.ogg"
    show kaori cur at l2, Shake(None, .25, dist=10)
    "Quick as lightning, he slaps Kaori's butt."
    show kaori sur at l2
    "Suddenly, time warps and slows. Kaori's body tenses and her eyes grow wide as her brain registers what just happened."
    show kaori ang at l2
    "Then the fire reaches her eyes and melts her frozen body."
    show vein:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    $renpy.pause(.5)
    play sound "audio/sfx/Human/light_punch.ogg"
    show bully3 extra at r2, Shake(None, .75, dist=25):
        linear .5 yoffset 1200
    "She brings her arm back and slugs the guy in the face so hard he collapses to the floor."
    show kaori ann at l2

    menu:
        "Good for you.":
            pf "Nice one, Kaori! That jerk got exactly what he deserved."
            show exclamation:
                xoffset 380
                yoffset 110
                xzoom .75
                yzoom .75        
            show kaori cur with dissolve
            "She spins around at the sound of my voice and blinks in surprise."
            voice "audio/voice/E2/D5/KI/123.ogg"
            ki "Huh? How long have you been standing there?"
            stop music fadeout 3
            pf "Long enough to see what that guy did to you."
            show kaori dis at l2
            "At the mention of the unconscious guy, Kaori's fierce glare returns."

        "Holy crap!":
            pf "Wow, Kaori, that was--"
            "I'm interrupted by a fist coming dangerously close to me."


            #timed
            $ qtebase = 3
            $ qtetotal = qteath + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E2D5KI_Freeze")
            $ E2D5KI_KaoriHit = 0
            
            menu:
                "Scream.":
                    $ E2D5KI_KaoriHit = 1
                    $ renpy.hide_screen ("timer_scr")
                    with Shake((0, 0, 0, 0), .5, dist=15)
                    "The inevitable looms ever closer. All I can do is let out a yelp as a sharp pain throbs in my stomach."

                "Dodge." if MCStory != 1:
                    $ renpy.hide_screen ("timer_scr")
                    "I shift out of the way and narrowly avoid getting a black eye."
                
                "{color=#00ff00}{b}Dodge.{/b}{/color}" if MCStory == 1:
                    $ renpy.hide_screen ("timer_scr")
                    "I shift out of the way and narrowly avoid getting a black eye."
                
                "Freeze.":
                    label E2D5KI_Freeze:
                        $ E2D5KI_KaoriHit = 1
                        $ renpy.hide_screen ("timer_scr")
                        with Shake((0, 0, 0, 0), .5, dist=15)
                        "Before I can even react, there's a sharp pain in my stomach. I double over, clutching at my abdomen."
                
                "Block." if MCStory != 1:
                    $ renpy.hide_screen ("timer_scr")
                    "Acting quickly, I push the incoming fist safely away from my face. That could have been bad."
                
                "{color=#00ff00}{b}Block.{/b}{/color}" if MCStory == 1:
                    $ renpy.hide_screen ("timer_scr")
                    "Acting quickly, I push the incoming fist safely away from my face. That could have been bad."

            if E2D5KI_KaoriHit == 0:
                pf "Hey, you almost hit me!"
                show kaori ang at l2
                voice "audio/voice/E2/D5/KI/124.ogg"
                ki "Sorry, but you shouldn't sneak up on me like that!"

            else:
                pf "What the hell was that for, Kaori?"
                "I rub at my chin and work my jaw. That girl sure can pack a punch!"
                show kaori dis at l2
                voice "audio/voice/E2/D5/KI/125.ogg"
                ki "What are you doing sneaking up on me like some kind of pervert!"

            show kaori ann at l2
            pf "I've been here this whole time."
            voice "audio/voice/E2/D5/KI/126.ogg"
            ki "Why didn't you say something then?"
            stop music fadeout 3
            pf "You seemed a little busy…"
            show kaori dis at l2
            "Kaori glances back down at the unconscious guy."

        "Back away slowly…":
            "That escalated quickly. It might be better to stay away until Kaori's had a chance to cool down."
            "I nonchalantly take one step back, when Kaori turns her head and locks eyes with me. I stand in place while she points at the unconscious guy on the floor."
            show kaori ang at l2
            voice "audio/voice/E2/D5/KI/127.ogg"
            ki "Did you see what that creep did?"
            stop music fadeout 3
            show kaori ann at l2
            pf "Yup."
            show kaori dis at l2
            voice "audio/voice/E2/D5/KI/128.ogg"
            ki "What a little pervert!"

    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    "She nudges him with her foot, and watches as he doesn't stir."
    pf "He's clocked out for the night."
    show kaori ann at l2
    voice "audio/voice/E2/D5/KI/129.ogg"
    ki "Serves him right!"
    "Whistles break from the silent onlookers as a few of the girls cheer and the guys start laughing."
    show kaori dis at l2
    voice "audio/voice/E2/D5/KI/fbro2/1.ogg"
    fbro2 "Damn, did you see what she just did to Takeshi?!"
    voice "audio/voice/E2/D5/KI/fbro3/1.ogg"
    fbro3 "Yeah, I'm not getting on her bad side."
    voice "audio/voice/E2/D5/KI/fbro2/2.ogg"
    fbro2 "Nope, me neither."
    ### VOICE - line labelled "fbro3" actually did this recorded line, inserting anyway- not changing character until notified
    voice "audio/voice/E2/D5/KI/fbro3/2.ogg"
    fbro4 "She's kind of scary actually…"
    pf "Why don't we get out of here?"
    show kaori neu at l2
    "Kaori nods."

    "We're about to move when a tall, buff pilot slams a bottle onto a nearby table."
    show bully2 extra at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E2/D5/KI/fbro5/1.ogg"
    fbro5 "Poor Takeshi."
    "Dropping into a chair, he laughs."
    stop music fadeout 2.0
    voice "audio/voice/E2/D5/KI/fbro5/2.ogg"
    fbro5 "So you can handle yourself when it comes to strength, but can you do the same when it comes to alcohol?"
    show storm:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori thi at l2
    "Kaori crosses her arms and snorts."
    voice "audio/voice/E2/D5/KI/130.ogg"
    ki "Not interested."
    voice "audio/voice/E2/D5/KI/fbro5/3.ogg"
    fbro5 "What's the matter? You scared?"
    "A taunting song of \"ooohs\" circle from the onlookers."
    show kaori mis at l2
    "Kaori laughs."
    voice "audio/voice/E2/D5/KI/131.ogg"
    ki "Me, scared? No way! I'm just trying to save you from embarrassment."
    voice "audio/voice/E2/D5/KI/fbro5/4.ogg"
    fbro5 "No, I get it. Drinking is a {i}man's game{/i}. Women aren't built to hold their alcohol."
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    show kaori dis at l2 with dissolve
    "Kaori's eyes flash, and the smile drops from her face."
    voice "audio/voice/E2/D5/KI/132.ogg"
    ki "What did you say?"
    voice "audio/voice/E2/D5/KI/fbro5/5.ogg"
    fbro5 "It's probably best that we don't do this, actually. I wouldn't want you to hurt yourself."
    "The chair scrapes along the floor as Kaori sits down."
    show vein:
        xoffset 365
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ang at l2
    voice "audio/voice/E2/D5/KI/133.ogg"
    ki "The only person who'll be hurting is you after I drink you under the table!"
    show kaori ann at l2

    menu:
        "This is a bad idea.":
            "A health-nut like Kaori doesn't strike me as someone who's used to drinking. She could get really sick if she's not careful."
            pf "Kaori, are you sure you want to do this?"
            voice "audio/voice/E2/D5/KI/134.ogg"
            ki "Of course!"
            pf "Just think about what you're doing."
            show kaori mis at l2
            voice "audio/voice/E2/D5/KI/135.ogg"
            ki "Don't worry, I can beat this guy."
            pf "But what if you can't? Is it really worth the risk?"
            show kaori ann at l2
            "She looks me hard in the eyes."
            voice "audio/voice/E2/D5/KI/136.ogg"
            ki "I can and I will."
            "My protests fall on deaf ears."

        "Let me do it instead.":
            "I glance at the bulky man sitting across from Kaori. There's no way she'll be able to out-drink a guy this big."
            pf "Kaori, wait."
            show kaori ske at l2
            voice "audio/voice/E2/D5/KI/137.ogg"
            ki "What?"
            pf "Let me do it instead. I can take this guy no problem."
            show kaori ann at l2
            "She narrows her eyes at me."
            voice "audio/voice/E2/D5/KI/138.ogg"
            ki "You don't think I can take him?"
            pf "That's not what I said…"
            show kaori dis at l2
            voice "audio/voice/E2/D5/KI/139.ogg"
            ki "I can fight my own battles."
            "I shrug. Guess that didn't work."

        "Who am I to stop her?":
            "Kaori's old enough to make her own choices. If she wants to drink with this guy then what gives me the right to stop her?"
            "Still, I should stick around to make sure she doesn't get herself too sick."

    "Someone places two shot glasses on the table--one in front of each challenger--and fills them up. Then he explains the rules."
    show kaori ann at l2
    voice "audio/voice/E2/D5/KI/fbro2/3.ogg"
    fbro2 "First person to reach 10 shots is the winner."
    "Kaori reaches for hers first and downs it before her challenger takes a drink. She doesn't even flinch from the burning liquid."
    show kaori ang at l2
    voice "audio/voice/E2/D5/KI/140.ogg"
    ki "Another!"
    show kaori ann at l2
    voice "audio/voice/E2/D5/KI/fbro5/6.ogg"
    fbro5 "Hey!"
    "He quickly downs his cup while Kaori's is being refilled, then fills up his own cup."
    show kaori mis at l2
    "Kaori grins."
    voice "audio/voice/E2/D5/KI/141.ogg"
    ki "Try and keep up, okay?"
    "Instead of responding, the guy throws back his drink, and Kaori follows."
    hide kaori
    hide bully2
    with dissolve
    "An even larger crowd gathers around the pair as they drink shot after shot. Everyone watches with baited breath, but neither competitor shows any sign of weakness." 
    "Kaori is like a machine, and empties her cup faster than it can be filled. {w}The crowd stares at her with admiration."
    "Her challenger keeps up a steady pace and the race is close."
    "After her tenth shot, Kaori slams her cup onto the table right before her opponent."
    show kaori ann b3 at l2
    show bully2 extra at r2:
        xzoom -1
    with dissolve
    
    stop music fadeout 3.0
    voice "audio/voice/E2/D5/KI/142.ogg"
    ki "Done!"
    voice "audio/voice/E2/D5/KI/fbro5/7.ogg"
    fbro5 "Damn!"
    show kaori mis b3 at l2
    "The crowd erupts into a roar of cheers as they equally congratulate Kaori and tease her challenger. The pilot tries to stand but looks a little queasy and sits back down."
    hide bully2
    show kaori cur b3 at cc
    with dissolve
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    "Kaori is also unsteady on her feet, but I catch her before she falls."
    show kaori neu b3 at cc
    voice "audio/voice/E2/D5/KI/143.ogg"
    ki "I'm okay."
    show kaori dis b3 at cc
    "I let go, and she squints up at me."
    show kaori ske b3 at cc
    voice "audio/voice/E2/D5/KI/144.ogg"
    ki "What did you do to your face?"
    pf "Huh?"
    show kaori cur b3 at cc
    voice "audio/voice/E2/D5/KI/145.ogg"
    ki "Your face. It's so blond."
    pf "Uh, I'm sorry?"
    show kaori mis b3 at cc
    voice "audio/voice/E2/D5/KI/146.ogg"
    ki "No, it's not bad."

    menu:
        "Geez, Shou or Mayu should take Kaori home.":
            pf "Go home, Kaori, you're drunk."
            show kaori ann b3 at cc
            voice "audio/voice/E2/D5/KI/147.ogg"
            ki "No, I'm not. Drunk is just weakness entering the body."
            pf "That's not right."
            show kaori cur b3 at cc
            voice "audio/voice/E2/D5/KI/148.ogg"
            ki "Shhhhh."
            "She floats a finger near my face but doesn't quite know where to put it."
            show shou ske at l3 with dissolve
            "Shou came over after all the commotion and sees Kaori's floating finger. He calmly collects her hand and places it back to her side."
            voice "audio/voice/E2/D5/SS/127.ogg"
            ss "Okay, that's fun and all, but I think it's time to go."
            show shiny:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori hap b3 at cc
            voice "audio/voice/E2/D5/KI/149.ogg"
            ki "Time to go… on an adventure?"
            show drop:
                xoffset 230
                yoffset 20
                xzoom .75
                yzoom .75
            show shou hap at l3
            voice "audio/voice/E2/D5/SS/128.ogg"
            ss "Sure!"
            show kaori mis b3 at cc
            voice "audio/voice/E2/D5/KI/150.ogg"
            ki "I bet I can get there first!"
            show shou cur at l3
            voice "audio/voice/E2/D5/SS/129.ogg"
            ss "What?"
            hide kaori with dissolve
            show shou sur at l3 with dissolve
            "She pushes past Shou and runs towards the door."
            show panic:
                xoffset 230
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/SS/130.ogg"
            ss "No! Wait!"
            hide shou with dissolve
            "Stumbling slightly, he chases after her amid a backdrop of laughter."
            #fade to black
            scene black with fade
            stop music fadeout 5
            "I hang out a little longer at the party, and head home once everything dies down. {w}It was a great night, even if things got a little wild!"
            #end
            jump E2D5KI_End

        "I should take Kaori home before things get worse.":
            "Yup, she's drunk and it's late. I think it's time for her to leave before she embarrasses herself even more. {w}Kaori won't be able to get home alone. I better walk her back."
            "I help her to her feet."
            pf "C'mon, Kaori, time to go."
            show kaori ske b3 at cc
            voice "audio/voice/E2/D5/KI/151.ogg"
            ki "No, you can't tell me what to do."
            "As she talks, I lead her towards the door anyway."
            show kaori thi b3 at cc
            voice "audio/voice/E2/D5/KI/152.ogg"
            ki "Fine, I'm going, but only because I want to go."
            stop ambient fadeout 3
            scene black with fade
            #stop music fadeout 3
            "Hm, that sounds like a very \"Kaori\" thing to say. Maybe she's not as drunk as I thought."
            play ambient "audio/ambience/Night Crickets.ogg" fadein 3
            scene bg campus main night with fade
            #play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 3
            "The cool night breeze is a welcome relief from the stuffy dorm. As we walk through the silent campus, Kaori trips over a root, and I catch her fall."
            show kaori cur b2 at cc with dissolve
            "She gasps as I hold her, but doesn't push me away."

            menu:
                "Let her go.":
                    "Once she's back on her feet, I let go."
                    show kaori neu b2 at cc
                    pf "Sorry."
                    show dots:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    "She stares at me, but doesn't say anything."
                    if MCStory != 3:
                        "I can't tell what she's thinking."
                    else:
                        "I get the feeling she didn't want me to let her go, but that can't be right."

                "Pull her closer.":
                    "I pull her into me."
                    pf "You're lucky I was here to catch you."
                    show kaori neu b2 at cc
                    voice "audio/voice/E2/D5/KI/153.ogg"
                    ki "Um."
                    pf "Really? That's all you're going to say?"
                    show storm:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    show kaori thi b2 at cc
                    "She scrunches her face, as if trying to remember something."
                    show kaori cur b2 at cc
                    voice "audio/voice/E2/D5/KI/154.ogg"
                    ki "Oh!"
                    show kaori ann b2 at cc
                    voice "audio/voice/E2/D5/KI/155.ogg"
                    ki "Stop being a perv!"
                    "I laugh, and let go of her."

                "It's weird to see clumsy Kaori.":
                    "I immediately set her back on her feet."
                    pf "You need to be more careful."
                    show kaori ann b2 at cc 
                    voice "audio/voice/E2/D5/KI/156.ogg"
                    ki "Thanks, it came out of the ground and attacked me."
                    pf "That's not how it happened."

            show kaori neu b2 at cc
            "She's uncharacteristically quiet for a while. It's strange to see her so calm. Usually she's so… fiery."
            show kaori mis b2 at cc
            voice "audio/voice/E2/D5/KI/157.ogg"
            ki "Your reaction time is better than I remember."
            pf "Thanks?"
            show kaori smi b2 at cc
            voice "audio/voice/E2/D5/KI/158.ogg"
            ki "You've improved a lot since our first match."

            if E2D5S4_Gladiator == 1:
                voice "audio/voice/E2/D5/KI/159.ogg"
                ki "I still can't believe you took out all three of them by yourself."
                "She looks straight into my eyes."
                ### NOTE Points - "if high points with kaori:"
                # temporarily set to 0
                if kaoromance > 0:
                    "My heart beats faster under her gaze."
                    show kaori smi b2 at cc
                    "She leans in closer to me."
                show kaori mis b2 at cc
                voice "audio/voice/E2/D5/KI/160.ogg"
                ki "You are really impressive."

            else:
                show kaori mis b2 at cc
                voice "audio/voice/E2/D5/KI/161.ogg"
                ki "I mean, I had no idea you'd actually be so much help for this last match."

            "Do my ears deceive me or did Kaori just give me a compliment?"
            pf "Is that really what you think?"
            show kaori smi b2 at cc
            voice "audio/voice/E2/D5/KI/162.ogg"
            ki "Yeah."
            pf "I never knew you felt that way."
            show kaori ske b2 at cc
            voice "audio/voice/E2/D5/KI/163.ogg"
            ki "So what?"
            pf "Nothing. It's just nice to know that you like me."
            show kaori thi b3 at cc with dissolve
            "Her cheeks are red, but I can't tell if it's from the alcohol or this conversation."
            voice "audio/voice/E2/D5/KI/164.ogg"
            ki "Shut up, it's not like that."
            scene bg campus building night with dissolve
            "We arrive in front of her building, and Kaori steps to the entrance."
            
            
            
            
            
            if E2KIS2_Completed == 0:
                jump E2D5KI_Goodnight
            
    ### NOTE Bug - This dialogue section was written here but I'm currently not seeing any way for the player to access it even if they did complete this section
    # Is it supposed to go in the "Goodnight" label? Either way, this needs to be moved/adjusted for it to happen
    if E2KIS2_Completed == 1:
        show kaori neu b2 at cc with dissolve
        menu:
            "Ask her about that mysterious man in the parking lot.":
                "Kaori has opened up to me a lot. I wonder if she'll tell me who she was with the other night."
                pf "Wait."
                show kaori neu b2 at cc
                "She turns back to me."
                pf "Can I ask you something?"
                voice "audio/voice/E2/D5/KI/165.ogg"
                ki "What?"
                pf "That night I ran into you in the parking lot, what were you doing with that older guy?"
                show kaori mis b2 at cc
                "She cocks her head to the side, amused."
                voice "audio/voice/E2/D5/KI/166.ogg"
                ki "Why? Are you jealous?"
                show kaori smi b2 at cc
    
                menu:
                    "I'm concerned.":
                        pf "No, I'm just worried."
                        show kaori mis b2 at cc
                        voice "audio/voice/E2/D5/KI/167.ogg"
                        ki "You don't have to be worried. I can take care of myself."
                        pf "I don't doubt that."
    
                    "I don't care if he's your boyfriend.":
                        pf "Me, jealous? I don't care if you're seeing anyone else. It's just he's a lot older than you and I'm worried about his intentions."
                        show note:
                            xoffset 720
                            yoffset 110
                            xzoom .75
                            yzoom .75
                        show kaori mis b2 at cc
                        "Kaori bursts out laughing."
                        voice "audio/voice/E2/D5/KI/168.ogg"
                        ki "His intentions are pure. Although I don't know if I can say the same for you."
    
                    "No.":
                        pf "Whatever, I don't even know why I asked."
                        show kaori mis b2 at cc
                        "Kaori smirks."
                        voice "audio/voice/E2/D5/KI/169.ogg"
                        ki "Mmhm."
    
                jump E2D5KI_Goodnight
    
    
            "Don't ask her anything.":
                jump E2D5KI_Goodnight
    
    label E2D5KI_Goodnight:
        pf "So, do you have your ID?"
        show kaori neu b2 at cc with dissolve
        "Kaori nods, and fishes it out of her pocket."
        show kaori smi b2 at cc
        voice "audio/voice/E2/D5/KI/170.ogg"
        ki "Goodnight, thanks for walking me home."
        pf "Are you going to be okay? Do you need help getting back into your room?"
        show kaori mis b2 at cc
        voice "audio/voice/E2/D5/KI/171.ogg"
        ki "Nu-uh, I won't fall for that. You aren't getting into my room."
        pf "That wasn't my intention."
        show kaori smi b2 at cc
        voice "audio/voice/E2/D5/KI/172.ogg"
        ki "I'll be fine."
        pf "Okay, goodnight then."
        ### NOTE Points - "if you have high points with Kaori:"
        # temporarily set to 0
        if kaoromance > 0:
            show kaori cur b2 at cc
            voice "audio/voice/E2/D5/KI/173.ogg"
            ki "Oh, I almost forgot!"
            pf "Hm?"
            show kaori hap b2 at cc
            pf "Eh?!"
            # sprite zoom and perhaps a screen nod?
            "I'm caught off-guard as she combs her hands through my golden locks."
            show heart:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D5/KI/174.ogg"
            ki "Ah! It's so soft and fluffy!"
            show kaori smi b2 at cc
            $renpy.pause(1.0)
            "What."
            "Just."
            "Her voice."
            "???"
            "I'm too stunned to react. {w}Kaori steps back and admires her handiwork."
        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
        "She smiles, then swipes her ID and disappears into the building."
        $renpy.pause(1.0)
        hide kaori with dissolve
        $renpy.pause(1.0)
        "That was kind of an {i}interesting{/i} night… {w}If only I was able to record drunk Kaori for sober Kaori to see."
        "...I'm feeling embarrassed just {i}thinking{/i} about it."
        scene black with fade
        stop music fadeout 5
        "With Kaori safely inside, I head back to my bike and drive home."
        jump E2D5KI_End
    
    label E2D5KI_End:
        $ E2D5KI_Completed = 1
        stop ambient fadeout 3
        "It's late by the time I get home, and everyone is already asleep. I tiptoe into my room and collapse onto my bed. Exhausted, I fall asleep as soon as my head hits the pillow."
        jump E2D6S1

