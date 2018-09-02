#AFTERNOON  
label E4SSS2:
$ E4SSS2_Completed = 1

$ shoOut = "sCasual"

"I feel my phone vibrate in my pocket and \"Shou\" flashes across the screen."
pf "Hello?"
voice "audio/voice/E4/Shou/Shou Arc/52 Copy.ogg"
ss "Meet me at the garage! ASAP!"
pf "Huh? Why?"
voice "audio/voice/E4/Shou/Shou Arc/53 Copy.ogg"
ss "I have to show you something cool."

if E2SSS3_Completed == 1:
    pf "Another fancy car?"
    voice "audio/voice/E4/Shou/Shou Arc/54 Copy.ogg"
    ss "Even better!"
    
pf "Alright, I'll be over in a bit."
voice "audio/voice/E4/Shou/Shou Arc/55 Copy.ogg"
ss "Make haste!"

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"I hop on my bike and drive over, wondering what exactly his surprise could be."

scene bg homekaito garage day with fade
show shou smi at cc with dissolve
"When I arrive at the garage, Shou waits impatiently for me by the entrance. He ushers me in without a word and then navigates to a secluded part of the garage."
"A big blanket covers an outline of a car."
show shou hap
play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
voice "audio/voice/E4/Shou/Shou Arc/56 Copy.ogg"
ss "Here it is!"
pf "That's a pretty sweet beige blanket, man."
show shou dis
"Shou frowns and shakes his head."
voice "audio/voice/E4/Shou/Shou Arc/57 Copy.ogg"
ss "No, no! It's what's underneath!"
pf "Oh?"
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/58 Copy.ogg"
ss "Yup!"
pf "Well, enough with the suspense already!"
show shou hap
voice "audio/voice/E4/Shou/Shou Arc/59 Copy.ogg"
ss "Roger!"
"With one swooping grab, Shou throws the blanket off."
"Beside him is a vintage model 2017 Furd Moosetang in fresh blue paint and white racing stripes."
"I've seen this in old school car photos but never one up close. This is too cool!"
pf "Where'd you get it?"
show shou mis
voice "audio/voice/E4/Shou/Shou Arc/60 Copy.ogg"
ss "Get it? I built it."
pf "Built it?!"
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/61 Copy.ogg"
ss "Yeah. I found the frame from an old mechanic's shop and then thought I'd try to restore it. It was hard to find all the different pieces, and I've been working on it for a few years, but it's finally done!"
"He grins proudly."
voice "audio/voice/E4/Shou/Shou Arc/62 Copy.ogg"
ss "I thought you'd appreciate an American manufactured car."
"He's right about that!"
show shou thi
voice "audio/voice/E4/Shou/Shou Arc/63 Copy.ogg"
ss "I still can't believe these things needed refueling every week. Talk about a non-sustainable source of energy!"
pf "Yeah, it's pretty insane when you about think how hard the oil companies were trying to roadblock the electric car."
show shou hap
voice "audio/voice/E4/Shou/Shou Arc/64 Copy.ogg"
ss "I have to give big props to Tezla and their revolutionary Model Trio!"
"We both nod. I still can't imagine what people from 2017 would think if they knew we'd have self-driving cars with renewable energy that only needed a monthly charge!"
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/65 Copy.ogg"
ss "But the best part is still coming up."
pf "What is it?"
voice "audio/voice/E4/Shou/Shou Arc/66 Copy.ogg"
ss "The roar of an engine of course! I've seen MeTube videos of it but never had the pleasure of hearing one."
"My bike is the closest I've come to hearing an authentic engine, and even that is an inadequate comparison. I'm pretty excited too!"
"Shou pulls out the keys to the car and opens the driver side door. He slips the key in the ignition then looks at me."
voice "audio/voice/E4/Shou/Shou Arc/65 Copy.ogg"
voice "audio/voice/E4/Shou/Shou Arc/67 Copy.ogg"
ss "Ready?"
pf "Do it!"
"He turns the key...!"
show shou hap
"A deep rumbling escapes the cylinders as the engine fires up!"

menu:
    "That's really noisy!":
        pf "Geez, it sounds like a GEAR just shot an explosive round."
        voice "audio/voice/E4/Shou/Shou Arc/68 Copy.ogg"
        ss "I know, right! Amazing."
        pf "...That's one way to describe it."

    "WOAH.":
        "I point to the car."
        pf "This, I like."
        "Shou laughs with pride."
        voice "audio/voice/E4/Shou/Shou Arc/69 Copy.ogg"
        ss "Me too!"

    "Not bad.":
        voice "audio/voice/E4/Shou/Shou Arc/70 Copy.ogg"
        ss "Pretty sweet, huh?"
        "He beams."
        pf "I'd be lying if I said it wasn't."

show shou cur
"We hear a really strange noise followed by painful screech of grinding metal."
pf "What was that--"
show shou sur
"The engine makes dying noises, then the car goes silent. Black smoke seeps out from under the hood."
show shou sad
stop music fadeout 25
voice "audio/voice/E4/Shou/Shou Arc/71 Copy.ogg"
ss "No!"
"Shou pops the hood and fiddles around under there, muttering to himself."
show shou win
voice "audio/voice/E4/Shou/Shou Arc/72 Copy.ogg"
ss "Oh man… I knew it! Curse you DatBoi_69!"
pf "What's going on?"
show shou thi
voice "audio/voice/E4/Shou/Shou Arc/73 Copy.ogg"
ss "He was the guy on Kajiji who sold me this defective part."
"He points at something. With my minimal understand of an engine's framework, all I can do is nod in sympathy."
voice "audio/voice/E4/Shou/Shou Arc/74 Copy.ogg"
ss "I knew I shouldn't have trusted him."
pf "Sorry man."
"Shou shakes his head."
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/75 Copy.ogg"
ss "Nah, it's okay. This is actually good."
pf "Huh?"
voice "audio/voice/E4/Shou/Shou Arc/76 Copy.ogg"
ss "Well, I was starting to feel a little sad when I was finishing up the car. It's been so much fun building it that I wasn't quite ready to let it go and start something new... but now it doesn't have to end!"
"I guess spending that much time on one project can get you pretty attached to it."
pf "I'm sure you'll get it working better than before."
show shou hap
"Shou grins."
voice "audio/voice/E4/Shou/Shou Arc/77 Copy.ogg"
ss "That's the plan!"
"He scratches the back of his head."
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/78 Copy.ogg"
ss "Sorry, I guess it wasn't much of a show. I probably should have tested it out first, but I was too excited."
pf "No way! The ignition was worth it."
voice "audio/voice/E4/Shou/Shou Arc/79 Copy.ogg"
ss "You got that right!"
"We both grin."
pf "It looks like you've got some work to do so I'm going to head out."
pf "Let me know when it's ready... for a test drive, that is."
show shou hap
voice "audio/voice/E4/Shou/Shou Arc/80 Copy.ogg"
ss "Of course!"
"I'm excited to see the real finished project. I've never had a chance to drive a muscle car! Or a manual."
scene black with fade
"After we say our goodbyes, Shou gets back to work and I leave."



stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4SSS2_Completed = 1