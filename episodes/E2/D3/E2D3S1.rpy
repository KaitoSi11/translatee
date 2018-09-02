#
label E2D3S1:
    
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
    
    $ day = 3
    $ timeSpent = "none"
    #black bg
    $renpy.pause(2.5)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(2.5)
    #alarm
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    stop sound fadeout 1
    scene bg homekaito myroom day with fade
    
    "I wake up after the first sound of my alarm and hop out of bed."
    "Today is the interview."
    "As I get dressed, I practice my speech in my head."
    scene black with fade
    stop ambient fadeout 5
    "Breakfast goes by in a blur as I try to anticipate what questions they will ask me."
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    scene bg campus auditorium day with fade
    "Before long, I reach the campus. As if in a daze, I go to class and take a seat by the window."
    show professorM extra at cc with dissolve
    voice "audio/voice/E2/D3/S1/profm/1.ogg"
    profm "Good morning, class. I hope you are all prepared for the pop quiz."
    ### VOICE - missing line
    stu2m "Pop quiz?! I didn't hear about a pop quiz!"
    voice "audio/voice/E2/D3/S1/profm/2.ogg"
    profm "You are absolutely right! That is why, young man, it is called a \"pop\" quiz."
    
    stop music fadeout(1)
    "The only person who is amused by that is the professor."
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 3
    hide professorM with dissolve
    "He hands one page out to each student, and soon I am staring at a sheet of questions."
    
    ### NOTE Points - "I think this actually meant to check if you've gotten ever Int check so far"
    if MCStory == 2:
        "I breeze through the quiz. These questions are so easy since the material is a repeat of what I studied at CINY."
        #Automatically max + intel points
    
    else:
        "{i}What is the difference between overheating a core and draining a core{/i}?"
        
        menu:
            "It's the same thing.":
                "I don't feel confident about that answer."
            
            
            "Overheating occurs when a core is utilized too much in a short span of time, while draining a core is when the total energy available is depleted.":
                "That sounds about right!"
            
            "Draining occurs when a core is utilized too much in a short span of time, while overheating a core is when the total energy available is depleted.":
                "I think I might have mixed those up..."
            
            "PICK C, IT'S ALWAYS C.":
                "I go to circle C and realize this isn't a multiple choice question. Curse you pop quiz! I scribble down what I think might be correct, but I doubt it is."
    
    "I spend some time completing the rest of the questions."
    "..."
    "....."
    "With my quiz complete, I hand it in at the front of the class."
    ### VOICE - line missing
    profm "Thank you."
    "I nod and return to my seat. The professor waits for the rest of the class to finish before beginning the lesson."
    
    #Fade black
    scene black with fade
    $renpy.pause(2.5)
    scene bg campus auditorium day with fade
    $renpy.pause(1)
    
    show professorM extra at cc with dissolve
    
    voice "audio/voice/E2/D3/S1/profm/3.ogg"
    profm "That's all for today. Have a good afternoon."
    
    play sound "audio/sfx/Human/Class End.ogg"
    
    stop ambient fadeout 3
    stop music fadeout 3
    
    "As soon as class is dismissed, I rush out of the building."
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus main day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    "I'm not sure why I'm in such a hurry. I still have a few hours before I need to meet Yuuna. {w}I wonder what I should do to pass the time."
    
    $ freeTime = "afternoon"
    
    call E2FreeTime from _call_E2FreeTime_4
    
    jump E2D3S2
