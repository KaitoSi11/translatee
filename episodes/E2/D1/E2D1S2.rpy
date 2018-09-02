# E2D1S2
label E2D1S2:
    
    stop music
    stop ambient
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    #afternoon choice 1 ends

    "Remembering that the team rankings were supposed to be posted this morning, I take out my phone and notice an unread email from the school. {w}The rankings are posted online and can be accessed through the weblink. {w}I tap on the link embedded in the email and wait."
    "..."
    "The page doesn't load. Damn thing still isn't working for me."
    "There's a note at the bottom of the email saying a physical copy of the ranking is posted in the Pilot's Lounge, so I head there."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(2.5)
    #Lounge
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
    scene bg campus lounge day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1

    "Upon entering, I notice a crowd of pilots on the opposite wall in front of the posted ranks. They're surrounding a smiling guy with white hair and showering him with praise."

    if E1D3S5_AkiraNoticedMe == 1:
        "I have a brief feeling of deja-vu."

    "Pushing past the crowd, I eagerly check the board and search for my team. My stomach twists into knots… I really don't know what to expect. {w}Once I find our team, I breathe a sigh of relief.{w} Rank 21--that's not bad at all!"
    "The pilots beside me are still talking and I tune into their conversation."
    show akira neu at cc with dissolve
    show studentM extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E2/D1/S2/stu2m/1.ogg"
    stu2m "Congratulations on being ranked number one again this year, Akira!"
    show bully2 extra at l3 with dissolve:
        xoffset -100
    voice "audio/voice/E2/D1/S2/stu8m/1.ogg"
    stu8m "Yeah! That's awesome!"
    show akira smi at cc
    voice "audio/voice/E2/D1/S2/Akira/1.ogg"
    am "Thanks guys, but it's actually my team who deserves the congratulations. They all fought really well."
    voice "audio/voice/E2/D1/S2/stu2m/2.ogg"
    stu2m "Still, you were a big reason why your team got first rank. I watched the match and you were amazing out there."
    show akira hap at cc
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D1/S2/Akira/2.ogg"
    am "Thanks, I appreciate it."
    voice "audio/voice/E2/D1/S2/stu8m/2.ogg"
    stu8m "Don't you already have a sponsor too?"
    show akira smi at cc
    voice "audio/voice/E2/D1/S2/Akira/3.ogg"
    am "Yeah."
    voice "audio/voice/E2/D1/S2/stu8m/3.ogg"
    stu8m "Who is it?"
    voice "audio/voice/E2/D1/S2/Akira/4.ogg"
    am "It's Aludian Enterprises."
    voice "audio/voice/E2/D1/S2/stu8m/4.ogg"
    stu8m "I've heard their weapons are pretty cutting edge."
    voice "audio/voice/E2/D1/S2/stu2m/3.ogg"
    stu2m "Wow, you're so lucky! You basically had a sponsor waiting for you."
    hide studentM
    hide bully2
    with dissolve
    hide akira with dissolve
    "Before anyone else can reply, a group of girls cut through the crowd to read the rankings."
    show mei cur at cc with dissolve
    "A tall girl with long, dark hair steps forward and squints at the board, then she cheers excitedly."
    show mei hap at cc
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D1/S2/Mei/1.ogg"
    ms "Hey! We made it in the top ten!"
    # sprite jumping animation?
    "As she jumps up in excitement, my eyes are drawn to her chest… {w}but I look away before I catch myself staring. {w}Glancing around me, it seems like I wasn't the only guy she distracted…"
    show mei smi at cc
    voice "audio/voice/E2/D1/S2/stu3f/1.ogg"
    stu3f "Are you serious, Mei?"
    show studentF2 extra at l2 behind mei with dissolve
    "One of her teammates pushes past to double check the post."
    show mei hap at cc
    voice "audio/voice/E2/D1/S2/Mei/2.ogg"
    ms "Of course I'm serious!"
    voice "audio/voice/E2/D1/S2/stu3f/2.ogg"
    stu3f "We're in ninth place!"
    show studentF extra at l3 with dissolve:
        xoffset -200
    voice "audio/voice/E2/D1/S2/stu4f/1.ogg"
    stu4f "That's not bad at all..."
    show mei smi at cc
    voice "audio/voice/E2/D1/S2/Mei/3.ogg"
    ms "Especially considering how long we've actually practiced together."
    voice "audio/voice/E2/D1/S2/stu4f/2.ogg"
    stu4f "That's true."
    show akira smi at r3 with dissolve:
        xzoom -1
    "Akira joins Mei."
    voice "audio/voice/E2/D1/S2/Akira/5.ogg"
    am "Congratulations on your rank, Mei."
    show mei mis at cc
    show note:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D1/S2/Mei/4.ogg"
    ms "Thank you, but I'm sure it means nothing compared to being number one."
    show mei mis b1 at cc with dissolve
    "She flashes him a warm smile and rubs her arm, squeezing her chest together in the process."
    show dots:
        xoffset 1175
        yoffset 5
        xzoom .75
        yzoom .75
    show akira cur at r3
    "Akira falters for a second, then shakes his head and speaks earnestly."
    show akira neu at r3
    voice "audio/voice/E2/D1/S2/Akira/6.ogg"
    am "No, you girls are pretty impressive. You're a new team, right? Formed over the summer?"
    show mei smi b1 at cc
    "Mei nods."
    show akira smi at r3
    voice "audio/voice/E2/D1/S2/Akira/7.ogg"
    am "It's not often that a team who hasn't had much chance to practice and learn from each other is able to make top rank. You have every right to be proud."
    show regBlush:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show mei hap b1 at cc
    voice "audio/voice/E2/D1/S2/Mei/5.ogg"
    ms "Thanks, that means a lot."
    hide akira with dissolve
    show mei smi at cc with dissolve

    voice "audio/voice/E2/D1/S2/stu3f/3.ogg"
    stu3f "I can't believe Akira just said {i}we{/i} impressed him!"
    voice "audio/voice/E2/D1/S2/stu4f/3.ogg"
    stu4f "I know!"
    show studentM extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E2/D1/S2/stu2m/4.ogg"
    stu2m "Do you already have sponsors too?"
    show mei neu at cc
    voice "audio/voice/E2/D1/S2/Mei/6.ogg"
    ms "Not yet--but we aren't worried. We've had a few companies reach out to us today."
    voice "audio/voice/E2/D1/S2/stu2m/5.ogg"
    stu2m "It must be nice to not to worry about sponsorship. I think my team and I will go through the SBA to get a sponsor."
    "SBA? What's that?"
    hide studentM
    hide studentF
    hide studentF2
    with dissolve
    hide mei with dissolve
    "I do a quick search on my phone. {w}A website for a student run association pops up on the school network."
    "..."
    "Ah, it's the Sponsorship Bridging Association, a student association that pairs sponsorship opportunities with different teams. Sounds simple enough."
    "I click on the more information tab."
    "{i}Why should your team get a sponsor? The SBA prides themselves on pairing appropriate sponsors with ACE Academy teams who have proven their ability in battle. {w}These sponsors fund teams for their repair costs as well as provide them with equipment improvements.{/i}"

    "{i}This is a mutual relationship that benefits both the team--through equipment costs and repairs--and the sponsor by giving them greater exposure and an opportunity to advertise through their teams.{/i}"

    "I scan through the rest of their website, looking for the on-campus location. I should stop by and see if they can help us with a sponsor. {w}Instead of the location, I find the student volunteer list and a name pops out at me."
    # lightbulb / idea sfx
    play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
    $ renpy.pause(.75)
    "Yuuna Misaki!"

    "I didn't know she was a part of the SBA. Maybe she'll be willing to help us out."
    "It's a bit loud since those groups of pilots are still talking, so I move to a quiet corner and dial Yuuna's number."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1.0)
    voice "audio/voice/E2/D1/Yuuna/1.ogg"
    ym "Hello?"
    pf "Hi Yuuna, it's [pfirst]."
    voice "audio/voice/E2/D1/Yuuna/2.ogg"
    ym "Oh hi! How are you?"

    menu:
        "I'm fine, how are you?":
            pf "Good. How are you doing?"
            voice "audio/voice/E2/D1/Yuuna/3.ogg"
            ym "Quite well."
            pf "Great!"
            voice "audio/voice/E2/D1/Yuuna/4.ogg"
            ym "... Did you need something?"
            pf "Oh! Yes, I did. {w}I came across the SBA website today and noticed your name on the volunteer list. {w}Are you still a part of that association?"
            voice "audio/voice/E2/D1/Yuuna/5.ogg"
            ym "I am."

        "My day is about to get a whole lot better.":
            pf "I couldn't be better!"
            voice "audio/voice/E2/D1/Yuuna/6.ogg"
            ym "Oh? Why's that?"
            pf "Because I'm talking to my favourite SBA rep."
            voice "audio/voice/E2/D1/Yuuna/7.ogg"
            ym "Oh, thank you!"
            voice "audio/voice/E2/D1/Yuuna/8.ogg"
            ym "Wait, how did you know I'm part of the SBA?"
            pf "I saw your name on the volunteer list online."
            voice "audio/voice/E2/D1/Yuuna/9.ogg"
            ym "Ah, of course."

        "Explain the situation.":
            pf "I'm fine, but I need your help."
            voice "audio/voice/E2/D1/Yuuna/10.ogg"
            ym "Oh? With what?"
            pf "I saw your name on the SBA volunteer list."
            voice "audio/voice/E2/D1/Yuuna/11.ogg"
            ym "Oh!"
            "She seems genuinely surprised."
            pf "You work with them, right?"
            voice "audio/voice/E2/D1/Yuuna/12.ogg"
            ym "Yeah, I do. Sorry, I just wasn't expecting that."

    pf "I was looking to get our team a sponsor but wasn't sure how."
    voice "audio/voice/E2/D1/Yuuna/13.ogg"
    ym "Oh..."
    pf "Then I heard a few students talking about the SBA today and figured I'd check it out. When I saw your name, I just had to ask."
    voice "audio/voice/E2/D1/Yuuna/14.ogg"
    ym "I'd be happy to help you find a sponsor!"
    pf "Really? You don't mind?"
    voice "audio/voice/E2/D1/Yuuna/15.ogg"
    ym "It's no trouble at all! I'll check in with the association in the morning, and I'll be sure to keep you in the loop."
    pf "Thanks, I appreciate it."
    voice "audio/voice/E2/D1/Yuuna/16.ogg"
    ym "Did you need anything else? I don't mean to rush you but I've got to head out."
    pf "No, that's all."
    voice "audio/voice/E2/D1/Yuuna/17.ogg"
    ym "Okay, then I'll talk to you when I have something."
    pf "Great, thanks again for your help."
    voice "audio/voice/E2/D1/Yuuna/18.ogg"
    ym "Anytime. See you around!"
    pf "Yeah, see you."
    stop music fadeout 5
    "The phone clicks as she hangs up. At least we're one step closer to getting a sponsor… {w}I hope."

    $renpy.pause(1)
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(2.5)
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus main dusk with fade
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 1

    "I glance at the time. {w}It's still early in the evening. {w}What should I do?"

    #evening choice 1
    $ freeTime = "evening"
    
    call E2FreeTime from _call_E2FreeTime

    jump E2D1S3
