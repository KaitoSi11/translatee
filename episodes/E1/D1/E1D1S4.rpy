label E1D1S4:
        
    scene bg homekaito myroom night packed with fade
    "Alright, time to unpack."
    
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 1 fadeout 1
    
    scene bg homekaito myroom night with Dissolve(3.0)
    $ nikOut = "sSleepwear"
    
    $renpy.pause(1.0)
    "I manage to put most of my things away before I'm interrupted."
    
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    voice "audio/voice/E1/D1/S4/Nikki/1.ogg"
    sf "You done unpacking yet?"
    
    show nikki neu at r3 with dissolve:
        xzoom -1
    
    "Nikki seems tense. Although there's a small smile on her lips, her brows are furrowed in worry."
    
    pf "Just about. What about you?"
    
    show nikki ner at cc with dissolve:
        xzoom 1
    voice "audio/voice/E1/D1/S4/Nikki/2.ogg"
    sf "Almost… but hey, what do you think about this whole uniform thing? It's kinda weird, isn't it?"
    show dots:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She shifts uncomfortably from one foot to the other."
    
    menu:
        "I think it’s a great idea.":
            pf "It’ll be a nice change. And we won’t have to worry about mismatched socks or anything like that." 
            show nikki smi at cc
            "She giggles."
            show nikki mis at cc
            voice "audio/voice/E1/D1/S4/Nikki/3.ogg"
            sf "Maybe that's something that happens to you, but my socks always match."
    
        "It doesn't make a difference.":
            pf "Does it matter? We'll get used to it."
            show nikki thi at cc
            "Nikki stares at the ground."
            voice "audio/voice/E1/D1/S4/Nikki/4.ogg"
            sf "I suppose you're right."
    
        "It'll be like one of my Japanese animes!":
            pf "Are you kidding? It'll be great! Just think of all those girls in short skirts. Huehuehue."
            show nikki ske at cc
            "And those perfectly timed updrafts revealing cute, colorful panties--"
            
            show nikki ann
            play sound "audio/sfx/Human/light_punch.ogg"
            with Shake((0, 0, 0, 0), .5, dist=10)
            
            $renpy.pause(.25)
            pf "Ow!"
            "For such a small girl, she sure packs a punch."
            "Nikki sighs."
            #show tsuBlush:
             #   xoffset 720
              #  yoffset 160
               # xzoom .75
                #yzoom .75
            voice "audio/voice/E1/D1/S4/Nikki/5.ogg"
            sf "You’re hopeless."
            
    show nikki sur at cc with dissolve
    show exclamation:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S4/Nikki/6.ogg"
    sf "Oh, I almost forgot! What kind of uniform do you have to wear anyway? I mean, mine’s... normal, but you’re going to ACE Academy."
    
    "I shrug."
    
    pf "The dress code says something about distinguishing the students in the pilot program from the rest of the student body. The pilots wear teal markings to indicate their program." 
    
    show nikki cur at cc
    voice "audio/voice/E1/D1/S4/Nikki/7.ogg"
    sf "Ooh, that sounds good. You transferred directly into their pilot program, right?"
    
    pf "Yup." 
    
    show nikki hap at cc
    voice "audio/voice/E1/D1/S4/Nikki/8.ogg"
    sf "I heard that program is hard to get into, but I never doubted you! I hope they're ready for you because you're going to kick butt!"
    
    pf "Thanks, sis."
    
    "The clock on my nightstand flashes 11:00 PM."
    
    pf "I think it's time to go to bed."
    
    show nikki wor at cc
    voice "audio/voice/E1/D1/S4/Nikki/9.ogg"
    sf "What? Already?"
    
    "I gently herd her out of my room."
    show crying:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D1/S4/Nikki/10.ogg"
    sf "But it's not {i}that{/i} late!"
    
    pf "Come on. You don't want to be falling asleep in class now, do you?"
    
    show nikki sad at cc
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She pouts, and I'm worried she'll continue to argue, but she just mumbles something incoherent and turns towards her room."
    
    pf "Good night."
    
    show nikki smi at cc
    voice "audio/voice/E1/D1/S4/Nikki/11.ogg"
    sf "Night."
    
    hide nikki with dissolve
    play sound "audio/sfx/Impacts/Box Shuffling.ogg" fadein 5 fadeout 5
    
    "I return to my mess of boxes and try to organise them into something resembling a neat pile. {w}As I reach for the last box, a picture frame falls to the ground with a loud clatter. My heart tightens in my chest as I snatch it up and inspect it for any fractures. {w}Luckily, it's unharmed."
    
    
    $ persistent.gpix[0][0] = 1
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (1740, 180, 1920, 1080), 0) with dissolve
    
    "I run my finger over our smiling faces: me, Nikki, Mom, Dad. {w}We were at the fair and Nikki wanted to ride the roller coaster. {w}I remember Mom and I had just argued over something stupid before the picture was taken, but you'd never be able to tell from this photo. Mom always looked so poised and together."
    
    scene cg mc family photo at Zoom((1920, 1080), (1740, 180, 1920, 1080), (0, 0, 3840, 2160), 5.0)
    
    "I place the frame beside my computer, trying to ignore the lump in my throat."
    
    "I lay on my bed and close my eyes, but my thoughts refuse to quiet. {w}Eventually my exhaustion takes over and I fall asleep among a tangle of questions and \"what if's\" running through my mind."
    
    stop music fadeout 3
    stop ambient fadeout 3
        
    scene black with fade
    
    $renpy.pause(1)
    
    jump E1D2S1
