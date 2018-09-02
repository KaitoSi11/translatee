label E1D3S8:
    
    
    if (E1D3S1_BikeDrove == 1):
        $renpy.pause(1)
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadein 1 fadeout 1
        "I head to the parking lot and grab my bike. {w}Then I head home."
        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
        $renpy.pause(2.5)
        jump E1D3S9
    
    elif (E1D3S1_BusRide == 1):
        play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
        "I wait impatiently for the bus. When it pulls up, I climb on and grab an aisle seat."
        "As the bus moves on, I dream of my beautiful bike the entire way home."
        $renpy.pause(1.0)
        jump E1D3S9
    
    elif (E1D3S1_BikeImpounded == 1):
        play ambient "audio/ambience/Campus.ogg" fadein 1 fadeout 1
        scene bg campus main day with fade
        "The thought of riding the bus back home turns my stomach. If only I had my bike--"
        "I quickly check the time. Still a couple hours before closing. I can make it to the impound in time to get my bike back."
        stop ambient fadeout 3
        $renpy.pause(1)
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1 fadeout 1
        scene bg campus parking day with fade
        "I hustle to the parking lot and head straight for the security building. The same guard from before yawns as he watches a series of cameras. He glances at me as I approach and grunts in recognition."
        play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 1 fadeout 1
        show guard extra at cc with dissolve
        voice "audio/voice/E1/D3/S8/Guard/1.ogg"
        gua "Illegal parker. You're back."
        pf "Yeah… I'd like to pick up my bike."
        "He nods."
        voice "audio/voice/E1/D3/S8/Guard/2.ogg"
        gua "100 credits."
    
        menu:
            "Have my arm and leg while you're at it.":
                pf "That's extortion! There's no way it can cost this much!"
                voice "audio/voice/E1/D3/S8/Guard/3.ogg"
                gua "That's how much it costs."
                pf "But my bike was only in the lot for one night!"
                voice "audio/voice/E1/D3/S8/Guard/4.ogg"
                gua "Do you want your vehicle or not?"
                pf "Fine."
                "I clench my jaw but wire the credits anyway."
    
            "I'll give you 50 credits.":
                "I wire over 50 credits."
                play sound "audio/sfx/Technology/Payment Beep Failure.ogg"
                "His computer beeps in recognition of the transaction. The guard glances at the screen, then scowls."
                show dots:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                "I smirk at him."
                pf "Keep the change."
                voice "audio/voice/E1/D3/S8/Guard/5.ogg"
                gua "What kind of crap is this? It's 100 credits."
                pf "Yeah, and I sent over the credits."
                voice "audio/voice/E1/D3/S8/Guard/6.ogg"
                gua "But you still owe another 50 credits."
                pf "Such a generous tip and you still want more?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Guard/7.ogg"
                gua "I don't have time for your games."
                "He starts to turn away from me, when I wire over another 50 credits."
                pf "Geez, loosen up."
    
            "Just pay it.":
                "Let's just get this over with. I grumble to myself, but wire over the credits."
    
        play sound "audio/sfx/Technology/Payment Beep Success.ogg"
        "His computer beeps once the transaction has been approved and prints out a receipt. He offers it for me to sign, and I do."
        voice "audio/voice/E1/D3/S8/Guard/8.ogg"
        gua "You've got to go to the lot."
        pf "The lot?"
        voice "audio/voice/E1/D3/S8/Guard/9.ogg"
        gua "It's past the off-campus parking. There's a metal fence surrounding it. Even you won't be able to miss it."
        "He smirks at me, and I try not to show my irritation."
        pf "Thanks."
        "I turn to leave, but he stops me."
        show question:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Guard/10.ogg"
        gua "Aren't you forgetting something?"
        pf "What?"
        voice "audio/voice/E1/D3/S8/Guard/11.ogg"
        gua "The passcodes."
        "He hands me a copy of the receipt. There are two series of numbers scribbled on there."
        pf "Oh, right."
        "He points to one code, then the other."
        voice "audio/voice/E1/D3/S8/Guard/12.ogg"
        gua "Type this code to get into the impound, and type this code into the lock on your bike."
        pf "Got it, thanks."
        stop music fadeout 3
        hide guard extra with dissolve
        scene bg campus impound day closed with fade
        "I leave quickly and head in the direction of the lot. Once I get closer, I can easily spot the fence. There's an electronic lock on the gate."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Technology/Passcode Entry.ogg"
        "As I type in the passcode for the impound, I glance around, checking if there's a guard here, but I'm all alone."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Impacts/Impound Gate Open.ogg"
        scene bg campus impound day with Dissolve(2.5)
        "The gate opens with a sharp screech, temporarily cutting a rift in the otherwise silent air, and I walk in."
        
        "There are very few vehicles in the lot and I almost immediately spot my bike."
        ##NEW SOUND NEEDED##play sound "audio/sfx/Technology/Wheel Lock - Locking.ogg" fadeout 5
        "There's a wheel lock on my back tire, and I type the second code into the side panel. {w}It flashes green and unlocks with an echoing click."
        play music "audio/music/A Bad Feeling (GAME VERSION).ogg" fadein 1
        "I eagerly wheel my bike out of the lock and back towards the gate. {w}As I head out of the impound, I walk straight into the bully from yesterday, who is flanked on either side with two equally mean looking guys."
        show bully3 extra at cc with dissolve
        show bully extra at l3 with dissolve
        show bully2 extra at r3 with dissolve:
            xzoom -1
            
        menu:
            "Where the hell did you come from?!":
                "I move my bike to the side before returning to face them."
                pf "What are you doing here?"
                voice "audio/voice/E1/D3/S8/Ken/1.ogg"
                kt "We've been waiting for you."
                pf "... You mean you've been here this whole time?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/2.ogg"
                kt "Shut up!"
                "He motions for his friends, who slowly surround me. They loom over me and crack their knuckles ominously."
                pf "Three on one? The odds are still in my favour…"
    
            "Come at me, bro.":
                "I move my bike to the side before returning to face them. I roll my neck and crack my knuckles, then grin."
                pf "Didn't get enough the first time, I see. You ready to get your ass whooped again?"
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/3.ogg"
                kt "Tch, you won't be so smug once we're done with you."
                "He motions for his friends, who slowly surround me. They loom over me, and crack their knuckles ominously."
                pf "Well this should be entertaining."
    
            "Pretend they aren't there and push past them.":
                "I barely even glance at them, and when the two friends try to block my path, I wheel my bike over the toes of the nearest guy. He yelps in pain and grabs his feet, while the other guy stoops to help him."
                show question:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/4.ogg"
                kt "What the hell do you think you're doing?!"
                pf "Going home."
                show vein:
                    xoffset 675
                    yoffset 50
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D3/S8/Ken/5.ogg"
                kt "We're not finished here!"
                "He puts his hands on my bike to stop me."
                "I freeze. {w}A small twitch escapes me."
                "I calmly hop down from my bike and wheel it to the side. Then I walk straight up to the bully and punch him squarely in the jaw."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                pf "Touch my bike again…"
                "He staggers back but catches himself before he falls. He rubs his jaw, and his face flushes red."
    
        "He swings at me, and I--"
        
        $ qtebase = 2
        $ qtetotal = qteath + qtebase
        $ t_var = qtetotal
        show screen timer_scr(place="E1D3S8_QTEFreeze")
    
        menu: 
            "Freeze...":
                $ renpy.hide_screen ("timer_scr")
                label E1D3S8_QTEFreeze:
                    play sound "audio/sfx/Human/light_Punch.ogg"
                    "My legs become rooted to the ground as his fist connects with my stomach."
                    play sound "audio/sfx/Human/light_punch.ogg"
                    "I gasp for air as I try to ignore the throbbing pain in my belly and kick him in the ribs."
                    play sound "audio/sfx/Human/Med_Punch.ogg"
                    "He doubles over, but one of his friends hits me in the back."
                    "A sharp pain renders me temporarily immobile, but I manage to dive out of the way as the two lackeys charge at me. {w}They try to avoid each other, causing one of them to run face-first into the gate. {w}He clutches his face, the blood pouring from his nose."
    
            "Trip...":
                $ renpy.hide_screen ("timer_scr")
                "I try to move out of the way, but lose my footing."
                play sound "audio/sfx/Human/Med_Punch.ogg"
                "He jabs me in the chest, knocking the wind out of me, while one of his lackeys kicks me in the knee."
                play sound "audio/sfx/Human/light_punch.ogg"
                "My leg gives out and I stumble."
                "The second friend tries to kick my ribs, but I twist away in the nick of time. I swipe his legs out from beneath him, and he falls on his back. His head hits the ground with a sickening thump."
    
            "{color=#00ff00}{b}Dodge!{/b}{/color}" if (MCStory == 1):
                jump E1D3S8_MCStory1
            
            "Dodge!" if (MCStory != 1):
                label E1D3S8_MCStory1:
                $ renpy.hide_screen ("timer_scr")
                play sound "audio/sfx/Human/light_punch.ogg"
                "I easily evade his punch, and barely block a punch from his friend. The other assailant charges me, and at the last second, I step out of the way. {w}He skids to a halt, and while he's off-balance, I push him. He collides with the gate with a sickening crack. I stay light on my feet, while the other two circle me."
        
        "The bully glares at me, his face contorted with rage. His leg comes steadily closer to my face, when suddenly, somebody comes between us."
        hide bully extra
        hide bully2 extra
        hide bully3 extra
        with dissolve
        "He screams and falls to the ground as the new figure pushes his leg against the joint. {w}One friend charges the newcomer, who blocks him with impossible speed."
        ##NEW SOUND NEEDED#
        play sound [ "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg", "audio/sfx/Human/light_punch.ogg", "audio/sfx/Human/Med_Punch.ogg" ]
        "He strikes with precision, and pelts the friend with a flurry of punches. {w}The final fist to the jaw brings the attacker to his knees."
        
        pf "Look out!"
        "The newcomer turns just in time to block the bully from striking him in the back of the head. {w}Instead, he twists the bully's arm so he holds him in a wristlock. The bully yelps in pain and immediately freezes."
        voice "audio/voice/E1/D3/S8/Ken/6.ogg"
        kt "Ugh! Let go of me!"
        "He looks up, and suddenly the colour drains from his face."
        voice "audio/voice/E1/D3/S8/Akira/1.ogg"
        am "Only if you promise to leave this guy alone."
        show akira ang at cc with dissolve
        "His friends unsteadily climb to their feet and slowly back away."
        voice "audio/voice/E1/D3/S8/Bully1/1.ogg"
        Bully1 "Shit, is that Akira?"
        show akira ann at cc
        voice "audio/voice/E1/D3/S8/Bully2/1.ogg"
        Bully2 "Looks like it."
        voice "audio/voice/E1/D3/S8/Bully1/2.ogg"
        Bully1 "There's no way I'm getting tangled with him!"
    
        "The bully speaks through gritted teeth."
        voice "audio/voice/E1/D3/S8/Ken/7.ogg"
        kt "Yes, okay, got it."
        stop music fadeout 3
        "The newcomer lets go, and the bully scrambles out of his reach. {w}He collects his friends and leaves quickly."
        scene black with fade
        $renpy.pause(1)
        scene bg campus impound dusk with fade
        $renpy.pause(2.5)
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 1
        show akira wor at cc with dissolve
        $renpy.pause(1)
        show question:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/2.ogg"
        am "Are you okay?"
    
        if (E1D3S5_AkiraNoticedMe == 1):
            "I take a good look at the guy. That white hair looks really familiar…"
            show akira smi at cc with dissolve
            "He smiles at me, and the realization strikes me like lightning."
            pf "You're Akira!"
            show akira hap at cc
            voice "audio/voice/E1/D3/S8/Akira/3.ogg"
            am "Yup, and you're the new transfer student, right?"
            "I blink in surprise."
            pf "Oh, you've heard of me?"
            show akira thi at cc
            voice "audio/voice/E1/D3/S8/Akira/4.ogg"
            am "Sort of. I've heard about the \"American GEAR\"."
            pf "Ah…"
    
        else:
            pf "Yeah, thanks for helping me out."
            "I notice the teal stripes on his uniform. Guess he's a pilot too."
            show akira hap at cc with dissolve
            voice "audio/voice/E1/D3/S8/Akira/5.ogg"
            am "No problem. I know about those guys and they're never up to any good."
            show akira smi at cc
            voice "audio/voice/E1/D3/S8/Akira/5_01.ogg"
            am "I'm Akira."
            pf "I'm [pfirst]."
            show akira hap at cc
            voice "audio/voice/E1/D3/S8/Akira/6.ogg"
            am "Nice to meet you. I only wish it had been under happier circumstances."
            pf "Heh, yeah."
    
        show akira neu at cc
        pf "I hope I don't sound rude, but what exactly are you doing here?"
        "He holds up a similar receipt to mine."
        show akira hap at cc with dissolve
        voice "audio/voice/E1/D3/S8/Akira/7.ogg"
        am "Picking up my bike."
        show akira smi at cc
        pf "Did you park illegally too or something?"
        show akira hap at cc
        "He laughs."
        voice "audio/voice/E1/D3/S8/Akira/8.ogg"
        am "No, I actually have a parking pass."
        pf "Really? Then what's your bike doing in here?"
        show akira thi at cc
        show drop:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/9.ogg"
        am "It's kind of a long story, but you know that surly guard in the lot? He's had it out for me ever since I was a first year. I accidentally parked in a reserved spot without a pass… and it turned out to be \"his\" spot."
        pf "Oh no…"
        show akira smi at cc
        voice "audio/voice/E1/D3/S8/Akira/10.ogg"
        am "Yeah. He's never forgiven me for it. So every so often he claims there was a mix up in the system or something and my bike ends up in here." 
        pf "And you let him get away with it?"
        show akira hap at cc
        "He laughs again."
        voice "audio/voice/E1/D3/S8/Akira/11.ogg"
        am "I'm sure this unusual system glitch will be investigated at some point."
        show akira cur at cc
        voice "audio/voice/E1/D3/S8/Akira/12.ogg"
        am "Anyway, you okay?"
        pf "Yeah, I'll be fine, thanks. And you?"
        show akira smi at cc
        voice "audio/voice/E1/D3/S8/Akira/13.ogg"
        am "I'm fine."
        voice "audio/voice/E1/D3/S8/Akira/14.ogg"
        am "I better get my bike and head home."
        "I nod, and hop on my own bike."
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
        pf "Thanks again for stepping in. I owe you one."
        show akira mis at cc
        show note:
            xoffset 720
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S8/Akira/15.ogg"
        am "Don't worry about it. I'm sure I'll be seeing you around."
        pf "Yeah, see you around."
        hide akira with dissolve
        "He waves and soon disappears among the cars."
        play sound "audio/sfx/Vehicles/Bike Revving.ogg"
        stop music fadeout 3
        "I rev my engine, feeling the familiar rush of adrenaline, and drive out of the lot."
        stop ambient fadeout 3
        play sound "audio/sfx/Vehicles/Bike driving off.ogg"
        $renpy.pause(1)
        scene black with fade
        $renpy.pause(2.5)
    
        jump E1D3S9