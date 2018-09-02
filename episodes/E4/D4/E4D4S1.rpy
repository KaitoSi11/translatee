#
label E4D4S1:
    
    #beep beep
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "Pilot"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "Pilot"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "Pilot"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ day = 1
    $ timeSpent = "none"
    
    
    #blackscreen
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 1
    
    "I slap off my alarm and feel unusually energised this morning. Today is our match against Akira. and after the training session yesterday with Coach Ivan, I feel confident in our abilities."
    "This should be an exciting match!"
    scene black with fade
    stop ambient fadeout 5
    "After getting ready, I wolf down my breakfast and drive to school."
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus building day with fade
    "Yuuna stops me on my way to the pre-combat room."
    show yuuna hap at cc with dissolve
    voice "audio/voice/E4/Yuuna/E4/D4/1.ogg"
    ym "Hey!"
    pf "Oh hey, Yuuna."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D4/2.ogg"
    ym "I'm glad I ran into you."
    pf "Does it count as running into me if you knew exactly where I would be?"
    show yuuna mis
    voice "audio/voice/E4/Yuuna/E4/D4/3.ogg"
    ym "Yes."
    "She grins and thrusts her tablet in front of me."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D4/4.ogg"
    ym "Do you mind filling out this survey really quickly?"
    pf "Survey for what?"
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D4/5.ogg"
    ym "The session with Coach Ivan. Since yesterday's guest coach was a new initiative for Dasshu, they'd like to gauge how valuable you all thought the session was."
    voice "audio/voice/E4/Yuuna/E4/D4/6.ogg"
    ym "I've managed to track down everyone else, so yours is the last form I need."
    pf "Okay."
    "I take a minute to fill out the survey. Once I'm finished, I hand the tablet back to Yuuna."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D4/7.ogg"
    ym "Thanks."
    pf "No problem. {w}I'm kind of impressed that Dasshu would go the extra mile to get someone like Coach Ivan to consult for a non-professional team."
    show yuuna hap
    "Yuuna smiles."
    voice "audio/voice/E4/Yuuna/E4/D4/8.ogg"
    ym "That's one of the reasons I like them."
    pf "I wonder how they got him to agree."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D4/9.ogg"
    ym "Oh, it was easy. All I had to do was call."
    pf "Wait, what?"
    voice "audio/voice/E4/Yuuna/E4/D4/10.ogg"
    ym "Yeah, I found his contact information online and figured it couldn't hurt to reach out. I asked his manager if this was something they'd be interested in and luckily it was. Then I introduced the idea to Dasshu along with the proposal I'd put together."
    voice "audio/voice/E4/Yuuna/E4/D4/11.ogg"
    ym "After that it was just a matter of getting their approval and support with logistics."
    pf "You put all of this together?"
    # dots
    show yuuna cur b1
    "Yuuna blinks in surprise, then blushes."
    voice "audio/voice/E4/Yuuna/E4/D4/12.ogg"
    ym "It wasn't all me."
    pf "But the idea was yours… {w}Actually, you helped out with some of the logistics for the Dasshu event before the Ex Zee concert too."
    show yuuna ner b1
    voice "audio/voice/E4/Yuuna/E4/D4/13.ogg"
    ym "Yeah, but it was for stuff involving the team. I wanted to make sure you guys were getting properly introduced and represented."
    
    if yuurelatonship == 1:
        pf "Yuuna, you're amazing."
        show yuuna smi b2
        "She blushes even deeper."
        # regBlush
        voice "audio/voice/E4/Yuuna/E4/D4/14.ogg"
        ym "It was nothing, really."
    
    else:
        pf "I had no idea…"
        show yuuna smi b1
        voice "audio/voice/E4/Yuuna/E4/D4/15.ogg"
        ym "I was just doing my job."
        pf "You're doing an amazing job."
        # regBlush
        show yuuna smi b2
        "She blushes even deeper."
        
    show yuuna hap b2
    voice "audio/voice/E4/Yuuna/E4/D4/16.ogg"
    ym "Anyway, thanks for filling this out."
    pf "Sure… I'd better go in now. Kaori's probably about to blow a blood vessel waiting for me."
    
    if yuurelatonship == 1:
        show yuuna smi b2
        "She nods, then gets on her toes and kisses me."
        # heart
        voice "audio/voice/E4/Yuuna/E4/D4/17.ogg"
        ym "For luck."
        pf "Mm, maybe I need another."
        show yuuna mis b2
        "She grins and our lips meet again."
        voice "audio/voice/E4/Yuuna/E4/D4/18.ogg"
        ym "Now you absolutely can't lose."
        pf "We won't."
    
    else:
        # note
        voice "audio/voice/E4/Yuuna/E4/D4/19.ogg"
        ym "Good luck out there!"
        pf "Thanks!"
        
    stop music fadeout 5
    hide yuuna with dissolve
    stop ambient fadeout 3
    scene black with fade
    "She waves goodbye before heading towards the stadium while I head into the pre-combat room."
    scene bg campus battleroom day with fade
    play music "audio/music/Inventory (GAME VERSION).ogg" fadein 7
    show shou neu at l3 with dissolve:
        xoffset -150
    show kaori neu at cc:
        xoffset 200
        xzoom -1
    show mayu neu at r3:
        xoffset 200
        xzoom -1
    with dissolve
    "I quickly change into my pilot's outfit and join the rest of my team at the holotable. Kaori is busy plotting out the arena and our respective GEARs as everyone else silently watches."
    "It's finally starting to set in that we we're being matched against the {i}top{/i} pilot at ACE. The confidence that I felt earlier wanes."
    
    if MCStory == 3:
        "Judging by the faces of my teammates, I'm not alone in this feeling."
    
    "After a couple more seconds, Kaori takes a step back from the holograph and looks over her handiwork."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_01.ogg"
    ki "Okay. This is what the War Games layout will be."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_02.ogg"
    ki "As you all know, we'll be facing against REBORN--Akira's team. Mayu, can you report on their GEAR composition and weaponry?"
    "Mayu nods and and her fingers dart across the holotable."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-01.ogg"
    ma "REBORN is fully sponsored by Aludian Enterprises, which means they provide REBORN with the same cutting edge weaponry that they provide their professional teams."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-02.ogg"
    ma "Each GEAR is kitted out for specific purposes. That means individually they may have weaknesses, but as a unit they cover each other's vulnerabilities."
    show shou ske
    voice "audio/voice/E4/Shou/d4/1 Copy.ogg"
    ss "Hold on... we may have actually lucked out."
    # question
    show mayu ske
    "Mayu shoots Shou a questioning look."
    show shou neu
    voice "audio/voice/E4/Shou/d4/2 Copy.ogg"
    ss "Well, you know how they're smashing everyone in terms of points? Win or lose, they're still going to be the number one seeded team."
    show kaori ske
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_03.ogg"
    ki "Okay, how does that help us?"
    voice "audio/voice/E4/Shou/d4/3 Copy.ogg"
    ss "This happened last year as well. When REBORN was guaranteed the first ranked spot, they subbed in their backup pilots."
    show mayu cur
    voice "audio/voice/E4/Mayu/D4/Mayu D4-03.ogg"
    ma "Really? I didn't even notice."
    voice "audio/voice/E4/Shou/d4/4 Copy.ogg"
    ss "It's not a well known fact because their four-man GEAR equipment is always the same, but if you dig into their pilot history you'll see it."
    show mayu neu
    voice "audio/voice/E4/Shou/d4/5 Copy.ogg"
    ss "And the stats show that when they started putting in their subs, their overall performance \"did\" decline, even if it was just a little."
    show kaori cur
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_04.ogg"
    ki "So, what you're saying is that we'll be fighting against their backups since they already have a guaranteed first seed?"
    # drop
    show shou thi
    voice "audio/voice/E4/Shou/d4/6 Copy.ogg"
    ss "Everyone but Phoenix."
    pf "Phoenix?"
    show shou neu
    show kaori neu
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_05.ogg"
    ki "Akira's GEAR. Only he pilots it."
    "I'm surprised by Shou. He certainly didn't provide the same input in our previous matches as he did in this one--even when one of our matches was against his own roommate. This match must really mean something to him."
    
    menu:
        "We can use this in our favour.":
            pf "We'll press any advantage we can get."
            "Kaori nods."
            voice "audio/voice/E4/Kaori/D4/Kaori_D4_06.ogg"
            ki "Agreed."
        
        "This will feel like a hollow victory if we win.":
            pf "So we're fighting against their B team? That's not satisfying at all."
            show shou ner
            voice "audio/voice/E4/Shou/d4/7 Copy.ogg"
            ss "Don't underestimate them, broseph. They're still members of REBORN."
            pf "Why would they not want to guarantee a perfect pre-season run? Or do they think they can beat us that easily?"
            "Mayu shakes her head."
            voice "audio/voice/E4/Mayu/D4/Mayu D4-04.ogg"
            ma "What they're doing is actually best for the team overall. Pilot backups train in simulations or a controlled environment. These matches give them an opportunity to gain live experience without any negative consequences."
            "I frown. She's right. I know she's right because my team back at CINY utilised this strategy too... but it still doesn't make me feel any better. It's like being robbed of a clean win--if we do win."
    
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_07.ogg"
    ki "Okay, so we can definitely use this to our advantage."
    "Kaori changes up some of the notes on the holotable."
    show shou smi
    voice "audio/voice/E4/Shou/d4/8 Copy.ogg"
    ss "I have an idea. What if we employ the same tactic we did against Tatsuo's team? Focus down Akira."
    show mayu thi
    "Mayu shakes her head."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-05.ogg"
    ma "That won't work. Claw of the Wild's \"team\" {i}is{/i} Tatsuo. However, every member of REBORN is going to be strong even without Akira."
    show mayu neu
    voice "audio/voice/E4/Shou/d4/9 Copy.ogg"
    ss "True, but Akira still surpasses the rest of his team in terms of skill. Instead of focusing on Akira, what if we try to pull him out and play a 3v3 against the other members?"
    show kaori ske
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_08.ogg"
    ki "Who's going to handle a 1v1 with Akira?"
    show kaori neu
    "We all look at each other. Although none of us want to admit it, it's painfully clear that he would beat any one of us in a duel."
    pf "I can do it. We might not be able to beat him in a straight match, but we at least I have my  overdrive mode as our pocket ace again."
    show kaori smi
    "Kaori nods."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_09.ogg"
    ki "And since we haven't used it since the qualifiers, they definitely won't be expecting that."
    show shou smi
    voice "audio/voice/E4/Shou/d4/10 Copy.ogg"
    ss "That's right! As long a you can keep Akira busy, we have a strong chance of beating the rest of the team and then helping you with Akira."
    show mayu smi
    voice "audio/voice/E4/Mayu/D4/Mayu D4-06.ogg"
    ma "It won't be that easy, but I think this is our best chance at winning."
    "We hash out the details of the plan on the holotable."
    show kaori neu
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_10.ogg"
    ki "Remember not to immediately activate your overdrive mode when you start."
    
    menu:
        "Of course.":
            "I nod."
            pf "I'll be on a timer once it activates--3 minutes--so I should use it wisely."
            show kaori smi
            voice "audio/voice/E4/Kaori/D4/Kaori_D4_11.ogg"
            ki "Exactly."
        
        "Why not?":
            "I raise an eyebrow."
            pf "That doesn't make sense."
            # question
            show shou ske
            voice "audio/voice/E4/Shou/d4/11 Copy.ogg"
            ss "Broseph, doesn't the overdrive mode have a time limit?"
            "...I think so. It gives me pretty much infinite energy but the duration is finite."
            show mayu neu
            voice "audio/voice/E4/Mayu/D4/Mayu D4-07.ogg"
            ma "I believe Valerie's report mentioned it lasts 3 minutes."
            pf "Alright, I'll pace myself."
        
        "You worry about your task, I'll worry about mine.":
            pf "Eagle and I've got this. Just make sure you guys take out the others."
            show kaori dis
            "Kaori glares at me but doesn't argue."
            
    show shou neu
    show mayu neu
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_12.ogg"
    ki "Let's recap then."
    show kaori neu
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_14.ogg"
    ki "We'll create distance between the three of us and Eagle. With suppressive fire, we'll make it impossible for them to even attempt to gang up."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_16.ogg"
    ki "If they stick together, we can keep our distance and trap them in crossfire. When they start to create distance with one another, Eagle will hard engage Phoenix and we'll do the same with our respective opponents."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_17.ogg"
    ki "Positioning will play a big part. We'll have to capitalise on the fact that Akira doesn't have as much team cohesion practice with the subs as he would with the regular starters."
    "Kaori looks at me."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_15.ogg"
    ki "You'll keep Akira engaged as long as you can and will use the overdrive mode if it starts to look bad."
    "I nod."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_18.ogg"
    ki "That leaves the rest of us with a three on three. It'll be a tough match, but we should be able to beat REBORN's substitute pilots without Akira there."
    voice "audio/voice/E4/Shou/d4/12 Copy.ogg"
    ss "What if broseph goes down?"
    
    menu:
        "A valid concern.":
            pf "We should plan that out too."
        
        "I thought you had my back, bro.":
            pf "Thanks for the vote of confidence."
            show mayu ner
            voice "audio/voice/E4/Mayu/D4/Mayu D4-08.ogg"
            ma "I don't think he meant it like that..."
            show shou thi
            "Shou nods."
            voice "audio/voice/E4/Shou/d4/13 Copy.ogg"
            ss "I just meant it would be best to make sure we have all our bases covered."
            
    show shou neu
    show mayu neu
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_19.ogg"
    ki "Depending on the battle condition, it might be worth going for the safer points if things aren't in our favour."
    show shou cur
    voice "audio/voice/E4/Shou/d4/14 Copy.ogg"
    ss "You mean take out the weakened GEARs instead of going for a win?"
    show kaori thi
    show shou neu
    "Kaori crosses her arms, but nods. I blink in surprise. {w}Judging by the sour look on her face, I can tell this strategy isn't ideal for her, but the Kaori from before would never have even considered it. {w}She then looks at Mayu."
    voice "audio/voice/E4/Mayu/D4/Mayu D4-09.ogg"
    ma "I agree. That would be the best course of action."
    voice "audio/voice/E4/Shou/d4/15 Copy.ogg"
    ss "Broseph fights Akira. We fight the the other three. We win and gang up on Akira afterwards, otherwise go for the safe points instead of trying for the win."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_20.ogg"
    ki "Correct."
    "Shou nods."
    pf "Okay, got it."
    "My nerves are still jumpy, but I feel positive about our plan."
    stop music fadeout 8
    # note
    show mayu hap
    voice "audio/voice/E4/Mayu/D4/Mayu D4-10.ogg"
    ma "We can do this!"
    show shou ske
    show kaori ske
    "Everyone stares at Mayu. She blinks, then pokes two fingers together."
    show mayu ner
    voice "audio/voice/E4/Mayu/D4/Mayu D4-11.ogg"
    ma "I-I mean, if we try..."
    show shou hap
    show kaori mis
    "The team laughs."
    
    if mayrelatonship == 1:
        show mayu smi
        "I'm happy to see Mayu finally start to come out of her shell. I'm so lucky to have her."
    
    else:
        show mayu smi
        "Ever since she got together with Shou, she's been a lot more confident. I'm really happy for her."
        
    # sfx ?
    "The alarm rings signalling for us to get to our stations."
    voice "audio/voice/E4/Kaori/D4/Kaori_D4_21.ogg"
    ki "Let's go!"
    hide kaori with dissolve
    "After one deep breath, I follow Kaori out of the room."
    
    #black screen
    scene black with fade
    
    jump E4D4S2
