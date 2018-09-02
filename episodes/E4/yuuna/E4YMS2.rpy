#EVENING
label E4YMS2:

$ yuuHairF = "default"
$ yuuHairB = yuuHairF
$ yuuOut = "Dog"


"Yuuna pops into my mind and I decide to give her call. I wonder how she's spending her reading week."
"She answers the phone almost immediately."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/42.ogg"
ym "...Um, hello?"
pf "Hey, Yuuna…"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/43.ogg"
ym "Oh! I was in the middle of calling you when you called me."
if yuurelatonship == 1:
    pf "Does that mean you were thinking about me?"
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/44.ogg"
    ym "Yes!"
    pf "Oh… uh, good."
    "I'm a little surprised by how frank she is."
    pf "Well, obviously I was thinking about you too."
else:
    pf "What a crazy coincidence!"
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/45.ogg"
    ym "I know! I wanted to ask your advice about something."
    pf "About what?"
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/46.ogg"
    ym "Well… it's more something you need to see…"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/47.ogg"
ym "Would you like to come over?"
pf "Sure, I'll be right there."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/48.ogg"
ym "Great! I'll see you soon."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"When we hang up, I head to my bike and drive to Yuuna's house."

scene bg isokaze neighborhood dusk with fade

"After parking, I knock soundly on her door. There's a shuffling on the other side and it takes her a while before she opens the door a crack."
play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
show yuuna smi at cc with dissolve
$renpy.pause(.5)
show yuuna sur with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/49.ogg"
ym "No!"
hide yuuna with dissolve
"She slams the door shut again."
"Uh… That was strange…"
"There are more noises on the other side of the door before Yuuna flings it open."
show yuuna smi at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/50.ogg"
ym "Hi."
pf "Hey."
"{i}Woof!{/i}"
$ persistent.gpix[73][0] = 1
$ persistent.gpix[74][0] = 1

scene cg yuuna dog 1 with fade:
    xzoom .5
    yzoom .5
"I stare at the wriggling ball of fur trying to jump free from her arms."

menu:
    "PUPPY!":
        "I open my arms and Yuuna let's the pup hop into them. Its tail slaps my body with each wag as the puppy tries to plant kisses all over my face."
        pf "You didn't tell me you got a dog!"

    "Ugh, slobber factory.":
        $ E4YMS2_Slobber = 1
        "The puppy sticks out its tongue and tries to lick my face. I instinctively take a step back."
        pf "That's a dog in my face."

    "You...have a...dog?":
        "Yuuna tries to calm the puppy who alternates between licking her face and trying to lick mine."
        pf "Did you always have a dog?"
        "She laughs."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/51.ogg"
        ym "No."
        

voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/52.ogg"
ym "I'm just borrowing him for now."
pf "\"borrowing\"?"
scene black with fade
scene bg campus dorm dusk with fade
"Yuuna moves aside so I can enter and closes the door behind me. Then she puts the puppy down. It scampers to my leg and paws at my feet as I carefully make my way to the couch."
"Yuuna sits down beside me."
show yuuna thi at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/53.ogg"
ym "Okay, not really borrowing. I've been volunteering at the local animal shelter since I moved to Isokaze, and when I found out they needed foster homes for some of their pets I volunteered to take Mochi home with me."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/54.ogg"
ym "As you can tell, he loves people. And he's already been house broken so they don't think it'll be long before he gets adopted."
"Mochi tries fruitlessly to hop onto the couch and misses each time. After attempting a few more times, he sits back on his haunches and whines."
"Yuuna giggles, then scoops him back up in her arms. He settles into her lap."
pf "How long have you had him?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/55.ogg"
ym "About a week."
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/56.ogg"
ym "Actually, I wanted to ask you about that…"
pf "Hm?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/57.ogg"
ym "I'll have to give him back next week, but I don't really want to."
pf "You want to adopt him."
"She nods and fondly pets Mochi's head."
show yuuna neu
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/58.ogg"
ym "The house doesn't feel so big and empty when he's around."
"I glance around the living room. The space is conservatively decorated, but includes a lot of photographs of the family. Antique vases and cabinets tastefully fill the space. I wonder if these are family heirlooms or items passed down from generation to generation."
"Looking at all the smiling faces of Yuuna, Yuudai, and their parents, I can understand why Yuuna feels alone in such a big house. She's constantly reminded of the past."
pf "What did your parents say?"
"Yuuna bites her lip."
show yuuna wor
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/59.ogg"
ym "...I haven't told them yet."
pf "Not even about fostering the puppy?"
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/60.ogg"
ym "No…"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/61.ogg"
ym "I'm not sure what they'll say. We used to have dogs back when we still lived in the countryside so it's not like I don't know how to take care of them."
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/62.ogg"
ym "Maybe they won't even notice."
"Mochi's plush bed is in the corner where the kitchen and living room connect. Compared to the rest of the decor, his colourful and modern toys stick out like a sore thumb."
pf "I think they might."
"She frowns and furrows her brow."
scene cg yuuna dog 2 with fade:
    xzoom .5
    yzoom .5
"Mochi seems to sense her anxiety and places his front paws on her chest to lick her face again."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/63.ogg"
ym "Mochi!"
"She turns her face away but laughs."

menu:
    "Just ask your parents.":
        pf "You should just talk to your parents. I'm sure they'd understand if you told them why."
        "She wrinkles her brow again, then nods."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/64.ogg"
        ym "I suppose it can't be helped. They'd find out sooner or later."

    "Aww, he loves you. Keep him!":
        pf "Look how happy he is! I think he likes you."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/65.ogg"
        ym "I think so too!"
        pf "You should keep him. Your parents will understand. {w}You two are meant for each other."
        "She giggles."
        if yuurelatonship == 1:
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/66.ogg"
            ym "You might have some competition for my affection now."
            pf "Nevermind, he needs to go."
            "She laughs again."

    "Have you thought about the responsibilities?":
        pf "Having a dog is a lot of work. Since it's reading week, we've had more flexibility but what will you do when we're at school all day?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/67.ogg"
        ym "It's not like I live very far. I can always come home to let him out between classes. Plus, he has room to roam around the backyard."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/68.ogg"
        ym "I already have an estimate of how much money I'd need to cover his food and care and it's within my budget."
        "I shake my head, then grin."
        pf "Of course you would have thought about these things, miss manager."
        "She matches my smile."

pf "It sounds like you've already made up your mind."
scene black with fade
scene bg campus dorm dusk with fade
show yuuna smi at cc with dissolve
stop music fadeout 5
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/69.ogg"
ym "Maybe…"
"She pauses."
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/70.ogg"
ym "It's not that I'm worried my parents will say no. I don't think they'd be opposed to the idea… I just…"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/71.ogg"
ym "I don't want them to think they're bad parents."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/72.ogg"
ym "I understand why they don't stay here for too long, and I don't want them to think I'm lonely."
pf "Are you lonely?"
show yuuna sad
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/73.ogg"
ym "It can be a little quiet…"
if yuurelatonship == 1:
    pf "Well, whenever it starts feeling too quiet, you can always give me a call. I'll come and keep you company."
    show yuuna smi b2 with dissolve
    "She blushes."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/74.ogg"
    ym "Thanks."
    "We pause."
    pf "Do you ever miss the countryside?"
    "She blinks in surprise."
    show yuuna neu b1 with dissolve
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/75.ogg"
    ym "A little."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/76.ogg"
    ym "I love Isokaze, but sometimes I wish we were a little closer to nature."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/77.ogg"
    ym "What about you?"

    menu:
        "Me too!":
            pf "I know what you mean. Whenever I need to clear my head, I like to sit in the green of the trees and think."
            "Yuuna smiles."
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/78.ogg"
            ym "Me too. Something about being away from the noise of everyday life is really soothing."

        "I like indoor nature…":
            $ E4YMS2_Indoors = 1
            pf "Sure, I was a pro at Park Simulator."
            show yuuna neu
            "Yuuna frowns."
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/79.ogg"
            ym "\"Park Simulator\"?"
            pf "Yeah! It's this really fun game where you're a guy who goes to the park. You're trying to just relax but you have to dodge all the old people and children who want to disturb your peace and quiet."
            show yuuna thi
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/80.ogg"
            ym "I'm not sure we're talking about the same thing…"

    pf "Why don't we do something to get away this weekend?"
    show yuuna cur
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/81.ogg"
    ym "Like what?"
    pf "We could go camping."
    show yuuna thi
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/82.ogg"
    ym "But what about exams?"
    pf "We've already been studying hard for them all week. A break would be nice… especially since we don't want to get burned out."
    show yuuna smi
    "Yuuna looks thoughtful as a smile gradually graces her lips."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/83.ogg"
    ym "It doesn't sound so bad. Plus I haven't gone in a while."
    pf "Then it's about time, isn't it?"
    if E4YMS2_Indoors == 1:
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/84.ogg"
        ym "But you don't like the outdoors…"
        pf "I've gone camping a few times as a kid and it was always fun."
    show yuuna hap 
    
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/85.ogg"
    ym "Okay! Let's do it."

if yuurelatonship == 0:
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    
"Mochi yips and hops off of Yuuna's lap. He races towards his bed of toys, sliding on the hardwood floors."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/86.ogg"
ym "I think he wants to play."
if E4YMS2_Slobber == 1:
    "He is kind of cute when he's uncoordinated…"

menu:
    "Play fetch!":
        show yuuna cur
        "Mochi picks up a squeaky ball and I gently pry it from his mouth before tossing it across the room, careful to aim away from anything valuable."
        "Mochi speeds after the ball and diligently brings it back. As I pry it from his mouth again, his tail wags back and forth."
        "I fake a throw and Mochi goes barreling down the room, then freezes, his ears up as he sniffs around for the ball. When he sees it's still in my hand he comes barreling back."
        show yuuna hap
        "Yuuna bursts out laughing."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/87.ogg"
        ym "Mochi, you're so silly!"

    "Play tug-of-war!":
        show yuuna cur
        "Mochi grabs a thick braided rope in his mouth and I grab the other end then lightly tug. Mochi pulls back, his tail still wagging. I increase the pressure and Mochi pushes his weight back onto his hind legs so his butt is in the air. He growls affectionately as he shakes his head back and forth."
        "I gently let go and my end of the rope drops harmlessly to the ground. Mochi pauses, and cocks his head to the side as if asking what I'm doing."
        pf "You were too strong!"
        show yuuna hap
        "Yuuna giggles."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/88.ogg"
        ym "Mochi, you won!"

    "Forget toys! Give bellyrubs!":
        pf "Are you sure he wants to play? Or does he want… bellyrubs!"
        show yuuna cur
        "I catch up to the little puppy and scratch behind his ears. His tongue lolls out and he flops to the side, exposing his belly. I rub his belly and and he leans back in enjoyment. When I pause, he sits back up and nudges my hand."
        "Yuuna giggles."
        show yuuna mis
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/89.ogg"
        ym "What a little attention seeker."

    "I'll pass…":
        show yuuna smi
        "I remain on the couch while Yuuna showers Mochi with attention."

show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/90.ogg"
ym "Oops, now that he's all wound up I should probably take him for a walk so he doesn't accidentally wet himself."
pf "Yeah, that wouldn't be good."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/91.ogg"
ym "Do you want to join?"
"I glance out the window at the darkened sky."
pf "I should probably get back before it gets too late."
show yuuna smi
"Yuuna nods."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/92.ogg"
ym "Thanks for coming over."
pf "No problem."
pf "Bye Mochi!"
show yuuna hap
"Yuuna picks up one of Mochi's paws and waves it around."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/93.ogg"
ym "Bye bye!"
"We both laugh as Mochi looks down at his paw in confusion."

scene black with fade

"Yuuna grabs the leash and secures it around Mochi's neck, then we leave the house together. She heads towards the park while I head back to my bike and drive home."





stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4YMS2_Completed = 1