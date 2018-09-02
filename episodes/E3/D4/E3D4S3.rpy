
label E3D4S3:
    
    scene bg campus battleroom day with dissolve
    "When we enter the pre-combat room, Kaori is nowhere to be found. {w}She must already be changing."
    "Shou and I go to change, but Mayu stays back. She must be really upset if she's actively avoiding Kaori."

    #Fade to black, change room
    scene black with fade
    scene bg campus battleroom day with dissolve:
        xalign 0.99
        yalign 0.5
    
    show shou thi at r3 with dissolve:
        xzoom -1
    $renpy.pause(.75)
    voice "audio/voice/E3/D4/S3/shou/34.ogg"
    ss "Man, I'm not liking the vibe right now."
    
    if E3D4S2_Duelist == 1:
        if E3D4S2_Waited == 1: # get depowered by Mei (nothing first, then defend) OR Beat Mei (nothing first, then defend)
            show shou ner
            voice "audio/voice/E3/D4/S3/shou/35.ogg"
            ss "Not that I'm blaming you or anything. I mean you did hang back, but Mei charged at you..."
            pf "Yeah."
            show shou neu
            "I exhale."
    
        elif E3D4S2_Interfered == 1: # get depowered by Mei (Engaged) or Beat Mei (Engaged)
            pf "Were you expecting me to hang back?"
            show shou ner
            voice "audio/voice/E3/D4/S3/shou/36.ogg"
            ss "I didn't say that."
            show shou neu
            voice "audio/voice/E3/D4/S3/shou/37.ogg"
            ss "I probably would have done the same if I were in your position."
    
        else: # get depowered by Mei (Did not fight back)
            pf "I didn't engage Mei, so I don't see why Kaori would be upset."
            show shou neu
            voice "audio/voice/E3/D4/S3/shou/38.ogg"
            ss "It's because she didn't get her clean win."
            pf "What else could I have done?"
            show shou ner
            "Shou scratches the back of his head and sighs."
            show drop:
                xoffset 1175
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D4/S3/shou/39.ogg"
            ss "That was a lose-lose situation any way you look at it."
            "I shrug."
    
    
    else:
        show shou ner
        voice "audio/voice/E3/D4/S3/shou/40.ogg"
        ss "Do you think helping her was a mistake?"
        menu:
            "No, it was the best decision for the team.":
                $ E3D4S3_Thoughts = "Best"
                pf "You made the right call, Shou."
                show shou neu
                "He nods."
                voice "audio/voice/E3/D4/S3/shou/41.ogg"
                ss "It's annoying that Kaori is acting this way when no one did anything wrong."
    
            "No, she was being stupid.":
                $ E3D4S3_Thoughts = "Stupid"
                pf "I don't know what her personal vendetta is against Mei, but on the field in a team match is not the place for her to hash out her issues. We aren't going to sit back and just let ourselves get depowered."
                show drop:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou thi
                voice "audio/voice/E3/D4/S3/shou/42.ogg"
                ss "Yeah, no kidding."
                pf "Especially when she deviated from a plan {i}she{/i} made."
                show shou neu
                "Shou nods."
    
            "Yes, you should have trusted her.":
                $ E3D4S3_Thoughts = "Trusted"
                pf "She was having a duel. You can't just go in like that."
                show shou sad
                "Shou frowns."
                voice "audio/voice/E3/D4/S3/shou/43.ogg"
                ss "Yeah, but she wasn't dueling in a no-stakes match of bragging rights. The outcome affects all of us on the team."
                pf "But when you interfere, it feels like you don't trust Kaori to win."
                show shou neu
                "Shou blinks, then shakes his head."
                show storm:
                    xoffset 1175
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou thi
                voice "audio/voice/E3/D4/S3/shou/44.ogg"
                ss "That's a bit of a stretch..."
                "I shrug."
    
    pf "It's in the past now."
    show shou neu
    voice "audio/voice/E3/D4/S3/shou/45.ogg"
    ss "Yeah."
    hide shou with dissolve
    "Shou and I finish changing and head back to the pre-combat room."
    
    $ shoOut = "sUniform"
    $ mayOut = "sUniform"
    $ kaoOut = "sUniform"
    
    scene black with fade
    scene bg campus battleroom day with dissolve
    $renpy.pause(.5)
    show shou neu at l2 with dissolve
    $renpy.pause(.75)
    
    if E3D4S2_Duelist == 1:
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
        "As soon as we enter, Kaori stomps up to me. Mayu is nowhere to be found."
        show kaori ann at r2 with dissolve:
            xzoom -1
        voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_32.ogg"
        ki "Why did you do that?!"
    
        if E3D4S2_Waited == 1: # get depowered by Mei (nothing first, then retaliated) OR Beat Mei (nothing first, then retaliated)
            pf "Do what?"
            show kaori dis
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_33.ogg"
            ki "You engaged Mei."
            pf "No, Mei engaged {i}me{/i}."
            show kaori ann
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_34.ogg"
            ki "Yes, and you fought back."
            pf "...You expected me to just sit there and give her a free kill?"
            show dots:
                xoffset 1040
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ske
            "She opens her mouth to retort, but pauses."
    
        elif  E3D4S2_Interfered == 1: #ELIF E3D4S2_Interfered == 1 get depowered by Mei (Engaged) OR Beat Mei (Engaged)
            pf "Do what?"
            show kaori dis
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_35.ogg"
            ki "I told you I had it but you engaged her anyway."
            pf "How is that a bad thing? Isn't the goal to win the match?"
            show kaori ann
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_36.ogg"
            ki "Yes, but that's not what I mean."
            pf "Then what {i}do{/i} you mean?"
            show dots:
                xoffset 1040
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori dis
            "She frowns."
    
        else: #ELIF get depowered by Mei (Did not fight back)
            "I blink at her in confusion."
            pf "Do what exactly?"
            show kaori dis
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_37.ogg"
            ki "I told you to stay out of it."
            pf "Which is precisely what I did."
            show dots:
                xoffset 1040
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ann
            "She bites back another retort."
    
    
    else:
        show kaori neu at r2 with dissolve:
            xzoom -1
        "We arrive at the same time as Kaori. I watch Mayu walk into the change room. Kaori doesn't look at us but grabs her bag and starts to leave."
        show shou dis
        "Shou frowns."
        play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E3/D4/S3/shou/46.ogg"
        ss "Of course, make me look like the bad guy."
        show dots:
            xoffset 1040
            yoffset 110
            xzoom .75
            yzoom .75
        "Kaori stops in her tracks."
        show kaori dis
        voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_38.ogg"
        ki "What did you say?"
        show shou ske
        voice "audio/voice/E3/D4/S3/shou/47.ogg"
        ss "I said \"Of course, make me look like the bad\"--"
        show kaori ang
        voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_39.ogg"
        ki "I was about to take out Mei!"
        show kaori ann
        show shou thi
        voice "audio/voice/E3/D4/S3/shou/48.ogg"
        ss "It definitely didn't look like that."
        show vein:
            xoffset 1040
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_40.ogg"
        ki "Of course it didn't after {i}you{/i} came and distracted {i}me{/i}."
        show shou ann
        voice "audio/voice/E3/D4/S3/shou/49.ogg"
        ss "There we go. My fault, AGAIN."
        show kaori dis
        "Kaori tightens the grip on her bag."
        voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_41.ogg"
        ki "What do you want from me?"
    
        if E3D4S3_Thoughts == "Best":
            pf "Come on, guys..."
            "I look at Kaori."
            pf "I get you wanted a clean fight against Mei, but Shou did what was best for the team."
            show kaori ang
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_42.ogg"
            ki "You're on his side too?"
            show kaori ann
            pf "I'm not on anyone's side, but throwing the blame won't help."
            show shou dis
            voice "audio/voice/E3/D4/S3/shou/50.ogg"
            ss "Yeah, not when it's directed at the {i}wrong{/i} person."
            show kaori ske
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_43.ogg"
            ki "What's that suppose to mean?"
            show storm:
                xoffset 365
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D4/S3/shou/51.ogg"
            ss "You know exactly what that means."
            show kaori ann
            pf "Guys--"
    
        elif E3D4S3_Thoughts == "Stupid":
            pf "Kaori, you can't put Shou in an unfair position like that, then {i}blame{/i} him for making the right call."
            show kaori ann
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_44.ogg"
            ki "He didn't make the right call. He should have listened to me and stayed out of it."
            pf "Are you serious right now? Why would he not come to help his {i}teammate{/i}."
            show kaori dis
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_45.ogg"
            ki "Because I already had it."
            show shou dis
            voice "audio/voice/E3/D4/S3/shou/52.ogg"
            ss "Okay, great, you had it. So what difference does it make if I came in? All I did was speed up the process."
    
        elif E3D4S3_Thoughts == "Trusted":
            pf "Shou, we already talked about this."
            show shou dis
            "Shou frowns."
            voice "audio/voice/E3/D4/S3/shou/54.ogg"
            ss "You can't expect me to blindly trust someone when that same {i}someone{/i} stopped following the plan 10 seconds into the fight. We already had the lead and positional advantage, why throw that away?"
            show kaori ann
            voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_46.ogg"
            ki "Because."
            show question:
                xoffset 365
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske
            voice "audio/voice/E3/D4/S3/shou/55.ogg"
            ss "Because why?"
            
    show kaori dis
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_47.ogg"
    ki "You don't understand."
    
    
    if E3D4S2_Duelist == 1:
        show question:
            xoffset 365
            yoffset 20
            xzoom .75
            yzoom .75
        show shou ske
        voice "audio/voice/E3/D4/S3/shou/56.ogg"
        ss "How could he? You aren't making any sense at all."
    
    else:
        show vein:
            xoffset 365
            yoffset 20
            xzoom .75
            yzoom .75
        show shou ann
        voice "audio/voice/E3/D4/S3/shou/57.ogg"
        ss "Obviously not, because you are making zero sense right now."
        
    show kaori ann
    "Kaori tenses and glares at Shou."
    show kaori ang
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_48.ogg"
    ki "I don't have to explain myself to you."
    show kaori ann
    
    stop music fadeout 10
    voice "audio/voice/E3/D4/S3/mayu/Mayu-20.ogg"
    ma "No, Kaori."
    
    
    hide shou
    hide kaori
    with dissolve
    
    show shou ner at l3
    show kaori cur at cc:
        xzoom 1
    with dissolve
    show mayu dis at r3:
        xzoom -1
    with dissolve
    $renpy.pause(.75)
    "We turn around to see Mayu. Her jaw is set and her eyes are hard. I've never seen her this upset before. It's chilling. {w}Kaori's eyes widen."
    show kaori cur
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_49.ogg"
    ki "Mayu?"
    voice "audio/voice/E3/D4/S3/mayu/Mayu-21.ogg"
    ma "You put your personal agenda above the team and risked the match."
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori neu
    ki "..."
    show shou neu
    show mayu ann
    voice "audio/voice/E3/D4/S3/mayu/Mayu-22.ogg"
    ma "Our positioning was compromised and I had no support. Those two were out of position because of an aggressive call that {i}you{/i} made."
    
    if E3D4S2_Duelist == 1 and E3D4S2_Takedown == 0:
        voice "audio/voice/E3/D4/S3/mayu/Mayu-23.ogg"
        ma "That ended up costing us three depowered GEARs." # of which at least two were avoidable."
    
    else:
        voice "audio/voice/E3/D4/S3/mayu/Mayu-24.ogg"
        ma "That ended up costing us two depowered GEARs. One of which was avoidable."
        
    show kaori cur
    show mayu ang
    voice "audio/voice/E3/D4/S3/mayu/Mayu-25.ogg"
    ma "So no, you {i}do{/i} owe us an explanation."
    show mayu ann
    
    "Her voice is calm but severe. Mayu's ice is a lot more unnerving than any of Kaori's fiery outbursts."
    show kaori cur
    
    menu:
        "This is getting out of control.":
            pf "Let's all take a deep breath and calm down."
            show kaori ann
            show mayu dis
            show shou dis
            "They ignore me and continue to glare at each other."
    
        "Back off, Mayu.":
            "I stare down Mayu."
            pf "What's gotten into you, Mayu?"
            show shou dis
            "Shou chimes in."
            show kaori ann
            voice "audio/voice/E3/D4/S3/shou/58.ogg"
            ss "She's speaking the truth."
            pf "Maybe so, but having an attitude won't help."
            show dots:
                xoffset 230
                yoffset 20
                xzoom .75
                yzoom .75
            show shou ske
            show mayu dis
            "Shou looks like he's about to say something, but stops. Mayu looks a little calmer but still upset."
    
        "We're waiting for an answer, Kaori.":
            pf "Mayu has a point."
            "Shou nods and we all look at Kaori."
    
        "...":
            "I stay silent."
    
    "Kaori looks between the three of us, then sighs."
    show storm:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_50.ogg"
    ki "I get it, I made a mistake. But I can't be expected to always make the perfect calls."
    show mayu dis
    show shou ske
    voice "audio/voice/E3/D4/S3/shou/59.ogg"
    ss "We don't expect that from you either, but when you start throwing the blame around--"
    show kaori thi
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_51.ogg"
    ki "I'm sorry, okay?"
    
    if MCStory == 3:
        "Although she snapped her apology, I can tell it's not because of a lack of sincerity. It's because she's not used to apologizing."
    else:
        "That didn't sound very sincere."
        
    show shou thi
    voice "audio/voice/E3/D4/S3/shou/60.ogg"
    ss "It would help if you meant it."
    show kaori ann
    "Kaori clenches her hands into fists."
    voice "audio/voice/E3/D4/S3/kaori/e3d4_Kao_52.ogg"
    ki "I said I'm sorry! I messed up. It was my fault. Blame me. What else do you want?!"
    show mayu neu
    show shou dis
    pf "Let's drop it. She already said sorry."
    "Shou crosses his arms, but nods. At least Mayu seems to have returned to her normal demeanor."
    voice "audio/voice/E3/D4/S3/mayu/Mayu-26.ogg"
    ma "Okay."
    hide kaori
    hide mayu
    hide shou
    with dissolve
    "We usually celebrate as a team after a win, but I get the feeling that won't happen this time. {w}After picking up our stuff, we exit the pre-combat room."
    
    #Black screen, then outside building in Campus
    scene black with fade
    
    jump E3D4S4

