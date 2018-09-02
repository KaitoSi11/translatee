#
label E4D7VB:

    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sFlirty"
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L1.ogg"
    vb "Long time no see. Haven't had enough of me yet?"
    pf "Valerie, can we meet?"
    "She pauses. Concern replaces the playfulness in her voice."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L2.ogg"
    vb "Is everything okay?"
    pf "I… I don't know."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L3.ogg"
    vb "Where are you right now?"
    pf "At the Hangar."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L4.ogg"
    vb "Okay, I'll be right there."
    pf "No! Wait."
    pf "I… Do you think I could maybe go to you?"
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L5.ogg"
    vb "Okay."
    "She doesn't even bother with a playful retort. Do I sound that serious?"
    pf "Thanks, I'll be right there."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop ambient fadeout 3
    scene black with fade
    #play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    $renpy.pause(1.25)
    "We hang up, and as if in a daze I make my way over to Valerie's dorm. She buzzes me in and greets me at her door with a wide a smile, which turns into a worried smile as soon as she sees me. {w}Without a word, she stands aside and lets me in, then leads me to her bed."
    scene bg vacation hotel night with fade
    show valerie smi at cc with dissolve
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L6.ogg"
    vb "This isn't exactly how I expected your first visit to my room to go."
    "I glance at her roommate's neatly made bed."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L7.ogg"
    vb "She's out with some friends."
    show valerie smi
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L8.ogg"
    vb "What a wasted opportunity, huh?"
    "I chuckle weakly."
    
    
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    
    if E4D7S2_CoreDestroyed == 1:
        pf "Look, there's something I need to tell you. It's about my core."
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L9.ogg"
        vb "What is it?"
        pf "It's gone."
        show valerie sur
        "Valerie winces and lets out a small cry."
        show shocked:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L10.ogg"
        vb "Oh my god! Did somebody try to sabotage Eagle?!"
        
        "Before I answer she jumps off the bed and rummages through her desk."
        show valerie ann
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L11.ogg"
        vb "Don't worry, I saved the schematics so we can still put it back together again."
        pf "Valerie--"
        show valerie ang
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L12.ogg"
        vb "Who would stoop so low as to mess with your GEAR? Isn't that rules for expulsion or something?"
        pf "Valerie!"
        show valerie wor at cc with dissolve
        "She freezes."
        pf "I did this."
        show dots:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "She continues to stare at me."
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L13.ogg"
        vb "...Why?"
        pf "Because I had to."
        hide valerie with dissolve
        $renpy.pause(.5)
        "Valerie returns to the bed as I fill her in on everything I'd learned. My thoughts are scattered as but Valerie listens patiently. {w}Once I've finished, she looks at her desk."
    
    else:
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L14.ogg"
        vb "So, what have you got in your hand?"
        "I show her the drive."
        show question:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie ske
        "Valerie gives me a questioning look."
        show valerie neu
        pf "It's the data to my core."
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L15.ogg"
        vb "Your… core…"
        pf "Yeah."
        show valerie ske
        voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L16.ogg"
        vb "Okay, glad we got that cleared up. What exactly is it doing out of Eagle?"
        pf "Well…"
        hide valerie with dissolve
        $renpy.pause(.5)
        "Valerie listens attentively as I explain everything I'd learned. Even though my story jumped from one part to the next and back, she let me do most of the talking and hardly ever interrupted with questions. {w}After I finish, she stares at her desk."
    
    show valerie neu at cc with dissolve
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L17.ogg"
    vb "I see."
    pf "I know it's a lot to take in at once."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L18.ogg"
    vb "I understand why you did what you did."
    pf "Really?"
    show valerie neu
    "She nods."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L19.ogg"
    vb "And I think you did the right thing."
    "A heavy weight seems to lift off my shoulders. I hadn't realised just how much I was worried I'd made the wrong decision until Valerie validated my choice."
    show valerie wor
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L20.ogg"
    vb "But knowing that you aren't going to keep your core, what do you want me to do with the blueprints?"
    
    
    menu:
        "Delete it.":
            pf "Get rid of it."
            show drop:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie win
            "Valerie cringes, but nods."
            pf "I'm sorry, I know how much cracking this core meant to you."
            show valerie neu
            "She shakes her head."
            voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L21.ogg"
            vb "Obviously the engineer in me cries out in pain hearing that I have to destroy all that research, but the girlfriend in me agrees with you."
            show valerie smi
            "She flashes me that irresistible smile of hers."
            voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L22.ogg"
            vb "Just give me a minute to mourn?"
            "I didn't think I had it in me, but a laugh escapes."
            pf "You don't have to do it this second. I'll give you two a minute alone."
        
        "I'd rather keep dad's legacy alive.":
            pf "Nothing..."
            show valerie cur
            "She blinks."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L23.ogg"
            vb "Nothing?"
            pf "Nope. Let's keep the blueprints but don't let anyone know you have them."
            show valerie cur
            voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L24.ogg"
            vb "It'll be our little secret."
            pf "But for now, don't try to recreate the core either."
            show valerie dis
            "She pouts."
            show storm:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L25.ogg"
            vb "Aw, there goes your next birthday present."
            show valerie smi
            "She cracks a smile and I can't help but smile back."
            pf "I'm sure you'll think of something else."
            
    stop music fadeout 5
    show valerie neu
    "We fall silent."
    pf "I'm sorry, I know I must be kind of a drag to be around right now."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L26.ogg"
    vb "A little bit."
    "I crack another smile."
    pf "Gee, tell me how you really feel."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L27.ogg"
    vb "Hey, I'm just being honest! Honesty is the foundation of a relationship after all."
    "Honesty. {w}What would have happened if Dad had been honest with me about the core? Would he still be here? {w}Would I have forgiven him? Maybe he was right to keep this from me."
    show valerie smi
    "Valerie snuggles into my chest."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L28.ogg"
    vb "Hey."
    pf "Hey."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L29.ogg"
    vb "He loved you, you know."
    "I don't answer."
    show valerie neu
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L30.ogg"
    vb "I'm not going to pretend to know your father, but my guess is he had plenty of long nights debating the exact same thing you're wondering now."
    show valerie neu
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L31.ogg"
    vb "I don't know how many times I caught my mom seemingly staring at nothing while her coffee grew cold."
    show valerie neu
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L32.ogg"
    vb "Parents aren't perfect. They make mistakes too."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L33.ogg"
    vb "But that doesn't mean they don't care."
    show valerie neu
    "She pulls away and looks me in the eyes."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L34.ogg"
    vb "Obviously you have a lot of questions and want more answers, and that's okay. But don't forget that we can't change what's already happened."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L35.ogg"
    vb "It sucks that somebody else made this huge decision for you about your core, but at least {i}you{/i} get to decide what happens next."
    "She's right. There's no point in being angry or hurt. I can't change what Dad did. I don't want to remember him as someone I'm unsure about. I want to remember him as the father who worked long days and even longer weeks yet still managed to make time for his kids."
    stop music fadeout 5
    pf "When did you become an expert on parents?"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L36.ogg"
    vb "I'm an expert on many things--especially when it involves making you feel better."
    pf "Are you sure I'm feeling better now?"
    show valerie mis
    "Her mischevious grin returns."
    voice "audio/voice/E4/Valerie/ValE4D7/ValE4D7L37.ogg"
    vb "Let's check."
    show heart:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/music/Timeless.ogg" fadein 2
    show valerie hap b1 with dissolve
    "She throws her arms around my neck and kisses me. As she melts into me, we both fall back onto the bed and I give in to the warmth of her curves. Gently, she pulls away and smiles. I stare deeply into her blue eyes and feel a calm like the salty spray of the ocean wash over me."
    show valerie smi b2 with dissolve
    "In this moment, I have clarity. It rinses away all my stress and fears."
    "It's okay that I don't have all the answers now, because I'm looking at my future...{p}\n...and it is beautiful."

    jump E4Epilogue