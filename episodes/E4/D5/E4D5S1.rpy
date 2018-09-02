#
label E4D5S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sFlirty"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sCasual"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sCasual2"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sDate2"
    
    $ yuuHairF = "braided"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sCute"
    
    $ day = 5
    $ timeSpent = "none"
    

    if kaorelatonship == 1:
        jump E4D5KI
        
    elif mayrelatonship == 1:
        jump E4D5MA
        
    elif valrelatonship == 1:
        jump E4D5VB
        
    elif yuurelatonship == 1:
        jump E4D5YM
    
    
    label E4D5S1_RomanceReturn:
        
        
    if kaorelatonship == 0 and mayrelatonship == 0 and valrelatonship == 0 and yuurelatonship == 0:
        $renpy.pause(1)
        play ambient "audio/ambience/Morning.ogg" fadein 1
        $renpy.pause(1)
        #beep beep beep
        play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
        $renpy.pause(2.5)
        stop sound fadeout 1
        scene bg homekaito myroom blurry with fade
        "The familiar sound of my alarm wakes me up. I turn it off and rub the sleep from my eyes."
        "Why did I set an alarm when I don't have any classes today? {w}Oh, right, I wanted to get some studying done."
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
        scene bg homekaito myroom day with fade
        "Stifling a yawn, I force myself out of bed and head to the washroom to get ready."
        "Once I've gone through my morning routine, I'm a lot more awake and ready to hit the books."
        
        if MCStory == 2:
            "I crack open my first textbook and decide to give myself a mini-quiz. I feel more and more energised with each answer I get correct."
            "I'm confident that exams next week will be a breeze!"
        else:
            "I have to force myself not to start studying my easiest classes and focus first on the difficult material. The more I focus the more tired I get. How did I ever study in the past?"
    
        "After a couple of hours, my eyes are starting to cross and I need a break."
       
    else:
        $renpy.pause(2.5)
        scene bg homekaito myroom day with fade
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
        "I woke up from my nap feeling refreshed."
        "That really hit the spot!"
        
    "There's still a lot of time before my Aludian meeting this afternoon..."
    "I wonder if anyone is free."
    
    #afternoon
    $ freeTime = "afternoon"
    
    stop music fadeout 3
    call E4FreeTime from _call_E4FreeTime_5
    play ambient "audio/ambience/Campus Road.ogg" fadein 3
    scene bg campus intersection day with fade
    "It's almost time for my appointment with Aludian. I drive my bike downtown and park near Aludian Enterprises. {w}The building is impressive as the sunlight reflects off of the tinted windows. Aludian's signage is posted on the front entrance. It's large enough to be seen from a distance but isn't as gaudy as Warptech's signage."
    stop ambient fadeout 5
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    scene black with fade
    "The receptionist cheerfully greets me when I enter. I let her know my name and it's not long before I'm led to an engineer's office."
    #play ambient "audio/ambience/Campus Office.ogg" fadein 3
    scene bg campus office day with fade
    "He gestures for me to have a seat, which I accept."
    pf "Thank you for agreeing to meet with me."
    show receptionist extra at cc with dissolve
    voice "audio/voice/E4/Aludian Engineer/E4/D5/1.ogg"
    aeng "My pleasure. How may I be of assistance?"
    pf "I had a few questions about the core overdrive technology seen at ACE Academy's match yesterday."
    voice "audio/voice/E4/Aludian Engineer/E4/D5/2.ogg"
    aeng "What questions?"
    
    label E4D5S1_Questions:
        menu:
            "Ask an easy question to test what he'll tell me." if E4D5S1_Question1 == 0:
                $ E4D5S1_Question1 = 1
                pf "How is that technology enabled?"
                voice "audio/voice/E4/Aludian Engineer/E4/D5/3.ogg"
                aeng "I'm sorry, but I'm not allowed to divulge company secrets."
                pf "My apologies if the question was unclear. I meant to ask how Akira was able to enable the overdrive mode during the match."
                voice "audio/voice/E4/Aludian Engineer/E4/D5/4.ogg"
                aeng "Yes, I understand. Unfortunately that is not something I am at liberty to share."
                "Even Akira was able to give me that information. How come this man won't?"
                "Something strange is going on…"
            
            "Ask the question I'm dying to know." if E4D5S1_Question2 == 0:
                $ E4D5S1_Question2 = 1
                pf "How were you able to engineer the core's overdrive mode? That technology is not common knowledge."
                voice "audio/voice/E4/Aludian Engineer/E4/D5/5.ogg"
                aeng "I apologise, but I can't disclose company secrets."
                "I should have seen that coming. If they're so tight-lipped, does that mean there's some shady business going on here?"
                
        if E4D5S1_Question2 == 0:
            jump E4D5S1_Questions
        else:
            jump E4D5S1_Continued
            
    label E4D5S1_Continued:
        pf "I'm not sure what is going on here. As far as I'm aware, that technology has not been made available so how was that addition suddenly built into Akira's GEAR?"
        voice "audio/voice/E4/Aludian Engineer/E4/D5/6.ogg"
        aeng "Again, I'm sorry, but that's not something I'm at liberty to discuss."
        "Obviously this conversation is going nowhere. My frustration increases and makes my tongue loose."
        pf "Then what {i}can{/i} you discuss? So far that's been the only thing you've said!"
        "He frowns."
        stop music fadeout 7
        voice "audio/voice/E4/Aludian Engineer/E4/D5/7.ogg"
        aeng "I don't appreciate that tone."
        pf "I don't appreciate you stringing me along like this. Why did you agree to meet me if you had no intention of talking to me?"
        voice "audio/voice/E4/Aludian Engineer/E4/D5/8.ogg"
        aeng "If you ask me a question I am at liberty to answer, then I will gladly answer it for you."
        pf "The only answers I need are for the questions that I've asked."
        voice "audio/voice/E4/Aludian Engineer/E4/D5/9.ogg"
        aeng "I'm sorry, but it looks like I won't be able help you."
        "I cross my arms."
        pf "I'm not leaving here without answers."
        voice "audio/voice/E4/Aludian Engineer/E4/D5/10.ogg"
        aeng "Then I'm afraid I will have to call for security."
        hide receptionist with dissolve
        "I stare at him defiantly as he picks up the phone. In a matter of minutes, two burly guards show up in the office. They each grab a hold of one of my arms and drag me out of the office."
        show guard extra at r2 with dissolve:
            xzoom -1
        pf "Let me go!"
        pf "I can't leave until I get some answers!"
        voice "audio/voice/E4/Donnie/D5/1.ogg"
        don "What is the meaning of this?"
        show donnie ske at l2 with dissolve
        "A tall man dressed in a smart suit blocks the hallway."
        show question:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Donnie/D5/2.ogg"
        don "Why are the guards trying to forcibly remove this young man from the premises?"
        voice "audio/voice/E4/Guard/E4/D5/01.ogg"
        gua "We're just following orders, sir."
        show donnie ann
        voice "audio/voice/E4/Donnie/D5/3.ogg"
        don "I am the order here."
        "The guards look at each other then release me."
        hide guard with dissolve
        voice "audio/voice/E4/Donnie/D5/4.ogg"
        don "Thank you."
        show donnie neu at cc with dissolve
        "The man turns to me."
        voice "audio/voice/E4/Donnie/D5/5.ogg"
        don "What is this all about?"
        "Although he speaks softly, there is a clear air of authority around him. I don't dare act petulantly towards him, especially after he's given me a second chance to get my answers."
        pf "I'm sorry, sir, but I came here looking for an answer to a simple question."
        show donnie ske
        voice "audio/voice/E4/Donnie/D5/6.ogg"
        don "What question?"
        pf "It's in regards to the overdrive core from the ACE Academy match yesterday."
        show donnie neu
        "He studies me."
        voice "audio/voice/E4/Donnie/D5/7.ogg"
        don "You are a student there?"
        pf "Yes, a pilot."
        voice "audio/voice/E4/Donnie/D5/8.ogg"
        don "Come into my office. Perhaps I can help you."
        scene black with fade
        scene bg isokaze office day with fade
        play music "audio/music/Inventory (GAME VERSION).ogg" fadein 8
        "He dismisses the guards and leads me into a private office with large windows. I read the plaque on his desk--which is twice the size of my own--\"Donnie Roos, CEO\"."
        "I glance sharply at him but he doesn't seem to notice. Why is the CEO getting involved with that kind of dispute? He offers me a seat, which I take."
        "Maybe this is some sort of PR stunt… Although he seems helpful, I shouldn't let my guard down."
        show donnie neu at cc with dissolve
        voice "audio/voice/E4/Donnie/D5/9.ogg"
        don "Now, explain to me how I can help."
        "I go through my explanation about the match yesterday and mention who I am. He seems intrigued after hearing my name."
        show donnie cur
        voice "audio/voice/E4/Donnie/D5/10.ogg"
        don "You're the pilot of Eagle?"
        pf "Yes."
        show donnie neu
        voice "audio/voice/E4/Donnie/D5/11.ogg"
        don "Your GEAR caused quite a bit of intrigue in the R&D community with your unique core."
        pf "Then how exactly was Aludian able to possess that technology?"
        show donnie ske
        "He raises an eyebrow as if implying the answer is obvious."
        voice "audio/voice/E4/Donnie/D5/12.ogg"
        don "We partnered with Midori Energy to develop the core. Midori Energy supplied the schematics and of course the Aludian team worked hard to build and refine it."
        "I blink. {w}Midori Energy… does he mean Midori Energy, Inc.? That was Dad's company…"
        show donnie thi
        voice "audio/voice/E4/Donnie/D5/13.ogg"
        don "I'm surprised Dasshu, being an energy drink company, was able to acquire the technology before it went to market."
        "Something very weird is going on here, but I don't think Aludian is involved maliciously."
        pf "Um, yeah, I guess Dasshu has their sources."
        show donnie mis
        "He smiles."
        voice "audio/voice/E4/Donnie/D5/14.ogg"
        don "I don't doubt it."
        # sfx ?
        show donnie cur
        "The phone rings, interrupting our conversation."
        show donnie smi
        voice "audio/voice/E4/Donnie/D5/15.ogg"
        don "I'll have to take this."
        "I nod and stand."
        pf "Thank you very much for meeting with me. I appreciate your time."
        show donnie hap
        voice "audio/voice/E4/Donnie/D5/16.ogg"
        don "You're an interesting pilot. Perhaps our paths will cross again."
        $ persistent.gpix[12][0] = 1
        hide donnie with dissolve
        "He nods in dismissal and answers his phone while I leave his office."
        stop music fadeout 4
        scene black with fade
        "My mind is a whirlwind of questions as I leave the building and head back to my bike. Was dad working on this core for Midori Energy? I'd always thought this was a project for the two of us… but if that's not the case, then maybe they had something to do with--"
        "I shake my head trying to free myself from these thoughts. I can't jump to conclusions. I need to clear my head and calm down."
        play ambient "audio/ambience/Campus Road.ogg" fadein 3
        scene bg campus intersection dusk with fade
        "Maybe someone is free right now. I could use the distraction."
        
        #evening
        $ freeTime = "evening"
        
        call E4FreeTime from _call_E4FreeTime_3
        
        jump E4D5S2
