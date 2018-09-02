#
label E3VBS3:

$ valOut = renpy.random.choice(['sDate2'])
$ valHairF = renpy.random.choice(['default'])
$ valHairB = renpy.random.choice(['default'])
    
play sound "audio/sfx/Technology/Phone Dial.ogg"
"I dial Valerie's number. She better not have forgotten…"

play sound "audio/sfx/Technology/Phone Answer.ogg"
$renpy.pause(2.0)
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL99.ogg"
vb "I was wondering when you'd call."
pf "I guess that means you remembered our plans."
"Her voice turns to silk."
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL100.ogg"
vb "How could I forget? I have a really fun day planned for us."
pf "Awesome!"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL101.ogg"
vb "Are you ready now?"
pf "Yeah."
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL102.ogg"
vb "Great! I'll see you at the mall."
pf "Okay, see you."
"As soon as we hang up, I grab my keys and hop on my bike."


stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)
play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(5.5)


"After parking my bike, I meet Valerie at the mall entrance."

play ambient "audio/ambience/Mall.ogg" fadein 3
scene bg mall main day
show valerie neu at cc
with fade

$renpy.pause(1.0)
play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
show valerie smi
"She grabs my hand as soon as she sees me."
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL103.ogg"
vb "There you are! Come on, let's go inside."
pf "Where are we going?"
"She pulls me in front of the department store."
show valerie hap
show note:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL104.ogg"
vb "Shopping, of course!"
"Oh no…"
"I don't have time to think about it before Valerie starts piling clothes into my arms."
show valerie smi
pf "Uh, what are you doing?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL105.ogg"
vb "I'm going to try... {i}these{/i} on!"
pf "Why am I holding them?"
show valerie cur
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL106.ogg"
vb "I need my hands free so I can shop."
stop ambient fadeout 3.0
"Satisfied by the mountain of clothes in my hands, she pulls me towards the dressing room. She takes the clothes from me and heads into one of the stalls."
show valerie hap
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL107.ogg"
vb "I'll be right back, okay?"
hide valerie with dissolve
"Luckily, there are chairs right outside of the rooms. I take a seat while I wait for her."

$ valOut = renpy.random.choice(['sCute'])

"Before long, she pops out of the dressing room and models her first outfit for me."

show valerie smi at cc with dissolve
$renpy.pause(.75)
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL108.ogg"
vb "What do you think?"
"She shows off her clothes with a little twirl."

menu:
    "It's nice!":
        pf "I really like it."
        "Valerie grins."
        show valerie mis
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL109.ogg"
        vb "You think so?"
        pf "Yeah, you should you get it."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL110.ogg"
        vb "Hold that thought. I've got something better."

    "Could be better.":
        pf "It's not bad, but it doesn't do you justice."
        show valerie mis
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL111.ogg"
        vb "Oh yeah?"
        pf "You need something that accentuates your curves."
        "Valerie grins."
        show heart:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie hap
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL112.ogg"
        vb "I had no idea that you were such a fashionista."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL113.ogg"
        vb "Wait until you see the next one."

    "Meh.":
        "I shrug."
        pf "It's fine I guess?"
        show valerie cur
        show question:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL114.ogg"
        vb "You don't like it?"
        pf "I don't really know women's clothing."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL115.ogg"
        vb "That's okay, I know you'll like this next one better."

        
hide valerie with dissolve
"She disappears back into the dressing room. {w}I wait patiently, and after a few minutes, she emerges in a second outfit. This one fits her like a glove and shows a little bit more skin."

$ valOut = renpy.random.choice(['sFlirty'])

show valerie smi at cc with dissolve
$renpy.pause(.75)
"She steps out and pops her hip."
voice "audio/voice/MISSING/BATCH4/Valerie/ValE3Redos/E3ValerieArcS3Redo2.ogg"
vb "What about this?"

menu:
    "So pretty and beautiful!":
        "This outfit is a little risque but she wears it well."
        pf "You look breetty!"
        "My cheeks turn pink as soon as the words escape my mouth."
        show valerie cur
        "Valerie blinks."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL116.ogg"
        vb "Breetty?"
        pf "I meant to say pretty but then decided to say beautiful and that's what came out…"
        show valerie mis
        "She smirks."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL117.ogg"
        vb "An innocent little outfit like this and you're already tongue-tied. I can't wait to show you the next one I have!"
        "My eyes widen as I imagine what she has in store…"

    "Getting warmer…":
        pf "I like that you went with the curve hugger. You're headed in the right direction, but you're still not quite there…"
        show valerie mis
        "Valerie smirks."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL118.ogg"
        vb "Still not impressed? Then hold on for one more minute because this next one will surely blow you away."
        show valerie cur
        pf "I can't wait to be blown…"
        "Valerie raises an eyebrow."

    "Meh.":
        "I shrug."
        pf "Eh, it's okay, I guess."
        show valerie sad
        "Valerie frowns."
        show valerie neu
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL119.ogg"
        vb "Tough crowd… But there's no way you won't like this next one!"

        
hide valerie with dissolve
"She slips back into the dressing room, leaving me to wonder what her next outfit could be. {w}Before long, she slips back out and purrs at me."

$ valOut = renpy.random.choice(['Halloween'])
$ ValAccT = renpy.random.choice(['Halloween'])

show valerie hap b1 at cc with dissolve
$renpy.pause(.75)
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL120.ogg"
vb "Isn't this just purrrrfect?"

menu:
    "Sexyness overload!":
        "I can't believe what I'm seeing! Is this a dream come true? {w}I rub my eyes again and my face feels burning hot."
        show valerie mis b1
        "Valerie smirks."
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL121.ogg"
        vb "Cat got your tongue?"
        "All I can do is nod."

    "I knew I liked cats for a reason.":
        "I'm a little surprised by the outfit, but not disappointed. It's more than I could have asked for!"
        show valerie mis b1
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL122.ogg"
        vb "Sooo, what do you think?"
        "She plays with her tail."
        pf "I can't wait to see what you've got in store for the next one."
        show valerie hap b1
        show note:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        "She giggles."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL123.ogg"
        vb "Nu uh, this is all you get for today."
        pf "Aww…"

    "Meh.":
        "I shrug."
        pf "I'm not sure about this one… Kind of a weird choice."
        show valerie cur b1
        "Valerie drops all pretenses and stares at me in bewilderment."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL124.ogg"
        vb "Seriously? You don't like this at all?"
        "She turns and wiggles her tail at me."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL125.ogg"
        vb "How about now?"
        "I just shrug again."
        show valerie sad b1
        "Valerie shakes her head."
        show crying:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL126.ogg"
        vb "Nobody can resist nekogirl…"

hide valerie with dissolve
"She returns to the dressing room one last time and comes out wearing her original clothes."

$ valOut = renpy.random.choice(['sDate2'])
$ valAccT = renpy.random.choice(['emptyimage'])

show valerie smi at cc with dissolve
"She offers me the outfits."
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL127.ogg"
vb "Which one should I get?"

### NOTE - this is a new variable for the E3.5/E4 release
$ E3VBS3_Nekogirl = 0

menu:
    "Get the first one.":
        pf "The first one looked best on you."

    "Get the second one.":
        pf "You should get the second one."

    "Get the last one.":
        $ E3VBS3_Nekogirl = 1
        pf "There's no way you can leave this store without the third one."
        show valerie mis
        "Valerie seems amused."

    "Don't get any of them.":
        pf "Hm, I think you can find something better."
        "She frowns."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL128.ogg"
        vb "Oh, alright. I'll go put these back."
        "I wait as she puts her clothes on the discard rack. Then we leave the shop together."
        jump E3VBS3_NailJump

"She smiles."
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL129.ogg"
vb "I thought you'd like that one… Okay, I'll get it."
"I follow her to the check-out desk."

menu:
    "Offer to pay.":
        pf "Let me get that for you."
        show valerie cur
        "She blinks in surprise."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL130.ogg"
        vb "Are you sure?"
        pf "It's the least I can do after you planned our whole super fun day together."
        show valerie smi
        "She grins."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL131.ogg"
        vb "If you insist."
        "She steps back as I take out my card. Once we pay, she leads me out of the shop."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL132.ogg"
        vb "Thank you."
        pf "No problem."

    "Let her pay.":
        "She pays for her items and then leads me out of the shop."

label E3VBS3_NailJump:
show valerie hap
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL133.ogg"
vb "Time for part two!"
"She grabs my hand and pulls me forward."
pf "What are we doing next?"
"She looks back at me and winks."
show valerie smi
voice "audio/voice/MISSING/BATCH4/Valerie/ValE3Redos/E3ValerieArcS3Redo3.ogg"
vb "It's a surprise!"
pf "What is it?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL134.ogg"
vb "If I told you then it wouldn't be a surprise. Come on!"

hide valerie with dissolve

"We weave through the crowd of shoppers and stop right in front of a… {w}nail salon?"


pf "Uh, what is this?"

show valerie hap at cc with dissolve
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL135.ogg"
vb "Surprise!"
pf "I didn't sign up for this."
show valerie cur
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL136.ogg"
vb "You were the one who said you'd do everything I had planned for my mom."
pf "Uh--I mean--"
show valerie smi
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL137.ogg"
vb "Don't worry, this'll be fun!"
"She grabs my hand again and pulls me into the salon. {w}We're greeted by a young lady who asks if we've made an appointment. Valerie confirms her name and we are invited to sit in two comfortable chairs. Valerie immediately sits down and gets comfortable while she waits for the woman to return."
pf "If I sit here, do I have to get my nails done?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL138.ogg"
vb "No, but you should do it anyway."

menu:
    "I haven't done this before...":
        $ E3VBS3_GetNailed = 1
        "I sit down cautiously."
        pf "This is my first time."
        show valerie mis
        "Valerie smirks."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL139.ogg"
        vb "This is the first time you've been nailed?"
        "The heat rushes to my face."
        pf "That's not what I meant!"
        show valerie hap
        "Valerie laughs."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL140.ogg"
        vb "Don't worry, she'll be gentle."

    "I won't knock it 'til I've tried it.":
        $ E3VBS3_GetNailed = 1
        "I plop into the seat beside her."
        pf "Be gentle, this is my first time."
        show valerie hap
        "Valerie laughs."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL141.ogg"
        vb "Where's the fun in that?"

    "I'll pass.":
        pf "No thanks."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL142.ogg"
        vb "Aw, you'll be missing out!"
        pf "That's okay."
        show valerie hap
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL143.ogg"
        vb "It's super relaxing…"
        pf "I'm good."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL144.ogg"
        vb "Are you sure you want to pass up on the opportunity for a pretty girl to give you her undivided attention?"
        pf "I didn't. I'm here with you right now."
        show valerie smi
        "Valerie blinks, but seems pleased."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL145.ogg"
        vb "Alright, fine, you don't have to do it. But will you still sit with me?"
        pf "Of course."
        "I sit down in the seat beside her."

"Before long the woman returns with all of her essentials and begins by filling Valerie's nails."

if (E3VBS3_GetNailed == 1):
    "A second woman does the same with my nails."

show valerie smi
"Valerie takes in the rest of the salon and lets out a squeal of excitement."
show valerie cur
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL146.ogg"
vb "Oh! They have {i}crème de rêve{/i}!"
pf "What's that?"
"She uses her head to point to a small black vial on the counter."
show valerie hap
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL147.ogg"
vb "It's {i}crème de rêve{/i}!"
pf "...Okay?"
show valerie cur
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL148.ogg"
vb "You've never seen that before?"
pf "No."
show valerie smi
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL149.ogg"
vb "It's the best lotion ever! It makes your hands so smooth and soft. I'm surprised you've never heard of it."
pf "Sorry, I don't usually spend my time getting my nails done and checking out lotions. That's why I've never heard of creme de reve."
show note:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
"Valerie giggles."
pf "What?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL150.ogg"
vb "Sorry, your accent! It's \"crème de rêve\"."
"I listen carefully to how she pronounces it and try again."
pf "Crème de rêve…"
show valerie hap
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL151.ogg"
vb "That was really good!"

show valerie smi
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL152.ogg"
vb "Okay, try this: \"bonheur\"."

menu:
    "Bonheur.":
        "I try to mimic her as well as I can."
        pf "Bonheur."
        show valerie hap
        "Valerie giggles."
        pf "What? Did I say it wrong?"
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL153.ogg"
        vb "Oh no, that was perfect!"
        pf "Then wha…"
        "My cheeks turn red as I realise what it sounds like."
        pf "Valerie!"
        show valerie mis
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL154.ogg"
        vb "What? It's a real word. It means \"happiness\"."
        "She seems amused."

    "It's kind of hard.":
        "I grin."
        pf "Hmm, I see you like to go for the hard ones."
        show valerie hap
        "Valerie can't keep in her giggles."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL155.ogg"
        vb "What's hard?"
        pf "Bonheur… bonheur is hard."
        show valerie mis
        "Valerie bursts out laughing."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL156.ogg"
        vb "I wouldn't say that so loudly if I were you."
        pf "Is that even a real French word?"
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL157.ogg"
        vb "Yes, it means \"happiness\"."
        "She seems amused."

    "That's not going to happen.":
        pf "Yeah, I'm not saying that."
        show valerie hap
        "Valerie giggles."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL158.ogg"
        vb "Why not? It means \"happiness\"."
        pf "You know exactly why."
        "Her giggles turn to a full out laugh."
        show valerie mis
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL159.ogg"
        vb "Aw, you're no fun!"
        "She still seems amused."

show valerie smi
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL160.ogg"
vb "Alright, last one! Say \"je t'aime\"."

menu:
    "Je T'aime.":
        pf "Je T'aime."
        show valerie hap b1 with dissolve
        "Valerie smiles."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL161.ogg"
        vb "Aww."
        pf "What did I say?"
        show valerie smi b1
        show regBlush:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL162.ogg"
        vb "Something that makes me very happy."
        pf "What is it?"
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL163.ogg"
        vb "It's a secret."

    "Je Nope.":
        pf "Nice try. I'm not saying that."
        show valerie mis
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL164.ogg"
        vb "Aww, why won't you say this one? It's nothing bad."
        pf "I know. I know what it means."
        "Valerie giggles."
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL165.ogg"
        vb "Too bad."

if (E3VBS3_GetNailed == 1):
    "Our nails are finished and the women start straightening their stations."
    show valerie smi with dissolve
    voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL166.ogg"
    vb "Let me see!"
    "I show Valerie my freshly filed and pampered nails."
    voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL167.ogg"
    vb "Ooh, so pretty!"
    "I'll admit, they aren't too shabby."

else:
    "The woman finishes up Valerie's nails and begins straightening her station."

show valerie hap with dissolve
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL168.ogg"
vb "Look!"
"She flashes me her brightly painted nails."
show valerie smi
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL169.ogg"
vb "Aren't they pretty?"
pf "Yup, very nice."

if (E3VBS3_GetNailed == 0):
    voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL170.ogg"
    vb "You missed out."
    "I shrug. I don't regret my choice."

"Once we leave the salon, Valerie turns to me again."
show valerie mis
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL171.ogg"
vb "Are you ready for your last surprise?"
pf "I don't think I can handle another surprise…"
"She laughs and grabs my hand again."
show valerie hap
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL172.ogg"
vb "Don't be such a baby! You'll love this one. I promise!"

stop music fadeout 15
scene black with fade
"She hurries down the hall and flies right through a door marked \"Employee Only\"."
pf "Uh… Valerie… Where are we going?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL173.ogg"
vb "You'll see!"
"Although I'm a little nervous, I follow her up a series of stairs. Once my breathing starts to turn laborious, we reach the top of the staircase. Valerie pushes open a heavy door and I step out into the fresh air."

play ambient "audio/ambience/Rooftop.ogg" fadein 3
scene bg campus rooftop dusk with Dissolve(2.5):
    xzoom .925
    yzoom .925

show valerie mis b1 at cc with dissolve
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL174.ogg"
vb "What do you think?"
"The sun blazes a colourful trail in the sky as it sets towards the horizon. The rooftops of Isokaze look so small from up here as the lights of the city slowly sparkle on."
pf "This is amazing…"
"Valerie grins and leans on the railing, staring out into the city. I join her, and we enjoy the peace as the sun gradually settles down."
show valerie smi b1
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL175.ogg"
vb "Thank you."
"I turn to her, but she's still looking at the skyline."
pf "For what?"
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL176.ogg"
vb "For spending the whole day with me even though you didn't have to."
pf "I had a lot of fun."
show valerie mis b1
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL177.ogg"
vb "I know you're just saying that--"
pf "No, I mean it. I always have fun with you."
"She glances sideways at me."
show valerie hap b1
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL178.ogg"
vb "I'm so glad I moved to Japan."
"She faces me."
show valerie smi b1
show heart:
    xoffset 720
    yoffset 125
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL179.ogg"
vb "Meeting you has made starting over easy."
"Her gaze locks onto my own and she waits expectantly."

menu:
    "Hug her.":
        stop ambient fadeout 5
        play music "audio/music/You and I (GAME VERSION).ogg" fadein 7
        "I know exactly how she feels. I wrap my arms around her and hold her in an embrace."
        show valerie smi b2 with dissolve
        "Valerie responds immediately and holds me tight. She lingers into the hug, not wanting to let me go."

        menu:
            "Kiss her.":
                "I don't want to let her go either. I want to show her how I feel, but I need to be certain of my feelings."
                "Do I want to do this?"
                menu:
                    "Yes." if E3D4KI_Embraced == 0:
                        $ valrelatonship = 1
                        "I've never been more certain in my life."
                        scene black with fade
                        "Whenever I'm with her it feels like the world falls away and there is only the two of us. That kind of connection is hard to find. She's electric and fantastic and always keeps me guessing."
                        "Now it's my turn to be spontaneous."
                        
                        $ persistent.gpix[56][0] = 1
                        show cg valerie kiss 1:
                            alpha 0
                            xzoom .55
                            yzoom .55
                            yoffset -50
                            xoffset 50
                            
                        show cg valerie kiss 1:
                            parallel:
                                easein 2.0 alpha 1.0
                            parallel:
                                easein 2.0 xoffset 0


                        $renpy.pause(2.0)
                        "I lean in close, aiming for her cheek, when Valerie turns her head at the last second and my lips meet hers."
                        "I break away in surprise. She tastes like strawberries and I can't believe how soft her lips are."
                        "Valerie grins."
                        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL181.ogg"
                        vb "You missed."
                        "I match her smile."
                        pf "Right on target, actually."
                        "Her cheeks tinge pinks and she looks down. Her hand slips into mine and I squeeze it gently. Then she gets on her toes and kisses me again."
                        
                        $renpy.pause(2.0)
                        scene black with fade
                        
                        "We enjoy each other's company in the tranquility of the dusk until the stars twinkle in the sky and it's time to head home."
                        stop music fadeout 5
                        stop ambient fadeout 3
                        $renpy.pause(2.5)
                        $ E3VBS3_Completed = 1
                        jump E3D6S2

                    "No.":
                        "Actually, I don't think I feel the same way about her."
                        jump E3VBS3_BackLabel

            "Gently pull away.":
                stop music fadeout 7
                play ambient "audio/ambience/Rooftop.ogg" fadein 3
                label E3VBS3_BackLabel:
                show valerie cur with dissolve
                "I slowly detangle myself from her arms. Valerie reluctantly lets go. Although her face still holds a smile, her eyes seem disappointed."
                show valerie smi
                voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL180.ogg"
                vb "Well, I still have more on the agenda if you'd like to continue…"
                pf "I'm game if you are."
                "She nods and heads back through the door. I follow her back into the mall."



    "This was platonic.":
        pf "I understand. Friends always make a transition feel less painful."
        show valerie cur with dissolve
        "She furrows her brow as she explores my eyes, then sighs. She shakes her slightly as if to clear her mind, and smiles."
        show valerie smi
        voice "audio/voice/E3/Free/VB/S3/valerie/E3ValArcL182.ogg"
        vb "Come on, there's one more store I want to go to."
        "She heads back through the door and I follow her into the mall."

scene black with fade

"We continue to check off everything Valerie has on her list. By the time we're done, it's gotten late so we head home."


stop music fadeout 5
stop ambient fadeout 3
$renpy.pause(2.5)
$ E3VBS3_Completed = 1
jump E3D6S2
