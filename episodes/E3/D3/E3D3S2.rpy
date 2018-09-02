#
label E3D3S2:
    
    "I make my way towards the cafe to meet with our account manager from Dasshu."
    stop ambient fadeout 3
    scene black with fade
    "I try to anticipate what kind of questions he'll ask about Eagle so I can have answers ready. Yuuna said this wasn't an interview, but I still want to make a good impression."
    play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 3
    scene bg campus cafe day with fade
    "As I enter the cafe, I sweep my gaze across the room and spot a man wearing a \"Dasshu\" jacket. That must be him. {w}After ordering a cup of coffee, I walk over to greet him."
    pf "Hello."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    $ yurGlasses = 1
    show yuri neu at cc with dissolve
    "The man faces me, and I'm surprised by how young he looks. {w}He only seems to be a couple of years older than us."
    pf "I'm [pfirst], the pilot for Eagle from ACE-2049-11."
    show yuri smi
    "He smiles and gestures to the seat across from him. I accept the seat."
    voice "audio/voice/E3/D3/S2/acc/1.ogg"
    acc "Thanks for meeting me on such short notice. As I'm sure you know, I'm Yuri Aliyev, your account manager with Dasshu."
    "A waitress places our drinks on the table."
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show yuri cur
    "He takes a sip from his drink and seems pleasantly surprised. That must be some good coffee."
    show yuri hap
    voice "audio/voice/E3/D3/S2/acc/2.ogg"
    acc "I'm not going to put you on the spot, but I am curious about a few things."
    pf "About EAGLE?"
    show yuri cur
    voice "audio/voice/E3/D3/S2/acc/3.ogg"
    acc "Eagle?"
    "He looks genuinely confused. I guess my intel was incorrect..."
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/4.ogg"
    acc "No, about HyperDrive."
    "HyperDrive? That was the team I played for at CINY. Looks like Yuri did his homework on me."
    
    menu:
        "Sure, ask away.":
            pf "I'll try to answer the best I can."
            show yuri smi
            "He smiles."
    
        "Someone wants the inside scoop.":
            pf "You want to know all their secrets, eh?"
            show yuri hap
            "He laughs."
            voice "audio/voice/E3/D3/S2/acc/5.ogg"
            acc "Not exactly."
    
        "I'm still under their NDA.":
            pf "Be aware that I still have an active NDA with them."
            show yuri smi
            "He nods."
            voice "audio/voice/E3/D3/S2/acc/6.ogg"
            acc "Of course."
            
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/7.ogg"
    acc "I am more interested about the team and sponsorship dynamics in the west. I've researched that companies have official teams in a school rather than just sponsoring a different team from time to time."
    "I nod."
    pf "That's right."
    show yuri mis
    voice "audio/voice/E3/D3/S2/acc/8.ogg"
    acc "HyperDrive is an S-ranked division team at CINY. That's quite the accomplishment. I can see why you transferred into ACE with a history like that."
    
    menu:
        "Hard work paid off.":
            pf "Thank you. I practiced a lot and studied to make sure my application was strong from both sides."
            show yuri smi
            "Yuri seems pleased by my answer."
    
        "I'm a natural.":
            pf "Really? It was pretty easy to be honest."
            show yuri hap
            "Yuri grins."
            voice "audio/voice/E3/D3/S2/acc/9.ogg"
            acc "Very confident. Interesting."
    
        "I was just their primary backup.":
            pf "It wasn't all that much. I was just the primary backup and not on the starting line."
            show yuri smi
            voice "audio/voice/E3/D3/S2/acc/10.ogg"
            acc "Primary backup on a S ranked division team while being a first year... I'd say that is quite the accomplishment."
            pf "I suppose so."
            
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/11.ogg"
    acc "What were your teammates like?"
    pf "HyperDrive had about 20 pilots on the team. I didn't know all of them well, but I made a few friends."
    "Yuri takes another sip from his coffee."
    show yuri cur
    voice "audio/voice/E3/D3/S2/acc/12.ogg"
    acc "Ah, yes. I've heard the official company teams tend to recruit purely from an efficiency and winning standpoint. There's even internal competition within the team to see who are the strongest pilots."
    "I nod."
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/13.ogg"
    acc "Which means your solo rank must have been strong if you were the primary backup after the starting four."
    pf "Yeah. Although, I can't say everyone was pleased with a first year being a primary backup."
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show yuri mis
    "Yuri chuckles."
    voice "audio/voice/E3/D3/S2/acc/14.ogg"
    acc "I take it the more senior members of the team weren't pleased?"
    pf "Yup. Because of that, most of the people I considered to be close were other first years. But some of the seniors who were already on the starting line-up would help me train."
    show yuri smi
    voice "audio/voice/E3/D3/S2/acc/15.ogg"
    acc "Sounds like there was a very split dynamic among the team, which is not surprising given how large it is. It's hard to foster close camaraderie when everyone competes for the same spots."
    pf "There were definitely a lot of cliques that formed within the group. I tried to stay away from any drama and was just focused on bringing up my rank." 
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/16.ogg"
    acc "How well do you think that model works compared to the model here?"
    "I pause."
    pf "The pressures are different, but I do believe smaller teams make more efficient teams."
    pf "You're more invested in your personal training and development, not because there is a looming pressure that someone is just a number away from replacing you, but because you're an important member of your team."
    pf "And of course, you end up fostering closer relationships with your teammates."
    pf "But the whole sponsorship process here is incredibly imbalanced."
    "Yuri nods understandingly."
    
    pf "Honestly, I'm grateful you agreed to sponsor us. We were rejected a few times before and Yuuna was really disappointed by how unwilling most companies were to consider us."
    show yuri smi
    voice "audio/voice/E3/D3/S2/acc/17.ogg"
    acc "Ah, your team at ACE is a little unique. Even though you guys are an S ranked division team, because you're a new team with no history of performance, you're also considered high risk."
    
    pf "High risk?"
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/18.ogg"
    acc "Yeah, it's hard to gauge whether your team is a strong up-and-comer or if your entry into this division was a fluke. Most companies don't like that uncertainty."
    pf "If that's the case, how come you decided to take that risk?"
    show yuri mis
    "He grins."
    voice "audio/voice/E3/D3/S2/acc/19.ogg"
    acc "I know good talent when I see it."
    voice "audio/voice/E3/D3/S2/acc/20.ogg"
    acc "If I'd been too afraid to take risks, I never would have landed Yuudai. When I signed him on he was a new pilot, but already showed so much potential."
    show yuri neu
    "He looks wistful."
    voice "audio/voice/E3/D3/S2/acc/21.ogg"
    acc "What happened to him was tragic."
    voice "audio/voice/E3/D3/S2/acc/22.ogg"
    acc "The least I could do is help his sister… Especially after seeing how his death affected her."
    pf "Wait, what happened?"
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/23.ogg"
    acc "You don't know?"
    stop music fadeout 10
    show dots:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    "He falters."
    show yuri neu
    voice "audio/voice/E3/D3/S2/acc/24.ogg"
    acc "You should probably talk to Yuuna."
    pf "Oh, um, sure."
    "An uncomfortable silence settles while we both sip at our drinks. Once he downs the last of his coffee, he checks his phone then smiles politely."
    stop music fadeout 7
    #play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    show yuri hap
    voice "audio/voice/E3/D3/S2/acc/25.ogg"
    acc "I have to run to another meeting. Thanks again for stopping in to chat with me, and I'm sure we'll see each other soon."
    pf "Thanks, it was nice to meet you."
    hide yuri with dissolve
    "I say my goodbye and take another sip of my drink as I watch him leave. {w}What happened to Yuuna's brother? How come she never mentioned him to me?"
    "Questions race through my mind, but I clear them away as I finish my drink. {w}I shouldn't drive myself crazy thinking about questions I don't have the answers to. The next time I see Yuuna, I'll ask."
    
    "In the meantime, I still have time before I should go home. What should I do to clear my mind?"
    
    #evening choice
    
    $ freeTime = "evening"
    call E3FreeTime from _call_E3FreeTime_5
    
    jump E3D3S3

