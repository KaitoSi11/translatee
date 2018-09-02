#
label E4D2SS:
    
    show shou neu at cc with dissolve
    "As I glance around the group, everyone seems to be focused on the greenery around us… except for Shou, who seems to be focused on a perky hard body in a separate guided group further down the path."
    pf "Enjoying the view?"
    show shou cur
    "Shou snaps back to reality and grins."
    show shou smi
    voice "audio/voice/E4/Shou/d2/30 Copy.ogg"
    ss "You know it, broseph! It's beautiful."
    pf "Yeah… the garden is nice too."
    show dots:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "Shou pauses, then looks embarrassed."
    show shou thi
    voice "audio/voice/E4/Shou/d2/31 Copy.ogg"
    ss "Was I that obvious?"
    pf "Only if you consider openly staring obvious."
    show shou smi
    voice "audio/voice/E4/Shou/d2/32 Copy.ogg"
    ss "Well, what do you think of her? Cute, right?"
    
    menu:
        "Hell yeah!":
            pf "I certainly don't blame you for staring."
            show shou hap
            "Shou chuckles nervously."
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Shou/d2/33 Copy.ogg"
            ss "Let's not focus so much on me staring at her…"
        
        "Not my type.":
            pf "Eh."
            "I shrug."
            pf "She's alright, but not really my type."
            show shou ske
            voice "audio/voice/E4/Shou/d2/34 Copy.ogg"
            ss "Do you even have a type, broseph? I mean, you've been surrounded by girls and no one seems to really be your type."
            pf "Surrounded?"
            show shou neu
            voice "audio/voice/E4/Shou/d2/35 Copy.ogg"
            ss "Sure, at school... there's a major cutie with a booty over there…"
            
            if E2D5SS_Completed == 1:
                voice "audio/voice/E4/Shou/d2/36 Copy.ogg"
                ss "Those girls at my party…"
                
            if E2SSS4_Completed == 1:
                voice "audio/voice/E4/Shou/d2/37 Copy.ogg"
                ss "Those girls at the auto show my work put together…"
                
            pf "Okay, I got it."
            
    show shou smi
    voice "audio/voice/E4/Shou/d2/38 Copy.ogg"
    ss "We should go talk to her!"
    pf "I'm not sure Mayu would appreciate you doing that."
    show shou mis
    voice "audio/voice/E4/Shou/d2/39 Copy.ogg"
    ss "Not for me, for you!"
    pf "What?"
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou hap
    voice "audio/voice/E4/Shou/d2/40 Copy.ogg"
    ss "I'm going to wingman for you. It'll be a thank you for all those times you helped me out."
    pf "That's really not necessary--"
    hide shou with dissolve
    "My protests fall on deaf ears as Shou already starts to lag from the group. After he creates enough space, he hops off the path and walks through the garden."
    pf "What are you doing?"
    show shou smi at l3 with dissolve
    voice "audio/voice/E4/Shou/d2/41 Copy.ogg"
    ss "Taking a shortcut. We can't catch up to them by hanging around the group."
    pf "Smart thinking."
    show shou hap
    "He grins."
    voice "audio/voice/E4/Shou/d2/42 Copy.ogg"
    ss "I know!"
    "We pass our own group before hopping back on the path. I step back with no incident, but Shou trips and waves his arms wildly to balance himself."
    stop music fadeout 5
    show shou sur
    voice "audio/voice/E4/Shou/d2/43 Copy.ogg"
    ss "Whoa!"
    "He fails to keep his balance, but before he can faceplant on the hard gravel, I step in and catch him. As I continue to hold him up, Shou looks at me with admiration in his eyes."
    show shou cur at cc with dissolve
    voice "audio/voice/E4/Shou/d2/44 Copy.ogg"
    ss "You saved me, broseph!"
    pf "You would have done the same for me."
    "Suddenly, a croaky voice yells out."
    voice "audio/voice/E4/OldMan/(5).ogg"
    oldman "GET A ROOM!"
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
    show shou ske
    "Everyone around us freezes. As one, we turn towards the voice and see an old Japanese man waving his cane angrily in the air."
    show shou wor
    "Shou quickly removes himself from my arms and holds up his hands defensively."
    voice "audio/voice/E4/Shou/d2/45 Copy.ogg"
    ss "It's not what you think!"
    
    menu:
        "Yeah! I like girls!":
            pf "Yeah! We aren't together! In fact, we were on our way to talk to a girl!"
            show panic:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Shou/d2/46 Copy.ogg"
            ss "I have a girlfriend!"
            "The old man frowns."
            voice "audio/voice/E4/OldMan/(1).ogg"
            oldman "How inappropriate. Back in my day, a man's private affairs were kept private."
        
        "We are boyfriend and boyfriend.":
            pf "Yeah! We {i}were{/i} on our way to get a room!"
            show shou neu
            voice "audio/voice/E4/Shou/d2/47 Copy.ogg"
            ss "What."
            pf "We may be young and attractive but we aren't barbarians!"
            show panic:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            show shou wor
            voice "audio/voice/E4/Shou/d2/48 Copy.ogg"
            ss "What are you even saying?!"
            "The old man frowns so hard his wrinkles grow wrinkles."
            voice "audio/voice/E4/OldMan/(2).ogg"
            oldman "It's not right. Back in my day, love was between a man and a woman."
            pf "Well a lot has changed since the age of the dinosaurs."
            voice "audio/voice/E4/OldMan/(3).ogg"
            oldman "You damn miscreants!"
        
        "Mind your own business!":
            "I stare coldly at him."
            pf "How is what we are or aren't doing any of your business?"
            voice "audio/voice/E4/OldMan/(4).ogg"
            oldman "How rude. Back in my day young people respected their elders!"
    
    "With one last grumpy harrumph, the old man hobbles away towards the trees."
    pf "I thought we had to stay on the path…"
    show shou neu
    voice "audio/voice/E4/Shou/d2/49 Copy.ogg"
    ss "Forget about him, let's refocus our efforts--"
    show shou ner
    "Shou's face falls. I follow his line of sight and grimace as the cute girl laughs at us."
    pf "Maybe we should just go back…"
    show shou sad
    voice "audio/voice/E4/Shou/d2/50 Copy.ogg"
    ss "Yeah. Sorry, broseph."
    pf "It's okay."
    #black screen
    scene black with fade
    "Regrettably, we spent some more time together before rejoining the group."
    
    jump E4D2S2
