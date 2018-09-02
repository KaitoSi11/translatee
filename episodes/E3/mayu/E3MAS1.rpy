#
label E3MAS1:
    
    #Afternoon
    $ mayOut = renpy.random.choice(['sUniform'])
    $ meiOut = "sCasual"
    scene bg campus library day with fade
    ### NOTE - continuity is at risk, where this scene is currently available to players that have never interacted with Mayu before.
    # such as the 2nd line, "we've been jamming regularly together"
    if E2MAS2_Completed == 0:
        "Mayu and I discovered we both share an interest in music. She plays the violin while I play the piano. After we got to talking about music, Mayu promised she'd play for me."
        "True to her word, Mayu did end up playing for me. I jokingly mentioned we should start a band but she was receptive to the idea so we decided to go for it."
        
    elif E2MAS2_Completed == 1 and E2MAS4_Completed == 0:
        "True to Mayu's word, she did end up playing for me. I jokingly mentioned we should start a band but she was receptive to the idea so we decided to go for it."

    "I make my way to the music room. I've finally convinced Mayu we should expand the band and we're now holding auditions for our newest member."
    "After Mayu played for me for the first time, she's loosened up a lot and we've been jamming regularly together."
    "I found a flyer for local musicians. The community is sponsoring a talent night for both bands and solo artists. I know Mayu and I are ready to compete, and after much cajoling I got her agree to sign up."
    "The only problem is a \"band\" is considered three or more people. Neither one of us wants to perform alone, so the only thing left to do is recruit a third member."
    
    "Mayu is already setting up the music room when I arrive."
    pf "Hey, Mayu."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    show mayu hap at cc with dissolve
    "She pauses and smiles when she sees me."
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-01.ogg"
    ma "Hi! You made it!"
    show mayu smi b1
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-02.ogg"
    ma "I-I mean, of course you made it but you're early, which is nice."
    show mayu ner b1
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-03.ogg"
    ma "N-Not that I don't think you can be early to things, but…"
    "Her voice fades and she drops her gaze."
    pf "I'm a little nervous too."
    show mayu smi
    "Mayu flashes me an appreciative smile."
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-04.ogg"
    ma "I hope we find someone good."
    pf "Same here."
    show mayu cur
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-05.ogg"
    ma "There will only be singers auditioning today, right?"
    pf "Yeah, I think having a vocalist will best complement our sound."
    show mayu smi
    "Mayu nods."
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-06.ogg"
    ma "I agree."
    hide mayu with dissolve
    "I help her move some of the clutter to the corner of the room and set up a long table with chairs in the middle of the room for us to sit. {w}This is the judges' table."
    
    "Mayu sits at the table, while I poke my head out in the hall."
    pf "Will the first audition please enter the room?"
    show mayu neu at l1
    with dissolve
    show bully3 extra at r3:
        xzoom -1
    "As I return to my seat, a short student with slicked back hair walks in. He's changed out of his uniform and his shirt hangs loosely over his small frame. I squint to get a better look and notice his shirt is decorated with all different types of footwear: sandals, flip-flops, etc. {w}This is going to be interesting."
    
    "Mayu's brow is furrowed and she wears a hesitant smile. She seems just as apprehensive as I am."
    
    pf "Hello. What's your name?"
    "The boy wears a goofy grin."
    ### Voice - missing line?
    bh "Hi, I'm Bill Hang."
    pf "What are you going to sing today?"
    voice "audio/voice/E3/Free/MA/S1/bill/1.ogg"
    bh "She humps."
    show mayu smi
    "Mayu and I glance at each other. This was a popular song back when we were kids. {w}I nod."
    pf "Whenever you're ready."
    
    "Bill flashes us another lopsided grin. As he belts out a tune, he begins to bounce his knees and stiffly jerk his hips from side to side. He sings in a monotone and his cadence feels almost robotic. Paired with his strange dancing, he reminds me of someone gaining use of their limbs for the first time."
    show drop:
        xoffset 515
        yoffset 135
        xzoom .75
        yzoom .75
    "I glance over at Mayu who has a forced smile frozen on her face. Her eyes seem almost panicked."
    
    if MCStory == 3:
        "I can tell she's wondering if all our auditions are going to be as awful as this one because I'm wondering the same thing."
        "I catch her attention and give her a reassuring smile. She seems to relax some."
    
    "Finally, he finishes and waits expectantly for our feedback."
    
    menu:
        "At least you've got spirit.":
            "I put on my most comforting smile."
            pf "Thanks for coming out."
            "Bill continues to stare at me as if expecting more."
            pf "Um, you had great passion in your performance."
    
        "Yo dawg.":
            pf "Aiight dawg, I gotta be real with you. I was kind of feeling it, but I wasn't really feeling it. You feel me?"
    
        "My dog can sing better than that.":
            pf "The fact of the matter is you can't sing and you can't dance. In fact, I'm sure my dog would have put on a better performance."
            
    show mayu wor
    "Bill stares stoically as I give him my feedback, then looks expectantly at Mayu. She fidgets under his gaze as she tries to find something to say."
    show panic:
        xoffset 515
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-07.ogg"
    ma "Um… Well, it was… You were very brave to sing in front of us and I think it's great that you did."
    show mayu neu
    "She nods, seemingly satisfied with her review."
    
    "I'm about to dismiss him, when someone else interrupts me."
    show studentM2 extra at l3 with dissolve:
        xoffset -200
    voice "audio/voice/E3/Free/MA/S1/tj/1.ogg"
    tj "Excuse me, but are you in the wrong room? This audition is for {i}singers{/i}. I'm not sure what you thought you were doing up there but it certainly was not {i}singing{/i}."
    "Another student sits beside Mayu. He's wearing an ACE uniform without teal stripes, so he isn't a pilot."
    
    "Mayu merely glances over at the student, but otherwise doesn't react to his presence. Maybe he's one of her music friends. She must have asked him to sit in on our auditions and help us judge who would be a good fit."
    
    "Despite the new guy's scathing comments, Bill doesn't seem phased."
    voice "audio/voice/E3/Free/MA/S1/bill/2.ogg"
    bh "I did my very best and that's all I could have done."
    ### VOICE - used to say "very proud" but voice said "glad"
    voice "audio/voice/E3/Free/MA/S1/bill/3.ogg"
    bh "I have no professional training but I am very glad of my performance."
    
    show mayu smi
    "Mayu smiles encouragingly."
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-08.ogg"
    ma "That's great. Thank you for coming by."
    pf "Yeah, thanks. We'll be in touch."
    "Mayu's friend crosses his arms and waits for Bill to leave."
    hide bully3 extra with dissolve
    $renpy.pause(0.5)
    show gosunerd extra at r3 with dissolve:
        xzoom -1
    "Once Bill leaves, he is immediately replaced by another student. He's still in ACE uniform, but contrastly, his long dark hair falls to mid-back and covers one eye."
    voice "audio/voice/E3/Free/MA/S1/slasher/1.ogg"
    sl "Hi, my name is Slasher and I'll be singing an original song I wrote myself."
    show mayu hap
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-09.ogg"
    ma "Hi--"
    
    "He cuts Mayu off in the middle of her greeting and screams in a hoarse voice."
    
    show mayu sur
    voice "audio/voice/E3/Free/MA/S1/slasher/2.ogg"
    sl "DEATH. TO. ALL. METAAAAAAAAAAAAL!"
    "Oh god…"
    "I scream over Slasher before my ears literally begin to bleed."
    pf "THANK YOU! I think we've heard enough."
    "Mayu's eyes are wider than I've ever seen and she flinches every time Slasher belts out a word."
    show mayu win
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-10.ogg"
    ma "Um, thanks, if you could please stop for a second…"
    "Her friend clamps his hands over his ears and cringes in pain."
    voice "audio/voice/E3/Free/MA/S1/tj/2.ogg"
    tj "STOP FOR THE SAKE OF OUR SANITY!"
    "Slasher finally quiets down but looks confused."
    voice "audio/voice/E3/Free/MA/S1/tj/3.ogg"
    tj "Are you trying to turn us all into raving psychopaths? Because the only effect constant yelling has on me is making me angry."
    voice "audio/voice/E3/Free/MA/S1/slasher/3.ogg"
    sl "What? I haven't gotten to the killing part yet. Here, listen."
    voice "audio/voice/E3/Free/MA/S1/slasher/4.ogg"
    sl "SLEEP. IN. BLOOD. ETERNAAAAAAAAAL!"
    "Mayu and I shout simultaneously."
    show exclamation:
        xoffset 515
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ang
    # change to "Both of us" in one line?
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-11.ogg"
    ma "NO!"
    pf "NO!"
    show mayu ann
    "Slasher pauses again. Mayu's friend looks like he's about to speak again, but we silence him with death glares."
    
    menu:
        "That's...energetic.":
            pf "That's a very rowdy song and I really liked your energy."
    
        "What the hell, dawg?":
            pf "Look, dawg, I'm just keeping it real. It started a little rough, but you managed to make it your own. You made it {i}your own{/i}, yo!" 
    
        "I think I've gone deaf.":
            pf "That was quite possibly the worst song I've ever heard. I would say more but I can't hear myself over the ringing in my ears."
    
    "In response, Slasher opens his mouth, ready to belt out another line. Mayu immediately stops him."
    show mayu wor
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-12.ogg"
    ma "Wait! Um, your song is definitely very original, but it's not quite the direction we're going for this band."
    voice "audio/voice/E3/Free/MA/S1/slasher/5.ogg"
    sl "Whatever. You guys can't even begin to comprehend my genius."
    hide gosunerd with dissolve
    "Slasher turns on his heel and walks out of the room."
    show mayu neu
    "I breathe a sigh of relief, but brace myself for the next audition."
    show highschoolgirl2 extra at r3 with dissolve:
        xzoom -1
    "A girl walks in. She's wearing her ACE uniform and has her dark hair pulled back into a messy ponytail. She seems normal so far, but I don't want to get my hopes up."
    
    pf "Hello."
    "She smiles warmly and waves."
    voice "audio/voice/E3/Free/MA/S1/mk/1.ogg"
    mk "Hi, my name is Mitsuki."
    show mayu smi
    "Mayu seems hopeful."
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-13.ogg"
    ma "Feel free to begin whenever you're ready."
    "Mitsuki nods, and takes a deep breath. Her voice shakes as she sings a soft melody, but grows in power as she gains confidence."
    show mayu cur
    "Mayu and I blink at each other. She's actually good!"
    "I close my eyes and find myself getting lost in Mitsuki's voice. Before long, her song is done."
    show mayu smi
    "Mitsuki waits nervously for our feedback."
    "Mayu stands to her feet so suddenly her chair wobbles."
    show heart:
        xoffset 515
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu hap
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-14.ogg"
    ma "You were wonderful! You have a powerful voice which would perfectly complement our instruments. And the emotion behind your song… I could {i}feel{/i} what you were singing!"
    "Mitsuki blushes at Mayu's praise."
    voice "audio/voice/E3/Free/MA/S1/mk/2.ogg"
    mk "Thank you!"
    show mayu smi
    
    menu:
        "What Mayu said!":
            pf "I couldn't agree more with what Mayu said. That was a beautiful performance."
    
        "Yo dawg, that was blazing hot!":
            pf "You, girl, are in it to win it! Seriously, that was blazing hot! I bet you could sing the phone book and I would still be blown away."
    
        "This is it.":
            pf "One of my favourite things in the world... is when I sit in this chair... and meet a star for the first time. {i}You{/i} are a star. Well done."
    
    "Mitsuki breaks into a wide smile. The random guy raises a hand."
    voice "audio/voice/E3/Free/MA/S1/tj/4.ogg"
    tj "Excuse me, but what was that?"
    "Mitsuki blinks, obviously confused. I'm not sure what this guy is talking about either…"
    voice "audio/voice/E3/Free/MA/S1/tj/5.ogg"
    tj "This good shy girl act is soooo played out. Where's the confidence? The fire? And for god's sake have you ever heard of a comb?"
    show mayu neu
    "Mitsuki runs her hands through her hair."
    voice "audio/voice/E3/Free/MA/S1/mk/3.ogg"
    mk "I-I'm sorry! My last class was physical education and I was running a little late…"
    
    "I lean closer to Mayu."
    pf "What's with your friend? He's kind of a jerk…"
    show mayu sur
    stop music fadeout .15
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-15.ogg"
    ma "Wait--I thought he was {i}your{/i} friend!"
    show dots:
        xoffset 515
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu cur
    "We stare at each other for a second, then focus our attentions on the mystery guy."
    pf "Uh, hey."
    show mayu neu
    "He glances over at us."
    pf "Who are you?"
    voice "audio/voice/E3/Free/MA/S1/tj/6.ogg"
    tj "Excuse me?"
    "He pulls a face of disgust."
    voice "audio/voice/E3/Free/MA/S1/tj/7.ogg"
    tj "How dare you! Don't you know who I am?"
    pf "...No…"
    show mayu ner
    "Mayu shakes her head."
    "The guy scoffs."
    voice "audio/voice/E3/Free/MA/S1/tj/8.ogg"
    tj "Ugh. Clearly I have made a terrible mistake. You peasants wouldn't know greatness if it bit you in the ass."
    hide studentM2 with dissolve
    "With a loud sniff of disdain, he swaggaliciously exits the classroom. {w}Awkward."
    voice "audio/voice/E3/Free/MA/S1/mk/4.ogg"
    mk "So, um, did I pass?"
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 3
    show mayu smi
    pf "Yes! We'd love for you to join the band."
    voice "audio/voice/E3/Free/MA/S1/mk/5.ogg"
    mk "Really?!"
    show mayu hap
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-16.ogg"
    ma "Yes, absolutely! We have your information so we'll let you know when our next practice will be and hopefully we'll see you there."
    voice "audio/voice/E3/Free/MA/S1/mk/6.ogg"
    mk "Thank you! Yes! I'll be there! Okay, thank you again."
    hide highschoolgirl2 with dissolve
    "Grinning from ear to ear, Mitsuki practically skips out of the room."
    show mayu thi
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-17.ogg"
    ma "Is it strange that I feel kind of nervous?"
    pf "How come?"
    show mayu smi
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-18.ogg"
    ma "I don't know. I'm really excited! I'm already getting ideas for new pieces that will incorporate her voice, so I don't know why I'm so nervous."
    pf "It's probably because after how bad those previous auditions were, you're hoping this one good audition isn't a fluke."
    show mayu mis
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-19.ogg"
    ma "Maybe."
    "She smiles at me."
    show mayu smi
    voice "audio/voice/E3/Free/MA/S1/mayu/Mayu Arc-20.ogg"
    ma "We should probably clean up. I think our reserved time is running out."
    stop music fadeout 3.5
    hide mayu with dissolve
    scene black with fade
    "After Mayu and I clean up the music room, we part ways so she can go to class. I can't wait to see what kind of music the three of us will create together."
    
    $ E3MAS1_Completed = 1
    #end

