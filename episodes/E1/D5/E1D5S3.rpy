label E1D5S3:


"I know we have a whole week to work on our project, but I like getting my assignments done early. Hopefully Yuuna's the same way."
play sound "audio/sfx/Technology/Phone Dial.ogg"
"I dial her number and wait."

play sound "audio/sfx/Technology/Phone Answer.ogg"
"She picks up after a few rings."


voice "audio/voice/E1/D5/S3/yuuna/1.ogg"
ym "Hello?"
pf "Hi, Yuuna. It's [pfirst]."
voice "audio/voice/E1/D5/S3/yuuna/2.ogg"
ym "Hi! How are you?"
pf "Good. So, I was wondering if you wanted to get together and work on the project today."
voice "audio/voice/E1/D5/S3/yuuna/3.ogg"
ym "Sure! I'm actually glad you called. I wasn't sure about you, but I like getting a head start on my assignments."
"I can't help but smile."
pf "So do I."
"She laughs."
voice "audio/voice/E1/D5/S3/yuuna/4.ogg"
ym "Good thing we're partners! When are you free?"
pf "I'm free whenever. What about you?"
voice "audio/voice/E1/D5/S3/yuuna/5.ogg"
ym "Same."
pf "Okay, do you want to meet around noon?"
voice "audio/voice/E1/D5/S3/yuuna/6.ogg"
ym "Sure, at the library on campus?"
pf "Yeah, let's do that."
voice "audio/voice/E1/D5/S3/yuuna/7.ogg"
ym "Great, I'll see you then!"
pf "See you."
"We hang up."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)
play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(5.5)

"When I arrive on campus, I park my bike and wait in front of the library."

play ambient "audio/ambience/Campus.ogg" fadein 3
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg campus building day with fade



"It's a few minutes until noon. I hope Yuuna gets here soon."
"Every few minutes I check the time on my phone… {w}12:07… {w}12:13… {w}12:20… {w}She still hasn't arrived, so I text her."
"{i}Hey I'm here where are you?{/i}"

$renpy.pause(1.5)
play sound "audio/sfx/Technology/Phone Vibration Once.ogg" 
$renpy.pause(1.5)

"I don't have to wait long for my phone to vibrate."
"{i}Sorry! I'm still waiting for the bus. It should be getting here soon I think{/i}"
"{i}Ok I'll find us a room in the library{/i}"
"{i}Okay thanks{/i}"

stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
scene bg campus library day with fade

$renpy.pause(1.0)


"The library is mostly empty, which makes sense. Not too many people spend their Saturdays studying. Fortunately, that also means most of the collaborative spaces are open."
stop music fadeout 6
"Wandering the shelves, I gather a few reference books I think will be helpful, but I can't find the specific case study I'm looking for. Shrugging, I head into an empty room to wait for Yuuna. Flipping a nearby book to a random page, I half-heartedly skim it."
"I check the time again: 12:45. It doesn't seem like she's coming…"
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5.0
"Suddenly, I spot a flash of pink hair. {w}Yuuna is on the far side of the library searching for me. I wave at her and she smiles in acknowledgement before hurrying over."

$ yuuOut = "sCasual"

show yuuna ner at cc with dissolve
$renpy.pause(.5)

voice "audio/voice/E1/D5/S3/yuuna/8.ogg"
ym "I'm sorry I'm so late. The bus showed up way behind schedule, which is really unusual. I hope you aren't too angry with me."
"I return her smile."
pf "It's fine. I'm just glad you made it."
show yuuna smi with dissolve
"She slides into the chair across from me. I finally notice she isn't wearing her uniform."

menu:
    "I never realised how cute she is.":
        pf "You look really nice today. I like your outfit."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna smi b1 with dissolve
        "She blushes shyly."
        show yuuna hap b1 with dissolve
        voice "audio/voice/E1/D5/S3/yuuna/9.ogg"
        ym "Oh! Thanks. You look nice too."
        pf "Thanks."

    "She looks hot!":
        pf "I wish I could get you out of your uniform more often."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/10.ogg"
        ym "What?"
        "She furrows her brow."
        pf "Because that outfit really suits you."
        show yuuna cur
        voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
        ym "Oh…"
        show yuuna smi
        voice "audio/voice/E1/D5/S3/yuuna/12.ogg"
        ym "Thank you."
        
    "It's weird seeing her out of uniform.":
        pf "You look… different."
        show yuuna ner
        "She seems concerned."
        voice "audio/voice/E1/D5/S3/yuuna/13.ogg"
        ym "Is there something wrong?"
        pf "No, it's just weird seeing you in a sweater."
        show yuuna cur
        voice "audio/voice/E1/D5/S3/yuuna/14.ogg"
        ym "O-Oh… You don't like it?"
        pf "It's alright."

    "Don't say anything.":
        "It makes sense that she's not wearing a uniform since it's Saturday and I'm not wearing one either. No point in bringing it up when we can get straight to work."
        show yuuna cur
        "I notice Yuuna looking me over too."

show yuuna smi with dissolve
"She smiles."
voice "audio/voice/E1/D5/S3/yuuna/15.ogg"
ym "It's a little funny to see you out of uniform, but in a good way. It feels more personal somehow."
pf "Yeah, I understand."
"She points to the books beside me."
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/16.ogg"
ym "You already picked out references?"
"I nod."
pf "While I was waiting for you, but I couldn't find the case study we need."
voice "audio/voice/E1/D5/S3/yuuna/17.ogg"
ym "Did you check the database?"
pf "Not yet."
show yuuna smi
voice "audio/voice/E1/D5/S3/yuuna/18.ogg"
ym "Let's do that."
hide yuuna with dissolve
show yuuna smi at l3 with dissolve
$renpy.pause(.5)
"She stands and leads the way to the nearest computer. When we get there, she types in a quick search."
show yuuna thi with dissolve
voice "audio/voice/E1/D5/S3/yuuna/19.ogg"
ym "It says the book is available… Let's go check the shelves again."
hide yuuna with dissolve
"She leads me back towards the shelves, occasionally glancing back at me. Once we arrive, she scans the shelf for the book, and frowns when she doesn't see it."
show yuuna dis at cc with dissolve
show storm:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
$renpy.pause(.5)
voice "audio/voice/E1/D5/S3/yuuna/20.ogg"
ym "I don't understand. It should be here."
pf "Maybe the computer's wrong."
voice "audio/voice/E1/D5/S3/yuuna/21.ogg"
ym "Maybe… but we can't work on the project without it."
pf "Why don't we ask the front desk? Maybe they know where it is."
show yuuna smi
"She brightens up."
voice "audio/voice/E1/D5/S3/yuuna/22.ogg"
ym "Good idea."
"I start to head back the way we came, when I glance at the cart beside us. It's filled with books, but a specific title catches my eye."
pf "Wait--"
show yuuna cur with dissolve
"She pauses."
pf "Isn't that the book we need?"
"She leans towards the cart."
show yuuna hap
voice "audio/voice/E1/D5/S3/yuuna/23.ogg"
ym "It is!"
pf "Great!"
"I reach out to grab it..."
show shocked:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna sur with dissolve
"...but pause when I notice the horrified expression on Yuuna's face."
pf "What?"
voice "audio/voice/E1/D5/S3/yuuna/24.ogg"
ym "You can't just take that."
pf "Why not?"
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/25.ogg"
ym "That's the return cart."
pf "So?"
voice "audio/voice/E1/D5/S3/yuuna/26.ogg"
ym "The book hasn't been returned yet."
pf "What do you mean? It's already been checked back into the system and it's in the cart."
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/27.ogg"
ym "Yeah, but it hasn't been returned to the shelf yet."
pf "It'll be fine. We can make a copy of the section that we need and then put it back in this cart."
show yuuna ner
voice "audio/voice/E1/D5/S3/yuuna/28.ogg"
ym "But what if someone notices it's missing?"
"I glance around us. There isn't a librarian in sight."
pf "There's no one here. Besides, we'll be quick. Don't worry."
show yuuna thi
"She chews nervously on her lip before giving me a reluctant nod."
hide yuuna with dissolve
"I grab the book and we head for the copy machine. Yuuna's footsteps are nimble and quick and I have to catch up with her. She glances back at me frequently, obviously uncomfortable."
"She steps back when we reach the copy machine and let's me handle the copying. It takes a couple minutes for the machine to warm up, and Yuuna fidgets the entire time."
show yuuna neu at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/29.ogg"
ym "Is it working?"
pf "Yeah, it just needs a minute."
show panic:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/30.ogg"
ym "We should hurry up."
pf "Don't worry, we'll be fine."
"She seems unconvinced but stays quiet. The seconds seem to stretch and slow while we wait for the machine to process the copies. Yuuna continues to bite at her lip."
"Finally, the copier spits out our papers. Yuuna immediately collects them and begins walking. She quickens her pace the closer we get to the cart and doesn't relax until I nestle the book between its brethren."
pf "That wasn't so bad, was it?"
show yuuna smi
"She smiles faintly, but her face seems a little pale."
voice "audio/voice/E1/D5/S3/yuuna/31.ogg"
ym "At least we have what we need."
pf "Speaking of which, we should get to work."
"She nods and we return to our room."




stop ambient fadeout 3.0
stop music fadeout 2.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Ace Academy Library.ogg" fadein 2
play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
scene bg campus library dusk with fade

$renpy.pause(1.0)



"I type out the last couple of words on our report, then I lean back in my chair and grin at Yuuna."
pf "And we're done!"

show yuuna hap at cc with dissolve
"She breathes a sigh of relief."
show note:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/32.ogg"
ym "I'm glad we were able to get that finished. Now we don't have to worry about it for the rest of the week."
pf "Yeah."
show yuuna smi
"We'd been working for hours and it was getting pretty late."
"Yuuna is already packing up her laptop so I pack mine up too. She then layers the remaining reference books in her arms."
voice "audio/voice/E1/D5/S3/yuuna/33.ogg"
ym "I'll go ahead and return these."
pf "Do you need help with that?"
voice "audio/voice/E1/D5/S3/yuuna/34.ogg"
ym "No thanks. I'll just be a minute."
hide yuuna with dissolve
"She smiles reassuringly before she leaves."
"I tidy up the room while she takes care of the books and meet her outside of the building."



stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
scene bg campus building dusk with fade

show yuuna smi at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/35.ogg"
ym "Well, I better head to the bus stop."
pf "I'll go with you."

show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/36.ogg"
ym "Oh, you don't have to."
pf "I drove here so I don't mind. Besides, it's getting kind of late and who knows how long the bus will be."

show yuuna smi
"She nods and smiles in appreciation."


scene black with fade
$renpy.pause(1.5)
scene bg campus intersection dusk with fade


show yuuna smi at cc with dissolve
"The bus shelter is empty when we arrive, and as expected, the bus is nowhere to be found."
voice "audio/voice/E1/D5/S3/yuuna/37.ogg"
ym "We got a lot done today. You're very easy to work with."
pf "Thanks. For a moment, I thought you were ready to bail on me."
show yuuna cur
"She glances curiously at me."
voice "audio/voice/E1/D5/S3/yuuna/38.ogg"
ym "When was that?"
pf "When we found the case study."
voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
ym "Oh..."
show yuuna thi
"She shifts slightly."
voice "audio/voice/E1/D5/S3/yuuna/39.ogg"
ym "I thought about it. I've never done anything like that before."
"Now it was my turn to look confused."
pf "You've never borrowed a book?"
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/40.ogg"
ym "No, I've never borrowed a book {i}without permission{/i}."
pf "It wasn't really without permission..."
show yuuna dis
voice "audio/voice/E1/D5/S3/yuuna/41.ogg"
ym "We totally broke the rules!"
pf "I don't know if I'd go that far."
voice "audio/voice/E1/D5/S3/yuuna/42.ogg"
ym "We did! You're not supposed to use a book that's on the return cart. It's not done being processed."
pf "Yeah, but that's just a minor thing. It's like when you forget to clean up your tray in the cafeteria."
show yuuna neu
"She stares blankly at me."
pf "... Have you ever forgotten to clean up your tray?"
voice "audio/voice/E1/D5/S3/yuuna/43.ogg"
ym "Of course not. You're supposed to clean up after yourself."
pf "Okay, then it's like..."

label E1D5S3_YuunaLoopbackStart:
menu:
    "Taking extra chopsticks and napkins." if (E1D5S3_YuunaLoopbackOption1 == 0):
        $ E1D5S3_YuunaLoopbackOption1 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "When you're picking up food and you take extra chopsticks and napkins at the self-serve bar."
        show yuuna dis
        "Yuuna frowns."
        voice "audio/voice/E1/D5/S3/yuuna/44.ogg"
        ym "I only need one pair of chopsticks to eat."
        pf "They're for later."
        voice "audio/voice/E1/D5/S3/yuuna/45.ogg"
        ym "If everyone took things in excess then that leaves nothing for others."

    "Taking the pen from a bank." if (E1D5S3_YuunaLoopbackOption2 == 0):
        $ E1D5S3_YuunaLoopbackOption2 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "When you go to the bank--or anywhere with pens out in the open--and you take one of the pens after using it."
        show yuuna sur
        voice "audio/voice/E1/D5/S3/yuuna/46.ogg"
        ym "But that's {i}stealing{/i}!"
        pf "Usually it's by accident--you don't realise you've taken it until too late."
        show yuuna dis
        show storm:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        $renpy.pause(1.5)
        voice "audio/voice/E1/D5/S3/yuuna/47.ogg"
        ym "Accident or not--it's still taking something that doesn't belong to you."

    "Taking more than one after-dinner mint from a restaurant." if (E1D5S3_YuunaLoopbackOption3 == 0):
        $ E1D5S3_YuunaLoopbackOption3 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "When a restaurant has a bowl of mints or candy for the customers to take after a meal and you take more than one."
        show yuuna thi
        "She wrinkles her brow."
        voice "audio/voice/E1/D5/S3/yuuna/48.ogg"
        ym "I don't believe that's a custom in Japan."
        pf "Oh, must be an American thing then."

    "Taking extra free samples." if (E1D5S3_YuunaLoopbackOption4 == 0):
        $ E1D5S3_YuunaLoopbackOption4 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "When a store offers free samples and you wait a while before coming back again so the person handing out samples doesn't recognise you."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/49.ogg"
        ym "But what about the people who haven't already received a sample?"
        pf "What about them?"
        show yuuna dis
        voice "audio/voice/E1/D5/S3/yuuna/50.ogg"
        ym "If I take them, they won't have any."
        pf "They usually have a lot that they give away…"

    "Using multiple emails to vote for a contest entry when it's one vote per person." if (E1D5S3_YuunaLoopbackOption5 == 0):
        $ E1D5S3_YuunaLoopbackOption5 = 1
        $ E1D5S3_YuunaLoopbackCounter = E1D5S3_YuunaLoopbackCounter + 1
        pf "When a contest says it's only one vote per person so you use your other email accounts to vote for the entry you like."
        show yuuna neu
        voice "audio/voice/E1/D5/S3/yuuna/51.ogg"
        ym "But that would still be voting more than once per person because those emails belong to me."
        pf "Technically, I suppose it is."
        voice "audio/voice/E1/D5/S3/yuuna/52.ogg"
        ym "That's an unfair advantage."
        pf "Not if everyone does it."
        show yuuna dis
        "She gives me a disapproving look."

        
if (E1D5S3_YuunaLoopbackCounter == 3):
    jump E1D5S3_YuunaLoopbackEnd

else:
    pf "Okay, how about..."
    jump E1D5S3_YuunaLoopbackStart


label E1D5S3_YuunaLoopbackEnd:

$renpy.pause(.5)
show yuuna cur with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S3/yuuna/53.ogg"
ym "Do you do all of these things?"
pf "Um... no..."
"She stares at me with wide eyes."
voice "audio/voice/E1/D5/S3/yuuna/54.ogg"
ym "But that's breaking the rules."
pf "They're more like guidelines anyway."
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/55.ogg"
ym "I-I've never broken the rules."
pf "Not even once?"
show yuuna dis
voice "audio/voice/E1/D5/S3/yuuna/56.ogg"
ym "It would lead to utter chaos if everyone ignored the rules and did what they wanted."
pf "Kind of like this bus, right?"
show yuuna cur
voice "audio/voice/E1/D5/S3/yuuna/57.ogg"
ym "Huh?"
pf "Well, the schedule said it was supposed to be here about half an hour ago, but it's late."
show yuuna thi with dissolve
voice "audio/voice/E1/D5/S3/yuuna/11.ogg"
ym "Oh..."
show storm:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna dis
"She looks disappointed."
voice "audio/voice/E1/D5/S3/yuuna/58.ogg"
ym "I was hoping the bus issue would resolve itself before I had to go home."
pf "It doesn't seem like it's coming. Can anyone pick you up?"
"She shakes her head."
show yuuna neu
voice "audio/voice/E1/D5/S3/yuuna/59.ogg"
ym "My family is out of town this weekend. It's fine, I take the bus all the time."

label E1D5S3_StayLongerLoop:
menu:
    "Go home.":
        pf "Are you sure you'll be okay here?"
        show yuuna smi
        "She nods."
        voice "audio/voice/E1/D5/S3/yuuna/60.ogg"
        ym "Yes."
        pf "Alright, then I better get back before it gets too late."
        show yuuna smi
        voice "audio/voice/E1/D5/S3/yuuna/61.ogg"
        ym "Sure."
        pf "Text me when you get home."
        voice "audio/voice/E1/D5/S3/yuuna/62.ogg"
        ym "Okay."
        "She waves goodbye and I wave back, before heading to my bike and driving home."
        jump E1D5S7

    "Stay with her longer." if (E1D5S3_StayWithYuunaLoop == 0):
        $ E1D5S3_StayWithYuunaLoop = 1
        pf "Well, I'll wait with you a while longer. Hopefully it'll show up."
        show yuuna smi
        "She brightens up."
        voice "audio/voice/E1/D5/S3/yuuna/63.ogg"
        ym "You don't have to do that, but thanks. It's always nice to have company."
        
        scene black with fade
        $renpy.pause(1.5)
        scene bg campus intersection dusk with fade
        
        show yuuna thi at cc with dissolve
        
        "After another half an hour, the bus still doesn't show up."
        jump E1D5S3_StayLongerLoop

    "Offer her a ride.":
        pf "I can take you home."
        show yuuna smi
        "She smiles but shakes her head."
        voice "audio/voice/E1/D5/S3/yuuna/64.ogg"
        ym "I don't want to cause any trouble for you. I don't mind waiting."

        if (E1D2S2_talkwithyuunayes == 1):
            pf "It's no trouble at all. We ride the same bus line so you're on my route home."

        else:
            pf "You're waiting for bus 85 which goes to my area of Isokaze as well. It's no trouble at all."

voice "audio/voice/E1/D5/S3/yuuna/65.ogg"
ym "That's very kind of you, but you don't have to worry about me. I'm used to waiting for the bus."
pf "I know, but it's getting late and if I left you here alone I'd be worried you never got home safely."
show yuuna cur b1 with dissolve
"Her cheeks tinge pink and she looks away, a small smile playing at her lips."
voice "audio/voice/E1/D5/S3/yuuna/66.ogg"
ym "You'd be worried about me?"
pf "Yeah."
show yuuna smi b1
"She looks back at me, a full smile on her face."
voice "audio/voice/E1/D5/S3/yuuna/67.ogg"
ym "Well, it will get dark soon... and I wouldn't want you to worry..."
"I grin at her."
pf "Come on, let's go pick up my bike."
show yuuna hap b1
"She returns my smile with an even brighter smile."
voice "audio/voice/E1/D5/S3/yuuna/68.ogg"
ym "Okay, thanks."



stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
scene bg campus parking dusk empty with fade


"When we reach my bike, Yuuna's eyes widen in appreciation."
show yuuna cur at cc with dissolve
voice "audio/voice/E1/D5/S3/yuuna/69.ogg"
ym "You have a beautiful ride."
"I can't help myself from feeling a warmth of pride."
pf "Thanks! I brought her back from the States. She goes everywhere with me."
"I hop on my bike and pat the seat behind me. She carefully climbs on."
pf "Are you ready?"
show yuuna thi
voice "audio/voice/E1/D5/S3/yuuna/70.ogg"
ym "Um..."
pf "What is it?"
voice "audio/voice/E1/D5/S3/yuuna/71.ogg"
ym "What am I supposed to hold on to?"
pf "Oh... well, you're kind of supposed to hold onto me..."
show shoBlush:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
show yuuna sur b2 with dissolve
voice "audio/voice/E1/D5/S3/yuuna/72.ogg"
ym "What?!"
pf "What's wrong?"
show yuuna ner b2
show panic:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/73.ogg"
ym "Um, this was a bad idea. I--I should go wait for the bus."
"I feel her squirm behind me."

$ qtebase = 3
$ qtetotal = qtebase
$ t_var = qtetotal
show screen timer_scr(place="E1D5S3_timeout")

menu:
    "Help her.":
        $ renpy.hide_screen ("timer_scr")
        $ E1D5S3_HelpedYuuna = 1
        "Before she can hop off the bike, I reach back, grab her hands, and wrap her arms around my waist. Yuuna lets out a small gasp."
        pf "See? This isn't so bad, right?"
        show yuuna cur b2
        voice "audio/voice/E1/D5/S3/yuuna/74.ogg"
        ym "Umm, r--right..."

    "Let her go.":
        label E1D5S3_timeout:
        $ renpy.hide_screen ("timer_scr")
        "In one smooth motion she slides off the bike. Her cheeks are as pink as her hair."
        show yuuna smi b2
        voice "audio/voice/E1/D5/S3/yuuna/75_2.ogg"
        ym "Thank you for the offer."
        pf "Are you sure you don't want a ride?"
        voice "audio/voice/E1/D5/S3/yuuna/76_2.ogg"
        ym "Yeah, I'll see you another time."
        pf "Okay..."
        "She gives me one last smile before turning away. Once she's out of sight, I start my engine and go home."
        jump E1D5S7


stop ambient fadeout 3.0
scene black with fade
play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 4
$renpy.pause(3.0)

play sound2 "audio/sfx/Vehicles/Bike driving off.ogg" fadein 3 fadeout 5
$renpy.pause(3.0)

"I can feel the warmth of Yuuna against me and the softness of her chest pressing against my back...{w} I try not to think about it."
stop music fadeout 12

"Her grip tightens around my waist as we continue down the freeway."
"Yuuna diligently directs me towards her house. The scenery blends into a blur of colour as we drive by."
"After a few minutes, Yuuna's directions sound more confident and there's a tinge of excitement in her voice. Her grip relaxes slightly and I'm acutely aware of every time she presses close to me to speak."
"I feel her hand slip away for a moment--I assume to push the hair out of her eyes--and her chest pushes up against me again as she sighs."
pf "Are you okay?"
voice "audio/voice/E1/D5/S3/yuuna/75.ogg"
ym "Yes--sorry--I just love sunsets and the view right now is breath-taking."

play music "audio/music/Tender Moments (GAME VERSION).ogg" fadein 3.0

$renpy.pause(1.0)
$ persistent.gpix[64][0] = 1
show cg yuuna bike evening:
    alpha 0
    xzoom .60
    yzoom .60
    yoffset -50
    xoffset 150
    
show cg yuuna bike evening:
    parallel:
        easein 3.0 alpha 1.0
    parallel:
        easein 3.0 xoffset 50


$renpy.pause(2.0)

"I quickly glance towards the sun as it hovers over the horizon, reflecting a trail of golden fire on the glittering waves of the ocean."
pf "You definitely don't see sunsets like these in New York. I could get used to this."
voice "audio/voice/E1/D5/S3/yuuna/76.ogg"
ym "Are you liking it in Isokaze so far?"
pf "Yeah, but I haven't seen much outside of ACE."
voice "audio/voice/E1/D5/S3/yuuna/77.ogg"
ym "You should go to the park. It's so beautiful--especially in spring when the cherry blossoms bloom. I used to go there all the time and play on the statues."
voice "audio/voice/E1/D5/S3/yuuna/78.ogg"
ym "You'll learn a lot about the town's culture and history there too. Although I haven't been there since--a while so I'm not sure if it's changed at all."
pf "Maybe you can come with me and show me."
"She pauses." 

voice "audio/voice/E1/D5/S3/yuuna/79.ogg"
ym "Sure… After all, Isokaze is a pretty special place."
pf "Yeah, I'm beginning to see that."
"She leans closer into me, but doesn't say anything more." 

show cg yuuna bike evening:
    parallel:
        linear 3.0 xoffset 0
    parallel:
        linear 3.0 yoffset -50
    parallel:
        linear 3.0 xzoom .5
    parallel:
        linear 3.0 yzoom .5
    parallel:
        linear 2.5 alpha 0

$renpy.pause(2.0)
stop music fadeout 3.0
scene black with fade     
$renpy.pause(1.0)

"Before long, we arrive at her house."

play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 4.0
scene bg isokaze neighborhood night with fade

"She slips off the bike and waits for me to do the same. As I walk her to her front door, she turns to me. I don't anticipate her stopping and almost trip into her, but catch myself just in time. Still, I hear a slight gasp when she notices how close we are to each other. She suddenly becomes shy and takes a small step back."

show yuuna smi b1 at cc with dissolve

voice "audio/voice/E1/D5/S3/yuuna/80.ogg"
ym "Thanks for taking me home. I had a nice time today."
pf "Me too. Maybe we can hang out again?"
voice "audio/voice/E1/D5/S3/yuuna/61.ogg"
ym "Sure."
pf "And do something besides study."

show yuuna hap b1
"She laughs."
show regBlush:
    xoffset 720
    yoffset 100
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S3/yuuna/81.ogg"
ym "I'd like that."

show yuuna smi b1 with dissolve
voice "audio/voice/E1/D5/S3/yuuna/82.ogg"
ym "Have a good night. Get home safely, okay?"
pf "I will. Talk to you later."
hide yuuna with dissolve
$renpy.pause(.5)
"She turns towards her door while I go back to my bike. As I switch on the engine, I see her turn around. She gives me a brief wave before heading inside, and I wave back before heading home."

stop music fadeout 3.0
scene black with fade
$renpy.pause(2.0)   


jump E1D5S7