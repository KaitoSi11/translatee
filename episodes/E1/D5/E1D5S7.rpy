label E1D5S7:

$ nikOut = "sCasual"

play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
$renpy.pause(1.5)

scene bg homekaito main night with fade

"As I walk into the room, I'm assaulted by the sound of laughter. Seated in the living room is Nikki and two other girls. They glance up at me as I enter."

show nikki hap at cc
show highschoolgirl extra at l3
show highschoolgirl2 extra at r3
with dissolve

"Nikki greets me with a wide grin and waves me over, while the two girls begin whispering to each other." 
show nikki smi
voice "audio/voice/E1/D5/S7/Nikki/1.ogg"
sf "Hey, you're back! Where did you go?"

if (E1D5S1_EventAlone == 1):
    pf "I just went to the arcade to practice on the simulation stations."
    "Nikki's friends both perk up."
    voice "audio/voice/E1/D5/S7/HSS1/1.ogg"
    hstu1f "You mean GEAR simulations?"
    pf "Yeah."
    voice "audio/voice/E1/D5/S7/HSS2/1.ogg"
    hstu3f "Were there a lot of other pilots there?"
    pf "Um, not that I know of."
    show nikki ske
    voice "audio/voice/E1/D5/S7/HSS1/2.ogg"
    hstu1f "Ooh, the only pilot there…"
    "Nikki gives them a weird look, then shrugs."

elif (E1D5S1_EventKaori == 1):
    pf "I went to the store to check out tablets."
    voice "audio/voice/E1/D5/S7/Nikki/2.ogg"
    sf "Oh, really? Did you see anything good?"
    pf "Yeah."
    show nikki cur
    "She looks at my empty hands."
    voice "audio/voice/E1/D5/S7/Nikki/3.ogg"
    sf "But nothing good enough to buy?"
    pf "Oh, Kaori was the one who wanted a new tablet. I was just there to show her which one was good."
    show nikki dis
    voice "audio/voice/E1/D5/S7/Nikki/4.ogg"
    sf "That's kind of a lame date. I'm disappointed in you."
    "Nikki's friends seem to be on alert."
    pf "It wasn't a date!"
    show nikki mis
    voice "audio/voice/E1/D5/S7/Nikki/5.ogg"
    sf "Suuure, whatever you say."
    "Nikki's friend leans into her and whispers."
    voice "audio/voice/E1/D5/S7/HSS2/2.ogg"
    hstu3f "Does he have a girlfriend?"
    show nikki smi
    voice "audio/voice/E1/D5/S7/Nikki/6.ogg"
    sf "Nah--he wishes."
    "The two girls glance at each other and giggle."

elif (E1D5S1_EventShou == 1) or (E1D5S1_EventMayu == 1):
    pf "I hung out with friends."
    show nikki mis
    show question:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D5/S7/Nikki/7.ogg"
    sf "Oh yeah? You have friends?"
    pf "Very funny."
    "Nikki grins."
    show nikki neu
    voice "audio/voice/E1/D5/S7/Nikki/8.ogg"
    sf "Who?"
    pf "Just Shou and Mayu from my team."
    "Nikki's friends lean into her and whisper."
    voice "audio/voice/E1/D5/S7/HSS1/3.ogg"
    hstu1f "What team is he talking about?"
    voice "audio/voice/E1/D5/S7/Nikki/9.ogg"
    sf "His pilot team."
    voice "audio/voice/E1/D5/S7/HSS2/3.ogg"
    hstu3f "Oooh."
    "They both glance appreciatively at me again."

elif (E1D5S1_EventYuuna == 1):
    pf "I met up with Yuuna to work on our project."
    show nikki ske
    voice "audio/voice/E1/D5/S7/Nikki/10.ogg"
    sf "Seriously? You did homework on a Saturday?"
    pf "Yeah…"
    voice "audio/voice/E1/D5/S7/Nikki/11.ogg"
    sf "Riiiiight, I'm sure it had nothing to do with seeing a cute girl."
    "Nikki's friends suddenly seem to be on alert."
    pf "We really did do homework. In fact, we finished the project."
    show nikki cur
    voice "audio/voice/E1/D5/S7/Nikki/12.ogg"
    sf "You're telling me that you were alone with a cute girl for hours, and all you did was schoolwork?"
    pf "Um, yeah."
    "She sighs."
    show drop:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki dis
    voice "audio/voice/E1/D5/S7/Nikki/13.ogg"
    sf "You're so hopeless!"
    "Nikki's friends glance at each other and giggle."

pf "What are you guys doing?" 
show nikki neu
voice "audio/voice/E1/D5/S7/Nikki/14.ogg"
sf "Playing Draw-it."
pf "What's that?" 
"The first girl speaks before Nikki can." 
voice "audio/voice/E1/D5/S7/HSS1/4.ogg"
hstu1f "It's a fun game! You pick a word from the pile and draw it and people guess what it is." 
pf "Sounds easy enough."
show note:
    xoffset 1175
    yoffset 160
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S7/HSS2/4.ogg"
hstu3f "Join us! Then we can play in teams of two."
voice "audio/voice/E1/D5/S7/HSS1/5.ogg"
hstu1f "Yeah! Join us!"
pf "Uh…"
"I glance at Nikki, who shrugs."
voice "audio/voice/E1/D5/S7/Nikki/15.ogg"
sf "Sure, why not?"
pf "Okay."
"The two girls jump up excitedly."
show nikki cur
"The first one gets up from the couch and grabs my arm, then drags me back to sit with her."
voice "audio/voice/E1/D5/S7/HSS1/6.ogg"
hstu1f "Yay! You can be on my team." 
voice "audio/voice/E1/D5/S7/HSS2/5.ogg"
hstu3f "No! He should be on my team."
"The other girl grabs my other arm."
pf "Um."
voice "audio/voice/E1/D5/S7/HSS1/7.ogg"
hstu1f "Why? You and Nikki are like best friends. You two should be on a team!"
show nikki sur
"She tugs tighter on my arm."
voice "audio/voice/E1/D5/S7/HSS2/6.ogg"
hstu3f "But he's a pilot at ACE which means he's smarter and should be on my team!"
"I feel like I'm going to be ripped in half."
show crying:
    xoffset 720
    yoffset 160
    xzoom .75
    yzoom .75
show nikki dis with dissolve
voice "audio/voice/E1/D5/S7/Nikki/16.ogg"
sf "Ouch! I thought you guys were my friends not his?"

#hstu1f and hstu3f speaking simultaneously
voice "audio/voice/E1/D5/S7/HSS1/8.ogg"
hstu1f "We are!"
voice "audio/voice/E1/D5/S7/HSS2/7.ogg"
hstu3f "We are!"
show nikki ske
voice "audio/voice/E1/D5/S7/Nikki/17.ogg"
sf "Then how come you guys don't want to be on my team?"
"They glance at each other, but neither girl lets go of me. Nikki crosses her arms."
show nikki smi
voice "audio/voice/E1/D5/S7/Nikki/18.ogg"
sf "Fine. Well, he's my brother so he's going to be on my team."
"Both girls pout in disappointment and let go." 
voice "audio/voice/E1/D5/S7/HSS2/8.ogg"
hstu3f "You're no fun, Nikki."
show nikki neu
voice "audio/voice/E1/D5/S7/Nikki/19.ogg"
sf "Whatever. You guys can go first!" 
voice "audio/voice/E1/D5/S7/HSS1/9.ogg"
hstu1f "Fine." 

hide nikki
hide highschoolgirl extra
hide highschoolgirl2 extra2
with dissolve

show highschoolgirl extra at r1:
    xzoom -1
show highschoolgirl2 extra at r3:
    xoffset 75
    xzoom -1
show nikki neu at l3
with dissolve
$renpy.pause(.5)

"Nikki's friend picks up a card and smiles when she sees the word."
"She glances at me quickly then starts drawing. It's a guy with blond hair… wearing something eerily familiar."
"The second girl answers immediately." 
voice "audio/voice/E1/D5/S7/HSS2/9.ogg"
hstu3f "Hot! The word is hot!" 
show nikki cur
voice "audio/voice/E1/D5/S7/HSS1/10.ogg"
hstu1f "Yes!" 
"They both burst into a fit of giggles. Nikki grabs the paper and looks at it."
show question:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki ske
voice "audio/voice/E1/D5/S7/Nikki/20.ogg"
sf "What? How did you guess \"hot\" from that?"
"She shoves the drawing in my face."
show nikki cur
voice "audio/voice/E1/D5/S7/Nikki/21.ogg"
sf "Would you have known this was \"hot\"?"

menu:
    "No, but it's probably a girl thing.":
        pf "No, but I think you girls would know better than I would if a guy is hot or not."
        show nikki dis
        "Nikki blinks at me."
        voice "audio/voice/E1/D5/S7/Nikki/22.ogg"
        sf "Okay, never mind."

    "How else would you describe me?":
        pf "It's pretty obvious to me."
        "I grin at the girls, who both blush."
        show nikki dis
        voice "audio/voice/E1/D5/S7/Nikki/23.ogg"
        sf "What? Shut up. You're no help."

    "Probably not.":
        pf "I don't think \"hot\" is the word I would have gone for."
        show nikki neu
        voice "audio/voice/E1/D5/S7/Nikki/24.ogg"
        sf "Thank you!"

show confused:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki cur
voice "audio/voice/E1/D5/S7/Nikki/25.ogg"
sf "Why wouldn't you draw fire or like, a cup of coffee or something? Who is this even supposed to be?" 

show heart:
    xoffset 875
    yoffset 160
    xzoom .75
    yzoom .75
    
show heart2:
    xoffset 330
    yoffset 160
    xzoom -.75
    yzoom .75

"Both girls look at me and giggle again."
$renpy.pause(.75)
show shocked:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki sur b1 with dissolve
$renpy.pause(1.0)

"Nikki glances between the three of us then frowns." 

show nikki ann b1
voice "audio/voice/E1/D5/S7/Nikki/26.ogg"
sf "You guys, he's my brother!"
voice "audio/voice/E1/D5/S7/HSS2/10.ogg"
hstu3f "So?"
voice "audio/voice/E1/D5/S7/HSS1/11.ogg"
hstu1f "He's cute…"

show nikki ang b1
voice "audio/voice/E1/D5/S7/Nikki/27.ogg"
sf "But he's {i}my brother{/i}!" 
show nikki ann b1
"The girls exchange a glance then gasp."
voice "audio/voice/E1/D5/S7/HSS1/12.ogg"
hstu1f "Ohhh, we had no idea."
voice "audio/voice/E1/D5/S7/HSS2/11.ogg"
hstu3f "Yeah, we're sorry! But you should have said something."
show nikki cur with dissolve
"Nikki blinks in confusion."
voice "audio/voice/E1/D5/S7/Nikki/28.ogg"
sf "Huh? Said what?"
voice "audio/voice/E1/D5/S7/HSS1/13.ogg"
hstu1f "That you and him--you know."
"She nudges her head towards me."
voice "audio/voice/E1/D5/S7/HSS1/14.ogg"
hstu1f "The relationship you have with him…"
"Nikki continues to look blank for a few seconds..."
show frightful:
    xoffset 230
    yoffset 160
    xzoom .75
    yzoom .75
show nikki sur with dissolve
$renpy.pause(.5)
"...then her expression changes to horror."
voice "audio/voice/E1/D5/S7/Nikki/29.ogg"
sf "Oh my god, no!"
voice "audio/voice/E1/D5/S7/HSS2/12.ogg"
hstu3f "It makes sense as to why you got so protective over him." 
voice "audio/voice/E1/D5/S7/HSS1/15.ogg"
hstu1f "And why you wanted him on your team." 
voice "audio/voice/E1/D5/S7/HSS2/13.ogg"
hstu3f "Nikki, you don't have to be embarrassed. It's okay!"
show nikki win
voice "audio/voice/E1/D5/S7/Nikki/30.ogg"
sf "Gross, gross, gross!" 
"Things just got really weird."
pf "I'm going to head upstairs." 
voice "audio/voice/E1/D5/S7/HSS1/16.ogg"
hstu1f "Oh no! Stay and play with us." 
voice "audio/voice/E1/D5/S7/HSS2/14.ogg"
hstu3f "Yeah, stay!" 
show nikki ann
"Nikki stands and pushes me towards the stairs." 
voice "audio/voice/E1/D5/S7/Nikki/31.ogg"
sf "Don't listen to them. Just go!" 
pf "I'm going, I'm going!" 


stop ambient fadeout 3.0
scene black with fade
$renpy.pause(.5)


"I rush up the stairs but can still hear them arguing below." 
voice "audio/voice/E1/D5/S7/HSS2/15.ogg"
hstu3f "Why did you send him away, Nikki? We were having a good time."
voice "audio/voice/E1/D5/S7/HSS1/17.ogg"
hstu1f "Yeah, plus he's hot."
voice "audio/voice/E1/D5/S7/Nikki/32.ogg"
sf "Ew, you guys, stop it." 
voice "audio/voice/E1/D5/S7/HSS2/16.ogg"
hstu3f "It's not a crime to look." 
voice "audio/voice/E1/D5/S7/Nikki/33.ogg"
sf "Well, it should be! Excuse me, I'm just going to go throw up." 
"Their voices drift away as I enter my room and flop onto my bed."


$renpy.pause(.5)
stop music fadeout 20
scene bg homekaito myroom night with fade

"I will never understand girls. But it is kind of funny that they thought I was hot. Actually, they weren't so bad to look at…"
"I grin as I remember them clutching my arm close to their chests. With assets like that you kind of forget things... {w}like that they're only in high school."
"The smile drops off my face. Maybe it's a good thing Nikki doesn't bring her friends home very often."

play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
"Just then, my phone dings, announcing an email. Breathing in relief, I eagerly reach over and open the email."
"All team rankings will be posted on Monday." 
"I guess I'll find out my ranking when I go to school."

scene black with fade

"I spend the rest of my evening browsing online for cat videos until it's time for bed."
"As soon as my head hits the pillow, I fall asleep. Who knows what tomorrow will hold."

#jump E1END

jump E2D1S1