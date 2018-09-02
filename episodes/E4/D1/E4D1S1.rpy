#
label E4D1S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"

    $ meiHairF = "default"
    $ meiHairB = meiHairF
    $ meiOut = "sUniform"
    
    $ day = 1
    $ timeSpent = "none"
    
    #Monday November 8th:
    
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    
    $renpy.pause(1)
    scene bg homekaito myroom blurry with dissolve
    $renpy.pause(0.25)
    scene black with fade
    
    "The buzz of my alarm pulls me out of dreamworld and into reality. With a sleepy roll, I slap blindly at the sound."
    pf "Just five more minutes…"
    "The buzzing doesn't cease no matter how hard I slap my clock. I blink open bleary eyes as \"10:17 AM\" blinks back at me."
    scene bg homekaito myroom day with fade
    pf "Crap!"
    "I shoot straight up in bed. I'm late for class!"
    "I push the \"off\" button on my clock, but it doesn't stop the buzzing."
    "Wait… my alarm doesn't buzz…"
    "Glancing over at my desk, my phone buzzes loudly on the wood. {w}It's Valerie. She's probably wondering why I wasn't in class this morning."
    
    stop sound
    
    menu:
        "I hope she's calling to bring me notes.":
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
            pf "Hey, Valerie. Sorry I missed you in class today."
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L1.ogg"
            vb "Class?"
            "She sounds amused..."
            pf "Yeah, I don't know what happened but my alarm didn't go off."
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L2.ogg"
            vb "Probably because you didn't set it."
            pf "What?"
    
        "Pretend you were there all along.":
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
            pf "Hey, Valerie. That lesson today was pretty insane, huh?"
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L3.ogg"
            vb "Oh? You think so?"
            pf "Yeah… I'll be honest, I didn't understand most of it."
            "Valerie laughs."
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L4.ogg"
            vb "That doesn't surprise me."
            "That's not the reaction I was expecting…"
            pf "Why not?"
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L5.ogg"
            vb "It's hard to understand a lesson you didn't have."
            pf "Huh?"
    
        "Who calls this early?":
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
            pf "Why, Valerie?"
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L6.ogg"
            vb "Oh, did I wake you?"
            "I can hear the laughter in her voice."
            pf "Yes."
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L7.ogg"
            vb "Geez, when do you usually wake up when we don't have class?"
            pf "...We don't have class?"
            voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L8.ogg"
            vb "Of course not."
    
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L9.ogg"
    vb "It's reading week. We don't have classes silly!"
    "...That explains a lot."
    pf "Uh, if we don't have class, then why are you calling me?"
    
    if valrelatonship == 1:
        voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L10.ogg"
        vb "Maybe it's because I missed you."
        "I know that's not why she called, but I grin anyway."
        pf "Or…"
        voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L11.ogg"
        vb "Or maybe it's because I found something {i}interesting{/i} about Eagle's core."
    
    else:
        voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L12.ogg"
        vb "Because unlike somebody, I've been hard at work and found something {i}interesting{/i} about Eagle's core."
    
    pf "Really? What is it?"
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L13.ogg"
    vb "It's the secret to Eagle's maximum overdrive."
    pf "Wait, seriously? What does it say?"
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L14.ogg"
    vb "It says, \"Come to the Hangar right now.\"."
    pf "No, it doesn't."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L15.ogg"
    vb "Only one way to find out."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L16.ogg"
    vb "See you in a few!"
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "She doesn't wait for me to respond before the line goes dead."
    
    if valrelatonship == 1:
        "I know I'm supposed to be annoyed that she'd assume I'd just show up, but she's right that I will. My curiosity overpowers any feelings of irritation."
        "And the fact that I get to see Valerie again is a nice perk."
    
    else:
        pf "Valerie?"
        "..."
        "She's lucky my curiosity is stronger than my irritation."
    
    "I get dressed and ready for the day."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "Just as I'm about to head out the door, my phone beeps."
    "I pull out my phone, expecting another text from Valerie, instead I see an old alert."
    stop music fadeout 3
    "{i}Call Mom today!{/i}"
    "Mom…"
    "My chest tightens as if a hand is holding my heart. Today is--{i}was{/i}--her birthday. Last year, I was so busy at CINY that I completely forgot about Mom's birthday. I didn't give her a call until the next day, and even though she understood, I could tell she was disappointed. I created this alert right afterwards so I'd never forget again."
    "How could I have known that would be her last birthday? A spark of anger heats my blood. If Mom and Dad really were the target of foul play, somebody is going to pay for ripping them away from me… from Nikki."
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    play sound2 "audio/sfx/Technology/Phone Vibration Once.ogg"
    "My phone beeps again. I open up a message from Valerie telling me to hurry up."
    "I need to find out what's going on with Eagle. Maybe that'll give me a hint as to what happened to Mom and Dad…"
    scene black with fade
    stop ambient fadeout 3
    "I take a deep breath, then hop on my bike and hurry to school."
    
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    
    "When I arrive at the Hangar, I head straight for Eagle. Valerie stares intently at the terminal, biting her lip in concentration. She glances at me as I approach and smiles."
    show valerie smi at cc with dissolve
    $renpy.pause(.5)
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L17.ogg"
    vb "I almost thought you weren't going to show up."
    pf "Here I am."
    show valerie hap
    "She points to the terminal, fidgeting with excitement."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L18.ogg"
    vb "It took some time, but I've finally figured it out!"
    pf "You were able to reverse engineer the overdrive mode?"
    show valerie smi
    "Valerie nods."
    pf "That's incredible!"
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    "She grins proudly at my enthusiasm."
    voice "audio/voice/MISSING/BATCH4/Valerie/ValE4Redos/ValE4Redo2.ogg"
    vb "It took a little longer than I expected since the missing pieces were really hard to fill in."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L19.ogg"
    vb "The full schematics are unlike anything I've seen before. I wasn't even able to find anything remotely similar while researching."
    "Her brows furrow in thought, then she shakes her head and her excited grin returns."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L20.ogg"
    vb "Anyway, I've tested the data in the simulator and it worked flawlessly. Your core is calibrated to be able to use the overdrive mode on demand!"
    pf "That's awesome!"
    show valerie mis
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L21.ogg"
    vb "I haven't had a chance to try it in actuality though. As much as I'd love to hop in your cockpit, I'm not much of a pilot."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L22.ogg"
    vb "So I leave the test piloting to you!"
    "I nod."
    pf "Of course. You're amazing, Valerie."
    show valerie mis
    "Her smile broadens."
    
    if valrelatonship == 1:
        voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L23.ogg"
        vb "Don't I get a reward for that?"
        "She taps a finger against her cheek."
        show valerie smi b1
    
        menu:
            "Kiss her cheek.":
                pf "As you wish."
                "I oblige her by leaning forward and giving her a gentle peck on the cheek. She sighs happily."
                show regBlush:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L24.ogg"
                vb "Let me know if you need me to do anything more…"
                pf "I will."
                show valerie mis b2
                voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L25.ogg"
                vb "Just as long as I get that as my prize."
                "I grin."
                show valerie hap b1
                pf "I think we could work something out."
    
            "Kiss her lips.":
                show shoBlush:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                show valerie sur b2
                "I snake an arm around her waist and tug her close. She gasps in surprise but eagerly leans into me as my lips meet hers"
                show valerie hap b2
                "She lingers into the kiss before breathlessly pulling away."
                show heart:
                    xoffset 720
                    yoffset 125
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L26.ogg"
                vb "You're not very good at following directions."
                "I shrug and smirk."
                show valerie smi b1
                pf "Oh well."
                
    show valerie cur
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L27.ogg"
    vb "Oh, I almost forgot."
    show valerie neu
    "She returns to the terminal. As her fingers dance over the keyboard another screen opens up. It's packed tightly with a lot of information and the bottom has an open section to input a password.."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L28.ogg"
    vb "I couldn't figure this out... and it looks like any sort of tampering will potentially wipe the data..."
    pf "Hmm..."
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L29.ogg"
    vb "What's weird about it is that all those lines are not really code that needs to be deciphered. They read more like references I don't understand. Since you built Eagle, I wondered if this might mean something to you."
    "I glance at the screen. It does read like a whole bunch of inside jokes meshed together… some pieces seem familiar but strewn together like that throws me off."
    "I'm sure if I had time to sit down and concentrate I could work through this, but right now I'd rather focus on the overdrive mode."
    pf "Do you have all the data you need for the overdrive mode?"
    show valerie neu
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L30.ogg"
    vb "Yeah. Which is why I almost forgot about this. I'm not sure what's hiding behind here."
    pf "No rush then?"
    show valerie smi
    "She smiles."
    voice "audio/voice/E4/Valerie/ValE4D1/ValE4D1L31.ogg"
    vb "No rush. I do think we should book off some practice time in the arena and confirm the overdrive mode works though. I mean, theory is still theory."
    "I nod."
    pf "I was thinking the same thing. Let's tell the team about this and see if we can get a practice session in before the match."
    hide valerie with dissolve
    stop music fadeout 5
    "I shoot off an urgent group text. As I wait for everyone to show up, I pull up the arena schedule on my phone. Is there any chance it won't be fully booked because it's reading week?"
    "To my surprise, the arena is completely open tomorrow. {w}Talk about good luck!"
    
    jump E4D1S2
