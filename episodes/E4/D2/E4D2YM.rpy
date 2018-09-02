#
label E4D2YM:
    
    "As I glance around the group, everyone seems to be focused on the greenery around us. I look out past the field of flowers and admire how far and wide the garden is. It is pretty impressive."
    "A flash of striped fur peeks out amid the colourful petals. What was that?!"
    "A few paces later, I catch another glimpse of a grey striped tail before it disappears back among the flowers."
    "Is… Is that a lemur?!"
    
    menu:
        "There are no lemurs in Japan, stupid.":
            "Doubtful. I'm sure there are other animals with black and white striped tails. I should stick with the group and not wander off on my own."
        
        "Go investigate!":
            "Whoa, does this garden have exotic animals too? I've got to find out."
            "I step off the path and venture into the grass, careful not to step on any of the flowers. I'm not sure where the lemur went but they like trees, right? I steer towards a small grove of trees as I go deeper into the garden. {w}Right when I'm about to enter the grove, I pause. {w}Is that a voice? Turning around I spot Yuuna."
            show yuuna ner at cc with dissolve
            "She pants as she catches up to me."
            voice "audio/voice/E4/Yuuna/E4/D2/3.ogg"
            ym "Finally! Didn't you hear me calling you?"
            pf "No, sorry. What are you doing here? Why aren't you with the group?"
            show yuuna ske
            voice "audio/voice/E4/Yuuna/E4/D2/4.ogg"
            ym "I should be asking you that!"
            show yuuna wor
            voice "audio/voice/E4/Yuuna/E4/D2/5.ogg"
            ym "We're not supposed to deviate from the path. You could get in so much trouble!"
            voice "audio/voice/E4/Yuuna/E4/D2/6.ogg"
            ym "Come on, we need to go back."
            stop music fadeout 5
            "Yuuna grabs my hand."
            pf "Wait! We can't go back yet."
            show yuuna sur
            "She's about to reply when we hear a rustling in the bushes behind us. Yuuna's eyes grow wide."
            play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
            show frightful:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Yuuna/E4/D2/7.ogg"
            ym "What was that?"
            pf "I'm not sure…"
            "There's a chance it could be something dangerous. Is that why we're not supposed to stray from the path?"
            "The rustling intensifies."
            show yuuna wor
            pf "Yuuna! Get back!"
            hide yuuna with dissolve
            "Out of instinct, I step between Yuuna and the bushes and throw out my arms to protect her. Just as I get into position, a dainty cat hops out of the bush and pauses."
            "It wags its grey striped tail and licks a paw, then runs away."
            stop music fadeout 5
            "My cheeks redden as I realise what I'd done. I just tried to save Yuuna from a {i}cat{/i}."
            "I turn around and rub the back of my head, trying to ignore the heat in my cheeks."
            pf "Sorry, false alarm."
            play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
            show yuuna smi b2 at cc with dissolve
            "To my surprise, Yuuna's cheeks are just as red as mine and a broad smile graces her lips. Her eyes sparkle as she looks at me with admiration."
            pf "...What?"
            voice "audio/voice/E4/Yuuna/E4/D2/8.ogg"
            ym "You put yourself in danger to protect me."
            pf "It was just a cat."
            "She shakes her head."
            show yuuna hap b2
            voice "audio/voice/E4/Yuuna/E4/D2/9.ogg"
            ym "No! I mean, yeah, it was, but you didn't know that! You thought it was something dangerous and you didn't want me to get hurt."
            "My face feels even hotter as I try to stammer out a reply."
            pf "I-It's nothing, I just wanted you to be s--"
            show heart:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna smi b2
            "Yuuna cuts me off with a kiss as her lips press against mine. I blink in surprise, then melt into her kiss. Her hands rest on my chest as she gently pulls away. {w}Wrapping my arms around her, I pull her in close and kiss her again."
            #black screen
            scene black with fade
            "We spent some time together before rejoining the group."
            
    jump E4D2S2
