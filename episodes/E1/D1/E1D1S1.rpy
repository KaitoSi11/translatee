label E1D1S1:
    
    stop music fadeout 1
    
    scene black
    
    play ambient "audio/ambience/Bullet Train.ogg" fadein 4 fadeout 2

    $renpy.pause(2.0)
    
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    $renpy.pause(1.5, hard=True)
    
    
    voice "audio/voice/E1/D1/S1/Train Announcer/1.ogg"
    "Train Announcer" "Attention passengers:"

    voice "audio/voice/E1/D1/S1/Train Announcer/2.ogg"
    "Train Announcer" "We will be arriving at our destination shortly."

    voice "audio/voice/E1/D1/S1/Train Announcer/3.ogg"
    "Train Announcer" "Please ensure you have all your belongings prior to exiting."
    pf "...{w}...{w}..."
    
    $renpy.pause(.5)
    play sound "audio/sfx/Human/Poke_1.ogg"
    $renpy.pause(.75)
    
    pf "?!"
    
    "Something strikes my cheek! {w}I turn away from the window and see a small hand beside me."
    
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    #scene  bg travel train dusk with Dissolve(.1)
    scene white with dissolve
    scene bg travel train dusk at shaketrain with Dissolve(1.75)
    
    $renpy.pause(.25)

    
    show nikki smi b1 at cc with dissolve
    
    "Nikki." 
    
    "I glance at her sleeping form. She was always a bit of a restless sleeper. I move her hand back to her side, not as gently as I could have done it. We're almost there; she may as well wake up."

    play sound "audio/sfx/Human/Poke_1.ogg"
    $renpy.pause(.75)
    
    "She stirs and stretches with a wide yawn, hitting me in the face again. {i}That{/i} one she must have done on purpose!"
    
    show nikki neu at cc with Dissolve(.75)
    $renpy.pause(.25)
    
    $renpy.pause(.25)
    voice "audio/voice/E1/D1/S1/Nikki/1.ogg"
    sf "Oh, hey, bro. Looks like I dozed off there... Did you sleep well?"
    
    menu:
        "Revenge!":
            
            "I glance at her out of the corner of my eye and stretch just as widely, catching her on the cheek."
            
            play sound "audio/sfx/Human/Poke_1.ogg"
            show nikki win at cc, Shake(None, .3, dist=6)
            #Need shake effect
            $renpy.pause(.75)
            show nikki ann with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/2.ogg"
            sf "Hey!"
            
            
            show nikki ann
            "She swats back at me, but I just laugh."
            pf "Oh, sorry. I didn't see you there."
            voice "audio/voice/E1/D1/S1/Nikki/3.ogg"
            sf "Rude!"
        "What is this \"sleep\" you speak of?":
            pf "I couldn't sleep."
            show nikki cur
            voice "audio/voice/E1/D1/S1/Nikki/4.ogg"
            sf "Why not?"
            pf "I'm pretty sure there was a bear sleeping near me... at least, that's what it sounded like."
            show nikki sur with dissolve
            "Her eyes grow wide."
            voice "audio/voice/E1/D1/S1/Nikki/5.ogg"
            sf "Are you trying to say I snore?"
            pf "Honestly, I'm surprised it didn't wake you."
            show nikki dis with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/6.ogg"
            sf "You're joking, right? Do I really snore?"
            pf "How can such a small person make such a {i}loud{/i} noise?"
            show nikki wor
            voice "audio/voice/E1/D1/S1/Nikki/7.ogg"
            sf "Oh my god, I can never show my face in public again! Long rides are going to feel even longer if I can't nap! And what about sleepovers? Can I even get a boyfriend?"
            "I can't keep a straight face any longer and burst out laughing."
            pf "Nah, you're fine, sis. It was the guy behind us."
            show nikki ann with dissolve
            play sound "audio/sfx/Human/light_punch.ogg"
            with Shake((0, 0, 0, 0), .5, dist=5)
            "She hits me in the arm."
            voice "audio/voice/E1/D1/S1/Nikki/8.ogg"
            sf "That is not funny!"
            show nikki neu with dissolve
            "But I can see the smile threatening to escape her lips."
        "*grumble grumble*":
            "Folding my arms across my chest, I sink back into my seat and mutter under my breath. If I had been asleep, that would have been a rude awakening, so I think I'm entitled to be little grumpy."
            show nikki smi with dissolve
            voice "audio/voice/E1/D1/S1/Nikki/9.ogg"
            sf "D'aww, someone's a little cranky-pants!"
            "As she pats my head, I sink deeper into my seat, my protests gradually devolving into nothing more than a low growl."
            pf "Grrr…"
            "Nikki beams at me. At least one of us is enjoying this."
    

    "The sun shines in my eyes, catching my attention. {w}The sky is ablaze with deep reds and orange as the sun creeps towards its reflection on the glittering ocean. {w}A soft breeze ripples the trees beyond the coast. The leaves seem to wave goodbye to us as we race past." 
    
    hide nikki with dissolve
    show nikki cur at r2 with dissolve
    voice "audio/voice/E1/D1/S1/Nikki/10.ogg"
    sf "Doesn't it look like something out of a fairy tale?"
    
    stop music fadeout 5
    show nikki hap with dissolve
    "There's a smile on her lips, but her warm eyes search my own. After a moment, she looks down and slinks back into her chair." 
    
    show nikki thi
    voice "audio/voice/E1/D1/S1/Nikki/11.ogg"
    sf "You know, you didn't have to come too... You were already in your first year at CINY, and well... you didn't have to come too."
    
    $ E1D1S1_nikkimad = 0
    menu:
        "Great! Back I go then.":
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
            pf "That's a relief! I'll just wait for this train to turn around and then I'll take the first flight back to the States."
            show nikki wor
            voice "audio/voice/E1/D1/S1/Nikki/12.ogg"
            sf "Ah!? Umm..."
            "Her eyes grow wide and she bites her lip, trying to keep the worry out of her face." 
            "I can't help but laugh."
            pf "We're starting over here. A new life. There's no way I'd let you do that alone."
            show nikki neu with dissolve
            "Relief floods her face as she smiles."
            pf "But more importantly, I heard Japanese college girls are total babes."
            show nikki smi
            "Nikki's smile stays, but she rolls her eyes."
            voice "audio/voice/E1/D1/S1/Nikki/13.ogg"
            sf "You're ridiculous."
        "That's what big brothers are for.":
            play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
            pf "After everything that's happened… we're all we've got left. I wouldn't be a very good big brother if I let you move here alone."
            show nikki neu with dissolve
            "She sighs, but a smile plays at her lips."
            voice "audio/voice/E1/D1/S1/Nikki/14.ogg"
            sf "How did I know you were going to say something like that?"
        "Someone has to take care of you.":
            $ E1D1S1_nikkimad = 1
            pf "If I don't come, who will take care of you?"
            show nikki ann
            "Nikki frowns and her eyes lose their warmth."
            voice "audio/voice/E1/D1/S1/Nikki/15.ogg"
            sf "No one {i}needs{/i} to take care of me. I'm not a kid anymore. I'm about to start my last year of high school!"
            pf "That's not what I meant."
            "It's easy to forget she's no longer that little girl who pretends to be sick because she's too nervous to start her first day of school. {w}We've just been uprooted from the only life we've ever known, and yet Nikki is the epitome of calm as she waits for our train to stop."
            pf "Nikki…"
            hide nikki with dissolve
            $renpy.pause(.25)
            "But she's already turned her back to me and is fussing with her purse."  
    
    stop music fadeout 3
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    $renpy.pause(1.5, hard=True)
    
    voice "audio/voice/E1/D1/S1/Train Announcer/4.ogg"
    "Train Announcer" "We have arrived at Isokaze Station. Please stand clear of the doors."
    
    if (E1D1S1_nikkimad == 1) :
        "I can't help but feel a little bad."
    else:
        show nikki smi
        voice "audio/voice/E1/D1/S1/Nikki/16.ogg"
        sf "Oh, that’s our stop! C’mon!"
    
    scene black with fade
    jump E1D1S2
    