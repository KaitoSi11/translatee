#
label E3D3S3:
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    "As I enter the house, I hear soft giggles coming from the living room. A tuft of blonde hair peeks over the couch. Another wave of giggles floats from the couch, but cease abruptly as I step closer. {w}Nikki hangs up the phone and turns around to greet me."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show nikki neu at cc with dissolve
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_001.ogg"
    sf "Hi, big bro."
    "I plop down next to her."
    pf "Who was that guy?"
    show nikki sur b1
    "Her eyes grow wide."
    show panic:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_002.ogg"
    sf "H-How did you know it was a guy?"
    
    menu:
        "Who else could it be?":
            pf "I'm psychic."
            show nikki ske b1
            voice "audio/voice/E3/D3/S3/nikki/Nikki_3_003.ogg"
            sf "No, you're not."
            pf "You've never giggled on the phone before."
            show tsuBlush:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki dis b2
            voice "audio/voice/E3/D3/S3/nikki/Nikki_3_004.ogg"
            sf "I wasn't giggling!"
            "The blush in her cheeks tells me all I need to know."
    
        "You just told me.":
            pf "I didn't, but I do now."
            show nikki dis b1
            "She pouts."
            voice "audio/voice/E3/D3/S3/nikki/Nikki_3_005.ogg"
            sf "That's tricky!" 
    
        "Just stare at her.":
            "I continue to look at her."
            show nikki ner b1
            voice "audio/voice/E3/D3/S3/nikki/Nikki_3_006.ogg"
            sf "What?"
            pf "Do I really need to answer that?"
    
    pf "So, who was it?"
    show nikki thi b1
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_007.ogg"
    sf "No one."
    pf "Doesn't sound like no one…"
    show nikki dis
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_008.ogg"
    sf "He's just a classmate."
    show nikki cur
    "I reach around and grab Nikki's phone while she's distracted."
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki sur
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_009.ogg"
    sf "NO! GIVE IT BACK!"
    show nikki ann
    "She screams in my ear as she leaps over me, reaching towards her phone. I fend her off and keep the phone away from her grasping hands. As she continues to struggle, I worm my way off of the couch and flip through her call list before she can scramble to her feet."
    "The last dialed number is to a \"KEN\"."
    pf "What kind of weird Japanese name is {i}Ken{/i}?"
    "Nikki snatches the phone right as I speak, then pummels my chest with her fists."
    show nikki ang
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_010.ogg"
    sf "Oh my god! You are such a jerk!"
    show nikki ann
    pf "Is he even a real person?"
    show vein:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki ang
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_011.ogg"
    sf "Of course he is!"
    show nikki ann
    pf "But his name is {i}Ken{/i}."
    show nikki win
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_012.ogg"
    sf "Ugh! You're the worst!"
    # screen shake?
    # sfx
    play sound "audio/sfx/Human/light_punch.ogg"
    hide nikki with dissolve
    stop music fadeout 5
    "She hits me hard one last time before turning on her heel and storming upstairs."
    "When she's halfway to the top, she pauses."
    # reverb?
    voice "audio/voice/E3/D3/S3/nikki/Nikki_3_013.ogg"
    sf "And by the way, \"Ken\" means \"strong\" in Japanese!"
    # distant door slamming sfx?
    "Nikki stomps into her room and slams the door."
    pf "Oh yeah… Oops…"
    # kaito laugh voice ?
    "Still, \"Ken\"...{w}Hahaha!"
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
    "I hear laughter. {w}Is that me? Did I just laugh out loud?"
    show kaito smi at cc with dissolve
    "Kaito is leaning against the doorway behind me, a broad smile on his face. I jump when I see him."
    "First Akira and now Kaito… how is everyone always sneaking up on me?!"
    show kaito mis
    voice "audio/voice/E3/D3/S3/kaito/1.ogg"
    hk "Haha! That's good. Ken {i}is{/i} a funny name! It's like…"
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito hap
    voice "audio/voice/E3/D3/S3/kaito/2.ogg"
    hk "YEN! Hahaha!"
    "He continues laughing at his \"joke\", then gradually calms down."
    show kaito ske
    voice "audio/voice/E3/D3/S3/kaito/3.ogg"
    hk "Why does your face look like that?"
    pf "Like what? I always look like this."
    show kaito neu
    voice "audio/voice/E3/D3/S3/kaito/4.ogg"
    hk "No, like this."
    show confused:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito sur with dissolve
    "He mimics a look of cringing and disbelief."
    pf "I don't--what? {w}I should go do my homework…"
    show kaito mis
    voice "audio/voice/E3/D3/S3/kaito/5.ogg"
    hk "Good idea, get smart!"
    hide kaito with dissolve
    stop music fadeout 5
    "I slowly head towards the stairs, still unsure about what just happened."
    # stairs sfx
    scene black with fade
    "As I walk up the steps, I can still hear faint chuckles from Kaito and the echoes of \"Ken Yen\"."
    scene bg homekaito myroom night with fade
    "Since I was already in my room, I caught up on studying until it was time for sleep."
    #black screen
    scene black with fade
    stop ambient fadeout 3
    
    jump E3D4S1

