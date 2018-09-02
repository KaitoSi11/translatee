#EVENING EVENT
label E4KIS1:

$ kaoHairF = "default"
$ kaoHairB = kaoHairF
$ kaoOut = "kindergarten"

if E3KIS3_Completed == 1:
    $ kaorelatonship = 1

"I wonder what Kaori is up to… {w}I pull out my phone and give her a call."
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_01.ogg"
ki "Hello?"
pf "Hey, Kaori."
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_02.ogg"
ki "Hi."
pf "Are you busy?"
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_03.ogg"
ki "I'm just about to head to the daycare... It's going to be an extra busy day."

if E2KIS4_Completed == 0:
    "Shou and I caught Kaori's uncle in the campus parking lot one day right before we were going into town. He freely shared that Kaori volunteers at his daycare. He invited us to stop by but Kaori's death glare was enough to deter us. She may not act like it, but I think she's a little relieved that she doesn't have to hide this from us anymore."
    "Her uncle says Kaori is a big softie and a favourite instructor amongst the kids… {w}I'll believe it when I see it!"

pf "Extra busy?"
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_04.ogg"
ki "Yeah, we're understaffed since one person is on vacation and another person called in sick."
pf "Maybe I can help?"
"..."
pf "Hello?"
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_05.ogg"
ki "...If that's what you want, then I guess you can help."
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_06.ogg"
ki "But don't forget it's still work!"
pf "Yes ma'am!"
if E3KIS1_maamcall == 1:
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_07.ogg"
    ki "Don't start this again."
    pf "Yes--"
    "Kaori disconnects the call before I can finish. Rude!"

else:
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_08.ogg"
    ki "Don't call me \"ma'am\"! Now hurry up and get here."
    "Before I have a chance to say one of my sick rebuttals, she hangs up the phone. Damn."

"Oh well. I better not be late or Kaori will be angry."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"I find my bike and drive to the daycare."

scene bg isokaze shrine dusk with fade

"When I arrive, Kaori is nowhere to be found. I follow a group of adults into the building."

scene bg campus library dusk with fade

"They're either parents or staff, but either way they'll get me where I need to be. Considering there are no kids tagging along, I think it's safe to say that they're staff."
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 7
"We pass through one of the children's playrooms and continue into an office in the back. Kaori is there with another guy, discussing something I can't hear. She nods in greeting when I enter."
"Once everyone gets situated, the guy clears his throat."


show boyfriend smi at cc with dissolve

voice "audio/voice/E4/Eito/E4/Kaori/1.ogg"
ei "Hello, everyone! I know we haven't had one of these staff meetings in a while, but it's going to be a bit busy today since Daichi is on vacation and Hibiki called in sick."
show boyfriend hap
voice "audio/voice/E4/Eito/E4/Kaori/2.ogg"
ei "Luckily, Kaori's friend has offered to help out so we'll only be short one man instead of two!"
"Everyone stares at me as he smiles in my direction."
pf "Uh, hi, I'm [pfull]. Happy to help."
show boyfriend smi
voice "audio/voice/E4/Eito/E4/Kaori/3.ogg"
ei "Glad to meet you. I'm Eito Iwasa."
voice "audio/voice/E4/Eito/E4/Kaori/4.ogg"
ei "Since we'll have to do a little shuffling with coverage, here are everyone's roles for today."
"Eito checks his clipboard and goes down a list of names. Kaori watches silently as Eito takes charge. Once he's finished, he looks at me."
voice "audio/voice/E4/Eito/E4/Kaori/5.ogg"
ei "Since you're from ACE, we'll have you tutoring the older kids."
"I nod."
voice "audio/voice/E4/Eito/E4/Kaori/6.ogg"
ei "Kaori and I will attend to the toddlers and younger kids."

if kaorelatonship == 0:
    "I'm surprisingly pumped for this assignment. Tutoring kids should be a piece of cake considering how much I've helped Nikki in the past! I'm such a good {i}onii-chan{/i}."

if kaorelatonship == 1:
    "Wait, Kaori won't be in tutoring with me?"

    menu:
        "Don't say anything. It's no big deal.":
            "A twinge of jealousy makes my mouth taste stale, but I swallow it back down. {w}It makes sense that the more seasoned staff or volunteers would take care of the younger kids. I'd be concerned if they stuck some random guy with no childcare experience in there instead."
            "Although my brain sees reason, my heart still sees red."

        "I want to be assigned with Kaori.":
            pf "Is there any way I could help Kaori with the younger kids?"
            show boyfriend cur
            "The group starts whispering to each other. I guess I look like {i}that{/i} guy. {w}Kaori glares at me in warning, but Eito remains calm."
            show boyfriend smi
            voice "audio/voice/E4/Eito/E4/Kaori/7.ogg"
            ei "I don't mind switching if that's what you're more comfortable with. How much experience do you have with younger kids?"
            pf "...Not much."
            show boyfriend cur
            voice "audio/voice/E4/Eito/E4/Kaori/8.ogg"
            ei "A few months?"
            pf "...Less."
            show boyfriend neu
            "He frowns."
            voice "audio/voice/E4/Eito/E4/Kaori/9.ogg"
            ei "Hmm... The younger children need a lot more attention and guidance than the older kids."
            "Kaori snaps before Eito can continue."
            hide boyfriend with dissolve
            show kaori ann at l2
            show boyfriend cur at r2:
                xzoom -1
            with dissolve
            voice "audio/voice/MISSING/BATCH5/k_redo_17.ogg"
            ki "You can take care of the older kids. Eito and I have the most experience and will take care of the younger kids."
            "I can tell Kaori's annoyed. I'm not please either, but I bite my tongue. They have a point. I don't have any experience with young children and it'd be irresponsible of them to place me in there."
            pf "Fine."
            hide kaori
            hide boyfriend
            with dissolve


"With everyone's roles assigned, the group slowly disperses. One of the staff members offers to take me to the tutoring room. I thank them and follow her into a room filled with children between 4th-6th grade."

scene black with fade

"Seeing a new face, the kids kept interrupting me to ask questions about myself. They were especially curious because I didn't look very Japanese. They asked about where I was from, what was it like back home, what was it like to be a pilot..."
"I tried hard to keep their focus on their homework, but it was a lot tougher than I expected. Finally, I gave up and answered their questions."
"Once their questions were out of the way, they were able to focus on their homework. Although they tried hard, most of the children had difficulty grasping the material. I could tell they were frustrated, so I tried to think up different ways of explaining the same things, which helped immensely."

if E2KIS4_Completed == 1:
    "I understand why Kaori is so adamant to be there for these kids even when she's exhausted."

"After a while, it looks like everyone is on track."

if kaorelatonship == 1:
    "Knowing that Eito and Kaori are alone together still makes me uneasy..."

"I'll go see how Kaori is doing. {w}It doesn't take me long to find the younger kids. All I had to do was follow the sounds of shrieks and laughter."

$ persistent.gpix[35][0] = 1
scene cg kaori kindergarten 1 with fade:
    xzoom .5
    yzoom .5

"I gently push open the door and see Kaori surrounded by children! Both of her arms are full of kids and one even hangs off her back. The rest hug her legs. Although Kaori weakly protests, the huge smile on her face gives away her true feelings. {w}I've never seen her this happy before!"
"A chorus of \"Miss Kaori\" circles her as the children compete for her attention."
"Suddenly, the child on Kaori's back slips. With a sharp yelp, she grabs a strap on Kaori's clothing."

scene bg campus library dusk with fade

show kaori cur at r2 with dissolve:
    xzoom -1
show exclamation:
    xoffset 1040
    yoffset 110
    xzoom .75
    yzoom .75
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_09.ogg"
ki "Careful!"
"The strap falls off her shoulder as she bends down so the child can land softly on a table."
show boyfriend smi at l2 with dissolve
voice "audio/voice/E4/Eito/E4/Kaori/10.ogg"
ei "I got it."
"Eito gently places the strap back onto Kaori shoulder. I wait in secret glee for the impending doom Eito has inflicted upon himself by touching her, but to my surprise, Kaori doesn't react."
"As Eito tries to take one of the kids out of Kaori's hands, the child looks at Eito for a second, then burrows her face into Kaori's shoulder. Kaori laughs."

show kaori mis

voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_10.ogg"
ki "I don't think she wants to leave anytime soon."
show boyfriend hap
"Eito laughs too."
show boyfriend smi
voice "audio/voice/E4/Eito/E4/Kaori/11.ogg"
ei "I can't really blame her."

if kaorelatonship == 0:
    "O-la-la, do I sense young-love in the air? I can't help but grin."
    voice "audio/voice/E4/Eito/E4/Kaori/12.ogg"
    ei "Since you've got your hands full, why don't I take care of their snacks and set up for the next activity?"
    show kaori smi
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_11.ogg"
    ki "That'd be great, thanks."
    show boyfriend hap
    voice "audio/voice/E4/Eito/E4/Kaori/13.ogg"
    ei "No problem!"
    "They smile at each other. {w}Wow, a smile from Kaori! It must be serious!"
    scene black with fade
    "I tip-toe back out of the room and return to my older kids. It looks like Kaori is doing more than okay."

elif kaorelatonship == 1:
    "If it were anyone else, Kaori would have slapped them for touching her so intimately!"
    menu:
        "Confront Eito.":
            stop music fadeout 1.5
            "I stride up to the pair and stand between them while glaring at Eito."
            show kaori cur
            pf "Don't do that again."
            show boyfriend cur
            "Eito and Kaori seem equally shocked and confused."
            voice "audio/voice/E4/Eito/E4/Kaori/14.ogg"
            ei "...Don't do what again?"
            pf "Stop acting dumb. You think I don't know what you're trying to do?"
            show boyfriend sur
            show kaori sur
            "Eito glances nervously at the kids. As I follow his gaze, I soften my scowl. The children stare at me with wide eyes and trembling lips."
            show boyfriend neu
            "I didn't mean to scare them!"
            show kaori ann
            "Kaori frowns and puts the children back down on the floor."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_12.ogg"
            ki "Eito, please watch the kids for me. I'll be back in a minute."
            voice "audio/voice/E4/Eito/E4/Kaori/15.ogg"
            ei "Y-Yeah, sure thing."
            hide boyfriend
            hide kaori
            with dissolve
            "She grabs my arm and pulls me out of the room. As soon as we are outside, her ferocious glare returns."
            show kaori ang at cc with dissolve
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_13.ogg"
            ki "What is wrong with you?!"
            jump E4KIS1_upsetconv


        "Talk to Kaori in private.":
            stop music fadeout 3
            $ E4KIS1_TalkedKaori = 1
            show kaori neu
            "I stride into the room. Kaori glances as I approach and her smile falters. She looks at me with curiosity and concern."
            pf "Can we talk?"
            show kaori cur
            "My tone must have been severe because she blinks in surprise, then nods and places the children back on the ground."
            show kaori neu
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_14.ogg"
            ki "I'll be right back, Eito."
            show boyfriend hap
            voice "audio/voice/E4/Eito/E4/Kaori/16.ogg"
            ei "No problem, we'll be fine. Right, kids?"
            "The children had gone quiet when I entered, but Eito's over-enthusiasm brings them right back to life." 
            hide boyfriend
            hide kaori
            with dissolve
            "Kaori leads me through the hallway outside the room. As soon as we're outside, my emotions get the better of me and I can't hold it in anymore."
            show kaori neu at cc
            pf "What was that?"
            show question:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ske
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_15.ogg"
            ki "What was what?"

            label E4KIS1_upsetconv:
            play music "audio/music/Stress (GAME VERSION).ogg" fadein 3
            pf "Eito was touching you and you didn't even care!"
            show kaori ann
            "She furrows her brow."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_16.ogg"
            ki "Huh? What are you talking about?"
            pf "He put your strap back on!"
            show kaori ske
            "Kaori looks at me like I'm an idiot… and now that I've said that outloud, I feel like one too..."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_17.ogg"
            ki "Why would I care about that?"
            pf "Because!"
            show kaori ann
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_18.ogg"
            ki "Because why?"
            "Although I'm bubbling inside, I can't find the words to explain myself and silently fume."
            pf "...Just because!"
            stop music fadeout 3
            "Kaori scowls and let's out a frustrated sigh."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_19.ogg"
            ki "You aren't making any sense! You're acting like a--"
            show kaori cur b2 with dissolve
            "She freezes, and glances sharply at me. Then she looks away as she blushes."
            show shoBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori sur b2
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_20.ogg"
            ki "H-Hold on! Eito and I just work together!"
            show kaori cur b2
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_21.ogg"
            ki "You and I are..."
            show kaori thi b2
            "Her cheeks are beet red."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_22.ogg"
            ki "Y-You know..."
            "Kaori grabs my hand and squeezes it gently. I relax slightly at her touch."
            show kaori neu b2
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_23.ogg"
            ki "...So you have nothing to worry about, okay?"
            show kaori neu b2
            "She still doesn't make eye contact, but her look has softened completely, making her seem strangely vulnerable. Seeing her exposed like that makes me feel silly for acting jealous."
            pf "Okay."
            "We stand in awkward silence before Eito pops his head out."
            show boyfriend cur at l3 with dissolve:
                xoffset -200
            voice "audio/voice/E4/Eito/E4/Kaori/17.ogg"
            ei "Uh, I don't mean to interrupt, but the kids are getting restless without you, Kaori. This happens everytime they see you first... they forget all about me..."
            show kaori cur b1 with dissolve
            "Kaori blinks then chuckles."
            show kaori smi with dissolve
            #voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_24.ogg"
            voice "audio/voice/MISSING/BATCH5/k_redo_21.ogg"
            ki "Alright."
            hide kaori with dissolve
            "She gives me one last reassuring look, then heads back inside with the kids. Eito lingers beside me."

            if E4KIS1_TalkedKaori == 1:
                voice "audio/voice/E4/Eito/E4/Kaori/18.ogg"
                ei "Is everything okay?"
                pf "Yeah, my {i}girlfriend{/i} and I just had to talk about something."
                show boyfriend sur
                "Eito's eyes widen when he hears \"girlfriend\"."

            show boyfriend ner
            voice "audio/voice/E4/Eito/E4/Kaori/19.ogg"
            ei "Hey man, I'm really sorry! She doesn't talk about her personal life so I had no idea. Otherwise I would never--"
            pf "Well you know now. So back off and we'll be just fine."
            show boyfriend neu
            "That sounded a lot more curt than I intended, but he doesn't seem offended. He nods."
            "After a short pause, he speaks again."
            show boyfriend smi
            voice "audio/voice/E4/Eito/E4/Kaori/20.ogg"
            ei "You are one very lucky guy."
            pf "I know."
            scene black with fade
            "With this misunderstanding cleared up, I return to my older kids and continue to help with tutoring."

        "Don't do anything.":
            $ E4KIS1_nothing = 1
            "As much as it bothers me to see Eito interact with Kaori like that, I have to remain calm."
            scene black with fade
            "This isn't the type of environment where causing a scene would be appropriate, and now that I've had a chance to breathe and assess the situation, what happened isn't actually a big deal."
            "Besides, Kaori is a one-man girl. I needn't be so insecure."
            "I take another deep breath. After getting myself in order, I head back to the tutoring room."



"Another hour passes by in a blur, and before long, the parents trickle in to collect their children. The kids whine that they want to stay longer with Miss Kaori, but their parents urge them home. After all the kids have gone, the staff wave goodbye to each other and pack up to go home too."
"Before I go, I want to catch up with Kaori."

scene bg campus library dusk with fade

if E4KIS1_nothing == 0 and kaorelatonship == 1:
    show kaori neu at cc with dissolve
    "To my surprise, Kaori approaches me first. I acted stupidly today, and although we talked it out, I feel like I'm about to get another earful."
    play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
    show kaori sad
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_24.ogg"
    ki "...I'm sorry."
    "That catches me completely off-guard."
    pf "W-What?"
    show kaori wor
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_26.ogg"
    ki "I made you feel... ummm... uncomfortable…"
    show kaori sad
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_27.ogg"
    ki "I thought about it some more... and I maybe should have been more clear to Eito to begin with..."
    "Kaori looks worried as a soft blush stains her cheeks. Forget about earlier, now I feel even more guilty."
    pf "No, it's not your fault. I shouldn't have acted like that at all..."
    "We stand awkwardly, unsure what to say next."
    show miguel hap at l3 with dissolve:
        xoffset -200
    voice "audio/voice/E4/Miguel/miguel_01.ogg"
    mv "Kiss and make up already!"
    show kaori sur b2 with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_28.ogg"
    ki "U-Uncle! How long have you been there--wait, what are you doing?!"
    show miguel mis
    "I turn around to see Uncle Miguel holding up his cell phone."
    voice "audio/voice/E4/Miguel/miguel_02.ogg"
    mv "I must document this momentous occasion! For your children!"
    "Kaori's mouth drops open as her face turns as bright as a tomato. I'm positive my face is equally red!"
    show kaori ang b3 with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_29.ogg"
    ki "W-What?! D-Don't say r-ridiculous things like t-that! Give me that phone!"
    show miguel sur
    voice "audio/voice/E4/Miguel/miguel_03.ogg"
    mv "No, I cannot!"
    show kaori ann b3
    show miguel mis
    "Kaori charges after Miguel who skillfully keeps the phone just out of her reach."
    show kaori ang b3
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_30.ogg"
    ki "Uncle Miguel!"
    show miguel mis
    voice "audio/voice/E4/Miguel/miguel_04.ogg"
    mv "You will thank me one day, my sweet!"
    scene black with fade
    "I can't help but laugh at the sheer ridiculousness of the situation. {w}All in all, today was a good day."

elif E4KIS1_nothing == 1 and kaorelatonship == 1:
    "Kaori finds me first."
    show kaori smi at cc with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_31.ogg"
    ki "Hey you."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_32.ogg"
    ki "Sorry, we didn't have much of a chance to hang out today."
    pf "It's okay."
    show kaori cur
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_33.ogg"
    ki "I did see you come into the toddlers' room earlier but you left before I could say hi."
    pf "You had your hands full."
    show kaori smi
    "Kaori smiles."
    show kaori hap
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_34.ogg"
    ki "I heard the kids talking about you to their parents. They really liked you!"
    show kaori smi b1 with dissolve
    "She takes a step closer to me and her face turns red. She goes on her tiptoes and pecks me on the cheek."
    "I blink, surprised by her bold display of public affection."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_35.ogg"
    ki "T-That's your reward."
    pf "I should offer to help out more often if that's going to be my reward."
    show regBlush:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori smi b2 with dissolve
    "Kaori's blush deepens."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_36.ogg"
    ki "I'm almost ready to go. I'll see you in a few minutes."
    pf "Sure."
    scene black with fade
    "I wait for Kaori as she packs up her things. I can't remember why I was feeling insecure in the first place. I have nothing to worry about."
    "I couldn't have asked for a better day!"

elif kaorelatonship == 0:
    show kaori hap at r2:
        xzoom -1
    show boyfriend mis at l2
    with dissolve
    "I find her with Eito cleaning up the toddlers' room. Eito makes a comment which has Kaori  laughing."
    "Kaori laughing at somebody else's jokes? I never thought I'd see the day!"
    hide kaori
    hide boyfriend
    with dissolve
    "I chuckle to myself. Better not ruin their moment. I can catch up with Kaori tomorrow."
    "Before I can slip away again, Kaori notices me and heads over."
    show kaori smi at cc with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_37.ogg"
    ki "Hey."
    "I stop my giggling and clear my throat. She raises an eyebrow."
    show kaori cur
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_38.ogg"
    ki "Uh... what's up with you…?"
    voice "audio/voice/E4/Miguel/miguel_05.ogg"
    mv "I can't believe she doesn't know."
    show miguel hap at l3 with dissolve:
        xoffset -200
    "I spin around and spot Uncle Miguel chuckling behind me."
    pf "I know, right? It's cute how oblivious she is."
    show miguel smi
    "Miguel nods, but Kaori huffs."
    show kaori ske
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_39.ogg"
    ki "What is wrong with you two?!"
    show boyfriend hap at r3 with dissolve:
        xzoom -1
        xoffset 200
    voice "audio/voice/E4/Eito/E4/Kaori/21.ogg"
    ei "Hey Kaori, I'm heading off. I'll see you later!"
    show kaori hap b1 with dissolve
    "Kaori's demeanor softens when she waves at Eito."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_40.ogg"
    ki "Oh, yeah, sure! Good work today."
    show boyfriend mis
    voice "audio/voice/E4/Eito/E4/Kaori/22.ogg"
    ei "You too!"
    hide boyfriend with dissolve
    "Miguel chuckles again and pitches his voice high."
    show kaori cur b1
    show miguel hap
    voice "audio/voice/E4/Miguel/miguel_06.ogg"
    mv "{i}Good work today!{/i}"
    pf "{i}You too!{/i}"
    show kaori sur b2 with dissolve
    "Kaori freezes as her face turns beet red."
    show kaori thi b2 with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_41.ogg"
    ki "It's n-nothing like that!"
    show miguel mis
    voice "audio/voice/E4/Miguel/miguel_07.ogg"
    mv "Sure."
    pf "We believe you."
    show kaori ang b2
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_42.ogg"
    ki "Stop!"
    hide kaori with dissolve
    "She scowls at us then stomps back into the toddlers' room and throws toys into their bins."
    pf "Young love, so precious."
    show miguel hap
    "Miguel grins."
    scene black with fade
    "I'm glad I came out today. I got to see another side of Kaori… one that I won't soon let her forget!"
    
"After I gather all my things, I drive home."

stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4KIS1_Completed = 1