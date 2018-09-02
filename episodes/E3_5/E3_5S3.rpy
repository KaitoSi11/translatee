#
label E3_5S3:
    $ kaiOut = "sCasual"
    $ yukOut = "coat"
    #time skip
    $renpy.pause(1)
    scene bg homekaito main night with fade
    show nikki neu at l2 with dissolve
    # sfx for this?
    "Uncle Kaito returns with a triumphant smile and sets flat, green pumpkins on the table."
    show kaito hap at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E4/Kaito/d00/(24).ogg"
    hk "Here! I bought four kabochas."
    pf "Why four?"
    show kaito smi
    voice "audio/voice/E4/Kaito/d00/(25).ogg"
    hk "Just in case someone messes up. Or we get hungry."
    show nikki thi
    "Nikki seems thoughtful."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_018.ogg"
    sf "Hmm, they're a little small but I guess these will do. It would be better if we could have found the big orange ones, but I guess they're kind of hard to find in Japan."
    show kaito wor
    "Uncle Kaito frowns."
    show drop:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d00/(26).ogg"
    hk "Are these wrong?"
    show nikki smi
    pf "They'll be fine."
    show kaito neu
    "I tie an apron around my waist and grab one of the knives, then stab my pumpkin."
    show nikki mis
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_019.ogg"
    sf "Geez, look at that grin as he plunges in the knife…"
    show kaito smi
    "Kaito has already slipped on his apron and stabs his pumpkin too. Then he cuts a circle off of the top."
    voice "audio/voice/E4/Kaito/d00/(27).ogg"
    hk "Less talking and more carving!"
    show nikki hap
    "Nikki hurriedly sets up."
    show note:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_020.ogg"
    sf "Aye aye, captain!"
    hide kaito
    hide nikki
    with dissolve
    stop music fadeout 5
    "We fall silent while we carve in deep concentration. The only sounds are the squelch of pumpkins."
    $renpy.pause(0.5)
    "..."
    "I've almost finished my pumpkin when Nikki puts down her knife."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
    show nikki smi at l2 with dissolve
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_021.ogg"
    sf "Done! Look at this masterpiece!"
    "She swivels her pumpkin around and shows us a spooky face. She carved in narrow eyes and a long grin full of sharp teeth."
    show kaito sur at r2 with dissolve:
        xzoom -1
    show exclamation:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d00/(28).ogg"
    hk "How did you do that so quickly?!"
    show nikki neu
    "Nikki giggles."
    show kaito cur
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_022.ogg"
    sf "I told you. I'm the carving master."
    show nikki cur
    "She peeks at Uncle Kaito's pumpkin."
    show question:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_023.ogg"
    sf "You've only finished one eye?!"
    show kaito mis
    voice "audio/voice/E4/Kaito/d00/(29).ogg"
    hk "You can't rush brilliance."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_024.ogg"
    sf "What about you, big bro?"
    show kaito smi
    pf "Just finishing the last few touches…"
    "She looks at my pumpkin."
    show nikki ske
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_025.ogg"
    sf "Even he's almost finished. How come you've barely started?"
    show kaito mis
    voice "audio/voice/E4/Kaito/d00/(30).ogg"
    hk "Just wait, mine is going to be even better than the two of yours because I'm actually taking the time to do it right."
    "I think I hear a faint knock at the door but no one else reacts. It must have been my imagination..."
    show nikki mis
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_026.ogg"
    sf "I win by default because I was fastest."
    show kaito cur
    voice "audio/voice/E4/Kaito/d00/(31).ogg"
    hk "That's not fair! I thought we were being judged on best carving job."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_027.ogg"
    sf "It's both. Best and fastest carving. That's how we did it at home."
    show storm:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito ske
    voice "audio/voice/E4/Kaito/d00/(32).ogg"
    hk "I didn't know these rules…"
    show nikki neu
    "Nikki turns to me."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_028.ogg"
    sf "Who do you think is the winner?"
    
    menu:
        "Obviously, you.":
            pf "Yup, those are the rules. Nikki wins."
            show kaito sad
            voice "audio/voice/E4/Kaito/d00/(33).ogg"
            hk "Really, bud? I take you into my home and this is how you repay me?"
            show nikki smi
            "I shrug helplessly as Nikki laughs."
            pf "I learned a long time ago that it's futile to argue against Nikki."
            show note:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki hap
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_029.ogg"
            sf "That's right!"
    
        "Have you not seen my masterpiece?":
            pf "Um, clearly, the winner is me."
            show nikki cur
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_030.ogg"
            sf "I thought you weren't even finished."
            pf "I finished up while you two were arguing."
            "I spin my pumpkin around for them to view it."
            pf "Does this not scare your pants off?"
            show nikki ske
            "Nikki raises an eyebrow. Kaito looks down at his legs."
            show kaito mis
            voice "audio/voice/E4/Kaito/d00/(34).ogg"
            hk "Hm, my pants are still on so I'll have to say nope."
            show nikki mis
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_031.ogg"
            sf "Nice try."
            pf "Hmph, neither one of you knows good art when you see it."
    
        "Kaito's not even done yet.":
            pf "That's not fair. At least let Uncle Kaito finish before judging."
            show kaito neu
            show nikki dis
            "Nikki pouts."
            show storm:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_032.ogg"
            sf "That's not how we used to do it."
            pf "I know, but he's a newbie. Cut him some slack."
            show kaito ske
            voice "audio/voice/E4/Kaito/d00/(35).ogg"
            hk "Hey! I don't need a handicap!"
            show nikki neu
            "Nikki ignores Kaito and nods."
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_033.ogg"
            sf "You're right. I should have thought of that."
            show nikki smi
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_034.ogg"
            sf "Okay, Uncle Kaito, you can finish up and then I'll prove to you that mine is still the best."
            
    stop music fadeout 3
    "A singsong voice floats into the room, followed by a familiar face."
    voice "audio/voice/E4/Yuuki/E4/D0/1.ogg"
    hy "Surpriiiiise!"
    
    hide kaito
    hide nikki
    with dissolve
    
    
    show kaito cur at r3:
        xzoom -1
    show nikki sur at cc:
        xzoom -1
    with dissolve
    
    show yuki hap at l3
    with dissolve
    "Everyone freezes."
    pf "...Aunt Yuki?"
    show exclamation:
        xoffset 230
        yoffset 125
        xzoom .75
        yzoom .75
    show yuki cur with dissolve
    "For some reason, she looks just as surprised as the rest of us. Her eyes are wide and her mouth forms an \"o\". She's wearing a long, stylish trench coat, which she closes tightly. {w}Nikki's face breaks into a wide smile and she races to give Aunt Yuki a hug."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    show heart:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki hap
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_035.ogg"
    sf "Aunt Yuki!"
    show yuki hap
    "Yuki relaxes into a matching grin and hugs her back."
    show kaito smi
    voice "audio/voice/E4/Yuuki/E4/D0/2.ogg"
    hy "You've grown so tall! What happened?"
    show nikki smi
    "Nikki giggles."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_036.ogg"
    sf "You think so? I still hope I grow another inch or two."
    show nikki hap
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_037.ogg"
    sf "I can't believe you're finally here!"
    show yuki sur
    "Yuki blinks in surprise."
    show nikki neu
    voice "audio/voice/E4/Yuuki/E4/D0/3.ogg"
    hy "Oh! Right, I'm, uh, back from my… business trip…"
    show kaito cur
    show panic:
        xoffset 230
        yoffset 125
        xzoom .75
        yzoom .75
    "She looks at Kaito for back-up, but his face is a frozen mask of surprise...and fear?"
    
    menu:
        "Play along.":
            pf "Oh wow, Aunt Yuki! You were gone for a really long time."
            show nikki smi
            "Nikki giggles and follows my lead."
            show yuki 
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_038.ogg"
            sf "Yeah! This is the first time we've seen you since we moved here. What were you doing that took so long?"
            show yuki smi
            voice "audio/voice/E4/Yuuki/E4/D0/4.ogg"
            hy "Oh, you know, I was traveling doing company PR… boring stuff. You don't want to hear about it."
            show kaito ner
            "Uncle Kaito finally recomposes himself."
            voice "audio/voice/E4/Kaito/d00/(36).ogg"
            hk "It's okay, Yuki. They know."
            show yuki dis
            voice "audio/voice/E4/Yuuki/E4/D0/5.ogg"
            hy "They do?"
    
        "Say you know the truth.":
            pf "It's okay, Aunt Yuki, we know that you weren't on a business trip."
            show nikki smi
            "Nikki nods."
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_039.ogg"
            sf "Uncle Kaito told us what's really going on."
            show yuki dis
            "Aunt Yuki frowns."
            show kaito ner
            voice "audio/voice/E4/Yuuki/E4/D0/6.ogg"
            hy "You did?"
            
    show nikki neu
    voice "audio/voice/E4/Kaito/d00/(37).ogg"
    hk "They figured it out. I had no choice."
    show yuki wor
    voice "audio/voice/E4/Yuuki/E4/D0/7.ogg"
    hy "I see… Well, I suppose that makes things easier. Are you angry?"
    "I shake my head."
    pf "Of course not. We get it."
    show yuki ner
    voice "audio/voice/E4/Yuuki/E4/D0/8.ogg"
    hy "I'm sorry I didn't stop by to see you kids sooner but your uncle didn't even tell me you were here until a few weeks ago… when I really was traveling for work!"
    show nikki mis
    "Nikki mock glares at Kaito."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_040.ogg"
    sf "Seriously, Uncle?"
    show kaito wor
    voice "audio/voice/E4/Kaito/d00/(38).ogg"
    hk "I meant to tell her! I just never seemed to have time."
    show yuki mis
    show kaito cur
    voice "audio/voice/E4/Yuuki/E4/D0/10.ogg"
    hy "He wanted to hog you all to himself!"
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_041.ogg"
    sf "How rude!"
    show kaito smi
    "Nikki hugs Aunt Yuki again."
    show nikki cur
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_042.ogg"
    sf "Aunt Yuki, don't you want to take your coat off?"
    show yuki ner
    voice "audio/voice/E4/Yuuki/E4/D0/11.ogg"
    hy "Um…"
    "She steps back from Nikki and pulls her coat tighter."
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D0/12.ogg"
    hy "You know, it's a little chilly in here so I think I'll keep it on."
    show kaito ske
    show nikki ske
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_043.ogg"
    sf "Really? I don't think it's cold…"
    show drop:
        xoffset 230
        yoffset 125
        xzoom .75
        yzoom .75
    show yuki thi
    voice "audio/voice/E4/Yuuki/E4/D0/13.ogg"
    hy "I actually, um, didn't realise you kids were home…"
    $renpy.pause(0.5)
    show kaito sur
    show bulb:
        xoffset 1175
        yoffset 5
        xzoom .75
        yzoom .75
    play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
    $renpy.pause(0.5)
    "Kaito's eyes widen in understanding as Yuki makes eye contact."
    voice "audio/voice/E4/Kaito/d00/(39).ogg"
    hk "Oh… OH!"
    show kaito wor
    "He quickly jumps to his feet."
    show drop:
        xoffset 1175
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d00/(40).ogg"
    hk "Uh, Yuki, I need to talk to you about something. Um, in private."
    show yuki smi
    voice "audio/voice/E4/Yuuki/E4/D0/14.ogg"
    hy "Yes, sure!"
    hide kaito
    hide yuki
    with dissolve
    "Before the words are out of her mouth, the two of them are already halfway up the stairs."
    "I try to stifle my laughter as Nikki watches them leave, her mouth hanging open in confusion."
    show confused:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_044.ogg"
    sf "Is it me or was that really weird?"
    "Ah, sweet, innocent Nikki. If only you could stay this innocent forever."
    "I pat her on the head."
    pf "Don't you worry your pretty little head about it."
    show nikki dis
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_045.ogg"
    sf "What's that supposed to mean?"
    pf "You'll understand when you're older."
    show nikki thi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_046.ogg"
    sf "Now you're acting weird too…"
    hide nikki with dissolve
    $ yukOut = "sweater"
    "A few minutes later, Kaito and Yuki return. She's shed her coat and is wearing a pink sweater and a skirt."
    hide nikki with dissolve
    
    show nikki neu at l3
    with dissolve
    
    show kaito smi at r3:
        xzoom -1
    show yuki smi at cc:
        xzoom -1
    with dissolve
    
    $renpy.pause(.25)
    pf "Crisis averted?"
    show exclamation:
        xoffset 1175
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito dis b1 behind exclamation
    show yuki cur b2 behind exclamation
    with dissolve
    "Uncle Kaito shoots me a warning look as Aunt Yuki blushes. I struggle to hold in my grin."
    show yuki smi b2
    voice "audio/voice/E4/Yuuki/E4/D0/15.ogg"
    hy "Yup."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_047.ogg"
    sf "Aunt Yuki, if you weren't really away on business, what brings you back home?"
    show kaito wor b2
    show shoBlush:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show yuki sur b2
    with dissolve
    "Yuki's blush deepens and even Uncle Kaito's cheeks burn red."
    show kaito mis b2
    voice "audio/voice/E4/Kaito/d00/(1).ogg"
    hk "Hey! Look at the pumpkins we've been carving!"
    show yuki hap b2
    voice "audio/voice/E4/Yuuki/E4/D0/16.ogg"
    hy "Oh! Yes! I'd love to see them!"
    show nikki ske
    "Nikki glances over at me and raises her eyebrow again. I just laugh."
    hide kaito
    hide nikki
    hide yuki
    with dissolve
    
    "While Aunt Yuki inspects the pumpkins, Uncle Kaito and Nikki return to arguing about who is the pumpkin master. Yuki says she'll put everyone to shame."
    "I can't help but smile as I see Uncle Kaito slip his arm around Aunt Yuki. Maybe things are looking up for the two of them."
    scene black with fade
    "Before Nikki can challenge Aunt Yuki to a carving contest, I \"offer\" to take Nikki to the movies so Kaito and Yuki can \"catch up\"."
    "At first Nikki protests, but she has no choice but to go with me when I drag her out of the house."
    stop music fadeout 5
    "By the time the movie ends, Aunt Yuki and Uncle Kaito are nowhere to be found. I go to bed with a smile on my face and...{w} a glimmer of hope in my heart."
    stop ambient fadeout 3
    
    #"A glimmer of hope in my heart that there will be...{w} a Nikki route."
    #"j/k"
    #"That's all you guys get for the stream!"
    
    jump E3_5S4
