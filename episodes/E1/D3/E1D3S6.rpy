label E1D3S6:
    # Already in library, ambient is playing with no music
    "I enter through the sliding doors into the large, bright library. Row after row of tall shelvings filled with books stretch further than I can see."
    
    "Several students are scattered about the room. Some search the book shelves, while others study at the cubicle desks throughout the library." 
    
    if (E1D2S2_talkwithyuunayes == 0):
        $ E1D3S6_WentLibraryStudied = 1
        jump E1D3S7
    
    "I make my way to one of the empty desks when bright pink hair catches my eye."
    show yuuna neu at cc with dissolve
    "Yuuna concentrates on the large book in front of her." 
    
    menu:
        "Leave her alone.":
            $ E1D3S6_WentLibraryStudied = 1
            "She looks busy. I shouldn't disturb her."
            hide yuuna with dissolve
            jump E1D3S7
    
        "Go say hi.":
            $ E1D3S6_WentLibraryYuuna = 1
            play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 1
            "I head over." 
            pf "Hey, Yuuna."
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur at cc with dissolve
            show yuuna smi at cc with dissolve
            "She glances up at me and smiles."
            voice "audio/voice/E1/D3/S6/Yuuna/1.ogg"
            ym "Hey." 
            "I point to the chair beside her."
            pf "May I sit?"
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/2.ogg"
            ym "Of course." 
            pf "What are you reading?"
            show yuuna smi at cc
            voice "audio/voice/E1/D3/S6/Yuuna/3.ogg"
            ym "Just one of my text books."
            stop music fadeout 3
            "I glance at the open page and catch the words \"health\" and \"priority\". Must be a health physiotherapy book."
    
            if (E1D2S2_YuunaComesWithYouPass == 1):
                pf "Thanks again for helping me out yesterday."
                show yuuna hap b1 at cc with dissolve
                voice "audio/voice/E1/D3/S6/Yuuna/4.ogg"
                ym "It was nothing." 
                pf "No, I really appreciate it. It's rare to find someone who'd go out of their way to help a stranger."
                show yuuna smi b1 at cc
                show regBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                "Yuuna smiles."
                stop music fadeout 3
                voice "audio/voice/E1/D3/S6/Yuuna/5.ogg"
                ym "Well, I was happy to help."
                
            show yuuna smi at cc with dissolve
            voice "audio/voice/E1/D3/S6/Yuuna/6.ogg"
            ym "So, how are you enjoying ACE?"
            play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
    
            menu: 
                "Grrrrrreat!":
                    pf "It's awesome!"
                    show yuuna cur at cc with dissolve
                    "She blinks at my outburst."
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna thi b1 at cc with dissolve
                    "A couple of nearby students shush me, and she fidgets in embarrassment."
                    pf "Sorry about that."
                    "When she speaks next, her voice is significantly softer."
                    show yuuna hap b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/7.ogg"
                    ym "No worries. It's refreshing to see someone so enthusiastic. But now I'm curious as to what made it such a great day."
                    pf "Well, my first class seems promising, even though it's for first years. {w}It seems like the material is more ACE Academy specific so it won't be a complete repeat. I also managed to find a team for the qualifiers."
                    pf "Oh, and I met this really nice girl on the bus yesterday."
                    show yuuna ner b1 at cc with dissolve
                    show regBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "She blushes and a faint smile graces her lips."
                    show yuuna smi b1 at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/8.ogg"
                    ym "You're too kind. Which team did you join?" 
                    pf "The one with Shou and two other girls, Kaori and Mayu, I think."
                    show yuuna hap at cc with dissolve
                    "Yuuna nods knowingly." 
                    voice "audio/voice/E1/D3/S6/Yuuna/9.ogg"
                    ym "They should be a good team."
                    pf "Oh, you know them?"
                    show yuuna smi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/10.ogg"
                    ym "No, but I've heard about them."
                    pf "What have you heard?"
                    show yuuna thi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/11.ogg"
                    ym "Just the usual stuff--that they used to be part of this other good team but left due to disagreements with the leader."
                    pf "Ah yeah, I've heard that too."
                    show yuuna smi at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/12.ogg"
                    ym "I'm not a pilot so I don't really hear any of the in-depth gossip."
                    pf "That's okay. I'm new so I don't hear any of the in-depth gossip either."
                    show yuuna hap at cc
                    "She laughs quietly."
             
                "With you here, I think I could get used to this place.":
                    pf "It's not bad. Not bad at all."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/13.ogg"
                    ym "You're enjoying your time here?"
                    pf "Absolutely."
                    show yuuna hap at cc
                    "She seems pleased by my comment."
                    voice "audio/voice/E1/D3/S6/Yuuna/14.ogg"
                    ym "What do you like best about ACE?"
                    "I take a long look at her."
                    pf "Well, I'd have to say the sights here are the most beautiful I've seen so far."
                    show question:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna cur b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/15.ogg"
                    ym "Really? Even better than CINY?"
                    pf "Oh yes, CINY can't even compare."
                    "I flash her a boyish grin."
                    show yuuna sur b1 at cc with dissolve
                    show shoBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "She blinks in surprise, and seems almost confused by the blush growing on her cheeks."
                    show yuuna ner b1 at cc
                    "She quickly changes the subject."
                    show yuuna thi b1 at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/16.ogg"
                    ym "So, the qualifiers are coming up for pilots, right?"
                    pf "Yeah, and I've already snagged myself a team."
                    show yuuna hap b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/17.ogg"
                    ym "Oh, that's great!"
                    "Her face reddens again as the students beside us shush her."
                    show yuuna ner b1 at cc with dissolve
                    voice "audio/voice/E1/D3/S6/Yuuna/18.ogg"
                    ym "I mean, that's great."
                    show yuuna smi b1 at cc with dissolve
                    pf "I'm just as excited. I feel good about this team."
                    
                "It's fine, I guess.":
                    pf "It's alright." 
                    show yuuna ner at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/19.ogg"
                    ym "Oh… Are there things you miss from CINY that you haven't found here?"
                    pf "Not really."
                    show yuuna neu at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/20.ogg"
                    ym "I see."
                    show dots:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    "She falls silent and waits for me to say something."
                    pf "I mean, as far as schools go, this one isn't terrible."
                    show yuuna cur at cc
                    voice "audio/voice/E1/D3/S6/Yuuna/21.ogg"
                    ym "Oh, um, I suppose that's good."
                    pf "I pretty much only care about the GEAR battles anyway, so finding a team has been a win."
                    show yuuna smi at cc
                    "She smiles politely."
    
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/22.ogg"
            ym "Well, I'm glad to hear you're enjoying your time here."
            show yuuna cur at cc with dissolve
            "She casually glances at the clock on the wall, then her eyes grow wide."
            voice "audio/voice/E1/D3/S6/Yuuna/23.ogg"
            ym "Oh, I didn't realise what time it is. I have an appointment at the Registrar's Office."
            show yuuna neu at cc
            "She begins to pack up her things."
            show yuuna smi at cc
            voice "audio/voice/E1/D3/S6/Yuuna/24.ogg"
            ym "It was nice to see you again."
            pf "Yeah, you too. I'll see you tomorrow, right?"
            show yuuna cur at cc
            "She blinks."
            pf "I mean in class…"
            show yuuna hap at cc
            voice "audio/voice/E1/D3/S6/Yuuna/25.ogg"
            ym "Oh yeah! I'll see you then."
            hide yuuna with dissolve
            "With a smile and a quick wave goodbye, she leaves."
            stop music fadeout 3
            "I settle into her newly vacant desk and grab my tablet from my bag. Time to get to work."
            #fade to black
            scene black with fade
            $renpy.pause(2.5)
            "By the time I'm done, it's already kind of late. I quickly gather my things and head out."
            stop ambient fadeout 3
    
            jump E1D3S8