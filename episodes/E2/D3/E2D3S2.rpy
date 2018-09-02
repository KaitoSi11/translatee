#
label E2D3S2:
    
    #Afternoon choice end
    
    $ yuuOut = "sUniform"
    
    stop ambient fadeout 3
    scene black with fade
    scene bg campus library day with fade
    show yuuna neu at cc with dissolve
    "Yuuna is already waiting for me at the library. A tablet with the SBA logo is clutched in her hand. {w}She smiles and breathes a sigh of relief when she sees me."
    show yuuna smi at cc
    voice "audio/voice/E2/D3/Yuuna/1.ogg"
    ym "Oh good, you're still wearing your uniform. I forgot to tell you yesterday to wear it and remembered too late to text you."
    "Oh… I was so preoccupied on what I would say today that I forgot to think about what I'd wear."
    pf "No worries."
    "I hope my voice sounds more confident than I feel."
    
    ### NOTE Points - "IF medium or high points with Yuuna:"
    # temporarily set to 0
    if yuuromance > 0:
        show yuuna cur at cc
        "Yuuna notices the waver in my voice. She places a hand on my shoulder."
        "The heat of her hand soothes my nerves and I relax a little bit."
    
    else:
        show yuuna ner at cc
        "Yuuna shifts uneasily from one foot to the other."
    
    show yuuna neu at cc
    voice "audio/voice/E2/D3/Yuuna/2.ogg"
    ym "Okay, well, are you ready to go?"
    pf "Yeah."
    "She starts towards the bus stop, when I stop her."
    pf "I can drive us."
    
    if E1D5S3_HelpedYuuna == 1:
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna smi b1 at cc with dissolve
        "Her cheeks turn pink but she grins widely. I'm immediately reminded of how her face lit up the last time she saw my bike."
        show yuuna hap b1 at cc
        voice "audio/voice/E2/D3/Yuuna/3.ogg"
        ym "That would be great."
        "I lead her to my bike, and we both hop on with ease."
    
    else:
        show yuuna cur at cc
        voice "audio/voice/E2/D3/Yuuna/4.ogg"
        ym "Are you sure?"
        pf "Yeah, let's go."
        hide yuuna with dissolve
        scene bg campus parking day with dissolve
        "She follows me into the parking lot and to my bike. Without a second thought, I hop on, but Yuuna hesitates."
        show yuuna ner at cc with dissolve
        pf "What's wrong?"
        voice "audio/voice/E2/D3/Yuuna/5.ogg"
        ym "Oh, nothing, I just didn't know you had a motorcycle and not a car."
        hide yuuna with dissolve
        "She gingerly slides onto the bike."
    
    stop music fadeout 3
    scene black with fade
    # bike sfx
    stop ambient fadeout 3
    "Once she's settled, we speed off. Yuuna directs me where to go, and eventually tells me to park in front of an impressive building. It's narrow, but shoots straight into the sky, cutting through the clouds."
    play ambient "audio/ambience/Campus Office.ogg" fadein 1
    scene bg campus office day with fade
    "As we walk in, a perky receptionist greets us from behind her desk."
    # do we have a female receptionist sprite?
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 2
    show professorF extra at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E2/D3/S2/rc3f/1.ogg"
    rc3f "Welcome to Warptech Corporation! How may I help you?"
    show yuuna neu at l2 with dissolve
    "Yuuna steps forward."
    show yuuna smi at l2
    voice "audio/voice/E2/D3/Yuuna/6.ogg"
    ym "I'm Yuuna Misaki from Ace Academy's SBA. We have an appointment with Mr. Takeda."
    "The receptionist smiles and gestures to the empty chairs."
    voice "audio/voice/E2/D3/S2/rc3f/2.ogg"
    rc3f "Of course. If you'll please take a seat, he'll be with you shortly."
    hide professorF with dissolve
    show yuuna neu at cc with dissolve
    "As soon as we take our seats, the receptionist types a rapid sequence into her computer, then drags the document from her monitor onto her tablet and disappears into a hall in the back."
    "I glance at Yuuna. She's meticulously going over her notes."
    pf "Are you nervous?"
    show dots:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna thi at cc
    "She thinks for a minute."
    show yuuna neu at cc
    voice "audio/voice/E2/D3/Yuuna/7.ogg"
    ym "Not as much as I thought I'd be. Are you?"
    
    menu:
        "I'm either really nervous or really hungry.":
            pf "My stomach is in knots."
            show yuuna hap at cc
            "Yuuna smiles encouragingly."
            voice "audio/voice/E2/D3/Yuuna/8.ogg"
            ym "Don't worry, you'll do great."
            "Her confidence helps ease my nerves, and I smile back."
            pf "I'm glad I have you here with me."
            show regBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna smi b1 at cc with dissolve
            "A blush creeps into her cheeks, but she seems pleased."
        
        "Nobody can resist these pearly whites.":
            pf "Nah, I've got my secret weapon."
            show yuuna cur at cc
            voice "audio/voice/E2/D3/Yuuna/9.ogg"
            ym "What's that?"
            "I flash her a smile."
            pf "One look at me and she'll be hooked."
            show yuuna smi at cc
            voice "audio/voice/E2/D3/Yuuna/10.ogg"
            ym "We're meeting with a man."
            "I freeze as I run the scenario in my head."
            pf "Uh… It could still work..."
            show note:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna hap b1 at cc with dissolve
            "Yuuna chuckles."
        
        "Nerves are like feelings, they don't exist.":
            pf "No. There's no point in being nervous."
            show yuuna thi at cc
            voice "audio/voice/E2/D3/Yuuna/11.ogg"
            ym "I guess not, but it's not something that's easy to control."
            pf "Perhaps that's true for some, but not me."
            show yuuna ske at cc
            "She glances skeptically at me."
    
    scene black with dissolve
    # well I guess the female receptionist sprite is going to have a ponytail?
    stop music fadeout 2
    "The receptionist comes back and gestures for us to follow her. Her ponytail bounces behind her as she walks briskly down the hall and directs us into a spacious office."
    stop ambient fadeout 5
    scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    # the visuals of the cg don't align very well with what's written here. the man doesn't look any older than Kaito, isn't portly, and the desk isnt old fashioned mahogany
    "A portly, older man sits behind an old fashioned mahogany desk. His jowls wiggle as he offers us seats, which we both take. The walls are painted white, but one wall has a translucent sheen with Yuuna's SBA submission packet projected on it."
    scene cg takeda office sorry at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "His chair squeaks in protest as he leans forward to greet us."
    show note:
        xoffset 600
        yoffset 50
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D3/S2/pres1m/1.ogg"
    pres1m "Ms. Misaki, it's a pleasure to see you again."
    voice "audio/voice/E2/D3/Yuuna/12.ogg"
    ym "Thank you for agreeing to meet with us, Mr. Takeda. I'd like to introduce my associate."
    pf "I'm [pfull]. It's nice to meet you."
    scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    "He nods in acknowledgement while Yuuna continues."
    voice "audio/voice/E2/D3/Yuuna/13.ogg"
    ym "He is here to represent his team at ACE Academy."
    scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 15
    voice "audio/voice/E2/D3/S2/pres1m/2.ogg"
    pres1m "And you are in need of a sponsor."
    pf "Yes, sir."
    "He waves a hand towards the wall and shuffles the data on there."
    scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E2/D3/S2/pres1m/3.ogg"
    pres1m "As you can see, Ms. Misaki did a detailed job of describing you and your team in your application, but I'd like to hear it from you. Tell me about yourself."
    
    $ E2D3S2_Score = 0
    menu:
        "I've always had an interest in GEAR." if MCStory != 3:
            #good choice
            $ E2D3S2_Score += 3
            pf "I grew up in the world of GEARs and knew from an early age that I wanted to be a pilot. While a student at CINY, I began my program in piloting and earned top marks in all of my classes. I recently transferred and tested into the Pilot Program at ACE Academy, where I'm pursuing my degree in Piloting."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/4.ogg"
            pres1m "As a transfer student, that's not an easy program to test into."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "He sounds impressed."
        
        "{b}I've always had an interest in GEAR.{/b}" if MCStory == 3:
            #good choice
            $ E2D3S2_Score += 3
            pf "I grew up in the world of GEARs and knew from an early age that I wanted to be a pilot. While a student at CINY, I began my program in piloting and earned top marks in all of my classes. I recently transferred and tested into the Pilot Program at ACE Academy where I'm pursuing my degree in Piloting."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/4.ogg"
            pres1m "As a transfer student, that's not an easy program to test into."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "He sounds impressed."
        
        "I like long walks on the beach...":
            #bad choice
            $ E2D3S2_Score += 1
            pf "Well, of course I'm interested in Cenorobotics and becoming a pilot, but I'm more than just a mech guy. I like deep conversations over coffee and good food with good company. I'm also a Gemini, which makes me a bit unpredictable. Some people think Geminis have more than one personality."
            "I laugh nervously under Mr. Takeda's stoic gaze."
            show drop:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D3/S2/pres1m/5.ogg"
            pres1m "Hm. Thank you, that was very… enlightening."
            pf "Do you need more? I can keep going."
            scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/6.ogg"
            pres1m "That won't be necessary."
        
        "What's there to tell?":
            #medium choice
            $ E2D3S2_Score += 2
            pf "I'm in the Pilot Program at ACE Academy, as are my teammates. We need a sponsor to help us compete in the intercollegiate tournament, and that's why we're here."
            voice "audio/voice/E2/D3/S2/pres1m/7.ogg"
            pres1m "Hm, of course."
            "Yuuna leans in and whispers to me."
            voice "audio/voice/E2/D3/Yuuna/14.ogg"
            ym "I think he wanted you to share something about yourself that he didn't already know. He wants you to show him why you're the best choice."
            show dots:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "I nod at Yuuna before looking back at Mr. Takeda. {w}He waits patiently."
            pf "...{w}I was a pilot at CINY before transferring to Ace Academy."
            voice "audio/voice/E2/D3/S2/pres1m/8.ogg"
            pres1m "Interesting."
    
    scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E2/D3/S2/pres1m/9.ogg"
    pres1m "Tell me, out of all your other options, why did you choose Warptech Corporation?"
    
    menu:
        "You're the best around." if MCStory != 3:
            #Nothing's gonna ever keep you down
            #good choice
            $ E2D3S2_Score += 3
            pf "It was an easy decision. Warptech Corporation sets the standard for GEAR weaponry. I read about your latest announcement of the advancement in particle technology. Same output on beam weaponry while reducing core usage by 15 percent. None of your competitors have made a breakthrough like that yet."
            voice "audio/voice/E2/D3/S2/pres1m/10.ogg"
            pres1m "There has also been some controversy over that release."
            pf "Some are saying using the new technology will affect the longevity of a weapon, but there's no proof of that yet. I'd prefer to see evidence than believe rumors."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "He nods."
            if E2D3S2_Score >= 6:
                scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/11.ogg"
            pres1m "It's refreshing to see a young person keeping up to date with the latest releases."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "I think I detect a hint of approval in his voice."
        
        "{b}You're the best around.{/b}" if MCStory == 3:
            #Nothing's gonna ever keep you down
            #good choice
            $ E2D3S2_Score += 3
            pf "It was an easy decision. Warptech Corporation sets the standard for GEAR weaponry. I read about your latest announcement of the advancement in particle technology. Same output on beam weaponry while reducing core usage by 15 percent. None of your competitors have made a breakthrough like that yet."
            voice "audio/voice/E2/D3/S2/pres1m/10.ogg"
            pres1m "There has also been some controversy over that release."
            pf "Some are saying using the new technology will affect the longevity of a weapon, but there's no proof of that yet. I'd prefer to see evidence than believe rumors."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "He nods."
            if E2D3S2_Score >= 6:
                scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/11.ogg"
            pres1m "It's refreshing to see a young person keeping up to date with the latest releases."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "I think I detect a hint of approval in his voice."
        
        "Money, money, money… money!":
            #bad choice
            $ E2D3S2_Score += 1
            pf "It's safe to say your company is doing very well financially. That financial security is just what we need to improve our GEARs. {w}Plus, as top dog in your field, you guys come up with awesome new weapons. It'd be so cool to test those out before they're released to the public."
            show dots:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "Mr. Takeda wears his best poker face, and I can't detect any sort of emotion in him."
            scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/12.ogg"
            pres1m "I see."
            "Out of the corner of my eye, I think I see the ghost of a frown on Yuuna's face."
        
        "I didn't.":
            #medium choice
            $ E2D3S2_Score += 2
            pf "Well, actually, it was Yuuna who decided."
            "Yuuna stares blankly at me, but she smiles when Mr. Takeda glances at her."
            voice "audio/voice/E2/D3/Yuuna/15.ogg"
            ym "Warptech Corporation is a leader and innovator when it comes to GEAR weaponry. A team under your sponsorship would benefit greatly from your knowledge and expertise."
            "He nods, seemingly satisfied."
            
    scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E2/D3/S2/pres1m/13.ogg"
    pres1m "Okay, and why should Warptech Corporation choose you? In other words, what sets you apart from the competition?"
    
    menu:
        "We're a breath of fresh air." if MCStory != 3:
            #good choice
            $ E2D3S2_Score += 3
            pf "As a new team, we aren't so set in our ways that we stifle creativity. We're not afraid to try new strategies we think will benefit the team, and we're receptive to feedback."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            pf "That said, we're also acutely aware of our abilities. We work well together because we are upfront with each other not only about our strengths, but also about our weaknesses, and we use that knowledge to our advantage."
            if E2D3S2_Score >= 7:
                scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "I sneak a peek at Yuuna, who looks pleased."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "Mr. Takeda seems to appreciate my answer as well."
        
        "{b}We're a breath of fresh air.{/b}" if MCStory == 3:
            #good choice
            $ E2D3S2_Score += 3
            pf "As a new team, we aren't so set in our ways that we stifle creativity. We're not afraid to try new strategies we think will benefit the team, and we're receptive to feedback."
            scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            pf "That said, we're also acutely aware of our abilities. We work well together because we are upfront with each other not only about our strengths, but also about our weaknesses, and we use that knowledge to our advantage."
            if E2D3S2_Score >= 7:
                scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "I sneak a peek at Yuuna, who looks pleased."
            show note:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "Mr. Takeda seems to appreciate my answer as well."
        
        "My team is half women.":
            #bad choice
            $ E2D3S2_Score += 1
            pf "We've got women."
            "There's a pause while Mr. Takeda waits for me to elaborate."
            scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            show drop:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D3/S2/pres1m/14.ogg"
            pres1m "And?"
            pf "They're good to fight with {i}and{/i} good to look at. It's basically a win-win, am I right?"
            if E2D3S2_Score <= 5:
                scene cg takeda office annoyed at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            "I give Mr. Takeda a knowing wink and a friendly nudge."
            show storm:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            "He seems unimpressed. {w}Weird. Shou would get what I'm saying."
        
        "I'm international.":
            #medium choice
            $ E2D3S2_Score += 2
            pf "As someone who grew up overseas, I bring a new point of view to my Japanese teammates. If you invest in us, you'll be investing in international alliances."
            show question:
                xoffset 600
                yoffset 50
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D3/S2/pres1m/15.ogg"
            pres1m "But couldn't the same be said for any of the other international pilots studying at ACE?"
            "Uh…"
            scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
            voice "audio/voice/E2/D3/S2/pres1m/16.ogg"
            pres1m "And there is, of course, the potential backlash if we support an \"international pilot\" over a full team of domestic pilots."
            "Perhaps that wasn't the best angle to use..."
    
    scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
    voice "audio/voice/E2/D3/S2/pres1m/17.ogg"
    pres1m "Well, I think I've heard enough for now. Ms. Misaki, do you have a copy of your team's qualifier transcript?"
    voice "audio/voice/E2/D3/Yuuna/16.ogg"
    ym "Yes, of course."
    "She flips on her tablet and flicks a document onto the projected wall."
    
    
    if E2D3S2_Score >= 7:
        scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "The interview seems to be going well. I glance at Yuuna, who smiles encouragingly at me."
        scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "Mr. Takeda takes a quick glance at the file and frowns."
        scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        show question:
            xoffset 600
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D3/S2/pres1m/18.ogg"
        pres1m "Your team is only ranked 21?"
        pf "Yes, sir."
        scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "He sighs and turns off the projection."
        scene cg takeda office sorry at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/S2/pres1m/19.ogg"
        pres1m "You seem generally passionate about your team and your studies, and perhaps if the circumstances were different we would consider your candidacy. Unfortunately, Warptech only accepts teams who are ranked within the top ten from ACE Academy."
        scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        "As I'm still processing the rejection, Yuuna protests on my behalf."
        scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/Yuuna/17.ogg"
        ym "Mr. Takeda, couldn't you make an exception?"
        voice "audio/voice/E2/D3/Yuuna/18.ogg"
        ym "You said yourself that if rank weren't a factor his team would be a strong candidate. A representation by you would make a significant difference in their growth and development, and their success reflects positively on you and your company."
        scene cg takeda office sorry at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/S2/pres1m/20.ogg"
        pres1m "I'm sorry, Ms. Misaki."
        voice "audio/voice/E2/D3/S2/pres1m/21.ogg"
        pres1m "I do believe with skills like his he will find a sponsor. Just not with us."
        scene cg takeda office smile at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        stop music fadeout 5
        voice "audio/voice/E2/D3/Yuuna/19.ogg"
        ym "Won't you even give him a chance?"
        scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/S2/pres1m/22.ogg"
        pres1m "Ms. Misaki, I'm sure you understand the image that we have built and what would happen to that image if we stopped recruiting from the top ten."
        voice "audio/voice/E2/D3/S2/pres1m/23.ogg"
        pres1m "I thank you very much for your interest in us, and wish you the best of luck in your future endeavors."
        "His voice has a hard edge of finality. He gestures towards the door, then returns his attention to his desk."
    
    else:
        "Yuuna tries to still her jittering leg as she carefully watches Mr. Takeda. He quickly glances at the file, then bursts into a deep laugh that shakes his belly."
        scene cg takeda office happy at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        show vein:
            xoffset 600
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D3/S2/pres1m/24.ogg"
        pres1m "Is this a joke?"
        "Yuuna and I share a glance."
        scene cg takeda office neutral at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/Yuuna/20.ogg"
        ym "I don't understand."
        scene cg takeda office frown at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/S2/pres1m/25.ogg"
        pres1m "As per our history with ACE Academy, Warptech only accepts the most talented pilots. That means teams in the top ten."
        voice "audio/voice/E2/D3/Yuuna/21.ogg"
        ym "But Mr. Takeda, his team is very passionate about what they do and with a little help they can--"
        stop music fadeout 5
        scene cg takeda office annoyed at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with dissolve
        voice "audio/voice/E2/D3/S2/pres1m/26.ogg"
        pres1m "We are not a charity, Ms. Misaki. We don't have the time to hold hands and wait for the team to discover their untapped potential. We are a major corporation and are only interested in teams who have surpassed our expectations."
        voice "audio/voice/E2/D3/S2/pres1m/27.ogg"
        pres1m "Now stop wasting my time."
        
    scene black with fade
    stop ambient fadeout 3
    "All pretenses dropped, Yuuna storms out of the office, while I follow calmly behind. {w}Disappointment makes my feet feel heavy."
    show bg campus intersection day with fade
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 3
    show yuuna ann at cc with dissolve
    "After we leave the building, Yuuna whirls to face me."
    show yuuna ang at cc
    show vein:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D3/Yuuna/22.ogg"
    ym "What a hypocrite! How can his company promote taking risks when he won't take any himself?"
    show yuuna dis at cc
    voice "audio/voice/E2/D3/Yuuna/22_01.ogg"
    ym "I'm sorry you had to go through that."
    pf "It's okay, it was a long shot anyway. Even though we didn't get the sponsorship, I still appreciate you helping me out."
    show yuuna neu at cc
    voice "audio/voice/E2/D3/Yuuna/23.ogg"
    ym "Don't give up just yet. I will get you a sponsor."
    
    menu:
        "I'm not sure how far positive thinking will get us.":
            pf "I like your enthusiasm, but I'm not sure that alone will help us find a sponsor..."
            "She looks at me blankly."
            
        "Leaving less to the imagination might work out in our favour...":
            pf "We should show off more of our \"assets\" next time."
            show yuuna dis at cc
            voice "audio/voice/E2/D3/Yuuna/24.ogg"
            ym "I doubt that would work."
            "That's not the reaction I expected. I've never seen her so serious before."
            show yuuna neu at cc
            pf "I'm not sure what else we can try."
        
        "Let's be realistic.":
            pf "The teams we'll need to beat are all in the top 20. What are the chances of us finding a good sponsor who hasn't already been scooped up by competing teams?"
            show yuuna dis at cc
            voice "audio/voice/E2/D3/Yuuna/25.ogg"
            ym "It's fine. I'll take care of it."
            pf "How?"
            show yuuna neu at cc
            voice "audio/voice/E2/D3/Yuuna/26.ogg"
            ym "It's my job. Let's just get back to campus. There's work to do."
            
    hide yuuna with dissolve
    "Without waiting for me to answer, she hops on the back of my bike. I get on after her and start the engine."
    stop music fadeout 3
    scene black with dissolve
    "Yuuna is quiet the entire ride back to campus. When we arrive, she gives me a hurried goodbye and rushes off, leaving me wondering just what she has planned."
    play ambient "audio/ambience/Parking Lot.ogg" fadein 1
    $renpy.pause(1)
    scene bg campus parking dusk with fade
    "Well, sitting here and stewing in my thoughts isn't productive. I have some time before I need to go home. Maybe someone will be free."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    $ freeTime = "evening"
    
    call E2FreeTime from _call_E2FreeTime_2
    
    jump E2D3S3
