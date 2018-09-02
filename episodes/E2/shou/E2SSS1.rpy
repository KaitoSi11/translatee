#
label E2SSS1:
    
    $ shoOut = "sUniform"
    
    #Evening Choice- Call Shou
    
    "Let’s see if Shou wants to hang out at the arcade or something."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "I call and he picks up after a few rings."
    voice "audio/voice/E2/Free/SS/1.ogg"
    ss "What’s up?"
    
    menu:
        "Let us partake in the merriment of cyber skirmishing.":
            pf "It’s time."
            voice "audio/voice/E2/Free/SS/2.ogg"
            ss "Time?"
            pf "To go to war."
            voice "audio/voice/E2/Free/SS/3.ogg"
            ss "..."
            pf "I cannot do it alone. Will you follow me into the gates of purgatory?"
            voice "audio/voice/E2/Free/SS/4.ogg"
            ss "That's a hefty request, my good sir."
            pf "It involves free snacks at the arcade."
            voice "audio/voice/E2/Free/SS/5.ogg"
            ss "That's simply an offer I can't refuse."
            pf "I figured as much."
            voice "audio/voice/E2/Free/SS/6.ogg"
            ss "I'll meet you there."
    
        "Ask Shou out on a date.":
            pf "Shou, let’s go on a date."
            voice "audio/voice/E2/Free/SS/7.ogg"
            ss "... Isn't it a little too soon to switch teams?"
            pf "I thought about it, and I realised you’re the only person I want to be with."
            voice "audio/voice/E2/Free/SS/8.ogg"
            ss "Wait, are you being serious right now?"
    
            menu:
                "Yes.":
                    pf "More serious than I've ever been."
                    "The next few seconds of silence are painfully awkward."
    
                "No.":
                    pf "Really?"
    
            pf "Of course I'm kidding! {w}Want to hit up the arcade?"
            voice "audio/voice/E2/Free/SS/9.ogg"
            ss "Oh, haha! Of course I knew it was a joke. I was just playing along of course."
            "Although he tries to play it cool, I can tell he's flustered."
            voice "audio/voice/E2/Free/SS/10.ogg"
            ss "I'm down for the arcade. I'll meet you there."
    
        "Let’s go to the arcade.":
            pf "You busy?"
            voice "audio/voice/E2/Free/SS/11.ogg"
            ss "Yes, I’m on a date right now."
    
            menu:
                "My bad! Enjoy.":
                    pf "Oh sorry, didn't mean to disturb you. I'll leave you to it."
                    voice "audio/voice/E2/Free/SS/12.ogg"
                    ss "Wait, broseph! I was just kidding!"
                    pf "Uh, okay."
                    voice "audio/voice/E2/Free/SS/13.ogg"
                    ss "I'm glad you think I can get a date though."
                    pf "Uh, sure."
                    "... This is awkward."
                    pf "... Anyway, want to meet up at the arcade?"
                    voice "audio/voice/E2/Free/SS/14.ogg"
                    ss "Yeah!"
    
                "You? On a date? Haha!":
                    pf "Your left hand doesn't count."
                    voice "audio/voice/E2/Free/SS/15.ogg"
                    ss "That's cold, broseph."
                    pf "Maybe you should wear gloves."
                    "There's a pause, then Shou bursts out laughing."
                    voice "audio/voice/E2/Free/SS/16.ogg"
                    ss "Good one."
                    "I smile."
                    pf "Want to meet at the arcade?"
                    voice "audio/voice/E2/Free/SS/17.ogg"
                    ss "Sure. Meet you there in a few."
                    
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "After hanging up, I head out to the arcade."
    stop ambient fadeout 3
    #fade out
    scene black with fade
    $renpy.pause(2.5)
    stop music fadeout 5
    #fade in
    play ambient "audio/ambience/Arcade.ogg" fadein 3
    #bg arcade
    scene bg activity arcade day with fade
    
    "As I enter the building, I spot Shou waving at me."
    show shou smi at cc with dissolve
    "As soon as I join him, he leads me deeper into the arcade."
    pf "Where are we going?"
    voice "audio/voice/E2/Free/SS/18.ogg"
    ss "To a game which will showcase our skills."
    pf "But the GEAR simulators are the other way."
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    show shou mis at cc
    voice "audio/voice/E2/Free/SS/19.ogg"
    ss "Not those skills."
    "Shou stops in front of a shooting game and pulls a gun out of the holster."
    show shou hap at cc
    voice "audio/voice/E2/Free/SS/20.ogg"
    ss "Shall we see who the better marksman is?"
    "The game has inbuilt sensors so we can duck to the side to take cover or peek out and the game will read that movement. It's a team based game, but it sounds like Shou wants to turn it into a competition."
    
    $ E2SSS1_Coop = 0
    
    menu:
        "How about we work together instead?":
            $ E2SSS1_Coop = 1
            pf "You know this game is co-op, right?"
            show shou mis at cc
            voice "audio/voice/E2/Free/SS/21.ogg"
            ss "What's the harm in some friendly competition?"
            pf "Nothing, but I'd rather work together to beat the current high score."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/22.ogg"
            ss "Oh, that make sense!"
    
        "You're on!":
            pf "How about we raise the stakes?"
            show shou mis at cc
            voice "audio/voice/E2/Free/SS/23.ogg"
            ss "I like the sound of that. What are you thinking?"
            pf "Loser buys the winner lunch for a whole week."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/24.ogg"
            ss "I never took you for a gambling man…"
    
            menu:
                "It keeps things spicy.":
                    pf "It keeps things interesting."
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/25.ogg"
                    ss "Alright, then. May the best man win!"
    
                "I'm feeling lucky.":
                    pf "I know lady luck is on my side!"
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/26.ogg"
                    ss "Well, you're going to be disappointed since she's got my back tonight!"
    
                "It's not gambling when the results are already known.":
                    pf "It isn't gambling if I know I'm going to win."
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/27.ogg"
                    ss "Oh ho ho, let's see how confident you are after this!"
    
    
    #SFX digital shooting
    hide shou with dissolve
    "We throw a couple of tokens into the machine. Once the game loads, we jump straight into the action. Shou takes the lead… {w}and leads us straight into an enemy encampment."
    
    if E2SSS1_Coop == 1:
        pf "We'll need to work together to take this wave."
        show shou smi at cc with dissolve
        voice "audio/voice/E2/Free/SS/28.ogg"
        ss "Roger!"
        show panic:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou ner at cc
        voice "audio/voice/E2/Free/SS/29.ogg"
        ss "Er-- Uh oh."
        "Shou is quickly overwhelmed by the sheer number of enemy forces."
        show shou wor at cc
        voice "audio/voice/E2/Free/SS/30.ogg"
        ss "I need some cover fire!"
        pf "On it!"
        hide shou with dissolve
        "I concentrate on my aim and successfully free Shou so he can run for cover. Once he's settled, the two of us work closely to take out the rest of the team."
        "{i}New High Score!{/i}"
        show shou sur at cc with dissolve
        voice "audio/voice/E2/Free/SS/31.ogg"
        ss "Wow, we set the new high score?! I'm surprised how easy that was."
        pf "That's what happens when you have solid teamwork."
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/32.ogg"
        ss "True that, broseph!"
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        "He prompts a fist and I bump it."
    
    else:
        show shou ske at cc with dissolve
        voice "audio/voice/E2/Free/SS/33.ogg"
        ss "You're falling behind broseph--"
        show shou sur at cc
        voice "audio/voice/E2/Free/SS/34.ogg"
        ss "Ack!"
        "A large wave of enemies spawn on Shou's side."
        show panic:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou wor at cc
        voice "audio/voice/E2/Free/SS/35.ogg"
        ss "Ah, crap. I’m pinned! Give me some cover!"
    
        menu:
            "Help Shou.":
                hide shou with dissolve
                "It's still a team game."
                pf "Alright, I'm going in!"
                "I take out the shooters pinning him down."
                show shou hap at cc
                voice "audio/voice/E2/Free/SS/36.ogg"
                ss "Whew. I knew you’d pull through. Time to finish off this wave."
                pf "Yep."
                "We clear the game, however we weren't fast enough to make the leaderboard. {w}Maybe if we hadn't spent the beginning competing it might have been different."
                show shou smi at cc
                show note:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/Free/SS/37.ogg"
                ss "Not bad."
                pf "Yeah."
    
            "Nope.":
                "My character dives for cover."
                pf "Every man for himself."
                show shou sur at cc
                voice "audio/voice/E2/Free/SS/38.ogg"
                ss "You can't abandon another broseph!"
                pf "There's a week of free lunch riding on this."
                show shou wor at cc
                voice "audio/voice/E2/Free/SS/39.ogg"
                ss "Nooooooooooooooooooooooooo!"
                # fail sfx?
                "Shou’s screen flashes \"GAME OVER\"."
                show shou sad at cc
                show crying:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/Free/SS/40.ogg"
                ss "Et tu, bro-te?"
                "I merely smirk. {w}Once it seems the coast is clear, I peek out from my hiding spot and get wrecked by an enemy sniper."
                # fail sfx?
                "{i}GAME OVER!{/i}"
                show shou hap at cc
                voice "audio/voice/E2/Free/SS/41.ogg"
                ss "Haha! Karma!"
                "I shrug."
                pf "At least I still get free food."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/42.ogg"
                ss "No sir. Don't you see \"GAME OVER\" across your screen?"
                pf "Welching on our bet?"
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/43.ogg"
                ss "Nope, the deal was the loser pays for the winner. We're both losers."
                pf "I guess {i}technically{/i} speaking that's true…"
                
    hide shou with dissolve
    "After our shooting match, we head for the GEAR simulators."
    voice "audio/voice/E2/Free/SS/44.ogg"
    ss "Aww, no way!"
    "There's a long line which snakes around some of the other gaming stations."
    show shou thi at cc with dissolve
    voice "audio/voice/E2/Free/SS/45.ogg"
    ss "Well, I guess I should’ve expected this."
    pf "Why are there so many people?"
    show shou neu at cc
    voice "audio/voice/E2/Free/SS/46.ogg"
    ss "It’s because of the new update to the simulators."
    pf "Update?"
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/47.ogg"
    ss "The arcade has new prototype weapons by Aludian Enterprises installed into the sim."
    pf "Huh, I wonder what kind of weapons..."
    show shou hap at cc
    voice "audio/voice/E2/Free/SS/48.ogg"
    ss "Not sure, but I can't wait to find out!"
    
    pf "You’re pretty excited about this."
    show drop:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "He scratches his head and wears a sheepish grin."
    voice "audio/voice/E2/Free/SS/49.ogg"
    ss "Heh, yeah, it’s because I really do like GEARs."
    pf "What got you into them in the first place?"
    stop music fadeout 10
    show shou cur at cc
    voice "audio/voice/E2/Free/SS/50.ogg"
    ss "Oh… um…"
    show shou thi at cc
    "Shou looks like he's struggling to find the words."
    show shou neu at cc
    voice "audio/voice/E2/Free/SS/51.ogg"
    ss "No, it's stupid."
    pf "I'm sure it's not. You can tell me."
    show dots:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "It's strange to see him look so serious. {w}After a few more seconds of hesitation, Shou finally speaks."
    show shou thi at cc
    play music "audio/music/Kaori Itami (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/Free/SS/52.ogg"
    ss "...I… I got beat up a lot as a kid."
    
    "Now I feel like a jerk."
    pf "I didn’t know."
    show shou neu at cc
    "He takes a deep breath."
    voice "audio/voice/E2/Free/SS/53.ogg"
    ss "I was always the one being picked on in class or after school. That's why I hung out alone a lot."
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/54.ogg"
    ss "Then one year, my mom bought me this sweet GEAR action figure for my birthday! Man… I loved that thing. It was so awesome!"
    show shou sad at cc
    voice "audio/voice/E2/Free/SS/55.ogg"
    ss "But the kids from my class… they pulled it from my hands and laughed as the leader smashed it against the concrete."
    pf "Oh man…"
    show shou win at cc
    voice "audio/voice/E2/Free/SS/56.ogg"
    ss "I sat there, my eyes red from crying, and I thought… if only I had a real GEAR…"
    
    if MCStory == 3:
        stop music fadeout 3
        pf "Uh huh, and is this the part where you tell me your father was the mastermind behind it all. He did it to make you stronger."
        $renpy.pause(1)
        show shocked:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        show shou sur at cc with dissolve
        voice "audio/voice/E2/Free/SS/57.ogg"
        ss "How did you know?!"
        show shou ske at cc
        "Shou looks at me with amazement."
        show shou mis at cc
        voice "audio/voice/E2/Free/SS/58.ogg"
        ss "Nothing gets past you, huh?"
    
    else:
        pf "Shou… I’m sorry."
        show shou thi at cc
        "He doesn’t face me. If I had known this was such a sensitive topic, I wouldn’t have brought it up."
        voice "audio/voice/E2/Free/SS/59.ogg"
        ss "No, it’s good to finally talk about it, you know?"
        stop music fadeout 5
        show shou win at cc
        "Suddenly, his body starts shaking."
        pf "Are you alright? Look, I didn’t mean to bring up--"
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/60.ogg"
        ss "pfft…"
        pf "Wait… don’t tell me…"
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/SS/61.ogg"
        ss "Pffft ahaha! I can't believe you fell for it! Hahaha!"
    
        menu:
            "Okay, you got me.":
                pf "This will never be spoken of again."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/62.ogg"
                ss "You wish! This is way too good to keep to myself!"
                pf "You're never going to let me live this down, are you?"
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/63.ogg"
                ss "Nope!"
    
            "Give me back my sympathies.":
                pf "I take back every nice thing I just said."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/64.ogg"
                ss "Haha! I'm sorry! It was just too good to resist!"
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/65.ogg"
                ss "Maybe I should give up my piloting career to be an actor."
                pf "Don't push it."
    
            "I'm going to get you back one day.":
                pf "This means war."
                show shou mis at cc
                voice "audio/voice/E2/Free/SS/66.ogg"
                ss "Haha, it was just a joke! Come on!"
                pf "No, no. You started it and I'm going to end it."
                show shou smi at cc
                voice "audio/voice/E2/Free/SS/67.ogg"
                ss "Ha! You can try, but everyone knows the Shouster can out-prank anyone!"
    
    pf "So, what’s the real story?"
    show shou neu at cc
    "Shou shrugs."
    show shou thi at cc
    voice "audio/voice/E2/Free/SS/68.ogg"
    ss "There isn't one. There's just… a feeling, you know? Being inside the cockpit, your hands on the control panels, and the only thing you see out of your visuals is down the barrel of your opponent’s rifle."
    pf "You mean you like the thrill? Didn’t take you for an adrenaline junkie."
    show shou neu at cc
    voice "audio/voice/E2/Free/SS/69.ogg"
    ss "That's not exactly it."
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/70.ogg"
    ss "In a match, everyone is an equal. You could be the son of the president or missing a leg or whatever, and none of that matters. All that matters is if you have what it takes to win."
    pf "Well, matches aren't really equal. If you're the son of the president you could have the best equipped GEAR in the nation which will obviously give you the advantage over the GEAR with average equipment."
    show shou mis at cc
    voice "audio/voice/E2/Free/SS/71.ogg"
    ss "True, which is why matches held between standard GEARs are my favourite. Then it really is based on skill alone."
    "Shou's unusually serious and speaks in earnest. Although he's still smiling, it's not his usual goofy grin."
    "He might come off as someone who doesn't take anything seriously, but after what he just shared, I get the feeling this facade hides a mind that is observant and alert."
    pf "Hmm, interesting."
    show shou thi at cc
    voice "audio/voice/E2/Free/SS/72.ogg"
    ss "I don't share that with a lot of people. I don't think they'd understand."
    show shou hap at cc
    "I don't really know what to say. Luckily, Shou's signature grin returns."
    voice "audio/voice/E2/Free/SS/73.ogg"
    ss "Anyway, good talk!"
    
    menu:
        "You can talk to me anytime.":
            pf "I got your back, bro."
            show shou mis at cc
            voice "audio/voice/E2/Free/SS/74.ogg"
            ss "That's great, because there was something else on my mind..."
            pf "Wow, so soon?"
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            "Shou just laughs."
    
        "See you next session.":
            pf "That will be five hundred credits for this session."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/75.ogg"
            ss "What?" 
            pf "Your next therapy session is scheduled two weeks from now."
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/76.ogg"
            ss "That's pretty pricy. How come I don't get the \"friends and family\" discount?"
            "I just look at Shou who stares blankly at me. Suddenly, his eyes grow wide in understanding."
            show shou sur at cc
            voice "audio/voice/E2/Free/SS/77.ogg"
            ss "You mean we aren't friends?!"
    
        "Yup, no need to repeat it.":
            pf "Okay, then. Now we can focus on the games."
            show shou mis at cc
            "Shou grins and rattles the tokens in his pockets in anticipation."
    
    "The line dwindles as we've been talking, and before we know it, it's our turn."
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/78.ogg"
    ss "Looks like we're next!"
    hide shou with dissolve
    scene black with fade
    "Shou and I take our places inside the simulation pods, and we continue to battle each other until Shou has to leave."
    $ E2SSS1_Completed = 1
    
    stop ambient fadeout 3
    stop music fadeout 3
    $renpy.pause(1)
    #End Scene
