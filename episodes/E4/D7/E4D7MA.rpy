#
label E4D7MA:
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "yandere"
    
    voice "audio/voice/MISSING/BATCH8/D7-01.ogg"
    ma "Oh, hi! Sorry it took me so long to answer. I was a little surprised you called."
    pf "Sorry to bother you, Mayu, but do you think we could meet?"
    voice "audio/voice/MISSING/BATCH8/D7-02.ogg"
    ma "Is everything okay?"
    "I must sound weird because the worry immediately creeps into her voice."
    pf "Honestly, I don't know. I just found out something huge about my parents and my core."
    voice "audio/voice/MISSING/BATCH8/D7-03.ogg"
    ma "O-Oh… um, okay. Where would you like to meet?"
    pf "I can come to you."
    "She pauses."
    pf "Mayu?"
    voice "audio/voice/MISSING/BATCH8/D7-04.ogg"
    ma "I-I'm in my room…"
    pf "Oh…"
    "I'm not sure how to ask if I can go there without sounding like I have ulterior motives.  {w}Luckily, I don't have to."
    voice "audio/voice/MISSING/BATCH8/D7-05.ogg"
    ma "I-If you want to come here t-that would be okay."
    pf "Are you sure?"
    voice "audio/voice/MISSING/BATCH8/D7-06.ogg"
    ma "Yes!"
    "She doesn't even hesitate."
    voice "audio/voice/MISSING/BATCH8/D7-07.ogg"
    ma "I mean, yes."
    pf "Thanks, Mayu. I'll be there soon."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop ambient fadeout 3
    scene black with fade
    #play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    scene bg campus main night with fade
    
    "We hang up the phone. As if in a daze, I make my way towards her dorm. {w}Mayu greets me at her building's entrance. Her smile falters when she sees me and she furrows her brows."
    scene bg campus dormroom night with fade
    "We don't speak as she leads me to her room. I sit on the couch and look around the room as Mayu joins me."
    show mayu neu at cc with dissolve
    "This dorm definitely isn't like any others. Not only is this couch plush and comfortable, she also has a fireplace and a kitchenette. It feels more like a studio than a dorm room."
    show mayu ner b1
    "Mayu blushes."
    voice "audio/voice/MISSING/BATCH8/D7-08.ogg"
    ma "Sorry for the mess."
    "Everything is neatly arranged on all surfaces and her floors are spotless."
    pf "You have a really nice room."
    show mayu smi
    voice "audio/voice/MISSING/BATCH8/D7-10.ogg"
    ma "Thanks, it's smaller than my room back home but I still prefer this one. I like how cozy it is. Even though the dorm belongs to ACE, this room somehow still feels more like mine than my room at home ever did."
    "I spot the manga novels lining her shelves and little fantasy figurines she must have painted. I'm sure her father would not have allowed that in her room back home."
    "I'm glad she's found a place where she can express herself."
    
    
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    
    if E4D7S2_CoreDestroyed == 1:
        pf "There's something I need to tell you."
        show mayu neu
        voice "audio/voice/MISSING/BATCH8/D7-11.ogg"
        ma "Okay…"
        pf "My core is gone."
        show mayu sur
        "Mayu's eyes widen and her voice trembles slightly."
        show shocked:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/MISSING/BATCH8/D7-12.ogg"
        ma "But how--why would anyone--who would do such a thing?!"
        pf "I did."
        show mayu cur
        "She pauses and fixes her big, doe eyes on me."
    
    else:
        show mayu cur
        "She glances curiously at my hand."
        voice "audio/voice/MISSING/BATCH8/D7-13.ogg"
        ma "What are you holding?"
        "I look down and barely register my clenched hand. That's right…"
        "Opening my hand, I show her the drive."
        show question:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        "She cocks her head to the side."
        pf "It's the data to my core."
        voice "audio/voice/MISSING/BATCH8/D7-14.ogg"
        ma "...What are you doing with it?"
        pf "Just storing it for now."
        show mayu neu
        "She pauses."
        voice "audio/voice/MISSING/BATCH8/D7-15.ogg"
        ma "Okay… but what about when you're done storing it?"
        pf "That's what I'm trying to figure out."
        "She fixes her big, doe eyes on me."
        
    hide mayu with dissolve
    "I recount everything I've learned so far. Mayu lets me talk and my story comes out in a non-chronological mess. Every so often she would nod to let me know she was still listening, but otherwise she did not interrupt."
    "Once I'm done, she looks down."
    show mayu sad at cc with dissolve
    voice "audio/voice/MISSING/BATCH8/D7-16.ogg"
    ma "That's awful."
    voice "audio/voice/MISSING/BATCH8/D7-17.ogg"
    ma "I don't know what I would have done if I were you."
    pf "Maybe I acted too quickly…"
    show mayu sur
    "She looks up again."
    show exclamation:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/MISSING/BATCH8/D7-18.ogg"
    ma "No!"
    "I blink at her outburst."
    show mayu ann
    voice "audio/voice/MISSING/BATCH8/D7-19.ogg"
    ma "You did what was right, which was really brave of you."
    pf "Then how come it still feels like I was wrong?"
    show mayu sad
    "She places a sympathetic hand on my arm."
    voice "audio/voice/MISSING/BATCH8/D7-20.ogg"
    ma "Because that decision is a hard burden to bear, and I'm sorry you had to be the one to make it."
    "Somehow, her words make me feel a little bit lighter. I hadn't realised how anxious I was about what I'd done until someone validated my decision."
    "I look away."
    pf "I'm sorry, I guess I'm not that fun to be around right now."
    show mayu neu
    "She shakes her head."
    voice "audio/voice/MISSING/BATCH8/D7-21.ogg"
    ma "It's okay! You're going through a lot. I can't imagine what I'd do if I were in your shoes."
    show mayu ner
    voice "audio/voice/MISSING/BATCH8/D7-22.ogg"
    ma "I know it's hard to have one image of your father and suddenly that image is cracked to reveal a new person underneath."
    pf "I just keep wondering what if he'd told me… maybe he'd still be alive…"
    show panic:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu sur
    voice "audio/voice/MISSING/BATCH8/D7-23.ogg"
    ma "Ah, you mustn't think like that!"
    show mayu ann
    voice "audio/voice/MISSING/BATCH8/D7-24.ogg"
    ma "I know I'm probably the last person to tell you that because I'm always thinking about all the ways my life could have turned out differently, but focusing on your father's death and wondering if he'd be alive is dangerous."
    show mayu sad
    voice "audio/voice/MISSING/BATCH8/D7-25.ogg"
    ma "If you aren't careful, you'll be stuck in the same moment forever and it'll consume you until you forget about your own life."
    show mayu ner
    "She looks at her feet."
    voice "audio/voice/MISSING/BATCH8/D7-26.ogg"
    ma "It must be hard to have your dad taken away from you so suddenly, but that's a fact that can never be changed."
    #stop music fadeout 3
    pf "I know… but still…"
    "My voice trails off. What am I even trying to say?"
    #play music "audio/music/You and I (GAME VERSION).ogg" fadein 3
    show mayu neu
    "Mayu smiles gently and leans close to me."
    show mayu smi
    voice "audio/voice/MISSING/BATCH8/D7-27.ogg"
    ma "He loved you very much."
    pf "How can you be so sure?"
    voice "audio/voice/MISSING/BATCH8/D7-28.ogg"
    ma "That video he left you. He knew you would find it."
    stop music fadeout 4
    "She seems so sure of her answer. Her soft smile warms me from the inside and soothes my aching heart. Her quiet gentleness is a strength in itself, and with her support I can feel the pain and fear ease."
    "She's right. I know Dad loved me and Nikki, and this event shouldn't change my mind about that. He was only doing what the thought was best to protect me, and no matter how much I wish he would, he can never come back."
    "I pull Mayu into a hug."
    show mayu cur b1 with dissolve
    pf "Thank you. I don't know what I would do without you."
    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/music/Timeless.ogg" fadein 2
    show heart:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner b2 with dissolve
    "She blushes deeply and looks up at me. As if drawn to her, I lean in and let my lips gently brush against hers."
    show mayu sur b3 with dissolve
    "She blinks in surprise, then quickly melts into the kiss. As we pull away, I gaze deeply into her eyes."
    show mayu smi b3 with dissolve
    
    "In this moment, I have clarity. It rinses away all my stress and fears."
    "It's okay that I don't have all the answers now, because I'm looking at my future...{p}\n...and it is beautiful."
    
    jump E4Epilogue