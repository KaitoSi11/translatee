#
label E3SSS1:
$ shoOut = "sGym"

scene black with fade

"I feel productive today, but I don't want to hit the books and study just yet. {w}I know a good way to channel this energy! I'll work out at the gym."

if (MCStory == 1):
    "Besides, I have to maintain this sweet bod!"

else:
    "Other than my Physical Education class, I haven't been getting any exercise. I need to get back into a solid routine."

"I head to the rec center and get changed in the lockers. As I make my way to the weight room, I pass by the gymnasium. Normally, it's empty, but today it's full of people. Is there a class going on right now?" 

scene bg campus gym day with dissolve

"Unable to curb my curiosity, I peek into the room. The gym is decked out with equipment: balance beams, still rings, parallel bars, uneven bars, pommel horse, etc. I can't see the floor beneath the layer of blue mats. Students seem to fly and flip from all corners of the room."
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"My mouth drops open in wonder as I spot a very familiar face hanging on the still rings."

pf "Shou!"

"At the sound of his name, Shou turns towards the sound of my voice and loses his grip. I wince as he comes crashing onto the mat below. After a second, he gets up and rubs his head, then looks at me."

show shou cur at cc with dissolve

menu:
    "My bad!":
        "I feel a little guilty."
        pf "Sorry about that, man."
        show shou smi
        "Shou's signature smile graces his face."
        voice "audio/voice/E3/Free/SS/S1/shou/1.ogg"
        ss "Don't sweat it, broseph!"

    "Such grace, much elegant.":
        "I clap slowly."
        pf "I'll give that fall a solid 5 out of 7."
        show shou ske
        "Shou frowns."
        voice "audio/voice/E3/Free/SS/S1/shou/2.ogg"
        ss "Not funny, man! I was going for a personal record."

    "Whoops.":
        "Shou's attention is not the only one I attracted. A few heads turn in my direction and give me disapproving looks. {w}I guess I was a bit loud..."
        show shou smi
        "Thankfully, Shou is still his cheery self."
        voice "audio/voice/E3/Free/SS/S1/shou/3.ogg"
        ss "What's going on, broseph?"
        pf "Nothing much."

pf "What are you doing here?"
"Shou wipes the sweat off his face with his towel."
show drop:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
show shou hap
voice "audio/voice/E3/Free/SS/S1/shou/4.ogg"
ss "Trying to balance on the still rings."
pf "No, I mean, I didn't exactly picture you as a gymnastics type of guy."

show shou smi
voice "audio/voice/E3/Free/SS/S1/shou/5.ogg"
ss "Why not? It helps with staying fit, builds strength, flexibility, core training..."
show shou hap
"A pair of girls walk by us wearing the ACE Academy gym wear. Their stomachs are completely flat and they have perky features. They flash us smiles as they walk by."
show shou cur
voice "audio/voice/E3/Free/SS/S1/shou/6.ogg"
ss "...um, flexibility--"
pf "You already said that one."
voice "audio/voice/E3/Free/SS/S1/shou/7.ogg"
ss "Did I?"
"His attention is on another group of girls practicing their splits in the corner."
pf "Mmhm, and {i}that{/i} has nothing to do with it?"
show shou hap
"He grins."
show drooling:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/SS/S1/shou/8.ogg"
ss "It's a bonus."
pf "I'm pretty sure that's the main course for you."
show shou smi
voice "audio/voice/E3/Free/SS/S1/shou/9.ogg"
ss "I will neither confirm nor deny that."
"We both grin."
voice "audio/voice/E3/Free/SS/S1/shou/10.ogg"
ss "Plus, you're competing with yourself to always be better."
pf "Huh?"
voice "audio/voice/E3/Free/SS/S1/shou/11.ogg"
ss "You set personal records for yourself, and then the next time you come, you try to beat them!"
"I'm not entirely sure where he's going with this..."
pf "Like how long you can hold yourself up? I guess."
voice "audio/voice/E3/Free/SS/S1/shou/12.ogg"
ss "That's just step one. Once you're comfortable just holding your weight, then you start doing tricks like handstands. It's a lot harder than you think!"
"He motions towards the still bars."
voice "audio/voice/E3/Free/SS/S1/shou/13.ogg"
ss "Try it!"

menu:
    "Sure!":
        "I psych myself up."
        pf "Alright! Let's do it!"
        show shou hap
        voice "audio/voice/E3/Free/SS/S1/shou/14.ogg"
        ss "That's the spirit!"
        jump E3SSS1_BalanceJump

    "I'll pass.":
        pf "Eh, no thanks."
        show shou mis
        "He smirks."
        voice "audio/voice/E3/Free/SS/S1/shou/15.ogg"
        ss "Heh, scared?"

        menu:
            "Challenge accepted!":
                pf "Pfft, as if I could be scared of something so easy."
                pf "I'm going to wipe that grin off your face."
                show shou hap
                "Shou laughs."
                voice "audio/voice/E3/Free/SS/S1/shou/16.ogg"
                ss "You're underestimating it!"
                jump E3SSS1_BalanceJump

            "Still no.":
                pf "Good try, but still no."
                show shou neu
                "Shou frowns."
                voice "audio/voice/E3/Free/SS/S1/shou/17.ogg"
                ss "Alright, alright."
                jump E3SSS1_Covergence

                
    "Still rings is too easy.":
        pf "Pfft, anyone can do the still rings. All you have to do is hang."
        show shou ske
        voice "audio/voice/E3/Free/SS/S1/shou/18.ogg"
        ss "It actually involves a lot more technique than you think…"
        pf "How about we try something that's {i}actually{/i} challenging?"
        "I scan the room and point to the vault."
        pf "Like that!"
        show shou cur
        "Shou's eyes widen."
        voice "audio/voice/E3/Free/SS/S1/shou/19.ogg"
        ss "Do you even know what you're supposed to do on the vault?"
        pf "Umm…"
        show shou smi
        voice "audio/voice/E3/Free/SS/S1/shou/20.ogg"
        ss "You flip off it!"
        pf "You mean like flip onto it?"
        voice "audio/voice/E3/Free/SS/S1/shou/21.ogg"
        ss "No, no, you take a running start and flip {i}over{/i} it."
        pf "Oh…"
        show shou hap
        voice "audio/voice/E3/Free/SS/S1/shou/22.ogg"
        ss "Still want to try that?"

        menu:
            "I can't back down now!":
                pf "Yup!"
                "Shou shrugs."
                show shou smi
                voice "audio/voice/E3/Free/SS/S1/shou/23.ogg"
                ss "It's your funeral."
                "He leads me to the vault."
                jump E3SSS1_VaultJump

            "Let's revisit the still rings.":
                pf "Uhh, so, still rings, you said?"
                "Shou laughs."
                show shou smi
                voice "audio/voice/E3/Free/SS/S1/shou/24.ogg"
                ss "Hah, follow me."
                jump E3SSS1_BalanceJump

                
label E3SSS1_VaultJump:
    "Shou gestures to the vault."
    show shou smi
    voice "audio/voice/E3/Free/SS/S1/shou/25.ogg"
    ss "After you."
    pf "A running start, then flip?"
    voice "audio/voice/E3/Free/SS/S1/shou/26.ogg"
    ss "Yup."
    "I nod, gathering my resolve."
    hide shou with dissolve
    "Channeling my inner Usain Volt, I race towards the vault."


    $ qtebase = 3
    $ qtetotal = qteintel + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3SSS1_shortbus")

    menu:
        "Run...":
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_Overshoot

        "Trip...":
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_shortbus

        "Fall...":
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_shortbus

        "{color=#00ff00}{b}Jump!{/b}{/color}" if (MCStory == 1):
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_success
            
        "Jump!" if (MCStory != 1):
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_success

        "Pause...":
            $ renpy.hide_screen ("timer_scr")
            jump E3SSS1_Overshoot



label E3SSS1_Overshoot:
    "My legs keep pumping and the vault looms ever closer in front of me. Should I jump now? Before I know it, the vault is right in front of me! My hesitation costs me dearly and I crash face first into the springboard."
    show shou hap at cc with dissolve
    "Shou bursts out laughing."
    pf "Urgh…"
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/SS/S1/shou/27.ogg"
    ss "Hahaha!"
    pf "Thanks for your concern."
    "I rub my head as Shou catches his breath."
    show shou smi
    voice "audio/voice/E3/Free/SS/S1/shou/28.ogg"
    ss "S--Sorry… You okay, broseph?"
    pf "I think so."
    jump E3SSS1_Covergence

label E3SSS1_shortbus:
    "My legs keep pumping, when suddenly my foot scrapes the floor, causing me to faceplant."
    show shou hap at cc with dissolve
    show note:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    "Shou bursts out laughing."
    show shou smi
    voice "audio/voice/E3/Free/SS/S1/shou/29.ogg"
    ss "You okay, broseph?"
    "After a second, I push myself to my feet."
    pf "I think so…"
    voice "audio/voice/E3/Free/SS/S1/shou/30.ogg"
    ss "What happened?"
    pf "I'm not too sure myself."
    "There's probably a lesson in here somewhere about the dangers of pride."
    jump E3SSS1_Covergence

label E3SSS1_success:
    $ E3SSS1_SUCCESSFULLYATHLETIC = 1
    "My legs keep pumping, and as the vault draws near, I take a deep breath, readying myself. I push all the power into my legs as I leap over the springboard. My hands touch the vault briefly as I spring off of it and complete a flip. I land too hard on my feet and stumble a few steps, but I don't fall."
    show shou smi at cc with dissolve
    "Shou claps."
    voice "audio/voice/E3/Free/SS/S1/shou/31.ogg"
    ss "Bravo! Unfortunately, you didn't stick your landing so I'll have to dock you a few points…"
    pf "I'd like to see you do better."
    jump E3SSS1_Covergence

label E3SSS1_BalanceJump:
    hide shou with dissolve
    "I jump and catch the still rings, letting my body hang. The rings wobble around as I try to pull myself up."
    "Whoa! This is a lot harder than I thought it'd be…"
    voice "audio/voice/E3/Free/SS/S1/shou/32.ogg"
    ss "Use your core!"

    if (MCStory == 1):
        "I squeeze my core tight and slowly lift myself so my body makes a straight arrow shape over the rings. The rings tremble in time with my arms. Finding my center of balance, and feeling daring, I gingerly pull my legs straight out in front of me."
        "Shou watches me with wide eyes."
        "After holding this pose for a couple of seconds, I relax and hop back down to the ground."
        jump E3SSS1_SucccessfulInHolding

    else:
        "I squeeze my core tight and try to do a pull up. The rings shake precariously. I have to hold them…"
        "Just don't panic and keep it steady!"
        
        $ qtebase = 5
        $ qtetotal = qteintel + qtebase
        $ t_var = qtetotal
        show screen timer_scr(place="E3SSS1_RINGFAIL")

        menu:
            "Fall...":
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGFAIL

            "Panic...":
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGFAIL

            "Wobble...":
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGFAIL

            "{color=#00ff00}{b}Steady!{/b}{/color}" if (MCStory == 1):
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGSUCCESS
                
            "Steady!" if (MCStory != 1):
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGSUCCESS

            "Flail...":
                $ renpy.hide_screen ("timer_scr")
                jump E3SSS1_RINGFAIL      
        
        

label E3SSS1_RINGFAIL:
    "Oh no! I can't seem to find my center of balance and my arms give way. I fall ungracefully onto the mats."
    show shou cur at cc with dissolve
    "Shou winces in sympathy and offers me a hand."
    voice "audio/voice/E3/Free/SS/S1/shou/33.ogg"
    ss "You hurt, broseph?"
    pf "Just my pride…"
    "I accept his hand and he helps me to my feet."
    show shou mis
    voice "audio/voice/E3/Free/SS/S1/shou/34.ogg"
    ss "It's not as easy as it looks, huh?"
    "I reluctantly nod."
    pf "Yeah… I didn't realise there was more than just strength involved. There's balance and coordination too."
    jump E3SSS1_Covergence

label E3SSS1_RINGSUCCESS:
    $ E3SSS1_SUCCESSFULLYATHLETIC = 1
    "I manage to steady myself, and after finding my center of balance, I slowly do three pull-ups in a row."
    "Shou watches on with interest."
    "Afterwards, I let go and drop to my feet."
    label E3SSS1_SucccessfulInHolding:
    show shou cur at cc with dissolve
    voice "audio/voice/E3/Free/SS/S1/shou/35.ogg"
    ss "You sure you haven't done this before? You were a pro!"
    "I grin."
    pf "Nope, I knew I had nothing to worry about. Piece of cake."
    jump E3SSS1_Covergence

label E3SSS1_Covergence:
voice "audio/voice/E3/Free/SS/S1/hito/1_Hitomi.ogg"
hito "Shou!"
hide shou with dissolve

show shou cur at r2:
    xzoom -1
show studentF extra at l2
with dissolve

"A girl I don't recognise waves at Shou as she races over."
voice "audio/voice/E3/Free/SS/S1/hito/2_Hitomi.ogg"
hito "How's it going?"
show shou smi
voice "audio/voice/E3/Free/SS/S1/shou/36.ogg"
ss "Hey, Hitomi."
"She looks me up and down."

if (E3SSS1_SUCCESSFULLYATHLETIC == 1):
    "She smiles with interest."
    voice "audio/voice/E3/Free/SS/S1/hito/3_Hitomi.ogg"
    hito "Who's your impressive friend?"
    voice "audio/voice/E3/Free/SS/S1/shou/37.ogg"
    ss "You saw him too?!"
    "She nods."

else:
    "She smiles at me."
    voice "audio/voice/E3/Free/SS/S1/hito/4_Hitomi.ogg"
    hito "Who's your friend?"

show shou hap
voice "audio/voice/E3/Free/SS/S1/shou/38.ogg"
ss "Hitomi, meet Broseph."
voice "audio/voice/E3/Free/SS/S1/shou/39.ogg"
ss "Broseph, meet Hitomi."
show shou cur
"She blinks."
voice "audio/voice/E3/Free/SS/S1/hito/5_Hitomi.ogg"
hito "...Broseph?"
"Shou nods and beams."
pf "Uh, it's [pfirst]."
show shocked:
    xoffset 1040
    yoffset 20
    xzoom .75
    yzoom .75
show shou sur
voice "audio/voice/E3/Free/SS/S1/shou/40.ogg"
ss "Woah, really??"
show shou thi
"Uh, why is he surprised? I nod slowly. {w}He rubs his chin in thought."
voice "audio/voice/E3/Free/SS/S1/shou/41.ogg"
ss "I've been calling you broseph for so long, I forgot."
"Hitomi laughs and playfully touches Shou's arm."
voice "audio/voice/E3/Free/SS/S1/hito/6_Hitomi.ogg"
hito "Hehe, that's adorable!"
show shou hap
"Shou beams."
voice "audio/voice/E3/Free/SS/S1/hito/7_Hitomi.ogg"
hito "I'm just about done. How about you?"
show shou smi
voice "audio/voice/E3/Free/SS/S1/shou/42.ogg"
ss "I'm almost done too."
voice "audio/voice/E3/Free/SS/S1/hito/8_Hitomi.ogg"
hito "Okay, I'm going to start packing. Come find me when you want to head out."
"Shou nods. Hitomi smiles at him and then waves at me."
voice "audio/voice/E3/Free/SS/S1/hito/9_Hitomi.ogg"
hito "Nice to meet you!"
pf "Same."
hide studentF extra
hide shou
with dissolve

"She bounces out of the gym. I assume she's going to change in the locker room."

show shou smi at cc with dissolve

pf "You two know each other well?"
voice "audio/voice/E3/Free/SS/S1/shou/43.ogg"
ss "Kind of. We met in this class. Her dorm building is actually the one next to mine."
pf "That's pretty coincidental."
show shou hap
voice "audio/voice/E3/Free/SS/S1/shou/44.ogg"
ss "I know, right? Anyway, we ran into each other once and when she realised we lived so close together she's insisted that we walk back together ever since."

"The way that she acts towards Shou, it's obvious that she has more than a casual interest in him.  Of course, knowing Shou, that fact isn't obvious to him."

menu:
    "She's interested in you.":
        pf "Dude, you know she's into you, right?"
        show shou cur
        "Shou blinks then raises an eyebrow."
        show question:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E3/Free/SS/S1/shou/45.ogg"
        ss "What are you talking about?"
        pf "The laughing, the arm touching, the asking to walk back together..."
        "Shou shrugs."
        show shou smi
        voice "audio/voice/E3/Free/SS/S1/shou/46.ogg"
        ss "She's just friendly. You're looking too much into it."

        menu:
            "I'm telling Mayu.":
                pf "I wonder what Mayu would think if you were walking girls back to their dorms."
                show panic:
                    xoffset 720
                    yoffset 20
                    xzoom .75
                    yzoom .75
                show shou sur
                voice "audio/voice/E3/Free/SS/S1/shou/47.ogg"
                ss "Whaaa! Don't do that!"
                pf "I thought nothing's going on?"
                voice "audio/voice/E3/Free/SS/S1/shou/48.ogg"
                ss "Nothing {i}is{/i} going on. But I don't want Mayu to get the wrong impression."
                pf "You're not dating Mayu, so why would she care?"
                show shou neu
                voice "audio/voice/E3/Free/SS/S1/shou/49.ogg"
                ss "She wouldn't."
                pf "So then what's the issue?"
                show shou ske
                "Shou blinks, then frowns."
                voice "audio/voice/E3/Free/SS/S1/shou/50.ogg"
                ss "It's not an issue, but still..."
                pf "Alright, alright."
                "I think Shou is really confused about his own feelings..."

            "Why not pursue it?":
                pf "She's pretty cute… why not ask her out?"
                show shou cur
                "Shou blinks."
                voice "audio/voice/E3/Free/SS/S1/shou/51.ogg"
                ss "Wouldn't it become really awkward if she says no? We're in this class together."
                show shou neu
                voice "audio/voice/E3/Free/SS/S1/shou/52.ogg"
                ss "I'd rather not ruin a friendship by trying to go down another path."
                pf "If you say so."
                "What he's saying could literally be said about another girl he knows, whose name rhymes with \"nayu\"."

            "Alright, if you say so.":
                pf "Whatever you say, bro."
                show shou cur
                voice "audio/voice/E3/Free/SS/S1/shou/53.ogg"
                ss "I'm serious!"
                pf "Sure."
                "I give him a skeptical look."
                show shou ske
                voice "audio/voice/E3/Free/SS/S1/shou/54.ogg"
                ss "For realsies!"
                "I smirk and shrug."

    "Not my business.":
        "I don't want to stick my nose where it doesn't belong."


pf "Alright man, sounds like you'll be heading off soon and I still have to go work out."
show shou smi
"Shou nods."
voice "audio/voice/E3/Free/SS/S1/shou/55.ogg"
ss "It was good seeing you! You should stop by again."
pf "I'll think about it."


scene black with fade

"Shou gives me a broseph fist bump and we head our separate ways."
"I go work out until it's time to head home."


stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E3SSS1_Completed = 1