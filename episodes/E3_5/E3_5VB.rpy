#
label E3_5VB:
    
    show valerie smi at cc with dissolve
    "Valerie jumps in front of me just as I am about to walk."
    show valerie ske
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L3.ogg"
    vb "Hold on! I have to check something right {i}meow{/i}."
    pf "Hm?"
    "She looks me up and down."
    
    if E3_5S4_Costume != "Officer":
        show valerie dis
        "Valerie pouts."
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L4.ogg"
        vb "That's a bit tame. I thought you'd be a little more adventurous."
        
        menu:
            "Next time!":
                "Knowing Valerie, I should have realised she'd be disappointed in this choice."
                pf "Sorry, I'll pick something better next time."
                show valerie hap
                "She flashes me a playful smile."
                show heart:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L5.ogg"
                vb "I'm sure you will… I could even help you decide."
                "I'm almost afraid of what she'd pick for me…"
                show valerie smi
            
            "{i}Those{/i} ones are for the bedroom.":
                pf "I keep the \"adventurous\" ones for more private encounters."
                show valerie mis
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L6.ogg"
                vb "Now you're just being a tease!"
                pf "You're one to talk."
                show note:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                "She laughs."
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L7.ogg"
                vb "Alright mister, I'll let you get away with choosing this outfit... this time."
                show valerie smi
            
            "Meh.":
                pf "Oh well."
                show storm:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                "Valerie sighs."
                show valerie ner
                voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L8.ogg"
                vb "You can put in a little more effort for parties, y'know."
                pf "Uh, sure."
                "Valerie seems more disappointed by my attitude than the outfit."
                show valerie neu
    
    else:
        show valerie cur
        "Valerie places a finger on her lip and looks at me with innocent eyes."
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L9.ogg"
        vb "Hello, officer. I didn't expect to see you here."
        pf "Somebody called about a noise complaint."
        show valerie sur
        "Her eyes widen at my mischievous grin."
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L10.ogg"
        vb "I hope you're not about to do what I think you're about to do!"
        "I smirk and hold out my arm, then flex my bicep. The fabric tightens as I tense my muscles."
        show valerie smi
        "Valerie relaxes and smiles at my display of bravado."
        pf "Impressed?"
        show valerie hap
        "She giggles."
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L11.ogg"
        vb "At this rate you're going to attract the attention of all the other girls."
        pf "Are you jealous?"
        show valerie mis
        "Valerie smirks, a devilish glint in her eyes. She \"accidently\" drops the clutch in her hand."
        show shocked:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie sur
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L12.ogg"
        vb "Oh my, I'm so clumsy!"
        show valerie mis
        "Exaggerating her movements, she bends over and lingers with her fine behind in the air for a few seconds longer than necessary. Then she straightens up."
        "A commotion behind her catches my attention as two guys crash into each other. I narrow my eyes. I wonder what they were distracted by..."
        pf "Okay, you've made your point."
        show valerie ske
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L13.ogg"
        vb "Good, now you know how it feels."
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L14.ogg"
        vb "But just in case…"
        show valerie hap b1 at cc with dissolve:
            yoffset -100
            xzoom 1.25
            yzoom 1.25
        "She grabs my face and kisses me deeply. The heat rises in the pit of my stomach and I wrap my arms around her waist. Slowly, she pulls away, and I struggle to catch my breath."
        pf "What was that for?"
        show valerie mis b1
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L15.ogg"
        vb "Just a reminder so you don't forget who you belong to."
        "I grin, and lean in for another kiss. She responds eagerly and melts into me."
        pf "Ditto."
        show valerie smi b2 at cc with dissolve:
            yoffset 0
            xzoom 1
            yzoom 1
        "Her cheeks are flushed and she sighs contentedly."
        show heart:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L16.ogg"
        vb "With a kiss like that, there's no way I could forget."
    
    stop music fadeout 3
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L17.ogg"
    vb "C'mon, let's go meet up with the rest of the group."
    pf "Sure."
    hide valerie with dissolve
    "She smiles and leads the way."
    
    jump E3_5S5
