#
label E3D5S4:
    stop music fadeout 2
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    "The house is quiet when I get home. Uncle Kaito is still working his crazy hours and Nikki's probably still at her club."
    "Stifling a yawn, I trudge upstairs. It's been a long day and all I want to do is relax."
    stop ambient fadeout 3
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    scene black with fade
    # voice file for giggling?
    "As I pass by Nikki's room, I notice her door is closed. Huh, I guess she is home afterall. {w}I think nothing of it until I hear a deep, extremely male laugh behind Nikki's closed door. Nikki's giggle shortly follows."
    "WHAT.{w} IS.{w} THIS?"
    
    "There's a boy in Nikki's room? {w}And they're behind closed doors?! {w}Not on my watch!"
    # sfx?
    scene white with dissolve
    "I burst into her room."
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 3

    $ persistent.gpix[14][0] = 1
    $ persistent.gpix[15][0] = 1
    $ persistent.gpix[16][0] = 1
    $ persistent.gpix[17][0] = 1
    $ persistent.gpix[18][0] = 1
    $ persistent.gpix[19][0] = 1
    show cg nikki boyfriend 1 with dissolve:
        xzoom 0.5
        yzoom 0.5
        
    "Nikki's eyes widen and her mouth drops open. The boy twists to look at me from the chair beside the bed."
    pf "There's a boy in your room!"
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_001.ogg"
    sf "What are you doing?!"
    pf "Who is this guy?"
    show cg nikki boyfriend 2 with dissolve:
        xzoom 0.5
        yzoom 0.5
    "Nikki leaps from the bed and tries to push me away, but I stay rooted to the ground."
    pf "Is this Ken?"
    "I turn to the guy, ignoring Nikki pulling on my arm."
    pf "Are you Ken?"
    "He freezes like a deer in headlights, and stammers out an affirmation."
    stop music fadeout 5
    voice "audio/voice/E3/D5/S4/ken/1.ogg"
    ky "Y-Yes?"
    show cg nikki boyfriend 4 with dissolve:
        xzoom 0.5
        yzoom 0.5
        
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_002.ogg"
    sf "Leave him alone! We're just studying!"
    pf "\"Studying\"? Is that what the kids are calling it these days?"
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_003.ogg"
    sf "YES! What? No! \"Studying\" as in {i}studying{/i}!"
    "She points to her bed. I take another look around the room. Nikki's bed is sprawled with books, tablets, and laptops. Ken is holding an open textbook in his lap, a look of pure terror on his face. {w}I'm not fooled. I know underneath that \"good kid\" facade there is a demon just waiting to pounce on my cute, innocent imouto."
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_004.ogg"
    sf "Ken is in my class and we have an exam next week."
    "I glare at Ken, who cowers from my stare."
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_005.ogg"
    sf "Sooo, now that you know nothing weird is happening, you can leave."
    "I cross my arms."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
    pf "Actually, I think I'll stay and help you two study."
    show cg nikki boyfriend 3 with dissolve:
        xzoom 0.5
        yzoom 0.5
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_006.ogg"
    sf "What?!"
    pf "Whatever you're learning now, I already studied."
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_007.ogg"
    sf "Don't you have your OWN homework you can do? We're studying fine without you!"
    pf "Are you sure about that? I think {i}Ken{/i} here would appreciate the help."
    #stop music fadeout 3
    "I glare at Ken who gulps hard and nods."
    voice "audio/voice/E3/D5/S4/ken/2.ogg"
    ky "A-Actually, it would be an honor to have the help of an ACE pilot…"
    show cg nikki boyfriend 4 with dissolve:
        xzoom 0.5
        yzoom 0.5
    voice "audio/voice/E3/D5/S4/nikki/Nikki_4_008.ogg"
    sf "No, it wouldn't!"
    "I narrow my eyes at Ken. Very suspicious…"
    $ E3D5S4_Reaction = 0
    
    menu:
        "I've got my eyes on you.":
            $ E3D5S4_Reaction = 1
            pf "...Fine."
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_009.ogg"
            sf "Does that mean you'll LEAVE now?"
            "I never break eye contact with Ken."
            pf "I'm watching you, so whatever you're thinking, don't."
            "Ken nods rapidly, clearly shaken."
            voice "audio/voice/E3/D5/S4/ken/3.ogg"
            ky "I won't! I mean, I'm not thinking! I mean, not like that! Uh..."
            "I give him one final glare, before walking out of the room. {w}Nikki goes to close the door."
            pf "Door open."
            "She rolls her eyes."
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_010.ogg"
            sf "Fine, if that'll make you stop being crazy."
            "Before I leave, I make the universal \"I'm watching you\" sign with my fingers. Ken's eyes widen even further."
            scene black with fade
    
        "Don't try anything silly.":
            $ E3D5S4_Reaction = 2
            pf "Don't even think about it."
            "I didn't think it were possible, but Ken's eyes grow even wider. His gaze shifts helplessly to Nikki and back to me."
            voice "audio/voice/E3/D5/S4/ken/4.ogg"
            ky "I-I-There's nothing happening! I'm not thinking anything!"
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_011.ogg"
            sf "Get out! I'm not going to fail my test because you're being a total weirdo!"
            pf "Yeah, yeah, I'm leaving…"
            "I glare at Ken again."
            pf "Just remember, whatever you're thinking of doing to her, I will do to you."
            voice "audio/voice/E3/D5/S4/ken/5.ogg"
            ky "I-It's just math!"
            pf "{i}Twice.{/i}"
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_012.ogg"
            sf "Out!"
            "Nikki shoves me out of the room."
            pf "Door--"
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_013.ogg"
            sf "I know! We'll leave the door open so you stop being stupid."
            scene black with fade
    
        "Move him out of the room.":
            $ E3D5S4_Reaction = 3
            "Wordlessly, I cross the room and pull Ken to standing."
    
            if MCStory == 1:
                "I pick him up. He tenses as his feet leave the floor. Calmly, I carry him out of the room and close the door on him."
    
            else:
                "I grip his shoulders and steer Ken towards the door. Although clearly alarmed, he doesn't resist. Once outside of the room, I close the door on him."
    
            show cg nikki boyfriend 5 with dissolve:
                xzoom 0.5
                yzoom 0.5
                
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_014.ogg"
            sf "What are you doing?"
            pf "He clearly can't be trusted."
            show cg nikki boyfriend 6:
                xzoom 0.5
                yzoom 0.5
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_015.ogg"
            sf "He's not doing anything wrong!"
            show cg nikki boyfriend 5:
                xzoom 0.5
                yzoom 0.5
            pf "I didn't like that look he was giving you."
            "A hesitant knock is heard through the door. {w}Nikki glares at me."
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_016.ogg"
            sf "Let him back in."
            pf "Why?"
            show cg nikki boyfriend 6:
                xzoom 0.5
                yzoom 0.5
            ### VOICE - missing line
            voice "audio/voice/MISSING/BATCH7/Nikki_final_missed01.ogg"
            sf "Just let him in!"
            show cg nikki boyfriend 5:
                xzoom 0.5
                yzoom 0.5
            "Nikki looks about ready to burst."
            pf "Fine, but you have to keep the door open."
            show cg nikki boyfriend 6:
                xzoom 0.5
                yzoom 0.5
            voice "audio/voice/E3/D5/S4/nikki/Nikki_4_017.ogg"
            sf "Fine! But you have to promise to stop acting so crazy!"
            show cg nikki boyfriend 5:
                xzoom 0.5
                yzoom 0.5
            "I'm not the crazy one."
            "Regardless, as I open the door I'm greeted by a very confused Ken."
            show cg nikki boyfriend 2 with dissolve:
                xzoom 0.5
                yzoom 0.5
    
            # sfx dropping
            if MCStory == 1:
                "Gently picking him up, I carry him back into the room and plop him down in his chair."
    
            else:
                "I grip his shoulders and steer Ken back into the room, then plop him back down in his chair."
    
            pf "Continue."
            scene black with fade
            "I exit the room."
            
    scene bg homekaito myroom night with fade
    "Luckily, my room is across from Nikki's. I leave my door open too while I try to work on my assignments. I'm too distracted to focus as I strain to hear what they're talking about. Every so often I hear them repeat a math formula or compare answers on equations."
    stop music fadeout 5
    "Huh, I guess they really are studying… {i}this{/i} time!"
    "Eventually, I give up and watch videos on MeTube. {w}After about two hours, Ken goes home. Nikki slams the door shut to her room."
    "Sheesh, what's her problem?"
    scene black with fade
    "Now that I can finally focus again, I finish up my assignments and easily fall asleep afterwards."
    stop ambient fadeout 3
    
    jump E3D6S1