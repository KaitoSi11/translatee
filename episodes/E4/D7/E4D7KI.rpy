#
label E4D7KI:
    $ kaoOut = renpy.random.choice(['comfort'])
    $ kaoHairF = renpy.random.choice(['default'])
    $ kaoHairB = renpy.random.choice(['default'])
    voice "audio/voice/E4/Kaori/D7/kaori_D5_01.ogg"
    ki "Hello?"
    pf "Kaori, can we meet?"
    "A few seconds of silence pass."
    voice "audio/voice/E4/Kaori/D7/kaori_D5_02.ogg"
    ki "Okay, where are you?"
    "I'm a little surprised she didn't ask me why. She must have sensed the urgency in my voice."
    pf "At the Hangar, but I'd rather not meet here. {w}Can I meet you at your dorm?"
    "She hesitates."
    voice "audio/voice/E4/Kaori/D7/kaori_D5_03.ogg"
    ki "...Okay."
    pf "Thanks, I'll see you soon."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop ambient fadeout 3
    scene black with fade
    #play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    
    "We hang up the phone. As if in a daze, I make my way to Kaori's dorm. This time I have no trouble getting past the front desk and I'm soon knocking on her door."
    # sfx door knock then pause?
    $renpy.pause(0.5)
    scene bg campus kaoriroom night with fade
    "Kaori flings open the door and looks at me intensely before letting me in. I sit on the couch and she sits beside me."
    show kaori ske at cc with dissolve
    voice "audio/voice/E4/Kaori/D7/kaori_D5_04.ogg"
    ki "What's going on? You're acting really strange."
    pf "Sorry, it's been a long day."
    show kaori neu
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    pf "There's something I need to tell you."
    
    
    if E4D7S2_CoreDestroyed == 1:
        voice "audio/voice/E4/Kaori/D7/kaori_D5_05.ogg"
        ki "What is it?"
        pf "My core's gone."
        show shocked:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori sur
        "Kaori's eyes widen and she gasps sharply."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_06.ogg"
        ki "It's {i}gone{/i}?"
        pf "Yeah."
        show kaori ang
        "Her fierce scowl returns."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_07.ogg"
        ki "I can't believe someone would vandalize another person's property like that! We should report this to the school administration. They can look at their live feed and track down who did this."
        pf "No, Kaori--"
        show kaori ann
        voice "audio/voice/E4/Kaori/D7/kaori_D5_08.ogg"
        ki "Have you told Valerie yet? It might be a long shot but maybe she's got some blueprints or notes or something and can reconstruct your core since she's spent so much time studying it."
        pf "Kaori!"
        show kaori neu
        voice "audio/voice/E4/Kaori/D7/kaori_D5_09.ogg"
        ki "What?"
        pf "I don't need Valerie to reconstruct it."
        show kaori ske
        voice "audio/voice/E4/Kaori/D7/kaori_D5_10.ogg"
        ki "What will you use during matches then?"
        pf "I'll figure something out."
        show kaori ann
        "She narrows her eyes."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_11.ogg"
        ki "You're not making any sense right now!"
    
    else:
        "She glances at my clenched hand."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_12.ogg"
        ki "Does it have anything to do with that?"
        pf "Yeah."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_13.ogg"
        ki "What is it?"
        "I show her the drive."
        show question:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori ske
        "Kaori gives me a questioning look."
        pf "It's the data to my core."
        voice "audio/voice/E4/Kaori/D7/kaori_D5_14.ogg"
        ki "Why do you have your core's data in your hands?"
        pf "I downloaded it from Eagle."
        show kaori neu
        voice "audio/voice/E4/Kaori/D7/kaori_D5_15.ogg"
        ki "Obviously, but why?"
    
    stop music fadeout 10
    hide kaori with dissolve

    "I sigh, and tell her everything I've learned. She listens quietly, but her expression darkens the longer I talk."
    show kaori ann at cc
    voice "audio/voice/E4/Kaori/D7/kaori_D5_16.ogg"
    ki "That's so--I mean--how does--! Gah!"
    show kaori thi
    show storm:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    
    "I blink in surprise. It's not often Kaori's rendered speechless."
    pf "I know it's a lot to take in at once."
    show kaori ner
    voice "audio/voice/E4/Kaori/D7/kaori_D5_17.ogg"
    ki "That's not it. Well, it is a lot to take in, but…"
    show kaori sad
    voice "audio/voice/E4/Kaori/D7/kaori_D5_18.ogg"
    ki "I'm sorry your dad put this burden on you."
    show kaori neu
    "She then looks sideways at me."
    
    voice "audio/voice/E4/Kaori/D7/kaori_D5_19.ogg"
    ki "But if he had to trust somebody with this decision, I suppose he was right to trust you."
    pf "So you agree with my choice?"
    show kaori neu
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    "Kaori nods."
    voice "audio/voice/E4/Kaori/D7/kaori_D5_20.ogg"
    ki "It's what I would have done. Your core was way more than just a core. Knowing that, how could you continue to use it in the same way?"
    show kaori thi
    voice "audio/voice/E4/Kaori/D7/kaori_D5_21.ogg"
    ki "Besides, we can always find you a new core. I'm sure Valerie would enjoy the challenge of building a core from scratch and you already have some experience in doing that."
    show kaori neu
    voice "audio/voice/E4/Kaori/D7/kaori_D5_22.ogg"
    ki "Plus… I could help too."
    "I breathe a sigh of relief as a weight is lifted off my shoulders. I hadn't realised just how anxious I'd been about my decision. A part of me continued to wonder if perhaps I'd acted too rashly, but if someone as rational as Kaori agrees with me then I know I made the right choice."
    pf "Yeah, I'm not too worried about finding another core."
    show kaori thi
    "Kaori thinks."
    show kaori cur
    voice "audio/voice/E4/Kaori/D7/kaori_D5_23.ogg"
    ki "Although, if you want to get rid of the source data completely, you might want to talk to Valerie. Since she's worked on your core, she might have a copy of blueprints or something."
    #stop music fadeout 5
    pf "Good call. I'll talk to her later."
    show kaori neu
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "We lapse into silence."
    pf "Sorry, I guess I'm kind of boring to be around right now."
    show kaori mis
    "Kaori shrugs."
    #play music "audio/music/You and I (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E4/Kaori/D7/kaori_D5_24.ogg"
    ki "Better than you acting like a pervert all the time."
    "...Was she trying to make a joke?"
    show panic:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ner
    voice "audio/voice/E4/Kaori/D7/kaori_D5_25.ogg"
    ki "S-Sorry! I didn't mean to make light of the situation..."
    "I smile warmly."
    pf "No, it's okay, it's exactly what I needed."
    show kaori smi
    "I glance at her. For once, she looks sympathetic, but her lips are pressed into a thin line."
    voice "audio/voice/E4/Kaori/D7/kaori_D5_26.ogg"
    ki "You can't change what's happened in the past so there's no use dwelling on it."
    pf "Maybe... There are still so many unanswered questions..."
    show kaori neu
    voice "audio/voice/E4/Kaori/D7/kaori_D5_27.ogg"
    ki "I know. It's okay to want to make sense of things, but only if that will help you process what has happened."
    "She hesitates, then clasps my hand in hers and looks into my eyes."
    show kaori smi
    voice "audio/voice/E4/Kaori/D7/kaori_D5_28.ogg"
    ki "If you want to find answers, I'll help you."
    pf "Really?"
    show kaori smi
    voice "audio/voice/E4/Kaori/D7/kaori_D5_29.ogg"
    ki "Yes."
    
    menu:
        "Let's do it.":
            "I smile at her. With Kaori by my side, I won't have to worry about losing control of myself. If I waver in strength, if I get buried in the fear and pain, I can always count on her to keep me in line."
            "I nod."
            pf "Thank you."
            "She nods, but I can see she's worried about me."
            pf "I promise I'll be fine."
            stop music fadeout 8
            show kaori cur b1 with dissolve
            "Her cheeks flush."
            voice "audio/voice/E4/Kaori/D7/kaori_D5_31.ogg"
            ki "W-Who said anything about that?"
            pf "You didn't have to."
            show kaori smi b2 with dissolve
            "She looks away as her cheeks redden even more."
            show regBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D7/kaori_D5_32.ogg"
            ki "Don't be stupid."
        
        "No, let's put this to rest.":
            stop music fadeout 6
            "I smile at her. Kaori's keeping a brave face for me because she knows I'm vulnerable, but when I look into her eyes I can see just how worried she is about me."
            "If I go down this hole, who knows if I'll ever be able to crawl out again. I don't want to be someone who is fixated on the past, unable to move forward."
            pf "Thanks, but I think it's best to leave things as they are."
            "She nods, and relaxes slightly."
            
            
    "We settle into silence again. Kaori sneaks glances my way, then gently rests her head on my chest. As I feel her gentle weight against me, my mind clears. {w}Like usual, she makes sense. Whether or not Dad told me doesn't matter now. He's gone, and no amount of speculation can change that."
    "I'm lucky to have found someone to keep me grounded. With Kaori by my side, there is no mystery we can't solve."
    
    
    
    $ renpy.music.set_volume(1.0, channel="music")
    $renpy.pause(.5)
    play music "audio/music/Timeless.ogg" fadein 4
    show kaori cur b2 with dissolve
    "I run my fingers through her hair, and she glances up at my touch."
    
    "Slowly, I close the distance between our lips and kiss her. For once she doesn't seem surprised or shy away from my touch, but melts into the kiss. As we pull away, I gaze deeply into her eyes."
    show kaori smi b2 with dissolve
    "In this moment, I have clarity. It rinses away all my stress and fears."
    "It's okay that I don't have all the answers now, because I'm looking at my future...{p}\n...and it is beautiful."
    
    jump E4Epilogue