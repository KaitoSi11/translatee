#
label E3YMS3:


$ yuuOut = "sFashion"
$ yuuHairB = "default"
$ yuuHairF = "default"


"Between the cooking club and the improv class, hanging out with Yuuna has been a blast! I wonder if she's up to anything new today."

play sound "audio/sfx/Technology/Phone Dial.ogg"
"I pull out my phone and dial her number."
"It rings...{w}a few times...{w}still going..."

play sound "audio/sfx/Technology/Phone Answer.ogg"
$renpy.pause(1.0)
voice "audio/voice/E3/Free/YM/S3/yuuna/61.ogg"
ym "Hello?"
pf "Hey, Yuuna."
voice "audio/voice/E3/Free/YM/S3/yuuna/62.ogg"
ym "Oh, hi! Sorry about the delay in picking up. I was working on something and left my phone upstairs."
pf "Oh, sorry if I'm interrupting..."
voice "audio/voice/E3/Free/YM/S3/yuuna/63.ogg"
ym "It's okay, I'm just practicing my English."
pf "English?"
voice "audio/voice/E3/Free/YM/S3/yuuna/64.ogg"
ym "Yes."
"A few seconds of silence pass."
voice "audio/voice/E3/Free/YM/S3/yuuna/65.ogg"
### VOICE - used to read "I have a test up and coming for speaking" but voice gave difference
ym "{b}I have a test coming up and coming for speaking!{/b}"
pf "{b}I have a speaking test coming up{/b} would be the more natural way to say it."
voice "audio/voice/E3/Free/YM/S3/yuuna/66.ogg"
ym "Oh, I see. I thought it sounded a bit off."

menu:
    "Want to practice with me?":
        pf "If the test is for conversing in English, I can help out if you like."
        "Yuuna answers enthusiastically."
        voice "audio/voice/E3/Free/YM/S3/yuuna/67.ogg"
        ym "Really? You don't mind?"
        pf "Not at all!"
        voice "audio/voice/E3/Free/YM/S3/yuuna/68.ogg"
        ym "Then, yes, I'd love your help!"
        "I chuckle."
        pf "You didn't even have to think about it first!"
        "Yuuna laughs."
        voice "audio/voice/E3/Free/YM/S3/yuuna/69.ogg"
        ym "I was actually going to call you for help but I figured you didn't want to spend your Saturday teaching me English… especially when my speaking level is equivalent to that of a child."
        pf "I don't mind."
        jump E3YMS3_HelpHer

    "Good luck with your studying.":
        pf "Well, I better let you get back to your thing."
        voice "audio/voice/E3/Free/YM/S3/yuuna/70.ogg"
        ym "Wait!"
        pf "Hm?"
        voice "audio/voice/E3/Free/YM/S3/yuuna/71.ogg"
        ym "Umm..."
        voice "audio/voice/E3/Free/YM/S3/yuuna/72.ogg"
        ym "If you aren't busy, and um... don't mind... do you think I can practice my English with you?"

        menu:
            "Of course!":
                pf "Sure."
                voice "audio/voice/E3/Free/YM/S3/yuuna/73.ogg"
                ym "Really? I don't want to ruin your Saturday afternoon."
                pf "Don't worry about it. This sounds like fun!"

                label E3YMS3_HelpHer:
                    voice "audio/voice/E3/Free/YM/S3/yuuna/74.ogg"
                    ym "Thank you so much! Do you want to meet at the library?"
                    pf "On campus?"
                    voice "audio/voice/E3/Free/YM/S3/yuuna/75.ogg"
                    ym "No, I was thinking of the one in Isokaze. We should both be pretty close to it."
                    pf "Sounds like a plan. I'll see you soon."
                    voice "audio/voice/E3/Free/YM/S3/yuuna/76.ogg"
                    ym "Okay! See you there."

            "I'll pass.":
                $ E3D6S1_ChoseYuuna = 0
                pf "I actually have some other plans."
                voice "audio/voice/E3/Free/YM/S3/yuuna/77.ogg"
                ym "Oh okay."
                pf "Sorry."
                voice "audio/voice/E3/Free/YM/S3/yuuna/78.ogg"
                ym "Don't worry about it!"
                "This just got really awkward."
                pf "Uh yeah, anyway... See you."
                voice "audio/voice/E3/Free/YM/S3/yuuna/79.ogg"
                ym "Have a great weekend."
                "I hang up."
                "Based on that decision, I can safely conclude..."
                jump E3D6S1_Loner



"After hanging up, I search directions to the library on my phone. {w}It's only a short drive away! Good call, Yuuna. I ready myself and head out."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)
play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(5.5)


"Once I'm nearby the library, I'm impressed by the magnificence of the building."
"It's a lot larger than the one at ACE and the outside architecture is reminiscent of the building style of 30 years ago. It's a great contrast among the more modern structures surrounding it. I can tell the library has a lot of history."
"I park my bike on the street and follow the path to the library."

scene bg isokaze park day with fade

"The path winds through a quaint park with luscious greenery and a small fountain."
"Food trucks park along the edges offering tasty treats like ice cream and taiyaki."

"Before I enter the library, I shoot Yuuna a quick text to let her know I'm here. She responds immediately, telling me to meet her on the second floor."

scene black with fade

play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
scene bg campus library day with fade

$renpy.pause(1.0)

"The inside of the library is every bit as modern and reminiscent as the one at ACE. It doesn't surprise me. Our modern facilities are the most comfortable and technically relevant. It's much more conducive to research."

"Yuuna greets me at the top of the stairs."


play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 10
show yuuna hap at cc with dissolve
$renpy.pause(.5)
voice "audio/voice/E3/Free/YM/S3/yuuna/80.ogg"
ym "You're here!"
"I nod."
show yuuna smi
voice "audio/voice/E3/Free/YM/S3/yuuna/81.ogg"
ym "I managed to book us a private room so we can chat at a normal volume without disturbing anyone."
pf "Sounds good to me!"

hide yuuna with dissolve

"I follow her into the study room. Whereas the private study rooms at ACE also had the basic tables and chairs, this room has a touchscreen wall. Very nice! {w}Yuuna's notes are already spread across the table." 

show yuuna smi at cc with dissolve

if (E2YMS3_Completed == 1):
    pf "I'll admit I'm a little surprised you said you needed help with English speaking."
    pf "After all, {i}Hamlette{/i} is pretty advanced literature…"

else:
    pf "I didn't know you were studying English."
    voice "audio/voice/E3/Free/YM/S3/yuuna/82.ogg"
    ym "Yeah, I chose it as my foreign language. It's not too hard except for the speaking part…"
    pf "How come?"
    
voice "audio/voice/E3/Free/YM/S3/yuuna/83.ogg"
ym "Oh, well, I find reading and writing to be a lot easier to grasp because I have more time to think about what I want to say. Plus, I can review what I've already read or written to make sure I'm understanding everything correctly."
"She gives me a shaky smile."
show yuuna thi
voice "audio/voice/E3/Free/YM/S3/yuuna/84.ogg"
ym "But speaking doesn't offer that luxury. I feel like I'm put on the spot, because I kind of am, and I have to respond quickly and correctly. It's really stressful!"
show yuuna cur
voice "audio/voice/E3/Free/YM/S3/yuuna/85.ogg"
ym "Plus, it's hard to pronounce everything right…"
show yuuna smi
voice "audio/voice/E3/Free/YM/S3/yuuna/86.ogg"
ym "I'm a little jealous by how well you speak Japanese even though it's not your first language."

menu:
    "I use it all the time.":
        pf "Nikki and I speak Japanese to each other at home. Plus, my mom used to only speak Japanese to us even while we were living in the States."
        voice "audio/voice/E3/Free/YM/S3/yuuna/87.ogg"
        ym "Oh! So you've had constant practice!"
        pf "Yep."

    "I am kind of amazing, aren't I?":
        pf "It's one of my many talents."
        show yuuna mis
        voice "audio/voice/E3/Free/YM/S3/yuuna/88.ogg"
        ym "So humble!"
        pf "I call it confidence."
        "She giggles."

    "Eh, I guess.":
        pf "It worked out, I suppose."
        "Yuuna smiles."

pf "Anyway, how did you want to practice?"
show yuuna smi
voice "audio/voice/E3/Free/YM/S3/yuuna/89.ogg"
ym "The exam will be formatted to simulate a conversation, so maybe we can just have a normal conversation?"

pf "{b}Sounds good to me.{/b}"
show yuuna cur
voice "audio/voice/E3/Free/YM/S3/yuuna/90.ogg"
ym "Wait, are we starting?"
pf "{b}We already have!{/b}"
voice "audio/voice/E3/Free/YM/S3/yuuna/91.ogg"
ym "{b}Ah! Okay!{/b}"
show yuuna smi
"She smiles."
voice "audio/voice/E3/Free/YM/S3/yuuna/92.ogg"
ym "{b}My name is Yuuna, Yuuna Misaki.{/b}"

menu:
    "I am [pfull].":
        pf "{b}My name is [pfull]. I go to ACE Academy{/b}!"
        show yuuna hap
        voice "audio/voice/E3/Free/YM/S3/yuuna/93.ogg"
        ym "{b}Me too! I am also a student at ACE Academy.{/b}"
        voice "audio/voice/E3/Free/YM/S3/yuuna/94.ogg"
        ym "{b}I am studying...{/b}"
        show yuuna thi
        "She wrinkles her nose as she tries to think of the word."
        show yuuna smi
        voice "audio/voice/E3/Free/YM/S3/yuuna/95.ogg"
        ym "{b}...in the medical program!{/b}"
        pf "{b}Physiotherapy?{/b}"
        show yuuna hap
        voice "audio/voice/E3/Free/YM/S3/yuuna/96.ogg"
        ym "{b}Yes! Thank you for reminding me.{/b}"
        pf "{b}You're welcome.{/b}"

    "They call me Ceonardo Di Laprio.":
        pf "{b}Hello, I am Ceonardo Di Laprio!{/b}"
        show yuuna cur
        "Yuuna blinks in confusion."
        voice "audio/voice/E3/Free/YM/S3/yuuna/97.ogg"
        ym "What? I don't--"
        pf "{b}You're speaking Japanese!{/b}"
        "Her eyes widen. She recomposes herself."
        show yuuna smi
        voice "audio/voice/E3/Free/YM/S3/yuuna/98.ogg"
        ym "{b}Your name is different than I thought! I was confused.{/b}"
        "I smile. She recovered from that smoothly!"

        
stop ambient fadeout 3
scene black with fade



"We continue to speak in English, and even though there are the occasional pauses as Yuuna tries to recall a word or how to express her thoughts, she manages to carry the conversation for a long time."
"Sometimes she'll stop the conversation to check her pronunciation."
"The more we practice, the more she improves. The halts in her speech lessen and she speaks with greater confidence." 

scene bg campus library day with fade
$renpy.pause(1.0)

show yuuna hap at cc with dissolve
$renpy.pause(.5)

pf "{b}We've talked about so many things today!{/b}"
voice "audio/voice/E3/Free/YM/S3/yuuna/99.ogg"
ym "{b}Yes we have.{/b}"

show yuuna smi

"Yuuna smiles."
voice "audio/voice/E3/Free/YM/S3/yuuna/100.ogg"
ym "{b}I am much better at oral now thanks to you!{/b}"

menu:
    "Oh my...":
        stop music fadeout 5
        $ E3YMS3_Choice1 = 1
        "I'm too stunned to respond but my cheeks immediately flush red."
        show yuuna cur with dissolve
        "Yuuna's eyes widen at my strange reaction."
        voice "audio/voice/E3/Free/YM/S3/yuuna/101.ogg"
        ym "W-Why are you acting like that?"

    "Hahaha!":
        stop music fadeout 5
        $ E3YMS3_Choice1 = 2
        "I burst out laughing."
        show yuuna cur with dissolve
        voice "audio/voice/E3/Free/YM/S3/yuuna/102.ogg"
        ym "Ah! W-What are you doing?"
        "I cant stop myself as tears well up in my eyes. Yuuna shifts uncomfortably."
        voice "audio/voice/E3/Free/YM/S3/yuuna/103.ogg"
        ym "Was it something I said...?"

    "Better at {i}speaking.{/i}":
        stop music fadeout 8
        $ E3YMS3_Choice1 = 3
        pf "You mean: {b}I am much better at speaking now{/b}."
        show yuuna cur with dissolve
        "Yuuna blinks."
        show yuuna thi
        voice "audio/voice/E3/Free/YM/S3/yuuna/104.ogg"
        ym "Oh... I thought {b}oral{/b} means speaking."
        pf "It does...but..."
        show yuuna cur
        "She looks at me unsure."

"Hmm… should I tell her? It might make things awkward."

menu:
    "She should know what it means in case.":
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
        pf "The way you phrased {b}oral{/b} in your sentence..."
        "She listens closely."
        pf "Uh, it can be interpreted as..."
        "This is difficult to phrase without coming off as perverted."
        "She listens raptly to my every word. How am I supposed to explain this?!"
        pf "So {b}oral{/b} can mean speaking, but it is also related to the mouth."
        voice "audio/voice/E3/Free/YM/S3/yuuna/105.ogg"
        ym "Okay..."
        pf "The way you phrased your sentence, it can be interpreted as slang for... sexual pleasure derived from--"
        show yuuna sur b2 with dissolve
        $renpy.pause(1.0)
        show yuuna win b3 with dissolve
        voice "audio/voice/E3/Free/YM/S3/yuuna/106.ogg"
        ym "I-I understand!"
        "Yuuna interrupts me and her face turns bright red."
        voice "audio/voice/E3/Free/YM/S3/yuuna/107.ogg"
        ym "I d-d-didn't m-m-ean… ah!"
        "She buries her face in her hands."
        show yuuna thi b2 with dissolve
        "After she has a chance to compose herself, she emerges from behind her hands. Her face is still red."
        pf "Uh... I guess it's better you found out from me instead of saying it to the professor."
        show yuuna sur b2 with dissolve
        "Yuuna's eyes widen in horror."
        stop music fadeout 4
        voice "audio/voice/E3/Free/YM/S3/yuuna/108.ogg"
        ym "I would have died if that happened!"
        "I don't think she's kidding!"
        show yuuna ner b1 with dissolve
        voice "audio/voice/E3/Free/YM/S3/yuuna/109.ogg"
        ym "Thanks for telling me though... I umm... wouldn't have known otherwise."
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
        "I don't think Yuuna will ever say \"oral\" again."
        

    "I don't want to tarnish her innocence.":
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
        "There's no reality I can think of in which this conversation will end well."
        pf "It's nothing."
        
        if (E3YMS3_Choice1 == 1):
            pf "I was just thinking about something embarrassing I said earlier."

        if (E3YMS3_Choice1 == 2):
            pf "I just remembered a really funny joke Shou told me. Sorry about that."

        if (E3YMS3_Choice1 == 3):
            pf "It's a change of phrasing... nothing too different."

        show yuuna neu with dissolve
        voice "audio/voice/E3/Free/YM/S3/yuuna/110.ogg"
        ym "Okay..."
        "She doesn't seem convinced."
        pf "Maybe you can do a search on English slang since some words have different meanings."
        show yuuna cur
        "Yuuna lights up with interest."
        voice "audio/voice/E3/Free/YM/S3/yuuna/111.ogg"
        ym "Ah, yes! Slang! Certain phraseology can be interpreted differently."
        show yuuna smi
        voice "audio/voice/E3/Free/YM/S3/yuuna/112.ogg"
        ym "I didn't even consider studying that. Thank you!"
        pf "You're welcome."
        pf "{size=12}Just make sure you don't use an image search engine.{/size}"
        show yuuna cur
        voice "audio/voice/E3/Free/YM/S3/yuuna/113.ogg"
        ym "Im sorry?"
        pf "Nothing!"

show yuuna thi with dissolve
"Yuuna looks at the mound of notes still on her table and sighs."
pf "What's wrong?"
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/114.ogg"
ym "I still have homework I need to complete for all of my other classes, but I've been so focused on my exam that I haven't even started on anything else."
voice "audio/voice/E3/Free/YM/S3/yuuna/115.ogg"
ym "And I have some logistical stuff to take care of for the Dasshu event tomorrow."
pf "You mean for the photoshoot?"
"She nods."
"Yuuna will burn out if she hops right into more work."
pf "Maybe you should take a break before tackling all that?"
voice "audio/voice/E3/Free/YM/S3/yuuna/116.ogg"
ym "I don't know… I don't think I have time for one."
"She doesn't seem thrilled by the idea of more work. I think she can be persuaded."
pf "Alright, but since I helped you with your English you have to do me a favour first."
show yuuna cur
"Yuuna looks at me."
voice "audio/voice/E3/Free/YM/S3/yuuna/117.ogg"
ym "Oh, um, okay. What is it?"
"I need to think of an excuse to get her out of the library. What if we... oh I got it!"
pf "Ice cream!"
voice "audio/voice/E3/Free/YM/S3/yuuna/118.ogg"
ym "Ice cream?"
pf "Yes, I saw a vendor outside. You owe me one ice cream cone. Consider it payment for my tutoring services!"
show yuuna hap
"Yuuna laughs."
voice "audio/voice/E3/Free/YM/S3/yuuna/119.ogg"
ym "I suppose that's only fair."
"Success!"
pf "Shall we?"
show yuuna smi
voice "audio/voice/E3/Free/YM/S3/yuuna/120.ogg"
ym "Sure!"


stop ambient fadeout 3.0
scene black with fade

"She packs up her stuff and we head out of the library and straight for the ice cream truck."

play ambient "audio/ambience/Morning.ogg" fadein 3
scene bg isokaze park day with fade:
    yoffset -50
    xoffset -100

"Laughter and chatter floats on the cool breeze. I take in the ambiance as we wait in line. Yuuna studies the flavours, but glances at me when she feels my gaze on her. She flashes me a smile."
voice "audio/voice/E3/Free/YM/S3/iceman/1.ogg"
iceman "Next!"
"We walk up to the window."
voice "audio/voice/E3/Free/YM/S3/iceman/2.ogg"
iceman "Hello there young miss, what can I get for you?"

show yuuna smi at cc with dissolve

### NOTE - might change flavor to strawberry to match art, depends on voice file available
voice "audio/voice/E3/Free/YM/S3/yuuna/121.ogg"
ym "Hi, I'll just have vanilla please."
voice "audio/voice/E3/Free/YM/S3/iceman/3.ogg"
iceman "Of course! And for you, young man?"
stop music fadeout 25
pf "I'll get pistacchio ice cream if you have it."
voice "audio/voice/E3/Free/YM/S3/iceman/4.ogg"
iceman "Coming right up!"
show dots:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna cur
"Yuuna looks at me at me with curiosity."
pf "What's up?"
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/122.ogg"
ym "Um, nothing."
pf "Okay."
"It certainly doesn't feel like nothing."
voice "audio/voice/E3/Free/YM/S3/iceman/5.ogg"
iceman "Here you go!"
show yuuna smi
voice "audio/voice/E3/Free/YM/S3/yuuna/123.ogg"
ym "Thanks."
pf "Thank you."
"I go to pay, but Yuuna already has her card out and hands it to the man."

menu:
    "Let me pay!":
        "I scramble to pull out my wallet but Yuuna shakes her head."
        voice "audio/voice/E3/Free/YM/S3/yuuna/124.ogg"
        ym "I owe you one, remember?"
        pf "No, it's okay--"
        "The ice cream man hands Yuuna her card after tapping it against the machine."
        voice "audio/voice/E3/Free/YM/S3/iceman/6.ogg"
        iceman "Enjoy!"
        "I guess this battle is over before it began."

    "Free ice cream is the best ice cream!":
        "I happily lap at my cone, enjoying my ice cream like a child."
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap
        "Yuuna looks at me and laughs."

    "Each pay for our own?":
        pf "You don't have to pay for mine."
        voice "audio/voice/E3/Free/YM/S3/yuuna/125.ogg"
        ym "Consider it payment for helping me with my English practice! I won't take no for an answer."
        "I blink. She smiles but seems adamant."
        pf "If you say so."
        "She nods and pays for the ice creams."

hide yuuna with dissolve
"After she pays, Yuuna points to a bench."
voice "audio/voice/E3/Free/YM/S3/yuuna/126.ogg"
ym "Let's go take a seat."
pf "Alright."
hide yuuna with dissolve

"We sit down and stay silent as we enjoy our frozen treat. Every so often I catch her staring at my ice cream."

show yuuna cur at cc with dissolve

pf "...It seems like you wanted pistachio too."

show yuuna thi with dissolve
"Yuuna quickly looks away."
show drop:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/YM/S3/yuuna/127.ogg"
ym "Ah, sorry for staring. It's nothing like that."
pf "What is it?"
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/128.ogg"
ym "It's just a really strange choice of flavour."
pf "...I'm sorry?"
show yuuna ner
"Her eyes widen as she realises how that came across."
show panic:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/YM/S3/yuuna/129.ogg"
ym "Wait! I don't mean it in a bad way. I just mean it's not a popular flavour here."
show yuuna thi
voice "audio/voice/E3/Free/YM/S3/yuuna/130.ogg"
ym "There's only one person I knew who liked pistachio flavour the best..."
stop ambient fadeout 10
"Her eyes become a little dimmer."

if (MCStory == 3):
    "She said {i}knew{/i}..."

else:
    "I wonder who she's talking about..."

menu:
    "Your boyfriend.":
        pf "Your boyfriend?"
        show yuuna cur b1 with dissolve
        "Her cheeks blush."
        voice "audio/voice/E3/Free/YM/S3/yuuna/131.ogg"
        ym "I don't have a boyfriend!"
        pf "...An ex?"
        show yuuna thi b1 with dissolve
        voice "audio/voice/E3/Free/YM/S3/yuuna/132.ogg"
        ym "I-I've never been in a relationship."
        pf "Oh."

    "Your coworker":
        pf "Someone you worked with?"
        show yuuna neu
        "She shakes her head."
        voice "audio/voice/E3/Free/YM/S3/yuuna/133.ogg"
        ym "No..."

    "Your friend":
        pf "A friend?"
        show yuuna neu
        voice "audio/voice/E3/Free/YM/S3/yuuna/134.ogg"
        ym "Something like that."
        pf "Do you mean me?"
        show yuuna smi
        "She smiles but it's not as cheerful as before."
        ### VOICE - line change ?
        voice "audio/voice/E3/Free/YM/S3/yuuna/135.ogg"
        ym "Oh, I know two people who like it now…" #but I didn't mean you."

    "{color=#00ff00}{b}Family.{/b}{/color}" if (MCStory == 3):
        jump E3YMS3_TrackJump
        
    "Family." if (MCStory != 3):
        label E3YMS3_TrackJump:
        pf "Do you mean Yuudai?"
        show exclamation:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna sur with dissolve
        $renpy.pause(1.0)
        show yuuna neu with dissolve
        "She blinks at me in surprise. But then nods."
        jump E3YMS3_BrotherConvergence


pf "So who was it?"
show yuuna neu with dissolve
"She looks a little reluctant to answer, then sighs."
voice "audio/voice/E3/Free/YM/S3/yuuna/136.ogg"
ym "Yuudai, my brother."

label E3YMS3_BrotherConvergence:
play music "audio/music/Kaori Itami (GAME VERSION).ogg" fadein 10
show yuuna dis with dissolve
"Yuuna becomes quiet. She looks away, but not before I catch the way her eyes glisten."
"She rubs at her eyes."
voice "audio/voice/E3/Free/YM/S3/yuuna/137.ogg"
ym "Anyway, it doesn't matter now."
pf "It does matter."
show yuuna neu
"She looks curiously at me."
pf "I don't know what happened to your brother, but I know it must have been something tragic."
voice "audio/voice/E3/Free/YM/S3/yuuna/138.ogg"
ym "How?"
pf "I can tell from the way everyone avoids his name."
"She hangs her head."
show yuuna dis
voice "audio/voice/E3/Free/YM/S3/yuuna/139.ogg"
ym "They do it because of me."
pf "You don't have to feel guilty."
"She gives me that look again, a mixture of curiosity and bewilderment."
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/140.ogg"
ym "How did you know that?"
pf "Because I know what it's like to lose someone you love."
"Her look softens."
pf "Do you know why I came to Isokaze?"
voice "audio/voice/E3/Free/YM/S3/yuuna/141.ogg"
ym "To join the pilot program at ACE…"
pf "That's only part of it. I came here so Nikki wouldn't have to be alone after our parents died."
show yuuna sur with dissolve
"Her eyes widen, then she looks down."
show yuuna sad dissolve
voice "audio/voice/E3/Free/YM/S3/yuuna/142.ogg"
ym "I'm sorry..."
pf "It's okay... I… I don't talk about them much. Not even with Nikki. I don't want to think about what happened to them, and sometimes I feel guilty because it feels like I'm trying not to think of them…"
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/143.ogg"
ym "That's exactly how I feel."
"Yuuna takes a deep breath."
voice "audio/voice/E3/Free/YM/S3/yuuna/144.ogg"
ym "Yuudai was a pilot too."
voice "audio/voice/E3/Free/YM/S3/yuuna/145.ogg"
ym "He was actually the captain of the same team Akira is in now, and Dasshu was their first sponsor. Yuudai was ACE Academy's hidden jewel. Everyone noticed his potential, and he already had offers waiting for him before he even graduated."
show yuuna sad
voice "audio/voice/E3/Free/YM/S3/yuuna/146.ogg"
ym "...But then it happened."
"I stay quiet."
voice "audio/voice/E3/Free/YM/S3/yuuna/147.ogg"
ym "He had a cardiac arrest during one of his matches..."
"I blink in surprise. In all my musings and wonderings, hadn't even considered that to be a possibility!"
pf "How did that happen? Pilots are usually in the peak of health."
show yuuna dis
"Yuuna nods."
voice "audio/voice/E3/Free/YM/S3/yuuna/148.ogg"
ym "We were just as surprised. A few months earlier, though, he'd developed high blood pressure. He had medication to keep it in order."
voice "audio/voice/E3/Free/YM/S3/yuuna/149.ogg"
ym "But during that match, he didn't take his medication."
pf "...Oh."
voice "audio/voice/E3/Free/YM/S3/yuuna/150.ogg"
ym "He didn't forget. He wasn't like that."
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/151.ogg"
ym "You know that during season matches you're subjected to drug tests, right?"
"I nod. That was standard practice back at CINY too. It's probably standard for all schools."
voice "audio/voice/E3/Free/YM/S3/yuuna/152.ogg"
ym "If he'd taken his medication, it would have showed up on the report."
voice "audio/voice/E3/Free/YM/S3/yuuna/153.ogg"
ym "And then that would have revealed his health condition, which would have not only disqualified him from the match, but also jeopardised his entire piloting career."
"Yuuna looks down."
show yuuna sad with dissolve
voice "audio/voice/E3/Free/YM/S3/yuuna/154.ogg"
ym "Being a pilot was his dream."

"I think I remember a discussion Yuuna and I had a while back in which she'd mentioned pilots were punished for properly containing certain disorders because their medications were considered a risk. No wonder she's been so adamant for reform..."
stop music fadeout 10
"I'm quiet as I let all of this sink in."
pf "That's a very messed up situation... but being a pilot myself I can see where he was coming from..."
"Yuuna nods."
show yuuna dis
voice "audio/voice/E3/Free/YM/S3/yuuna/155.ogg"
ym "Me too. That's why I decided to study piloting health. How many pilots do you think have suffered the same fate as my brother because they feared the dream they worked so hard to achieve would be taken away? And most of the time, it's through no fault of their own." 
"I nod. I can hear the pain in her voice, but there's nothing I can say that will make her hurt go away. She falls silent."
show yuuna neu
voice "audio/voice/E3/Free/YM/S3/yuuna/157.ogg"
ym "Thanks."
pf "For what?"
voice "audio/voice/E3/Free/YM/S3/yuuna/158.ogg"
ym "I haven't told anyone this before. I didn't think I was ready to talk about him, but… now that I have…"
show yuuna smi with dissolve
"She smiles at me and there seems to be a spark of hope in her eyes. Maybe now she can start to heal."
voice "audio/voice/E3/Free/YM/S3/yuuna/159.ogg"
ym "I'm glad."
"I match her smile."
pf "That's what I'm here for."
$renpy.pause(1.0)
show yuuna sur
"{i}Plop!{/i}"
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
scene black with fade
"We blink at each other then look at Yuuna's hand. More specifically, her naked cone."
$ persistent.gpix[69][0] = 1
$ persistent.gpix[70][0] = 1
$ persistent.gpix[71][0] = 1
show cg yuuna icecream 1 with dissolve:
    xzoom 0.5
    yzoom 0.5

"She must have tilted it during our conversation and the ice cream slid right off the cone and onto the bench."
voice "audio/voice/E3/Free/YM/S3/yuuna/160.ogg"
ym "No! Ice cream!"
show cg yuuna icecream 2 with dissolve:
    xzoom 0.5
    yzoom 0.5
"She pouts, and looks so crestfallen, I can't stop my smile. I try to hide my amusement, but she looks so cute when she's dejected."
"Unfortunately, she notices my failed attempt at keeping cool and sticks out her lip."
voice "audio/voice/E3/Free/YM/S3/yuuna/161.ogg"
ym "This isn't funny!"
pf "You have to admit, it's a little funny."
"She shakes her head."
show cg yuuna icecream 3 with dissolve:
    xzoom 0.5
    yzoom 0.5
voice "audio/voice/E3/Free/YM/S3/yuuna/162.ogg"
ym "Not even the slightest!"

menu:
    "Time to get another cone.":
        pf "Let's go get you another one!"
        scene black with fade
        scene bg isokaze park day with fade:
            yoffset -50
            xoffset -100
        show yuuna hap at cc with dissolve
        "Yuuna beams."
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/YM/S3/yuuna/163.ogg"
        ym "Okay!"
        hide yuuna with dissolve
        "We clean up the mess as best we can and go back in line to get Yuuna another ice cream cone."
        "She finishes this one in record time! I guess she didn't want it to suffer the same fate as the last one."

    "Let's share mine.":
        pf "...Do you want to share mine?"
        scene black with fade
        scene bg isokaze park day with fade:
            yoffset -50
            xoffset -100
        "I offer her my cone."
        show yuuna ner b2 at cc with dissolve
        "Her cheeks flush and she shakes her head."
        voice "audio/voice/E3/Free/YM/S3/yuuna/164.ogg"
        ym "I couldn't..."
        pf "I don't mind."
        show yuuna cur b2
        voice "audio/voice/E3/Free/YM/S3/yuuna/165.ogg"
        ym "...Are you sure…?"
        "I nod."
        show yuuna smi b2
        "She tucks her hair behind her ear, leans in close, and bites off a part of the ice cream."
        pf "Wait, what?"
        show yuuna cur b2
        voice "audio/voice/E3/Free/YM/S3/yuuna/166.ogg"
        ym "What?"
        pf "...You can just bite ice cream like that?"
        show yuuna smi b2
        "She nods, smiling happily."
        pf "You are not human. No one should be able to do that!!"
        show yuuna hap b2
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        "She starts to giggle but quickly puts her hand in front of her mouth."
        "I laugh."
        "We finish the ice cream together."

    "SUCKS TO BE YOU.":
        "I laugh hysterically."
        pf "Hahaha! Guess who still has a perfectly delicious ice cream?"
        "I take a lick."
        pf "Mmm, so good!"
        "Suddenly, Yuuna slaps the cone out of my hand. My poor ice cream lands right beside Yuuna's."
        pf "No! Icecream!"
        "Yuuna pouts."
        voice "audio/voice/E3/Free/YM/S3/yuuna/167.ogg"
        ym "Serves you right for being so mean!"
        "She crosses her arms. We both look at each other and crack up laughing. We try to clean up the mess as best as we can."
        scene black with fade
        scene bg isokaze park day with fade:
            yoffset -50
            xoffset -100

show yuuna smi b1 at cc with dissolve
pf "Do you want to get back to studying?"
voice "audio/voice/E3/Free/YM/S3/yuuna/168.ogg"
ym "Yeah... but before I do, I want to show you something."
"She grabs my hand with both of hers."
show yuuna hap b1
voice "audio/voice/E3/Free/YM/S3/yuuna/169.ogg"
ym "C'mon!"
pf "Woah! Okay."

scene black with fade

"She leads me through the park, frequently glancing back at me with excited smiles. The further we go into the trees, the fewer people we see milling around."
"Yuuna stops abruptly."
voice "audio/voice/E3/Free/YM/S3/yuuna/170.ogg"
ym "We're here."
play ambient "audio/ambience/Shoreline.ogg" fadein 1
scene bg isokaze park2 day with Dissolve(2.5):
$renpy.pause(0.75)
"Trees surround us on all sides, only opening up to frame a picturesque view of the ocean. The clear, blue sky blends into the deep blue of the water. Birds sing a soft melody in the trees, complementing the serenity of the place."
show yuuna smi b1 at cc with dissolve
voice "audio/voice/E3/Free/YM/S3/yuuna/171.ogg"
ym "What do you think?"
"Yuuna searches my face, still holding my hand."

menu:
    "The view is amazing!":
        label E3YMS3_TheView:
        pf "I thought the sunset we saw together was amazing, but this is something else."
        "She smiles at me."
        voice "audio/voice/E3/Free/YM/S3/yuuna/172.ogg"
        ym "I stumbled upon this place a few years ago when I was looking for a quiet place to study."
        voice "audio/voice/E3/Free/YM/S3/yuuna/173.ogg"
        ym "I'm sure I'm not the only person who visits this place, but I haven't seen anyone else here before so I like to think it's my secret."
        voice "audio/voice/E3/Free/YM/S3/yuuna/174.ogg"
        ym "You're the first person I've brought here."
        "I smile warmly."
        pf "Thanks, Yuuna."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        "She blushes."
        voice "audio/voice/E3/Free/YM/S3/yuuna/175.ogg"
        ym "No, thank you for helping me with my English and… everything else."
        pf "What are friends for?"
        "She beams."

        scene black with fade

        "I'm not sure how long we stayed there, basking in the tranquility. All too soon, Yuuna says she has to head back to the library. Once we return to the busy park, we say goodbye and I head home." 

    "Pull her into my arms.":
        stop music fadeout 5
        "I feel closer to her than I've ever felt before. She makes me feel calm and grounded and always brings out the best in me."
        "I shared a deep part of my heart today, and not only did Yuuna understand and accept my me, she felt close enough to me to share her own story. I've never made so true a connection with anyone else."
        "I want to hold her in my arms and let her know how I feel."
        "If I do this, there's no turning back. Is this really what I want?" 

        menu:
            "Yes" if E3D4KI_Embraced == 0:
                play music "audio/music/You and I (GAME VERSION).ogg" fadein 5
                $ yuurelatonship = 1
                show yuuna neu b1
                "Worried by my silence, Yuuna looks down."
                voice "audio/voice/E3/Free/YM/S3/yuuna/176.ogg"
                ym "I'm sorry--"
                scene black with fade
                "She tries to turn away, but I don't let her. Instead, I gently tug on her hand and pull her into me."
                "She glances up at me in surprise as she falls into me. My arms wrap around her waist as I steady her. Her hands land on my chest, and I'm sure she can feel how rapidly my heart is beating."
                "Our gaze locks. Yuuna stares at me with her big doe eyes."
                $ persistent.gpix[72][0] = 1
                show cg yuuna embrace:
                    alpha 0
                    xzoom .55
                    yzoom .55
                    yoffset -50
                    xoffset 50
                    
                show cg yuuna embrace:
                    parallel:
                        easein 2.0 alpha 1.0
                    parallel:
                        easein 2.0 xoffset 0


                $renpy.pause(2.0)
                
                pf "It's beautiful."
                "Her cheeks turn pink and a smile spreads across her lips. As she melts into me, her arms snake around my neck, closing the distance between us."
                "I breathe in her perfume of lavender and spring as I feel her press closer against me."
                "My breathing becomes shallow. Yuuna's face is inches away from my own. Her breath tickles my skin…"
                "Then I taste the sweetness of ice cream as our lips meet. Without hesitation, she deepens the kiss."
                "When we finally pull away, she flashes me a breathless smile."

                $renpy.pause(2.0)
                scene black with fade
                $renpy.pause(1.0)

                "We enjoy each other's company, happy for the solitude of nature. I don't know how long we stayed there together before Yuuna reluctantly had to get back to her studying. Once we're back in the busy park, we say our goodbyes and I head home."

            "No":
                "I think I'm getting caught up in the romantic environment, but after some more reflection, I realise I only see her as a friend."
                jump E3YMS3_TheView
    

    
stop music fadeout 5
scene black with fade
stop ambient fadeout 3
$renpy.pause(2.5)
$ E3YMS3_Completed = 1
jump E3D6S2
    

