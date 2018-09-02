#
label E3D5S3:
    
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    play sound2 "audio/sfx/Technology/Phone Alarm.ogg"
    "My phone rings unexpectedly. It's Valerie."
    stop sound
    stop sound2
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    pf "Hello?"
    voice "audio/voice/E3/D5/S3/valerie/E3D5L1.ogg"
    vb "I've got a surprise for you. Come to the Hangar!"
    pf "What is--"
    # sfx ?
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "She hung up. {w}Of course she hung up. I guess I better go see what's up."
    
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    $renpy.pause(1.5)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    
    "After I swipe myself into the Hangar, I make a beeline to Eagle. Valerie is perched in front of my terminal, but jumps up once she sees me. She moves from the terminal and gestures for me to sit."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    show valerie hap at cc with dissolve
    voice "audio/voice/E3/D5/S3/valerie/E3D5L2.ogg"
    vb "Voilà!"
    "I stare at the scrolling code on the screen. {w}She's got to stop acting like I can read this stuff."
    pf "What is this?"
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L3.ogg"
    vb "It's a manual documentation! It needs to be cleaned up before it can be fully understood though."
    pf "Sooo, you called me over to show me something that's not complete?"
    
    if MCStory == 2:
        show valerie neu
        "Valerie crosses her arms."
        voice "audio/voice/E3/D5/S3/valerie/E3D5L4.ogg"
        vb "I thought you'd be able to appreciate the magnitude of this discovery."
        pf "I'm not trying to downplay the importance of this."
    
    else:
        show storm:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie dis
        "Valerie pouts."
        voice "audio/voice/E3/D5/S3/valerie/E3D5L5.ogg"
        vb "If you were even a little bit technical you'd be able to understand this achievement."
        
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L6.ogg"
    vb "Besides, my script is parsing it as we speak. It'll be done in a few minutes."
    show valerie neu
    "We wait patiently for her program to finish running. I watch as she keeps an eye on her script. She's confident in her program, yet keeps glancing at it, exposing the eagerness beneath her calm demeanor. {w}I can't help but wonder..."
    pf "How did you get into engineering?"
    show valerie ske
    voice "audio/voice/E3/D5/S3/valerie/E3D5L7.ogg"
    vb "Girls can't be engineers?"
    pf "That's not what I said."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie mis
    "Valerie laughs."
    voice "audio/voice/E3/D5/S3/valerie/E3D5L8.ogg"
    vb "It's like a puzzle."
    pf "What?"
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L9.ogg"
    vb "Taking things apart and putting it back together. Finding new ways to piece everything together to make it a better product."
    show valerie hap
    voice "audio/voice/E3/D5/S3/valerie/E3D5L10.ogg"
    vb "The possibilities are endless, even if we can't see all the solutions just yet."
    pf "And you just discovered that by accident?"
    show valerie neu
    "She shrugs and becomes strangely aloof."
    voice "audio/voice/E3/D5/S3/valerie/E3D5L11.ogg"
    vb "Things broke around the house a lot. If I didn't fix it, then it would be broken forever."
    pf "Why not just buy a new one?"
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L12.ogg"
    vb "It always worked fine once fixed. Why spend that extra money?"
    pf "But why did {i}you{/i} have to fix it? Why not your parents?"
    show valerie neu
    "She frowns in disdain."
    show valerie thi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L13.ogg"
    vb "My mom couldn't be bothered with things like that. If the computer broke she'd pretend the problem didn't exist until she needed to use it. Then she'd just go buy a new one because she needed to use it {i}immediately{/i}."
    show valerie neu
    voice "audio/voice/E3/D5/S3/valerie/E3D5L14.ogg"
    vb "Money was alway tight and… That's why I started trying to fix things."
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L15.ogg"
    vb "The first thing I ever properly fixed was my bike. I was fifteen and my neighbor at the time was a young woman at university. She helped me fix it, and when she learned I was interested in this stuff she gave me a bunch of \"How-To\" books for my birthday."
    pf "I guess I was lucky that my dad was pretty handy. He taught me how to take care of my things."
    show valerie mis
    "Valerie grins playfully."
    voice "audio/voice/E3/D5/S3/valerie/E3D5L16.ogg"
    vb "Could have fooled me. EAGLE's always a little worse for wear by the time he gets to me. Isn't that right, EAGLE?"
    "She coos affectionately at my GEAR."
    pf "It's not a puppy…"
    # sfx ?
    show exclamation:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie sur
    "A sharp beep interrupts our conversation. {w}Valerie whips back towards the screen."
    show valerie hap
    voice "audio/voice/E3/D5/S3/valerie/E3D5L17.ogg"
    vb "It's done!"
    show valerie cur
    "Valerie and I both lean to get a better look at the screen. I turn my head to ask her a question when her hair brushes my cheek. It's soft and smells like flowers. I hadn't realised how close we were to each other until now."
    
    if valerieSocialLink >= 4:
        show valerie mis
        "Valerie glances sideways at me and smirks, but doesn't move away. I move a step over as the heat rises in my cheeks."
    
    else:
        show valerie neu
        "Valerie is too focused on the screen to notice." 
    
    "Her slender fingers dance across the keyboard."
    show valerie cur
    voice "audio/voice/E3/D5/S3/valerie/E3D5L18.ogg"
    vb "Oh, this makes a lot of sense..."
    pf "What makes a lot of sense?"
    show valerie neu
    voice "audio/voice/E3/D5/S3/valerie/E3D5L19.ogg"
    vb "Why your core only activated that one time. The function of the core was set to debug mode with a single run instance."
    pf "English please."
    voice "audio/voice/E3/D5/S3/valerie/E3D5L20.ogg"
    vb "The overdrive mode was meant to be used for testing purposes, so it was set to only activate once."
    pf "What does that mean?"
    voice "audio/voice/E3/D5/S3/valerie/E3D5L21.ogg"
    vb "It means if we can figure out how to change this setting and find out the parameters of activation, you could use the overdrive mode on demand!"
    "My eyes widen as I consider the possibilities."
    pf "Are you serious?"
    show valerie smi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L22.ogg"
    vb "Yeah! In theory, anyway."
    "She squints at the code."
    show valerie hap
    voice "audio/voice/E3/D5/S3/valerie/E3D5L23.ogg"
    vb "That's not even the best part. Here are blueprints with algorithms and formulas!"
    pf "What do they say?"
    show valerie cur
    "Valerie puts a finger to her lip."
    show valerie thi
    voice "audio/voice/E3/D5/S3/valerie/E3D5L24.ogg"
    vb "Hm… It seems to be incomplete... but we might be able to use this and a bit of reverse engineering to fill in the gaps. If we can figure this out, we can understand the details of the core!"
    
    menu:
        "Good stuff!":
            pf "You're kind of amazing."
            show valerie mis
            "She grins."
            show heart:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D5/S3/valerie/E3D5L25.ogg"
            vb "About time you noticed!"
    
        "If only women came with a manual too.":
            pf "So, completing this code will help us learn everything we need to know to use my core?"
            show valerie smi
            voice "audio/voice/E3/D5/S3/valerie/E3D5L26.ogg"
            vb "Yes, of course!"
            pf "I wish understanding women were that easy."
            show note:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap
            "She laughs."
            show valerie mis
            voice "audio/voice/E3/D5/S3/valerie/E3D5L27.ogg"
            vb "It is… once you unlock her code."
            pf "That's pretty much impossible."
    
        "Can we have it ready for the next match?":
            pf "When can we have the overdrive mode ready?"
            show valerie neu
            "Valerie taps her lip."
            voice "audio/voice/E3/D5/S3/valerie/E3D5L28.ogg"
            vb "I'm not going to lie, it'll take some time. There's a lot to fill in here."
            show valerie hap
            voice "audio/voice/E3/D5/S3/valerie/E3D5L29.ogg"
            vb "But I'll give it my best!"
    
    "Why did Dad include this function for my core? And why didn't he tell me? I have so many questions and too few answers."
    pf "Let's keep this a secret."
    show valerie cur
    voice "audio/voice/E3/D5/S3/valerie/E3D5L30.ogg"
    vb "A secret?"
    pf "Yeah, there's no point in getting the team's hopes up when we don't even know if this will work. {w}Plus, I don't need anyone snooping around my GEAR."
    show valerie smi
    "I look pointedly at Valerie. She smiles innocently."
    show valerie ske
    voice "audio/voice/E3/D5/S3/valerie/E3D5L31.ogg"
    vb "What? That's what brought us together. Are you saying you wished you'd never met me?"
    pf "Of course not, but one Valerie is more than enough."
    show valerie mis
    "She smirks."
    voice "audio/voice/E3/D5/S3/valerie/E3D5L32.ogg"
    vb "Don't I feel special."
    show valerie neu
    "Valerie gets to work and I watch her for a while. She's working too fast for me to comprehend what she's doing, and I don't want to interrupt her groove to explain it to me."
    "After a few minutes, she glances back at me."
    
    if E3D2S5_Voyeur == 1:
        show valerie ske
        voice "audio/voice/E3/D5/S3/valerie/E3D5L33.ogg"
        vb "You really do like to watch, don't you?"
        pf "Huh?"
        show valerie mis
        voice "audio/voice/E3/D5/S3/valerie/E3D5L34.ogg"
        vb "First it was Shou and Mayu at the beach, now me…"
        pf "I didn't watch them!"
        show shiny:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie hap
        "Her eyes sparkle."
        voice "audio/voice/E3/D5/S3/valerie/E3D5L35.ogg"
        vb "So you just like watching me then? Too bad this isn't that interesting..."
    
    else:
        show valerie ske
        voice "audio/voice/E3/D5/S3/valerie/E3D5L36.ogg"
        vb "How about you sit in this chair and I'll watch you work?"
        "I guess she doesn't like me looking over her shoulder. I don't blame her. I hate that too."
        pf "I'll just give you some space then."
        show valerie smi
        "She turns back to the terminal."
        voice "audio/voice/E3/D5/S3/valerie/E3D5L37.ogg"
        vb "Thanks, I'll let you know once I'm done."
        
    hide valerie with dissolve
    stop music fadeout 5
    "After saying goodbye, I leave her to do her thing."
    
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    "I've still got some time before I head home tonight. What do I feel like doing?"
    
    #Evening Choice
    
    $ freeTime = "evening"
    call E3FreeTime from _call_E3FreeTime_6
    
    jump E3D5S4
