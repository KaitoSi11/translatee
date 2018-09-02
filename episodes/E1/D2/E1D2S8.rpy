label E1D2S8:
    
    stop music fadeout 5
    if (E1D2S2_YuunaComesWithYouPass == 0):
        #Yuuna's scene already puts you next to building. This is the filler to introduce building BG from Kaori / parking / Mayu...etc
        scene bg campus main day with fade
        "I pull up the map of the campus on my phone. Luckily, the routes are easy to follow and I’m soon standing before the auditorium. {w}Thank god for technology."
    stop ambient fadeout 3
    scene black with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 1
    scene bg campus auditorium day with fade
    "I take a deep breath, steeling my nerves, and firmly push open the doors to the auditorium. {w}After a quick scan of the room, I select a seat near the back. I can tell this is a first year introductory class based on how spread out the students are and how quiet the room is."
    "I hate that I have to take intro classes again. Some of my electives from CINY did not \"encompass the full scope of course material\". Whatever that means."
    
    "A hush blankets the auditorium as a man strides to the front of the room."
    show professorM extra at cc with dissolve
    voice "audio/voice/E1/D2/S8/Prof/1.ogg"
    profm "Good morning. This is Piloting 101. Is everyone where you are supposed to be?"
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 3
    "The professor waits patiently as a handful of students shuffle towards the nearest exit. I yawn and watch them leave with disinterest."
    play sound "audio/sfx/Technology/Phone Projection.ogg" fadein 1
    "He drags a webpage from his tablet onto the screen behind him."
    voice "audio/voice/E1/D2/S8/Prof/2.ogg"
    profm "This is the class weblink. Consider this portal as your lifeline for the course. You will find all your assignments and readings here. As well as your current grade in the course. You can find my contact information in the tab marked \"Contact\". My office hours are listed so please do not hesitate to stop by. Even I get lonely at times and I appreciate visitors."
    
    "That comment got a couple of weak chuckles from the room."
    
    menu:
        "He is thorough.":
            "Most students don't pay attention to these introductions but there’s nothing a professor dislikes more than a student who asks a question he’s already answered."
    
        "This is so boring.":
            "I've heard this speech about a million times now. Although the professors change, the speech never does."
            
        "{color=#00ff00}{b}Memorize the information.{/b}{/color}" if (MCStory == 2):
            "I automatically store the information into my memory."
    voice "audio/voice/E1/D2/S8/Prof/3.ogg"
    profm "Now that we’ve gotten all of the boring stuff out of the way, I’m sure you’re all eager to learn more about the qualifier exams on Friday."
    
    "The class visibly perks up."
    voice "audio/voice/E1/D2/S8/Prof/4.ogg"
    profm "The qualifier exam will not only register you as an active pilot, but will also provide you with your team ranking. I’m sure you’ve already picked out your teams by now, but I’d still like to remind you all that each team must have a minimum of four people in order to qualify." 
    
    "A hand shoots up from the middle of the room."
    
    show studentM extra at r3 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D2/S8/Prof/5.ogg"
    profm "Yes?"
    voice "audio/voice/E1/D2/S8/FirstYearStudent/1.ogg"
    stu7m "Are you sure exams are this Friday? That only gives us two days to find a team..."
    
    "Soft snickers fill the room. The student visibly shrinks from all of the eyes now focused on him."
    voice "audio/voice/E1/D2/S8/Prof/6.ogg"
    profm "The majority of students who begin their first year here at Ace Academy are aware of the timeline for the qualifier exams and use their summers to form a team and prepare. In the past, we had extended the preparation time before the exam, but found that the majority of students did not need nor want the extra days. So we adjusted our schedules accordingly."
    voice "audio/voice/E1/D2/S8/FirstYearStudent/2.ogg"
    stu7m "But what about those of us who didn’t know about the qualifier ahead of time? What do we do?"
    voice "audio/voice/E1/D2/S8/Prof/7.ogg"
    profm "I suggest you get to work finding yourself a team. Any other questions?"
    
    "The student scowls but shakes his head."
    
    hide studentM extra with dissolve
    voice "audio/voice/E1/D2/S8/Prof/8.ogg"
    profm "Good. The qualifier exam will pit your team's starting four against four AI GEARS. You will then be assigned a ranking based upon your overall performance relative to the other teams. Don't worry if you can't defeat all the AI GEARS. They are programmed to be extremely difficult to beat."
    voice "audio/voice/E1/D2/S8/Prof/9.ogg"
    profm "Please ensure your GEAR is in pristine condition for battle. All exams are demonstrated live instead of in a simulator to most accurately gauge ability."
    voice "audio/voice/E1/D2/S8/Prof/10.ogg"
    profm "Any questions?"
    
    "He is answered with silence."
    show note:
        xoffset 675
        yoffset 50
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S8/Prof/11.ogg"
    profm "Let’s get started then."
    
    #Screen fade black
    scene black with fade
    $renpy.pause(1)
    #Screen back to classroom
    scene bg campus auditorium day with fade
    show professorM extra at cc with dissolve
    voice "audio/voice/E1/D2/S8/Prof/12.ogg"
    profm "Please check the weblink for your assignments and have them complete for the next class. Welcome to Ace Academy. I hope you all have a great rest of the day."
    hide professorM extra with dissolve
    play sound "audio/sfx/Human/Class End.ogg"
    stop ambient fadeout 3
    stop music fadeout 3
    "A thunder of chairs scrape along the floor as students file out of the class. Those who remain chat animatedly in small groups."
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    play ambient "audio/ambience/Campus.ogg" fadein 1
    "Yawning, I wait for the crowd in front of the door to thin before making my way out of the room. Once I'm by the door, a snippet of a nearby conversation catches my attention."
    show studentM extra at l2 with dissolve
    voice "audio/voice/E1/D2/S8/stu7m/1.ogg"
    stu7m "Hey, did you see what they brought into the hangar today?"
    show studentM2 extra at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E1/D2/S8/stu8m/1.ogg"
    stu8m "Yeah, that ancient looking thing? Hah. I'll be amazed if it still works. Where the hell do you even find something like that? I bet they fished it out of the ocean!"
    
    "The students laugh loudly." 
    hide studentM extra
    hide studentM2 extra
    with dissolve
    "... I have a sinking feeling I know what they're talking about..."
    scene bg campus main day with fade
    "As I hurry out of the classroom, I check my phone and am excited to see an email notification. I eagerly read through the email. It's just a note letting me know my GEAR has been registered and I now have access to the hangar."
    
    "Well, that certainly makes things easy for me. At CINY, I spent {i}days{/i} going through the registration process. We had to submit all of the paperwork ourselves, and of course, nobody in the administrative office was ever helpful."
    
    "Satisfied, I put away my phone and make my way to the hangar."
    
    if (E1D2S4_MayuGaveDirections == 1):
        scene black with fade
        stop music fadeout 3
        stop ambient fadeout 3
        scene bg campus lounge day with fade
        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
        "Before long, I'm back in the Pilot's Lounge and head directly towards the guard. Without looking up from his holobook, he gestures towards the card reader."
        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
        "I tap my ID and hold my breath. The reader beeps affirmatively and the door slides open. I quickly step through."
        stop ambient fadeout 3
    
    else:
        "I bring up the map on my phone and touch the hangar, which lights up. Soon, pulsating lights dot the path from my current location to the hangar."
        scene black with fade
        stop music fadeout 3
        stop ambient fadeout 3
        play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
        "It's a bit of a trek away from the heart of the campus, but I make good time. I scan my ID and walk in."
        stop ambient fadeout 3
    
    jump E1D2S9
