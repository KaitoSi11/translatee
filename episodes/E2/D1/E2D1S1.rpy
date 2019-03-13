label E2D1S1:

    $ day = 1
    $ timeSpent = "none"
    #fade in
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 3
    "My alarm awakens me and I go through the routine of getting ready for the day."
    stop ambient fadeout 5
    scene black with fade
    $renpy.pause(1)
    "Никки уже была внизу, и после быстрого завтрака мы оба пошли в школу."
    scene bg campus auditorium day with fade
    #play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    $renpy.pause(1)
    "My class today is a little different from usual. {w}Students sit scattered around the room, but as I walk past them to find a seat, I overhear snippets of conversations in different languages. Like me, they're all foreign to Japan. {w}I settle into a seat at the back of the class, far from the entrance, and gaze out the window while I wait for the professor to enter."
    stop music fadeout 3
    "Suddenly, the room quiets down. {w}I glance at the door, expecting to see the professor, but a girl with bright blue eyes and blonde hair is there instead."
    
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    $ renpy.pause(.5)
    
    $ persistent.gpix[51][0] = 1
    $ persistent.gpix[52][0] = 1
    $ persistent.gpix[53][0] = 1
    show cg valerie classroom intro1:
        alpha 0
        xzoom .55
        yzoom .55
        xoffset -100
    
    show cg valerie classroom intro1:
        parallel:
            easein 3.0 alpha 1.0
        parallel:
            easein 3.3 xoffset -0
        
    
    $ renpy.pause(3.5)
    
    "Although she has her hip cocked to the side, she still carries a commanding presence. {w}All eyes are focused on her, but she doesn't even blink at the attention."
    
    $ renpy.pause(.25)
    
    show cg valerie classroom intro2 with dissolve
    
    $ renpy.pause(.33)
    
    show cg valerie classroom intro3 with dissolve
    
    $ renpy.pause(.33)
    
    "She scans the room, and when her gaze settles on me, she flashes me an excited grin."
    
    

    "I overhear the two guys next to me commenting about her."

    voice "audio/voice/E2/D1/S1/stu6m/1.ogg"
    stu6m "Who is that girl?"
    voice "audio/voice/E2/D1/S1/stu5m/1.ogg"
    stu5m "She must be new. I would have remembered a hottie like her."
    "I can feel the heat of everyone's glares as she steadily makes her way towards me."
    voice "audio/voice/E2/D1/S1/stu6m/2.ogg"
    stu6m "Hey--she's coming our way!"
    voice "audio/voice/E2/D1/S1/stu5m/2.ogg"
    stu5m "C-Could it be? Is she coming to us?"
    "Whispers float behind her, but she ignores them and sits in the empty desk beside me."
    
    hide cg valerie classroom with Dissolve(1.5)
    
   
    
    $ renpy.pause(1.0)
    
    show valerie smi at cc:
        xzoom 1
    with dissolve
    
    $ renpy.pause(.33)
    
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO1.ogg"
    vb "Hey, how's it going?"
    "I wait for the other guys to answer, but they whisper to each other instead."
    voice "audio/voice/E2/D1/S1/stu5m/3.ogg"
    stu5m "Who's that guy? Does she know him?"
    voice "audio/voice/E2/D1/S1/stu6m/3.ogg"
    stu6m "She must. Why else would she search him out?"
    voice "audio/voice/E2/D1/S1/stu5m/4.ogg"
    stu5m "You're right. She's way out of his league."
    "She continues to stare at me, waiting expectantly."

    menu:
        "She must be talking to me...":
            pf "Uh, good… And you?"
            show valerie hap at cc
            show note:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO2.ogg"
            vb "Better, now that I've found you!"
            pf "...You were looking for me?"
            show valerie mis at cc
            "She merely smirks."

        "I'm such a chick magnet.":
            pf "Great, now that you're here."
            "I flash her an equally charming smile."
            show valerie smi at cc
            show note:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO3.ogg"
            vb "Of course I'm here. I would never miss a chance to speak to you."
            "Huh, was she looking for me?"

        "I don't know her. She can't be talking to me.":
            "I look away from her, confident she hadn't directed that question at me."
            pf "..."
            show dots:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            "After a moment, she touches my arm."
            show valerie cur at cc
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO4.ogg"
            vb "Hey."
            pf "Huh?"

    pf "Do we know each other?"
    show valerie hap at cc
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO5.ogg"
    vb "No, but I saw you at the qualifiers."
    pf "You did?"
    show valerie smi at cc
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO6.ogg"
    vb "Yeah, I watched you take out those two AIs by yourself."
    pf "Ah, right."
    "She leans in closer to me, and her voice takes on a breathy tinge."
    show valerie mis at cc
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO7.ogg"
    vb "You were really impressive. I've never seen anybody's core do that before."

    menu:
        "Thank You.":
            pf "T-Thanks..."
            show valerie cur at cc
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO8.ogg"
            vb "How did you do it?"
            pf "W-Well, actually, I--"

        "I can do a lot more with my 'core'.":
            pf "That's not the most impressive thing about my core either."
            show valerie cur at cc
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO9.ogg"
            vb "No?"
            pf "Some might say that it's larger than average."
            "She places a finger to her lip and smirks."
            show valerie mis at cc
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO10.ogg"
            vb "That doesn't sound very comfortable for the frame."

        "Ok.":
            "I immediately lean back when she leans in. Why is she getting so close?"
            pf "Yeah, everyone was surprised by my core."
            show valerie cur at cc
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO11.ogg"
            vb "So, how did you do it?"

    stop music fadeout 3.0
    "Before I can answer, the professor walks in."
    show valerie smi at cc with dissolve
    "The girl gives me a lingering smile before shifting back into her seat."
    hide valerie with dissolve
    show professorF extra at cc with dissolve
    voice "audio/voice/E2/D1/S1/prof3f/1.ogg"
    prof3f "Good morning, class. Welcome to the Foreign Exchange International Bridging. This class is for those who are new to Japan or who would like a stronger understanding of Japanese culture and the history of the Isokaze. That means most of your assignments will require you to leave campus and explore the city."

    if MCStory == 1:
        "I hope that also means fewer papers to write."

    else:
        "This class should be interesting. It'll be nice to get off campus every once in a while."

    voice "audio/voice/E2/D1/S1/prof3f/2.ogg"
    prof3f "Now, let's begin… "
    $renpy.pause(1)
    #fade to black
    scene black with fade
    $renpy.pause(1)
    #class end
    scene bg campus auditorium day with fade
    show professorF extra at cc with dissolve

    voice "audio/voice/E2/D1/S1/prof3f/3.ogg"
    prof3f "You'll find your first class assignment online. Let me know if you have any questions, otherwise, have a great rest of your day."
    hide professorF with dissolve
    play sound "audio/sfx/Human/Class End.ogg" fadein 1
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3.0
    "The cute girl turns back to me and hands me a torn sheet of paper."
    show valerie smi at cc with dissolve
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO12.ogg"
    vb "Don't lose this, okay?"
    show valerie mis at cc
    "She winks."
    pf "What is it?"
    show valerie smi at cc
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO13.ogg"
    vb "It's my number."

    menu:
        "But we only just met!":
            pf "Isn't it a little too soon to be giving me this?"
            show valerie cur at cc
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO14.ogg"
            vb "You think so? I just thought it'd be nice to have a friend in class."
            pf "Oh… Actually, yeah, that would be nice."
            "I write down my number and pass it to her."
            show valerie smi at cc
            "She smiles her thanks."

        "We're so in sync.":
            "I hand her a similarly torn sheet of paper."
            show valerie cur at cc
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO15.ogg"
            vb "What's this?"
            pf "That's my number."
            show valerie hap at cc
            "She laughs."
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO16.ogg"
            vb "Looks like I beat you to the punch."
            show valerie smi at cc
            pf "Don't get used to it."

        "I don't even know you.":
            pf "Why are you giving me this?"
            "She brushes a stray hair from her eyes."
            show valerie mis at cc
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO17.ogg"
            vb "I was hoping we could get a chance to continue our earlier conversation."
            "I fold my arms, unconvinced."
            show valerie smi at cc
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO18.ogg"
            vb "And it'd be nice to get to know someone in the same class in case we ever have questions."
            pf "Oh, well that makes sense."
            "I scribble down my own number and hand it to her."
            pf "Here."
            show valerie smi at cc
            "She smiles."
            voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO19.ogg"
            vb "Thanks."

    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO20.ogg"
    vb "Call me some time, okay?"
    "She grabs her bag and starts to leave."
    pf "Wait!"
    show valerie cur at cc
    "She flips her hair and lets her gaze fall back on me."
    pf "What's your name?"
    show valerie smi at cc
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO21.ogg"
    vb "Valerie."
    pf "I'm [pfirst]."
    show valerie mis at cc
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D1/Valerie/EP2_D1_REDO22.ogg"
    vb "I know."
    "She winks at me again and turns away."
    stop music fadeout 3
    hide valerie with dissolve
    "I watch Valerie's hips sway mesmerisingly as she exits the room, and I'm left wondering what exactly just happened. {w}I've never met a girl as bold as her before… {w}And how did she know my name? From the qualifiers?"
    "I shake the questions out of my head and collect my things."
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 3
    show studentM2 extra at l2 with dissolve
    voice "audio/voice/E2/D1/S1/stu5m/5.ogg"
    stu5m "Did you see that? He didn't even ask for it but she just gave that guy her number!"
    show studentM extra at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E2/D1/S1/stu6m/4.ogg"
    stu6m "No way!"
    "The two of them crowd me as I pack up."
    voice "audio/voice/E2/D1/S1/stu6m/5.ogg"
    stu6m "Dude, that was amazing."
    pf "What was?"
    voice "audio/voice/E2/D1/S1/stu5m/6.ogg"
    stu5m "That chick was all over you! What's your secret?"
    pf "Huh?"
    voice "audio/voice/E2/D1/S1/stu5m/7.ogg"
    stu5m "I mean, how did you get a girl like that to just give you her number?"
    voice "audio/voice/E2/D1/S1/stu6m/6.ogg"
    stu6m "Yeah, usually we have to ask for it and that hardly ever works."
    "I shrug and shoulder my bag."

    menu:
        "Nothing in particular.":
            pf "I didn't do anything. She just gave it to me."
            "They frown."
            voice "audio/voice/E2/D1/S1/stu5m/8.ogg"
            stu5m "Guys like us should look out for each other."
            pf "\"Guys like us\"?"
            voice "audio/voice/E2/D1/S1/stu6m/7.ogg"
            stu6m "Yeah, tell us how you did it."

        "You have to be {color=#FFBF00}[pfirst]{/color}.":
            pf "I can't explain why women are just drawn to me."
            voice "audio/voice/E2/D1/S1/stu5m/9.ogg"
            stu5m "Neither can we."
            "I'm not sure whether I should be offended or not."

        "No idea.":
            pf "Who knows."
            voice "audio/voice/E2/D1/S1/stu5m/10.ogg"
            stu5m "That's it right here!"
            voice "audio/voice/E2/D1/S1/stu6m/8.ogg"
            stu6m "So you have to be aloof and the girls will flock to you?"
            pf "Uh, sure."

    "A few students hover in the doorway, unsure if they should enter the classroom or not."
    pf "Look, I've got to go. Other people need to use this room."
    voice "audio/voice/E2/D1/S1/stu6m/9.ogg"
    stu6m "One day, we'll learn your true secret!"
    stop ambient fadeout 3
    stop music fadeout 3
    hide studentM
    hide studentM2
    with dissolve
    scene black with fade
    "I leave before they can say anything else."
    
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus main day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 1
    
    "Now that class is over, I've got some free time. {w}What do I feel like doing?"
    
    #afternoon choice 1
    $ freeTime = "afternoon"
    
    call E2FreeTime from _call_E2FreeTime_3
    
    jump E2D1S2
