#
label E4D5KI:
    
    play ambient "audio/ambience/Morning.ogg" fadein 3
    $renpy.pause(1.0)
    
    "I wake up from some vigorous shaking and open my eyes to the familiar frown of my favourite fiery redhead."
    scene bg homekaito myroom day with fade
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show kaori cur at cc with dissolve:
        xzoom -1
        
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_01.ogg"
    ki "Hey! Wake up!"
    "Still groggy, I half mumble a response."
    pf "How did you get in here?"
    show kaori ske
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_02.ogg"
    ki "Nikki let me in and told me you were still sleeping."
    show kaori neu
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_03.ogg"
    ki "Now, wake up!"
    
    menu:
        "I'm awake!":
            pf "Okay, I'm awake! Just please, no more shaking."
            show kaori smi
            "Kaori eases up and softens her look."
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_04.ogg"
            ki "Sorry, but that was the only thing that worked. You're a really deep sleeper."
            pf "Uh, how long were you trying to wake me up?"
            show kaori cur b1 with dissolve
            "Kaori blushes."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori thi b1
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_05.ogg"
            ki "I don't know! Not long! I just got here!"
            pf "Ooookay…"
            show kaori neu
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_06.ogg"
            ki "Go get dressed!"
            
        "It's time to sleep. You sleep too!":
            #stop music fadeout 4
            pf "No, I'm not waking up."
            show kaori ske
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_07.ogg"
            ki "What?"
            "I reach out from under my bed and grab Kaori's arms, then pull her into me."
            show kaori sur b1 with dissolve
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_08.ogg"
            ki "Ah!"
            "She loses her balance and her torso falls on top of me and my bed."
            show kaori ann b1
            #play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_09.ogg"
            ki "Hey! Let me go!"
            "She begins to pull away but I hold her close. Her face is inches away from my own and her hair tickles me as it falls around her face."
            "I gently kiss her cheek."
            show kaori cur b2 with dissolve
            "She pauses and I can feel the warmth in her face as I kiss her cheek again."
            pf "Join me."
            show kaori thi b2
            "She hesitates, then tries to pull away again."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_10.ogg"
            ki "N-No! We have to--"
            "Another voice calls out, interrupting Kaori."
            show kaori cur b2
            voice "audio/voice/E4/Nikki/Day 5/Nikki_04_516.ogg"
            sf "Geez, guys, at least close your door!"
            show nikki ske at r3 with dissolve:
                xoffset 200

            "Nikki pops her head into the room and mimics a look of disgust before closing the door for us."
            show kaori ner b3 with dissolve:
                xzoom 1
            "Kaori breaks free from my grasp and leaps away from me as soon as she hears Nikki's voice."
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_11.ogg"
            ki "Nothing's happening!"
            "I hear Nikki's laughter clearly from the other side of the door."
            show nikki thi
            voice "audio/voice/E4/Nikki/Day 5/Nikki_04_517.ogg"
            sf "Likely story!"
            hide nikki with dissolve
            show kaori sur b3
            "Kaori whirls on me. Her face is even redder than I thought was possible."
            show kaori win b3
            #stop music fadeout 3
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_12.ogg"
            ki "Idiot!"
            show kaori ann b2 with dissolve
            "Kaori pouts."
            show kaori dis b1 with dissolve
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_13.ogg"
            ki "Ugh, forget it."
            pf "I was just teasing! I'll get up."
            "She crosses her arm like she doesn't believe me."
            #play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
        
        "Fine, but I won't be happy about it.":
            "I grumble to myself as I sit up."
            show kaori smi
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_14.ogg"
            ki "Don't look so sour. I came all this way for you."
            "I brighten up a little and keep the grumbling to a minimum."
            "Kaori hides a smile."
            show note:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_15.ogg"
            ki "That's better, I guess."
    
    "I'm about to throw off my blankets when I remembered what I decided to wear to bed last night…"
    pf "You might want to look away for a second."
    show kaori cur
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_16.ogg"
    ki "Why?"
    
    menu:
        "Tell her you're indecent.":
            pf "Uh, well, I wasn't expecting anyone to show up this morning so… I'm not exactly… dressed…"
            "Kaori blinks, then whirls to face away from me."
            show shocked:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori sur
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_17.ogg"
            ki "Why aren't you wearing any pajamas?!"
            pf "I just told you why!"
            show kaori ske
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_18.ogg"
            ki "Do you not usually wear them?"
            pf "Uhhh--"
            show kaori win b2 with dissolve
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_19.ogg"
            ki "Nevermind! I don't want to know."
            "She races for the door."
            show kaori thi b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_20.ogg"
            ki "I-I'll be waiting outside. Just hurry up!"
            hide kaori with dissolve
            "Kaori steps out of the room and loudly closes the door behind her. She must really want to ensure the door was actually closed."
        
        "Throw off the covers and show her!":
            "A mischievous grin spreads across my face."
            pf "Because of this."
            show kaori sur b2 with dissolve
            show shoBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "I flip the blankets off of me and reveal my boxers in all of their glory."
            "Kaori averts her eyes and whirls away from me."
            show kaori thi b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_21.ogg"
            ki "Y-You idiot! Why are you naked?"
            pf "I'm not naked."
            show kaori ann b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_22.ogg"
            ki "You may as well be!"
            pf "It's not like I was expecting anyone to show up in my room this morning."
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_23.ogg"
            ki "S-So? Are you trying to tell me you always sleep naked?"
            pf "Well--"
            show kaori dis b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_24.ogg"
            ki "Idiot!"
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_25.ogg"
            ki "Hurry up and get dressed!"
            "I shrug and swing my legs over the bed."
            show kaori sur b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_26.ogg"
            ki "Wait!"
            pf "What?"
            show kaori thi b2
            "Kaori races towards the door."
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_27.ogg"
            ki "At least wait for me to leave first."
            pf "Why? You've already seen them…"
            show kaori ann b2
            voice "audio/voice/E4/Kaori/D5/Kaori_D5_28.ogg"
            ki "That's not the point!"
            hide kaori with dissolve
            "Before I can respond, she pulls open the door and slams it shut behind her."
            "I can't stop the grin on my face. {w}She's so cute when she's flustered!"
    
    "I slide out of bed and grab my clothes. After I get dressed, I let Kaori back into the room while I head to the washroom to freshen up. When I return, Kaori is already sitting at my desk."
    "She looks up as I join her."
    show kaori neu at cc with dissolve
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_29.ogg"
    ki "Here."
    "My tablet pings with a notification as I set up my books and notes. I open the attachment she sent me."
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_30.ogg"
    ki "These are the templates I use for my study guides. I thought they might be helpful for you."
    "I'm impressed as I scan through the template. Kaori definitely takes her studies seriously because these are really thorough guides."
    pf "Thanks, these look great."
    show kaori smi
    "She nods, but seems pleased."
    voice "audio/voice/E4/Kaori/D5/Kaori_D5_31.ogg"
    ki "Okay, let's get to work."
    hide kaori with dissolve
    scene black with fade
    "We study together for a few hours before Kaori has to leave. I got through most of my classes with her here to help quiz me and feel pretty confident about our session together. {w}After I walk her to the bus stop, I come home and head straight for my bed."
    stop music fadeout 3
    stop ambient fadeout 3
    "I need a nap after that intense session…"
    "Before long, I'm fast asleep."
    
    jump E4D5S1_RomanceReturn
