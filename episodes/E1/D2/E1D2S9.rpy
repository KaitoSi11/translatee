label E1D2S9:
    
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    scene bg campus hangar day with fade
    
    "I follow a long hallway, which leads into a grand space filled with towering GEARs. {w}Every one of them is sleek, refined, and updated with the latest model of accessories and weapons. {w}They weren't kidding when they said Japan was the leader in mecha technology."
    
    "I walk past severals rows of GEAR until..."
    play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 1
    #scene cg GEAR hangar first at Zoom((1920, 1080), (0, 0, 3840, 2160), (0, 0, 3840, 2160), 0) with Dissolve(2.5)
    
    #show cg GEAR hangar first with Dissolve(2.0):
    #    xzoom .9
    #    yzoom .9
    #    yoffset -800
    #    linear 8.0 yoffset 0
        
    #$renpy.pause(4.0, hard=True)
    #"...I am reunited with Eagle."
    
    #show cg GEAR hangar first with Dissolve(1.0):
    #    parallel:
    #        linear 4.0 xzoom .5
    #    parallel:
    #        linear 4.0 yzoom .5
    #    parallel:
    #        linear 2.0 yoffset 0

    $ persistent.gpix[3][0] = 1
    show cg GEAR hangar first with Dissolve(2.0):
        xzoom 1.5
        yzoom 1.5
        yoffset -500
        linear 5.0 yoffset 0
        
    $renpy.pause(3.0, hard=True)
    "...I am reunited with Eagle."
    
    show cg GEAR hangar first with Dissolve(1.0):
        parallel:
            linear 4.0 xzoom 1
        parallel:
            linear 4.0 yzoom 1
        parallel:
            linear 2.0 yoffset 0
            
        
    $renpy.pause(4.0)
    "A crowd of students surround it. They speak in hushed tones, but break into snickers when they notice me."
    
    "I push my way towards them, but they disperse before I even reach them. Most are trying to hide their laughter and failing miserably."
    
    "I give my GEAR a detailed inspection to make sure it didn't suffer any dings or damages during transit. {w}So far so good. My GEAR may be a bit bulkier than others, but it's in great working condition, which ultimately, is what matters. The colours are still bright, too. I wonder if they polished it for me or if it always looked this good."
    $ ss = Character("Shou Shinjirou", color="#01DF3A")
    stop music fadeout 5
    voice "audio/voice/E1/D2/S9/Shou/23.ogg"
    ss "The other guys might laugh at your GEAR, but I sense that it's different."
    scene bg campus hangar day with fade
    show shou mis at cc with dissolve
    voice "audio/voice/E1/D2/S9/Shou/24.ogg"
    ss "Spirit."
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou hap at cc
    voice "audio/voice/E1/D2/S9/Shou/25.ogg"
    ss "Something that makes it stand out amongst the others. Yes, I can feel this one is truly special indeed."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 1
    "Uh? I hadn't noticed the student beside me. His arms are folded and he's nodding with closed eyes, as if he's saying something truly deep and meaningful."
    
    menu:
        "Can I help you…?":
            "He seems harmless enough… {w}Sort of. I may as well see what he wants. I might even be able to ask some questions of my own afterwards."
    
            pf "Hey, can I help you there?"
    
        "Damn right it's something special!":
            "I'm glad at least {i}someone{/i} here knows a good GEAR when he sees one. I also fold my arms and nod. I'm tempted to ask him to repeat himself so I can record those words of wisdom."
    
            pf "Damn right. I think the other guys are just scared."
    
        "Shuffle away from this lunatic.":
            "There's clearly something \"not right\" about this guy. Who says things like that? Especially to someone you've just met."
    
            show shou hap at cc with dissolve:
                xzoom 0.75
                yzoom 0.75
                
            "I shuffle away from him, hoping he'd take the hint."
            #shou sprite movements maybe
            "..."
    
            show shou hap at cc with dissolve:
                xzoom 1
                yzoom 1
                
            "As if in sync, he moves closer whenever I move away. When I mistakenly make eye contact, he grins at me. Alright… getting sort of scared now."
    
            "Maybe I can distract him with conversation until I find a way to escape."
    
    pf "Uh, Do you need something?"
    show shou sur at cc with dissolve
    show shocked:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S9/Shou/2.ogg"
    ss "Oh, right!"
    stop music fadeout 3
    "He seems almost surprised, as if he'd forgotten why he came. He fidgets so much I wonder if he's nervous."
    show shou smi at cc
    play music "audio/music/Bright New Day (GAME VERSION).ogg"
    voice "audio/voice/E1/D2/S9/Shou/3.ogg"
    ss "The names, Shou. Shou Shinjirou. Pleased to meet you!"
    show shou hap at cc
    "He thrusts his hand out in greeting, grinning from ear to ear. I cautiously shake his hand."
    
    pf "Uh, hi, I'm [pfull]."
    show shou smi at cc
    voice "audio/voice/E1/D2/S9/Shou/4.ogg"
    ss "You're a second year pilot too, right?"
    
    pf "Yeah. How did you--"
    show shou mis at cc
    voice "audio/voice/E1/D2/S9/Shou/5.ogg"
    ss "Not that many students transfer during second year, you know? You're the talk of the Pilot's Lounge! A mysterious, foreign transfer student."
    
    "That would explain the interest around my GEAR. I guess I didn't quite live up to their expectations. I'm not sure what they were expecting, though."
    show shou hap at cc
    show bulb:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S9/Shou/6.ogg"
    ss "And I deduced that {i}you{/i} are this transfer student."
    
    "I wonder what gave me away? It couldn't possibly have been my magnificent golden locks."
    show shou ske at cc with dissolve
    voice "audio/voice/E1/D2/S9/Shou/7.ogg"
    ss "I've got to say… I thought you'd be taller."
    show shou neu at cc
    "He starts comparing our heights with his hand, and is a bit disappointed to find we're about the same height. Again, just what was he expecting? We don't all look like {i}Ceonardo DiLaprio{/i}. I think his perception of America is a bit skewed…"
    show shou smi at cc
    voice "audio/voice/E1/D2/S9/Shou/8.ogg"
    ss "Anyway, you're new here, which means you're not part of a team yet, right?"
    
    "Right. That's been on my mind since class ended. I nod, almost certain I know what he's about to say next."
    show shou hap at cc
    voice "audio/voice/E1/D2/S9/Shou/9.ogg"
    ss "Well, it just so happens that my team is lacking that oh-so-vital fourth member we need to be able to compete."
    
    "He looks at me hopefully, then leans in close… a little too close. Personal space, man!"
    show shou mis at cc with dissolve
    voice "audio/voice/E1/D2/S9/Shou/10.ogg"
    ss "You see where I'm going with this, don't you? Basically, what I'm saying is, you should join my team because we're awesome."
    $ E1D2S9_AgreeJoinShouTeam = 0
    menu:
        "Sounds like fun. Sign me up!":
            "What the hell, he seems friendly enough. Plus, I'm not exactly in a position to be picky about whose team I join."
    
            pf "Sure, why not?"
            show shou hap at cc
            show note:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S9/Shou/11.ogg"
            ss "Now that’s what I’m talking about, broseph!"
    
            "Excitement brightens his face, and I’ll admit, the feeling is somewhat infectious."
            show shou smi at cc
            voice "audio/voice/E1/D2/S9/Shou/12.ogg"
            ss "Come on, our lounge is that way. I’ll introduce you to the team!"
            hide shou with dissolve
            "Shou and I start making our way down the hall."
            voice "audio/voice/E1/D2/S9/Shou/13.ogg"
            ss "Now… where should I start? Oh right, so there’s this girl--" 
            $ E1D2S9_AgreeJoinShouTeam = 1
    
        "Sorry. I want to see what my options are.":
            pf "As fun as that sounds, I'd like to check out the other teams before committing to any of them."
            show shou ner at cc with dissolve
            voice "audio/voice/E1/D2/S9/Shou/14.ogg"
            ss "Aww."
    
            "For a second he almost looks heartbroken, but that is quickly replaced by his usual goofy grin."
            show shou hap at cc
            voice "audio/voice/E1/D2/S9/Shou/15.ogg"
            ss "That's cool, I understand. No big deal."
    
            "I'm glad he's taking it so well. I was worried he wouldn't leave me alone until I joined him."
            show shou smi at cc
            voice "audio/voice/E1/D2/S9/Shou/16.ogg"
            ss "Most of the other pilots generally hang out in the Pilot's Lounge. If anyone's looking for more team members, you'll find them there."
    
            pf "Thanks. I'll see you around."
            show shou mis at cc
            voice "audio/voice/E1/D2/S9/Shou/17.ogg"
            ss  "For sure. Good luck, broseph. Just remember, we're always here if you change your mind!"
            hide shou with dissolve
            "We wave goodbye before heading our separate ways."
    
        "Haha. No.":
            "I'm not sure I want to be stuck with this weirdo for longer than I have to."
            pf "Thanks, but no thanks."
            show shou ner at cc
            show drop:
                xoffset 720
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D2/S9/Shou/18.ogg"
            ss "Oh…"
            pf "I'm not sure if I'd be a good fit."
            show shou sad at cc
            "His face falls, and I almost feel bad for him, but his frown is quickly replaced with his usual grin."
            show shou hap at cc with dissolve
            voice "audio/voice/E1/D2/S9/Shou/19.ogg"
            ss "No worries, man. I get it. You're new and want to check everything out before making a decision, right?"
            pf "Uhh, right. Sure. Whatever."
            show shou smi at cc
            voice "audio/voice/E1/D2/S9/Shou/20.ogg"
            ss "Okay, well, the pilots usually hang out in the Pilot's Lounge. You can introduce yourself and see how things go."
            pf "Thanks."
            "This guy's being surprisingly cool about everything…"
            show shou mis at cc
            voice "audio/voice/E1/D2/S9/Shou/21.ogg"
            ss "Not sure how many teams are on the market for another member."
            "Ha, I'll take my chances."
            pf "Well, thanks for the tip. Maybe I'll see you around."
            show shou hap at cc
            voice "audio/voice/E1/D2/S9/Shou/22.ogg"
            ss "Good luck, broseph."
            hide shou with dissolve
            "Still grinning, he waves, then heads out."
            "I can't tell if I've hurt his feelings or not. Well, not my problem. After one last glance at my GEAR, I also head out."
    
    stop music fadeout 3
    if (E1D2S9_AgreeJoinShouTeam == 0):
        "So, my best bet for now is to head to the pilot’s lounge."
    
        if (E1D2S4_MayuGaveDirections == 1):
            scene bg campus hangar day with fade
            "Since I cut through the pilot lounge earlier today to reach the hangar, I know where I'm headed and don't bother with the campus map."
            "Within a few minutes, I'm at the lounge door."
    
    
        else:
            "I pull up the campus map again. A small red light pulsates when I try to locate the pilot's lounge."
            "I'm about to head towards the exit, when I spot a group of pilots heading in the opposite direction."
            "Hm, maybe they need another team member."
            "They're already a good distance in front of me, so I hustle to keep up, and follow them through a winding tunnel. I'm pretty sure this is how people get murdered…"
            "Eventually, the group disappears through a door, which leads to… the Pilot's Lounge. Huh, good to know!"
            
    scene black with fade
    stop ambient fadeout 3
    jump E1D2S10
