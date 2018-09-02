#
label E2D4S1:
    
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
    
    $ day = 4
    $ timeSpent = "none"
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    "I wake up and yawn. Another day, another class."
    stop sound fadeout 1.0
    "As if on autopilot, I get dressed and go through my morning routine. Then I hop on my bike and drive to school."
    stop ambient fadeout 3
    $renpy.pause(1)
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus auditorium day with fade
    "When I arrive, I head straight for class and wait for the professor. {w}He arrives promptly and begins class."
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    show professorM extra at cc with dissolve
    ### VOICE - the VA says "military grenade weaponry"
    voice "audio/voice/E2/D4/S1/prof1m/1.ogg"
    prof1m "Good morning. Today, we'll be discussing the differences between military grade weaponry and those used for recreational matches."
    
    menu:
        "Yaaawn! I already know this.":
            #+Athletic
            "This material is simple stuff. Time for a discreet power nap."
            scene black with fade
            "..."
            "What is this weird feeling? It's like somebody's watching me..."
            scene bg campus auditorium day with fade
            "I open my eyes and see the entire class watching me."
            show professorM extra at cc with dissolve
            pf "..."
            pf "Uh."
            voice "audio/voice/E2/D4/S1/prof1m/6.ogg"
            prof1m "During that specific qualifier match, the GEAR's energy core is what surged with additional power, not his weapons."
            "I feel like I might have missed something important."
        
        "I want to learn!":
            #+Intel
            "This should be interesting stuff! I focus on the professor's lecture."
            voice "audio/voice/E2/D4/S1/prof1m/2.ogg"
            prof1m "The fundamental difference between the two is that military grade weaponry are configured for energy output which can cause lethal damage."
            voice "audio/voice/E2/D4/S1/prof1m/3.ogg"
            prof1m "Recreational weaponry is closely regulated so it can't actually destroy the GEAR frame."
            voice "audio/voice/E2/D4/S1/prof1m/4.ogg"
            prof1m "Since the shields on a GEAR get the brunt of the damage, we consider a \"de-powered\" GEAR in recreational matches as \"destroyed\"."
            voice "audio/voice/E2/D4/S1/stu2m/1.ogg"
            stu2m "What if someone brought in an unregulated weapon for a match?"
            voice "audio/voice/E2/D4/S1/prof1m/5.ogg"
            prof1m "Before every match, the equipment of each GEAR is checked and double checked to ensure its energy output is within the proper parameters."
            voice "audio/voice/E2/D4/S1/stu2m/2.ogg"
            stu2m "What about the qualifier matches? There was a GEAR that did some energy output override thing."
            "As one, the class looks at me."
            pf "Uh."
            voice "audio/voice/E2/D4/S1/prof1m/6.ogg"
            prof1m "During that specific qualifier match, the GEAR's energy core is what surged with additional power, not his weapons."
            
    voice "audio/voice/E2/D4/S1/prof1m/7.ogg"
    prof1m "Although I must admit, I've never seen a core do that before. Hopefully this young man can enlighten us as to how he did it."
    
    menu:
        "I have no idea how I did it.":
            pf "Uh, to be honest, I'm still trying to figure that out."
            voice "audio/voice/E2/D4/S1/prof1m/8.ogg"
            prof1m "Hmm, interesting."
            voice "audio/voice/E2/D4/S1/prof1m/9.ogg"
            prof1m "Perhaps once you've figured it out you'd be inclined to share with us what happened. Until then, let's get back to the lesson plan. I'm sure you all don't want to waste time on something that won't be on the exam anyway."
            "The class lets out a weak chuckle. Most refocus their attention on the professor, but a few students continue to look at me with interest."
        
        "No one finds out my secret!":
            pf "Nice try. Our team isn't giving up that information."
            "The class looks disappointed, but the professor grins."
            voice "audio/voice/E2/D4/S1/prof1m/10.ogg"
            prof1m "Smart move. Don't give away your advantage."
            voice "audio/voice/E2/D4/S1/prof1m/11.ogg"
            prof1m "Let's get back to the lesson."
        
        "Why are you talking about my core?":
            pf "I thought this lesson was about military versus recreational weaponry. Why are we talking about me?"
            "The class looks disappointed. However, the teacher nods."
            voice "audio/voice/E2/D4/S1/prof1m/12.ogg"
            prof1m "Of course, we shouldn't get distracted. Let's get back to the lesson on hand."
    
    "He returns to his lecture."
    #black screen
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Human/Class End.ogg"
    stop ambient fadeout 3
    "Once class ends, I hurry out of the room."
    play ambient "audio/ambience/Campus.ogg" fadein 11
    scene bg campus main day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    "My phone is already in my hand by the time I get outside. {w}Let's see if anyone's free."
    
    $ freeTime = "afternoon"
    
    call E2FreeTime from _call_E2FreeTime_7
    
    jump E2D4S2
