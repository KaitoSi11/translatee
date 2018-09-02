#
label E3D6S2:

$ nikHairF = renpy.random.choice(['default'])
$ nikHairB = nikHairF
$ nikOut = renpy.random.choice(['sCasual'])

play ambient "audio/ambience/Night Crickets.ogg" fadein 3
scene bg homekaito main night with fade

"I arrive home expecting an empty house. Instead, Nikki is lounging on the couch watching TV."

if E3D6S1_ChoseAlone == 1:
    label E3D6S2_ChoseAlone:
        play ambient "audio/ambience/Night Crickets.ogg" fadein 3
        scene bg homekaito main night with fade
        $renpy.pause(0.5)
    
play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
pf "Hey, Nikki."
"She cranes her head to look at me but doesn't move from her spot."
show nikki smi at cc with dissolve
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_001.ogg"
sf "You're home."
pf "Did Uncle Kaito come back yet?"
show nikki neu
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_002.ogg"
sf "Yeah, but then he left again. He said he had to go meet someone then tried to sneak out when I wasn't paying attention… But I {i}was{/i} paying attention and I saw him go."
show nikki thi
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_003.ogg"
sf "It was kind of weird, like he thought he'd be in trouble if I caught him."
"Hm, Uncle Kaito trying to keep a secret from Nikki… Could he be going to see Aunt Yuki?"
"Well, if he hasn't talked to Nikki about it yet then I won't mention it either."

if (E3KIS3_Completed == 1):
    pf "So, what did you do today?"
    show nikki neu
    voice "audio/voice/E3/D6/S2/nikki/Nikki_5_004.ogg"
    sf "I asked Uncle Kaito if I could work at his cafe and today was my first day."
    pf "How was it?"

else:
    pf "So, how was your day at the cafe?"

"Nikki groans and slinks further into the couch."
show nikki dis
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_005.ogg"
sf "Ohmygod I think my arms are going to fall off! They had me washing dishes, and while I'm so happy that Uncle Kaito's restaurant is booming, if I have to wash another plate again today I will scream."

menu:
    "That great, huh?":
        pf "Sounds like you could use a break."
        show nikki neu
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_006.ogg"
        sf "Yup. That is why I will never move from this spot ever again."
        pf "What if you have to use the bathroom?"
        show nikki cur
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_007.ogg"
        sf "Okay, yes, I'll move for that."
        pf "What if Uncle Kaito comes home and needs your help with something?"
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_008.ogg"
        sf "Well, yeah, I'll move for that too."
        pf "What if--"
        show nikki ann
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_009.ogg"
        sf "Okay fine! I will never move from this spot ever again, except for some special circumstances."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_010.ogg"
        sf "Happy?"
        pf "Yup."

    "So what does that mean for dinner tonight?":
        pf "You mean, after dinner tonight, right?"
        show nikki cur
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_011.ogg"
        sf "What?"
        pf "You'll scream if you wash another plate again {i}after{/i} we have dinner."
        "Nikki pauses, then bursts out laughing."
        show nikki smi
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_012.ogg"
        sf "Hahaha! Dinner! That's funny. You're on your own tonight, mister."
        pf "But what will I eat?"
        "She half-heartedly reaches towards the end table, but drops her arms when they don't reach and points instead."
        show nikki neu
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_013.ogg"
        sf "The take-out menus are over there. Knock yourself out."
        pf "Wow, you couldn't even reach over to grab one? Your laziness knows no bounds."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_014.ogg"
        sf "Says the guy who woke up at noon today."
        pf "It was before noon, thank you very much."

    "You've finally adulted.":
        pf "Congratulations, you now know what to look forward to for the rest of your life."
        show nikki win
        "Nikki groans again."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_015.ogg"
        sf "Stoooop!"
        pf "But at least when you're older you'll get paid."

pf "So, are you going back tomorrow then?"
"She shakes her head."
show nikki smi
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_016.ogg"
sf "Nope!"
pf "You've quit already?"
show nikki neu
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_017.ogg"
sf "No, silly. I'm just not scheduled to work tomorrow."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_018.ogg"
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed02.ogg"
sf "Today was exhausting, but it was still cool to be in the kitchen! And I was only on dish duty because I'm new. I know it won't be long before I'm prepping meals with the rest of the chefs."
pf "What are you going to do instead?"
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_019.ogg"
sf "Watch Ex Zee's concert on TV!"
show nikki smi b1 with dissolve
"She sighs wistfully."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_020.ogg"
sf "I bet he's even dreamier in person…"
pf "I'll let you know if that's true."
show nikki cur with dissolve
"Nikki gives me a skeptical look."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_021.ogg"
sf "Did you just say what I think you said?"
pf "If you thought I said I'm going to be at the concert, then yes."
"She stares at me, then snorts."
show nikki mis
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_022.ogg"
sf "Yeah, right. Those tickets were sold out as soon as they went on sale."
pf "I didn't say I had a ticket. I said I'm going to the concert."
show nikki cur
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_023.ogg"
sf "How would you be able to get in without a ticket?"
pf "When you're a pilot, you make all sorts of connections… like the ones who sponsor your team {i}and{/i} this concert…"
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_024.ogg"
sf "Wait, Dasshu is sponsoring this concert…"
"Nikki's mouth drops open and her eyes grow wide with hope."
show nikki sur
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_025.ogg"
sf "YOU'RE GOING TO THE CONCERT?"
"She hops over the couch and grabs my arm."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_026.ogg"
sf "Please tell me you can bring your adorable and totally deserving little sister!"

menu:
    "It probably won't be that great anyway.":
        pf "No, sorry. I only get to go because Dasshu is holding a promotional event beforehand and Ex Zee is another one of their sponsees."
        show nikki cur
        pf "It'll probably be really boring anyway."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_027.ogg"
        sf "What kind of event is it?"
        pf "A photoshoot."
        show nikki dis
        "She stares flatly at me."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_028.ogg"
        sf "So, not only do you get to go to what will inevitably be the best concert on Earth, but your \"work\" is to just stand around, talk, and get your picture taken?"
        pf "Um, yeah."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_029.ogg"
        sf "And Ex Zee will be there getting his picture taken with you guys?"
        pf "...Maybe."
        show nikki ann
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_030.ogg"
        sf "Awwhhh!"
        "She groans and collapses onto the couch."
        show nikki dis
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_031.ogg"
        sf "Everything you're saying is making even more frustrated that I can't go!"
        pf "I'm sorry!"

    "Nope, he's all mine!":
        $ E3D6S2_FakeTears = 1
        pf "Nope! But maybe, when I meet him, I'll tell him that you're kind of a fan."
        show nikki wor
        "Her voice turns into a high squeal."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_032.ogg"
        sf "You have backstage passes?!"
        pf "Even better. Dasshu is holding a promotional event before the concert which we all have to attend and I'll see him there."
        pf "Maybe we'll even take a picture together."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_033.ogg"
        sf "Are you sure you can't bring a plus one?"
        pf "I don't need my crazy fangirl sister there to embarrass me. I'm trying to gain points, not lose them."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_034.ogg"
        sf "I'll be on my best behaviour!"
        pf "Nope."
        "Her shoulders slump in defeat, and tears gather in her eyes."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_035.ogg"
        sf "O-Oh… Okay…"
        pf "Uh…"
        show nikki win with dissolve
        "She sniffles between words."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_036.ogg"
        sf "Y-You go… have fun… I'll just be here… wishing…I…could...gooooo...."
        "Nikki's last word transforms into a wail of despair."
        pf "Whoa! Hey! Wait! Don't cry!"
        "She hides her face."

    "Sorry, but it's just all business, no pleasure.":
        pf "Sorry, I'm only allowed to attend because Dasshu is holding a promotional event beforehand and I've got to go to that."
        pf "It's a concert, but I've still got to work."
        show nikki sad
        "Nikki looks disappointed, but nods."
        voice "audio/voice/E3/D6/S2/nikki/Nikki_5_037.ogg"
        sf "I see…"

pf "Look, I'm sorry I can't take you, but I'll get you an autograph, okay?"
show nikki cur
"She perks up."

if (E3D6S2_FakeTears == 1):
    "Her eyes are suspiciously dry."
    
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_038.ogg"
sf "You promise?"
pf "I promise."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_039.ogg"
sf "And he'll make it out to \"Nikki\"?"
pf "...Probably?"
show nikki hap
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_040.ogg"
sf "Good enough!"
"She throws her arms around my neck and pulls me into a hug."
show nikki smi
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_041.ogg"
sf "Thank you, big bro! That would be an amazing present!"
show nikki neu
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_042.ogg"
sf "I mean, a more amazing present would be taking me or getting me tickets to the show, but this is a solid second."
pf "Argh, you're crushing me!"
"She lets go, then sinks back into the couch."
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_043.ogg"
sf "Anyway, you should probably order dinner now."
pf "Why?"
voice "audio/voice/E3/D6/S2/nikki/Nikki_5_044.ogg"
sf "I'm hungry, and I'm not cooking."
"My stomach growls in response."
pf "I guess I'm hungry too."
"I go check out the take-out menus."

scene black with fade
stop music fadeout 6
stop ambient fadeout 6
"After a delicious dinner, I head up to my room and do a little more research on Dasshu and their other sponsees."
"It's likely that I'll end up talking to some of them and I don't want to seem ignorant. Once I'm done, I go to bed and drift to sleep."

jump E3D7S1
