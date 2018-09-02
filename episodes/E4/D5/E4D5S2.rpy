#
label E4D5S2:
    
    $ yukOut = renpy.random.choice(['sweater'])
    $ kaiOut = renpy.random.choice(['sCasual'])
    stop ambient fadeout 3
    scene black with fade
    #play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    
    "When I arrive home, Yuki is rummaging through the drawers in the living room. She glances at me and grins."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show yuki hap at cc with dissolve
    voice "audio/voice/E4/Yuuki/E4/D5/1.ogg"
    hy "Oh good! You're here! Where are your rubber bands?"
    pf "Huh?"
    show yuki cur
    show exclamation:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Yuuki/E4/D5/2.ogg"
    hy "Rubber bands! I need them."
    pf "Why?"
    show yuki smi
    "She just smiles."
    voice "audio/voice/E4/Yuuki/E4/D5/3.ogg"
    hy "Do you know where they are?"
    pf "Yeah, they're in the bottom drawer of the table beneath the mirror."
    "Yuki searches through the drawer and pulls out a rubber band."
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D5/4.ogg"
    hy "Thanks!"
    hide yuki with dissolve
    "I watch her curiously as she wanders into the kitchen. She ties the rubber band around the nozzle sprayer next to the faucet."
    "Afterwards, she grabs Uncle Kaito's phone, which was lying unattended on the kitchen table. I peek over her shoulder and watch her change his lockscreen to a screenshot of his home screen."
    "Then she puts the phone back down."
    "I follow her back into the living room where she takes a seat on the couch and flips through a magazine as if nothing just happened."
    pf "What's going on?"
    show yuki smi at cc with dissolve
    voice "audio/voice/E4/Yuuki/E4/D5/5.ogg"
    hy "As soon as Kaito comes out I want you to block your number and call his phone."
    pf "Why?"
    show yuki mis
    voice "audio/voice/E4/Yuuki/E4/D5/6.ogg"
    hy "Just do it! It'll be worth it."
    "I shrug and join her on the couch."
    pf "If you say so."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    "We didn't have to wait long before Kaito emerges from the back room. I do as Aunt Yuki asks and immediately call his phone. Yuki watches me closely as I do, then grins."
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D5/7.ogg"
    hy "Kaito, are you going into the kitchen? Do you mind getting me a glass of water?"
    voice "audio/voice/E4/Kaito/d05/(2).ogg"
    hk "No problem."
    show heart:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Yuuki/E4/D5/8.ogg"
    hy "Thank you!"
    hide yuki with dissolve
    "As soon as Kaito walks through the kitchen door, Yuki and I bolt off of the couch and creep in the doorway to watch what unfolds."
    "Kaito picks up an empty glass in one hand and his phone in the other. He puts the glass down beside the sink as he focuses on his phone. When he turns on the faucet, the rubber band forces the water to spray out of the nozzle and it catches Kaito all over his chest."
    "He yelps in surprise and quickly shuts off the water, then tries desperately to swipe his phone."
    show yuki hap at l2 with dissolve
    "Aunt Yuki and I can't hold back our laughter and fall into a fit of giggles by the door. Uncle Kaito looks increasingly worried as he can't get his phone to work."
    show kaito dis at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E4/Kaito/d05/(3).ogg"
    hk "Yuki! This isn't funny! I think you damaged my phone!"
    "She's too busy laughing to answer."
    show kaito ann
    voice "audio/voice/E4/Kaito/d05/(4).ogg"
    hk "I need this for work! This is serious."
    show yuki smi
    "Finally, Yuki composes herself."
    voice "audio/voice/E4/Yuuki/E4/D5/9.ogg"
    hy "Relax, your phone is fine."
    show kaito dis
    voice "audio/voice/E4/Kaito/d05/(5).ogg"
    hk "Clearly, it's not! It's frozen."
    voice "audio/voice/E4/Yuuki/E4/D5/10.ogg"
    hy "No, it's not. Give it here."
    show kaito ske
    "She plucks the phone out of his hand and unlocks it. He furrows his brow in confusion."
    show yuki mis
    voice "audio/voice/E4/Yuuki/E4/D5/11.ogg"
    hy "I just changed your wallpaper. Funny, right?"
    show confused:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito ner
    "I can't help but laugh at the expression on Kaito's face. It's relief plus irritation plus confusion rolled into one. My laugh makes Yuki want to laugh, although she tries her best to keep a straight face in front of Kaito."
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D5/12.ogg"
    hy "Oh, Kaito! Your face!"
    show kaito mis
    "She breaks down into laughter. Soon, even Kaito cracks a smile at the both of us."
    show drop:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d05/(6).ogg"
    hk "One day, Yuki, you are going to give me a heart attack."
    show yuki sur
    voice "audio/voice/E4/Yuuki/E4/D5/13.ogg"
    hy "Don't say things like that!"
    show kaito wor
    "I slowly compose myself and Kaito glances at me."
    show yuki smi
    voice "audio/voice/E4/Kaito/d05/(7).ogg"
    hk "You were in on this too? I thought you were on my side!"
    pf "Sorry, but Yuki's the fun one."
    show yuki smi
    "She smiles and gives me a hug."
    show kaito mis
    voice "audio/voice/E4/Kaito/d05/(8).ogg"
    hk "Alright, fun one. Since this was all your fault to begin with, you should be the one to clean up the kitchen."
    voice "audio/voice/E4/Yuuki/E4/D5/14.ogg"
    hy "Fair enough."
    hide yuki with dissolve
    "Yuki goes to grab some towels while Uncle Kaito and I head into the living room."
    stop music fadeout 4
    "I should tell him about what I learned at Aludian."
    pf "Uncle Kaito, I need to tell you something. It involves my Dad."
    show kaito neu
    "His smile drops."
    voice "audio/voice/E4/Kaito/d05/(9).ogg"
    hk "What is it?"
    pf "Yesterday, during my match with Akira's team, Akira's GEAR went into overdrive mode."
    show kaito ner
    voice "audio/voice/E4/Kaito/d05/(10).ogg"
    hk "The same overdrive mode your core can do?"
    pf "Yeah. I confronted Aludian about it this afternoon and they told me that Midori Energy was the one who supplied them with the technology."
    show dots:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    "Uncle Kaito looks grave."
    voice "audio/voice/E4/Kaito/d05/(11).ogg"
    hk "That was your father's company."
    pf "Exactly…"
    show kaito thi
    voice "audio/voice/E4/Kaito/d05/(12).ogg"
    hk "Was this technology a research project he was working on for the company?"
    pf "I don't know. He never mentioned anything to me about it when we were building Eagle. When I discovered Eagle had this ability, I assumed it was something Dad had created just for me… but now I'm not so sure."
    show kaito neu
    "Kaito nods."
    voice "audio/voice/E4/Kaito/d05/(13).ogg"
    hk "I'll have the PI investigate Midori Energy and see if there are any connections."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    "Before I can respond, Aunt Yuki returns to the living room."
    show yuki smi at l2 with dissolve
    voice "audio/voice/E4/Yuuki/E4/D5/15.ogg"
    hy "How about a little TV time with my two favourite boys?"
    pf "I'm up for that."
    show kaito smi
    voice "audio/voice/E4/Kaito/d05/(14).ogg"
    hk "Same here."
    pf "Is Nikki home?"
    voice "audio/voice/E4/Kaito/d05/(1).ogg"
    hk "Not yet."
    voice "audio/voice/E4/Yuuki/E4/D5/16.ogg"
    hy "She's such a busy bee. She can join us when she comes back."
    #
    hide kaito
    hide yuki
    with dissolve
    "We throw in a movie and Uncle Kaito and Aunt Yuki add their own commentary to what's going on. Normally, it would be annoying, but I'm just happy to see that they're getting along so well again."
    scene black with fade
    "Eventually, Nikki comes home and snuggles between Kaito and Yuki on the couch. For the first time in a while, I feel like I'm part of a family again. It's not just Nikki and me anymore. {w}Judging by Nikki's smiles, I think she feels the same way."
    stop ambient fadeout 3
    stop music fadeout 3
    "We watch until the late hours in the night, then I say my goodnights and go to bed. It's not long before I've drifted off to sleep."
    $ renpy.pause(3.25)
    
    ### DAY 6 START
    
    if E4KIS1_Completed == 1 and E4KIS2_Completed == 1 and kaorelatonship == 1:
        jump E4KIS3
        
    elif E4MAS1_Completed == 1 and E4MAS2_Completed == 1 and mayrelatonship == 1:
        jump E4MAS3
        
    elif E4VBS1_Completed == 1 and E4VBS3_Completed == 1 and valrelatonship == 1:
        jump E4VBS4
        
    elif E4YMS1_Completed == 1 and E4YMS2_Completed == 1 and yuurelatonship == 1:
        jump E4YMS3
    #
    #
    elif E3SSS3_Completed == 1 and E4SSS1_Completed == 1 and E4SSS2_Completed == 1:
        play ambient "audio/ambience/Morning.ogg" fadein 3
        $renpy.pause(1)
        scene bg homekaito myroom day with fade
        "I wake up with a yawn and stretch."
        "After going through my morning ritual, I decide what I want to do."
        
        menu:
            "Hang out with Shou.":
                jump E4SSS3
            
            "I wonder what Nikki's up to.":
                jump E4SFS1
    
    else:
        jump E4SFS1
        
    jump E4D7S1
