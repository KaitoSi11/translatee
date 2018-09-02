#
label E3_5S4:
    
    #EPISODE 3.5 (October 31th - Halloween)
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "Halloween"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "Halloween"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "Halloween"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "Halloween"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "Halloween"
    
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    stop sound
    scene bg homekaito myroom blurry with fade
    
    "I blink bleary eyes as my alarm wakes me and quickly slap it off. Why is this even going off today? I don't have anything planned for this morning so I can afford to sleep in."
    scene black with fade
    "I close my eyes, roll over, and fall back asleep."
    stop ambient fadeout 3
    $renpy.pause(1)
    "..."
    "....."
    $renpy.pause(1)
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    $renpy.pause(0.5)
    "After what feels like mere minutes, my slumber is once again disturbed. This time it's from the buzzing of my phone."
    scene bg homekaito myroom blurry with fade
    "My arm shoots out from beneath the blankets and grabs my phone. I squint from the blinding rays peeking through my curtains and retreat into the safety underneath my covers. {w}Hm, the call is from Shou."
    stop sound
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    pf "Hello?"
    voice "audio/voice/E4/Shou/d0/1 Copy Copy.ogg"
    ss "Broseph, you ready or what?"
    pf "Huh?"
    voice "audio/voice/E4/Shou/d0/2 Copy Copy.ogg"
    ss "...Were you sleeping? Dude, its 5:00PM."
    pf "What?!"
    scene bg homekaito myroom dusk with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    "I throw off my blanket and push back the curtains, letting in the blinding rays of… dusk."
    pf "Crap! How did I sleep the whole day away?"
    voice "audio/voice/E4/Shou/d0/3 Copy Copy.ogg"
    ss "I don't know, but the Halloween party is starting soon at the Pilot's Lounge! Do you have any idea what that means?!"
    
    menu:
        "Fun Party times!":
            pf "Yeah yeah, I'm getting ready now. I'll meet you on campus in a few."
        
        "Slutty everything.":
            pf "Costumes."
            voice "audio/voice/E4/Shou/d0/4 Copy Copy.ogg"
            ss "Yessss..."
            pf "Of the sexy variety."
            voice "audio/voice/E4/Shou/d0/5 Copy Copy.ogg"
            ss "You got that right!"
            "His excitement is infectious."
            pf "Don't worry, I'll be on campus soon enough."
        
        "I'd rather be sleeping.":
            pf "Meh."
            "Shou yells in my ear."
            voice "audio/voice/E4/Shou/d0/6 Copy Copy.ogg"
            ss "BROSEPH! Naughty nurses! Nekogirls! Maids--"
            "I pull the phone away from my ringing ear."
            pf "Alright, I got it! Geez."
            voice "audio/voice/MISSING/BATCH2/10.ogg"
            ss "Hurry up!"
            pf "I'm on my way."
    
    voice "audio/voice/E4/Shou/d0/7 Copy Copy.ogg"
    ss "Good, I'll see you there."
    "After hanging up, I throw my phone down on my bed and try to make myself look presentable."
    "I still have my old costumes from my time back at CINY. Any of them would be doable this time around. What do I want to dress up as?"
    
    $ E3_5S4_Costume = "None"
    
    menu:
        "One of the Ninja Rangers!":
            $ E3_5S4_Costume = "Ranger"
            "Time to cosplay my favourite anime!"
            "I pull out my Balance, the Ranger of Justice outfit."
            if E2KIS3_Ranger != "Justice":
                "Balance might not have been my favourite Ranger, but he definitely has the coolest outfit out of all of them."
        
        "Legolaz from Lord of the GEARs.":
            $ E3_5S4_Costume = "Legolaz"
            "One of my favourite fantasy characters, Legolaz!"
            "There's never been an archer as badass as him!"
        
        "Sexy Police Officer!":
            $ E3_5S4_Costume = "Officer"
            "Being sexy isn't just for the ladies. Guys can be a little risque during halloween too!"
            "I pull out a questionable police officer uniform that hugs a little too tight... or maybe it hugs {i}just right{/i}."
        
        "Badman, the Dark Night.":
            $ E3_5S4_Costume = "Badman"
            "I'm Badman."
            "'Nuff said."
    
  
    
    stop music fadeout 5
    "After prepping and changing into my costume, I hop on my bike and head to campus."
    scene black with fade
    $renpy.pause(1)
    #play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg campus building night with fade
    "When I reach the Pilot's Lounge main entrance, I text Shou… only to see him waving at me."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    show shou smi at cc with dissolve
    voice "audio/voice/E4/Shou/d0/8 Copy Copy.ogg"
    ss "Broseph!"
    pf "Hey."
    "He's in a Yasogamee High School uniform."
    pf "Pursona 4!"
    show shou hap
    "He grins."
    voice "audio/voice/E4/Shou/d0/9 Copy Copy.ogg"
    ss "That's right!"
    "I never noticed until now, but the \"real\" Shou looks and acts very similarly to Yozuke Hamanura."
    pf "That's a perfect Yozuke cosplay man. Good stuff."
    show shou ske
    "His eyes widen in surprise."
    # question
    voice "audio/voice/E4/Shou/d0/10 Copy Copy.ogg"
    ss "Yozuke?"
    pf "Yeah."
    show shou dis
    "He frowns."
    voice "audio/voice/E4/Shou/d0/11 Copy Copy.ogg"
    ss "No! Not Yozuke! I'm supposed to be Yuu Nurakami!"
    pf "...Mmm... I don't see it. You definitely fit the profile of a secondary character, the protagonist's best friend."
    show shou wor
    voice "audio/voice/E4/Shou/d0/12 Copy Copy.ogg"
    ss "No way! I won't settle for that role!"
    pf "I'm afraid it's already been decided..."
    pf "...Because you look {i}exactly{/i} like Yozuke in that cosplay."
    show shou ann
    "He looks like he's about to argue, but then sighs."
    # storm
    show shou neu
    voice "audio/voice/E4/Shou/d0/13 Copy Copy.ogg"
    ss "I knew I should have gotten the white wig sooner. It was still being delivered!"
    "At least he accepts his fate."
    show shou mis
    voice "audio/voice/E4/Shou/d0/14 Copy Copy.ogg"
    ss "Speaking of outfits..."
    "He looks at me."
    
    if E3_5S4_Costume == "Ranger":
        # note
        voice "audio/voice/E4/Shou/d0/15 Copy Copy.ogg"
        ss "Balance from Ninja Rangers!"
        pf "Yup, you know your anime."
        show shou smi
        voice "audio/voice/E4/Shou/d0/16 Copy Copy.ogg"
        ss "I watched it a ton as a kid."
        pf "Pfft, you still watch it now."
        # drop
        show shou hap
        "He scratches the back of his head and smiles."
        voice "audio/voice/E4/Shou/d0/17 Copy Copy.ogg"
        ss "Hehe, yep!"
    
    elif E3_5S4_Costume == "Legolaz":
        voice "audio/voice/E4/Shou/d0/18 Copy Copy.ogg"
        ss "One does not simply dress up as Legolaz. Where's your bow?"
        pf "Did you forget about the weapon code for ACE? We are still on campus."
        show shou cur
        "Shou blinks."
        voice "audio/voice/E4/Shou/d0/19 Copy Copy.ogg"
        ss "Oh, right. Good call."
    
    elif E3_5S4_Costume == "Officer":
        show shou ske
        voice "audio/voice/E4/Shou/d0/20 Copy Copy.ogg"
        ss "Why do you look like a male stripper?"
        pf "Don't hate me 'cause you ain't me."
        "I flex for good measure."
        # drop
        voice "audio/voice/E4/Shou/d0/21 Copy Copy.ogg"
        ss "You're not fooling anyone."
        pf "We'll see about that when we get to the party!"
    
    elif E3_5S4_Costume == "Badman":
        # note
        voice "audio/voice/E4/Shou/d0/22 Copy Copy.ogg"
        ss "Master Waine, which Badman are you?"
        pf "The best one."
        show shou smi
        "Shou nods solemnly."
        voice "audio/voice/E4/Shou/d0/23 Copy Copy.ogg"
        ss "I would expect nothing less."
    
    "Two guys dressed as salt and pepper shakers enter the building."
    show shou mis
    voice "audio/voice/E4/Shou/d0/24 Copy Copy.ogg"
    ss "Shall we get going?"
    pf "Where are the girls?"
    show shou smi
    voice "audio/voice/E4/Shou/d0/25 Copy Copy.ogg"
    ss "They met up in Kaori's dorm to get ready. They'll be over soon. We can head in first."
    pf "Alright."
    hide shou with dissolve
    
    stop ambient fadeout 3
    scene black with fade
    #play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    #play music "audio/music/Inventory (GAME VERSION).ogg" fadein 3
    scene bg campus lounge night with fade
    
    "We enter the Pilot's Lounge and I gape at the surroundings. There are fake cobwebs lining the corners of the ceiling and walls, and fake bats and spiders are strategically placed in nooks and crannies. The lights are dimmed, which gives the place a spookier feel. {w}I barely even recognise the Lounge! This place looks awesome!"
    
    "There's a decent number of people here, and I recognise most of the pilots. I assume there are also engineers and team managers here too. It's a little hard to tell who everyone is while they're in costume."
    "...And there are some pretty great costumes here! Some people went full out creative and dressed up as hilarious memes or puns while others shilled out for fancy, well-crafted costumes."
    "But of course, the winners of the evening are all of the beautiful ladies who can only technically be considered dressed."
    "I sigh contently."
    "This takes me back to my first CINY costume party."
    
    voice "audio/voice/E4/Shou/d0/26 Copy Copy.ogg"
    ss "I...I think I'm in heaven..."
    show shou sur at cc with dissolve
    "Shou's eyes are wide and his mouth hangs agape. He's staring hard at a group of girls dressed in a range of costumes, from sexy teachers to cute Japanese idol cosplays."
    # exclamation
    show shou cur
    voice "audio/voice/E4/Shou/d0/27 Copy Copy.ogg"
    ss "Woah, there they are!"
    "Shou points a group of girls standing near the couches. As I squint to get a better look, I realise it's the rest of our team."
    show shou smi
    voice "audio/voice/E4/Shou/d0/28 Copy Copy.ogg"
    ss "Looks like they made it here before us. C'mon!"
    hide shou with dissolve
    "Shou and I weave through the crowd and make our way to the girls."
    show valerie smi at r1 with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    show shou hap at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    show kaori neu at l1 behind valerie with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind kaori with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show yuuna neu at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    voice "audio/voice/E4/Shou/d0/29 Copy Copy.ogg"
    ss "Hey!"
    show shou sur b1
    "Shou's demeanor changes mid-word from excited to confused."
    
    
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L1.ogg"
    vb "Hey there, cuties."
    show yuuna hap
    voice "audio/voice/E4/Yuuna/E4/D0/1.ogg"
    ym "Hello!"
    ki "Hi."
    show mayu smi
    "Mayu smiles and waves."
    # dots
    show shou wor b2
    "Shou's face is bright red and he's having trouble making eye contact. {w}I don't blame him!"
    "Kaori is wearing a knight outfit from a currently popular fantasy anime… and in typical anime fashion, the armor is more aesthetically pleasing than functional."
    "As a healthy heterosexual male, Yuuna's witch costume makes it hard to focus on her face." 
    "Mayu is dressed in a cute magical girl cosplay. I'm impressed by the intricacies of her costume and how well it compliments her."
    "Finally, Valerie... I think the plethora of guys ogling her speaks volumes about her nekogirl outfit."
    
    
    if E3VBS3_Completed == 1 and E3VBS3_Nekogirl == 1:
        "It looks just as good on her this time as it did when she modeled it for me at the mall."
    elif E3VBS3_Completed == 1 and E3VBS3_Nekogirl == 0:
        "Valerie must have gone back another time to pick this up… unless she snuck it into her purchases that day she modeled it for me at the mall. Either way, I'm not complaining!"
        
    show valerie mis
    show yuuna smi
    "Valerie spins her tail playfully."
    voice "audio/voice/E4/Valerie/ValE4D0/ValE4D0L2.ogg"
    vb "So, what do you boys think?"
    # heart
    show shou hap b1
    show kaori dis
    voice "audio/voice/E4/Shou/d0/30 Copy Copy.ogg"
    ss "What a time to be alive."
    # note
    "Valerie giggles."
    show shou smi
    voice "audio/voice/E4/Shou/d0/31 Copy Copy.ogg"
    ss "Let's go get some drinks?"
    show kaori neu
    show mayu smi
    show valerie smi
    show yuuna smi
    #stop music fadeout 3
    "We all nod and head over to the bar."
    hide shou
    hide valerie
    with dissolve
    hide kaori
    hide mayu
    hide yuuna
    with dissolve
    
    ### TEST
    #$ mayrelatonship = 1
    #
    
    #play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 10
    
    if kaorelatonship == 1:
        jump E3_5KI
    elif mayrelatonship == 1:
        jump E3_5MA
    elif valrelatonship == 1:
        jump E3_5VB
    elif yuurelatonship == 1:
        jump E3_5YM
    else:
        scene black with fade
        "I excuse myself to freshen up in the restroom as the group heads towards the bartender."
        jump E3_5S5
        
