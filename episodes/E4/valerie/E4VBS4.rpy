#WEEKEND
label E4VBS4:

$ valHairF = "default"
$ valHairB = valHairF
$ valOut = "sDate"

play ambient "audio/ambience/Morning.ogg" fadein 3
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
scene bg homekaito myroom day with fade

"I wake up at the sound of my alarm and stretch."

if E4VBS3_Nofancoaster == 1:
    "Today is the day I face my fears and ride the plummeting carriage of doom."
else:
    "Today is going to be an amazing day full of fun rides and overpriced food!"

"I throw back my blankets, feeling wide awake, and get ready."
stop ambient fadeout 3
scene black with fade
"After eating a hearty breakfast, I hop on my bike and head to the train station."
scene bg travel trainstation day with fade
"I spot Valerie on the platform. She greets me with a hug."
show valerie hap at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL156.ogg"
vb "Hey you, ready for our date?"
pf "Of course I am, but are you?"
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL157.ogg"
vb "Are you kidding? This is the highlight of my week!"
"I grin."
pf "I like your enthusiasm."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"The train soon arrives and we climb aboard. Valerie claims a window seat and watches the trees zip by. I wonder what she's thinking about."
"The gentle roar of the engines relaxes me and soon lulls me to sleep."
"Valerie shakes me awake when we arrive."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL158.ogg"
vb "Wake up, sleepyhead. We're here."
"I blink the sleep out of my eyes and follow Valerie off the train."
play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
scene bg amusementpark day with fade
"As we exit the station, I can see the colourful rails of roller coasters twisting around each other. Every few seconds, screams permeate the air as a coaster whizzes past."
"The ferris wheel towers above the rest of the attraction, like a beacon guiding visitors to their destination."
"\"Marvelous World!\" hangs above the entrance in huge letters. We have a Marvelous World back in the States too, which I haven't been to since I was young. I wonder if this one will be similar to the American one."
"Valerie grabs my hand and squeals."
show valerie hap at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL159.ogg"
vb "How cool is that?! Let's go!"
"She takes off running towards the entrance, dragging me behind her. After we pay for our tickets and get past the main gates, Valerie slowly spins in a circle, drinking in the sights around her."
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL160.ogg"
vb "What should we do first?"
"I squint at the map in my hands."


label E4VBS4_Loopback:
$ E4VBS4_LoopCounter += 1

menu:
    "The spinning ride!" if E4VBS4_choice1 == 0:
        $ E4VBS4_choice1 = 1
        "A lot of people hate the spinning ride, but it's my favourite! I point to it on the map."
        pf "This one, the Breakfast Scrambler."
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL161.ogg"
        vb "Okay! Lead the way!"
        "I follow the map and weave through the park. Valerie holds onto my hand, half smiling at the attractions and half avoiding walking into people."
        "When we arrive, she squeals again."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL162.ogg"
        vb "This is so cute!"
        "While waiting in line, she stakes out which plate she wants to ride. When it's our turn to file on, she heads straight towards a pink plate and sits between two strips of bacon while I sit on a scrambled egg opposite her."
        pf "Don't forget to hold on!"
        show valerie mis
        "She grins and grabs onto the wheel in the middle, giddy with excitement."
        hide valerie with dissolve
        "As the ride jerks to a start, the two of us twist the wheel as quickly as possible and spin so quickly I feel as if we're going to fly off into the distance."
        "Valerie laughs as the wind whips her hair."
        "Eventually the ride stops, but the world keeps on spinning. On unsteady legs,we stumble off the ride. Valerie giggles when she stumbles into me."
        show valerie cur at cc with dissolve
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL163.ogg"
        vb "It's like being drunk."
        "We make our way to the nearest bench and plop down. Valerie leans on me."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL164.ogg"
        vb "That was fun!"
        pf "Yeah, I love that ride! I'm kind of surprised you do too. Nikki hates it."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL165.ogg"
        vb "Really? It's kind of topsy-turvey, like you're rebelling against your own body and trying to do your own thing! Right now my body is trying to catch up with my brain."
        pf "Ha, that's an interesting way to view it."
        pf "I'm just glad nobody puked."
        show valerie wor
        "Valerie wrinkles her nose."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL166.ogg"
        vb "I don't even want to think about that!"

    "A roller coaster!"if E4VBS4_choice2 == 0:
        $ E4VBS4_choice2 = 1
        "One thing this park does not skimp on is roller coasters."

        if E4VBS3_Nofancoaster == 1:
            pf "It's time for me to be a man."
            show valerie cur
            "Valerie looks at me curiously."
            pf "Let's go on a roller coaster."
        else:
            pf "I want to go on a roller coaster."

        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL168.ogg"
        vb "Yes! That sounds fun! Which one?"
        pf "I'm not sure. You pick."
        "I hand the map over to Valerie, which she ignores. Instead she looks up at the sky."
        show valerie cur
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL169.ogg"
        vb "I want to go on that red one!"
        "I look to where she's pointing, then consult the map."
        pf "That one is the Dragon's Roar."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL170.ogg"
        vb "Oooh, it already sounds promising."
        "Following the map, we make our way towards the ride. As we get closer, I can see all the twists and turns… at one point we even go upside down!"
        
        if E4VBS3_Nofancoaster == 1:
            "Oh no… what did I just get myself into?"
        else:
            "Whoa! That's pretty intense!"
            
        "We get in line, and then climb into the car and get strapped in."
        hide valerie with dissolve
        "My feet are dangling off the ground, and Valerie swings her legs excitedly."
        "Suddenly, the ride jerks to a start and slowly climbs higher and higher. My heart beats faster in anticipation, and pumps wildly when we pause."
        "The beginning of the ride is shaped like a large dragon's mouth. We hear a sucking noise, as if breathing in air, then when the exhale comes, we shoot forward at lightning speed!"

        menu:
            "WOAH!":
                "A hoarse scream rips out of my throat as we go speeding along the rails!"

            "Pokerface!":
                "I clutch at my harness as we speed along the rails!"

        
        "Valerie shrieks beside me, a huge smile on her face."
        "In a blink of an eye, the ride slows to a stop and we file out. My heart gradually calms down as we walk back to the main path."
        "Valerie grins playfully."
        show valerie hap at cc with dissolve
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL171.ogg"
        vb "Was it as good for you as it was for me?"
        if E4VBS3_Nofancoaster == 1:
            pf "Never again."
        else:
            pf "Definitely one of the better ones I've been on!"
            
        show valerie mis
        "Valerie grins."


    "Must eat everything!" if E4VBS4_choice3 == 0:
        $ E4VBS4_choice3 = 1
        show valerie smi
        "I look around at all the different food options. There are the familiar favourites like funnel cake and cotton candy, along with some unusual favourites like takoyaki and yakitori."
        pf "What's the point of going to an amusement park if we don't get fair food?"
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL172.ogg"
        vb "Ooh, good thinking. I can't leave before getting a funnel cake!"
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL173.ogg"
        vb "What are you going to get?"

        menu:
            "Yakitori.":
                pf "Yakitori! Everything is better on a stick!"
                show valerie mis
                "Valerie grins."

            "Takoyaki.":
                pf "Takoyaki! Can't get enough of those little balls!"
                show valerie mis
                "Valerie smirks."
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL174.ogg"
                vb "No comment."

            "Funnel cake.":
                pf "Also a funnel cake."
                "She smirks."
                show valerie hap
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL175.ogg"
                vb "You have good taste."

            "Cotton Candy.":
                pf "Cotton candy!"
                show valerie sur
                "My voice came out in a squeak. Valerie laughs as I flash her a sheepish smile."
                show valerie hap
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL176.ogg"
                vb "Come along then. Hold my hand so you don't get lost."

        "We chow down on our food, and Valerie devours her entire funnel cake."
        show valerie hap
        pf "Whoa! That's impressive! Most people aren't able to eat the whole thing."
        show valerie cur
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL177.ogg"
        vb "It was just too delicious to stop!"


if E4VBS4_LoopCounter == 2:
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL179.ogg"
    vb "Okay, my turn to choose!"

else:
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL178.ogg"
    vb "What do we want to do next?"
    jump E4VBS4_Loopback


"Valerie grabs my hand and weaves through the crowd of people."
pf "Where are we going?"
show valerie mis
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL180.ogg"
vb "You'll see."
hide valerie with dissolve
"I blindly follow Valerie as she expertly dodges people. If I were small and petite I could slip between people too… but I'm not, so it's a good thing she's holding onto me."
"Eventually, she pauses in front of the Ferris Wheel."
stop music fadeout 6
"We get in line, and she disappears for a second. Where did she go? I don't have to worry long, though, before she returns as if nothing had happened."
scene black with fade
"Once our turn is up, we slip into the seat and pull the bar down around us. Then the wheel gently begins to turn and we rise above the park."
"The people look like ants on the ground, scurrying back and forth, shuffling in lines. The store fronts and stalls look like blocks from children's toys."
"Valerie stares below."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL181.ogg"
vb "Doesn't everything feel so surreal from up here? All the small things seem so insignificant."
pf "Yeah…"
"As soon as reach the peak, the wheel jerks to a stop."
pf "Uh, is this a part of it?"
"Valerie doesn't answer, but looks at me."
pf "What are the odds of us getting stuck up here? It's like every single rom com out there."
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
"She smirks."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL182.ogg"
vb "I know. I asked the guy to do this."
$ persistent.gpix[60][0] = 1
scene cg valerie ferris wheel with Dissolve(2.0):
    xzoom .5
    yzoom .5
"She slips her hands around my arm."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL183.ogg"
vb "Romantic, right?"
pf "How did you get him to do that?"
"She looks up at me, smiles alluringly, and bats her eyelashes."
pf "Ah, I see. I thought you just paid him off."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL184.ogg"
vb "I wish I had that kind of money to burn… but at least I've still got my charms."
pf "Well, not everyone can be as charming as you."
"Valerie blushes slightly, then kisses me."
pf "Mm, now I've been charmed too."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL185.ogg"
vb "You're not the only one."

menu:
    "Kiss her.":
        "I put my arm around her and pull her close to me then kiss her again as the world fades away. In this moment, there is only us and the clouds."

    "Hold her close.":
        "I put my arm around her and pull her close. She leans into me as we watch the clouds, secluded from the bustling of the park."

scene black with Dissolve(2.0)
"All too soon, the Ferris Wheel begins moving again and we're safely returned to the ground."

"Valerie and I continue to explore all the park has to offer. We alternate between riding more rides and checking out the merchandise. Valerie buys a keychain as a memento."

scene bg isokaze park dusk with fade

"After the sun sets and the park is winding down, we head towards the exit with the rest of the crowd."
"Valerie leans against me, a wide smile on her face."
show valerie hap at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL186.ogg"
vb "Amusement parks are even more fun than I imagined!"
"I chuckle."
pf "You're talking like you've never been to one before."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL187.ogg"
vb "I haven't!"
"I freeze, and she stumbles into me."
show valerie cur
pf "Seriously?!"
"She blinks."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL188.ogg"
vb "Well, yeah, it wasn't something we were able to afford when I was growing up."
pf "I know they're a little pricey, but a basic admissions ticket is still only around 50 credits."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL189.ogg"
vb "I know to most people that doesn't seem like much, but when you live paycheck to paycheck, every cent counts."
pf "I'm sorry, I didn't mean to be rude."
show valerie smi
"She smiles gently."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL190.ogg"
vb "It's okay, it's not something you think about until you're put in that situation."
"We continue to walk in silence."
pf "Well, now I feel like a jerk."
"Valerie squeezes my arm reassuringly, but a mischievous smile spreads across her lips."
show valerie mis
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL191.ogg"
vb "Does that mean you're going to make it up to me?"

menu:
    "Yes.":
        pf "It's the least I could do."
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL192.ogg"
        vb "Good!"

    "I don't have a choice do I?":
        pf "I like how you phrase it as if I had a choice."
        show valerie hap
        "Valerie grins."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL193.ogg"
        vb "You're a quick learner."


    "Depends.":
        pf "Depends on what it is."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL194.ogg"
        vb "I haven't decided yet."
        pf "Then I haven't decided yet either."

stop music fadeout 5
"The conversation lulls as we exit the park and make our way to the hotel."
pf "So, where are we staying?"
show valerie thi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL195.ogg"
vb "About that… remember when you said you would make things up to me?"
pf "Yeah…"
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL196.ogg"
vb "I want to stay in a love hotel!"
play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
"I miss a step and trip, but steady myself."
pf "I'm sorry, I thought you said you wanted to stay at a love hotel."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL197.ogg"
vb "That's right!"
pf "Didn't you already make a reservation at another hotel?"
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL198.ogg"
vb "About that… don't be mad!"
pf "...What did you do?"
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL199.ogg"
vb "Our reservation may or may not be at a love hotel… and by that I mean it is."
pf "Valerie!"
show valerie sad
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL200.ogg"
vb "Are you really turning down a chance to go to a {i}love hotel{/i} with {i}moi{/i}?"
"I feel the heat rise in my cheeks and I have to look away. Is she really suggesting…?! {w}Noticing my blush, Valerie speaks quickly."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL201.ogg"
vb "Don't worry, it's nothing like that!"
pf "Oh."
"I'm not sure if I should be disappointed or relieved."
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL202.ogg"
vb "I've just heard a lot about them and I'm really curious! But it'd be awkward to go alone…"
pf "Well, I suppose we don't have a choice since you already made the reservation… and if I'm honest, I'm kind of curious about them too…"
"Valerie smirks."
show valerie mis
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL203.ogg"
vb "Plus, anything could happen."

menu:
    "I'm not ready for that kind of thing!":
        "I blush."
        pf "I thought you said it wasn't like that!"
        show valerie hap
        "Valerie giggles."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL204.ogg"
        vb "I just like seeing you blush."

    "Like if I had a \"motherboard\"?":
        "I grin."
        pf "Oh yeah? Like when you have to add components to the sockets of your motherboard?"
        show valerie sur b2 with dissolve
        "Valerie's face turns bright red."
        
        if E4D2S3_Innocent == 1:
            show valerie dis b2
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL205.ogg"
            vb "I knew that was you!"
            pf "Tell me more about how the power supply supplies power."
            show valerie sur b3 with dissolve
            "Her cheeks grow even redder."
            show valerie ang b3 with dissolve
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL206.ogg"
            vb "Je vais prendre ma revanche!"
            show valerie smi b1 with dissolve
            "She tries to stay mad, but bursts out laughing."
        else:
            "I managed to catch her off-guard! Success."
            show valerie smi b2
            "Her confident smile returns a second later."
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL207.ogg"
            vb "Yes, exactly like that."
            pf "Maybe you can explain that to me again."
            show valerie mis b2
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL208.ogg"
            vb "You'll just have to wait."
            pf "That's probably for the best. I'm a visual learner anyway."
            show valerie hap b1 with dissolve
            "She bursts out laughing."

    "I don't think so.":
        pf "I don't know what you're talking about."
        show valerie mis
        "She smirks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL209.ogg"
        vb "That's fine. You'll find out later anyway."
        "I glance at her, and she giggles."


hide valerie with dissolve
"Valerie leads us to the hotel. It's easy to spot right away as it's the only gaudy building shaped like a castle."
scene bg campus building dusk with fade
"When we enter the lobby, the first thing I notice is the small lingerie shop."
"I guess that's one kind of gift shop…"
"Valerie stops in front of a poster advertising the different room options."
show valerie smi at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL210.ogg"
vb "I picked this hotel specifically because it has so many options. Which one would you want to see?"
"I read a few of the more \"interesting\" ones from the list."

menu:
    "Fifty Shades of Gear.":
        pf "Fifty Shades of how to be restrained."
        "Valerie grins mischievously."
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL211.ogg"
        vb "Sounds pretty adventurous!"
        "That's not the reaction I was expecting..."
        pf "Really? You'd be comfortable with something like that?"
        show valerie cur
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL212.ogg"
        vb "Of course I'd be comfortable."
        show valerie thi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL213.ogg"
        vb "And I wouldn't make your restraints {i}that{/i} tight so you'd be comfortable too."
        pf "Wait what?"
        show valerie mis
        "She flashes me a devilish smile. Uh oh."


    "Battleship room.":
        pf "I'm on a ship!"
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL214.ogg"
        vb "I bet you'd like to {i}submerge{/i} into dreamworld together."
        pf "Only if you'll call me \"Admiral\"."
        show valerie smi
        "Valerie smirks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL215.ogg"
        vb "Welcome back, Captain."
        pf "That's what I'm talking about!"
        "She smirks."

    "Ramen room!":
        pf "Whoa! They have a ramen room! We have to stay in there!"
        show valerie sur
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL216.ogg"
        vb "You want to sleep in a bed shaped like a bowl of ramen?"
        pf "It's like two of my favourite things in the same place."
        show valerie thi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL217.ogg"
        vb "I think that room would just make me hungry."

    "Naughty classroom.":
        pf "I hope you brought your ACE uniform because you're about to go to detention."
        show valerie mis
        "Valerie tries to keep a straight face."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL218.ogg"
        vb "If you like a girl in a school outfit, then classes at ACE must be torture for you."
        "I look Valerie up and down."
        pf "Only my International Bridging class. There's a real hottie in there and she makes it really hard to concentrate."
        "Valerie smiles."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL219.ogg"
        vb "Really? I have a feeling it's only going to get worse for you then."
        "I can feel the heat rise in my face as I imagine the possibilities."

show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL220.ogg"
vb "Maybe next time we can stay in there, but I've already picked a room."
stop music fadeout 6
pf "Why did you ask me which room I wanted if it didn't even matter?"
show valerie mis
"She smirks."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL221.ogg"
vb "To learn about your little secrets."
hide valerie with dissolve
scene black with fade
"Valerie goes to the reception to check-in and we're handed the keys to our room. When we arrive at the room, Valerie opens the door and I step into Paris."
scene bg vacation hotel night with fade
"The wallpaper is a backdrop of Paris, complete with the Eiffel Tower overlooking the wide bed. Our dining room table is reminiscent of an outdoor cafe, and Valerie takes a seat."
show valerie smi at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL222.ogg"
vb "Pretty cool, right? It looks even better than the pictures!"
pf "It definitely is cool, but…"

if MCStory == 3:
    "Out of all the potential themes, Valerie chose Paris. I think she's feeling a little homesick…"
    pf "Are you missing home at all?"
else:
    pf "Out of all the different themes out there, why did you choose Paris?"

show valerie cur
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
"She blinks."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL223.ogg"
vb "I just wanted to see what their version of Paris would be."
pf "Well, is it accurate?"
show valerie thi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL224.ogg"
vb "Yeah…"
"She looks back at the Eiffel Tower."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL225.ogg"
vb "My mom took me to see the Tower once. It was the only time she took me to the city."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL226.ogg"
vb "Well, her and Louie. He paid for our trip, but he thought it was going to be a romantic weekend in Paris for just the two of them."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL227.ogg"
vb "Mom wasn't able to find a sitter for me so she had no choice but to bring me along."
pf "That doesn't sound like it made for a very pleasant trip."
show valerie thi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL228.ogg"
vb "It was less than ideal, but I remember looking up at the Eiffel Tower and being in awe by how tall it was. It seemed to poke through the clouds and I wanted nothing more than to go up to the very top."
pf "Did you?"
"She shakes her head."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL229.ogg"
vb "They had other plans. It's on my to-do list, though."
pf "Then you will do it. We can go to Paris together and I'll take you up the Eiffel Tower."
show valerie cur
"Valerie looks at me with strange expression, as if she's trying to figure me out, before she smiles."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL230.ogg"
vb "It's a date."

voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL231.ogg"
vb "Let's see what else this room is hiding."
hide valerie with dissolve
"After exploring more of the room, we discovered a slot machine in the corner. It's a very random addition and very out of theme with the rest of the decor. The minibar was actually a vending machine for condoms and lube."
"Thank goodness Valerie wasn't standing beside me. My face was red enough without her teasing comments!"

"Soon we get ready for bed. I crawl into the bed on my side and Valerie crawls onto her side. We lie in silence, but I notice the gap between us is gradually getting smaller and smaller, until Valerie spoons my chest. I throw my arm around her and she places her arm over mine."
pf "Thanks for bringing me to Paris."
show valerie hap b2 at cc with dissolve
"She flips over on her other side and faces me."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL232.ogg"
vb "I'm glad I got to go with you."
show valerie smi b2
"I brush her hair out of her eyes and kiss her gently. Her sweet taste lingers in my mouth and all I can think about is how wonderful and mysterious Valerie is. She's sweet but sharp, confident yet vulnerable, and I'm the only person who gets to see all the different sides of her."
"When I'm with her, nothing else exists. There is only us and the moments we create, like a picture or stillness in time."

$ qtetotal = 5
$ t_var = qtetotal
show screen timer_scr(place="E4VBS4_nolove")

menu:
    "I love you.":
        $ renpy.hide_screen ("timer_scr")
        $ E4VBS4_Loving = 1
        pf "Je t'aime."
        show valerie hap b3 with dissolve
        "Valerie glances sharply at me and her cheeks flush, but she doesn't look away. She breaks into a smile which warms my soul and kisses me deeply."
        show valerie smi b3 with dissolve
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL233.ogg"
        vb "Je t'aime."
        scene black with fade
        jump E4VBS4_conv

label E4VBS4_nolove:
    $ renpy.hide_screen ("timer_scr")
    scene black with fade
    "With Valerie wrapped in my arms, listening to the gentle ebb and flow of her breathing, I fall asleep in the city of love."
    jump E4VBS4_conv

    
label E4VBS4_conv:
stop music fadeout 3
$renpy.pause(2.0)
play ambient "audio/ambience/Morning.ogg" fadein 2
$renpy.pause(1.0)
"A gentle stir wakes me. I blink open my eyes and see Valerie slipping out of bed."
scene bg vacation hotel day with fade
pf "Where are you going?"
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
show valerie smi at cc with dissolve
"My voice is thick with sleep. Valerie grins and crawls back over to kiss my cheek."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL234.ogg"
vb "It's time to wake up. We've got a train to catch, remember?"
pf "Mmm…"
"I'm not ready to leave the warm bed, but I reluctantly do so anyway."
stop ambient fadeout 3
scene black with fade
"We both get ready in silence, but there's no awkwardness to it. After we check out, we pick up a quick breakfast and wait for the train. {w}Soon, it arrives and we get on."
"Valerie leans her head on my shoulder. We spend the entire ride enjoying the comfort of each other's company."
"Once we get to my bike, I drop her off at ACE."
scene bg campus main day with fade
$renpy.pause(.5)
show valerie smi b1 at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL235.ogg"
vb "I couldn't have asked for a better way to end the week."
pf "Me neither."
if E4VBS4_Loving == 1:
    show valerie hap b2 with dissolve
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL236.ogg"
    vb "I'll see you soon, mon amour."
else:
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL237.ogg"
    vb "I'll see you soon."
    
scene black with fade
"She kisses me one last time before heading back towards her dorm. After I watch her go, I drive back home."



stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4VBS4_Completed = 1
jump E4D7S1