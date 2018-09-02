#
label E3_5KI:
    
    "Kaori grabs my arm before I can join the rest of the group."
    show kaori smi at cc with dissolve
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_01.ogg"
    ki "Hey you."
    pf "Hi."
    
    if E3_5S4_Costume == "Ranger":
        show kaori hap
        "Her eyes sparkle as a smile graces her lips."
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_02.ogg"
        ki "You dressed up as Balance!"
        pf "Yup, I thought you might like it."
        show kaori smi b1
        "She nods."
        show heart:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_03.ogg"
        ki "It suits you."
    
    elif E3_5S4_Costume == "Legolaz":
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_04.ogg"
        ki "Did you dress up as a fantasy character?"
        "I nod."
        show kaori mis
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_05.ogg"
        ki "It's too bad we didn't plan it together. We could have been from the same show or movie."
        pf "That would have been cool."
        show heart:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori smi b1
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_06.ogg"
        ki "I mean, it still works well for you."
    
    elif E3_5S4_Costume == "Officer":
        show kaori ske
        "Kaori raises an eyebrow."
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_07.ogg"
        ki "W-What are you wearing?"
        
        menu:
            "Flex!":
                "I hold up my arm and flex my bicep. The fabric tightens as I tense my muscles."
                pf "You like what you see?"
                show kaori cur b1
                "Kaori stares very obviously for a beat, then quickly looks away as her cheeks redden."
                show kaori thi b1
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_08.ogg"
                ki "Stop that!"
                "I smirk and lower my arm."
                show storm:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori dis b1
                "She sighs and gives me a \"you're an idiot\" look."
                "Worth it!"
            
            "You're under arrest.":
                show kaori cur
                "Kaori's eyes widen as I spin her around and hold her hands behind her back."
                show shoBlush:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori sur b1
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_09.ogg"
                ki "H-Hey! What do you think you're doing?"
                pf "You're under arrest."
                show kaori win b1
                "She struggles under my grip."
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_10.ogg"
                ki "Stop this at once!"
                pf "Now where did I put those handcuffs--"
                "Kaori let's out a squeal before I feel a sharp pain in my shin."
                # screen shake?
                pf "Ow!"
                show kaori ann b2
                "I let go in my surprise and she twists away from me."
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_11.ogg"
                ki "That's enough of your perverted fantasies!"
                show kaori thi b2
                "Her face is completely red, but she refuses to make eye contact and seems more embarrassed than angry."
                pf "Aw, fine."
                
        show kaori neu b1
        "She takes a deep breath and recomposes herself."
                    
    elif E3_5S4_Costume == "Badman":
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_12.ogg"
        ki "Badman?"
        pf "That would be me."
        show kaori mis
        "She smirks."
        voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_13.ogg"
        ki "So you're a superhero now, huh?"
        
        menu:
            "Always!":
                "I nod."
                pf "Who doesn't want to be one."
                show kaori smi b1
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_14.ogg"
                ki "I suppose that's fair."
            
            "I'm Badman.":
                pf "I'm Badman."
                show drop:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                show kaori ske
                "Kaori raises an eyebrow."
                pf "...Badman."
                "She sighs and smiles."
                show kaori mis b1
                voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_15.ogg"
                ki "You're an idiot."
                pf "No, I'm Badman."
                
    show kaori thi b1
    "Kaori self-consciously places a hand on her bare hip and looks away."
    show tsuBlush:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_16.ogg"
    ki "So... umm... what do you think of this outfit?"
    
    menu:
        "Cute!":
            "I smile warmly."
            pf "You look amazing."
            show kaori cur b1
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_17.ogg"
            ki "Really? You think it looks good?"
            pf "Yeah, but I'm pretty sure you can make anything look good."
            show kaori smi b2
            "Kaori's face is as red as her hair and she smiles."
            show regBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_18.ogg"
            ki "T-Thank you."
        
        "A bit revealing...":
            pf "I mean it looks good, but aren't you a bit too... exposed?"
            show kaori cur b1
            "Kaori looks down at herself. I think I just made her feel even more self-conscious."
            show kaori ner b2
            "She looks back at me and frowns."
            show kaori dis b2
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_19.ogg"
            ki "Well, it's what Lea wears!"
            pf "Lea?"
            show kaori ann b2
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_20.ogg"
            ki "The Knight! The character I'm cosplaying! This is her armour."
            pf "I wasn't trying to say it looked bad."
            show kaori thi b2
            "She shakes her head and sighs."
            show storm:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_21.ogg"
            ki "Nevermind, just forget I said anything."
            "She asked for my opinion and I was just being honest..."
    
    stop music fadeout 3
    voice "audio/voice/E4/Kaori/D0/Kaori_Halloween_22.ogg"
    ki "Let's go meet up with the rest of the team."
    pf "Alright."
    hide kaori with dissolve
    
    jump E3_5S5
