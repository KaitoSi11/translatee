#
label E3SSS3:
$ shoOut = "sCasual"

"I'm a little worried about Shou meeting with his brother today. Their last encounter was less than pleasant, and that was with me there. I'm not sure how it'll be if it's just the two of them together."
"I don't want to intrude, but I think it would be good for them to have a mediator. And since I was invited, it wouldn't be out of line for me to join them."
"I'll just text Shou and ask what he's up to today."
"..."
"Shou responds immediately with an address for a restaurant. {w}I guess that solves whether or not I should show up!"
"I reread the text. Wait, this can't be right… it's impossible to get a reservation at this restaurant unless you reserve months in advance. Akio has only been in town for a few days. How did he manage to swing a reservation? Has he been planning this for a while?"
"Hmm… I recall Shou's warning about his brother… maybe I shouldn't have dismissed him so quickly."
"In any case, I don't want to be late. I clean myself up and try to look as presentable as I can, then hop on my bike."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)
play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(5.5)

"The parking lot is filled with expensive cars, and my bike feels a little out of place. Although I didn't dress casually, I still feel underdressed compared with the suits and cocktail dresses other patrons are wearing. I'm out of my element."

scene bg store ramen day with fade

"As soon as I make my way inside, I am greeted by a well dressed man."
voice "audio/voice/E3/Free/SS/S3/wait/1.ogg"
wait "Can I help you?"
"The maitre d'hotel looks down his nose at me, as if my very presence offends him."
pf "I am meeting my friends, Akio and Shou Shinjirou."
"He sighs heavily and skeptically scrolls through the reservations. When he finds the reservation, he does little to hide his surprise."
voice "audio/voice/E3/Free/SS/S3/wait/2.ogg"
wait "Follow me."
"He leads me to where Akio is sitting."

play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
show akio smi at cc with dissolve

"Akio stands as I approach and offers me a handshake. I blink in surprise but take his hand. His grasp is firm and businesslike."
"Of course, he works in London so he's familiar with our customs." 
show akio hap
voice "audio/voice/E3/Free/SS/S3/aks/11.ogg"
aks "I'm glad you could make it."
"I nod."
show akio smi
pf "Thank you for the invitation. {w}Is Shou here yet?"
voice "audio/voice/E3/Free/SS/S3/aks/12.ogg"
aks "He said he's running late."
pf "Ah, okay."
"Well, this is awkward..."

menu:
    "What's up with you and Shou?":
        "It might be rude of me to bring this up right away, but it's not like I know anything about Shou and Akio."
        pf "Akio."
        "He offers me a polite smile."
        voice "audio/voice/E3/Free/SS/S3/aks/13.ogg"
        aks "Yes?"
        pf "Shou acts a bit strange when you're around..."
        show akio dis
        "He sighs and nods."
        voice "audio/voice/E3/Free/SS/S3/aks/14.ogg"
        aks "A bit."
        show akio neu
        voice "audio/voice/E3/Free/SS/S3/aks/15.ogg"
        aks "We don't see each other much... only every few months or so."
        "I can't imagine a life where I'd only see Nikki a few months at a time. Even when I was at CINY we saw each other frequently. And if we couldn't physically hang out with each other, we were always messaging back and forth."
        voice "audio/voice/E3/Free/SS/S3/aks/16.ogg"
        aks "The age difference has always been a factor between us, and after he moved to ACE it's been harder to keep in touch with him."
        pf "I see."

    "How did your lectures go?":
        pf "How was your presentation at ACE?"
        show akio hap
        "Akio grins broadly."
        voice "audio/voice/E3/Free/SS/S3/aks/17.ogg"
        aks "It went well! The academic level of ACE students is quite impressive. I was especially pleased by the level of participation and engagement from the audience. If you're interested, perhaps you could attend the next one."
        pf "Sure, just let me know when."
        show akio smi
        voice "audio/voice/E3/Free/SS/S3/aks/18.ogg"
        aks "Of course."
        "He seems pleasant enough…"

    "Stay quiet.":
        "I'm not good at small talk, so I'm not even going to try. If he wants to talk to me he can."

stop music fadeout 5
hide akio with dissolve

show shou neu at l2
show akio neu at r2:
    xzoom -1
with dissolve
voice "audio/voice/E3/Free/SS/S3/shou/87.ogg"
ss "Hey, guys."
"Shou sits down in an empty seat. He sits straighter than usual, taking care not to slouch. {w}This is new."
pf "Hey."
voice "audio/voice/E3/Free/SS/S3/aks/19.ogg"
aks "Hi, Shou."
show shou hap
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
voice "audio/voice/E3/Free/SS/S3/shou/88.ogg"
ss "You guys haven't ordered yet? I'm starving!"
show akio smi
"Huh… He seems to be in better spirits..."

if (MCStory == 3):
    "I can't help but feel like he's just putting up a front."

show shou smi
"Shou unabashedly grabs a menu. I follow suit, but as I continue to flip through the options, my heart sinks. I don't see anything under 100 credits. Even the appetizers cost an arm and a leg! This is insane!"
"Considering Akio made the reservation, I doubt he'd have any qualms about the price. I glance at Shou to see if he's also freaking out, but he seems unphased."

menu:
    "Pick whatever is inexpensive.":
        $ E3SSS3_FoodChoice = 1
        "Well, just because they can afford to eat here doesn't mean I can. I look for the cheapest option."

    "Just order normally.":
        $ E3SSS3_FoodChoice = 2
        "Well, it's not every day I have a chance to eat in an upscale restaurant. Let's make the most of it!"

    "Order nothing and pray to jebus for complimentary bread buns.":
        $ E3SSS3_FoodChoice = 3
        "I'd rather not spend my entire weekly budget on one meal."

"Just as I finalise my choice, a waiter appears."
voice "audio/voice/E3/Free/SS/S3/wait/3.ogg"
wait "Are you ready to order?"
"Shou and Akio nod."
voice "audio/voice/E3/Free/SS/S3/aks/20.ogg"
aks "I'll do the butternut squash risotto with scallops and lemon juice."
voice "audio/voice/E3/Free/SS/S3/shou/89.ogg"
ss "I'd like to order a medium rare rib-eye steak with balsamic reduction and crisp rosemary potatoes."

if (E3SSS3_FoodChoice==1):
    pf "I'll have... a salad."
    show shou cur
    show akio cur
    voice "audio/voice/E3/Free/SS/S3/wait/4.ogg"
    wait "What type of a salad?"
    pf "Uh, one with lettuce?"
    "All three of them look at me with confusion."
    pf "...And cheese?"
    voice "audio/voice/E3/Free/SS/S3/wait/5.ogg"
    wait "Would you like a Caesar salad?"
    "I think I've embarrassed myself enough."
    show akio smi
    show shou smi
    pf "Sure, let's go with that."


elif (E3SSS3_FoodChoice==2):
    "What Shou ordered sounds delicious! My mouth is already watering."
    pf "Make that two for the rib-eye."
    show shou hap
    show note:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    "Shou grins."
    voice "audio/voice/E3/Free/SS/S3/shou/90.ogg"
    ss "Good choice!"


elif (E3SSS3_FoodChoice==3):
    pf "I'm fine, thank you."
    show shou cur
    show question:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/SS/S3/shou/91.ogg"
    ss "Are you sure?"
    pf "Yeah, I ate before coming."
    "I can feel my stomach grumbling in protest."
    voice "audio/voice/E3/Free/SS/S3/shou/92.ogg"
    ss "If you say so!"
    
voice "audio/voice/E3/Free/SS/S3/wait/6.ogg"
wait "Thank you. I'll go get these prepared for you gentlemen."
"After collecting our menus, he disappears."
"Akio faces Shou."

show akio smi
voice "audio/voice/E3/Free/SS/S3/aks/21.ogg"
aks "So, how are you?"
show shou smi
voice "audio/voice/E3/Free/SS/S3/shou/93.ogg"
ss "... Good, you?"
voice "audio/voice/E3/Free/SS/S3/aks/22.ogg"
aks "Same."
show shou neu
show dots:
    xoffset 365
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/SS/S3/shou/94.ogg"
ss "..."
show akio neu
show dots:
    xoffset 1040
    yoffset 5
    xzoom .75
    yzoom .75
aks "..."
"This is going just as well as I expected."

menu:
    "Steer the conversation towards the recent match.":
        pf "Shou, what rating do you think our team is at now?"
        show shou cur
        voice "audio/voice/E3/Free/SS/S3/shou/95.ogg"
        ss "You mean after our match against Mei's team?"
        pf "Yeah."
        show akio cur
        voice "audio/voice/E3/Free/SS/S3/aks/23.ogg"
        aks "Oh, you won your last match?"
        show shou mis
        voice "audio/voice/E3/Free/SS/S3/shou/96.ogg"
        ss "Yeah. Actually, so far we're undefeated."
        show akio smi
        "Akio looks genuinely impressed. Shou grins."

    "Comment about the weather.":
        pf "So, how about that weather we've been having?"
        show shou ske
        "Shou looks confused."
        show question:
            xoffset 365
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/SS/S3/shou/97.ogg"
        ss "What about it?"
        pf "Um… it's been… sunny…"
        show shou neu
        voice "audio/voice/E3/Free/SS/S3/shou/98.ogg"
        ss "Yup."
        show akio smi
        voice "audio/voice/E3/Free/SS/S3/aks/24.ogg"
        aks "That's much better than London. It always rains there."
        "We fall silent again. What did I expect? This wasn't the most stimulating choice."

if (E2MAS4_Completed == 0):
    show akio smi
    voice "audio/voice/E3/Free/SS/S3/aks/25.ogg"
    aks "How are things with the Akemi girl? Are you two a couple yet?"
    show shou sur b1 with dissolve
    "Shou blushes."
    show shoBlush:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/SS/S3/shou/99.ogg"
    ss "W-What?! Why would you say that?!"
    show akio cur
    voice "audio/voice/E3/Free/SS/S3/aks/26.ogg"
    aks "Really? You're still in denial?"
    pf "That's what I've been telling this guy."
    show shou ner b1
    voice "audio/voice/E3/Free/SS/S3/shou/100.ogg"
    ss "Neither one of you knows what you're talking about!"
    "Akio looks at me."
    voice "audio/voice/E3/Free/SS/S3/aks/27.ogg"
    aks "Is he always this hopeless?"
    pf "Yup."
    show akio smi
    "Akio nods in understanding."
    show shou neu with dissolve
    voice "audio/voice/E3/Free/SS/S3/shou/101.ogg"
    ss "I can hear you, you know..."
    "We laugh."

stop music fadeout 8
show shou smi
voice "audio/voice/E3/Free/SS/S3/shou/102.ogg"
ss "Anyway, how's mom and dad?"
voice "audio/voice/E3/Free/SS/S3/aks/28.ogg"
aks "They're good. They'd be better if you called once in awhile."
"Shou looks a little sheepish."
show shou ner
voice "audio/voice/E3/Free/SS/S3/shou/103.ogg"
ss "Sorry, I've been busy... but I'll call them soon."
### VOICE - missing line
aks "I'm sure they'll be glad to hear from you."
show shou neu
voice "audio/voice/E3/Free/SS/S3/shou/104.ogg"
ss "Are they still… the same?"
show akio neu
"Akio gives Shou a long look. I can't read his expression, but Shou looks away."
voice "audio/voice/E3/Free/SS/S3/aks/29.ogg"
aks "They're still running the business. It's going well."
play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 5
"Shou's smile falters."
voice "audio/voice/E3/Free/SS/S3/aks/30.ogg"
aks "They've moved forward with the acquisitions that were in the pipeline and are looking for new portfolios to invest in."
voice "audio/voice/E3/Free/SS/S3/aks/31.ogg"
aks "We all met with the board of trustees last week to discuss the transition from--"
show shou dis
voice "audio/voice/E3/Free/SS/S3/shou/105.ogg"
ss "Stop."
show akio cur
"Akio blinks."
voice "audio/voice/E3/Free/SS/S3/aks/32.ogg"
aks "Shou?"
voice "audio/voice/E3/Free/SS/S3/shou/106.ogg"
ss "I knew you didn't come here just to hang out."
show akio neu
voice "audio/voice/E3/Free/SS/S3/aks/33.ogg"
aks "What do you mean?"
voice "audio/voice/E3/Free/SS/S3/shou/107.ogg"
ss "Don't play dumb with me. I know what you're doing."
show akio dis
"Akio's expression hardens."
voice "audio/voice/E3/Free/SS/S3/aks/34.ogg"
aks "We're going to have this conversation eventually. You can't keep putting it off."
"Shou stands up."
show shou ann
voice "audio/voice/E3/Free/SS/S3/shou/108.ogg"
ss "Excuse me, I just remembered I have to {i}conveniently{/i} leave right now."
show vein:
    xoffset 365
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/SS/S3/shou/109.ogg"
ss "Just like you {i}conveniently{/i} showed up at ACE."
"He looks accusingly at Akio."
show akio ske
voice "audio/voice/E3/Free/SS/S3/aks/35.ogg"
aks "Shou--"
hide shou with dissolve
show akio neu with dissolve
"Shou leaves before Akio can say anything more. {w}Akio leans back in his chair and sighs. He seems like he's drained of energy. {w}Actually, now that I've taken a better look at him, I notice the bags under his eyes. This trip must be taking a toll on him."
voice "audio/voice/E3/Free/SS/S3/aks/36.ogg"
aks "I can't say I'm surprised…"
"He looks at me and I catch the disappointment and worry in his face."
voice "audio/voice/E3/Free/SS/S3/aks/37.ogg"
aks "Can you talk to him? I know he doesn't want to talk to me right now, but he needs to see reason. It won't be long before he graduates, and he needs to think about his future. As much as he wishes he weren't, he {i}is{/i} a part of this family and his decision affects all of us."
"I don't know what's going on with Shou and his family's business, but I do know that right now my friend is really upset."
pf "I'll go check on him."
stop music fadeout 5
voice "audio/voice/E3/Free/SS/S3/aks/38.ogg"
aks "Thank you. I'll take care of things here."
"I nod and look for Shou."

scene black with fade

"I find him in the parking lot, searching for his car."

play ambient "audio/ambience/Parking Lot.ogg" fadein 5
scene bg campus impound day with fade

pf "Shou!"
"He turns around."

play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
show shou ang at cc with dissolve
voice "audio/voice/E3/Free/SS/S3/shou/110.ogg"
ss "I knew he was up to something. I just knew it."
pf "Slow down, man."
show shou ann
voice "audio/voice/E3/Free/SS/S3/shou/111.ogg"
ss "This isn't the first time he's done this."
voice "audio/voice/E3/Free/SS/S3/shou/112.ogg"
ss "He shows up {i}unexpectedly{/i} and always steers the conversation towards the family business."
voice "audio/voice/E3/Free/SS/S3/shou/113.ogg"
ss "Maybe I'm a fool for thinking this, but just it'd be nice if just once he could be my brother."

menu:
    "Can I help in anyway?":
        pf "Anything I can do to help?"
        show shou dis
        voice "audio/voice/E3/Free/SS/S3/shou/114.ogg"
        ss "Yeah, make sure he stops showing up out of the blue."
        "I give him a pointed look and he sighs."

    "Ask what's going on.":
        pf "I know I shouldn't pry, but what's this about?"

    "Just listen for now.":
        "I stay silent and let Shou vent."

show shou dis
voice "audio/voice/E3/Free/SS/S3/shou/115.ogg"
ss "We have a family business overseas, Shinjirou Inc."
"It doesn't sound familiar..."
voice "audio/voice/E3/Free/SS/S3/shou/116.ogg"
ss "It's not well known to the public, but our company supplies tools and equipment for industrial grade GEARs... Mining, construction, that kind of stuff."
pf "He mentioned a board of trustees...?"
show shou neu
voice "audio/voice/E3/Free/SS/S3/shou/117.ogg"
ss "Yeah, Shinjirou Inc. is basically their empire."
pf "...I mean, how big are we talking? Are we talking like millions?"
voice "audio/voice/E3/Free/SS/S3/shou/118.ogg"
ss "Billions."
pf "What?"
"My eyes widen."
pf "You're a billionaire?"
voice "audio/voice/E3/Free/SS/S3/shou/119.ogg"
ss "No, my parents are."

menu:
    "I see where this is going.":
        pf "And you don't want to be a part of it?"

    "Same difference.":
        pf "Isn't that pretty much the same thing?"
        voice "audio/voice/E3/Free/SS/S3/shou/120.ogg"
        ss "It's not. It's their business and their wealth."
        pf "You don't want to be involved?"

show shou neu
voice "audio/voice/E3/Free/SS/S3/shou/121.ogg"
ss "It feels like I don't really have a choice."
voice "audio/voice/E3/Free/SS/S3/shou/122.ogg"
ss "I'm trying to avoid it for as long as I can. It's why I didn't want them to sponsor us when we were looking."
voice "audio/voice/E3/Free/SS/S3/shou/123.ogg"
ss "I don't know why, but lately my parents seem adamant that I inherit the business."
voice "audio/voice/E3/Free/SS/S3/shou/124.ogg"
ss "I thought that studying piloting, one of the few careers my parents approve of, would get them off my back. For a while it did, so I don't know what changed."
show shou dis
show storm:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
"His eyes darken."
voice "audio/voice/E3/Free/SS/S3/shou/125.ogg"
ss "Yes, I do. They were never going to let me be free. This was just their way of placating me so that when they reintroduced their \"grand plan\" I'd be more receptive."
"Shou kicks a rock on the ground."
show shou ann
voice "audio/voice/E3/Free/SS/S3/shou/126.ogg"
ss "What annoys me the most is that Akio has an MBA {i}and{/i} he's founded his own company which is still relevant to the family business."
voice "audio/voice/E3/Free/SS/S3/shou/127.ogg"
ss "Why aren't my parents forcing {i}him{/i} to take over?"
voice "audio/voice/E3/Free/SS/S3/shou/128.ogg"
ss "Is it because he found success on his own and I'm the..."
"His voice trails off."
show shou sad
voice "audio/voice/E3/Free/SS/S3/shou/129.ogg"
ss "...I'm the useless one?"
pf "You're in one of the top piloting programs in the country and you're an invaluable member of our team. How can you say you're useless?"
voice "audio/voice/E3/Free/SS/S3/shou/130.ogg"
ss "Compared to my brother--"
pf "He's already graduated and had a lot of time to build his own success."
show shou thi
voice "audio/voice/E3/Free/SS/S3/shou/131.ogg"
ss "I suppose that's true…"
"He falls silent."
pf "Why don't you just tell your parents no?"
show shou neu
voice "audio/voice/E3/Free/SS/S3/shou/132.ogg"
ss "And destroy my parents legacy or force my brother to retire his?"
"I can understand his dilemma… this isn't the most ideal situation."
voice "audio/voice/E3/Free/SS/S3/shou/133.ogg"
ss "Anyway, I'm sorry you got involved."
voice "audio/voice/E3/Free/SS/S3/shou/134.ogg"
ss "I was hoping with you around he wouldn't bring up this business and would just act like a normal brother. Obviously I was was wrong."
pf "Don't worry about it."
voice "audio/voice/E3/Free/SS/S3/shou/135.ogg"
ss "I need to clear my head."
"I glance back towards the restaurant. I'm sure Akio will understand…"
pf "Alright. I'll tell Akio for you. Just let me know if you need anything."
voice "audio/voice/E3/Free/SS/S3/shou/136.ogg"
ss "Thanks."

hide shou with dissolve

stop music fadeout 10
"Shou hops into his car and drives off."
"Akio waits for me at the entrance of the restaurant. When he sees me, he nods."

show akio neu at cc with dissolve
voice "audio/voice/E3/Free/SS/S3/aks/39.ogg"
aks "I assume that was my brother driving off in a hurry?"
pf "Yeah…"
show akio sad
"He sighs, and for a moment I catch a glimpse of sadness in his eyes."
show akio neu
voice "audio/voice/E3/Free/SS/S3/aks/40.ogg"
aks "I see."
"Maybe Shou is wrong about his brother. Maybe he does care..."
"Akio quickly regains his composure."
voice "audio/voice/E3/Free/SS/S3/aks/41.ogg"
aks "It was a pleasure to meet you, although I wish it'd been under happier circumstances. I apologize for getting you involved."
pf "It's alright."
voice "audio/voice/E3/Free/SS/S3/aks/42.ogg"
aks "I suppose it's best for Shou to have some time to cool off."
pf "Are you going to be in town much longer?"
"He shakes his head."
voice "audio/voice/E3/Free/SS/S3/aks/43.ogg"
aks "My flight leaves tonight."
voice "audio/voice/E3/Free/SS/S3/aks/44.ogg"
aks "If I don't get a chance to see him, could you tell Shou I said goodbye?"
pf "Sure."
"He hesitates."
voice "audio/voice/E3/Free/SS/S3/aks/45.ogg"
aks "And that I'm sorry."
"I blink, but nod."
show akio smi
"Akio smiles and shakes my hand once more, then heads over to the parking lot."

hide akio with dissolve

"I get the feeling there's something Akio is hiding from Shou. He seemed truly remorseful just now. I wonder if he wants to be a big brother to Shou as badly as Shou wants him to be…"
"But if that's the case, why can't he be that brother?"
"I feel like I'm caught in the middle, which makes me sympathise even more with Shou. If I'm already feeling this torn, I can't imagine what Shou must be feeling."

scene black with fade

"The day is still young so I head to the mall to run some errands. The dispute between Shou and his brother is still fresh on my mind… I decide to go to the arcade to clear my head. There isn't much I can do so there's no use stressing about it."
"Shou sends me a text apologising for leaving me behind at the restaurant and a reassurance that he's fine."
"Then he asks me not to tell the others about this. I assure him I won't."
"Once the sun begins to set, I head back home."


stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E3SSS3_Completed = 1

jump E3D6S2