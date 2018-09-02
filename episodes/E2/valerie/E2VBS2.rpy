#
label E2VBS2:
    
    #Event 2 - Evening Choice (>50 Points AND NOT DAY4)
    
    scene black with fade
    stop ambient fadeout 2
    stop music fadeout 2    
    scene bg campus main dusk with fade
    
    "As I'm passing by the quad, I spot a familiar blonde head waving me over.{w} Valerie sits cross-legged on the grass with a sketchpad in her lap. Across from her is a male student holding a basic pose with his hands on his waist. {w}As I approach, he eyes me suspiciously, but is careful not to move."
    show valerie smi at cc with dissolve
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5.0
    "Valerie pats the space next to her, so I sit down."
    pf "What are you doing?"
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO27.ogg"
    vb "Practicing my nudes."
    voice "audio/voice/E2/Free/VB/stu2m/1.ogg"
    stu2m "N-Nude?"
    show valerie ann at cc
    "The model shifts out of place, but Valerie stops him."
    show exclamation:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie ang at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO28.ogg"
    vb "Hey! Don't move."
    show valerie ann at cc
    "He seems uncertain but resumes his position. {w}Valerie returns her attention to me."
    show valerie hap at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO29.ogg"
    vb "Want to see?"
    "I can clearly see it's not a nude, so I'm not sure where she's going with this."
    show valerie smi at cc
    pf "Uh, sure..."
    voice "audio/voice/E2/Free/VB/stu2m/2.ogg"
    stu2m "Whoa! Wait!"
    show studentM extra at r3 with dissolve:
        xzoom -1
    "The student breaks from his pose and practically leaps towards Valerie's sketchbook. As he looks at the drawing, he sighs in relief."
    voice "audio/voice/E2/Free/VB/stu2m/3.ogg"
    stu2m "It's not a nude."
    show valerie ske at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO30.ogg"
    vb "Of course not. You're clothed."
    voice "audio/voice/E2/Free/VB/stu2m/4.ogg"
    stu2m "Yeah…?"
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO31.ogg"
    vb "I asked you to model because I wanted to draw you exactly as I saw you. If I wanted you nude, we'd most likely be in my bedroom."
    "The model turns bright red as she speaks."
    voice "audio/voice/E2/Free/VB/stu2m/5.ogg"
    stu2m "I-Is that what you want? Because we could do that..."
    show valerie neu at cc
    "She shakes her head."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO32.ogg"
    vb "No, I wanted a live model in the quad to capture the sunset."
    voice "audio/voice/E2/Free/VB/stu2m/6.ogg"
    stu2m "Then let me get back to my pose."
    show storm:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie dis at cc
    stop music fadeout 5
    "Valerie sighs, then pouts."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO33.ogg"
    vb "No, it's too late. We've missed the light. This is ruined."
    voice "audio/voice/E2/Free/VB/stu2m/7.ogg"
    stu2m "Sorry… Maybe we can do this another time? I can give you a call."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
    show valerie thi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO34.ogg"
    vb "Ohhh… um, unfortunately, I don't have a phone."
    voice "audio/voice/E2/Free/VB/stu2m/8.ogg"
    stu2m "Oh."
    show drop:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie hap at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO35.ogg"
    vb "Yeah, I just moved here and I haven't gotten all of that set up yet."
    voice "audio/voice/E2/Free/VB/stu2m/9.ogg"
    stu2m "I can help you with that if you want."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO36.ogg"
    vb "That's so sweet! But I already have someone who's helping me out."
    show valerie mis at cc
    "She smiles at me and puts a hand on my arm."
    
    menu:
        "What is happening?":
            pf "Uhhh… What?"
            show valerie smi at cc
            "The student eyes me again while Valerie laughs."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO37.ogg"
            vb "You offered to take me to get my new SIM card, remember?"
            pf "I did? When?"
            show valerie hap at cc
            # sfx?
            "She playfully hits my arm."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO38.ogg"
            vb "You are so silly!"
            "She is way too happy about this. Is she drunk right now? Why is this guy glaring at me?"
    
        "Play along.":
            "I grin at her."
            pf "That's right. In fact, that's what we were planning on doing this evening."
            show valerie smi at cc
            "She doesn't miss a beat."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO39.ogg"
            vb "Yeah, I was supposed to find him after we were done here, but someone's a little early."
            pf "I just couldn't stay away."
            "I place a hand over hers romantically."
            show heart:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO40.ogg"
            vb "Aww!"
    
        "I'm not going to be a part of this.":
            pf "Don't get me involved."
            show valerie cur at cc
            "She furrows her brow."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO41.ogg"
            vb "Are you taking back your offer?"
            show valerie ner at cc
            pf "I never made an offer."
            "The student frowns."
            
    voice "audio/voice/E2/Free/VB/stu2m/10.ogg"
    stu2m "Nevermind. I'd better get going."
    hide studentM with dissolve
    stop music fadeout 5
    "He turns away before we can say anything."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO42.ogg"
    vb "Bye!"
    "Valerie waves at his retreating form."
    show valerie neu at cc
    "Once he's out of view, she sits back down and discards the half-finished drawing. Then flips to a fresh page."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5.0
    pf "You gave me your number. I know you have a phone."
    show valerie thi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO43.ogg"
    vb "Obviously. Who doesn't have a phone?"
    pf "Why'd you tell that guy you didn't?"
    show valerie hap at cc
    "She ignores me."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO44.ogg"
    vb "Go stand over there and strike a pose."
    pf "What?"
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO45.ogg"
    vb "I need you to model for me."
    
    menu:
        "Strike a heroic pose.":
            "I shrug."
            pf "Okay."
            "I push myself back onto my feet and hold an imaginary sword in the air for my \"victory\" pose."
            show heart:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO46.ogg"
            vb "Ooh, I'd definitely count on you to save the day."
    
        "Unleash my inner sexy beast.":
            "Once she sees what I've got in store for her, she'll forget all about sketching and will want to do other things."
            "I get on my feet and flash her an intimate, yet smouldering gaze."
            show valerie ner b1 at cc with dissolve
            "She's taken aback, and quickly averts her eyes."
            "Can't say I'm surprised!"
    
        "Posing is lame.":
            pf "No."
            show valerie ann at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO47.ogg"
            vb "You scared off my last model! You owe me."
            pf "I'm sure you did that all on your own."
            show valerie dis at cc with dissolve
            $renpy.pause(.5)
            show valerie sad at cc with dissolve
            "She pouts, and gives me sad eyes."
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO48.ogg"
            vb "Pleeeease?"
    
            menu:
                "Okay.":
                    pf "Fine, but only if you'll stop looking at me like that."
                    show valerie hap at cc
                    "She instantly perks up."
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO49.ogg"
                    vb "Yay!"
    
                "Still no.":
                    $ E2VBS2_Refuse = 1
                    pf "Sorry, the answer is still no."
                    show question:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO50.ogg"
                    vb "Really? Are you looking at these eyes?"
                    pf "Nobody makes better \"puppy dog\" eyes than my sister. You've got a long way to go."
                    show valerie neu at cc
                    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO51.ogg"
                    vb "Hmm, Interesting…"
    
        "I call this \"Bloo Steal\".":
            "I look to the right, spike up my hair, and pop my collar. Then I pout my lips as if I'd just eaten a lemon and suck in my cheeks. Finally, I keep my eyes big and wide while simultaneously furrowing my brow."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie ske at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO52.ogg"
            vb "Uh, what is that?"
            pf "Bloo Steal. You like it?"
            show valerie wor at cc
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO53.ogg"
            vb "I'm not sure what I'm looking at."
            pf "Okay, how about this?"
            "I keep the same face but suck slightly less on my cheeks."
            pf "I call this \"Flash Feel\"."
            show drop:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO54.ogg"
            vb "Riiight…" 
    
    if E2VBS2_Refuse == 1:
        show valerie neu at cc with dissolve
        "We fall into silence. {w}Valerie fidgets with her pencil, then begins to sketch again."
    
    else:
        show valerie neu at cc with dissolve
        "She falls silent as she begins to sketch me. {w}The quiet adds weight to her gaze and I begin to feel self-conscious every time she looks at me."
    
    "I decide to break the silence with the first thing I think of."
    pf "So, have you given any more thought to our class assignment?"
    show valerie cur at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO55.ogg"
    vb "What about it?"
    pf "I think going out and exploring the city will be fun."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO56.ogg"
    vb "Me too. I've never been to Japan before."
    "For some reason, that surprises me."
    pf "What made you decide to come to ACE?"
    show valerie neu at cc
    "She hesitates, which also surprises me. She's usually lightning fast with her retorts."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO57.ogg"
    vb "I've always wanted to come to Asia and ACE has a great engineering program. It was the perfect opportunity for me to leave France."
    pf "Aren't there other comparable schools in Europe? I know Germany has a strong program too."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO58.ogg"
    vb "Yes, but what is the point of staying so close to home? Everything back there is the same. I want to study engineering, of course, but I also want to experience life."
    show valerie hap at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO59.ogg"
    vb "That's why I'm excited for this Foreign Exchange class."
    pf "I see…"
    
    if MCStory == 3:
        "She really doesn't seem to like talking about her home in France. I wonder why."
        
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO60.ogg"
    vb "What about you? Have you been to Japan before?"
    pf "Yeah, I'm half Japanese."
    show valerie cur at cc
    "She looks back up at me and stares for a long moment, then grins."
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO61.ogg"
    vb "Yes, I can tell."
    pf "But I've never really seen Isokaze before."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO62.ogg"
    vb "So that means we'll be sharing new experiences together."
    pf "Yeah, I guess so."
    "A soft smile plays at her lips, but she's quiet again."
    show valerie neu at cc
    "After a few more minutes, she drops her pencil and offers me her sketchpad."
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO63.ogg"
    vb "Okay! What do you think?"
    
    if E2VBS2_Refuse == 1:
        pf "You drew me anyway?"
        "She captured me mid-sentence, but my body is relaxed and comfortable."
        pf "This is really well-done."
        show valerie hap at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO64.ogg"
        vb "Thanks."
    
    else:
        pf "Hey, this looks just like me!"
        show valerie hap at cc
        "She laughs."
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO65.ogg"
        vb "You don't have to sound so surprised."
    
    pf "How did you finish so quickly?"
    show valerie smi at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO66.ogg"
    vb "It's just a rough sketch. Nowhere near done."
    
    if MCStory == 2:
        pf "Even so, it's pretty detailed. Your shading brings the sketch to life. You've even used the softened negative space to draw the viewer's eyes to the portrait."
        show valerie cur at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO67.ogg"
        vb "What?"
        "I point to what I'm talking about."
        pf "See here? And here."
        show valerie smi at cc
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO68.ogg"
        vb "Oh, I see what you mean. I don't think about this stuff when I draw. I just draw what I see."
    
    pf "Have you been drawing for a long time?"
    show valerie hap at cc
    "She nods."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO69.ogg"
    vb "I doodled all the time as a kid. I used to draw on the walls at home."
    pf "I bet your mom loved that."
    show valerie thi at cc
    "She looks away, then shrugs."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO70.ogg"
    vb "I've never had lessons or anything, if that's what you mean. I just like to draw."
    pf "Well, you've got a lot of talent."
    show valerie mis at cc
    "She smirks."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO71.ogg"
    vb "Maybe one day, I'll show you some of my other talents."
    pf "What other talents?"
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO72.ogg"
    vb "You'll see… if you play your cards right."
    show valerie neu at cc
    "She stretches, then pushes herself to her feet."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO73.ogg"
    vb "I'd better be off. It's getting late."
    pf "What? You're leaving?"
    show valerie hap at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO74.ogg"
    vb "Don't sound so sad. You'll see me again."
    pf "I didn't mean it like that."
    show valerie smi at cc
    "She rips the drawing out of her book and hands it to me."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO75.ogg"
    vb "Here, you can keep it."
    pf "Thanks."
    show valerie mis at cc
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO76.ogg"
    vb "Don't miss me too much, okay? I'll see you later."
    hide valerie with dissolve
    "She waves and winks at me."
    pf "Bye."
    scene black with fade
    stop music fadeout 3
    "I watch her go, holding the signed drawing in my hand."
    stop ambient fadeout 3
    $renpy.pause(1)
    $ E2VBS2_Completed = 1
    
