label E2MAS4:


$ mayOut = "sFashion"
"I wonder if Mayu is free today. I'm still really curious as to how she is on the violin."

play sound "audio/sfx/Technology/Phone Dial.ogg"
"Taking my phone out of my pocket, I tap Mayu's name."

play sound "audio/sfx/Technology/Phone Answer.ogg"
"She answers only after one ring."

voice "audio/voice/E2/Free/MA/S4/0-01.ogg"
ma "Hello?"
pf "Hey, Mayu."

menu:
    "See if she's free to play for me today.":
        pf "I was just calling to see if you're free today."
        voice "audio/voice/E2/Free/MA/S4/0-02.ogg"
        ma "Not at the moment."
        pf "Oh..."
        voice "audio/voice/E2/Free/MA/S4/0-03.ogg"
        ma "W-Wait! I mean I'm not free because I was just about to call you."
        pf "Really?"
        voice "audio/voice/E2/Free/MA/S4/0-04.ogg"
        ma "Yes. I promised I'd play for you this weekend so that's what I'm going to do."
        "Wow, she doesn't take her promises lightly. That being said, I'm really excited to finally hear Mayu play the violin!"

    "Cash in on the \"private show\"!":
        pf "I was calling to see if we're still good to do our one-on-one session."
        voice "audio/voice/E2/Free/MA/S4/0-05.ogg"
        ma "Of course, I made you a promise and I have to keep it."
        "I think my {i}suggestive{/i} choice of words flew right over her head. {w}On another note, I'm excited to hear her play!"

    "I hope you haven't forgotten about your promise.":
        pf "Do I get to hear you play the violin today?"
        voice "audio/voice/E2/Free/MA/S4/0-06.ogg"
        ma "Yes of course. I made a promise!"
        pf "Well, it's awesome that you're following through on your word."
        voice "audio/voice/E2/Free/MA/S4/0-07.ogg"
        ma "I always keep my promises."

pf "Alright. Do you want to meet in the music room on campus?"
voice "audio/voice/E2/Free/MA/S4/0-08.ogg"
ma "Okay! I'll head over right now."
pf "Great, me too. I'll be there in a few--"
"..."
"Did she just hang up on me?"
play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
$renpy.pause(1)
"Bzzt! {w} {i}Mayu Akemi{/i} flashes across my phone."
play sound "audio/sfx/Technology/Phone Answer.ogg"
$renpy.pause(1)
pf "Hello?"
voice "audio/voice/E2/Free/MA/S4/0-09.ogg"
ma "I-I'm so sorry for hanging up! I meant to say \"okay\", but I just nodded my head instead..."
"I suppress a chuckle. She sounds so cute when she's flustered."
pf "It's okay."
voice "audio/voice/E2/Free/MA/S4/0-10.ogg"
ma "Sorry again...Um... I'll see you soon!"
pf "Alright, see you."
"There are a couple of awkward seconds of silence before she finally hangs up. I guess she was making sure not to cut me off this time. Sometimes I wonder if she is too polite for her own good."
"Time to head out."

#((Back to day 6))
jump E2D6S1_Nikki

label E2MAS4_Continued:
    #((Back with bike on campus))
    
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    "I arrive on campus and park as far away as I can."
    
    "There is absolutely no way I want to be caught riding my bike while it looks like {i}that{/i}."
    
    
    play ambient "audio/ambience/Campus.ogg" fadein 3
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    scene bg campus main day with fade
    
    "It's quite a jog before I arrive on the main campus quad."
    
    
    
    if MCStory == 1:
        "But I easily covered the distance with time to spare."
    
    else:
        "I'm breathing heavily and feel warm by the time I arrive, so I take a few deep breaths to cool down."
    
    
    "Pulling up the campus map on phone, I plot out the route for the music rooms and make my way to the cluster of liberal arts buildings, then enter the music hall."
    
    stop ambient fadeout 3
    scene black with fade
    
    "The first two practice rooms are empty, while the third one has a petite girl with her back facing the door. {w}That's Mayu!"
    
    scene bg campus library day with fade
    "She hasn't noticed me at the entrance yet..."
    
    menu:
        "Greet her.":
            pf "Hey, Mayu."
            
            show mayu smi at cc with dissolve
            "She cautiously turns towards the door but smiles when she sees me."
            voice "audio/voice/E2/Free/MA/S4/0-11.ogg"
            ma "Hi."
            "After offering a wave, I walk towards her."
    
        "SNEAK ATTACK!":
            stop music fadeout 2
            "Time to bring out my inner ninja!"
            play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 2
            "I crouch down and tip-toe over to Mayu. My steps are inaudible due to my past training as a covert operative, the details of which I cannot narrate."
            pf "Boo!"
            show frightful:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur b1 at cc with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-12.ogg"
            ma "Ahh!"
            show mayu win b1 at cc, Shake(None, .5, dist=5)
            "Mayu squeals in surprise as she jumps away from me."
            show mayu wor b1 with dissolve
            "Realising it's just me, she presses a hand over her chest."
            voice "audio/voice/E2/Free/MA/S4/0-13.ogg"
            ma "D-Don't do that...!"
            
            if E1D2S4_MayuGaveDirections == 1:
                show mayu sad b1
                voice "audio/voice/E2/Free/MA/S4/0-14.ogg"
                ma "This is the second time now!"
                
            "She's breathing heavily. I can't help but feel a little guilty."
            pf "Sorry."
            show mayu dis b1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-15.ogg"
            ma "It's okay..."
            "Her voice doesn't sound very convincing. As her body tension releases, I can see something gripped in her hand."
            pf "What's that?"
            show mayu neu b1 with dissolve
            "Mayu opens her hand revealing a small canister of pepper spray."
            pf "Well, that could have ended badly."
            "My eyes feel itchy just from looking at it."
            voice "audio/voice/E2/Free/MA/S4/0-16.ogg"
            ma "It's for emergencies... just in case..."
            pf "Yeah I get that. I'm just {i}really{/i} glad your first reaction was not to spray it."
            "She tucks it away in her pocket."
            stop music fadeout 5
            voice "audio/voice/E2/Free/MA/S4/0-17.ogg"
            ma "It used to be, but Shou's been on the receiving end a few times."
            pf "A few times...?"
            show mayu thi b1
            "Mayu sighs."
            voice "audio/voice/E2/Free/MA/S4/0-18.ogg"
            ma "You think he'd learn...I just use it more carefully now."
            "Thank goodness for Shou's shenanigans. {w}In any case, I'm just glad that Mayu seems more relaxed now."
            play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    
    "Her instrument is already unpacked and her music is on the stand."
    pf "I'm surprised by how fast you set everything up."
    show mayu ner b1 with dissolve
    voice "audio/voice/E2/Free/MA/S4/0-19.ogg"
    ma "O-Oh, I got here as soon as we hung up to practice..."
    pf "Practice?"
    voice "audio/voice/E2/Free/MA/S4/0-20.ogg"
    ma "Yes. I haven't played for anyone outside of family so I got a little nervous and wanted to practice."
    pf "I mean, you're just playing for me... it's nothing serious."
    show mayu ann b1
    voice "audio/voice/E2/Free/MA/S4/0-21.ogg"
    ma "It is!"
    show mayu sur b1 with dissolve
    $renpy.pause(.66)
    show mayu ner b1 with dissolve
    "Mayu blinks after realising she raised her voice. She looks down meekly and shuffles her feet."
    voice "audio/voice/E2/Free/MA/S4/0-22.ogg"
    ma "I mean, it's my first time."
    
    menu:
        "I believe in you.":
            pf "Just pretend like it's a practice session and I'm not even here!"
            
            if E2D5MA_MayuScene == 1:
                show mayu cur b1
                pf "Like in the Herry Podder books, this is my veil of invisibility!"
                "I pretend to put a cape over myself."
                show mayu smi b1
                "Mayu giggles."
    
            else:
                show mayu smi b1
                "Mayu smiles."
                voice "audio/voice/E2/Free/MA/S4/0-23.ogg"
                ma "Okay, I'll try that."
    
    
        "...Your choice of words...":
            pf "Your {i}first time{/i}?"
            show mayu neu b1
            voice "audio/voice/E2/Free/MA/S4/0-24.ogg"
            ma "Yes."
            $renpy.pause(.33)
            show mayu sur b1 with dissolve
            $renpy.pause(.66)
            show mayu ner b2 with dissolve
            "Her cheeks turn red and she looks away."
            voice "audio/voice/E2/Free/MA/S4/0-25.ogg"
            ma "I-I mean f-first time playing for an audience!"
            "I smirk at her reaction."
    
        "Let's hear it.":
            pf "There's a first time for everything."
            show mayu neu b1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-26.ogg"
            ma "Okay, I'll give it a shot."
            "Her voice doesn't match the confidence in her words."
    
    stop music fadeout 1.5
    show black with fade
    hide mayu

    show cg mayu violin 1 with fade:
        xzoom .5
        yzoom .5
    "I take a seat on a nearby piano bench and watch as she readies her violin and bow."
    "She still looks a little nervous and re-tunes her violin to help her relax.{w} Once content, she closes her eyes and begins playing."
    $ persistent.gpix[37][0] = 1
    $ persistent.gpix[38][0] = 1
    $ persistent.gpix[39][0] = 1
    $ persistent.gpix[40][0] = 1
    $ renpy.pause(.5)
    show cg mayu violin 2 with dissolve
    $renpy.pause(1.0)
    play sound "audio/sfx/UI or Plot Element/MayuViolin.ogg" fadein 2
    
    $ renpy.pause(3, hard=True)
    "I'm listening to her music...{p=26.5}...?"
    
    stop sound fadeout .33
    $renpy.pause(.66)
    
    "She stops abruptly."
    
    show cg mayu violin 3 with dissolve
    "Mayu opens her eyes and looks dejected."
    
    voice "audio/voice/E2/Free/MA/S4/0-27.ogg"
    ma "I'm sorry! That must have sounded so awful! I made so many mistakes..."
    
    if MCStory == 2:
        "There were a few notes out of place but it wasn't noticeable unless you were really listening for it."
    
    else:
        "It sounded pleasing to me..."
    
    "Maybe her nerves are affecting her performance."
    
    menu:
        "You were awesome!":
            pf "What do you mean? I thought you were wonderful!"
            show cg mayu violin 1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-28.ogg"
            ma "You're just saying that to make me feel better."
            pf "No, really! From a technical standpoint, your playing is brilliant! You've inspired me…"
            "I flip around and face the piano."
            pf "Let's do it again…together."
            "Mayu blinks in surprise, but nods."
    
        "You need to put your heart into it." if (MCStory != 2):
            pf "You played it well, but you were missing a {i}key{/i} component."
            "Mayu looks up at me with curiosity."
            voice "audio/voice/E2/Free/MA/S4/0-29.ogg"
            ma "I was?"
            pf "Yes, your heart and soul!"
            "She blinks, unsure what I mean."
            pf "Don't get me wrong, the performance was near perfect from a technical standpoint, but music is an art. You need to {i}feel{/i} it. Let the music share what you can't put into words."
            show cg mayu violin 1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-30.ogg"
            ma "I'm sorry, I don't follow..."
            "I turn to face the piano."
            pf "Once more, from the top!"
            show cg mayu violin 3 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-31.ogg"
            ma "O-Okay!"
    
        "{color=#00ff00}{b}You need to put your heart into it.{/b}{/color}" if (MCStory == 2):
            pf "You played it well, but you were missing a {i}key{/i} component."
            "Mayu looks up at me with curiosity."
            voice "audio/voice/E2/Free/MA/S4/0-29.ogg"
            ma "I was?"
            pf "Yes, your heart and soul!"
            "She blinks, unsure what I mean."
            pf "Don't get me wrong, the performance was near perfect from a technical standpoint, but music is an art. You need to {i}feel{/i} it. Let the music share what you can't put into words."
            show cg mayu violin 1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-30.ogg"
            ma "I'm sorry, I don't follow..."
            "I turn to face the piano."
            pf "Once more, from the top!"
            show cg mayu violin 3 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-31.ogg"
            ma "O-Okay!"
            
            
        "Let's do round two.":
            "I swivel around on the bench and face the piano."
            pf "Play that song again."
            "Mayu's eyes widen in surprise."
            voice "audio/voice/E2/Free/MA/S4/0-32.ogg"
            ma "E-Eh?"
            pf "Trust me, just play it."
            show cg mayu violin 1 with dissolve
            voice "audio/voice/E2/Free/MA/S4/0-33.ogg"
            ma "Okay..."
    
    
    "My fingers hover over the piano keys as I glance back at Mayu."
    show cg mayu violin 1 with dissolve
    "She nods at me and readies her violin."
    
    
    $renpy.pause(.5)
    show cg mayu violin 2 with dissolve
    $renpy.pause(1.0)
    play sound "audio/music/Mayu Akemi (GAME VERSION).ogg" fadein 2
    
    $ renpy.pause(3, hard=True)
    "We play music together...{p=61}...!"
    
    stop sound fadeout .33
    $renpy.pause(.66)
    
    show cg mayu violin 1 with dissolve
    "The music fades to an end, as we stare silently at each other. While there are no words, I feel the bond between us grow stronger."
    
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show cg mayu violin 4 with dissolve
    voice "audio/voice/E2/Free/MA/S4/0-34.ogg"
    ma "You were incredible!"
    pf "{i}We{/i} were incredible."
    "Mayu beams and nods."
    
    hide cg mayu with fade
    
    hide black with fade
    
    show mayu smi b1 at cc with dissolve
    voice "audio/voice/E2/Free/MA/S4/0-35.ogg"
    ma "I didn't know you could play the piano so well."
    
    menu:
        "{i}Your{/i} violin made it sound good.":
            pf "I was really just playing off of you. I wouldn't sound nearly as good without you leading."
            show regBlush:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            "Mayu blushes shyly."
            voice "audio/voice/E2/Free/MA/S4/0-36.ogg"
            ma "I don't know about that..."
    
        "Just another one of my talents.":
            "I grin confidently."
            pf "Beginners luck I suppose."
            show exclamation:
                xoffset 720
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu sur b1 with dissolve
            "Mayu's eyes widen."
            voice "audio/voice/E2/Free/MA/S4/0-37.ogg"
            ma "That's really impressive!"
            "I chuckle."
            pf "I'm kidding. I used to play duets with my sister when we were younger."
            show mayu smi b1
            voice "audio/voice/E2/Free/MA/S4/0-38.ogg"
            ma "Oh."
            pf "Speaking of hidden gifts..."
    
        "It's from practicing.":
            pf "I used to practice a lot when I was younger." 
    
            if MCStory == 2:
                pf "Now I usually play alone to relax."
                voice "audio/voice/E2/Free/MA/S4/0-39.ogg"
                ma "It's peaceful."
                "We both nod. {w}She understands exactly what I mean."
    
            else:
                pf "I don't play much anymore, but I guess the basic skills are still there."
                show mayu hap b1
                voice "audio/voice/E2/Free/MA/S4/0-40.ogg"
                ma "You're very talented!"
                pf "Nah, not as talented as you."
                show regBlush:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu smi b1 with dissolve
                "Mayu blushes."
    
    pf "Have you ever considered playing as part of an orchestra?"
    show mayu smi b1
    "To my surprise, Mayu nods."
    voice "audio/voice/E2/Free/MA/S4/0-41.ogg"
    ma "Actually, when I was in high school I was invited to audition for a spot in our local community symphony orchestra."
    pf "That's amazing! How did you do?"
    stop music fadeout 10.0
    show mayu ner b1 with dissolve
    "She looks away."
    voice "audio/voice/E2/Free/MA/S4/0-42.ogg"
    ma "I didn't audition..."
    pf "Why not?"
    voice "audio/voice/E2/Free/MA/S4/0-43.ogg"
    ma "It's just not something I could have done."
    pf "Because you'd never played in front of people?"
    show mayu neu b1
    voice "audio/voice/E2/Free/MA/S4/0-44.ogg"
    ma "No--I mean, sort of. I was nervous about that too, but mostly it was because I knew my father would never approve."
    pf "Did you ask him?"
    show mayu sur b1 with dissolve
    "Her eyes grow wide at the suggestion, and she emphatically shakes her head."
    show panic:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/MA/S4/0-45.ogg"
    ma "Of course not!"
    pf "Why not?"
    show mayu sad b1 with dissolve
    "She sighs."
    voice "audio/voice/E2/Free/MA/S4/0-46.ogg"
    ma "Akemis are pilots. It's in our blood and it's what we are born to do."
    pf "But is that what {i}you{/i} want to do?"
    show mayu cur b1
    "Mayu blinks at me."
    voice "audio/voice/E2/Free/MA/S4/0-47.ogg"
    ma "What do you mean?"
    pf "Is a GEAR pilot what you want to be?"
    show mayu neu b1
    voice "audio/voice/E2/Free/MA/S4/0-48.ogg"
    ma "Yes, I've never considered anything else."
    pf "What about being a musician? The fact that you were asked to audition for a professional orchestra proves you have the talent."
    voice "audio/voice/E2/Free/MA/S4/0-49.ogg"
    ma "Music is important for a well-rounded education, and it keeps the mind sharp, but it's not a profession."
    pf "Of course it's a profession! Think of all the musical geniuses in the past… the composer who put together the music we just played--"
    show mayu ann b1 with dissolve
    voice "audio/voice/E2/Free/MA/S4/0-50.ogg"
    ma "It just couldn't happen!"
    $renpy.pause(.66)
    show mayu ner b1 with dissolve
    "Mayu blushes at her outburst."
    voice "audio/voice/E2/Free/MA/S4/0-51.ogg"
    ma "Besides, I probably wasn't good enough to earn the seat in the orchestra anyway."
    
    if MCStory == 3:
        "She looks away and speaks quickly, as if blurting an afterthought. I can tell this is her way of justifying passing up the audition."
    
    else:
        pf "I don't believe that."
        "She looks away and shrugs. {w}Maybe this isn't what she needed to hear from me."
    
        
    "Mayu shuffles her feet as silence settles in."
    "..."
    "....."
    play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 7.5
    pf "Simple question: do you enjoy playing music?"
    show mayu neu b1 with dissolve
    "She looks up at me, but doesn't hesitate in her response."
    voice "audio/voice/E2/Free/MA/S4/0-52.ogg"
    ma "Yes."
    pf "Did you enjoy playing music with me?"
    show mayu neu b2 with dissolve
    "She blushes."
    voice "audio/voice/E2/Free/MA/S4/0-53.ogg"
    ma "Yes."
    pf "Then the only thing left for us to do is to start a band!"
    show mayu cur b2 with dissolve
    "Mayu blinks."
    voice "audio/voice/E2/Free/MA/S4/0-54.ogg"
    ma "I don't know about that..."
    pf "It's purely to keep our minds sharp and ensure we have a well-rounded education. Nothing professional about it."
    show mayu smi b2 with dissolve
    "A smile plays on her lips."
    voice "audio/voice/E2/Free/MA/S4/0-55.ogg"
    ma "Well, I can't argue with that…"
    pf "I propose we plan our first practice session as a newly formed band."
    "Mayu nods."
    voice "audio/voice/E2/Free/MA/S4/0-56.ogg"
    ma "When?"
    "I grin."
    pf "No time like the present!"
    show mayu mis b2 with dissolve
    "She giggles, and raises her violin to her chin."
    show note:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/MA/S4/0-57.ogg"
    ma "Ready!"
    
    scene black with fade
    
    "This time I lead us into a fast-paced tempo and Mayu easily keeps up. This type of music doesn't seem to be something she's used to, but judging by the big smile on her face, she's enjoying herself immensely."
    "We continue to play together for a while until it gets late. We schedule our next {i}band{/i} meeting and then head out. I'm looking forward to the next session!"
    
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    $ E2MAS4_Completed = 1
    #end
    jump E2D6S2
