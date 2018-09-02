#
label E3D5S2:
    
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3

    scene bg campus lounge day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    "I check out the menu on display in the Lounge. There's the usual Japanese fare that I can find in the dining hall too. Today's special is Naporitan Spaghetti, popularly known as \"ketchup spaghetti\". {w}The bartender approaches me and waits expectantly. Hm…"
    
    menu:
        "Order Naporitan Spaghetti.":
            "When in Rome… {w}Or I guess in this case, when in Japan…"
            pf "One Naporitan Spaghetti please."
            "The bartender nods."
    
        "Choose something safe.":
            "I take another look at their regular menu. I'll just order a bento."
            pf "I'll have the bento."
            "The bartender nods."
    
        "I think I lost my appetite.":
            "On second thought, I'm not really hungry."
            "The bartender has waited for a few minutes for me to decide. I feel a little obligated to order something."
            pf "Uh, I'll get a water."
            "The bartender nods."
    
            
    "He brings me my order and I take it to an empty table. As soon as I sit down, someone slides into the seat across from me. I'm ready to apologise and ask if this table was taken, when I take a good look at the girl smiling at me."
    show mei smi at cc with dissolve
    pf "Mei?"
    show mei hap
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_29.ogg"
    ms "Is this seat taken?"
    pf "Uh, no. You can sit here."
    show mei smi
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_30.ogg"
    ms "Thanks."
    "This is a little uncomfortable after what happened yesterday. I think she feels it too."
    
    if E3D4S4_ChaseKaori == 1:
        show mei thi
        voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_31.ogg"
        ms "So, um, how's Kaori?"
        pf "She'll be okay."
        show mei neu
        "Mei nods."
        voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_32.ogg"
        ms "I thought so."
    
    else:
        pf "Um, have you talked to Kaori yet?"
        show mei ner
        voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_33.ogg"
        ms "No. I figured it would be best to give her some space."
        
    show mei wor
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_34.ogg"
    ms "I haven't seen her that upset since--"
    show dots:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show mei dis
    "She hesitates."
    pf "Since Ryouta?"
    show mei cur
    "Mei blinks, but seems relieved."
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_35.ogg"
    ms "Oh, Kaori told you about Ryouta?"
    
    if E3D4S4_ChaseKaori == 0 or (E3D4S4_ChaseKaori == 1 and E3D4S4_Consoled == 1):
        pf "Sort of…"
        "I'm not about to tell her I was listening in on their conversation a few days ago."
    
    else:
        pf "Something like that."
        
    show mei ner
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_36.ogg"
    ms "Did she say it was all my fault?"
    pf "It was certainly implied."
    show mei neu
    "Mei sighs."
    show storm:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_37.ogg"
    ms "I wish I'd never said anything."
    "I blink. Mei doesn't strike me as someone who has many regrets. She's always cheerful and seems to take whatever life throws at her in stride."
    pf "I believe that you meant well."
    show mei smi
    ### VOICE - line said "Thank you!" but voice gave "Thanks"
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_38.ogg"
    ms "Thanks."
    show mei ske
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_39.ogg"
    ms "If only Kaori can see that. I wasn't trying to ruin her friendship with Ryouta or my friendship with her."
    show mei smi
    ### VOICE - line said "best friends" but voice just gave "friends"
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_40.ogg"
    ms "They would have been so cute together! You know, if Ryouta hadn't been such a jerk. And how awesome would it have been if my two friends ended up together?"
    pf "Sounds like you were excited for her."
    show mei hap
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_41.ogg"
    ms "I was! Even back then Kaori was more reserved around people. She didn't like to show her feelings, so I was so excited when she told me she liked Ryouta."
    pf "If he was such a jerk, why were you friends with him?"
    show mei ske
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_42.ogg"
    ms "He wasn't always like that. Honestly, I don't know why he exploded the way he did. We used to do everything together. His family even took us on their vacations!"
    show mei smi
    ### VOICE - read as "so when we entered middle school he worked hard to change his image." but voice changed some words slightly
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_43.ogg"
    ms "I knew him back in elementary school when he still had huge glasses and would tell goofy jokes that were too smart to be funny. Kids used to pick on him a lot, so we entered middle school and he worked hard to change his image."
    show mei neu
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_44.ogg"
    ms "He lost the glasses and became more serious. The more I think about it, the more I think he stuck with us out of obligation rather than true feeling. We were his only friends for a long time until he hit his growth spurt. Then all the girls were suddenly interested."
    show mei thi
    "Mei looks thoughtful."
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_45.ogg"
    ms "Actually, I think it was when other girls started to notice him that Kaori liked him too."
    pf "Do you still keep in touch with him?"
    # sfx ?
    show mei dis
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_46.ogg"
    ms "Of course not!"
    "She hits the table for emphasis."
    show vein:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show mei ann
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_47.ogg"
    ms "I told him all that stuff in confidence thinking maybe it would give him a push to make a move."
    show mei ang
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_48.ogg"
    ms "Well, he made a move alright! He went out of his way to hurt Kaori. What kind of friend is that? That's not a person I want to associate with."
    show mei ann
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_49.ogg"
    ms "It's just frustrating that Kaori would lump me into the same category as {i}him{/i}."
    
    menu:
        "That sounds like her.":
            pf "I can see that."
            show mei ske
            "Mei raises an eyebrow."
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_50.ogg"
            ms "Don't tell me you agree with her…"
            pf "No, no! You don't sound anything like Ryouta. I meant I can definitely see Kaori jumping to conclusions."
            show mei dis
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_51.ogg"
            ms "She's just so stubborn too! She wouldn't even listen to me when I tried to explain."
            pf "Then why do you keep trying?"
    
        "This explains so much.":
            pf "Thank you, Mei."
            show mei ske
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_52.ogg"
            ms "Huh? For what?"
            pf "I finally understand why Kaori acts so… Kaori-like."
            show exclamation:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show mei sur
            "Mei's eyes widen."
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_53.ogg"
            ms "You think {i}I{/i} turned her into that?"
            pf "It makes sense. She's withdrawn, quick to make judgements, stubborn…"
            show mei hap
            "Mei laughs."
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_54.ogg"
            ms "She's always sort of been like that."
            show mei cur
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_55.ogg"
            ms "...I think."
            show mei mis
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_56.ogg"
            ms "She's always been stubborn at least."
            pf "If it's been so long, why do you still try so hard with her?"
    
        "Why even bother?":
            pf "Why do you keep trying with Kaori then?"
            
    show mei ske
    "Mei looks at me as if I've sprouted a third arm."
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_57.ogg"
    ms "She's my friend."
    show mei neu
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_58.ogg"
    ms "I left her alone for a while so she could cool off, and I admit I was angry at her for a long time too. But then I saw her withdraw completely…"
    show mei ner
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_59.ogg"
    ms "No one should be alone."
    show mei neu
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_60.ogg"
    ms "I know she hasn't forgiven me yet, but she will."
    pf "How can you be so sure?"
    show mei smi
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_61.ogg"
    ms "It might take her a little longer, but in the end, Kaori always sees reason."
    "Mei is completely confident that Kaori will forgive her. That must be how she can still act so familiarly with her, even though Kaori doesn't reciprocate those feelings."
    "I have to admit, I kind of admire Mei for that."
    show mei hap
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_62.ogg"
    ms "Anyway, since I really didn't get the chance to say it yesterday, congrats on your win!"
    "I blink."
    pf "Oh, thanks."
    show mei mis
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_64.ogg"
    ms "But don't get used to it. Onna-Bugeisha has a lot of practicing to do. It won't be so easy the next time we battle."
    
    menu:
        "You call that easy?":
            pf "I wouldn't say that was easy... Your team put up a good fight."
            show mei hap
            "Mei grins."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_65.ogg"
            ms "I know."
    
        "You're still going to lose.":
            pf "You can train, but we'll be training just as hard. The outcome will be the same."
            show mei hap
            "Mei grins."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_66.ogg"
            ms "We'll see."
    
        "This was a good fight.":
            pf "If the next match we have is half as good as the one we just had, I'll be satisfied."
            show mei hap
            "Mei grins."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_67.ogg"
            ms "Don't worry, us girls won't be going down easy."
    
    show mei smi
    "From the corner of my eye, I spot Kaori and Shou enter the Pilot's Lounge. Shou's still alive and in one piece! They must have worked things out with each other."
    "That's a relief. {w}Kaori searches the room and briefly makes eye contact with me before glancing away. Then, to my surprise, she walks over to us. Shou follows."
    
    stop music fadeout 5
    show mei sur
    
    show kaori neu at l3
    with dissolve
    
    show shou smi at r3:
        xzoom -1
    with dissolve
    "Mei is just as surprised when Kaori and Shou sit with us."
    show mei neu
    ### VOICE - missing line
    voice "audio/voice/MISSING/BATCH2/8.ogg"
    ss "What's going on, Broseph?"
    pf "Nothing much. Where's Mayu?"
    show mei smi
    show shou hap
    ### VOICE - missing line
    voice "audio/voice/MISSING/BATCH2/9.ogg"
    ss "Class."
    "I look over at Kaori."
    show shou smi
    pf "Hey, Kaori."
    voice "audio/voice/E3/D5/S2/kaori/1.ogg"
    ki "Hi."
    show kaori thi
    "She looks sideways at Mei."
    voice "audio/voice/E3/D5/S2/kaori/2.ogg"
    ki "Hi, Mei."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3.0
    show mei cur
    "Mei doesn't react right away..."
    show mei hap
    show kaori sur
    "...Then squeals in delight and throws her arms around Kaori!"
    show kaori sur b1
    show heart:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show mei smi
    $renpy.pause(.75)
    voice "audio/voice/E3/D5/S2/mei/MeiEp3_Line_68.ogg"
    ms "Hiiiiiiiiiiii!"
    show panic:
        xoffset 230
        yoffset 100
        xzoom .75
        yzoom .75
    show kaori ang b1 with dissolve
    voice "audio/voice/E3/D5/S2/kaori/3.ogg"
    ki "Ah! Mei! Stop it!"
    "Kaori pulls away in a huff while Mei laughs."
    scene black with fade
    stop ambient fadeout 3
    #fade out
    "The four of us continue to chat together. The tensions felt from yesterday are completely gone, as if the day never happened. Mei even got Kaori to laugh!"
    #stop music fadeout 3
    $renpy.pause(0.5)
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    #play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    "Eventually, we all go our separate ways as everyone heads to their class or other obligations. I still have some free time…"
    
    # AFTERNOON CHOICES
    
    $ freeTime = "afternoon"
    call E3FreeTime from _call_E3FreeTime_3
    
    jump E3D5S3