label E1D5S6:

"I wonder what Mayu is up to."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"I dial her number..."
play sound "audio/sfx/Technology/Phone Answer.ogg"
"...and she answers almost immediately."
voice "audio/voice/E1/D5/S6/Mayu/1.ogg"
ma "Hello?"
pf "Uh, hi. It's [pfirst]."
voice "audio/voice/E1/D5/S6/Mayu/2.ogg"
ma "Oh, hi."
pf "Hi."
voice "audio/voice/E1/D5/S6/Mayu/3.ogg"
ma "...Hi."
"We pause."

stop music fadeout 3.0
menu:
    "... I didn't think this through.":
        pf "... So, uh… How are you?"
        voice "audio/voice/E1/D5/S6/Mayu/4.ogg"
        ma "Good, thank you, and you?"
        pf "Good, good."
        voice "audio/voice/E1/D5/S6/Mayu/5.ogg"
        ma "..."
        "I can practically hear her confusion."
        voice "audio/voice/E1/D5/S6/Mayu/6.ogg"
        ma "Um... are you looking for Shou?"
        pf "Uh, well--"
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3.0
        "I'm interrupted by a clamouring in the background and can make out a muffled Shou."
        voice "audio/voice/E1/D5/S6/Shou/4.ogg"
        ss "Me? Is it for me?"
        "His voice becomes clear."
        voice "audio/voice/E1/D5/S6/Shou/5.ogg"
        ss "Sup, broseph!"
        pf "Oh hey, Shou. Are you and Mayu hanging out?"
        voice "audio/voice/E1/D5/S6/Shou/6.ogg"
        ss "Yeah, we're just at the cafe getting our nom on. Come join us!"

        menu:
            "No, thanks.":
                $ E1D5S1_EventMayu = 0
                $ E1D5S6_MayuNoThanksLoop = 1
                pf "It sounds like you two are having a good time and I don't want to intrude."
                voice "audio/voice/E1/D5/S6/Shou/7.ogg"
                ss "You won't intrude!"
                pf "Thanks, but I'll pass. Maybe another time."
                voice "audio/voice/E1/D5/S6/Shou/8.ogg"
                ss "Okay, talk to you later!"
                stop music fadeout 5.0
                pf "Bye."
                "Well, that didn't work out. I wonder if anyone else is free."
                jump E1D5S1_WeekendChoiceSelection

            "Sure!":
                pf "You don't mind?"
                voice "audio/voice/E1/D5/S6/Shou/9.ogg"
                ss "No way! The more the merrier!"
                pf "Cool, I'll be right over."
                voice "audio/voice/E1/D5/S6/Shou/10.ogg"
                ss "See you soon!"
                "We hang up, and I head to my bike."
                stop music fadeout 3.0
                stop ambient fadeout 3.0
                scene black with fade
                jump E1D5S5_ConvergenceFromMayuCall

jump E1D5S7