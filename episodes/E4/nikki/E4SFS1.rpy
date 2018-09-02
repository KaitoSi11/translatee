#WEEKEND EVENT
label E4SFS1:

$ yukOut = renpy.random.choice(['sweater'])
$ kaiOut = renpy.random.choice(['sCasual'])
$ nikOut = renpy.random.choice(['sCasual'])
$ nikHairF = renpy.random.choice(['default'])
$ nikHairB = renpy.random.choice(['default'])


"I can hear both Kaito and Nikki downstairs. Does she not work today?"
scene black with fade
"I've barely seen Nikki since she started working at the restaurant, and although I didn't have classes this week, I was still busy with school."
"Maybe we can catch up today…"
scene bg homekaito main day with fade 
"As soon as I head downstairs, Kaito and Nikki greet me with matching grins. It's like they were waiting for me."
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
show kaito mis at l2
show nikki mis at r2:
    xzoom -1
with dissolve

"I have a bad feeling about this…"

voice "audio/voice/E4/Kaito/E4Nikki/(9).ogg"
hk "Hey bud, sleep well last night?"
pf "Um, yeah, thanks."
show nikki smi
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki01.ogg"
sf "That's good! Feeling well rested?"
pf "...Yes…"
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki02.ogg"
sf "Great!"
"Their smiles don't budge."
pf "What's going on?" 
show kaito hap
voice "audio/voice/E4/Kaito/E4Nikki/(10).ogg"
hk "Oh, nothing… We just had a small favour to ask."
show nikki neu
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki03.ogg"
sf "Yes, so small! Teeny tiny!"
"That doesn't sound promising."
pf "What is it?"
show kaito smi
voice "audio/voice/E4/Kaito/E4Nikki/(11).ogg"
hk "We're a little understaffed at one of our restaurants."
voice "audio/voice/E4/Kaito/E4Nikki/(12).ogg"
hk "More specifically, the one Nikki works at."
"Nikki nods."
show nikki cur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki04.ogg"
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed06.ogg"
sf "We were hoping you could come and help out!"
"Really? That's it?"
pf "Uh, I guess I could help... I don't have any other plans right now..."
show nikki hap
show kaito mis
"Kaito bursts into a big grin."
voice "audio/voice/E4/Kaito/E4Nikki/(1).ogg"
hk "Perfect! He said yes!"
show nikki smi
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed07.ogg"
sf "He can't back out now!"
pf "What?"
hide kaito with dissolve
"Kaito races towards the door."
voice "audio/voice/E4/Kaito/E4Nikki/(2).ogg"
hk "I'll be in the car! Come out when you guys are ready!"
show nikki cur
"He disappears, leaving a nervous-looking Nikki."
pf "What did he mean by ready?"
show nikki smi
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed08.ogg"
sf "Don't worry about it."
"I narrow my eyes."
pf "Nikki."
show nikki neu
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed09.ogg"
sf "It's nothing! The restaurant is just doing a theme today."
"Oh no… any theme is bound to be bad."
pf "What kind of theme?"
show nikki cur
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed10.ogg"
sf "One of maids… in a cafe..." #Really really small text
pf "Maid cafe?!"
show nikki smi
"She slides to the side and reveals a neatly pressed butler costume."

menu:
    "Sounds like fun!":
        $ E4SFS1_Fun = 1
        "My eyes widen. What a snazzy outfit!"
        pf "Ooh, this is kind of exciting! I've never done anything like this before."
        show nikki ske
        "Nikki looks suspicious."
        voice "audio/voice/MISSING/BATCH7/Nikki_final_missed11.ogg"
        sf "You really don't mind?"
        pf "Of course not! I'm always down to try something new. Plus, I can't keep my uncle and sister hanging."
        show nikki smi
        "Nikki jumps up and squeezes me in a big hug."
        voice "audio/voice/MISSING/BATCH7/Nikki_final_missed12.ogg"
        sf "Thanks! You're the best!"
        pf "No problem. Let's hurry up and get changed. Uncle Kaito is waiting."

    "NO.":
        "Haha! Not happening!"
        show nikki sur
        "Wordlessly, I turn around and head back up the stairs."
        show nikki dis
        stop music fadeout 4
        voice "audio/voice/MISSING/BATCH7/Nikki_final_missed13.ogg"
        sf "H-Hey! Where do you think you're going?"
        pf "Somewhere that's not a maid cafe."
        "She frowns."
        voice "audio/voice/MISSING/BATCH7/Nikki_final_missed15_02.ogg"
        sf "Really?"
        pf "Yes, really."
        show nikki thi
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki3.ogg"
        sf "Okay..."
        "Wait, that was too easy..."
        show nikki sad
        "Nikki looks down."
        "Oh no… not this!"
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki4.ogg"
        sf "I-I just thought you'd want to spend some time with me..."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki06.ogg"
        sf "And it's just a tiny request..."
        show nikki win
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki07.ogg"
        sf "But if you can't, it's okay... you can't..."
        "She ends with a series of sniffles."

        menu:
            "WOMAN TEARS, MY ONLY WEAKNESS.":
                pf "Ugh, fine I'll go."
                show nikki smi
                "Nikki immediately perks up."
                play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
                voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki08.ogg"
                sf "Okay, good, hurry up and get dressed!"
                "She grins and starts fussing with the outfits."
                "How can she do that so convincingly?!"
                "Oh well, I guess there's no turning back now."

                
hide nikki with dissolve
scene black with fade
"I grab the outfit, then head to my room and get changed. Once I'm done, I look in the mirror."

if E4SFS1_Fun == 1:
    "Looking good [pfirst]!"
else:
    "It might not be my first choice in outfit, but I still look pretty damn good."


    
$ nikOut = renpy.random.choice(['maid'])

scene bg homekaito main day with fade 
"Nikki is waiting for me downstairs, dressed in her maid outfit."
show nikki hap at cc with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki09.ogg"
sf "Looking sharp, big bro!"
pf "Thanks, you're not looking too bad yourself."
show nikki smi
"Nikki grins."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki10.ogg"
sf "Let's not keep Kaito waiting any longer."
"I nod and we both head out."
stop ambient fadeout 3

scene black with fade 
"As soon as I step into the car, Kaito's eyes widen and he chokes back a laugh."
voice "audio/voice/E4/Kaito/E4Nikki/(3).ogg"
hk "Ahem, that's a good look for you."
"What a guy."
stop music fadeout 8
pf "Where's your costume, Uncle?"
"His laugh fills the car."
voice "audio/voice/E4/Kaito/E4Nikki/(4).ogg"
hk "Oh, no, I'm not working. I'm just the chauffeur."
pf "Too bad. I bet you would have been a hit."
voice "audio/voice/E4/Kaito/E4Nikki/(5).ogg"
hk "Oh there's no doubt about that."
"As soon as we arrive, Kaito waves goodbye, and I follow Nikki in."


scene bg campus cafe day with fade

play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 5
"Nikki introduces me to all of her colleagues and they greet me with pleasant smiles. Everyone else is dressed up as well, which is comforting. A part of me was worried that this was all an elaborate hoax."

"The \"head butler\" gives me a rundown of the basics and how to act."
"I'm reminded of my high school days when I waited tables. It's pretty much the same thing but with a whole lot more \"miss\" and \"sir\" strewn in."

show nikki neu at cc with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki11.ogg"
sf "You all good?"
"Nikki pokes her head in our room just as we finish the training."
pf "Yep."
show nikki smi
"She smirks."
play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki12.ogg"
sf "This is going to be so much fun!"
hide nikki with dissolve
"She grabs my hand and we head out onto the floor."

"It's a little daunting at first, but the customers are all thrilled and it's not long before I get into character. This is a lot more fun than I originally thought!"

"This is the first time I've seen Nikki at work. She flits from table to table, charming everyone she meets. Most of the regulars request to be placed in her in section and are even willing to wait until her tables are free. {w}I've even had a few of my tables ask if she could come over so they could meet her. Whenever that happens, Nikki would happily oblige and shoot me a smug grin."
"Oh, it's on now! I won't be beaten so easily!"
"I up my butler game--something I never thought I'd ever have to do--and step up to the plate! At least now my customers aren't requesting for Nikki anymore. Ha!"
"As the cafe fills up and we're getting loaded with people, we somehow both end up at the same table."
pf "How can I serve you today?"
show nikki smi at cc with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki13.ogg"
sf "It would be my honor to serve you today!"
"She shoots them big doe eyes and an endearing smile. {w}Curses! In a battle of adorableness, I would never win."
pf "Ah, it would seem that you are already in good hands. My apologies."
"I bow. The customers look at me with interest."
show nikki cur
voice "audio/voice/E4/Cafe Customer 1/E4/Nikki/1.ogg"
cafec1 "Oh my, what a gentleman!"
"Nikki gives me a dirty look when the table isn't paying attention, then looks apologetic."
show nikki cur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki14.ogg"
sf "Oh! I'm so sorry! You were here first!"
"She pouts."
show nikki win
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki15.ogg"
sf "Please forgive me!"
voice "audio/voice/E4/CafeCustomer2/E4/Nikki/1.ogg"
cafec2 "She's adorable!"
show nikki neu
"I'm losing them!"
pf "No no, it's okay. I insist. Your care and attention is at a level I strive to achieve."
show nikki smi
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki16.ogg"
sf "You're too humble! Your ability to predict customer's needs is commendable!"
voice "audio/voice/E4/Cafe Customer 1/E4/Nikki/2.ogg"
cafec1 "Oh my goodness, what a cute couple!"
show nikki sur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki17.ogg"
sf "Couple?!"
pf "Couple?!"
show nikki ske
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki18.ogg"
sf "Hold on, I think you have the wrong idea--"

show highschoolgirl extra at l3 with dissolve
voice "audio/voice/E4/Nikki_FemaleHighSchooler1/FHS_01.ogg"
hstu1f "Nikki! You finally did it!"
show highschoolgirl2 extra at r3 with dissolve
voice "audio/voice/MISSING/BATCH3/1.ogg"
hstu3f "I knew it! Even {i}other{/i} people can see it!"

show nikki sur
"Nikki's eyes widen as her two friends skip over."
"Are they stalking me?!"
show nikki cur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki19.ogg"
sf "You guys, what are you doing here?"
#hstuf1 "You told us to come support you, remember?"
#hstuf3 "She's too busy being in love to remember silly things like that."
"Nikki's friends look at each other then giggle."
voice "audio/voice/E4/Nikki_FemaleHighSchooler1/FHS_02.ogg"
hstu1f "It was only a matter of time before they kindled their relationship."
voice "audio/voice/MISSING/BATCH3/2.ogg"
hstu3f "I'm so happy for you two!"

voice "audio/voice/MISSING/BATCH1/3.ogg"
cafec1 "They really are lovely together!"
show nikki ner
"Their outbursts catch the attention of other restaurant patrons, and soon everyone is making comments about \"the lovely couple\"."
show nikki sur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki20.ogg"
sf "Wait--you guys have it all wrong!"
pf "Uhh yeah, we're actually brother and sister."
show nikki ske
stop ambient fadeout 2.5
stop music fadeout 1.5
"The cafe goes silent."

voice "audio/voice/MISSING/BATCH1/4.ogg"
cafec1 "Wait, despite being siblings, they are true to their hearts?"
voice "audio/voice/E4/CafeCustomer2/E4/Nikki/2.ogg"
cafec2 "It's even more romantic than I thought!"
show nikki sur
voice "audio/voice/E4/Nikki_FemaleHighSchooler1/FHS_03.ogg"
hstu1f "So cute!"

play sound "audio/sfx/general/cheering.ogg" fadein 3
"The crowd looks at each other then starts clapping and cheering!"

play music "audio/music/Baka! (GAME VERSION).ogg" fadein 5
show nikki win
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki21.ogg"
sf "No, no, no! Ugh!"

show nikki ann
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki22.ogg"
sf "He's my brother. We are NOT in that kind of a relationship!"
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki23.ogg"
sf "This isn't an anime! These things don't happen!"
"She points at me."
show nikki dis
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki24.ogg"
sf "I do love my brother--"
play sound "audio/sfx/general/cheering.ogg" fadein 2
"The crowd cheers again."
stop sound fadeout 1
show nikki ang
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki25.ogg"
sf "NO! Let me finish!"
show nikki dis
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki26.ogg"
sf "I love my brother as my {i}brother{/i}. But what you guys are trying to {i}hint{/i} at will never, ever, EVER be a thing!"
"Nikki huffs and crosses her arms. Her message comes across loud and clear."
voice "audio/voice/MISSING/BATCH1/5.ogg"
cafec1 "What about as...DLC?"
show nikki ang
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki27.ogg"
sf "NO."

scene black with fade

"Despite the little {i}bump{/i} in the day, the rest of the shift goes well. A lot of people would pull me aside and repeat, \"I'm sorry she doesn't feel the same... unrequited love can be so tough...\""
stop music fadeout 4
"Whatever that means."
"As we wait for the bus home, Nikki makes me promise never to speak of this day again. I am all too happy to agree."

scene bg homekaito main night with fade
play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 7
"When we arrive home, Yuki and Kaito are sitting on the couch, huddled beneath a blanket."
"As soon as Kaito sees me, he grins."
show kaito smi at l3:
    xoffset -200
show yuki smi at l2
with dissolve

voice "audio/voice/E4/Kaito/E4Nikki/(6).ogg"
hk "How was your day, bud?"

if E4SFS1_Fun == 1:
    pf "Pretty fun actually!"
    show kaito mis
    voice "audio/voice/E4/Kaito/E4Nikki/(7).ogg"
    hk "I'm glad you enjoyed yourself!"

else:
    pf "I hate you."
    show kaito hap
    "Yuki and Kaito burst out laughing."
    show kaito hap
    voice "audio/voice/E4/Kaito/E4Nikki/(8).ogg"
    hk "Aw, it couldn't have been all bad."

show yuki smi
voice "audio/voice/E4/Yuuki/E4/Nikki/1.ogg"
hy "You guys hungry? I can whip something up!"
pf "Sure."
show nikki smi at r3 with dissolve:
    xzoom -1
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki28.ogg"
sf "We can't say no to Aunt Yuki's delicious cooking!"
show yuki hap
voice "audio/voice/E4/Yuuki/E4/Nikki/2.ogg"
hy "Aw, thank you."
show kaito dis
#hk "Hey! How come you guys weren't so thankful when I was cooking?"
"Kaito furrows his brows and is just about to speak when Nikki chimes in immediately."
show nikki ske
show yuki smi
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki29.ogg"
sf "Ordering take-out is not cooking."
show kaito mis
"Kaito laughs then grins."
voice "audio/voice/MISSING/BATCH4/Kaito_MissingLines-03.ogg"
hk "Well {i}someone{/i} had to cook it."
"Nikki and Yuki both sigh."
show nikki dis
show yuki dis
with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Nikki30.ogg"
sf "You're hopeless!"
voice "audio/voice/E4/Yuuki/E4/Nikki/3.ogg"
hy "You're hopeless!"
show nikki cur
show yuki cur
show kaito cur
pf "Whoa…"
"That was scarily in sync!"
show nikki smi
show yuki hap
with dissolve
show kaito smi
with dissolve
"They blink at each other, then laugh as Kaito and I join in. Aunt Yuki and Nikki head into the kitchen together."

scene black with fade

"I offer to help out but they both respond with a firm \"no\". I can tell when I'm not wanted..."
"Uncle Kaito and I hang out together until it's time for dinner. After an amazing meal, we settle down and Nikki suggests another family movie night. With everyone's busy schedules, it's rare for all of us to spend the evening together. Still, I hope this will become a more frequent thing!"
"We stay up way past our bedtimes watching movies, and Kaito falls asleep on the couch. As we giggle at his snores, we all decide it's time to go to bed."
"I return to my room and easily fall to sleep."







stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
jump E4D7S1
$ E4SFS1_Completed = 1