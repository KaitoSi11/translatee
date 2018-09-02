#
label E4D5MA:
    
    play ambient "audio/ambience/Morning.ogg" fadein 3
    $renpy.pause(1.0)
    
    
    "I wake up unexpectedly and blink my eyes at the sunlight filtering through my curtains. Is it morning already?"
    
    scene bg homekaito myroom day with fade

    "I wonder what woke me up… For some reason I can't get the feeling I'm being watched out of my head. It must be my imagination."
    "I roll over in bed to check the time when I see a dark-haired woman sitting beside my bed."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show mayu smi at cc with dissolve:
        xzoom -1
    pf "Mayu?"
    show mayu hap
    "She smiles cheerfully at me."
    voice "audio/voice/E4/Mayu/D5/Mayu D5-01.ogg"
    ma "Good morning!"
    pf "What are you doing here?"
    show mayu smi
    voice "audio/voice/E4/Mayu/D5/Mayu D5-02.ogg"
    ma "Waiting for you to wake up."
    show mayu sur b2 with dissolve
    "She must have noticed the expression on my face, because her eyes widen and her cheeks turn pink."
    voice "audio/voice/E4/Mayu/D5/Mayu D5-03.ogg"
    ma "N-No! Not like that! To study!"
    pf "What?"
    show mayu cur b2
    voice "audio/voice/E4/Mayu/D5/Mayu D5-04.ogg"
    ma "I-I came over so we could study together but you were sleeping so soundly and I didn't want to disturb you so I thought I'd just sit here and wait for you and--"
    "She finally pauses to take a breath."
    
    show mayu win b2
    voice "audio/voice/E4/Mayu/D5/Mayu D5-05.ogg"
    ma "I-I'm sorry!"
    "Mayu practically leaps out of the chair and reaches for her bag."
    show mayu thi b2
    voice "audio/voice/E4/Mayu/D5/Mayu D5-06.ogg"
    ma "T-This was a bad idea! I should go--"
    show mayu cur b2
    pf "Wait!"
    "I jump out of bed and grab her arm to stop her and pull her towards me. To my surprise, she doesn't try to resist like I had expected, and she ends up losing her balance and falling on top of me."
    show mayu ner b3 with dissolve
    "When she meets my gaze, her face turns red and she quickly looks away. My cheeks must be just as flushed. We immediately pull apart from each other."
    pf "I'll go get ready and then we can study."
    show mayu smi b3
    voice "audio/voice/E4/Mayu/D5/Mayu D5-07.ogg"
    ma "O-Okay."
    hide mayu with dissolve
    "I grab my clothes and head to the washroom to get dressed. After I return, Mayu is sitting at my desk with her books and notebook open. I gather up my tablet and textbooks and join her."
    scene black with fade
    "After a couple of hours, Mayu has to head out. I walk her to the bus stop, then when I return home I hop back into bed."
    stop music fadeout 3
    stop ambient fadeout 3
    "I need a nap after all that studying! Before long I'm fast asleep."
    
    jump E4D5S1_RomanceReturn
    
