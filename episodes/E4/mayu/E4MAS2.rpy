##
label E4MAS2:
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "yandere"
    
    "Tonight is the talent show! Mayu, Mitsuki, and I have been practicing non-stop since auditions and we're feeling as confident as ever… {w}maybe."
    "Uncle Kaito let me borrow his car so we could load the instruments and any other equipment. I hope the girls are ready for me."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    "I give Mayu a call. She answers almost immediately."
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-32.ogg"
    ma "Hi!"
    pf "Hey, Mayu. Are you ready to go?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-33.ogg"
    ma "Yup. I have Mitsuki here too."
    voice "audio/voice/E4/Mitsuki/E4/Mayu/1.ogg"
    mk "Hey!"
    "I hear Mitsuki through the line."
    pf "Haha, okay, I'll be there in a few minutes."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-34.ogg"
    ma "Okay, see you soon!"
    
    scene black with fade
    "Once we hang up, I drive to ACE and pick up the rest of my team, then we head straight to the venue. The talent show is being held at a local music club. It's already full of patient spectators and participants waiting to set up."
    scene bg nightclub with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 8
    "Mitsuki sees a friend and dips out to say hello while Mayu and I wait for our turn to play. Most of the bands are actually pretty good! I guess Isokaze is full of untapped potential."
    show mayu smi at cc with dissolve
    "Mayu and I bob along to a particularly catchy pop song. Although a smile is on her face, she hugs her arms tightly."
    
    if mayrelatonship == 1:
        show mayu cur
        "I put my arm around her, and she glances at me in surprise, then leans into me."
        
    pf "Are you nervous?"
    show mayu ner
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-35.ogg"
    ma "Yeah…"
    pf "Don't worry, we're going to be great out there."
    show mayu wor
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-36.ogg"
    ma "I know, but…"
    # panic
    "She looks around and hugs herself even closer."
    show mayu ner
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-37.ogg"
    ma "There are just so many people."
    pf "Once we're onstage and the spotlight is on us, you won't even be able to see them. It'll be just like when we're practicing."
    show mayu neu
    "She nods slowly, mulling over my words."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-38.ogg"
    ma "That makes sense."
    show mayu smi
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-39.ogg"
    ma "Thanks."
    "She grins."
    show highschoolgirl2 extra at r3 with dissolve:
        xzoom -1
    "Mitsuki returns as we're on deck to play next. She bounces excitedly backstage."
    voice "audio/voice/E4/Mitsuki/E4/Mayu/2.ogg"
    mk "We're really going to do this aren't we?"
    voice "audio/voice/E4/Mitsuki/E4/Mayu/3.ogg"
    mk "I'm so nervous. My heart is beating so fast!"
    voice "audio/voice/E4/Mitsuki/E4/Mayu/4.ogg"
    mk "Are you nervous?"
    
    menu:
        "WHERE IS THE BATHROOM?":
            "My stomach is turning in circles."
            pf "I think I'm going to be sick."
            show mayu sur
            "Mayu blinks at me in surprise."
            # exclamation
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-40.ogg"
            ma "You seemed okay a second ago!"
            pf "That was before we were about to go onstage!"
        
        "We're going to rock!":
            pf "Are you kidding? We've worked really hard for this and I'm ready to give it my all!"
            "Mitsuki grins."
            voice "audio/voice/E4/Mitsuki/E4/Mayu/5.ogg"
            mk "Yeah! You're right! We're going to be amazing out there!"
            "Even Mayu seems to relax a bit."
            show mayu hap
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-41.ogg"
            ma "Let's do our best!"
    
    hide mayu
    hide highschoolgirl2 extra
    with dissolve
    "Soon, we're introduced onto the stage. Mitsuki bounces out, a ball of energy, while Mayu and I slowly follow suit."
    "I take a deep breath and try to clear my mind of everything. The cheers from the audience slowly fade away as I play my first note."
    "Mayu's violin joins in the melody before Mitsuki's voice rings loud and clear."
    "I let the music envelop me, twisting my senses with the ebb and flow of the melody. My fingers dance across the keys on their own as I listen to the chords I know so well."
    "When I strike the last chord, the note hangs in the still air before the crowd erupts into applause."
    "My breath comes out in short gasps after giving my all in that performance. Sweat drips down Mitsuki's face as she takes a bow, and even Mayu's cheeks are flustered."
    "As she rushes off the stage, Mitsuki pumps the air excitedly."
    show highschoolgirl2 extra at r3:
        xzoom -1    
    show mayu cur at l3
    with dissolve
    voice "audio/voice/E4/Mitsuki/E4/Mayu/6.ogg"
    mk "That was amazing! Good job, guys!"
    pf "Yeah! I think that was our best one yet."
    "Mayu looks as if she's in a daze."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-42.ogg"
    ma "Listen to the crowd…"
    "The cheers and applause are still going, but slowly dying down as the next band preps to go onstage."
    
    voice "audio/voice/E4/Mitsuki/E4/Mayu/7.ogg"
    mk "Oh! There are my friends! I'll catch up with you in a bit!"
    hide mayu
    hide highschoolgirl2 extra
    with dissolve
    show mayu smi at cc with dissolve
    "Mitsuki runs off again to chat with some of her friends who came to the show. Mayu and I head back out to the audience."
    
    if mayrelatonship == 0:
        "We're about to head to the bar to grab waters, when a couple of girls stop us."
        show studentF extra at l3
        show studentF2 extra at r3
        with dissolve
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_01.ogg"
        girl1 "Hey! You two were part of that band who just played, right?"
        show mayu cur
        "Mayu blinks and looks at me."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-43.ogg"
        ma "Um, yeah…"
        "The girls squeal!"
        show mayu sur
        voice "audio/voice/E4/Female High Schooler 2/E4/Mayu/1.ogg"
        girl2 "I knew it! Oh my god! You were amazing up there!"
        pf "Thanks!"
        "The first girl giggles nervously."
        show mayu cur
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_02.ogg"
        girl1 "Would it be okay if we got your autograph?"
        pf "Sure!"
        "With a wide smile, I sign the papers they hold out. Then they turn to Mayu."
        voice "audio/voice/E4/Female High Schooler 2/E4/Mayu/2.ogg"
        girl2 "Could we get yours too?"
        "Mayu blinks in surprise."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-44.ogg"
        ma "You want mine too?"
        voice "audio/voice/E4/Female High Schooler 2/E4/Mayu/3.ogg"
        girl2 "Yes, of course!"
        show mayu smi
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-45.ogg"
        ma "O-Okay!"
        "She takes the pen offered to her and signs her name in perfect script. The girls look at the signature in awe."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_03.ogg"
        girl1 "Thanks so much!"
        voice "audio/voice/E4/Female High Schooler 2/E4/Mayu/4.ogg"
        girl2 "Yes, thank you!"
        pf "It was our pleasure. We're glad you enjoyed the show."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_04.ogg"
        girl1 "This will mean even more when you guys end up being famous."
        "Mayu's eyes widen."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-46.ogg"
        ma "Famous?"
        voice "audio/voice/E4/Female High Schooler 2/E4/Mayu/5.ogg"
        girl2 "Yeah! You guys were awesome! You'll totally make it one day."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_05.ogg"
        girl1 "Anyway, thanks again!"
        pf "Enjoy the rest of the show."
        hide studentF
        hide studentF2
        with dissolve
        "They smile broadly as they disappear into the crowd. Mayu turns to me excitedly."
        show mayu cur
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-47.ogg"
        ma "We have fans!"
        pf "And one day we'll be famous."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-48.ogg"
        ma "Do you really think so?"
        pf "It's possible."
        show mayu thi
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-49.ogg"
        ma "Famous…"
        "Mayu has a dreamy look in her eye. I bet she's imagining what that would be like."
    
    else:
        show mayu smi
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-50.ogg"
        ma "I'm going to go freshen up. I'll be right back."
        pf "Sure, I'm going to get a water. I'll be by the bar."
        "Mayu nods, then heads off to the ladies' room."
        hide mayu with dissolve
        "I order a water and down it at the bar. As I wait for Mayu to return, a girl approaches me and smiles shyly."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_06.ogg"
        girl1 "Excuse me, are you a part of that band that just played?"
        show studentF extra at cc with dissolve
        "I blink in surprise."
        pf "Oh, um, yeah I am."
        "Her face lights up in excitement."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_07.ogg"
        girl1 "Oh! You guys were so wonderful out there!"
        pf "Thanks."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_08.ogg"
        girl1 "How long have you been playing piano?"
        pf "Since I was a kid. I started a little later than most, but that just motivated me to practice harder."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_09.ogg"
        girl1 "That's still really impressive."
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_10.ogg"
        girl1 "I appreciate a guy who understands hard work."
        "She brushes my arm playfully. Wait, did I send the wrong signals?"
        pf "Oh, actually..."
        "Suddenly, she pales."
        pf "...Are you okay?"
        "Her eyes widen at something behind me. She looks like she's seen a ghost!"
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_11.ogg"
        girl1 "Ah! I...I…"
        scene black with fade
        "I look behind me and see a glimpse of the most innocent smile."
        $ persistent.gpix[48][0] = 1
        $ persistent.gpix[49][0] = 1
        $ persistent.gpix[50][0] = 1
        scene cg mayu yandere 1 with fade:
            xzoom .5
            yzoom .5
        "When I blink, I see Mayu looking confused."
        scene cg mayu yandere 3 with dissolve:
            xzoom .5
            yzoom .5        
        "Oh! When did she get back?"
        voice "audio/voice/E4/Mayu_FemaleHighSchooler1/FHS1_12.ogg"
        girl1 "I gatta go!"
        "Before I can even say goodbye, she disappears. {w}Huh, that was weird."
        scene cg mayu yandere 1 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-51.ogg"
        ma "Who was that?"
        pf "I think she was a fan of our band."
        scene cg mayu yandere 3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-52.ogg"
        ma "Really?"
        pf "Yeah… I'm not sure why she left though…"
        "Mayu touches my arm and smiles."
        stop music fadeout .5
        scene cg mayu yandere 2 with dissolve:
            xzoom .5
            yzoom .5
        $renpy.pause(.5)
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-53.ogg"
        ma "Too bad she couldn't stay."
        "!!!"
        scene cg mayu yandere 3 with dissolve:
            xzoom .5
            yzoom .5
        $renpy.pause(.5)
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
        "Mayu looks at me with curiosity."
        "Wait, what was that? I think I've been in Japan so long that I'm starting to imagine things…"
        
        scene black with fade
        scene bg nightclub with fade
    
    hide mayu with dissolve
    "We stick around for the rest of the set and enjoy the music and ambiance."
    
    if mayrelatonship == 1:
        "Mayu sighs."
        pf "What's wrong?"
        show mayu ner at cc with dissolve
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-54.ogg"
        ma "Nothing, I've just been thinking about next week…"
        pf "Ah. I'm not looking forward to exams either. Studying has really been stressing me out. I need to do something to let out all my pent up energy."
        show mayu cur
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-55.ogg"
        ma "Me too. What do you normally like to do to let off steam?"
        pf "Hmm, it's been a while, but back at CINY my friends and I would go paintballing whenever we needed to let loose."
        "Mayu blinks."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-56.ogg"
        ma "Paintballing?"
        pf "Yeah! Have you been? It's really fun!"
        "She shakes her head."
        pf "Really?! Well, I'm definitely taking you then."
        "Her eyes widen."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-57.ogg"
        ma "O-Okay…"
        pf "Trust me, you'll love it. How about we go this weekend?"
        show mayu smi
        "She nods."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-58.ogg"
        ma "Sure. I could use a break from studying."
        pf "Great!"
        hide mayu with dissolve
    
    "After all the performances are over, the winners are announced. {w}We placed in third! Mayu and Mitsuki practically skip back to the car, and I can't keep the grin off my face. This was a great end to a great evening!"
    scene black with fade
    "After dropping the girls off at ACE, I drive back home."
    stop music fadeout 3
    stop ambient fadeout 3
    $renpy.pause(2.5)
    $ E4MAS2_Completed = 1
