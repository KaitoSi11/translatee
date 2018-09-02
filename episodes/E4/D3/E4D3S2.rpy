#
label E4D3S2:

    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    ### NOTE - scene contains edits of parts removed / changed
    
    stop ambient fadeout 3
    #stop music fadeout 3
    scene black with fade
    "It's about time for our session with Coach Ivan. I double check my email, then make my way to the precombat room. That's where we're supposed to meet him."
    #play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus battleroom day with fade
    "As I walk in, I see the rest of my team crowded around the holotable."
    show yuuna smi at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu smi at l2  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show shou smi at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    show valerie smi at r3 behind kaori with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
        
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L1.ogg"
    vb "I can't believe he sent all this. This is incredible!"
    show yuuna hap
    "Yuuna grins." # proudly
    show note:
        xoffset 5
        yoffset 100
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Yuuna/E4/D3/1.ogg"
    ym "Yup! This consultation isn't just for the pilots. It's for everyone on the team."
    show yuuna smi
    "Valerie scrolls through the projected hologram pausing at an image of a GEAR loaded with statistics. {w}As I approach, I can make out what looks like the game plans of previous professional matches, complete with sketches, tactics, movements, and calls. This sort of edited information is incredibly valuable for all parties on the team."
    show shou cur
    "Shou is the first to notice me."
    show exclamation:
        xoffset 625
        yoffset 20
        xzoom .5
        yzoom .5
    show shou hap
    voice "audio/voice/E4/Shou/d3/1 Copy.ogg"
    ss "Broseph!"
    "Once he sounds my arrival, the rest of my team grin or wave at me."
    show shou smi
    pf "Hey guys."
    "Shou puts an arm around my shoulder."
    show shou mis
    voice "audio/voice/E4/Shou/d3/2 Copy.ogg"
    ss "Are you ready to meet Ivan?!" # I mean, meeting a pro war gamer is intense, but one that won two MVPs?!"
    pf "You know it!"
    
    #if yuurelatonship == 1:
        #"I glance again at Yuuna and grin when she catches my eye."
        #pf "I still have no idea how you set this up. Can you be even more amazing?"
        #"She blushes."
        #ym "Hopefully today's coaching session is beneficial. I have other ideas down the pipeline I'd love to make happen too."
        #ss "That'd be awesome!"
        
    #else:
        #"Shou looks at Yuuna."
        #ss "You're awesome!"
        #"Yuuna blushes."
        #ym "Thank you."
        
    show shou smi
    "There's nothing left to do but wait for Ivan to arrive. {w}Valerie and Mayu continue to scroll through the holotable while the rest of us take seats on the couches lining the walls."
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_01.ogg"
    ki "What do you guys think Coach Ivan is like?"
    "Is Kaori nervous? She keeps a cool facade but her gaze constantly darts towards the door."
    show shou mis
    voice "audio/voice/E4/Shou/d3/3 Copy.ogg"
    ss "I heard he's the shot caller on his team. He's the one leading the tactics and pulling in the high numbers."
    show mayu hap
    voice "audio/voice/E4/Mayu/D3/Mayu D3-01.ogg"
    ma "Mhm, he's received the MVP award twice already!"
    show shou smi
    show mayu smi
    "I remember they'd mentioned that yesterday as well… I wrack my brain trying to understand why I hadn't heard of him before."
    pf "The only player I remember who won two MVP awards on the national stage is \"Strong Arm Gear\"."
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_02.ogg"
    ki "Right. That's his alias for the global stage."
    show mayu cur
    voice "audio/voice/E4/Mayu/D3/Mayu D3-02.ogg"
    ma "I always thought it was a little strange that he never even took off his helmet for interviews."
    show valerie mis
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L2.ogg"
    vb "He doesn't need to. He doesn't even speak in interviews."
    show mayu neu
    show kaori smi
    "Kaori nods."
    pf "What?"
    show yuuna mis
    show valerie smi
    voice "audio/voice/E4/Yuuna/E4/D3/2.ogg"
    ym "That's his persona... and it's worked really well for him."
    show mayu smi
    "Hearing all of this just makes me even more curious about what kind of person Coach Ivan is."
    show question:
        xoffset 625
        yoffset 20
        xzoom .5
        yzoom .5
    show shou ske
    voice "audio/voice/E4/Shou/d3/4 Copy.ogg"
    ss "Wait, how is he going to coach us? Does he even know how to talk?"
    show kaori ske
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_03.ogg"
    ki "Don't be stupid Shou. Of course he can talk."
    show dots:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori cur
    "Kaori blinks."
    
    show kaori thi
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_04.ogg"
    ki "...I think."
    #"We all look at Yuuna."
    #ym "Y-Yes! Of course he talks."
    #vb "You spoke with him?"
    #ym "No... I spoke with his manager..."
    show shou neu
    stop music fadeout 5
    voice "audio/voice/E4/Shou/d3/5 Copy.ogg"
    ss "Actually, I've heard rumors that his face was half burnt during a racing motorcycle accident. That's why he always wears a helmet."
    show kaori neu
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_05.ogg"
    ki "I think I remember reading that too."
    "Ouch! I cringe just remembering the rare couple of times I fell off my bike… I don't even want to imagine how painful it would be to fall off my bike while {i}racing{/i}."
    show mayu wor
    voice "audio/voice/E4/Mayu/D3/Mayu D3-03.ogg"
    ma "W-What if he's scary…?"
    show valerie mis
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L3.ogg"
    vb "I've heard he yells at first year pilots... or worse."
    show mayu sur
    "Mayu's eyes widen."
    show panic:
        xoffset 320
        yoffset 135
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Mayu/D3/Mayu D3-04.ogg"
    ma "W-What?"
    show valerie hap
    "Valerie pats Mayu sympathetically on the back."
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L4.ogg"
    vb "It was nice knowing you."
    show mayu sad
    voice "audio/voice/E4/Mayu/D3/Mayu D3-05.ogg"
    ma "N-No… but why?"
    "Her eyes well up with tears."
    show kaori dis
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_06.ogg"
    ki "Stop being mean, Valerie."
    
    if mayrelatonship == 1:
        show mayu cur b1
        "I place an arm around Mayu."
        pf "I won't let anything happen to you."
        show mayu smi b2
        "She looks up at me and blushes."
        show regBlush:
            xoffset 450
            yoffset 135
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Mayu/D3/Mayu D3-06.ogg"
        ma "Okay."
        show mayu smi b1
        pf "Valerie's just teasing anyway."
        
    else:
        voice "audio/voice/E4/Shou/d3/6 Copy.ogg"
        ss "Don't listen to Valerie. She's just teasing."
        
    "Valerie smirks." # leans back into her seat and smirks."
    voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L5.ogg"
    vb "Or am I?"
    $renpy.pause(0.25)
    # sfx ?
    hide valerie with dissolve
    hide kaori
    hide shou
    with dissolve
    hide mayu
    hide yuuna
    with dissolve
    $renpy.pause(0.5)
    show yuuna ner at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show shou ner at l1 with dissolve:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    show kaori ner at r1 with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    show valerie ner at r2 with dissolve:
        xoffset 50
        yoffset 35
        xzoom 0.75
        yzoom 0.75
    "The door slides open, catching all of our attention."
    
    
    "A muscular man, well over 6 feet tall, commands the room. He's wearing a leather jacket with black pants. A polished helmet hides his face."
    "He crosses the room with thunderous steps and pauses before us, as large and silent as a mountain."
    
    $ ivaHelmet = "1"
    $ ivaOut = "default"
    
    show ivan neu at r3 with dissolve:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    "The group glances nervously at each other other. Nobody wants to break the silence."
    pf "Er, hello."
    "His helmet slowly turns towards me, and I fidget beneath his gaze. I can't see his eyes, which makes this all the more disconcerting. {w}After a moment, his helmet surveys the rest of the team. {w}Kaori remains stoic while Mayu tries to make herself small. Both Yuuna and Valerie look uncertain while Shou seems confused about how he should feel."
    stop music fadeout 3
    "Coach Ivan nods. He puts his hands on either side of his helmet."
    hide ivan with dissolve
    "Shou catches my eyes in anticipation. Are we actually going to see what's underneath the helmet?"
    
    $ ivaHelmet = "0"
    $ ivaOut = "open"
    

    show ivan smi at r3 with dissolve:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    "Coach Ivan pulls it off in one sweeping motion, revealing a shiny bald head and the most beautiful mustache I've ever seen. Underneath his mustache is a beaming smile."
    show ivan hap
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    show note:
        xoffset 1575
        yoffset 5
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Ivan Poddubny/1.ogg"
    ip "A GLORIOUS DAY TO MAKE YOUR ACQUAINTANCE."
    show kaori cur
    show yuuna cur
    show valerie cur
    show shou cur
    show mayu cur
    "...What?"
    
    if MCStory == 1:
        "His jacket has somehow unzipped itself and reveals a perfectly sculpted 8-pack. It puts my meager 6-pack to shame."
    else:
        "His jacket has somehow unzipped itself and reveals washboard abs I can only achieve in my dreams."
        
    show ivan ann
    voice "audio/voice/E4/Ivan Poddubny/2.ogg"
    ip "UNDER THE WINGS OF EXPERIENCE, I SHALL TEACH YOU TO SOAR THE SKIES."
    show shou hap
    "Kaori's face falls. She looks like her nightmare has come to life. The rest of the girls are mirrors of confusion. Shou, on the other hand, looks as if his dreams have come true."
    voice "audio/voice/E4/Shou/d3/7 Copy.ogg"
    ss "Uh, do you know someone named Tatsuo by any chance?"
    "Ivan looks at Shou. Even with his smile, his piercing gaze is unsettling and Shou scoots back."
    show ivan sur
    voice "audio/voice/E4/Ivan Poddubny/3.ogg"
    ip "YOU SPEAK OF MY NEPHEW?"
    show drop:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    show kaori thi
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_07.ogg"
    ki "That explains a lot..."
    "Yuuna stands up."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D3/3.ogg"
    ym "Hi Mr. Poddubny, thank you for agreeing to coach our team this afternoon."
    show ivan ann
    voice "audio/voice/E4/Ivan Poddubny/4.ogg"
    ip "UTTER NOT MY FAMILY NAME, FOR FORMALITIES BETWEEN FRIENDS MUST NOT EXIST."
    show yuuna hap
    show mayu neu
    show kaori neu
    show shou smi
    voice "audio/voice/E4/Yuuna/E4/D3/4.ogg"
    ym "Oh, um, okay…Ivan... Thank you!"
    show ivan neu
    "He nods."
    voice "audio/voice/E4/Ivan Poddubny/5.ogg"
    ip "OF COURSE. WE WILL BEGIN WITH LESSON ONE."
    voice "audio/voice/E4/Ivan Poddubny/6.ogg"
    ip "TO SPROUT INTO A MAGNIFICENT TREE, WE MUST FIRST WATER THE ROOTS."
    voice "audio/voice/E4/Kaori/D3/Kaori_D3_08.ogg"
    ki "The foundations?"
    show ivan smi
    voice "audio/voice/E4/Ivan Poddubny/7.ogg"
    ip "YES, FIERY FLOWER. THE ROOTS."
    "Ivan motions us to the holograph. We cautiously approach and Ivan projects an image of a seed."
    show ivan ann
    voice "audio/voice/E4/Ivan Poddubny/8.ogg"
    ip "FIRST, THE SEED REQUIRES SUNLIGHT, WATER, CARBON DIOXIDE, AND RICH SOIL."
    voice "audio/voice/E4/Ivan Poddubny/9.ogg"
    ip "THE KEY TO REMEMBER IS THE SYMBIOTIC RELATIONSHIP BETWEEN PLANT AND ENVIRONMENT."
    voice "audio/voice/E4/Ivan Poddubny/10.ogg"
    ip "THROUGH LIGHT ENERGY ABSORBED BY CHLOROPHYLL, CONVERSION OCCURS OF CARBON DIOXIDE AND WATER TO CREATE GLUCOSE AND OXYGEN."
    show ivan neu
    "...Have I fallen asleep and started dreaming I'm in class again?"
    
    show shou thi
    voice "audio/voice/E4/Shou/d3/8 Copy.ogg"
    ss "Geez, this is like listening to Valerie explain--"
   
    
    if E4D2S3_Innocent == 0:
        show valerie ann
        "{i}Wham!{/i}"
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L6.ogg"
        vb "Did you say something?"
        "Shou rubs his fresh bruise."
        show shou wor
        voice "audio/voice/E4/Shou/d3/9 Copy.ogg"
        ss "Of course not! Nothing at all."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4D3/ValE4D3L7.ogg"
        vb "Good."
        "Valerie turns back to the holograph. Shou looks at me."
        show shou thi
        voice "audio/voice/E4/Shou/d3/10 Copy.ogg"
        ss "I think she's been hanging around Kaori for too long--"
        # sfx ?
        "{i}Wham!{/i}"
        show kaori ann
        voice "audio/voice/E4/Kaori/D3/Kaori_D3_09.ogg"
        ki "Did you say something?"
        show shou win
        voice "audio/voice/E4/Shou/d3/11 Copy.ogg"
        ss "NO!"
        show ivan ang
        show kaori cur
        show valerie cur
        voice "audio/voice/E4/Ivan Poddubny/11.ogg"
        ip "NO? YOU DARE QUESTION THE WONDROUS FEAT OF PHOTOSYNTHESIS?"
        show shou wor
        show ivan neu
        "Ivan stalks up to Shou and stares him down. His mustache droops in disappointment."
        show shou win

        voice "audio/voice/MISSING/BATCH2/17.ogg"
        ss "No! I mean, yes! Yes, that it's wondrous… Please don't hurt me!"
        show shou thi
        show dots:
            xoffset 1575
            yoffset 5
            xzoom .5
            yzoom .5
        "Ivan stares suspiciously at Shou before resuming his lecture."
        "We try to follow the best we can as he continues to talk."
        "After finishing his lecture on planet science, he looks at all of us."
        
    else:
        pf "Shhh! Do you want to get caught or what?"
        "Shou freezes mid-sentence then closes his mouth. Valerie eyes us suspiciously, then shrugs and resumes listening to Ivan ramble about some plant mumbo jumbo."
    
    show ivan neu
    voice "audio/voice/E4/Ivan Poddubny/12.ogg"
    ip "UNDERSTOOD?"
    "He is met with silence."
    show ivan thi
    "Ivan uses his fingers to elongate his moustache in great thought."
    voice "audio/voice/E4/Ivan Poddubny/13.ogg"
    ip "DEMONSTRATION WILL TRIUMPH EXPLANATION?"
    voice "audio/voice/E4/Mayu/D3/Mayu D3-07.ogg"
    ma "Yes, please."
    "Ivan nods solemnly."
    show note:
        xoffset 1575
        yoffset 5
        xzoom .5
        yzoom .5
    show ivan ann
    voice "audio/voice/E4/Ivan Poddubny/14.ogg"
    ip "MAKE HASTE TO THE SIMULATIONS!"
    
    #fade black
    scene black with fade
    
    jump E4D3S3
