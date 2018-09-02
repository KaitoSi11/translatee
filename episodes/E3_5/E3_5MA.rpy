#
label E3_5MA:
    
    show mayu smi b1 at cc with dissolve:
        yoffset -100
        xzoom 1.25
        yzoom 1.25
    "As I'm about to follow the group, someone slips their hand into mine. I glance over at a blushing Mayu, who quickly retracts her hand."
    show mayu ner b2 at cc with dissolve:
        yoffset 0
        xzoom 1
        yzoom 1
    voice "audio/voice/E4/Mayu/D0/Mayu D0-01.ogg"
    ma "Sorry..."
    "I smile."
    pf "What's up?"
    voice "audio/voice/E4/Mayu/D0/Mayu D0-02.ogg"
    ma "Umm... I just wanted to..."
    show mayu cur b1
    "She looks me up and down curiously."
    
    if E3_5S4_Costume == "Ranger" or E3_5S4_Costume == "Badman":
        show mayu hap b1
        voice "audio/voice/E4/Mayu/D0/Mayu D0-03.ogg"
        ma "I like your outfit. A hero suits you well!"
        pf "Thanks!"
    
    elif E3_5S4_Costume == "Legolaz":
        show mayu smi b2 at cc with dissolve:
            yoffset -100
            xzoom 1.25
            yzoom 1.25
        "Mayu slips her hands back into mine and leans in close to me. Her blush deepens and her voice softens."
        voice "audio/voice/E4/Mayu/D0/Mayu D0-04.ogg"
        ma "\"I would rather share one lifetime with you than face all the ages of this world alone. I choose a mortal life.\""
        
        menu:
            "Mayu?!":
                "My eyes widen and my face feels like it's on fire."
                show mayu cur b2
                pf "W-What are you saying?"
                show mayu ner b2 at cc with dissolve:
                    yoffset 0
                    xzoom 1
                    yzoom 1
                "Mayu blinks, then steps back and avoids eye contact with me."
                show panic:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Mayu/D0/Mayu D0-05.ogg"
                ma "I-It's from L-Lord of the GEARs! I-I was just quoting a l-line..."
                "Oh... {w}that's right. Anyone who's a fan of the movie knows that line. {w}Still, my heart is racing."
                pf "Sorry. I remember, yes."
                show mayu wor b2
                "Mayu nods."
                voice "audio/voice/E4/Mayu/D0/Mayu D0-06.ogg"
                ma "B-But I guess I should only say that if you were dressed as Aragear."
                "I shake my head."
                pf "It was lovely nonetheless."
                show mayu smi b2
                "She looks up at me and smiles, clearly more relaxed than before."
                show regBlush:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Mayu/D0/Mayu D0-07.ogg"
                ma "Thanks."
            
            "Continue quoting Lord of the GEARs.":
                pf "\"You cannot give me this.\""
                show mayu smi b3
                voice "audio/voice/E4/Mayu/D0/Mayu D0-08.ogg"
                ma "\"It is mine to give to whom I will.\""
                "Her blush deepens but she keeps eye contact with me."
                show heart:
                    xoffset 720
                    yoffset 135
                    xzoom 1
                    yzoom 1
                voice "audio/voice/E4/Mayu/D0/Mayu D0-09.ogg"
                ma "\"Like my heart.\""
                "I can feel my face heating up. Mayu's face is just as red."
                show mayu cur b2
                voice "audio/voice/E4/Mayu/D0/Mayu D0-10.ogg"
                ma "O-Oh! I-I'm really glad you knew the quote."
                pf "Of course."
                show mayu smi b2
                voice "audio/voice/E4/Mayu/D0/Mayu D0-11.ogg"
                ma "It's my favourite scene in the movie. It's so powerful."
                pf "You can tell the two characters care about each other so much... and want the best for one another regardless of their personal happiness."
                "Mayu nods then smiles warmly."
                show regBlush:
                    xoffset 720
                    yoffset 135
                    xzoom 1
                    yzoom 1
                voice "audio/voice/E4/Mayu/D0/Mayu D0-12.ogg"
                ma "I'm glad I can talk about this stuff with you."
                "I match her smile."
                pf "That's what I'm here for."
                show mayu ner b1 at cc with dissolve:
                    yoffset 0
                    xzoom 1
                    yzoom 1
    
    elif E3_5S4_Costume == "Officer":
        show dots:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        show mayu cur b2
        "She blinks at me, and a steady blush grows on her cheeks."
        voice "audio/voice/E4/Mayu/D0/Mayu D0-13.ogg"
        ma "Um... that is an interesting choice."
        pf "You don't like it?"
        show mayu ner b2
        voice "audio/voice/E4/Mayu/D0/Mayu D0-14.ogg"
        ma "No, I mean, umm... It's just a little... maybe..."
        pf "You don't have to like it. There's no problem with having a differing opinion."
        show mayu cur b2
        voice "audio/voice/E4/Mayu/D0/Mayu D0-15.ogg"
        ma "Oh! Well, in that case... I think that..."
        show mayu hap b2
        voice "audio/voice/E4/Mayu/D0/Mayu D0-16.ogg"
        ma "I think you could look better in other costumes!"
        "I smirk."
        pf "That wasn't so hard, right?"
        show mayu smi b2
        "She smiles triumphantly."
        show note:
            xoffset 720
            yoffset 135
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Mayu/D0/Mayu D0-17.ogg"
        ma "Right!"
        
    show mayu ner b1
    "Mayu looks back down again and shyly steps from one foot to the other."
    voice "audio/voice/E4/Mayu/D0/Mayu D0-18.ogg"
    ma "Umm... so… what do you think of my costume?"
    
    menu:
        "Cute!":
            pf "Super adorable of course!"
            show mayu cur b2
            "Mayu blushes."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-19.ogg"
            ma "You really mean that?"
            pf "Of course! It looks like it took some time to put together."
            show mayu smi b2
            voice "audio/voice/E4/Mayu/D0/Mayu D0-20.ogg"
            ma "Yes, it was a little hard to put on, but hearing you say you like it made the trouble worth it..."
            pf "Anytime."
            show heart:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            "She plays with her skirt but looks pleased nonetheless."
        
        "All that's missing is a tentacle monster!":
            pf "Don't magical girls usually fight monsters in mangas and anime?"
            show mayu smi b1
            voice "audio/voice/E4/Mayu/D0/Mayu D0-21.ogg"
            ma "That's right."
            pf "If only there was a friendly neighborhood octopus around."
            show mayu ske
            "Mayu furrows her eyebrows."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-22.ogg"
            ma "Oh, um... I'm not sure what you mean?"
            pf "Well, you know an octopus has tentacles."
            show mayu neu
            voice "audio/voice/E4/Mayu/D0/Mayu D0-23.ogg"
            ma "Yes..."
            pf "Magical girls and tentacles...?"
            show drop:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Mayu/D0/Mayu D0-24.ogg"
            ma "...I don't follow."
            show mayu ske
            "She tilts her head to one side and looks at me with curiosity."
            "There's no way she doesn't know what I'm hinting at! No one who likes mangas and anime can be that innocent."
            pf "You... really don't know what I mean?"
            show mayu neu
            "She shakes her head."
            voice "audio/voice/E4/Mayu/D0/Mayu D0-25.ogg"
            ma "Sorry..."
            "I pat her on the head."
            show mayu smi b1
            pf "Don't worry about it. It's an inside joke."
            "She blushes at my touch and nods."
            show heart:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Mayu/D0/Mayu D0-26.ogg"
            ma "O-Okay."
    
    stop music fadeout 3
    pf "Let's go meet up with the rest of the group?"
    voice "audio/voice/E4/Mayu/D0/Mayu D0-27.ogg"
    ma "Sure!"
    "Mayu beams and waits for me to lead the way."
    hide mayu with dissolve
    
    jump E3_5S5
