label E1D2S2:
    
    play ambient "audio/ambience/Bus Stop.ogg" fadein 1
    scene bg isokaze neighborhood day with fade
    
    "Cars whip by as I approach the bus shelter. {w}There are a few people waiting. I plunge my hands into my pocket and lean against the shelter to wait."
    
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    "A sharp squeal of brakes announces the bus's arrival. A few people trickle off the bus, and I fumble in my bag for my ID."
    scene bg travel bus day with fade
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "As I enter, I tap my ID on the scanner, which responds with an affirmative beep."
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    "Without waiting for me to find a seat, the bus jerks to a start, nearly knocking me over. There aren't too many free seats available, so I stumble unsteadily towards the back of the bus."
    stop ambient fadeout 5
    play ambient "audio/ambience/Bus.ogg" fadein 1
    "As I glance around, I notice that a majority of passengers are wearing ACE Academy uniforms. That's comforting, I suppose."
    "There's a free seat beside a girl my age."

    $ persistent.gpix[61][0] = 1
    $ persistent.gpix[62][0] = 1
    $ persistent.gpix[63][0] = 1
    scene cg yuuna bus meeting1 with dissolve:
        xzoom .5
        yzoom .5
    "She stares intently out of the window and sits with her back uncomfortably straight."
    "Her uniform lacks teal stripes. {w}I guess she's not a pilot."
    
    "She seems pretty cute, so I wonder why there's an empty seat beside her. {w}Maybe she's not that friendly?"
    
    menu:
        "Meh, I'll take my chances. It'd be nice to know at least one person from ACE Academy.":
            $ E1D2S2_talkwithyuunayes = 1
    
        "I'll find another spot.":
            $ E1D2S2_talkwithyuunayes = 0
        
    if (E1D2S2_talkwithyuunayes == 1):
    
        "I fall ungracefully into the seat beside her."
        "We sit in silence as I muster the courage to speak with her. Eventually, she shifts uncomfortably under my gaze, and I clear my throat."
    
        pf "Um, you go to ACE Academy too?"
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
        "I mentally slap myself for choosing such an idiotic question. Obviously she does. That was one of the first things I noticed. To my surprise, she smiles warmly at me."
        scene cg yuuna bus meeting3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/1.ogg"
        ym "Yes, I do."
    
        "She gestures at my uniform."
        scene cg yuuna bus meeting2 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/2.ogg"
        ym "You're in the pilot program? I've heard it's very competitive and difficult to get into."
    
        menu: 
            "Yes.":
                pf "Yes."
                voice "audio/voice/E1/D2/S2/Yuuna/3.ogg"
                ym "… Yes you're in the pilot program? Or yes the program is very difficult to get into?"
                pf "Uh… yes."
                voice "audio/voice/E1/D2/S2/Yuuna/4.ogg"
                ym "Oh… um, okay."
                scene cg yuuna bus meeting1 with dissolve:
                    xzoom .5
                    yzoom .5
                "She waits politely for me to say more, but when I don't, she resumes her gaze out of the window. {w}Every once in a while I catch her glance sideways at me."
    
            "Nah, it was easy!":
                "I wave a hand dismissively."
                pf "I managed to get in without any trouble."
                scene cg yuuna bus meeting3 with dissolve:
                    xzoom .5
                    yzoom .5
                voice "audio/voice/E1/D2/S2/Yuuna/5.ogg"
                ym "Oh, I see."
                "Her smile seems strained."
    
            "It just needs hard work.":
                pf "I think anyone can make it as long as they try."
                scene cg yuuna bus meeting3 with dissolve:
                    xzoom .5
                    yzoom .5
                "She gives me a polite smile."
    
        pf "Right, I didn't catch which program you're in. Or your name, for that matter. I'm [pfull]."
        scene cg yuuna bus meeting3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E1/D2/S2/Yuuna/6.ogg"
        ym "I'm Yuuna, Yuuna Misaki. I'm studying PHPT."
        pf "\"PHPT\"?"
        voice "audio/voice/E1/D2/S2/Yuuna/7.ogg"
        ym "Pilot Health and Physiotherapy."
        stop music fadeout 3
        stop ambient fadeout 5
        "Before I can ask anything else, the bus grinds to a stop."
    
        play sound "audio/sfx/Vehicles/Bus Chime.ogg"
        $renpy.pause(1)
        voice "audio/voice/E1/D2/S2/Bus Announcer/1.ogg"
        "Bus Announcer" "ACE Academy."
        
        scene black with fade
        scene white with fade
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main day with Dissolve(2)
    
        "I hop off the bus and Yuuna follows suit. The roar of the departing bus does not dampen the student chatter. Yuuna pulls out her phone and checks her schedule."
        
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        show yuuna neu at cc with dissolve
        
        label E1D2S2_yuunaloop:
            menu:
                "Ask where her class is.":
                    pf "So, what's your first class?"
                    show yuuna smi at cc with dissolve
                    voice "audio/voice/E1/D2/S2/Yuuna/8.ogg"
                    ym "Introduction to Psychology."
                    pf "Psychology?"
                    
                    voice "audio/voice/E1/D2/S2/Yuuna/9.ogg"
                    ym "Mental health is just as important as physical health. That class is--"
                    "She points over her shoulder towards a towering building in the distance."
                    voice "audio/voice/E1/D2/S2/Yuuna/10.ogg"
                    ym "--all the way over there. What class do you have?"
                    "I check my own phone."
                    pf "Piloting 101."
                    show yuuna sur at cc
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S2/Yuuna/11.ogg"
                    ym "Oh, you're a first year?"
                    pf "No, second. The credit wasn't accepted when I transferred."
                    show yuuna smi at cc
                    voice "audio/voice/E1/D2/S2/Yuuna/12.ogg"
                    ym "Oh, I see. Well, welcome to ACE Academy!"
                    
                    pf "Heh, thanks!"
                    show yuuna hap at cc
                    voice "audio/voice/E1/D2/S2/Yuuna/13.ogg"
                    ym "Well, if there's anything you need help with or if you have any questions, feel free to ask. I pretty much know this campus inside-out."
    
                    menu:
                        "See if she knows how someone gets a parking permit.":
                            $ E1D2S2_YuunaComesWithYouPass = 1
                            "A thought dawns on me."
                            pf "Actually, do you know where I can get a parking permit?"
                            show yuuna smi at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/14.ogg"
                            ym "I do. I can take you there now, actually, since I have some time before class starts."
    
                            pf "Great, that helps a lot! Thanks."
                            show yuuna hap at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/15.ogg"
                            ym "Of course! Follow me."
                            hide yuuna with dissolve
    
                            "Yuuna weaves through the throng of students and it takes most of my concentration not to lose her."
                            "I notice the number of students lounging around the front lawn. I assume those are the upper classmen--the ones who are used to university workings. The students with worried eyes, moving somewhere between a walk and a jog must be first years."
                            scene bg campus building day with fade
                            "Eventually, we pause in front of a grand building… {w}which looks just like the ones we passed. I stare hard at it, trying to find a way to distinguish it from the others."
                            show yuuna neu at cc with dissolve
                            "Yuuna watches me."
    
                            voice "audio/voice/E1/D2/S2/Yuuna/16.ogg"
                            ym "Is everything okay?"
    
                            pf "Huh? Oh, yeah."
                            show yuuna smi at cc
                            voice "audio/voice/E1/D2/S2/Yuuna/17.ogg"
                            ym "Then let's go inside."
    
                            pf "Sure."
                            hide yuuna with dissolve
                            "After sneaking one last look, I follow Yuuna inside."
                            stop ambient fadeout 3
                            scene black with fade
                            "She takes me through a series of hallways before pausing in front of a door marked \"Campus Administration\"."
                            "We both reach for the door at the same time, but I'm faster."
                            "She smiles as I hold the door for her."
                            voice "audio/voice/E1/D2/S2/Yuuna/18.ogg"
                            ym "Oh! Thank you."
                            stop music fadeout 3
                            scene bg campus office day with fade
                            play ambient "audio/ambience/Campus Office.ogg" fadein 1
                            "What would have been a spacious office is instead crowded with irritated students. Only one person mans the desk and he does not look like someone who is particularly accommodating."
                            show yuuna smi at cc
                            "Yuuna points to a row of chairs against the far wall."
                            voice "audio/voice/E1/D2/S2/Yuuna/19.ogg"
                            ym "I'll wait for you over there."
                            pf "Thanks, hopefully this doesn't take too long. If it does, feel free to leave. I don't want you to be late."
                            voice "audio/voice/E1/D2/S2/Yuuna/20.ogg"
                            ym "Don't worry, I have some time."
                            show yuuna hap at cc
                            "She smiles reassuringly before heading over to the seats."
                            hide yuuna with dissolve
                            "I stand in line. {w}As I crane my neck to see the front of the line, I catch the scowl on the administrator's face. He shakes his head, but the student continues to argue with him."
                            "This is going to take a while…"
                            jump E1D2S5
    
                        "Head out on your own.":
                            pf "Good to know, thank you. I think it may be best for me to do some exploring on my own, though."
                            show yuuna smi at cc
                            "She nods in understanding."
                            voice "audio/voice/E1/D2/S2/Yuuna/21.ogg"
                            ym "Sure. I guess I'll see you around, then?"
                            pf "I hope so."
                            hide yuuna with dissolve
                            "She waves goodbye before I lose her in the crowd of students."
                            "I check my phone and notice I still have about an hour before class begins. {w}Should I actually head to class early or should I explore a bit?"
                            jump E1D2S4
    
                "I have to run.":
                    
                    pf "I should probably head to class. I don't want to get lost on my first day." 
                    show yuuna smi at cc
                    "She nods in understanding."
                    voice "audio/voice/E1/D2/S2/Yuuna/21.ogg"
                    ym "Sure. I guess I'll see you around, then?"
                    pf "I hope so."
                    hide yuuna with dissolve
                    "She waves goodbye before I lose her in the crowd of students."
                    "I check my phone and notice I still have about an hour before class begins. {w}Should I actually head to class early or should I explore a bit?"
                    jump E1D2S4
    
                "Sooo…" if (E1D2S2_yuunaloopback == 0):
                    $ E1D2S2_yuunaloopback = 1
                    pf "Sooo…"
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna thi at cc with dissolve
                    "I look everywhere but at Yuuna. {w}She shifts awkwardly in her spot, fiddling with a piece of thread on her sleeve. {w}As the seconds tick by, the silence grows increasingly heavy."
                    jump E1D2S2_yuunaloop
                    
    elif (E1D2S2_talkwithyuunayes == 0):
    
        "She doesn't look like she wants to be bothered."
        scene bg travel bus day with fade
        "I make my way to the back of the bus and am lucky enough to find a window seat. I sit down and watch the blur of trees go by."
    
        $renpy.pause(3)
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    
        "My pocket vibrates."
        "It's a reminder to check the email I had sent myself last night. {w}I'd collected all the information I needed for my first day and compiled it into one email for easy access."
        "I scroll through and refresh myself on my class schedule and information. {w}When I click on a location, it pulls up a detailed map of the campus. This could come in handy."
        "I spend the next few minutes studying the different parts of the campus. {w}A red pulsating light indicates the largest buildings, while the smaller ones flash yellow. {w}My classes don't seem to be too far from each other, which is fortunate. Now there's no way I'll get lost."
    
        "..."
    
        "A hotdog stand? {w}I swear these exist on every campus. Although, it's kind of surprising to find one in a Japanese school… and that it's marked on the official map."
    
        play sound "audio/sfx/Vehicles/Bus Chime.ogg"
        $renpy.pause(1)
        voice "audio/voice/E1/D2/S2/Bus Announcer/1.ogg"
        "Bus Announcer" "ACE Academy."

        "I quickly gather my things and shuffle off the bus with the rest of the students."
        
        scene black with fade
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
        scene white with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main day with Dissolve(2)
    
        "The first thing I notice is how clean and well-kept the campus is. {w}It's like walking into a brochure. The trees and hedges are neatly trimmed; not a single leaf is astray. The grass is mowed. Even the architecture shows off clean lines and designs. {w}I loved CINY, but it could have used a few tips on upkeep."
        "I check the time. {w}I have about an hour before class starts. {w}Should I head to class early? The last thing I'd want is to be late to my first class. {w}On the other hand, sitting around in an empty classroom for an hour seems counterproductive. I could be spending that time checking out the different aspects of campus."
    
        jump E1D2S4
