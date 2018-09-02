#
label E3KIS3:

    $ kaoOut = renpy.random.choice(['comfort'])
    $ kaoHairF = renpy.random.choice(['default'])
    $ kaoHairB = renpy.random.choice(['default'])
    stop ambient fadeout 3
    scene black with fade
    "I grab my keys and head to ACE. {w}After a short drive, I arrive at the Academy."
    play ambient "audio/ambience/Campus.ogg" fadein 3
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    scene bg campus main day with fade
    
    if (E2D5KI_Completed == 1):
        "I recall the building Kaori led me to when she was... not quite feeling herself."
    
    else:
        "I pull up an old team email. After the qualifier, we all had exchanged information in case of an emergency."
        stop ambient fadeout 3
        
    scene bg campus office day with fade
    "I follow a group of girls into the building and am about to join them at the elevator when a voice stops me."
    voice "audio/voice/E3/Free/KI/S3/rec1/1_Receptionist.ogg"
    rec1 "Excuse me, may I help you?"
    show professorF extra at cc with dissolve
    "It's the front desk agent for the dorm. {w}This is an all girls dorm so it makes sense that I'd get stopped."
    
    menu:
        "{color=#00ff00}{b}I'm here to check up on my teammate.{/b}{/color}" if (MCStory == 3):
            jump E3KIS3_IntelJump
    
        "I'm here to check up on my teammate." if (MCStory != 3):
            label E3KIS3_IntelJump:
                pf "Hi, I'm on GEAR team ACE-2049-11. I'm here to meet with my teammate."
                voice "audio/voice/E3/Free/KI/S3/rec1/2_Receptionist.ogg"
                rec1 "Of course, I just need to see your student ID."
                "I provide the proper identification."
    
        "Which is Kaori's room?":
            pf "Hi, I'm trying to meet my friend, Kaori Itami."
            voice "audio/voice/E3/Free/KI/S3/rec1/3_Receptionist.ogg"
            rec1 "Of course, please let me know your visitation purpose and sign this logbook."
            pf "She's my teammate on ACE-2049-11. We are going over some plans."
            voice "audio/voice/E3/Free/KI/S3/rec1/4_Receptionist.ogg"
            rec1 "Of course, student ID please."
            "I provide my student card."
    
        "None of your business.":
            hide professorF with dissolve
            "I ignore her and head towards the elevators."
            voice "audio/voice/E3/Free/KI/S3/rec1/5_Receptionist.ogg"
            rec1 "Excuse me!"
            "Continuing to ignore her, I arrive in front of the lobby. The elevators don't have buttons! They seem to be card activated."
            pf "Damn."
            "With no other choice, I head back to the front desk. The receptionist looks irritated but her professional demeanor pulls through."
            show professorF extra at cc with dissolve
            voice "audio/voice/E3/Free/KI/S3/rec1/6_Receptionist.ogg"
            rec1 "You need a visitors pass. You'll have to explain your reason for visitation and sign the logbook before I can give you one."
            pf "I'm on team ACE-2049-11. I need to see my teammate, Kaori Itami."
            voice "audio/voice/E3/Free/KI/S3/rec1/7_Receptionist.ogg"
            rec1 "ID Please."
            "I provide my student card."
            
    voice "audio/voice/E3/Free/KI/S3/rec1/8_Receptionist.ogg"
    rec1 "Thanks. Just one moment."
    "I fidget as her fingers dance across the keyboard. Can't she type faster?"
    voice "audio/voice/E3/Free/KI/S3/rec1/9_Receptionist.ogg"
    rec1 "Hmm, Ms. Itami hasn't acknowledged the buzzer."
    pf "Her phone died. We were chatting earlier."
    voice "audio/voice/E3/Free/KI/S3/rec1/10_Receptionist.ogg"
    rec1 "Oh! Okay, that makes sense. You're all set then."
    "She hands me a visitors pass."
    voice "audio/voice/E3/Free/KI/S3/rec1/11_Receptionist.ogg"
    rec1 "Just swipe this on the elevator door. It'll guide you to your floor. Room number 45."
    pf "Thanks."
    hide professorF with dissolve
    "That was easy…"
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "I make my way to the elevators and swipe to activate them."
    #Fade to black
    scene black with fade
    "Following the instructions, I easily find room number 45 and knock on the door."
    # sfx knock?
    $renpy.pause(1)
    "..."
    "No answer--"
    #Door opening noise
    "The door flies open."
    scene bg campus dormhallway with fade
    show kaori cur at cc with dissolve
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_93.ogg"
    ki "You...!"
    "Kaori blinks at me in surprise."
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori sur
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_94.ogg"
    ki "What are you doing here?!"
    
    menu:
        "I was worried about you.":
            pf "You called me, didn't leave a message, and then didn't reply when I texted and called you back. I thought something might be up."
            show kaori ske
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_95.ogg"
            ki "Like what?"
            pf "Like something happened..."
            show kaori neu
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_96.ogg"
            ki "I don't follow?"
            "My face turns red. Does she seriously have no idea? This would be very awkward to explain."
            show kaori thi b1
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_97.ogg"
            ki "Nevermind, I don't want to know what you're thinking."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "Her face is red too. I think she finally got it."
            pf "...Anyway..."
    
        "They call me stalker-kun.":
            pf "I got tired of looking into your room with binoculars from the other building and thought I'd pay you a visit instead."
            show kaori thi
            "Kaori rolls her eyes and crosses her arms."
            show storm:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_98.ogg"
            ki "Seriously?"
            show kaori dis
            "Damn, she's getting too used to my sarcasm."
            pf "Well, it might be more to do with your response… or lack thereof."
    
        "Your security here is rubbish.":
            pf "I was right to be worried about you. This place has the security of a hot dog stand."
            show kaori ske
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_99.ogg"
            ki "Why were you worried about me?"
            pf "You didn't answer your phone, which is unlike you."
            show kaori dis
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_100.ogg"
            ki "So you decided to break into my dorm?"
            pf "{i}Break{/i} into? More like {i}casually amble{/i} into."
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "She replies with a stony stare."
    
    pf "Why didn't you respond to any of my calls or messages? Are you okay?"
    show kaori neu
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_101.ogg"
    ki "I'm fine."
    
    # sfx for this?
    "As she replies, I take out my phone and call her number. I hear it ring faintly somewhere in her room."
    
    pf "Your phone seems to be working fine."
    show kaori ske
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_102.ogg"
    ki "Why wouldn't it be?"
    pf "Well, {i}you{/i} called {i}me{/i} first. Then you ignored any of my attempts to call you back. Why would you ignore me unless your phone wasn't working?"
    show kaori thi
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_103.ogg"
    ki "You think too much into things."
    pf "Why did you call me? I think I deserve to know, especially after I came all this way."
    show kaori dis
    "She crosses her arms and frowns."
    stop music fadeout 3
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_104.ogg"
    ki "I didn't ask you to come over here."
    
    #Stomach rumble sound
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    "I'm about to retort when my stomach gurgles."
    
    
    show question:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ske
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_105.ogg"
    ki "What was that?"
    "Uh oh… That would be my breakfast not agreeing with me..."
    pf "Um, I need to use your bathroom."
    show kaori sur
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_106.ogg"
    ki "No way! You're not getting in my room!"
    show kaori ann
    "She tries to close the door on me but I stop her with a foot."
    pf "Seriously! This is an emergency! Trust me, I {i}won't{/i} be able to make it home in time..."
    show kaori ang
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_107.ogg"
    ki "T-That's not my problem!"
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    show kaori ann
    voice "audio/voice/E3/Free/KI/S3/dormf1/1.ogg"
    dormf1 "Kaori! What is it this time--"
    
    "I turn towards the voice behind me. A girl wearing shorts and a tanktop stands in the hallway, her hands on her hips. She freezes when she sees me, and her mouth drops open in horror." 
    "This isn't good. I'm sure all she's seeing is a strange man trying to force his way into Kaori's room."
    pf "Uh. This isn't what it looks like."
    voice "audio/voice/E3/Free/KI/S3/dormf1/2.ogg"
    dormf1 "Kyaah! I'm calling security!"
    # sfx ?
    scene black with Dissolve(0.25)
    "Kaori let's go of the door and I crash onto the floor."
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_108.ogg"
    ki "Wait, Himeki! It's okay! He's one of my piloting teammates."
    voice "audio/voice/E3/Free/KI/S3/dormf1/3.ogg"
    dormf1 "R-Really?"
    "Himeki glares at me."
    voice "audio/voice/E3/Free/KI/S3/dormf1/4.ogg"
    dormf1 "He looks like a pervert to me!"
    pf "Thanks for that."
    scene bg campus kaoriroom day with fade
    "I rub my head as I slowly get back up."
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_109.ogg"
    ki "It's okay. He's just picking something up."
    pf "{size=16}More like dropping something off...{/size}"
    voice "audio/voice/E3/Free/KI/S3/dormf1/5.ogg"
    dormf1 "If you say so... but I'll be here in case he tries something!"
    "Kaori smiles."
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_110.ogg"
    ki "Thanks, but he wouldn't dare."
    "Himeki glares at me one last time before she goes back into her room. Kaori returns to her room and closes the door behind us."
    show kaori dis at cc with dissolve
    stop music fadeout 5
    "Clearly irritated by what happened, she quickly points towards the bathroom."
    show vein:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ann
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_111.ogg"
    ki "Congratulations, you made it in. Now do your thing and leave! I'm {i}not{/i} talking to you!"
    
    menu:
        "Okay, thanks.":
            pf "I'll be quick."
            hide kaori with dissolve
            "I head towards the bathroom."
    
        "Aw, lighten up.":
            pf "I was hoping to have a stimulating conversation about quantum physics from the bathroom, but I guess I can flush that thought down the toilet."
            show kaori dis
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_112.ogg"
            ki "I thought you really had to go?"
            pf "I do."
            hide kaori with dissolve
            "I rush into the bathroom. {w}Kaori has even less of a sense of humour today than usual."
    
        "Go do your business.":
            hide kaori with dissolve
            "Finally! {w}I head straight to the bathroom without saying a word."
    
    
    scene black with fade
    "I shut the door behind me and get comfortable on the porcelain throne."
    "..."
    "Her bathroom is pristine clean. Her items on the sink are neatly lined up and there are no stray items that shouldn't be there."
    "..."
    "Alright, time to get out of here. {w}I reach for the toilet paper and pull off the last sheet! Oh no..."
    "She must have some in the cabinet. I open it up but can't find any extra rolls. The rest of the drawers yield the same result."
    
    pf "Kaori."
    $renpy.pause(1)
    "No answer."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
    pf "...Kaori!"
    "Still no answer. Is she seriously doing this right now?"
    
    label E3KIS3_LoopbackChoice:
    menu:
        "I need TP!":
            pf "You don't have any more toilet paper..."
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_113.ogg"
            ki "Check the cabinet under the sink."
            pf "You don't think that's the first place I'd check given my predicament?"
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_114.ogg"
            ki "Ugh, give me a minute."
            "Why is she so moody? It's not my fault she has no toilet paper."
            "Kaori opens what I assume is a closet door, and a few seconds later, knocks on the bathroom door."
    
        "Fine, I'll just use something else.":
            pf "Well there's no toilet paper here, so I guess I'll just use this towel instead--"
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_115.ogg"
            ki "Don't you {i}dare{/i}!"
            pf "Oh, now she responds."
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_116.ogg"
            ki "This is why I didn't want to let you in. You only cause trouble."
            pf "This towel is so soft and fluffy... Perfect!"
            voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_117.ogg"
            ki "Argh! Stop! just give me a minute."
            "Sufficiently riled, I hear Kaori open what I assume is a closet in the distance. A few seconds pass and then I hear a knock on the door."
    
        "Kaori!" if (E3KIS3_LoopbackChoiceVariable == 0):
            $ E3KIS3_LoopbackChoiceVariable = 1
            "Third time's the charm?"
            pf "Kaori!"
            "..."
            "Guess not."
            jump E3KIS3_LoopbackChoice
            
    stop music fadeout 5
    "I open the door just a crack and Kaori thrusts her hand in. I grab the coveted roll of toilet paper and she disappears. I'm saved!"
   
    "After washing my hands, I exit the bathroom. Kaori sits on her bed, her phone in hand."
    scene bg campus kaoriroom day with fade
    show kaori neu at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    pf "Thanks."
    "She shrugs, her eyes glued to her phone."
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_118.ogg"
    ki "Sure."
    pf "So, that's it then?"
    show kaori ske
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_119.ogg"
    ki "Huh?"
    pf "You won't tell me why you called?"
    show kaori neu
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_120.ogg"
    ki "It's nothing."
    "I sigh."
    pf "Alright. I can tell I'm clearly not needed here. Sorry to bother you."

    if (E3D4S4_ChaseKaori == 0):
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_121.ogg"
        ki "See you."
        hide kaori with dissolve
        scene black with fade
        "As I leave her dorm, I can't get over the feeling that she had something on her mind. Oh well."
        "I'm already out of the house and don't feel like going back to an empty home anyway. {w}I head to the arcade and spend my time beating kids half my age in video games to feel better about myself."
        stop music fadeout 3
        "Once it starts to get dark, I head home."
        jump E3D6S2
    
    else:
        "My hand is on the door when Kaori stops me."
        show kaori cur
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_122.ogg"
        ki "Wait."
        "I pause. She puts down her phone."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_123.ogg"
        ki "Can I ask you something?"
        pf "Sure."
        show kaori thi
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_124.ogg"
        ki "Umm..."
        show dots:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        "She goes quiet and stares at her lap. Did she change her mind…?"
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_125.ogg"
        ki "I'd been looking at different exchange programs and postgraduate opportunities in North America, more specifically in the States."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_126.ogg"
        ki "I was just curious how things are over there…"
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_127.ogg"
        ki "Maybe it'd be worth exploring those options?"
        menu:
            "New adventures!":
                pf "I'd recommend it. Change is always a bit daunting in the beginning, but you end up meeting some amazing people and having invaluable experiences."
                show kaori cur
                "Kaori nods."
                show kaori smi
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_128.ogg"
                ki "I… I see."
    
            "Japan is better for the GEAR industry.":
                pf "If you are strictly thinking about your career growth, I believe Japan has better opportunities."
                show kaori cur
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_129.ogg"
                ki "Really?"
                pf "Yeah, they're still the leaders in Cenorobotics research and technological advancements. Many American pilots come to Japan searching for better opportunities, actually."
                show kaori neu
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_130.ogg"
                ki "Oh, okay."
    
            "It's all the same. Globalization is too prevalent.":
                pf "Culturally, there will be differences, but in terms of GEARs and such, everything is pretty similar."
                pf "Regulations, rules, etc. are all decided at a global level and standardised everywhere."
                show kaori cur
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_131.ogg"
                ki "I suppose that's true."
                pf "Mhm."
                show kaori neu
    
            "I think she has a different question in mind." if (E3D4KI_Embraced == 1):
                stop music fadeout 5
                pf "...That's not what you {i}really{/i} want to talk about. Is it?"
                jump E3KIS3_RomanceJump
                
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_132.ogg"
    ki "Thanks for your input."
    pf "No problem. Was that everything?"
    show kaori thi
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_133.ogg"
    ki "Yeah. Sorry. That's why I called earlier but it seemed like such a trivial thing that I really didn't want to bother you with it."
    pf "This isn't trivial at all. Besides, if there's something on your mind I'm happy to listen. That's the whole point of being friends."
    show kaori smi
    voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_134.ogg"
    ki "Okay."
    
    
    if (E3D4KI_Embraced == 0):
        "She smiles. She seems a lot more relaxed now."
        pf "You're all set then?"
        show note:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_135.ogg"
        ki "Yep, thanks again."
        pf "No problem."
        pf "I'll see you later."
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_136.ogg"
        ki "See you."
        hide kaori with dissolve
        scene black with fade
        "It's still bright out and I don't feel like going home to an empty house. I decide to go to the arcade and practice simulation matches. Talking about our future as pilots, if only briefly, has put me in a productive mood."
        stop music fadeout 3
        "Once it starts to get dark, I head home."
        jump E3D6S2
    
        
    elif (E3D4KI_Embraced == 1):
        stop music fadeout 5
        show kaori neu
        "She looks thoughtfully at me, processing what I just said."
        pf "...Is there something else you wanted to ask me?"
        jump E3KIS3_RomanceJump
    
        
    label E3KIS3_RomanceJump:
        show kaori cur b1
        "Her cheeks turn red and she quickly looks away."
        show kaori thi b1
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_137.ogg"
        ki "Why would you think that?"
        pf "Because I know you, Kaori."
        show kaori cur b1
        "She looks at me with surprise. Then she sighs."
        stop music fadeout 3
        show kaori thi b1
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_138.ogg"
        ki "A-Actually, there is something else."
        pf "What is it?"
        play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
        "She stands up from the bed and walks up to me..."
        show kaori neu b1
        "...A lot closer than I was expecting. The heat flows into my face as she stares straight into my eyes."
        show kaori ner b1
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_139.ogg"
        ki "After the match..."
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_140.ogg"
        ki "When you..."
        show kaori thi b1
        "She looks away, unsure about her words."
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_141.ogg"
        ki "You know..."
        
        menu:
            "That's how I feel about you.":
                pf "Yeah, I know."
        
            "I know what?":
                pf "I don't follow."
                show kaori sad b1
                "She shakes her head."
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_142.ogg"
                ki "Are you really going to make me say it?"
        
            "...":
                "I stay silent, waiting for her to continue."
                show kaori sad b1
                "She looks up at me again with uncertainty in her eyes."
                
        show kaori ner b2 with dissolve
        "Her face is as bright as her hair."
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_143.ogg"
        ki "I, umm...I..."
        show kaori thi b2 with dissolve
        "She struggles to speak, glancing at everything except me."
        "..."
        #stop music fadeout 2
        show kaori win b2 with dissolve
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_144.ogg"
        ki "Anime!"
        pf "What?"
        show drop:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori thi b2
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_145.ogg"
        ki "I-I mean, the new season of {i}Ninja Ranger{/i} is out... so... if you want... we can watch it. I mean, if you're not busy! Actually you're probably busy. Forget I mentioned anything--"
        
        menu:
            "Sounds like fun.":
                pf "Sure, let's watch it."
                show kaori cur b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_146.ogg"
                ki "Oh!"
                show kaori smi b2
                "I didn't know it was possible, but her blush deepens and a small smile graces her lips."
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_147.ogg"
                ki "Umm... okay."
        
            "Netflicks and chill?":
                "I grin at her."
                pf "Are you asking me to Netflicks and chill?"
                show kaori neu b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_148.ogg"
                ki "No, the episodes are downloaded."
                pf "...Right, of course."
                "I sigh. Too bad..."
                
        show kaori smi b2
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_149.ogg"
        ki "Let me just load it up. You can sit here..."
        "She points to the bed. {w}My eyes grow wide. Is she suggesting what I think…?"
        pf "R-Really?"
        show shoBlush:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori sur b3 with dissolve
        "Her expression matches my own when she realises what she's implied."
        voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_150.ogg"
        ki "I-It becomes a couch! The dorm is small."
        show kaori thi b2 with dissolve
        "True to her words, she pulls at a handle and half of the bed folds up into a backrest. I take a seat as she fiddles around on her computer and sets up the connection to her TV."
        #hide kaori with dissolve
        show kaori neu b2
        stop music fadeout 5
        "She starts the first episode, then hesitates before sitting next to me."
        #scene black with fade
        "..."
        #show cg kaori couch 1 with dissolve:
        #    xzoom 0.5
        #    yzoom 0.5
        "We watch the show in silence, but as I sneak discreet glances at her, I catch her sneaking glances at me too."
        
        menu:
            "Time to do the sneaky {i}arm around the chair{/i}.":
                play music "audio/music/You and I (GAME VERSION).ogg" fadein 5
                "I yawn and slowly extend my arm behind her head. Kaori suddenly turns to face me, catching me frozen awkwardly mid-posture."
                show kaori cur b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_151.ogg"
                ki "Are you tired?"
                pf "Uhhh... no, no... I'm just stretching."
                show kaori smi b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_152.ogg"
                ki "Oh, okay."
                "She returns her attention to the TV."
                scene black with fade
                "With her attention diverted, I complete my \"yawn\" by resting my arm around her shoulder."
                $ persistent.gpix[33][0] = 1
                $ persistent.gpix[34][0] = 1
                show cg kaori couch 1 with dissolve:
                    xzoom 0.5
                    yzoom 0.5
                "She tenses once she feels my touch and blinks at me. Her face is a blank mask."
                pf "Uhh…"
                show cg kaori couch 2 with dissolve:
                    xzoom 0.5
                    yzoom 0.5
                "To my surprise, she closes her eyes and leans in closer."
        
            "Be confident and direct.":
                play music "audio/music/You and I (GAME VERSION).ogg" fadein 5
                "I know what those looks mean. Without hesitation, I wrap my arm around her shoulder."
                show kaori cur b2
                "She tenses immediately."
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_153.ogg"
                ki "What do you think you're doing?"
                pf "Shhh... Just let it happen."
                show kaori sur b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_154.ogg"
                ki "H-Hey! You can't just do whatever you please!"
                pf "Stop being such a tsundere all the time, Kaori."
                show kaori ann b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_155.ogg"
                ki "Don't call me a tsundere!"
                pf "Why? It's the truth."
                show kaori ang b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_156.ogg"
                ki "I'm not a tsundere!"
                show kaori ann b2
                pf "That's a very tsundere thing to say."
                "She hits my chest."
                pf "You're really not helping your case."
                show kaori dis b2
                voice "audio/voice/E3/Free/KI/S3/kaori/Date_Kaori_157.ogg"
                ki "Ugh! You're such an idiot."
                "She frowns but I grin."
                pf "If you really want me to stop, just tell me and I will."
                show cg kaori couch 1 with dissolve:
                    xzoom 0.5
                    yzoom 0.5
                ki "..."
                show cg kaori couch 2 with dissolve:
                    xzoom 0.5
                    yzoom 0.5
                "She snuggles closer into me in response."
                    
            "I'm imagining things. Just focus on the show.":
                play music "audio/music/You and I (GAME VERSION).ogg" fadein 5
                show cg kaori couch 1 with dissolve:
                    xzoom 0.5
                    yzoom 0.5                
                "Her glances become more and more frequent and I work hard to ignore them and watch the show."
                show cg kaori couch 2 with dissolve:
                    xzoom 0.5
                    yzoom 0.5
                "!"
                "I feel a gentle presence at my side. It's Kaori. She's staring hard at the TV, but is now leaning into me. {w}Noticing my gaze, she takes my arm and places it around her. I can't stop the smile from spreading on my face."
        
        "I try to focus on the show, but all I can think about is how her chest rises and falls with each breath she takes. {w}I pull her in closer and she eagerly responds by placing a hand on my chest."
        "Her hair tickles my cheek and I catch a whiff of her shampoo. She smells so good, like peaches and summer. {w}I gently brush her hair away. {w}At my touch, she glances up at me and my fingers trace the outline of her cheek."
        "Slowly, we lean towards each other, getting closer and closer… until our lips finally meet. Kaori's kiss is surprisingly gentle. She blushes as we finally pull away but flashes me a small smile."
        
        
        #black screen
        scene black with fade
        stop music fadeout 5
        
        "We run through the entire season of {i}Ninja Ranger{/i} before we realise how late it is. {w}After saying goodbye, I head home."
        
        $ E3KIS3_Completed = 1
        
        jump E3D6S2