#
label E2VBS1:
    
    # Event 1 - Afternoon Choice (>30 Points AND NOT DAY4)
    
    "I should spend some time on my studies, but I don't want to be cooped up inside when it's such a nice day out."
    "Taking a stroll through campus, I find an isolated bench near the campus cafe and pull out my tablet. {w}Maybe I'll take a look at my first assignment for my Foreign Exchange International Bridging class."
    "I log into my weblink, but can't find the tab for my class… {w}Maybe the professor hasn't set it up yet? I wonder if anyone else is having trouble."
    "Good thing that Valerie girl gave me her number in class. {w}I find it in my phone and give her a call."
    stop music fadeout 3
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "She answers the phone almost immediately."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    
    if day < 3:
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO1.ogg"
        vb "Oh my, someone's eager! Aren't you supposed to wait three days before calling a girl?"
        
        menu:
            "I've never heard of that rule before.":
                pf "Really? But I've always called a girl when I needed her."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO2.ogg"
                vb "Oooh, you need me?"
                pf "Yes, I need help."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO3.ogg"
                vb "The answer is yes."
                pf "I haven't asked you yet."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO4.ogg"
                vb "Sorry, go ahead."
        
            "Don't flatter yourself.":
                pf "I only reserve that for the pretty girls."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO5.ogg"
                vb "Am I not pretty?"
                pf "Well, I called you didn't I?"
                vb "..."
                "The line goes silent."
                "Ladies can't resist bad-boys and jerks. She must be swooning over my manly charm."
                pf "Anyway, I have a question for you."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO6.ogg"
                vb "Okay…"
        
            "I didn't call to play games.":
                pf "Okay."
                play sound2 "audio/sfx/Technology/Phone Answer.ogg"
                "I hang up the phone. I don't want to play her stupid mind-games. I have an assignment I need to do."
                "I log back into my weblink, but the class tab still doesn't show up."
                "... Damn. {w}I don't want to fail my first assignment..."
                "With a deep sigh, I redial Valerie's number."
                play sound "audio/sfx/Technology/Phone Dial.ogg"
                $renpy.pause(2.5)
                play sound "audio/sfx/Technology/Phone Dial.ogg"
                $renpy.pause(2.5)
                play sound2 "audio/sfx/Technology/Phone Answer.ogg"
                "She let's the phone ring for a while, then answers."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO7.ogg"
                vb "Two phone calls in under half an hour? That's a little desperate."
                pf "I called you for a reason."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO8.ogg"
                vb "And that is?"
                
    else:
        voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO9.ogg"
        vb "{b}Allô?{/b}"
        
        menu:
            "Bonjour!":
                pf "{b}Bon-jour~!{/b}!"
                "She giggles at my attempt."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO10.ogg"
                vb "Your accent is adorable!"
                pf "{b}Oui oui, mademoiselle.{/b}."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO11.ogg"
                vb "Hehe! What's up?"
            
            "No hablo.":
                pf "{b}Me no hablo francés.{/b}."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO12.ogg"
                vb "That's spanish."
                pf "sí."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO13.ogg"
                vb "... I speak French."
                pf "sí, señorita."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO14.ogg"
                vb "Nevermind. What's up?"
                
            "I don't speak French.":
                pf "I don't understand French."
                voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO15.ogg"
                vb "Oh sorry, force of habit. What's up?"
    
    pf "Are you able to access the Foreign Exchange International Bridging class's weblink?"
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO16.ogg"
    vb "... This is why you called me?"
    pf "Why else would I call?"
    "She sighs."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO17.ogg"
    vb "Hold on, let me log in."
    "I wait in silence while she types on the line."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO18.ogg"
    vb "Yeah, I can see it. Why?"
    pf "What's the assignment?"
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO19.ogg"
    vb "The professor wants us to go off-campus and explore the city of Isokaze."
    "She pauses, then her voice turns into silk."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO20.ogg"
    vb "Ohhh, now I understand why you called." 
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO21.ogg"
    vb "Yes, I would love to."
    pf "What? Love to what?"
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO22.ogg"
    vb "Be your partner!"
    pf "Partner?{w} … Like for life?"
    "She laughs."
    ##LINEMISSING##
    voice "audio/voice/E2/missing/valerie/1.ogg"
    vb "Slow your roll, mister. We haven't even gone on a date yet."
    pf "So partner for…?"
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO23.ogg"
    vb "Partner for the project, silly. We can work in pairs."
    pf "Oh."
    "Exploring the city with another person would make it more fun than going alone."
    pf "Sure, yeah, let's do that."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO24.ogg"
    vb "Great! When do you want to get together?"
    pf "How about this weekend."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO25.ogg"
    vb "It's a date!"
    pf "Uh, no it isn't."
    voice "audio/voice/E2/Free/VB/ValerieEP2VALERIEARCREDO26.ogg"
    vb "We'll meet at the park. See you then!"
    pf "It's not a date--"
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    "She hangs up before I can finish. {w}I really hope she was joking about that."
    $ E2VBS1_Completed = 1
    
    stop ambient fadeout 3
    stop music fadeout 3
    scene black with fade
    $renpy.pause(1)
    #end
