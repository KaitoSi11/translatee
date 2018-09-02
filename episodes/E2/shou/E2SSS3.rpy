#
label E2SSS3:
    
    #Event 3 
    $ shoOut = "sCasual"
    
    pf "Maybe I’ll see what Shou’s up to right now."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    "I dial his number but he doesn't pick up."
    "Hm, he must be busy. I’ll just--"
    play sound "audio/sfx/Technology/Phone Alarm.ogg"
    "The phone rings as Shou calls me back."
    stop sound
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1)
    # then voice
    voice "audio/voice/E2/Free/SS/104.ogg"
    ss "Hey! Sorry about that, broseph."
    pf "Don’t sweat it."
    # sfx? could grab a car shop sfx and then put the phone edit on top
    "There are loud whirrings and bangings on Shou's end of the line."
    pf "Uh, you busy right now or something?"
    voice "audio/voice/E2/Free/SS/105.ogg"
    ss "Kind of. I'm at the shop."
    pf "Uh, like a grocery store?"
    "Shou laughs."
    voice "audio/voice/E2/Free/SS/106.ogg"
    ss "No, the auto shop! I work here."
    "I didn't know Shou had a job…"
    pf "Oh, I can call you later."
    voice "audio/voice/E2/Free/SS/107.ogg"
    ss "Wait! I've got big news!"
    pf "Hm?"
    voice "audio/voice/E2/Free/SS/108.ogg"
    ss "So this Prince of Arabia guy just pulled into the shop in a car so expensive you could probably trade it for an island!"
    pf "Seriously?"
    voice "audio/voice/E2/Free/SS/109.ogg"
    ss "You won't believe how amazing this car is. You should come check it out!"
    
    menu:
        "To check out a badass ride? Consider me there.":
            $ E2SSS3_Cars = 1
            pf "I’m coming right now!"
            voice "audio/voice/E2/Free/SS/110.ogg"
            ss "Sweet! Just be careful around it, okay?"
            pf "Relax, I’ll be as careful around it as I am around Eagle."
            "Shou laughs."
            voice "audio/voice/E2/Free/SS/111.ogg"
            ss "I've seen what Eagle looks like after a match..."
            pf "Okay, bad example."
    
        "Think the Prince will mind us taking it for a spin?":
            $ E2SSS3_Cars = 1
            pf "You’ll let me have a go at it, right?"
            voice "audio/voice/E2/Free/SS/112.ogg"
            ss "A go?"
            pf "You can’t put a gorgeous car in front of me and expect me not to take it for a ride."
            voice "audio/voice/E2/Free/SS/113.ogg"
            ss "Wha--No! Maybe it was a bad idea to tell you about it after all..."
            pf "Too late, I’m on my way."
            voice "audio/voice/E2/Free/SS/114.ogg"
            ss "Just promise me you won't touch it!"
    
        "I’m not really that interested in cars.":
            $ E2SSS3_Cars = 0
            pf "I drive a motorcycle. Cars aren't really my thing."
            voice "audio/voice/E2/Free/SS/115.ogg"
            ss "Last chance broseph!"
            "I'm not doing much else anyways. And, honestly, what are the chances of me ever seeing a car that expensive in my near future?"
            pf "Alright, I'll be over in a few."
            voice "audio/voice/E2/Free/SS/116.ogg"
            ss "Awesome! See you soon."
            
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene black with fade
    "As soon as we hang up, Shou texts me the address to his workplace. {w}I program it into the GPS in my helmet and head out."
    $renpy.pause(1)
    # garage ambient? hangar might work for now
    #play ambient "audio/ambience/Hangar.ogg" fadein 3
    #fade into detail shop.
    scene bg homekaito garage day with fade
    show shou hap at cc with dissolve
    "I step into the shop and am greeted by Shou's smiling face. He points to the side and I see the car."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    "In the middle of the room is the most expensive Beaugatti I have ever laid eyes on. I've only ever seen the car in video games and pictures. Seeing it in person nearly takes my breath away."
    show shou mis at cc
    voice "audio/voice/E2/Free/SS/117.ogg"
    ss "Can you find your words yet?"
    "I almost forgot Shou was there."
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/118.ogg"
    ss "What do you think?"
    
    if E2SSS3_Cars == 0:
        pf "Yep, that’s a car, alright."
        show shou hap at cc
        "Shou laughs."
        show note:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/SS/119.ogg"
        ss "You aren't fooling me! I know you're impressed."
    
    else:
        pf "Damn, that is one sweet ride!"
        show shou hap at cc
        voice "audio/voice/E2/Free/SS/120.ogg"
        ss "Did I tell you or what?"
        pf "We’re taking it for a spin. Let’s go!"
        show shou cur at cc
        "Shou quickly intervenes."
        show shou neu at cc
        voice "audio/voice/E2/Free/SS/121.ogg"
        ss "Nope. You're a good broseph, but you aren't worth losing my job."
        pf "Not even a little bit?"
        show shou mis at cc
        voice "audio/voice/E2/Free/SS/122.ogg"
        ss "Sorry."
        pf "Aw."
        
    show shou smi at cc
    "We continue to admire the car in silence."
    show dots:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "..."
    show shou cur at cc
    voice "audio/voice/E2/Free/SS/123.ogg"
    ss "What would you do if you had this much money to spend, anyway?"
    show shou smi at cc
    
    menu:
        "Buy myself a girlfriend.":
            pf "Get myself a hot girl!"
            show shou hap at cc
            voice "audio/voice/E2/Free/SS/124.ogg"
            ss "Why am I not surprised?"
            pf "You can’t tell me you wouldn’t do the same."
            show shou mis at cc
            ### VOICE - No "Tsk, tsk." at the beginning
            voice "audio/voice/E2/Free/SS/125.ogg"
            ss "You still have a lot to learn my misinformed, friend. Women are not toys you can buy."
            pf "Don’t tell me…"
            show shou smi at cc
            voice "audio/voice/E2/Free/SS/126.ogg"
            ss "That’s right--"
            pf "You’re batting for the other team?!"
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/127.ogg"
            ss "If by \"other team\" you mean \"defending women-kind\" then yes."
            "I raise an eyebrow."
            pf "What if I said I'd buy you one too?"
            show shou smi at cc
            voice "audio/voice/E2/Free/SS/128.ogg"
            ss "Then you'd be best the broseph a guy could ask for!"
    
        "Upgrade Eagle.":
            pf "I would upgrade Eagle's hardware! Some new weaponry wouldn't hurt either."
            show shou mis at cc
            voice "audio/voice/E2/Free/SS/129.ogg"
            ss "Keeping it simple, I like that. You can also spend some extra cash on tuning."
    
        "Quit school.":
            pf "I would quit school."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/130.ogg"
            ss "Wait, really?"
            pf "Why do I need a degree when I already have a GEAR to pilot and battle in arenas whenever I want? With all that money, I don't need to worry about a job!"
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/131.ogg"
            ss "So you'll live the rest of your life battling away in the arena and spend the money on repairs?"
            pf "Yep."
            show question:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/SS/132.ogg"
            ss "That sounds great?"
            "He doesn't seem convinced."
    
        "Travel.":
            pf "It’d be nice to travel the world."
            show shou hap at cc
            voice "audio/voice/E2/Free/SS/133.ogg"
            ss "Ahh, I feel you. Where would you go?"
    
            menu:
                "France.":
                    pf "I’ve always wanted to go see the Eiffel Tower. Maybe visit the countryside, too."
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/134.ogg"
                    ss "Don’t forget the accent, ma cherie."
                    pf "What."
                    show note:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou hap at cc
                    voice "audio/voice/E2/Free/SS/135.ogg"
                    ss "I am Le Fran~cais!"
                    pf "Don't do that."
    
                "Italy.":
                    pf "Probably to Italy."
                    show shiny:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou cur at cc
                    voice "audio/voice/E2/Free/SS/136.ogg"
                    ss "Really? There’s so much to see in Italy... I wouldn’t know where to start."
                    pf "I'd start with Rome so that I can see the Colosseum."
                    show shou smi at cc
                    voice "audio/voice/E2/Free/SS/137.ogg"
                    ss "To think, thousands of years ago people battled with swords and axes. Now we’re still battling in arenas but in GEARs."
                    pf "Right? Feels like we're going back to our origins."
    
                "China.":
                    pf "China would be nice. I could definitely live off of their food for the rest of my life."
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/138.ogg"
                    ss "If you ever visit China, Sichuan is a must go."
                    pf "You've been before?"
                    show shou smi at cc
                    voice "audio/voice/E2/Free/SS/139.ogg"
                    ss "Yup."
                    pf "Lucky! I'll put that down on my list of place to go."
    
                "Back to America.":
                    pf "I think I’d go back to America."
                    show shou cur at cc
                    voice "audio/voice/E2/Free/SS/140.ogg"
                    ss "Back to New York?" 
                    pf "Nah, it'd  be fun to do a road trip around the country, or go vacationing in Hawaii."
                    show shiny:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou sur at cc
                    voice "audio/voice/E2/Free/SS/141.ogg"
                    ss "Hawaii! Hello beautiful babes! If you do go back, you’re not leaving without me."
    
                "Egypt.":
                    pf "I'd go to Egypt to see the pyramids."
                    show bulb:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou cur at cc
                    voice "audio/voice/E2/Free/SS/142.ogg"
                    ss "Oh, don’t forget that big cat thing."
                    pf "You mean the sphinx... ?"
                    show shou hap at cc
                    voice "audio/voice/E2/Free/SS/143.ogg"
                    ss "Yes, the sphinx!"
                    pf "You know the \"big cat thing\" is actually a lion."
                    show shou smi at cc
                    voice "audio/voice/E2/Free/SS/144.ogg"
                    ss "A lion is technically a cat… just a big one!"
    
                "Everywhere.":
                    pf "I can't decide! there are so many places."
                    show shou mis at cc
                    voice "audio/voice/E2/Free/SS/145.ogg"
                    ss "Everyone has a place they want to go to."
                    pf "If I have that much money, what's stopping me from traveling the whole world?"
                    show shiny:
                        xoffset 720
                        yoffset 20
                        xzoom .75
                        yzoom .75
                    show shou cur at cc
                    voice "audio/voice/E2/Free/SS/146.ogg"
                    ss "Oooh, yeah, I'd do that too!"
    
        "Feed my dark addiction...":
            stop music fadeout 1.0
            pf "The money would go to… unspeakable things."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/147.ogg"
            ss "Like what?"
            pf "I said they're unspeakable!"
            show shou ske at cc
            voice "audio/voice/E2/Free/SS/148.ogg"
            ss "Unspeakable? Like something from {i}Fifty Shades of GEAR{/i}?"
            pf "...That is tame in comparison."
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou thi at cc
            voice "audio/voice/E2/Free/SS/149.ogg"
            ss "Yeaaaaaaahhhhhhhhh, I don't think I want to know."
            "I nod."
            show shou smi at cc
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
            pf "Good choice."
    
    
        "Take over the world.":
            pf "The same thing we do every night..."
            show shou cur at cc
            voice "audio/voice/E2/Free/SS/150.ogg"
            ss "What?"
            pf "Take over the world!"
            show dots:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            show shou hap at cc with dissolve
            "Shou stares at me, then starts laughing."
            voice "audio/voice/E2/Free/SS/151.ogg"
            ss "Did you hit your head on your way here?"
            pf "You just don't understand my genius."
    
    
    pf "What would you do if you had this much money?"
    show shou thi at cc
    voice "audio/voice/E2/Free/SS/152.ogg"
    ss "Eh, I really don't know."
    stop music fadeout 5
    pf "No way, everyone has something they want. There must be something."
    show shou neu at cc
    voice "audio/voice/E2/Free/SS/153.ogg"
    ss "That’s the problem isn’t it? Everyone has something they want."
    "Shou's cheerful demeanor changes into something serious."
    pf "Is that so bad?"
    show shou thi at cc
    voice "audio/voice/E2/Free/SS/154.ogg"
    ss "Only when money becomes the only thing on a person’s mind."
    show shou neu at cc
    voice "audio/voice/E2/Free/SS/155.ogg"
    ss "You’d be surprised how many people out there care more about what's in someone’s pockets rather than their hearts."
    $renpy.pause(1)
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    show exclamation:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur at cc
    mec1m "Shou! Time to get crackin’. Get the toolbox, will you?"
    show shou smi at cc
    voice "audio/voice/E2/Free/SS/156.ogg"
    ss "You got it! Alright broseph, I’m going to go back to work. Feel free to check the place out."
    show shou cur at cc
    "He’s about to leave, then pauses."
    show shou mis at cc
    voice "audio/voice/E2/Free/SS/157.ogg"
    ss "Don’t you dare touch the car on your way out!"
    "I throw my hands up in defense."
    pf "I wouldn't dare."
    hide shou with dissolve
    "The shop is full of cars in different states of repair. I wonder if Shou worked on any of these..."
    "Shou picks out a wrench and spanner from the toolbox and goes straight to work. He’s quick with his hands, and there are no traces of hesitation in his movements."
    "It's obvious he's been doing this for a while, and as I continue to watch him, he seems to do good work."
    "Still, it’s getting late and I feel a little awkward hanging around when everyone's busy."
    scene black with fade
    stop music fadeout 5
    "I say my goodbyes to Shou and head home."
    stop ambient fadeout 3
    $renpy.pause(1)
    $ E2SSS3_Completed = 1
    
    #End scene

