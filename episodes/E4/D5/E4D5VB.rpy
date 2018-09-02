#
label E4D5VB:

    play ambient "audio/ambience/Morning.ogg" fadein 3
    $renpy.pause(1.0)
    
    "A pressure on top of me jolts me awake."
    scene bg homekaito myroom day with fade
    "My eyes snap open and I stare into eyes as blue as the ocean waves."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show valerie smi at cc with dissolve:
        xzoom -1
    "Valerie leans forward when she notices I'm awake. Her hair falls about her face like a halo. I'm acutely aware of her legs straddling either side of me as her hands rest on my chest."
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L1.ogg"
    vb "Good morning."
    
    menu:
        "Can't tell if dreaming or awake…":
            "This can't be real life… can it?"
            "I close my eyes and open them again. Valerie cocks her head to the side and gives me a questioning look."
            show valerie dis
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L2.ogg"
            vb "That's not exactly the greeting I was expecting…"
            pf "Are you real or is this a dream?"
            show valerie hap
            "She giggles."
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L3.ogg"
            vb "I'm as real as can be."
            "She takes my hand and places it against her heart."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L4.ogg"
            vb "See?"
            "My face heats up and I quickly pull my hand away."
            pf "Uh, yeah, definitely feels real to me."
            show valerie mis
            "Valerie grins slyly."
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L5.ogg"
            vb "Besides, I highly doubt I'd be dressed like this in any dream of yours… or dressed at all for that matter…"
            "Valerie laughs as I squirm."
            pf "I don't know what you're talking about."
            show valerie hap
            "Suddenly the warm confines of my bed feels like a sauna. When did it get so hot in here?"
        
        "I could get used to this.":
            "I grin."
            pf "It is a good morning, but do you know what would make it a great morning?"
            show valerie cur
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L6.ogg"
            vb "What?"
            "I pull her down so she is lying flat on top of me."
            show valerie sur b2 with dissolve
            "Valerie squeals in surprise as she loses her balance. As soon as her face is within reach I press my lips against hers in a lingering kiss.{w} Slowly, she pulls away with a smile."
            show valerie smi b2 with dissolve
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L7.ogg"
            vb "That wasn't too bad."
            pf "I think the word you're looking for is \"great\"."
            show valerie thi b2
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L8.ogg"
            vb "Mm, I'm not convinced. I think I need another one to make an informed decision."
            "I grin and kiss her again, this time leaving her breathless."
            show valerie smi b2
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L9.ogg"
            vb "Okay, that one was pretty great."
        
        "What are you doing?":
            pf "Uh, Valerie? What are you doing here?"
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L10.ogg"
            vb "I'm your morning wake up call!"
            pf "...What?"
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L11.ogg"
            vb "Wake up!"
            "She bounces slightly on my bed."
            pf "Okay, okay, point made."
            show valerie mis
            "Valerie grins."
    
    pf "As much as I appreciate seeing you, how exactly did you get in here?"
    show valerie cur with dissolve
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L12.ogg"
    vb "Your sister let me in."
    pf "Ohhh…"
    "That's kind of surprising. I didn't think Nikki would have approved."
    "Valerie leans close to me again."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L13.ogg"
    vb "So, does this mean you're awake now?"
    pf "Yeah, I'm awake."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L14.ogg"
    vb "Good! Then it's time to get out of bed!"
    "She looks expectantly at me."
    pf "I would, but you're kind of on me."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L15.ogg"
    vb "I'm not sure I see the problem."
    show valerie smi
    pf "For some reason, I don't feel very motivated to get out of bed…"
    show valerie sur
    "A sharp shriek interrupts us, and another blonde head barges into my room."
    show nikki sur at r3 with dissolve:
        xoffset 200
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_501.ogg"
    sf "What is going on here?!"
    show nikki dis
    "Nikki darts towards Valerie and tugs on her arm."
    show valerie cur
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L16.ogg"
    vb "Hey!"
    "Valerie wobbles unsteadily on top of me."
    show nikki ann
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_502.ogg"
    sf "You said you were just going to study!"
    show valerie ann
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L17.ogg"
    vb "We are studying!"
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_503.ogg"
    sf "What could you possibly be studying like this?"
    show valerie mis
    "Valerie smirks."
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L18.ogg"
    vb "Anatomy."
    show nikki sur b2 with dissolve
    "Nikki freezes. Her eyes grow wide and her face turns bright red."
    show nikki win b2
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_504.ogg"
    sf "You--I can't--UGH!"
    "She resumes tugging on Valerie's arm."
    show nikki ann b2
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_505.ogg"
    sf "You have to leave!"
    pf "Calm down, Nikki, nothing's going on."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L19.ogg"
    vb "Okay, okay, I'm sorry. It was just a joke!"
    show nikki dis
    show valerie smi
    "Valerie slips out of Nikki's grasp and removes herself from my bed."
    "She points to her half-open bag, which looks like it was carelessly tossed to the ground."
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L20.ogg"
    vb "Look, there are my books."
    pf "You're making a huge deal out of nothing."
    "Nikki grudgingly crosses her arms."
    voice "audio/voice/E4/Nikki/Day 5/Nikki_04_506.ogg"
    sf "Fine, but you have to leave the door open."
    "She continues to stand there and glare at Valerie."
    pf "You can leave now."
    
    if E3D5S4_Reaction == 1:
        "Nikki stares straight into Valerie's eyes."
        show valerie cur
        show nikki ann
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_507.ogg"
        sf "I've got my eyes on you, so whatever you're thinking, don't."
        show valerie mis
        "Valerie looks amused."
        voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L21.ogg"
        vb "I'm not thinking anything."
        "Nikki narrows her eyes and continues to glare at Valerie, who's trying hard to keep a straight face."
        pf "Nikki! Go!"
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_508.ogg"
        sf "I'm going!"
        "When she reaches the doorway she turns around and gives Valerie the universal \"I'm watching you\" sign. Then she stomps out of the room, but not before yelling \"door open\" behind her."
        hide nikki with dissolve
    
    elif E3D5S4_Reaction == 2:
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_509.ogg"
        sf "Fine!"
        "She stares straight into Valerie's eyes."
        show valerie cur
        show nikki ann
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_510.ogg"
        sf "Don't even think about it."
        voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L22.ogg"
        vb "About what?"
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_511.ogg"
        sf "Just remember, whatever you're thinking of doing to him, I will do to you… twice."
        pf "Nikki! What the hell?"
        show valerie smi
        "Valerie bites her lips trying hard to contain her amusement."
        voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L23.ogg"
        vb "I promise to be on my best behaviour."
        "Nikki starts to walk out of the room."
        show nikki ang
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_512.ogg"
        sf "Don't forget, door open!"
        pf "Just go already!"
        show nikki ann
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_513.ogg"
        sf "I'm going!"
        hide nikki with dissolve
        "She stomps out of the room."
    
    elif E3D5S4_Reaction == 3:
        "Wordlessly, Nikki walks behind Valerie and begins to push her out of the room."
        show valerie sur
        voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L24.ogg"
        vb "What are you doing?"
        "I leap out of bed."
        pf "Stop it!"
        "Nikki immediately looks away."
        show nikki win
        show valerie cur
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_514.ogg"
        sf "Ew, put some pants on or something!"
        pf "Not until you leave."
        show nikki ann
        voice "audio/voice/E4/Nikki/Day 5/Nikki_04_515.ogg"
        sf "Fine! But don't you two try anything!"
        hide nikki with dissolve
        "Nikki stomps out of the room, and I suddenly realise I'm standing in my boxers in front of Valerie. I blush as she looks me up and down with amusement."
        show valerie hap b2 with dissolve
        voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L25.ogg"
        vb "That's a good look for you."
        "My face reddens as I quickly pull on some pants."
    
    pf "Sorry about that. I don't know what's gotten into her."
    show valerie smi with dissolve
    "Valerie laughs."
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L26.ogg"
    vb "She just cares about her brother."
    pf "I suppose."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D5/ValE4D5L27.ogg"
    vb "Anyway, we'd better actually get to studying before Nikki pops a blood vessel."
    pf "Right, give me a minute."
    
    if E3D5S4_Reaction == 3:
        "I grab my clothes and head to the washroom to finish up getting dressed."
    else:
        "I grab my clothes and head to the washroom to get dressed."
        
    show valerie smi
    "Once I've made myself presentable, I rejoin Valerie at my desk and we start on the first subject."
    scene black with fade
    "True to her word, Valerie is no slouch when it comes to her grades and her study guides were the most thorough I've ever seen."
    "After a couple hours of studying, Valerie has to leave. I walk her to the bus stop. When I came back home I head straight for my bed."
    stop music fadeout 3
    stop ambient fadeout 3
    "Time to catch up on some of those z's! Before long, I'm fast asleep."
    
    jump E4D5S1_RomanceReturn
