label E1D2S6:
    
    
    
    "I extend my hand toward her, but she swats it away."
    scene cg kaori intersection fall4 at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E1/D2/S6/Kaori/1.ogg"
    ki "Don't touch me!"
    
    "She takes several deep breaths, then heaves herself unsteadily to her feet."
    scene bg campus intersection day with fade
    "Once she finds her footing, she dusts off her uniform. {w}Suddenly, she whirls on me." 
    show kaori ang at cc with dissolve
    voice "audio/voice/E1/D2/S6/Kaori/2.ogg"
    ki "Are you blind?! You could have killed me!"
    
    pf "I'm really--"
    voice "audio/voice/E1/D2/S6/Kaori/3.ogg"
    ki "What were you thinking?! I swear, these days, any idiot can get a license."
    show kaori ann at cc with dissolve
    "She gestures to her books strewn across the road."
    show vein:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ang at cc
    voice "audio/voice/E1/D2/S6/Kaori/4.ogg"
    ki "Look! Look at what you've done!"
    
    "It's not a pretty sight."
    show kaori ann at cc with dissolve
    "She runs her hands through her hair in growing frustration. Whenever I try to apologise, she interrupts me with another verbal beating."
    
    "She's a fiery one, that's for sure."
    
    menu:
        "Apologise and offer to help gather her things.":
            "I don't deserve this barrage of insults, but I can understand her anger and frustration. {w}I admit I'm in the wrong, so I'll bite my tongue and take the abuse." 
    
            "She takes a breath and stoops to pick up her things. It'll take forever for her to gather all of this stuff by herself. {w}I wheel my bike to the side of the road and try to help her, but whenever I pick something up she snatches it out of my hands."
    
            "I need to get her attention so I can make things right. I pick up a book, and before she can snatch it back, I offer it to her."
            show kaori ske at cc
            voice "audio/voice/E1/D2/S6/Kaori/5.ogg"
            ki "Huh? Wha..."
    
            "Her gaze flicks back and forth from me to the book, her eyes narrowing the longer she does so."
            show kaori ann at cc
            voice "audio/voice/E1/D2/S6/Kaori/6.ogg"
            ki "Why are you still here? Haven't you caused enough trouble?"
    
            "She steals the book out of my hands."
    
            pf "Look, I'm really sorry."
            show kaori dis at cc
            "She folds her arms, the fire easing in her eyes."
    
            pf "So, can I help you?"
    
            "She shrugs, and drops the book I returned back into her bag."
            show kaori thi b1 at cc with dissolve
            voice "audio/voice/E1/D2/S6/Kaori/7.ogg"
            ki "Whatever. Do what you want."
    
            "I think that's her way of saying \"yes\"."
    
            "I jump right into gathering her fallen items. It's not long before we're done."
            show kaori neu at cc with dissolve
            "She checks her bag."
            voice "audio/voice/E1/D2/S6/Kaori/8.ogg"
            ki "That looks like everything."
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            show kaori thi at cc with dissolve
            $renpy.pause(1)
            "An uncomfortable silence falls between us. {w}She gazes down at her feet for a moment." 
    
            "The previous hostility is gone. I mean, she still looks annoyed, but not in the \"I'm about to bludgeon you to death with my books and dump your body in the sewer\" kind of way."
            show kaori dis at cc
            voice "audio/voice/E1/D2/S6/Kaori/9.ogg"
            ki "Thanks... I guess. Even if this was all your fault to begin with."
    
            "I rub the back of my head with a sheepish grin."
    
            pf "No problem. And again, I really am sorry for all of this."
            show kaori ann at cc
            voice "audio/voice/E1/D2/S6/Kaori/10.ogg"
            ki "Whatever. I'm going to be late if I stand around chatting to an idiot like you all day. Bye."
            hide kaori with dissolve
            "She shoulders past me and marches away at a brisk pace. I soon lose her as she turns the corner."
    
            "Well that was… something."
            play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
            "I head back to my bike, confident that I did the right thing."
            
            stop music fadeout 3
            
            $ E1D2S3_MetKaoriWasNice = 1
            
            jump E1D2S7
    
        "Help her quickly so I don't lose too much time.":
            "{i}Someone's{/i} got an attitude problem, but I'd be a complete jerk if I just left now."
    
            "I sigh. Let's get this over with so I can get to the academy on time."
    
            "I reluctantly wheel my bike to the side, and begin to gather her fallen items. Thankfully, there isn't much, so it shouldn't take long..."
            show kaori ske at cc with dissolve
            "She yanks the items out of my hands."
    
            "... Or maybe it will."
            show kaori ang at cc
            voice "audio/voice/E1/D2/S6/Kaori/11.ogg"
            ki "What are you doing?! I didn't ask for your help!"
            show kaori ann at cc
            "And the ringing in the my eardrums is back. {w}Wincing, I tilt my head away from her, and hope that my ears aren't bleeding."
    
            pf "Yeesh. Shouldn't you be thankful I'm taking the time to help you? We'll be done in seconds if you let me help. Come on."
            show kaori ang at cc with dissolve
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S6/Kaori/12.ogg"
            ki "No! Just leave it!"
            
            "I'm going to be here all day if I argue with her. I step around her and grab her bag off the ground. Trying my best to ignore her verbal barrage of complaints and insults, I collect the remaining items."
            show kaori ann at cc with dissolve
            "I try to hand back her bag, but she snatches it out of my hands."
    
            "A \"thank you\" would be nice."
    
            pf "See? All there, and that took no time at all."
            show kaori dis at cc
            "She rummages inside her bag, ruining my neat packing job. Does she think I might have tried to steal something? I'm not {i}that{/i} bad."
    
            "Content, she closes the bag back up and gives me a dull look. At least she's visibly less angry than before."
            voice "audio/voice/E1/D2/S6/Kaori/13.ogg"
            ki "... Fine."
            hide kaori with dissolve
            "Without another word, she turns on her heel and heads in the direction of the academy."
    
            pf "... Still waiting on that \"thank you\"."
    
            "I trek back to my bike, feeling just a little bit more deaf than before."
            
            stop music fadeout 3
            
            $ E1D2S3_MetKaoriWasNice = 1
            
            jump E1D2S7
    
        "Whatever, I'm out.":
            $ E1D2S3_MetKaoriWasRudeNoHelmet = 1
            
            "This is going nowhere. She isn't injured, so I don't have any problem with leaving."
    
            if (E1D2S3_mcwithhelmet == 0):
                play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
                "I start up my bike and sail past her, regretting ever stopping for someone as crazy as her in the first place."
                stop ambient fadeout 3
                play ambient "audio/ambience/Open Road No Helmet.ogg" fadein 1
    
            if (E1D2S3_mcwithhelmet == 1):
                play sound "audio/sfx/Vehicles/Bike Ignition.ogg"
                "I put my helmet back on and start the bike."
                play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 5 fadeout 5
                "As I make my way past her, I think I hear muffled shouting behind me. I'm too far to make out what she says, which is probably for the best."
                stop ambient fadeout 3
                play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
    
    scene black with fade
    jump E1D2S7
