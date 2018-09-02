#
label E4D5YM:

    play ambient "audio/ambience/Morning.ogg" fadein 3
    $renpy.pause(1.0)
    
    "Soft light beams on my face. Mixed with the pitter patter of soft footsteps, I am gently awoken from slumber."
    scene bg homekaito myroom day with fade
    
    "Yawning widely, I blink open my eyes and see Yuuna placing her bag beside my desk. She tucks a strand of her long hair behind her ear before glancing over at me."
    "When she sees that I'm awake, her face lights up in a wide smile."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show yuuna hap at cc with dissolve
    voice "audio/voice/E4/Yuuna/E4/D5/1.ogg"
    ym "Rise and shine!"
    pf "Yuuna?"
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D5/2.ogg"
    ym "Mhm."
    "She walks over to me and sits on the edge of my bed."
    pf "What are you doing here?"
    show yuuna cur
    voice "audio/voice/E4/Yuuna/E4/D5/3.ogg"
    ym "I'm here to study! Don't you remember?"
    pf "Uhh--"
    "Yuuna leans over me."
    show yuuna hap
    voice "audio/voice/E4/Yuuna/E4/D5/4.ogg"
    ym "Time to get up, sleepyhead! Up up!"
    
    $ E4D5YM_Sleep = 0
    
    menu:
        "Must sleep more!":
            $ E4D5YM_Sleep = 1
            pf "No, it's still time for sleep."
            show yuuna dis
            voice "audio/voice/E4/Yuuna/E4/D5/5.ogg"
            ym "How can you sleep when the sun is shining so brightly in the sky?"
            "I roll over in my bed and pull the blankets over my head. No more sun. Just sweet, sweet darkness."
            "My comforting darkness is ripped away as my blankets are stripped from me. I look over at Yuuna holding my covers."
            show yuuna sur b3 with dissolve
            "Her eyes are wide and her mouth is open."
            voice "audio/voice/E4/Yuuna/E4/D5/6.ogg"
            ym "Y-You're in your boxers?!"
            "I glance down at myself."
            pf "Well, yeah, it's not like I was expecting company this morning…"
            "Yuuna's face is bright red as she drops the blankets."
    
            menu:
                "Quickly cover up!":
                    "I grab the fallen blankets and cover myself again. My face feels as hot as the sun."
    
                "I like an aggressive woman.":
                    pf "You can remove more if you like."
                    "I didn't think it was possible, but Yuuna's face grows even redder."
                    show yuuna win b3
                    voice "audio/voice/E4/Yuuna/E4/D5/7.ogg"
                    ym "No! That's not--I wasn't trying--"
                    pf "If that's what you do when you aren't trying, I can't wait to see what happens when you do try."
                
                "This isn't a big deal.":
                    pf "What's the problem? You've seen me in my swimsuit before. This isn't that different."
                    show yuuna win b3
                    voice "audio/voice/E4/Yuuna/E4/D5/8.ogg"
                    ym "Yes, it is!"
                    pf "How?"
                    show yuuna wor b3
                    voice "audio/voice/E4/Yuuna/E4/D5/9.ogg"
                    ym "You're in your underwear!"
                    pf "..."
    
            show yuuna ner b2 with dissolve
            "Yuuna squeals and runs to my closet. Then starts throwing any clothes she can find at me."
            pf "Hey! Wha--"
            "I dodge a pair of jeans, more T-shirts, even more of my boxers. That'll teach me not to put my laundry away…"
            voice "audio/voice/E4/Yuuna/E4/D5/10.ogg"
            ym "Time for you to get dressed!"
            "A small mountain of clothes is piled on top of me."
            pf "Uh, yeah, I'll get right on that."
            hide yuuna with dissolve
            "I grab what I need from the pile and slip out from beneath the clothes. Then I head to the washroom to get dressed."
    
        "Boobs in my face.":
            "At this angle, my direct line of sight stares right down Yuuna's top. {w}I could get used to waking up like this every morning!"
            show yuuna sur
            "Yuuna follows my gaze and quickly straightens back up."
            show yuuna dis b2 with dissolve
            voice "audio/voice/E4/Yuuna/E4/D5/11.ogg"
            ym "Ahem!"
            pf "For some reason, I'm feeling a lot more energised than I was a second ago."
            show yuuna cur b2
            voice "audio/voice/E4/Yuuna/E4/D5/12.ogg"
            ym "Does that mean you're ready to get out of bed?"
            pf "I don't know… I think I might need a little more than that to tempt me…"
            "Yuuna's eyes sparkle."
            show yuuna mis b2
            voice "audio/voice/E4/Yuuna/E4/D5/13.ogg"
            ym "Oh yeah?"
            "She leans in close. Her lips are just a breath away from my own. Instinctively, I lean forward to meet her lips, but instead my lips meet empty air!"
            pf "Wha…?"
            show yuuna hap b2
            "Yuuna giggles, then stands up."
            pf "Hey! That's not fair!"
            show yuuna mis b2
            voice "audio/voice/E4/Yuuna/E4/D5/14.ogg"
            ym "If you want the kiss then you need to get out of bed."
            pf "Deal!"
            "I throw back the covers and hop out of bed. Yuuna's eyes widen as I scoop her into me. I run my hands through her luxurious hair as my lips finally meet hers."
            show yuuna smi b3 with dissolve
            "Yuuna sighs into the kiss, but all too soon she pulls away. Her cheeks are as bright as her hair and she looks anywhere but at me."
            voice "audio/voice/E4/Yuuna/E4/D5/15.ogg"
            ym "That was great and all, but…"
            pf "But what?"
            show yuuna cur b3
            voice "audio/voice/E4/Yuuna/E4/D5/16.ogg"
            ym "You should probably get dressed now."
            "I glance down at myself and realise I'm just wearing my boxers. {w}Oops! Now it's my turn to blush."
            hide yuuna with dissolve
            "I quickly grab my clothes and head to the washroom to get dressed."
    
        "I'm up!":
            pf "Okay, I'm up!"
            "I throw back my blankets and step out of bed."
            show yuuna sur b2 with dissolve
            "Yuuna grins in triumph, but just as suddenly her mouth opens in shock."
            pf "What?"
            voice "audio/voice/E4/Yuuna/E4/D5/17.ogg"
            ym "Why are you only in your boxers?!"
            pf "I sleep in these."
            "Her face turns bright red and she turns away from me."
            show yuuna win b2
            voice "audio/voice/E4/Yuuna/E4/D5/18.ogg"
            ym "Sorry! You should probably go get dressed!"
            pf "Yeah, good idea."
            hide yuuna with dissolve
            "I grab my clothes and head to the washroom to get dressed."
    
    "Once I'm presentable I return to my room to see Yuuna sitting patiently at my desk. Her books and tablet are opened and she'd even opened some of my textbooks for me too."
    
    if E4D5YM_Sleep == 1:
        "She also cleaned up the clothes from my bed and put them neatly back in my closet."
    
    "I join her at the desk, and she's back to her usual self."
    show yuuna smi at cc with dissolve
    voice "audio/voice/E4/Yuuna/E4/D5/19.ogg"
    ym "I figured we could start with History so I got your book for you."
    pf "Thanks."
    "I turn on my tablet and Yuuna and I begin to compare notes."
    scene black with fade
    "We've studied a few times before, so Yuuna and I easily worked up a rhythm of quizzing each other. After a couple of hours, Yuuna had to leave. {w}After we said our goodbyes, I crawled right back into bed."
    "Studying really takes it out of a guy… I'm exhausted."
    stop music fadeout 3
    stop ambient fadeout 3
    "Before long, I fall asleep."
    
    jump E4D5S1_RomanceReturn
