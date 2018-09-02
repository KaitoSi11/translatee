label E2MAS3:
    
    
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    
    play ambient "audio/ambience/Campus.ogg" fadein 5.0
    scene bg campus building day with fade
    
    "I wonder if Mayu was serious about playing the violin for me. I'm actually really curious how well she plays."
    
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    "I dial Mayu's number."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "She answers the phone."
    
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5.0
    
    voice "audio/voice/E2/Free/MA/S3/0-01.ogg"
    ma "Hello?"
    pf "Hey, Mayu! About that violin session..."
    voice "audio/voice/E2/Free/MA/S3/0-02.ogg"
    ma "Um..."
    pf "... well, I'm ready to listen if you're ready to play!"
    voice "audio/voice/E2/Free/MA/S3/0-03.ogg"
    ma "Ah! Sorry, but my father is coming to visit again and I have errands I need to run before he gets here."
    "Wasn't her father just here?"
    pf "Oh, he comes to visit often, doesn't he?"
    "There's a slight pause, and I'm positive she's nodding."
    voice "audio/voice/E2/Free/MA/S3/0-04.ogg"
    ma "He's an alumni of ACE and has regular business with the dean, so he's here very often."
    pf "Your father knows the dean?"
    voice "audio/voice/E2/Free/MA/S3/0-05.ogg"
    ma "Yeah, they were classmates here at ACE. But that's not why he's here so often. ACE has the strongest pilot program in Japan, so naturally most of the graduates here are accepted into my father's military program."
    ##LINEMISSING##
    voice "audio/voice/MISSING/BATCH8/Missing Mayu-04.ogg"
    
    ma "He and the dean have been working together to build a bridging program between ACE and the military college."
    pf "And your father teaches at the military college?"
    voice "audio/voice/E2/Free/MA/S3/0-06.ogg"
    ma "Yup."
    pf "That's pretty impressive…"
    "I knew Mayu's father was pretty distinguished based on what I'd heard about him, but I had no idea he was this distinguished. No wonder Mayu always seems worried or stressed when he comes to visit. {w}I mean, it would be like if Hideo Akemi came to visit--"
    pf "Wait a minute! {w}Mayu!"
    voice "audio/voice/E2/Free/MA/S3/0-07.ogg"
    ma "Eh?!"
    pf "Your last name is Akemi!"
    voice "audio/voice/E2/Free/MA/S3/0-08.ogg"
    ma "Um, yes…"
    pf "The same \"Akemi\" as \"Hideo Akemi\"?"
    voice "audio/voice/E2/Free/MA/S3/0-09.ogg"
    ma "Hm? You mean Grandfather?"
    
    menu:
        "How can you say that so casually?!":
            pf "Grandfather?! Do you know who he is?"
            voice "audio/voice/E2/Free/MA/S3/0-10.ogg"
            ma "Yes… He's my grandfather…"
            pf "And the father of military GEAR piloting!"
            voice "audio/voice/E2/Free/MA/S3/0-11.ogg"
            ma "I suppose that's true too."
    
        "I wish my grandfather was famous.":
            pf "I bet you get to go to all the cool events since your grandfather is pretty much the founder of military piloting."
            voice "audio/voice/E2/Free/MA/S3/0-12.ogg"
            ma "I don't know about that…"
            "She hesitates."
            voice "audio/voice/E2/Free/MA/S3/0-13.ogg"
            ma "Although, I have gotten to meet some interesting people."
            pf "Knew it!"
    
        "This explains a lot.":
            pf "No wonder you're so good at tactical planning. You come from a family of tacticians."
            voice "audio/voice/E2/Free/MA/S3/0-14.ogg"
            ma "Oh!"
            voice "audio/voice/E2/Free/MA/S3/0-15.ogg"
            ma "T-Thanks, but I don't know if that's true."
            "It also explains why she takes her training so seriously. As the granddaughter of the first military GEAR pilot, she has some large shoes to fill."
    
            
    if E1D4S1_Pioneer == 1:
        pf "Oh man, I wish I'd put two and two together earlier. My history class project is about him…"
    
    voice "audio/voice/E2/Free/MA/S3/0-16.ogg"
    ma "Anyway, I should get going. I'm sorry I can't play for you today."
    pf "That's okay. Are you free over the weekend? Maybe we can postpone until then."
    voice "audio/voice/E2/Free/MA/S3/0-17.ogg"
    ma "Sure."
    pf "Great, don't back out on me, okay?"
    "I respond jokingly, but Mayu takes me seriously."
    voice "audio/voice/E2/Free/MA/S3/0-18.ogg"
    ma "I promise you will have your private show this weekend!"
    "Uh… Did she just say what I think she said?"
    voice "audio/voice/E2/Free/MA/S3/0-19.ogg"
    ma "I mean concert! I-I'll play then--I mean, I'll play for you then. P-Play my violin!"
    "I try to hold back a laugh."
    pf "Okay."
    voice "audio/voice/E2/Free/MA/S3/0-20.ogg"
    ma "I-I have to go! Bye!"
    "She quickly ends the call."
    "Although I can't see her, I can imagine how adorable Mayu looks when she's flustered, and I'm a little disappointed to have missed it."
    "Oh well, at least I have the weekend to look forward to."
    
    
    stop music fadeout 5
    stop ambient fadeout 5
    scene black with fade
    
    $ E2MAS3_Completed = 1

