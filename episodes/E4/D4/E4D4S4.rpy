#
label E4D4S4:
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 5
    scene bg homekaito main night with fade
    "Uncle Kaito and Nikki are both sitting on the couch watching TV when I arrive."
    pf "Hi Uncle Kaito, hey Nikki."
    
    show kaito smi at l2 with dissolve
    "Kaito grins at me."
    voice "audio/voice/E4/Kaito/d04/(20).ogg"
    hk "Welcome back. How was your match?"
    pf "Actually, it--"
    show nikki hap at r2 with dissolve:
        xzoom -1
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_401.ogg"
    sf "Finally, you're home! I thought you were going to miss it!"
    pf "Miss what?"
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    show nikki ske
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_402.ogg"
    sf "The Moscars, of course! Did you forget?"
    "In all of the excitement of today, I completely forgot about the Moscars! My expression must have given away my thoughts because Nikki shakes her head."
    
    menu:
        "I forgot!":
            pf "Whoops."
            show question:
                xoffset 1040
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_403.ogg"
            sf "Seriously? How could you forget when your favourite actor, Ceonardo DiLaprio, was nominated?"
            show kaito neu
            voice "audio/voice/E4/Kaito/d04/(21).ogg"
            hk "To be fair, he's been nominated five times before."
            show nikki wor
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_404.ogg"
            sf "That's not the point, Uncle!"
        
        "Play it cool. How could I forget?":
            pf "There's no chance I'd ever forget this moment when Ceonardo DiLaprio will finally win that Moscar he so rightly deserves."
            show nikki mis
            "Nikki laughs."
            show note:
                xoffset 1040
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_405.ogg"
            sf "You've said that every time he's been nominated and each time you've been wrong."
            pf "I've got a good feeling about this one."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_406.ogg"
            sf "You say that every year too."
        
        "I don't usually watch this.":
            "I'm not sure why Nikki is making such a big fuss. She's the one who watches these types of shows, not me."
            pf "Does it count as forgetting if I never planned to watch it in the first place?"
            show nikki thi
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_407.ogg"
            sf "Really? But Ceonardo DiLaprio was nominated this year."
            "He was? Will this year be the year he finally wins?"
            show nikki mis
            "Nikki speaks in a sing-song voice."
            show note:
                xoffset 1040
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_408.ogg"
            sf "You know you want to watch with us…"
            show kaito hap
            voice "audio/voice/E4/Kaito/d04/(22).ogg"
            hk "Yeah! I have a good feeling about this year."
            pf "Alright, but I don't know if I can take watching my boy Ceo lose again."
            show nikki smi
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_409.ogg"
            sf "We'll be here to make you feel better and not laugh in your face."
            pf "...Thanks…"
            
    hide kaito
    hide nikki
    with dissolve
    "I snuggle in between them on the couch just as the opening number starts."
    "I only partially pay attention to most of the nominations. Every so often I peek at Uncle Kaito and Nikki. Kaito looks about as engaged as I am, while Nikki is practically on the edge of her seat. Every so often she'd shout out who she hopes to win."
    show kaito ner at r2:
        xzoom -1
    show nikki ner at l2
    with dissolve
    "Finally, it's the moment we've all been waiting for--the nominations for best actor. Ceonardo DiLaprio is nominated for his role in {i}The Apparition{/i} against a handful of people no one cares about."
    stop music fadeout 3
    "Uncle Kaito and I look over at each other in solidarity. Nikki leans so far forward in her seat I'm afraid she's going to fall off."
    
    voice "audio/voice/E4/Announcer/D4/16.ogg"
    an "And the Moscar goes to…"
    "I hold my breath as the announcer rips open the envelope in the slowest way possible."
    voice "audio/voice/E4/Announcer/D4/17.ogg"
    an "...Ceonardo DiLaprio!"
    play music "audio/music/Victory! (GAME VERSION).ogg" fadein 3
    show kaito hap
    show nikki sur
    with dissolve
    # jumping?
    "Nikki jumps up and screams while Kaito throws a fist in the air and shouts excitedly."
    
    menu:
        "Jump up with Nikki.":
            show nikki hap
            "I leap off of the couch and jump up and down with Nikki. She throws her arms around me in a hug."
            pf "He finally did it!"
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_410.ogg"
            sf "I know!"
            show drop:
                xoffset 1040
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaito/d04/(1).ogg"
            hk "I'm feeling a little left out here…"
            show nikki smi
            "Nikki and I glance at each other and laugh. Then we each give Kaito a high five."
        
        "That'll do, Ceonardo, that'll do.":
            "I can't hold back my grin and a wave of pride washes over me. This was a long time coming--it's about time he was formally recognised for his talents!"
            show exclamation:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki hap
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_411.ogg"
            sf "He won!"
            voice "audio/voice/E4/Kaito/d04/(2).ogg"
            hk "I can hardly believe it!"
        
        "Is this real life?":
            "I sit quietly, still in shock. Have my eyes and ears deceived me or did they just announce Ceonardo DiLaprio as the winner?"
            show nikki hap
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_412.ogg"
            sf "Did you hear that, big bro? Ceonardo won!"
            voice "audio/voice/E4/Kaito/d04/(3).ogg"
            hk "He won!"
            show nikki ske
            "Nikki pauses and gives me a weird look."
            show drop:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_413.ogg"
            sf "I thought you'd be more excited about this."
            "I surreptitiously pinch myself and flinch. This isn't a dream!"
            pf "He finally won!"
        
        "So what?":
            pf "Calm down, it's only an actor receiving an award. Not like this doesn't happen all the time."
            
            if E1D4S6_Ceonardo == 1:
                show drop:
                    xoffset 365
                    yoffset 160
                    xzoom .75
                    yzoom .75
                show nikki ske
                voice "audio/voice/E4/Nikki/Day 4/Nikki_04_414.ogg"
                sf "Aren't you the one who's always going on about how he should have won a Moscar? How come you aren't more excited?"
                pf "He doesn't need some fancy trophy to be a winner in my eyes."
                
            else:
                show nikki smi
                voice "audio/voice/E4/Nikki/Day 4/Nikki_04_415.ogg"
                sf "Well, this {i}doesn't{/i} happen all the time for {i}Ceonardo DiLaprio{/i}."
                show kaito smi
                voice "audio/voice/E4/Kaito/d04/(4).ogg"
                hk "She's got a point. Let the man have his moment!"
                "I laugh."
                pf "Alright, alright."
    
    pf "Honestly, Nikki, I'm surprised you're so excited by this. I didn't realise you liked him."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_416.ogg"
    sf "This is a momentous event. What's not to like about it?"
    show kaito cur
    show nikki cur
    "Before I can answer, she shushes me."
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_417.ogg"
    sf "He's about to give his speech!"
    show nikki neu
    show kaito smi
    "We watch as Ceonardo graciously accepts his Moscar and runs through his list of thanks."
    "Ceonardo DiLaprio" "...And finally, I'd like to mention how thankful I am that we took care of global warming back in 2016 so everyone can still enjoy the wonders of snow."
    "The audience roars with applause as Ceo walks off the stage."
    stop music fadeout 3
    voice "audio/voice/E4/Kaito/d04/(5).ogg"
    hk "What a classy guy."
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_418.ogg"
    sf "Yeah…"
    show nikki smi
    "Nikki gets back on her feet."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    show bulb:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_419.ogg"
    sf "Anybody want a snack?"
    show kaito cur
    "Kaito perks up."
    voice "audio/voice/E4/Kaito/d04/(6).ogg"
    hk "I wouldn't say no that."
    show kaito smi
    pf "Same here."
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_420.ogg"
    sf "Be right back!"
    hide nikki with dissolve
    "She runs off into the kitchen and returns with a plate of strawberries."
    show nikki hap at l2
    show kaito cur
    with dissolve
    voice "audio/voice/E4/Kaito/d04/(7).ogg"
    hk "Ooh, strawberries!"
    show kaito hap
    "Uncle Kaito's face lights up as he grabs the closest one to him. Without hesitation, he takes a huge bite, then catches himself as chocolate dribbles down his chin."
    pf "Wait, is that chocolate?"
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_421.ogg"
    sf "Yeah!"
    "I pick up a strawberry and pop it in my mouth."
    pf "Mmm, cream-filled."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_422.ogg"
    sf "I also have some filled with gelatin and cookie butter."
    show kaito sur
    voice "audio/voice/E4/Kaito/d04/(8).ogg"
    hk "This is… amazing!"
    show nikki hap b1
    "She beams."
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_423.ogg"
    sf "Do you really think so?"
    show kaito hap
    voice "audio/voice/E4/Kaito/d04/(9).ogg"
    hk "Yes!"
    "I eat another strawberry in response."
    show kaito smi
    voice "audio/voice/E4/Kaito/d04/(10).ogg"
    hk "Where did you find this idea?"
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_424.ogg"
    sf "I don't know… I was just thinking about how I wanted chocolate-covered strawberries, but I hate when the chocolate comes off unevenly or the shell breaks off when you bite into it. I figured this was a better, yet still delicious, alternative."
    pf "I can confirm it is."
    "Uncle Kaito eats another strawberry."
    show kaito mis
    voice "audio/voice/E4/Kaito/d04/(11).ogg"
    hk "Do you think you can make this at the cafe?"
    show shiny:
        xoffset 365
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki cur
    "Nikki's eyes glitter."
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_425.ogg"
    sf "Seriously? You think it's that good?"
    show kaito smi
    voice "audio/voice/E4/Kaito/d04/(12).ogg"
    hk "Definitely. It's a simple twist on a familiar treat. I have no doubts it'll be well-received."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_426.ogg"
    sf "I'd be honored!"
    voice "audio/voice/E4/Kaito/d04/(13).ogg"
    hk "Great! What do you want to call them?"
    
    menu:
        "Cupberries.":
            pf "You should call them \"Cupberries\"."
            show nikki thi
            "Nikki wrinkles her nose."
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_427.ogg"
            sf "I don't know…"
            pf "Why not? It rolls off the tongue!"
            show kaito cur
            voice "audio/voice/E4/Kaito/d04/(14).ogg"
            hk "\"Cupberries\"... hmm…"
            pf "Uncle Kaito doesn't hate it."
            show drop:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki ner
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_428.ogg"
            sf "It sounds kind of… inappropriate?"
            pf "I don't know what you're talking about."
        
        "Strawberry Dream.":
            pf "What about \"Strawberry Dream\"?"
            show nikki thi
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_429.ogg"
            sf "...That's not terrible."
            show kaito cur
            "Uncle Kaito looks thoughtful."
            voice "audio/voice/E4/Kaito/d04/(15).ogg"
            hk "It's vague enough that it can encompass all the different filling options."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_430.ogg"
            sf "Hmm…"
        
        "Fruitsuckles.":
            pf "Call them \"Fruitsuckles\"."
            show panic:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki wor
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_431.ogg"
            sf "No!"
            pf "Why not?"
            show nikki dis
            voice "audio/voice/E4/Nikki/Day 4/Nikki_04_432.ogg"
            sf "Because I {i}want{/i} people to eat them!"
            show kaito ner
            voice "audio/voice/E4/Kaito/d04/(16).ogg"
            hk "I'm not sure having the word \"suck\" in the title is the strongest marketing strategy."
            pf "You're sucking out the inside of the fruit. Not that the fruit sucks."
            
    show kaito mis
    voice "audio/voice/E4/Kaito/d04/(17).ogg"
    hk "We'll think about it."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_433.ogg"
    sf "Right."
    pf "Well, since nobody here seems to appreciate my genius, I'm going to bed."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_434.ogg"
    sf "It is getting late."
    show kaito smi
    "Uncle Kaito stifles a yawn."
    voice "audio/voice/E4/Kaito/d04/(18).ogg"
    hk "Yeah, I think I'm going to turn in too."
    "He starts to get up, then pops the last strawberry into his mouth."
    show nikki mis
    voice "audio/voice/E4/Nikki/Day 4/Nikki_04_435.ogg"
    sf "I thought you were going to bed?"
    show kaito mis
    voice "audio/voice/E4/Kaito/d04/(19).ogg"
    hk "I couldn't leave the poor thing to live on that plate all alone. Better that he's with his friends."
    pf "Yup, definitely time for me to go to bed."
    show nikki smi
    "Nikki giggles."
    scene black with fade
    "After I help her clean up the kitchen a bit, I head upstairs and dream of dessert."
    
    stop music fadeout 3
    stop ambient fadeout 3
    $renpy.pause(2.5)
    
    jump E4D5S1
