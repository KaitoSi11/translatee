#
label E2KIS2:
    
    $ migGlasses = 0
    $ kaoOut = "sFashion"
    
    
    #Event 2 - Evening Choice (>50 Points)
    
    "I'm finally done with classes for the day! {w}For some reason, I'm strangely tired and don't feel much like hanging around campus. I'll go home and rest up."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Parking Lot.ogg" fadein 3
    scene bg campus parking dusk with fade
    
    "I walk to the parking lot and spot my bike where I left it. As soon as I reach it, a sleek white car pulls up and blocks the exit. The car has tinted windows and looks like something way out of my price range. As I can only see the back of the car, I guess that it might be a Panther."
    
    "Although the engine is still running, there's no movement from the car. {w}That's kind of weird. Are they waiting for someone? If so, I wish they'd pick a different spot. How am I supposed to leave if they're blocking the exit? Besides, wouldn't it make more sense to pick someone up closer towards campus and not in the heart of the parking lot?"
    
    stop music fadeout 5
    "I hop on my bike as I ponder these questions. Just as I'm about to back out, the passenger door opens, and a smooth leg steps out. Following the leg is a cute girl with red hair… Wait a minute!"
    show kaori neu at r1:
    show miguel neu at r3:
        xoffset 150
    with dissolve
    
    
    "That's Kaori!"
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    menu:
        "Duck out of the way!":
            "I hop back off my bike and hide behind a parked car. The last thing I need is for Kaori to see me and accuse me of spying on her!"
            "... Which I guess is what I'm technically doing anyway."
            "The driver's side door opens and an older man steps out. He looks European… definitely not Japanese. I guess he's in his mid-thirties, and I can tell he keeps in shape by the way his shirt clings to his biceps. He reaches into the back of the car and hands Kaori a bag. {w}With a wide smile, he envelopes her into a hug. I wait for the inevitable slap, but it never happens. Instead, Kaori accepts the hug without protest."
            "That can't be right! {w}I emerge from behind the car and walk back to my bike to get a better look."
    
        "Stay still.":
            "I pause on my bike, ready to watch the scene unfold. I'm far enough away that Kaori won't spot me."
            "The driver's side door opens and an older man steps out. He looks European… definitely not Japanese. I guess he's in his mid-thirties, and I can tell he keeps in shape by the way his shirt clings to his biceps. He reaches into the back of the car and hands Kaori a bag. {w}With a wide smile, he envelopes her into a hug. I wait for the inevitable slap, but it never happens. Instead, Kaori accepts the hug without protest."
            
    
    "How is she so calm right now? She's even smiling back at him!"
    "He tries to linger in the hug, but Kaori gently pulls away and waves goodbye to him. The man waves back as he returns to his car and drives off."
    
    hide miguel
    hide kaori
    with dissolve
    
    "As she heads back toward the campus, her path leads her straight to my parked bike."
    
    show kaori neu at cc with dissolve
    
    pf "Hey, Kaori."
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori cur at cc
    "She jumps slightly at my voice."
    show kaori ske at cc
    voice "audio/voice/E2/Free/KI/20.ogg"
    ki "Oh, it's you."
    "She glances behind her and sighs with relief when the white car is nowhere in sight."
    show kaori neu at cc
    voice "audio/voice/E2/Free/KI/21.ogg"
    ki "What are you doing here?"
    
    menu:
        "I was on my way home.":
            pf "Just picking up my bike so I can go home."
            show kaori cur at cc
            voice "audio/voice/E2/Free/KI/22.ogg"
            ki "Oh. Right, of course."
            pf "What about you?"
            show kaori neu at cc
            voice "audio/voice/E2/Free/KI/23.ogg"
            ki "Heading to my dorm."
    
        "I could ask you the same thing.":
            pf "I think the better question is, what are {i}you{/i} doing here?"
            show kaori dis at cc
            "Kaori crosses her arms."
            voice "audio/voice/E2/Free/KI/24.ogg"
            ki "I asked you first."
            pf "But I know your answer will be more interesting than mine."
            show kaori ann at cc
            voice "audio/voice/E2/Free/KI/25.ogg"
            ki "You're wrong. I'm just going to my dorm."
    
        "Nothing.":
            pf "I'm not doing anything."
            pf "What are you doing here?"
            show kaori dis at cc
            voice "audio/voice/E2/Free/KI/26.ogg"
            ki "Also nothing."
            "I raise an eyebrow."
            pf "That's why you're in a parking lot?"
            show kaori ann at cc
            voice "audio/voice/E2/Free/KI/27.ogg"
            ki "No! I'm going to my dorm."
    
    pf "Oh, okay. What were you up to today?"
    show kaori ske at cc
    voice "audio/voice/E2/Free/KI/28.ogg"
    ki "Does it matter?"
    pf "I'm just curious. I want to learn more about you."
    
    ### NOTE Points - "IF high points with Kaori:"
    # temporarily set to 0
    if kaoromance > 0:
        show kaori neu b1 at cc with dissolve
        "Her expression softens slightly and I think I see a faint blush of pink on her cheeks."
    else:
        show kaori neu at cc
    voice "audio/voice/E2/Free/KI/29.ogg"
    ki "It's nothing. Just a thing I went to."
    
    if MCStory == 3:
        "Hm, Kaori is being really evasive. While I'm curious as to who that man was, it's obvious she doesn't want to talk about it."
    
    menu:
        "Continue to pry.":
            pf "Uh huh… and did you go to this \"thing\" alone?"
            show kaori ske at cc with dissolve
            "Kaori looks sharply at me and her body tenses."
            voice "audio/voice/E2/Free/KI/30.ogg"
            ki "Why?"
            pf "No reason… Just that you and your ride seemed pretty close."
            show drop:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori neu at cc
            "Kaori's face turns white but her voice stays level."
            voice "audio/voice/E2/Free/KI/31.ogg"
            ki "I don't know what you're talking about."
    
            menu:
                "I'm worried about you.":
                    $ E2KIS2_Response = "Worry"
                    pf "Kaori, who was that guy?"
                    show kaori dis at cc
                    "Kaori gets defensive."
                    voice "audio/voice/E2/Free/KI/32.ogg"
                    ki "No one."
                    pf "He looked a lot older than you."
                    show vein:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E2/Free/KI/33.ogg"
                    ki "So?"
                    pf "Are you in trouble? Why is a guy twice your age hanging around--"
                    show kaori ann at cc
                    voice "audio/voice/E2/Free/KI/34.ogg"
                    ki "I don't have have to explain myself to you."
            
                "Oh ho ho, Kaori has a boyfriend~!":
                    $ E2KIS2_Response = "Boyfriend"
                    pf "I knew there had to be a reason you were able to resist my manly charm."
                    show kaori dis at cc
                    "She narrows her eyes."
                    voice "audio/voice/E2/Free/KI/35.ogg"
                    ki "What?"
                    pf "You're into the more {i}mature{/i} types."
                    show question:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    show kaori ske at cc
                    voice "audio/voice/E2/Free/KI/36.ogg"
                    ki "Huh?"
                    pf "You know, someone who's been around the block once or twice."
                    show kaori sur at cc with dissolve
                    "She pauses, then her mouth drops open in shock."
                    show kaori ang at cc
                    voice "audio/voice/E2/Free/KI/37.ogg"
                    ki "You're such an idiot!"
                    show kaori ann at cc
                    pf "You don't have to be embarrassed. It's only natural that {i}needs{/i} come up--"
                    show vein:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    show kaori ang at cc
                    voice "audio/voice/E2/Free/KI/38.ogg"
                    ki "Shut up! It's not like that!"
                    show kaori ann at cc
                    pf "Then what is it like?"
            
                "Is he a family friend?":
                    $ E2KIS2_Response = "Family"
                    pf "It's weird to see a guy that old hanging around a girl your age."
                    show kaori dis at cc
                    voice "audio/voice/E2/Free/KI/39.ogg"
                    ki "Then don't look. Nobody asked for your opinion."
                    pf "Do your parents know him or something? You seem to trust him easily."
            
            voice "audio/voice/E2/Free/KI/40.ogg"
            ki "It's none of your business, so just drop it."
            "Kaori seems snappier than usual. I must have hit a nerve."
            stop music fadeout 5
            pf "Okay, I'm sorry--"
            show kaori neu at cc
            voice "audio/voice/E2/Free/KI/41.ogg"
            ki "Whatever, it's fine. I need to go though."
            pf "Yeah, okay. I'll see you later."
            hide kaori with dissolve
            "She barely waves goodbye and heads towards the campus dorms."
    
        "Leave it alone.":
            $ E2KIS2_Response = "Relax"
            stop music fadeout 5
            "I should respect Kaori's privacy and trust that she'll tell me when she's ready."
            pf "Okay, if you say so."
            show kaori smi at cc with dissolve
            "She nods."
            voice "audio/voice/E2/Free/KI/42.ogg"
            ki "I'm going now. I'll see you later."
            pf "Yeah, later."
            hide kaori with dissolve
    
    "Hm, I wonder what that was all about…"
    scene black with dissolve
    "As soon as Kaori is out of view, I kick my bike into gear and head home."
    $ E2KIS2_Completed = 1
    stop ambient fadeout 3
    $renpy.pause(1)
    
    #end

