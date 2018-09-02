#
label E4D2VB:
    
    "As I glance around the group, everyone seems to be focused on the greenery around us… everyone except for a certain adventurous blonde…"
    "I spot Valerie a few steps off the pathway, staring into a small pond. A strong weeping willow droops its branches around her, partially obscuring her from view."
    "When no one is paying attention, I slip away from the group."
    show valerie neu at cc with dissolve
    pf "Valerie!"
    show valerie smi
    "She grins."
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L2.ogg"
    vb "I knew you'd come find me."
    stop music fadeout 3
    pf "We should get back to the group."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show valerie smi b1 at cc with dissolve:
        yoffset -100
        xzoom 1.25
        yzoom 1.25
    "She leans in close and playfully draws circles on my chest."
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L3.ogg"
    vb "Why? Don't you want to be alone with me?"
    "I quickly look around in case anyone is watching, but no one's in sight…"
    show valerie hap b1
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L4.ogg"
    vb "We could go on our own secret adventure."
    
    menu:
        "No, we should rejoin the group.":
            pf "As fun as that sounds, I don't want to get everyone in trouble because we're walking where we aren't supposed to."
            show valerie dis at cc with dissolve:
                yoffset 0
                xzoom 1
                yzoom 1
            "Valerie pouts."
            show storm:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L5.ogg"
            vb "Where's your sense of adventure?"
            pf "I'd feel more adventurous if we were together back home… without the group."
            show valerie mis
            "Valerie's smirk returns."
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L6.ogg"
            vb "I suppose we can postpone our adventure for later."
            scene black with fade
            "Together, we head back to the path and rejoin the group unnoticed."
            jump E4D2S2
        
        "I like where this is going.":
            "I wrap my arms around her but she slips from my grasp. Her playful smile taunts me."
            show valerie smi at cc with dissolve:
                yoffset 0
                xzoom 1
                yzoom 1
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L7.ogg"
            vb "Let's go then."
            hide valerie with dissolve
            "She runs further into the garden towards a grove of trees."
            pf "Hey, wait!"
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L8.ogg"
            vb "Make me!"
            "Then she disappears among the branches. I race after her, but she's nowhere to be found. {w}After weaving through the trees, I slow down, trying to guess which direction she's gone."
        
            if MCStory == 3:
                "The hair on my neck rises and I feel a presence. Valerie jumps out from among the leaves and pounces on me."
            
            else:
                "Just as I'm about to lose hope, Valerie jumps out from the leaves and pounces on me."
    
            # sfx ?
            # screen shake and delay ?
            stop music fadeout 3
            show valerie smi b1 at cc with dissolve:
                yoffset -100
                xzoom 1.25
                yzoom 1.25
            "Startled, I barely catch her in time as we topple to the ground. Valerie pins me. Her hair tickles my cheek."
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L9.ogg"
            vb "You're trapped."
            # shake sprite?
            play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
            show valerie cur b2 with dissolve
            "Two can play at that game. A slow smile spreads across my face and Valerie looks at me with confusion. Then she lets out a short cry as I roll over and pin her to the ground."
            pf "Now who's the trapped one?"
            show valerie smi b2
            "To my surprise, Valerie grabs my face and pulls me into a kiss. I melt into the sweetness of her lips and linger in the sensation. {w}All too soon, she pulls away, leaving me breathless. {w}How could I have ever gotten so lucky?"
            "Valerie's blue eyes sparkle."
            show heart:
                xoffset 770
                yoffset 125
                xzoom .7
                yzoom .7
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L10.ogg"
            vb "You got me."
            pf "I did. {w}What happens now?"
            show valerie mis b2
            "She slowly wraps her arms around my neck, never losing her mischievous smile."
            voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L11.ogg"
            vb "Usually this is the part where it fades to black and implies certain {i}activities{/i} have happened."
            "I grin."
            #fade to black
            stop music fadeout 3
            scene black with fade
            "We spent some time together and then rejoin the group."
            
            jump E4D2S2
