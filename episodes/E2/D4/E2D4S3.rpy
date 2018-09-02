#
label E2D4S3:
    
    $renpy.pause(2.5)
    # it might not be fitting to play this ambient, but otherwise we don't have much for sounds to play here
    # also, doesnt seem like we'll be playing any music until the intense stuff happens
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main dusk with fade
    
    "An uneventful drive later, I arrive at home."
    
    $ valOut = "Hoodie"
    $ valHairF = "hoodieOn"
    $ valHairB = "hoodieOn"
    
    pf "I'm back!"
    "I walk into an eerily quiet living room. Looks I'm the first one here. {w}It feels a bit strange. {w}Nikki's bright smile is usually here to greet me."
    "Maybe she has an after-school club activity or something?"
    "I reach for my pocket to see if she texted me. {w}My heart sinks as my hands grab air. There's a void where my phone should be. {w}Crap, I must have left it in my GEAR!"
    "The sun is setting and it'll be evening by the time I reach campus. Hopefully it won't be too much trouble getting to Eagle after hours. I remember CINY was pretty restrictive on who can enter the hangar at night."
    stop ambient fadeout 3
    #Black screen
    scene black with fade
    "I hop back on my bike and drive back to ACE Academy."
    "Surprisingly, traffic is heavy and it takes longer than expected to reach campus."
    
    #Night time campus main
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg campus main night with fade
    "A handful of students cross the quad as they head towards either their evening classes or the bus station. Even though the sky is an inky darkness, the pathways on campus are still bathed with a soft light. It's kind of peaceful."
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    #play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    #Pilots lounge
    scene bg campus lounge night with fade
    "The Pilot's Lounge is just as busy as always, but I don't recognise too many of the students here. {w}Most of them must be upperclassmen, either third or fourth year. {w}I slip through unnoticed and arrive at the Hangar entrance."
    show guard extra at cc with dissolve
    "I'm about to swipe in when the guard stops me."
    
    voice "audio/voice/E2/D4/S3/Guard/1.ogg"
    gua "Hold on. What's your business in the hangar?"
    pf "I forgot something."
    "It's not a lie, but it would be too embarrassing to tell him the whole truth. {w}Luckily the guard doesn't seem to care. He gives me a quick once over and nods."
    voice "audio/voice/E2/D4/S3/Guard/2.ogg"
    gua "Alright, go ahead and swipe."
    pf "Thanks."
    hide guard with dissolve
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "I bring my student ID in proximity of the sensor. A second later, the success chime sounds as the door slides open."
    stop ambient fadeout 3
    # black BG
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 1
    # can we get a night version of the hangar bg?
    scene bg campus hangar day with fade
    "I follow the tunnel to the hangar. The sound of power tools, machinery and metallic ringing echoes along the walls. {w}It makes sense that most of the repair work happens after hours. It's a lot safer for them to work without the threat of students walking around causing potential disasters."
    
    "Instinctively, my feet lead me to Eagle."
    
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
    
    pf "What the...?"
    
    "A bluish hue from an active terminal display illuminates my docking station. {w}That doesn't seem right… {w}I'm sure I turned everything off when I left."
    
    "Cautiously, I tip-toe towards my GEAR."
    $ valOut = "Hoodie"
    $ valHairF = "hoodieOn"
    $ valHairB = "hoodieOn"
    show valerie neu at cc with dissolve
    "There's a figure crouched in front of Eagle! The person is dressed entirely in black and wearing a hoodie that hides his or her face. Still engrossed in my GEAR, the stranger hasn't detected my presence yet."
    
    menu:
        "Stay quiet and sneak up from behind.":
            "Staying in the shadows, I continually creep towards Eagle. As I close the distance between us, I notice how small and petite the person is. It must be a girl… {w}but I can't think of anyone who'd be so interested in my GEAR."
            show valerie wor at cc
            # Metal Gear alert sfx? lol
            show exclamation:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            "Once I'm only a few steps away, she tenses, as if noticing a presence."
            
            if MCStory == 1:
                # shake animation?
                show valerie sur at cc
                "Before the person can react, my hand grasps her shoulder and she gives a small squeak of surprise. Roughly, I spin her around to face me."
            
            else:
                #timed
                $ qtebase = 3
                $ qtetotal = qteath + qtebase
                $ t_var = qtetotal
                show screen timer_scr(place="E2D4S3_Miss")
                menu:
                    "Grab!":
                        $ renpy.hide_screen ("timer_scr")
                        # shake animation?
                        show valerie sur at cc
                        "Before she can react, I grab her shoulder and roughly spin her to face me."
        
                    "Miss...":
                        label E2D4S3_Miss:
                            $ renpy.hide_screen ("timer_scr")
                            hide valerie with dissolve
                            "I reach out to grab her, but she evades my grasp and begins running. I sprint after her."
                            jump E2D4S3_Run
        
            $ valHairF = "hoodieOff"
            $ valHairB = "hoodieOff"
            pf "Valerie? What are you doing here?"
            show valerie hap at cc
            "She grins."
            show valerie smi b1 at cc with dissolve
            "Her gaze flicks to my hand still on her shoulder."
            show regBlush:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO1.ogg"
            vb "I never would have guessed you like it rough."

            menu:
                "It's not like that!":
                    "I quickly let go of her."
                    pf "That's not it at all!"
                    show heart:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie mis b1 at cc
                    voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO2.ogg"
                    vb "It's okay, I like this side of you."
                    pf "This isn't a joke."
                    show valerie neu at cc with dissolve
                    "Her smile falters."
                    pf "What were you doing to Eagle?"
                    jump E2D4S3_Convergence

                "I can be possessive too.":
                    pf "That's how I get when someone's messing with my baby."
                    "That came out more as a warning than a joke."
                    show valerie mis b1 at cc
                    voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO3.ogg"
                    vb "Sound's like you're overly attached."
                    "She flashes me a playful smirk, but I don't smile back."
                    show valerie neu at cc with dissolve
                    pf "What were you doing messing around with Eagle?"
                    jump E2D4S3_Convergence

                "I am not amused.":
                    show valerie neu at cc with dissolve
                    "I scowl and the smile on her face wavers."
                    pf "What the hell were you doing to Eagle?!"
                    show panic:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie wor at cc
                    "She flinches at the harshness of my tone."
                    jump E2D4S3_Convergence
    
        "Call out!":
            pf "HEY!"
            # Metal Gear alert sfx? lol
            show exclamation:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie wor at cc with dissolve
            $renpy.pause(.5)
            hide valerie with dissolve
            "My legs begin pumping before the words are out of my mouth. The figure darts away from my terminal but I continue to give chase. As I close the distance between us, I can better judge from the stranger's outline that she's a girl."
            pf "Stop!"
            "My screams catch the attention of the few people in the Hangar. They either stand around in confusion or continue with their work."
    
            label E2D4S3_Run:
                $ E2D4S3_RanAfter = 1
                "Whoever this girl is, she sure is fast."
                show guard extra at r2 with dissolve:
                    xzoom -1
                "We near a patrolling guard, who immediately becomes alert."
                pf "HEY! Stop her!"
                scene black with fade
                "The guard steps in front of the girl, who makes a sharp turn away from him. Seeming to anticipate her reaction, he turns with her and easily apprehends her."
                "I skid to a halt just as the guard forces the girl to stop. Her hood slips off, exposing light blonde hair."
                
                voice "audio/voice/E2/D4/S3/Guard/3.ogg"
                gua "What's going on here?"
                pf "This girl was messing with my GEAR!"
                "The girl spins around at the sound of my voice and stares at me with intelligent blue eyes."
                "Wait a minute--I know those eyes…"
                scene bg campus hangar day with fade
                $ valHairF = "hoodieOff"
                $ valHairB = "hoodieOff"
                show guard extra at r2 with dissolve:
                    xzoom -1
                show valerie neu at l2 with dissolve
                pf "{i}You{/i}!"
                show note:
                    xoffset 365
                    yoffset 125
                    xzoom .75
                    yzoom .75
                show valerie mis at l2
                "She winks at me."
                "The guard's eyes narrow and he speaks gruffly."
                voice "audio/voice/E2/D4/S3/Guard/4.ogg"
                gua "Is this true?"
                show valerie sad at l2
                "She fixes her big, doe eyes on him, and her lip trembles."
        
                menu:
                    "It's the girl from class?":
                        pf "Valerie?"
                        show valerie neu at l2
                        "In an instant, she loses her timid expression."
                        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO4.ogg"
                        vb "Yes?"
                        pf "It was you this whole time?"
                        show valerie ner at l2
                        "She nods, looking a little worried. For once I'm at a loss for words. I really wasn't expecting it to be someone I know."
                        pf "...Damn, you're fast."
                        show valerie cur at l2 with dissolve
                        show valerie neu at l2 with dissolve
                        "She blinks and tries to hide a smile as the guard frowns."
                        voice "audio/voice/E2/D4/S3/Guard/5.ogg"
                        gua "You know this girl?"
                        pf "Um, yeah."
                        voice "audio/voice/E2/D4/S3/Guard/6.ogg"
                        gua "So is there a problem here or not?"
                        pf "No, no problem. I'm sorry to have troubled you."
                        show valerie ner at l2
                        "Valerie seems surprised, but doesn't disagree."
                        
                        voice "audio/voice/E2/D4/S3/Guard/12.ogg"
                        gua "Alright, I'll let you two off with a warning this time."
                        voice "audio/voice/E2/D4/S3/Guard/13.ogg"
                        gua "You--"
                        "He points to me."
                        voice "audio/voice/E2/D4/S3/Guard/14.ogg"
                        gua "Get yourself together. Stop screaming and disturbing everyone's evening over nothing."
                        "Geez, that's a little harsh…"
                        "But I nod anyway."
                        voice "audio/voice/E2/D4/S3/Guard/15.ogg"
                        gua "And you--"
                        show valerie sad at l2
                        "He points to Valerie, who hangs her head."
                        voice "audio/voice/E2/D4/S3/Guard/16.ogg"
                        gua "Next time wear something that doesn't resemble a cat burglar."
                        "He leaves, shaking his head and muttering under his breath."
                        show valerie neu at cc with dissolve
        
                    "Just kidding! Play it off as intentional.":
                        pf "Yes, it's true, but it's because I told her to."
                        show valerie cur at l2
                        voice "audio/voice/E2/D4/S3/Guard/7.ogg"
                        gua "You what?"
                        "I rub the back of my head and look apologetic."
                        pf "Yeah, she's an engineer so I asked her to look at my GEAR, but then forgot I asked that."
                        "He responds flatly, clearly unconvinced."
                        voice "audio/voice/E2/D4/S3/Guard/8.ogg"
                        gua "You forgot."
                        pf "Yes."
                        show valerie neu at l2
                        voice "audio/voice/E2/D4/S3/Guard/9.ogg"
                        gua "So you chased her down with murder in your eyes."
                        pf "Whoa, I'm not sure I'd go so far as murder--"
                        voice "audio/voice/E2/D4/S3/Guard/10.ogg"
                        gua "And why didn't she just confront you instead of high-tailing it when you called out?"
                        pf "Uhh…"
                        show valerie wor at l2
                        "Valerie hides her face and her voice grows thick."
                        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO5.ogg"
                        vb "I-I'm so sorry! I'm not used to the Hangar at night and when he yelled so ferociously I was so scared I couldn't think straight. Please forgive me!"
                        show valerie win at l2
                        show crying:
                            xoffset 365
                            yoffset 125
                            xzoom .75
                            yzoom .75
                        "She sobs heavily, her chest heaving, and the guard shifts uneasily."
                        
                        voice "audio/voice/E2/D4/S3/Guard/12.ogg"
                        gua "Alright, I'll let you two off with a warning this time."
                        show valerie sad at l2
                        voice "audio/voice/E2/D4/S3/Guard/13.ogg"
                        gua "You--"
                        "He points to me."
                        show valerie neu at l2
                        voice "audio/voice/E2/D4/S3/Guard/14.ogg"
                        gua "Get yourself together. Stop screaming and disturbing everyone's evening over nothing."
                        "Geez, that's a little harsh…"
                        "But I nod anyway."
                        voice "audio/voice/E2/D4/S3/Guard/15.ogg"
                        gua "And you--"
                        show valerie sad at l2
                        "He points to Valerie, who hangs her head."
                        voice "audio/voice/E2/D4/S3/Guard/16.ogg"
                        gua "Next time wear something that doesn't resemble a cat burglar."
                        hide guard extra with dissolve
                        "He leaves, shaking his head and muttering under his breath."
                
                        show valerie smi at cc with dissolve
                        "Valerie lifts her head once the guard is gone and grins at me, not a tear in sight."
                        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO6.ogg"
                        vb "You think he bought it?"
                        pf "Uh, what?"
                        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO7.ogg"
                        vb "The crying."
                
                        if MCStory == 3:
                            pf "I don't know. I could see right through those fake sobs."
                            show valerie dis at cc
                            show storm:
                                xoffset 720
                                yoffset 125
                                xzoom .75
                                yzoom .75
                            "She pouts."
                            voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO8.ogg"
                            vb "Aw, that's no fun."
                            show valerie smi at cc
                            "But her pout doesn't last long before it turns into a smile."
                
                        else:
                            "Well, I bought it…"
                            pf "Yeah, I think he did."
                            show valerie hap at cc
                            show note:
                                xoffset 720
                                yoffset 125
                                xzoom .75
                                yzoom .75
                            "She laughs."
                            voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO9.ogg"
                            vb "That was too easy."
                            show valerie smi at cc
                            "She focuses a radiant smile on me."
        
                    "Admit my mistake.":
                        pf "Wait, it's okay. You can let her go."
                        show valerie cur at l2
                        show question:
                            xoffset 365
                            yoffset 125
                            xzoom .75
                            yzoom .75
                        "Valerie blinks in surprise, all traces of sadness gone from her face."
                        voice "audio/voice/E2/D4/S3/Guard/11.ogg"
                        gua "What?"
                        pf "I actually know her. Everything is fine."
                        "He stares hard at me."
                        pf "I'm sorry for the inconvenience."
                        "He continues to stare, then sighs and rubs his temples."
                        show valerie neu at l2
                        stop music fadeout 5
                        voice "audio/voice/E2/D4/S3/Guard/12.ogg"
                        gua "Alright, I'll let you two off with a warning this time."
                        voice "audio/voice/E2/D4/S3/Guard/13.ogg"
                        gua "You--"
                        "He points to me."
                        voice "audio/voice/E2/D4/S3/Guard/14.ogg"
                        gua "Get yourself together. Stop screaming and disturbing everyone's evening over nothing."
                        "Geez, that's a little harsh…"
                        "But I nod anyway."
                        voice "audio/voice/E2/D4/S3/Guard/15.ogg"
                        gua "And you--"
                        show valerie sad at l2
                        "He points to Valerie, who hangs her head."
                        voice "audio/voice/E2/D4/S3/Guard/16.ogg"
                        gua "Next time wear something that doesn't resemble a cat burglar."
                        "He leaves, shaking his head and muttering under his breath."
                        show valerie neu at cc with dissolve
        
                
                hide guard with dissolve
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO10.ogg"
                vb "Hey, thanks for covering for me back there. I'm a little surprised you did, honestly."
                "My jaw sets."
                pf "Yeah, well, maybe I shouldn't have."
                pf "What were you doing to Eagle?"
                jump E2D4S3_Convergence
    
    
    label E2D4S3_Convergence:
        show valerie ner at cc
        show panic:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO11.ogg"
        vb "Nothing! I promise."
        pf "You were obviously doing something with the terminal. That's not \"nothing\"."
        show valerie neu at cc
        "She holds up her hands in defense."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO12.ogg"
        vb "I wanted to get a better reading on your core. I'm not altering anything--just studying."
        pf "Why?"
        show valerie smi at cc
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO13.ogg"
        vb "To figure out how your core was able to sustain such a high energy output for so long without completely burning out."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO14.ogg"
        vb "Given the size of your core and the cooling system, the heat dissipation doesn't seem like it would have sustained longer than a few seconds... Yet, it lasted almost 10 minutes!"
        show valerie thi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO15.ogg"
        vb "Maybe there's a direct coolant injection to the primary source? I also didn't consider the acceleration of airflow given the hidden frame openings. Perhaps a quick calculation using..."
    
        if MCStory == 2:
            "The more she talks, the faster my anger melts away and is replaced by respect."
    
        else:
            "My eyes start to glaze over as she continues her technical jargon. As I struggle to pay attention, I can't help but be a little impressed."
    
        "She's more than meets the eye."
    
        if MCStory == 3:
            "I notice that the longer she speaks, the more relaxed her body becomes and her voice is laced with excitement. {w}She's really passionate about how GEARs work, and I believe that she's telling the truth when she said she never intended to sabotage Eagle."
    
        else:
            "Even though she claims she means Eagle no harm, how can I know she's telling the truth? I only met her a few days ago…"
            "Still, it seems like she's genuinely curious about how my core works."
    
        show valerie smi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO16.ogg"
        vb "Here, I'll prove I wasn't changing anything."
    
        if E2D4S3_RanAfter == 1:
            "We return to Eagle where she props up the terminal."
    
        "I watch as Valerie retraces a few screens with all the configuration data unmodified."
        pf "Okay."
        show valerie cur at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO17.ogg"
        vb "Huh?"
        pf "I get it. You were curious, but you can't just break into other people's robots and mess with their parts!"
        show valerie sad at cc
        "She looks away."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO18.ogg"
        vb "I'm sorry."
    
        $renpy.pause(1)
        show dots:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        $renpy.pause(1)
        show valerie ske at cc
        "We're silent, then she looks sideways at me."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO19.ogg"
        vb "So I guess you wouldn't want to know that your primary weapon can actually benefit from an airflow exhaust here and here."
        pf "What?"
        "She points inside my open GEAR."
        show valerie smi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO20.ogg"
        vb "You see right there?"
        pf "...Yes, I think."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO21.ogg"
        vb "It will still require validation testing, though. You should probably get your engineer to check it out."
        pf "My engineer?"
        show valerie mis at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO22.ogg"
        vb "Yeah--you know--the person who makes sure all your GEARs are working properly and helps you with any upgrades or improvements."
        pf "Don't the sponsors do that?"
        show valerie neu at cc
        "Valerie shakes her head."
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO23.ogg"
        vb "They help a lot when it comes to major repairs or new items, but an engineer on your team takes care of any general maintenance and the like."
        pf "Oh."
        
        $ E2D4S3_EngineerGet = 0
    
        menu:
            "Maybe we should get an engineer.":
                $ E2D4S3_EngineerGet = 2
                pf "I'll ask my team about getting an engineer. It sounds like we could really benefit from one."
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO24.ogg"
                vb "You definitely would."
                show valerie smi at cc
                "She scoots closer and smiles."
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO25.ogg"
                vb "And luckily for you, you already have one person perfect for the job."
                pf "Really?"
                show note:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                show valerie mis at cc
                "She scoots even closer and bats her eyelashes at me."
                pf "Who's that?"
                show valerie dis at cc
                "Valerie sighs."
                show valerie smi at cc
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO26.ogg"
                vb "Just think about it."
    
            "Okay, I'll tell \"my engineer\" that.":
                $ E2D4S3_EngineerGet = 1
                pf "Thanks for the heads-up. I'll be sure to let her know."
                show valerie ske at cc
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO27.ogg"
                vb "Her?"
                pf "Yeah. {w}My engineer. Like you said, she should look at it."
                show valerie mis at cc
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO28.ogg"
                vb "Ohhh, right. You do that."
                pf "I will. She'll fix it too, because she's great at what she does."
                show valerie hap at cc
                "Valerie doesn't buy it and is trying hard to hold back a laugh."
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO29.ogg"
                vb "I'm sure she is… but I'll bet she's nothing compared to me."
                
                ### NOTE FreeTime - "IF completed Event 2:"
                if E2VBS2_Completed == 1:
                    pf "Hmm, I wouldn't be so sure. At least {i}she{/i} has a mobile phone."
                    show valerie cur at cc with dissolve
                    show note:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    show valerie hap at cc with dissolve
                    "Valerie blinks in surprise, then laughs."
                    show valerie smi at cc
                
                else:
                    pf "No, she's cuter."
                    show note:
                        xoffset 720
                        yoffset 125
                        xzoom .75
                        yzoom .75
                    "Valerie laughs."
                    voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO30.ogg"
                    vb "Hehe, Good joke."
    
            "We're just fine without one.":
                pf "I can fix that myself."
                show valerie cur at cc
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO31.ogg"
                vb "You sure?"
                pf "I built this GEAR. I can repair it too."
                show valerie smi at cc
                "She shrugs."
                voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO32.ogg"
                vb "If that's what you prefer."
    
        "There's another pause. {w}To avoid the awkwardness, I shut down the open terminal."
        pf "So, we should get going then."
        show valerie neu at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO33.ogg"
        vb "Yeah."
    
        show dots:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "Neither one of us moves."
        pf "Don't touch my GEAR again without my permission."
        show valerie smi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO34.ogg"
        vb "I promise I won't."
        "I wait for her to leave, but she doesn't budge."
        
        pf "Okay… goodbye…"
        show valerie hap at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO35.ogg"
        vb "Bye!"
        "She stands in place and waves."
        
        pf "You aren't leaving."
        show valerie smi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO36.ogg"
        vb "Neither are you."
        pf "Okay, on the count of three we'll leave together."
        "She nods."
        
        pf "One…"
        pf "Two…"
        pf "Three!"
    
        "We both stay put."
        pf "You didn't move!"
        show valerie mis at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO37.ogg"
        vb "Neither did you!"
        voice "audio/voice/E2/D4/S3/Guard/17.ogg"
        gua "What the hell are you kids still doing here?"
        "Security catches us off-guard, and we simultaneously stammer nonsense."
        "He shakes his head."
        voice "audio/voice/E2/D4/S3/Guard/18.ogg"
        gua "If your business here is done, then you have to leave."
        show valerie neu at cc
        "Valerie glances at me and I glance at her, still waiting for her to move. {w}She doesn't."
    
        "Suddenly, a strong hand grips my arm."
        pf "Hey!"
        show guard extra at r3 with dissolve:
            xzoom -1
        show valerie sur at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO38.ogg"
        vb "Ah!"
        "The guard holds Valerie too. He physically leads us toward the exit."
        voice "audio/voice/E2/D4/S3/Guard/19.ogg"
        gua "You should get home. It's late."
        stop ambient fadeout 3
        scene black with fade
        $renpy.pause(1)
        #play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
        scene bg campus lounge night with fade
        show valerie neu at cc with dissolve
        "We pass through the doors, and the guard shuts them behind us. {w}Valerie and I are once again standing in silence."
        show valerie smi at cc
        voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO39.ogg"
        vb "Well, I'll see you around."
        
        ### NOTE FreeTime - "IF completed Event 1:"
        if E2VBS1_Completed == 1:
            pf "This weekend, right? We have to do our project."
            show valerie mis at cc
            voice "audio/voice/E2/D4/Valerie/ValerieE2D4REDO40.ogg"
            vb "Yup, it's a date."
            show heart:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            hide valerie with dissolve
            "She winks at me, then turns around and leaves. {w}I call after her."
            pf "It's not a date!"
            "My protest falls on deaf ears. {w}Oh well. I'm sure she was joking anyway… {w}maybe."
            stop music fadeout 3
            stop ambient fadeout 3
            scene black with fade
            "I head to the parking lot."
    
        else:
            pf "Yeah, see you."
            stop music fadeout 3
            stop ambient fadeout 3
            scene black with fade
            "We both head our separate ways. She walks toward the dorms while I head to the parking lot."
        
        $renpy.pause(1)
        "Once I reach my bike, I drive home."
        $renpy.pause(2.5)
        play ambient "audio/ambience/Night Crickets.ogg" fadein 1
        scene bg homekaito main night with fade
        "Nikki still isn't home by the time I return. {w}Where can she be?"
        "I reach into my pocket for my phone and grasp empty air."
        "..."
        "{i}Oh crap, not again!{/i}"
        #fade to black
        scene black with fade
        
        $ valOut = "sUniform"

        
        jump E2D5S1
    
