#
label E2D2S3:
    
    stop music
    stop ambient
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    #Afternoon Choice end

    "I'm basically done for the day, but I don't feel like going home just yet. I wander the campus aimlessly as I decide what I want to do."

    menu:
        "Study at the library.":
            $ context = "library"
            "I should stay on top of my classes and get some studying done."
            stop ambient fadeout 3
            scene black with fade
            $renpy.pause(2.5)
            play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
            scene bg campus library day with fade
            play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
            "I'm more familiar with the campus now and have no trouble finding the library. {w}Students lounge in the open areas, a coffee in one hand and a book in the other. It reminds me of CINY. I guess some things just translate across cultures."
            "I'm a little surprised by how many students are here so early in the semester, and it takes me a while to find an empty desk. {w}I finally find one on the third floor. It's not as secluded as I'd like it to be, but it'll do."
            "Settling into my desk, I can't help but notice all the graffiti. {w}Yup, some things really don't change."
            "Pulling out my tablet, I get to work."
            scene black with fade
            $renpy.pause(2.5)
            #time pass
            scene bg campus library day with fade
            $renpy.pause(1)
            show studentM extra at cc with dissolve
            "After about half an hour, I'm interrupted by the student at the desk beside me. He's wearing stripes on his uniform so he must be a pilot."
            voice "audio/voice/E2/D2/S3/stu7m/1.ogg"
            stu7m "Sorry to bother you. I don't know if you recognise me or not but we have Piloting 101 together."
            "He looks vaguely familiar, but we've never spoken before. I nod."
            voice "audio/voice/E2/D2/S3/stu7m/2.ogg"
            stu7m "I'm wondering if you can help me with a question."
            pf "Sure."
            voice "audio/voice/E2/D2/S3/stu7m/3.ogg"
            stu7m "For what use were GEAR initially developed?"

            menu:
                "Civilian.":
                    pf "I think it was for civilian use, which is why it's so popular today."
                    "The student looks thoughtful."
                    voice "audio/voice/E2/D2/S3/stu7m/4.ogg"
                    stu7m "Hmm, are you sure? I'll double check that in the text. Thanks."
                    hide studentM with dissolve
                    "He returns behind the desk blinders and refocuses on his studies."
                    "Now that I think about it, I might have given him the wrong answer."

                "Military.":
                    # + intelligence
                    pf "It was for military use, but now they're used commercially everywhere."
                    "He grins."
                    voice "audio/voice/E2/D2/S3/stu7m/5.ogg"
                    stu7m "Oh yeah, I think I remember reading that! Thanks!"
                    hide studentM with dissolve
                    "After another nod of thanks, he returns to his text."
                    "I feel smarter for having known the answer."

                "Government.":
                    pf "I think it was for government use, and it was transformed into commercial use only after receiving government approval."
                    "He frowns."
                    voice "audio/voice/E2/D2/S3/stu7m/6.ogg"
                    stu7m "Hmm… That doesn't sound right, but thanks anyway."
                    hide studentM with dissolve
                    "He returns to his desk and refocuses on his studies."
                    "I'm disappointed that I got that wrong. Maybe I need to study harder."

            #time pass
            scene black with fade
            $renpy.pause(1)
            "Nobody else bothers me after that, and I'm able to complete my studying in peace."
            $renpy.pause(1)
            scene bg campus library dusk with fade
            jump E2D2S3_Convergence

        "Check out the quad.":
            "It's a gorgeous day and I don't want to be cooped up inside. I'll go to the quad and see what's happening there."
            "I remember briefly passing through the quad last week, so I have a vague idea of how to get there. Mostly I just follow the greenery."
            "After a few minutes, I spot the open lawn of green grass. A couple of guys are running around the yard, playing some sort of game. At the same time, a bunch of students are having a picnic in the shade of a giant oak, and a few others are reading on the benches lining the yard."
            "Something flies towards my head, coming dangerously close to my eyes."

            #timed
            $ qtebase = 3
            $ qtetotal = qteath + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E2D2S3_Freeze")
            
            menu:
                "Duck!":
                    $ renpy.hide_screen ("timer_scr")
                    # + some athleticism
                    "Instinctively, I drop down as whatever it is flies over my head and lands softly in the grass. As I walk over to collect it, I realise it's a frisbee. {w}Two boys join me when I pick it up."
                    show studentM2 extra at l2 with dissolve
                    show studentM extra at r2 with dissolve:
                        xzoom -1
                    voice "audio/voice/E2/D2/S3/stu5m/1.ogg"
                    stu5m "Thanks for getting that for us."
                    pf "No problem."
                    jump E2D2S3_Win
        
                "Freeze!":
                    label E2D2S3_Freeze:
                        $ renpy.hide_screen ("timer_scr")
                        "My feet are rooted to the ground and I squeeze my eyes shut as I prepare for the inevitable. An instant feels like a lifetime before something hard crashes into my forehead, knocking me over."
                        "My vision blurs and darkens."
                        "When I'm able to see again, two boys are hovering over me."
                        show studentM2 extra at l2 with dissolve
                        show studentM extra at r2 with dissolve:
                            xzoom -1
                        voice "audio/voice/E2/D2/S3/stu5m/2.ogg"
                        stu5m "Are you hurt?"
                        pf "Just my pride."
                        "My head throbs."
                        jump E2D2S3_Lose
        
                "Catch!" if (MCStory != 1):
                    $ renpy.hide_screen ("timer_scr")
                    # + highest athleticism
                    "My body reacts even before I can fully process what's going on, and I reach out and grab the object. {w}It's a frisbee."
                    "One of the guys races towards me."
                    show studentM2 extra at l2 with dissolve
                    voice "audio/voice/E2/D2/S3/stu5m/3.ogg"
                    stu5m "Nice catch, man!"
                    pf "Heh, thanks."
                    voice "audio/voice/E2/D2/S3/stu6m/1.ogg"
                    stu6m "Over here!"
                    "The other guy waves at me and gestures for me to throw it back."
                    "I do, and he leaps into the air, catching it easily."
                    show studentM extra at r2 with dissolve:
                        xzoom -1
                    voice "audio/voice/E2/D2/S3/stu6m/2.ogg"
                    stu6m "Nice throw!"
                    jump E2D2S3_Win
                    
                "{color=#00ff00}{b}Catch!{/b}{/color}" if (MCStory == 1):
                    $ renpy.hide_screen ("timer_scr")
                    # + highest athleticism
                    "My body reacts even before I can fully process what's going on, and I reach out and grab the object. {w}It's a frisbee."
                    "One of the guys races towards me."
                    show studentM2 extra at l2 with dissolve
                    voice "audio/voice/E2/D2/S3/stu5m/3.ogg"
                    stu5m "Nice catch, man!"
                    pf "Heh, thanks."
                    voice "audio/voice/E2/D2/S3/stu6m/1.ogg"
                    stu6m "Over here!"
                    "The other guy waves at me and gestures for me to throw it back."
                    "I do, and he leaps into the air, catching it easily."
                    show studentM extra at r2 with dissolve:
                        xzoom -1
                    voice "audio/voice/E2/D2/S3/stu6m/2.ogg"
                    stu6m "Nice throw!"
                    jump E2D2S3_Win
        
                "Trip...":
                    $ renpy.hide_screen ("timer_scr")
                    "I try to move out of the way, but my foot catches on a root and I fall over. The object misses me entirely and lands safely a few feet away."
                    "I roll onto my back, trying to catch my breath, and two faces lean over me."
                    show studentM2 extra at l2 with dissolve
                    show studentM extra at r2 with dissolve:
                        xzoom -1
                    voice "audio/voice/E2/D2/S3/stu5m/4.ogg"
                    stu5m "Hey, you okay?"
                    pf "Yeah."
                    jump E2D2S3_Lose
        
        
                "Run!":
                    $ renpy.hide_screen ("timer_scr")
                    "Acting on their own, my legs start pumping and I'm sprinting away from whatever's flying at me. A quick glance back lets me know it's still on my tail."
                    
                    $ qtebase = 3
                    $ qtetotal = qteath + qtebase
                    $ t_var = qtetotal
                    show screen timer_scr(place="E2D2S3_Run")
                    
                    menu:
                        "Dodge!":
                            $ renpy.hide_screen ("timer_scr")
                            # + athleticism
                            "At the last second, I swerve out of the way, and the object lands safely in the grass beside me. {w}I walk over and notice it's just a frisbee."
                            "Two guys jog up to me."
                            show studentM2 extra at l2 with dissolve
                            show studentM extra at r2 with dissolve:
                                xzoom -1
                            voice "audio/voice/E2/D2/S3/stu5m/5.ogg"
                            stu5m "Hey! You alright?"
                            pf "Yeah, it missed me."
                            voice "audio/voice/E2/D2/S3/stu5m/6.ogg"
                            stu5m "Oh good!"
                            jump E2D2S3_Win
                        
                        "Run...":
                            label E2D2S3_Run:
                                $ renpy.hide_screen ("timer_scr")
                                "I keep running, and something strikes the back of my head, knocking me off balance. I manage to catch myself before I face-plant into the grass, but my head throbs."
                                "Somebody is beside me."
                                show studentM2 extra at l2 with dissolve
                                voice "audio/voice/E2/D2/S3/stu5m/7.ogg"
                                stu5m "Hey, are you okay?"
                                pf "Yeah."
                                show studentM extra at r2 with dissolve:
                                    xzoom -1
                                jump E2D2S3_Lose
        
            label E2D2S3_Win:
                voice "audio/voice/E2/D2/S3/stu6m/3.ogg"
                stu6m "Sorry about that. Butterfingers here can't aim to save his life."
                voice "audio/voice/E2/D2/S3/stu5m/8.ogg"
                stu5m "That's not true! It just slipped a little."
                pf "It's okay."
                jump E2D2S3_Together
        
            label E2D2S3_Lose:
                "One guy offers me a hand, which I take."
                voice "audio/voice/E2/D2/S3/stu6m/4.ogg"
                stu6m "We're really sorry about that."
                voice "audio/voice/E2/D2/S3/stu5m/9.ogg"
                stu5m "It was my fault. I threw the frisbee a little too hard and it got away from us."
                pf "These things happen."
                voice "audio/voice/E2/D2/S3/stu5m/10.ogg"
                stu5m "Thanks for being so cool about it."
                jump E2D2S3_Together
        
            label E2D2S3_Together:
                "The first guy squints at me, then his face lights up in recognition."
                voice "audio/voice/E2/D2/S3/stu6m/5.ogg"
                stu6m "Wait a minute, I know you! You're the chick magnet."
                pf "What?"
                voice "audio/voice/E2/D2/S3/stu5m/11.ogg"
                stu5m "Oh yeah! From the Foreign Exchange class."
                voice "audio/voice/E2/D2/S3/stu6m/6.ogg"
                stu6m "Remember us?"
                pf "Um, yeah."
                voice "audio/voice/E2/D2/S3/stu5m/12.ogg"
                stu5m "It's awesome that you're here!"
                "An idea dawns on him."
                voice "audio/voice/E2/D2/S3/stu5m/13.ogg"
                stu5m "Hey, you want to play with us?"
                voice "audio/voice/E2/D2/S3/stu6m/7.ogg"
                stu6m "Yeah! You should join us!"
        
                menu:
                    "Sure.":
                        $ context = "frisbee"
                        "I shrug. These guys are a bit excitable but otherwise don't seem so bad."
                        pf "Okay, I'll play."
                        voice "audio/voice/E2/D2/S3/stu6m/8.ogg"
                        stu6m "Awesome!"
                        voice "audio/voice/E2/D2/S3/stu5m/14.ogg"
                        stu5m "Let's move away from other people so there's no chance we'll accidentally hit anyone… again."
                        pf "Heh, good idea."
                        #time pass
                        scene black with fade
                        $renpy.pause(1)
                        "Those guys aren't too bad. I learned that they're from Korea and have been inseparable since childhood."
                        $renpy.pause(1)
                        scene bg campus main dusk with fade
                        jump E2D2S3_Convergence
        
                    "I'll pass.":
                        $ context = "noFrisbee"
                        "I'm not really in the mood."
                        pf "Thanks, but not this time."
                        voice "audio/voice/E2/D2/S3/stu5m/15.ogg"
                        stu5m "Say no more. You've got a hot date, don't you?"
                        voice "audio/voice/E2/D2/S3/stu6m/9.ogg"
                        stu6m "A smooth talker like him? Of course he does."
                        voice "audio/voice/E2/D2/S3/stu5m/16.ogg"
                        stu5m "Seriously, what's your secret?"
                        "Oh no, not this again."
                        jump E2D2S3_Convergence


        "Hang out at the Pilot's Lounge.":
            $ context = "lounge"
            stop ambient fadeout 5
            "There's nothing in particular I feel like doing, so I'm going to relax in the Pilot's Lounge."
            scene black with fade
            play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
            scene bg campus lounge day with fade
            "The leaderboard is still posted and people are still crowded around the rankings, talking. I decide to head to the bar and get a drink."
            show receptionist extra at cc with dissolve
            "The bartender waits for my order."

            menu:
                "Nothing alcoholic.":
                    "It's the middle of the day and way too early for a drink."
                    pf "I'll have a water, please."
                    "He nods and silently fills my glass."
                    hide receptionist with dissolve
                    pf "Thanks."

                "Order hard liquor.":
                    pf "Barkeep, I'll have the drink of men! On the rocks."
                    "He blinks in surprise, then nods and gets to work. I guess he doesn't come across too many people who order this."
                    "After a minute, he sets my glass down in front of me."
                    barm "The drink of men, as requested."
                    "I grin, and give him a generous tip."
                    pf "Thanks, my man."
                    "He seems confused."
                    barm "This is too much money."
                    pf "It's your tip."
                    barm "I can't accept this. You've paid enough for the drink."
                    hide receptionist with dissolve
                    "I shrug and take back the credits."

                "Beer.":
                    pf "I'll get whatever's on tap."
                    "He nods, and grabs a frosty mug, then expertly fills it to the perfect head-to-beer ratio."
                    barm "Your beer."
                    pf "Thanks."
                    hide receptionist with dissolve
                    "I pay for it, and he silently accepts my credits."

            "I find an empty table near one of the TVs and sip my drink. A professional GEAR exhibition match is on: USA vs. Japan. {w}USA is in the lead! I watch intently, secretly rooting for the USA team."
            show studentM2 extra at cc with dissolve
            "A pilot sits across from me, blocking my view of the match."
            voice "audio/voice/E2/D2/S3/stu2m/1.ogg"
            stu2m "Hey, you're part of the team that ranked 21, aren't you?"
            pf "Um, yeah..."
            voice "audio/voice/E2/D2/S3/stu2m/2.ogg"
            stu2m "I watched your match. You're not bad for a new guy. What's that thing you did with your core?"
            pf "Sorry, how did you know which team was mine in the rankings?"
            "He seems surprised."
            voice "audio/voice/E2/D2/S3/stu2m/3.ogg"
            stu2m "Your team is the only one listed without a name."
            pf "There's a name listed. It's ACE-2049-11."
            voice "audio/voice/E2/D2/S3/stu2m/4.ogg"
            stu2m "Yeah, but it's a generic name. One that was assigned because the team never submitted a name."
            pf "Oh."
            "I hadn't thought about a team name. Maybe this is something we should discuss at our next team meeting. I make a mental note to bring it up."
            voice "audio/voice/E2/D2/S3/stu2m/5.ogg"
            stu2m "Anyway, I just wanted to say congratulations on your ranking. That's a big deal for a new team."
            pf "Thanks. What ranking did you get?"
            "He grins."
            voice "audio/voice/E2/D2/S3/stu2m/6.ogg"
            stu2m "22."
            pf "Ha, no way."
            voice "audio/voice/E2/D2/S3/stu2m/7.ogg"
            stu2m "Yeah, you guys just beat us. Maybe I'll see you on the battlefield."
            pf "Maybe."
            "The roaring crowd interrupts our conversation. Glancing up at the TV, I see Japan is now tied for the lead."
            voice "audio/voice/E2/D2/S3/stu2m/8.ogg"
            stu2m "Did you see that?"
            pf "No, I missed it."
            voice "audio/voice/E2/D2/S3/stu2m/9.ogg"
            stu2m "That guy just took out the USA range GEAR! He faked them out by breaking formation and took them by surprise."
            pf "Really?"
    
            if E1D4S4_FollowMatchPlan == 0:
                voice "audio/voice/E2/D2/S3/stu2m/10.ogg"
                stu2m "Kind of like what you did. I didn't realise that was a real strategy."
                "Neither did I. Maybe I should bring this up to Kaori..."
                "I picture the ferocity of her glare and change my mind."
                
            hide studentM2 with dissolve
            "Looking back up, I hope to see a recap of the play I missed. Instead, there's an advertisement for ModBuzz's new product line."
            "A hot woman in an awfully tight spandex suit hops out of her GEAR and onto a beach. Her suit strategically falls away into a bikini, and she lounges on the beach with her GEAR. Every so often the accessories on the GEAR disappear and reappear with ModBuzz's latest additions."
            "The student glances up and scoffs."
            show studentM2 extra at cc with dissolve
            voice "audio/voice/E2/D2/S3/stu2m/11.ogg"
            stu2m "ModBuzz is such a ripoff."
            "I snap out of my daze."
            voice "audio/voice/E2/D2/S3/stu2m/12.ogg"
            stu2m "Their new \"environmentally friendly\" line? Sounds like an excuse to overcharge the public for the same stuff."

            menu:
                "We should all be more environmentally friendly.":
                    ### NOTE Item
                    #best shield
                    pf "I think it's great that a distinguished company such as ModBuzz is becoming more environmentally conscious and bringing awareness to such an important issue."
                    voice "audio/voice/E2/D2/S3/stu2m/13.ogg"
                    stu2m "I'm not saying being environmentally conscious isn't important. I just don't see how a shield affects the environment."
                    pf "She'll tell you."
                    "I nod towards the girl on the TV who is cheerfully explaining the science behind the new line."

                "Who cares? This ad is about the girl anyway.":
                    ### NOTE Item
                    #mediocre shield
                    pf "If buying a ModBuzz hippie friendly item gets me a date with that girl, then they can take my money."
                    "He laughs and glances back at the screen."
                    voice "audio/voice/E2/D2/S3/stu2m/14.ogg"
                    stu2m "She's talking about their hippie science, but I still don't see how a shield affects the environment."
                    pf "Neither do I, but right now, not much about her is being shielded and that's all that matters."

                "It's just another marketing scam.":
                    ### NOTE Item
                    #worst shield
                    pf "It's another way for large corporations to prey on the gullible and stupid."
                    voice "audio/voice/E2/D2/S3/stu2m/15.ogg"
                    stu2m "You agree with me?"
                    "He seems surprised by my reaction. {w}I guess not that many people share our views."
                    pf "It's all metal anyway. It'll all be disposed of in the same way."
                    voice "audio/voice/E2/D2/S3/stu2m/16.ogg"
                    stu2m "Yeah!"

            voice "audio/voice/E2/D2/S3/stu2m/17.ogg"
            stu2m "Anyway, it looks like they've got a promotion going on."
            "Another glance at the TV informs me if I text \"GREENPROTECT\" to the number listed, I'm eligible to win a free item from their latest line."
            voice "audio/voice/E2/D2/S3/stu2m/18.ogg"
            stu2m "You going to participate?"

            menu:
                "Text \"GREENPROTECT\".":
                    pf "Why not?"
                    "I'm always down for free stuff."
                    "It only takes me a few seconds to text the number above. {w}I wonder when I find out if I've won an item or not."
                    voice "audio/voice/E2/D2/S3/stu2m/19.ogg"
                    stu2m "Heh, maybe you'll actually win something."
                    pf "You going to do it?"
                    voice "audio/voice/E2/D2/S3/stu2m/20.ogg"
                    stu2m "Nah, don't think so."
        
                "Don't text.":
                    pf "No, not interested."
                    "I never liked ModBuzz, and their new line doesn't do anything to change my feelings towards them."
                    "He nods."
                    voice "audio/voice/E2/D2/S3/stu2m/21.ogg"
                    stu2m "Me neither."
                    
            hide studentM2 with dissolve
            "The match comes back on and we continue watching the game."
            #time pass
            scene black with fade
            $renpy.pause(1)
            ### NOTE ITEM
            #You get an item!
            scene bg campus lounge dusk with fade
            jump E2D2S3_Convergence

    label E2D2S3_Convergence:
        stop music fadeout 5
        play sound "audio/sfx/Technology/Phone Alarm.ogg"
        "My phone rings and Yuuna's name flashes on the screen."
    
        if context == "library":
            "I shouldn't be chatting on the phone while in the quiet study spaces. I pack up my tablet and head into the group study room where talking is allowed."
    
        if context == "frisbee":
            pf "Sorry, guys, I've got to take this. It's been fun!"
            "The guys nod, and wave at me."
            "I answer the phone as I search for a secluded spot to talk."
    
        if context == "noFrisbee":
            "Saved by the bell…"
            pf "Sorry, but I'm getting a call."
            voice "audio/voice/E2/D2/S3/stu6m/10.ogg"
            stu6m "From a girl?"
            pf "Yeah, actually."
            "He taps his nose."
            voice "audio/voice/E2/D2/S3/stu6m/11.ogg"
            stu6m "We won't keep you."
            voice "audio/voice/E2/D2/S3/stu5m/17.ogg"
            stu5m "But next time,  join us."
            pf "Sure."
            hide studentM
            hide studentM2
            with dissolve
            "We wave goodbye as I answer the phone."
    
        if context == "lounge":
            "I move to a quieter spot on the opposite side of the lounge."
    
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
        play sound "audio/sfx/Technology/Phone Answer.ogg"
        pf "Hi, Yuuna. How goes the search?"
        voice "audio/voice/E2/D2/Yuuna/1.ogg"
        ym "Actually, that's why I called you. I have some good news!"
        pf "What is it?"
        voice "audio/voice/E2/D2/Yuuna/2.ogg"
        ym "I got you an interview!"
        pf "Already? It's only been a day. {w}How'd you do it?"
        voice "audio/voice/E2/D2/Yuuna/3.ogg"
        ym "Lots of phone calls."
        "I laugh."
        pf "Thanks, Yuuna. This is great!"
        voice "audio/voice/E2/D2/Yuuna/4.ogg"
        ym "I know. It's with Warptech Corporation."
        "I nearly drop the phone."
        pf "How did you get a major player like Warptech interested in us?"
        voice "audio/voice/E2/D2/Yuuna/5.ogg"
        ym "I told them the truth. You guys are a strong, up-and-coming team, and with the right sponsor there to support you, you'll be unstoppable!"
        pf "Heh, thanks. We'd definitely have an advantage if we had access to Warptech's weaponry.{w}  When is the interview?"
        voice "audio/voice/E2/D2/Yuuna/6.ogg"
        ym "Yeah, about that..."
        "Her hesitation is ominous."
        voice "audio/voice/E2/D2/Yuuna/7.ogg"
        ym "Your interview is tomorrow."
    
        menu:
            "Drop the phone.":
                "The phone fumbles from my grip, but I catch it before it falls."
                voice "audio/voice/E2/D2/Yuuna/8.ogg"
                ym "Hello? You okay?"
                pf "Did you say tomorrow?"
                voice "audio/voice/E2/D2/Yuuna/9.ogg"
                ym "I know it's last minute, but their next availability is a few weeks away. I didn't think you could wait that long."
                pf "No, you're right. Sooner is better."
    
            "Hahaha!":
                pf "Good one. Any second now Kashton Utcher is going to jump out and then we'll all have a good laugh."
                voice "audio/voice/E2/D2/Yuuna/10.ogg"
                ym "Huh?"
                pf "This isn't a joke?"
                voice "audio/voice/E2/D2/Yuuna/11.ogg"
                ym "No, I'm serious. It's tomorrow and you need to be there."
    
            "Okay.":
                pf "I'll be there."
                "There's a pause before Yuuna speaks."
                voice "audio/voice/E2/D2/Yuuna/12.ogg"
                ym "Oh... Good!"
                pf "Is something wrong?"
                voice "audio/voice/E2/D2/Yuuna/13.ogg"
                ym "No, I was just expecting you to protest a little more."
                pf "Why?"
                voice "audio/voice/E2/D2/Yuuna/14.ogg"
                ym "Well, it is pretty short notice."
                pf "Okay."
                voice "audio/voice/E2/D2/Yuuna/15.ogg"
                ym "... Nevermind."
    
        pf "I need to call my team. I don't know if they'll be able to make it."
        voice "audio/voice/E2/D2/Yuuna/16.ogg"
        ym "They don't all need to be there. As long as one member of the team is there the interview can happen."
        voice "audio/voice/E2/D2/Yuuna/17.ogg"
        ym "Can you make it?"
        pf "I need time to prepare… especially if I'm going alone."
        voice "audio/voice/E2/D2/Yuuna/18.ogg"
        ym "No, I'll be there, and as a member of the SBA I'll be taking the lead in presenting your credentials. I've got everything under control."
        pf "Alright. I'll make my own preparations tonight and meet you tomorrow."
        voice "audio/voice/E2/D2/Yuuna/19.ogg"
        ym "Great, I'll meet you in front of the library after class."
        pf "Thanks again, Yuuna. I owe you one."
        voice "audio/voice/E2/D2/Yuuna/20.ogg"
        ym "It was my pleasure!"
        "We both hang up. The first thing I do is send a group text to my team."
        "{i}Got an interview with Warptech Corp tomorrow afternoon. {w}Can any of you join? {w}Ok if can't, I have it under control.{/i}"
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "A minute after I've sent the text, I receive a reply. It's from Shou, which is no surprise. He's always freakishly quick to respond."
        "{i}Broseph, I'll be hanging fritz on the doc plan{/i}"
        "I literally have no idea what that means. {w}I text him back."
        "{i}So you mean... yes?{/i}"
        #shake
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "Bzzt!"
        "{i}Haha! You're funny. Good luck and let me know how it goes.{/i}"
        "At least I got my answer. One down, two more to go."
        "I've still got some time before I need to go home."
        
        $ freeTime = "evening"
        
### NOTE FreeTime
    call E2FreeTime from _call_E2FreeTime_5

    jump E2D2S4
