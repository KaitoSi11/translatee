#
label E4D1S2:
    
    scene black with fade
    $renpy.pause(1)
    #play music "audio/music/Idle Conversation (GAME VERSION).ogg"
    scene bg campus hangar day with fade
    
    "Kaori is the first to arrive."
    show kaori neu at r2:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at r3:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    with dissolve
    voice "audio/voice/E4/Kaori/D1/Kaori_01_d1.ogg"
    ki "This better be important. Exams are next week, you know."
    pf "Trust me, you'll want to hear this."
    show kaori thi
    "Kaori taps her foot impatiently."
    voice "audio/voice/E4/Kaori/D1/Kaori_02_d1.ogg"
    ki "Where is everybody else?"
    pf "They're coming."
    show kaori dis
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 10
    "A few minutes later, Shou and Mayu trickle in with Yuuna tagging along."
    show kaori dis at r2:
        xoffset 50
        xzoom -0.75
        yzoom 0.75
    show valerie neu at r3 behind kaori:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    with dissolve
    show mayu neu at l2 behind shou:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show shou smi at cc behind kaori:
        xzoom 0.75
        yzoom 0.75
    with dissolve
    show yuuna neu at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    with dissolve
    voice "audio/voice/E4/Mayu/D1/Mayu D1-01.ogg"
    ma "Sorry if we're late…"
    show shou hap
    voice "audio/voice/E4/Shou/d1/1 Copy.ogg"
    ss "Look who we found trying to break into the Hangar!"
    show yuuna ner b1
    "Yuuna's cheeks flush."
    voice "audio/voice/E4/Yuuna/E4/D1/1.ogg"
    ym "I wasn't trying to break in! I was just about to text that I needed someone to let me in."
    show kaori ske
    show shou mis
    "Shou grins."
    voice "audio/voice/E4/Shou/d1/2 Copy.ogg"
    ss "Sure, that explains why you were pulling on the doors."
    show drop:
        xoffset 30
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna thi b1
    voice "audio/voice/E4/Yuuna/E4/D1/2.ogg"
    ym "I was just... testing to see if maybe they were unlocked…"
    show shou smi
    pf "Wait, Yuuna, how did you get on campus so fast?"
    show yuuna smi b1
    voice "audio/voice/E4/Yuuna/E4/D1/3.ogg"
    ym "I was studying in the library when I got your text."
    show kaori neu
    voice "audio/voice/E4/Kaori/D1/Kaori_03_d1.ogg"
    ki "Speaking of which, can you finally tell us what's going on so we can all get back to studying?"
    show valerie smi
    show yuuna neu
    "I glance over at Valerie who nods."
    pf "Valerie found out how to activate Eagle's overdrive mode on demand."
    show exclamation:
        xoffset 30
        yoffset 100
        xzoom .5
        yzoom .5
    show yuuna sur
    show shocked:
        xoffset 720
        yoffset 20
        xzoom .5
        yzoom .5
    show shou sur
    with dissolve
    show kaori cur
    show mayu sur
    with dissolve
    voice "audio/voice/E4/Shou/d1/3 Copy.ogg"
    ss "Are you serious?!"
    "Shou's voice rings out above the team's collective exclamations of surprise."
    show valerie hap
    "Valerie nods."
    show note:
        xoffset 1575
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L32.ogg"
    vb "Yup! Sorry it took so long."
    show shou neu
    show kaori mis
    show mayu neu
    voice "audio/voice/E4/Kaori/D1/Kaori_04_d1.ogg"
    ki "The fact that you managed to figure it out at all is really impressive."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D1/4.ogg"
    ym "Yeah, I don't think just anyone would have been able to."
    show valerie smi b1
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L33.ogg"
    vb "Maybe."
    "Valerie answers modestly but there's a slight blush of colour in her cheeks."
    show kaori neu
    show shou ske
    voice "audio/voice/E4/Shou/d1/4 Copy.ogg"
    ss "So what exactly do you mean by \"overdrive mode can be activated on demand\"?"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L34.ogg"
    vb "Well, initially the programming was set to a single run instance because it was in debug mode."
    
    if E3D4S2_Takedown == 0 or E3D4S2_Duelist == 0:
        show mayu cur
        voice "audio/voice/E4/Mayu/D1/Mayu D1-02.ogg"
        ma "That explains why your core didn't react last match when you got depowered."
        "I nod."
        show mayu neu
        
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L35.ogg"
    vb "I found a way to change the options of activation."
    show valerie neu
    show shou neu
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L36.ogg"
    vb "That being said, it's calibrated and tested in simulation but..."
    "Valerie looks at me."
    pf "We want to reserve the arena so we can live test it."
    "Kaori nods."
    voice "audio/voice/E4/Kaori/D1/Kaori_05_d1.ogg"
    ki "That makes sense. We definitely want to get a handle of it before our next match on Thursday."
    pf "Why exactly do we have a match scheduled during reading week?"
    show kaori ske
    show shou ske
    show yuuna ner
    "Everyone stares blankly at me."
    show question:
        xoffset 1250
        yoffset 110
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Kaori/D1/Kaori_06_d1.ogg"
    ki "Why wouldn't we?"
    pf "At CINY, everything was cancelled during reading week--classes, clubs, everything. They really wanted us to focus on studying."
    show shou ner
    voice "audio/voice/E4/Shou/d1/5 Copy.ogg"
    ss "That must have been torture!"
    show kaori neu
    show yuuna neu
    show mayu thi
    voice "audio/voice/E4/Mayu/D1/Mayu D1-03.ogg"
    ma "I don't think it's a terrible idea. That just means there are fewer distractions from studying."
    show frightful:
        xoffset 810
        yoffset 50
        xzoom .5
        yzoom .5
    show shou wor
    voice "audio/voice/E4/Shou/d1/6 Copy.ogg"
    ss "I know… torture!"
    show mayu neu
    
    menu:
        "I preferred it that way.":
            pf "I actually appreciated that everything was cancelled. It helped me focus on studying, and I got high marks on my exams last year."
    
            if E3D6S1_ChoseYuuna == 1:
                show yuuna hap
                "Yuuna smiles."
                show note:
                    xoffset 30
                    yoffset 100
                    xzoom .5
                    yzoom .5
                voice "audio/voice/E4/Yuuna/E4/D1/5.ogg"
                ym "If our study sessions are any indication, I'm positive you'll pass with flying colors this year too."
                show yuuna smi
                "I match her grin."
                pf "Thanks."
            
            elif E3D6S1_ChoseYuuna == 0 and E1D5S1_EventYuuna == 1:
                show yuuna hap
                "Yuuna smiles."
                show note:
                    xoffset 30
                    yoffset 100
                    xzoom .5
                    yzoom .5
                voice "audio/voice/E4/Yuuna/E4/D1/6.ogg"
                ym "If our history project was any indication, I'm sure you'll do well this year too."
                show yuuna smi
                "I match her grin."
                pf "Thanks."
            
            else:
                show shou sad
                "Shou shakes his head."
                voice "audio/voice/E4/Shou/d1/7 Copy.ogg"
                ss "Broseph, you have much to learn."
    
        "Tell me about it!":
            pf "Seriously, I was so bored I found myself actually missing class…"
            show shou sad
            "Shou pats my shoulder sympathetically."
            voice "audio/voice/E4/Shou/d1/8 Copy.ogg"
            ss "I am so sorry."
        
        "They didn't have to cancel {i}everything{/i}.":
            pf "It was nice that classes were cancelled, but I suppose cancelling all clubs and activities was a bit much."
            show shou neu
            "Shou nods."
            
    show kaori thi
    voice "audio/voice/E4/Kaori/D1/Kaori_07_d1.ogg"
    ki "Focus, guys!"
    show shou ner
    voice "audio/voice/E4/Shou/d1/9 Copy.ogg"
    ss "Sorry…"
    show kaori neu
    show yuuna neu
    "Yuuna seems thoughtful."
    show shou neu
    voice "audio/voice/E4/Yuuna/E4/D1/7.ogg"
    ym "Since your match is on Thursday, that doesn't give you much time to practice. Isn't the arena already booked up this week?"
    pf "Actually, it's completely open tomorrow. I was thinking we could head over around--"
    stop music fadeout 3
    show kaori ner
    show exclamation:
        xoffset 810
        yoffset 50
        xzoom .5
        yzoom .5
    show shou wor
    with dissolve
    show yuuna wor
    show mayu wor
    with dissolve
    voice "audio/voice/E4/Shou/d1/10 Copy.ogg"
    ss "NO! Are you crazy?! We can't do that!"
    show valerie ske
    "I blink at Shou's outburst. Valerie looks just as confused as I am, but the rest of team wears matching looks of horror."
    show question:
        xoffset 1575
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L37.ogg"
    vb "What is up with those faces? You guys look like you've seen a ghost."
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    show shou thi
    voice "audio/voice/E4/Shou/d1/11 Copy.ogg"
    ss "I mean, you're not too far off. The arena is haunted!"
    show valerie hap
    "Valerie bursts out laughing and I let out a few chuckles."
    pf "What are you talking about? We've used the arena plenty of times and we've been fine."
    show shou ner
    voice "audio/voice/E4/Shou/d1/12 Copy.ogg"
    ss "It's not always haunted… only tomorrow!"
    show kaori ann
    show valerie smi
    voice "audio/voice/E4/Kaori/D1/Kaori_08_d1.ogg"
    ki "It's not haunted, you idiot!"
    "I can always count on Kaori to be reasonable."
    show kaori wor
    voice "audio/voice/E4/Kaori/D1/Kaori_09_d1.ogg"
    ki "It's cursed!"
    "...Nevermind."
    pf "What?"
    show valerie cur
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L38.ogg"
    vb "How is it cursed?"
    voice "audio/voice/E4/Yuuna/E4/D1/8.ogg"
    ym "It's the curse of Yori and Nori."
    show kaori ner
    show valerie neu
    pf "You too, Yuuna?"
    show shou ske
    voice "audio/voice/E4/Shou/d1/13 Copy.ogg"
    ss "Broseph, Yori and Nori are no joke! Haven't you heard the legend?"
    pf "No…"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L39.ogg"
    vb "What legend?"
    show shou dis
    show kaori neu
    show mayu neu
    show yuuna wor
    "Shou takes on a serious tone."
    voice "audio/voice/E4/Shou/d1/14 Copy.ogg"
    ss "Many years ago, there was a set of twin brothers, Nori and Yori, who attended ACE, and they were both top pilots here."
    voice "audio/voice/E4/Shou/d1/15 Copy.ogg"
    ss "They were fiercely competitive in the arena, and their matches were thrilling to watch. Yori was the older twin by a few seconds, and no matter how often they battled, he always took first rank."
    show shou neu
    voice "audio/voice/E4/Shou/d1/16 Copy.ogg"
    ss "Nori hated being outmatched and overshadowed by his brother and trained harder than any other pilot at school."
    voice "audio/voice/E4/Shou/d1/17 Copy.ogg"
    ss "At the end of the season, the twins' highly anticipated match was just as exciting as ever--especially when Nori took the title of first rank from his brother!"
    pf "I guess Nori's training finally paid off."
    show valerie ske
    "Valerie raises an eyebrow."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L40.ogg"
    vb "Seriously? This is so cliche!"
    show shou dis
    "Shou gives her a look but otherwise ignores her."
    voice "audio/voice/E4/Shou/d1/18 Copy.ogg"
    ss "It was all anyone could talk about, but Yori was furious. He didn't think it was possible that his brother could surpass him. He accused his brother of cheating and continued to pester Nori until Nori couldn't take it anymore."
    show shou neu
    voice "audio/voice/E4/Shou/d1/19 Copy.ogg"
    ss "They agreed to one final match--no holds barred--which would prove who was the better pilot once and for all."
    voice "audio/voice/E4/Shou/d1/20 Copy.ogg"
    ss "Obviously, the school would never allow no holds barred matches so they set up a time after hours to meet in the arena."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L41.ogg"
    vb "Boooring!"
    show kaori wor
    voice "audio/voice/E4/Kaori/D1/Kaori_10_d1.ogg"
    ki "Just wait!"
    show valerie neu
    voice "audio/voice/E4/Shou/d1/21 Copy.ogg"
    ss "When they met in the ring, they readied their weapons like usual. Charging their laser guns, they waited for the signal…"
    show shou ner
    voice "audio/voice/E4/Shou/d1/22 Copy.ogg"
    ss "As soon as it sounded, they simultaneously unleashed their shot which collided in a huge explosion!"
    show kaori ner
    show storm:
        xoffset 1575
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie dis
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L42.ogg"
    vb "That's not how explosions happen!"
    show shou wor

    voice "audio/voice/MISSING/BATCH2/12.ogg"
    ss "Trust me! It happened! I don't know how it did, but it did!"
    "Mayu and Yuuna nod along with Shou."
    show shou ner
    voice "audio/voice/E4/Shou/d1/23 Copy.ogg"
    ss "After the smoke cleared, standing in the middle of the arena were the twins' two GEARs."
    pf "Okay..."
    show shou wor
    voice "audio/voice/E4/Shou/d1/24 Copy.ogg"
    ss "That's not the weird part. The weird part is that there was no trace of the brothers. Both the cockpits were completely empty!"
    show frightful:
        xoffset 315
        yoffset 135
        xzoom .5
        yzoom .5
    "Mayu shudders."
    voice "audio/voice/E4/Mayu/D1/Mayu D1-04.ogg"
    ma "There weren't even ashes or anything."
    show valerie ann
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L43.ogg"
    vb "Wait, let's go back a second to this \"explosion\". How did the GEARs even survive that?"
    show shou neu
    voice "audio/voice/E4/Shou/d1/25 Copy.ogg"
    ss "That's part of the mystery."
    show shou thi
    voice "audio/voice/E4/Shou/d1/26 Copy.ogg"
    ss "They say that the brothers' spirits are trying to finish that battle to see who is the better pilot, and any pilot who dares get between them will suffer the consequences."
    show valerie ske
    "Valerie cocks her head to the side."
    show drop:
        xoffset 1575
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L44.ogg"
    vb "You guys really believe this stuff?"
    show shou ner
    voice "audio/voice/E4/Yuuna/E4/D1/9.ogg"
    ym "It's real! Ever since then, anyone who's used their GEAR on the anniversary of the brothers' battle has ended up with serious injuries."
    show kaori sur
    voice "audio/voice/E4/Kaori/D1/Kaori_11_d1.ogg"
    ki "Yeah, there was the kid who's GEAR malfunctioned and started moving on its own!"
    show kaori wor
    show mayu sad
    voice "audio/voice/E4/Mayu/D1/Mayu D1-05.ogg"
    ma "And the girl who's GEAR got stuck after it depowered so she was trapped inside. They had to remove the whole front of her cockpit to get her out."
    show panic:
        xoffset 30
        yoffset 100
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Yuuna/E4/D1/10.ogg"
    ym "Those are just the reported ones! A lot of times what happens in the arena stays in the arena..."
    show valerie neu
    "Valerie looks at me."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L45.ogg"
    vb "What do you think?"
    show kaori ner
    
    menu:
        "I can't handle the curse!":
            stop music fadeout 5
            pf "The arena is clearly cursed!"
            show valerie wor
            "Valerie groans."
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L46.ogg"
            vb "Oh no, not you too?"
            pf "I've got enough to deal with without having to worry about vengeful spirits."
    
        "I got 99 problems but a curse ain't one.":
            stop music fadeout 5
            pf "I don't believe in ghosts or curses."
            show shou ske
            voice "audio/voice/E4/Shou/d1/27 Copy.ogg"
            ss "Then how do you explain all the bad things that have happened on that day?"
            pf "I don't know... coincidence?"
    
        "Better safe than sorry.":
            stop music fadeout 5
            pf "I don't want to tempt fate. We can check out my core another day."
            show valerie wor
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L47.ogg"
            vb "Aw, are you sure you wouldn't rather test it out?"
            pf "Ehh…"
            

    show shou neu
    voice "audio/voice/E4/Shou/d1/28 Copy.ogg"
    ss "The point is we {i}cannot{/i} be anywhere near our GEARs tomorrow."
    show kaori neu
    show valerie neu
    show yuuna neu
    show mayu neu
    with dissolve
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show shou smi
    voice "audio/voice/E4/Shou/d1/29 Copy.ogg"
    ss "In fact, we should get out of ACE Academy all together and go somewhere fun!"
    show valerie cur
    "Valerie's dismissiveness shifts to intrigue."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L48.ogg"
    vb "Oooh, I like fun!"
    pf "Where were you thinking?"
    show shou hap
    "A sly grin spreads across Shou's face as he whips out a handful of tickets."
    show valerie cur
    show mayu cur
    voice "audio/voice/E4/Shou/d1/30 Copy.ogg"
    ss "The hot springs, of course!"
    show yuuna cur
    pf "How long have you been carrying those?"
    show shou mis
    voice "audio/voice/E4/Shou/d1/31 Copy.ogg"
    ss "You don't want to know."
    show valerie smi
    "I raise an eyebrow."
    show shou hap
    show mayu neu
    voice "audio/voice/E4/Shou/d1/32 Copy.ogg"
    ss "Let's just say I've got these ready for next year too."
    pf "That sounds like a whole lot of fan service."
    show shou smi
    voice "audio/voice/E4/Shou/d1/33 Copy.ogg"
    ss "I don't know what you're talking about."
    show valerie hap
    "Valerie squeals and starts playing with her hair."
    show heart:
        xoffset 1575
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L49.ogg"
    vb "I can't wait to go! The water is going to feel so good…"
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D1/11.ogg"
    ym "I could use a break from studying…"
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L50.ogg"
    vb "You should come, Yuuna!"
    show yuuna hap
    "Yuuna smiles."
    voice "audio/voice/E4/Yuuna/E4/D1/12.ogg"
    ym "Okay, you've convinced me."
    show valerie mis
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L51.ogg"
    vb "Wow, that was easier than I thought."
    show yuuna smi
    voice "audio/voice/E4/Shou/d1/34 Copy.ogg"
    ss "What about you, Kaori?"
    show kaori dis
    "Kaori frowns."
    show valerie smi
    voice "audio/voice/E4/Kaori/D1/Kaori_13_d1.ogg"
    ki "We don't have time for this. Don't you all have exams to study for?"
    show shou mis
    voice "audio/voice/E4/Shou/d1/35 Copy.ogg"
    ss "We've got the whole week to study! Besides, even Mayu's going."
    show mayu ner b1
    "Mayu looks away as Kaori's gaze lands on her."
    show kaori ske
    voice "audio/voice/E4/Kaori/D1/Kaori_12_d1.ogg"
    ki "Are you going too?"
    voice "audio/voice/E4/Mayu/D1/Mayu D1-06.ogg"
    ma "Yeah… I'll study better once I've had a short break."
    
    if kaorelatonship == 1:
        pf "You should go too, Kaori. It wouldn't be nearly as fun without you there."
        show kaori cur b1
        "Kaori's cheeks turn pink."
        voice "audio/voice/E4/Kaori/D1/Kaori_14_d1.ogg"
        ki "O-Oh, does that mean you're going too?"
        pf "Only if you are."
        show kaori ner b2
        "Her face reddens even more."
        voice "audio/voice/E4/Kaori/D1/Kaori_15_d1.ogg"
        ki "I guess I can go… but we can't stay longer than a day!"
        show shou smi
        voice "audio/voice/E4/Shou/d1/36 Copy.ogg"
        ss "Of course not! We'll be back the following morning."
        show kaori thi b2
        voice "audio/voice/E4/Kaori/D1/Kaori_16_d1.ogg"
        ki "We better be, or I'm coming back without you."
        "Shou throws his arms around us."
    
    else:
        show shou hap
        voice "audio/voice/E4/Shou/d1/37 Copy.ogg"
        ss "C'mon Kaori! Live a little! If Mayu can go, then you can go. I mean, does anyone here study more than she does?"
        show mayu wor b1
        "Mayu frowns."
        voice "audio/voice/E4/Mayu/D1/Mayu D1-07.ogg"
        ma "What's that supposed to mean?"
        show kaori dis
        show shou smi
        voice "audio/voice/E4/Shou/d1/38 Copy.ogg"
        ss "Just that you're really smart."
        
        if mayrelatonship == 0:
            show mayu ner b2
            "Mayu blushes deeply but looks pleased."
        else:
            show mayu smi b1
            "Mayu smiles."
            
        show shou mis
        voice "audio/voice/E4/Shou/d1/39 Copy.ogg"
        ss "Soooo, you coming, Kaori?"
        show kaori thi
        show mayu smi b1
        "Kaori sighs."
        show storm:
            xoffset 1250
            yoffset 110
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Kaori/D1/Kaori_17_d1.ogg"
        ki "Fine, but I'm coming back first thing the next morning with or without you guys!"
        
    show note:
        xoffset 720
        yoffset 20
        xzoom .5
        yzoom .5
    show shou hap
    show mayu smi
    voice "audio/voice/E4/Shou/d1/40 Copy.ogg"
    ss "Yes! The gang's all going!"
    show kaori neu
    voice "audio/voice/E4/Kaori/D1/Kaori_18_d1.ogg"
    ki "Since my day tomorrow is pretty much shot, I need to get as much studying done now as I can. I'll see you guys later."
    hide kaori with dissolve
    "Kaori hurries out."
    show shou smi
    pf "I actually should get some studying done too."
    voice "audio/voice/E4/Yuuna/E4/D1/13.ogg"
    ym "Me too."
    voice "audio/voice/E4/Mayu/D1/Mayu D1-08.ogg"
    ma "Same here."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L52.ogg"
    vb "It's time for me to hit the books too."
    show shou ske
    show yuuna cur
    show mayu cur
    "Everyone pauses to stare at her."
    show valerie ske
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L53.ogg"
    vb "What?"
    voice "audio/voice/E4/Shou/d1/41 Copy.ogg"
    ss "...You study?"
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L54.ogg"
    vb "Of course! How else do you think I get straight A's?"
    show shou sur
    "Shou's eyes widen."
    voice "audio/voice/E4/Shou/d1/42 Copy.ogg"
    ss "...You have straight A's?!"
    show valerie mis
    "Valerie laughs."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L55.ogg"
    vb "Don't sound so surprised!"
    show yuuna neu
    show mayu neu
    
    if valrelatonship == 1:
        show shou mis
        "Shou puts his hand on my shoulder."
        voice "audio/voice/E4/Shou/d1/43 Copy.ogg"
        ss "You sure know how to pick 'em, broseph."
        show valerie hap
        "I grin and Valerie seems pleased."
        
    show shou sad
    voice "audio/voice/E4/Shou/d1/44 Copy.ogg"
    ss "Aww, if everyone else is going to study then what am I supposed to do?"
    show valerie smi
    pf "...Study?"
    show shou thi
    "Shou sighs."
    voice "audio/voice/E4/Shou/d1/45 Copy.ogg"
    ss "I guess."
    show yuuna smi
    
    if mayrelatonship == 0:
        show mayu smi
        voice "audio/voice/E4/Mayu/D1/Mayu D1-09.ogg"
        ma "We can study together."
        show shou cur
        "Shou perks up."
        show shou hap
        voice "audio/voice/E4/Shou/d1/46 Copy.ogg"
        ss "Suddenly studying sounds like a great idea!"
        show regBlush:
            xoffset 315
            yoffset 135
            xzoom .5
            yzoom .5
        show mayu smi b1
        "Mayu smiles shyly. Shou takes her hand and the two of them wave before walking away."
        hide shou
        hide mayu
        with dissolve
    
    else:
        pf "You'll be fine."
        show shou neu
        voice "audio/voice/E4/Shou/d1/47 Copy.ogg"
        ss "I guess. See you guys later."
        hide shou with dissolve
        "He sighs deeply one last time before heading off."
        pf "What are the odds that he'll actually study?"
        show mayu smi
        voice "audio/voice/E4/Mayu/D1/Mayu D1-10.ogg"
        ma "Slim to none."
    
    pf "Alright, well, I'm out. I'll see you guys later."
    hide valerie
    hide yuuna
    hide mayu
    with dissolve
    "Everyone says their goodbyes and heads their separate ways."
    stop ambient fadeout 3
    #black screen
    scene black with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 5
    scene bg campus library day with fade
    stop music fadeout 3
    "I find a quiet spot in the library and spend a few hours studying."
    scene black with dissolve
    #time skip
    $renpy.pause(2.5)
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    scene bg campus library day with fade
    "Once the words start to blur on the page, I decide to take a break. I wonder if anyone else is ready for a break too?"
    
    $ freeTime = "afternoon"
    
    call E4FreeTime from _call_E4FreeTime_2
    
    jump E4D1S3
