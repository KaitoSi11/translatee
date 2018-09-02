#EVENING EVENT
label E4KIS2:

    $ kaoOut = "sGym"
    $ kaoHairF = "tied"
    $ kaoHairB = "tied"


"Just as I am about to dial Kaori's number, she calls me instead. I answer."
pf "Hey."
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_43.ogg"
ki "Hi, are you busy?"
pf "Not particularly, what's up?"
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_44.ogg"
ki "Did you want to come to the gym with me? I'm going to try a new routine and would like to have a spotter."
pf "Yeah, sure thing. The gym in the rec center?"
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_45.ogg"
ki "Yes, thanks."
pf "No problem, see you there."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"I make my way to the rec center and quickly get changed. Once I'm done, I enter the gym."
scene bg campus gym night with fade
play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
show kaori neu at cc with dissolve
"Kaori is in her \"gym uniform\" and I stifle a laugh. I thought I'd be used to it by now... but I'm not."

if kaorelatonship == 0:
    "As she stretches, I notice a few guys staring very obviously at her, but Kaori is too focused to notice."
    "They got lucky this time."

pf "Hey, Kaori."
"She nods."
show kaori smi
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_46.ogg"
ki "Hi. Thanks for agreeing to help."
pf "No problem, I was going to get a workout in anyway."
pf "So what's this new routine you have planned?"
"She hands me her phone and I scroll through."
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_47.ogg"
ki "I've mainly been doing endurance training and would like to incorporate more mass building."

menu:
    "Sounds good!":
        pf "Alright, let's get started then."

    "Why would you want to gain mass as a girl?":
        "I raise an eyebrow."
        pf "...Mass building?"
        show kaori cur
        "She nods, but her eyes narrow."
        if kaorelatonship == 0:
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_48.ogg"
            ki "...Yes."
            pf "I mean, it's your choice, but really?"
            show kaori dis
            "She crosses her arms and frowns."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_49.ogg"
            ki "I'm not trying to bulk up the way you think."
            show kaori ann
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_50.ogg"
            ki "But even if I were, it'd be none of your business!"
            "I shrug. Like I said, it's her choice."
            pf "Alright, alright. Ready to begin?"
        elif kaorelatonship == 1:
            pf "I mean, you look really good right now. I'm not sure why you'd want to... \"get big\"."
            show kaori dis
            "She hits me hard on the arm. That stings!"
            pf "Ow!"
            show kaori ann
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_51.ogg"
            ki "Because trying to knock some sense into someone as dense as you requires a lot of strength!"
            "I rub my fresh bruise."
            pf "You seem plenty strong already..."
            "Kaori glares at me."
            pf "B-But do as you wish!"

    "What's the occasion?":
        pf "Any reason for the new routine?"
        show kaori neu
        "Kaori shakes her head."
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_52.ogg"
        ki "Not particularly. My routine was just getting a bit too repetitive and this will be a nice change of pace."
        pf "Fair enough. Are you ready to start then?"

show kaori neu
"She nods and we find an empty bench. She begins gathering weights and adds them to the bar..."
"...and keeps adding weights..."
"My jaw drops as she adds 100 pounds to the bar. Is this petite girl for real?"
hide kaori with dissolve
"Kaori lies down on the bench and I stand by her head. She adjusts her grip and focuses her breathing, then lifts the bar off and begins her reps."
"Although I knew Kaori took her fitness seriously, I'm still impressed. She's attracted a few more onlookers too, so I'm not the only one impressed." 
"With one final exhale, she places the bar back on the bench." 
show kaori neu at cc with dissolve
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_53.ogg"
ki "Alright, warm-ups are done."
"Those were just warm-ups?!"
hide kaori with dissolve
"She adds another 20 pounds to her weights and repeats her reps."
"After she's completed her sets, she slides out from the bench and wipes her face with a towel."

menu:
    "Good job!":
        pf "Very nice!"
        show kaori smi at cc with dissolve
        "Kaori offers me a smile."
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_54.ogg"
        ki "Thanks."

    "Geez, how much of her weight is just muscle?":
        pf "Benching more than your body weight is very impressive."
        show kaori smi at cc with dissolve
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_55.ogg"
        ki "Thanks."
        show kaori sur b1 with dissolve
        "Suddenly, her face turns pink and she hits me on the arm."
        show kaori dis b1
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_56.ogg"
        ki "Hey, don't try to guess my weight!"
        "I grin. Guilty as charged."

show kaori neu
voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_57.ogg"
ki "Okay, your turn now."

if MCStory == 1:
    "It's my time to shine!"
else:
    "I mainly do cardio at the gym to stay fit and only occasionally do endurance training. I don't think I can bench much more than her."

"How do I want to play this?"

menu:
    "Go with a safe 100 pounds and high reps.":
        "I pull off 20 pounds and slide onto the bench. Kaori spots for me as I begin my reps. After 3 sets, I finish."
        show kaori smi
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_58.ogg"
        ki "I didn't know you do endurance training too."
        pf "Yeah, I'm not too interested in becoming a beefcake."
        "Kaori grins, clearly amused."

    "Let's push it up a bit to 140 pounds.":
        "I add extra weights to the bar, and push my limit while doing a double set."
        "Kaori nods once I'm done."
        show kaori smi
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_59.ogg"
        ki "I'm glad to see you keep up with your training."
        pf "Of course, a healthy body is important."
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_60.ogg"
        ki "Exactly! If only Shou believed that too. I tried to set up a regular gym schedule with him in the past, but gave up when he kept slacking."
        pf "I don't mind being your partner."
        show kaori hap
        show note:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_61.ogg"
        ki "I'd like that. We can motivate each other to push our limits!"
        pf "Exactly!"
        "She smiles."

    "Beast mode activation, 200 pounds.":
        if MCStory == 1:
            "LET'S DO THIS!"
            "I slap on weights until I've reached 200 pounds. With great determination, I pump out some mad reps with my swoll body."
            show kaori cur
            "Once complete, Kaori stares at me with her mouth hanging open."
            show kaori cur b1 with dissolve
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_62.ogg"
            ki "...I... didn't know you were so fit."
            "I smirk."
            if kaorelatonship == 0:
                pf "How else would I impress the ladies?"
                show kaori thi
                "Kaori rolls her eyes."
                voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_63.ogg"
                ki "Of course that's your reason."
                pf "Whatever works!"
            if kaorelatonship == 1:
                pf "Are you impressed?"
                show kaori thi b2 with dissolve
                "Kaori blushes."
                show tsuBlush:
                    xoffset 720
                    yoffset 110
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_64.ogg"
                ki "I-It was only alright!"

        else:
            "It's time to man up! I add a bunch of weights and soon I'm at 200 pounds."
            show kaori ske
            "Kaori looks skeptical."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_65.ogg"
            ki "...Uh, are you sure about this?"
            pf "Let me show you how a man handles his weights."
            show kaori neu
            "I slide under the bench and grab the bar."
            "As soon as I lift it off the bench, the bar droops lower and lower and I can't seem to push it back up to the bench."
            show kaori cur
            "Oh crap!"
            pf "...I think I need some help."
            show kaori mis
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_66.ogg"
            ki "Is this what a man looks like when he's handling his weights?"
            "Kaori looks amused as I struggle to keep the bar from squishing me."
            show kaori smi
            "Right before it touches my chest, she intervenes and helps me lift it back up. My face burns from a mixture of embarrassment and exertion."
            show kaori mis
            show note:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_67.ogg"
            ki "Very impressive."
            "She masks a giggle with her hand."
            pf "Laugh it up!"

if kaorelatonship == 1:
    hide kaori with dissolve
    "We run through the rest of her routine, one exercise after another. She times her rest periods down to the second, and diligently follows the mantra of \"one more rep\"."
    "I follow her routine as well. It's definitely more challenging than the typical stuff I do at the gym."
    "Once we've completed her list, Kaori turns to me."
    show kaori neu at cc with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_68.ogg"
    ki "Do you have any specific exercises you want to do?"
    "I shake my head."
    pf "That was a solid workout."
    "Kaori nods. She gathers the weights and places them back where she found them, then wipes down the equipment."
    stop music fadeout 10
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_69.ogg"
    ki "Come on."
    "I follow Kaori towards the mats."
    pf "Uh, what are we doing now?"
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_70.ogg"
    ki "Stretching."
    pf "Oh."
    show kaori ske
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_71.ogg"
    ki "You don't want to be stiff, right?"
    pf "Right."
    show kaori neu
    "Kaori loosens up and shakes out her limbs, then begins with basic stretches as I follow suit."
    "As she interlaces her arms behind her, she glances over at me."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_72.ogg"
    ki "Actually, do you think you could help me stretch? I can help you too."
    pf "Uh…"
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_73.ogg"
    ki "Here, pull on my arms."
    "I move behind her and gently pull her arms back."
    pf "Is this good?"
    show kaori smi
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_74.ogg"
    ki "Mmhm."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
    "As I hold her in position, I look up at the mirror in front of us… and straight at Kaori's chest. I quickly look away. With her arms pulled back like that it leaves her chest wide open!{w} Thankfully, her eyes are closed so she can focus on her breathing." 
    show kaori neu
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_75.ogg"
    ki "Next stretch."
    "I drop Kaori's arms. She gets down on the mat and lies down on her stomach."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_76.ogg"
    ki "Hold me under the knee and help me lift my leg up."
    "...I have never been more thankful to the person who created Japanese gym uniforms. I admire the perfect roundness of her derriere and the slight jiggle as she lifts her leg--"
    show kaori ske
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_77.ogg"
    ki "Hey! Did you hear me?"
    pf "Huh?"
    pf "Oh right…"
    show kaori neu
    "I kneel down beside her and do as she asks, gently holding her leg up."
    show kaori cur
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_78.ogg"
    ki "Wait, I need support for my lower back. Can you put your hand there?"
    "You don't have to ask me twice! I rest my hand on her lower back, right above the curve of her butt, and lift again."
    show kaori win b2 with dissolve
    #voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_79.ogg"
    voice "audio/voice/MISSING/BATCH5/k_redo_18.ogg"
    ki "Ah!"
    pf "Too much?"
    show kaori thi b2 with dissolve
    "She shakes her head."
    
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_80.ogg"
    ki "No, a little more…"
    "As I lift her leg higher, her uniform bottom rides up, revealing firm, porcelain flesh."
    "!"
    "I avert my gaze as my heart beats faster. Do I tell her or just pretend I don't see this?"
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_81.ogg"
    show kaori smi b1 with dissolve
    ki "Okay, your turn."
    "I let out the breath I didn't realise I was holding as Kaori untangles herself from her position."
    pf "Uh, I'm good, we can continue with your stretches."
    "She shrugs, then lies down on her back and lifts one leg."
    show kaori cur
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_82.ogg"
    ki "Can you push my leg forward?"
    "I hover over her and hold her up by her calf to gently apply pressure."
    show kaori neu
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_83.ogg"
    ki "No, you have to be lower. I need your support for my leg."
    pf "...Lower where?"
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_84.ogg"
    ki "Kneel down and push that way."
    "I do as she asks, and she holds her leg straight against my shoulder."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_85.ogg"
    ki "More!"
    "I lean in, using my body to help keep her leg straight."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_86.ogg"
    ki "Still more."
    "Scooting even closer to her, I gently lean in a little more. {w}The back of my neck tingles and I look around the room at the myriad of eyes on me. After glancing in the mirror, I quickly break away from her. {w}From that angle it looks like I'm--"
    "My face reddens. Kaori bolts straight up and frowns."
    show kaori ann
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_87.ogg"
    ki "Why'd you stop?"

    menu:
        "Explain why.":
            pf "I think that's enough stretching for now."
            show kaori cur
            "She looks curiously at me."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_88.ogg"
            ki "What's going on?"
            pf "...Well, it's a little uncomfortable."
            show kaori neu
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_89.ogg"
            ki "No, the pressure was okay. I've been working on my flexibility so a little burn is good."
            pf "No, I mean for me."
            show kaori cur
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_90.ogg"
            ki "Huh?"
            pf "You seriously don't see it?"
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_91.ogg"
            ki "See what?"
            pf "Alright, go back."
            show kaori neu
            "We get back into the same position and I gesture towards the mirror."
            pf "What does that look like to you?"
            show kaori cur with dissolve
            $renpy.pause(.5)
            show kaori sur b3 with dissolve
            show shoBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "She looks blankly at the mirror, then her eyes grow wide as her face turns bright red. She scoots away from me."
            show kaori win b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_92.ogg"
            ki "I-I think that's enough stretching for today!"
            pf "R-Right!"

        "Why did I stop? Let's keep going!":
            pf "No reason. Let's get back into position."
            show kaori dis
            "She narrows her eyes but raises her leg again. I lean in just as close as before."
            pf "How's that feel?"
            show kaori neu
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_93.ogg"
            ki "Mm, good."
            "I grin."
            pf "Are you sure? Do you want me to go {i}deeper{/i}?"
            show kaori smi
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_94.ogg"
            ki "Well, maybe a little…"
            "I chuckle softly as I apply more pressure. Kaori frowns."
            show kaori cur
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_95.ogg"
            ki "Why are you laughing?"
            pf "I'm just happy to get a chance to be so close to you."
            show kaori cur b1 with dissolve
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_96.ogg"
            ki "O-Oh!"
            $renpy.pause(.5)
            show kaori sur b3 with dissolve
            show shoBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "She blinks and then turns her face away from me and towards the mirror. When she notices our position in the mirror, her eyes grow wide and her face turns bright red. She pushes me away."
            pf "Why'd you stop?"
            show kaori ang b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_97.ogg"
            ki "Because you--you--!"
            "I smirk. She wants to call me a pervert but knows she can't because I was only following instructions."
            pf "Was I doing it wrong?"
            show kaori win b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_98.ogg"
            ki "N-No!"
            pf "Did it not feel good?"
            show kaori ann b3
            "Her blush deepens."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_99.ogg"
            ki "T-That's enough! We're done with stretching!"
            pf "Aw, too bad."
            show kaori dis b3
            "She glares at me."

        "Innocence is bliss.":
            pf "Um, I'm just feeling a little tired now."
            show kaori neu
            "She nods."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_100.ogg"
            ki "We worked really hard today."

    hide kaori with dissolve
    "We put the mats away and head towards the locker rooms. Right before we split to get changed, she grabs my hand and looks down."
    show kaori smi at cc with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_101.ogg"
    ki "Thanks for helping me today. You did really well."
    pf "I'm glad you asked me to join you."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_102.ogg"
    ki "We should do this again."
    pf "Definitely."
    show kaori b2 with dissolve
    "She hesitates, then her cheeks turn pink as she quickly kisses me on the lips."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_103.ogg"
    ki "I'll see you in a few minutes!"
    hide kaori with dissolve
    "Before I can answer, she disappears into the women's locker room."
    "A smile spreads across my face as I enter the men's locker room. We'll definitely have to do this again soon!"

    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sCasual"
    
    "I quickly get changed, then meet Kaori out front."
    show kaori cur at cc with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_104.ogg"
    ki "So, there was something I wanted to ask you."
    pf "What's up?"
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_105.ogg"
    ki "AnimeCon is this weekend and I was thinking maybe we could go together…"
    show kaori thi
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_106.ogg"
    ki "But only if you want to!"
    "I grin."
    pf "Sure, that sounds like fun."
    show kaori hap
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_107.ogg"
    ki "Really? Okay!"
    "Kaori smiles. She seems genuinely excited for it."
    show kaori smi
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_108.ogg"
    ki "I better get back to studying."
    "I nod."
    pf "I'll see you later."
    
    scene black with fade
    "She waves, a small smile still on her lips, as we part ways."


else:
    "A loud vibration interrupts us. Kaori pulls out her phone and reviews her text messages."
    show kaori smi b1 with dissolve
    "As she reads, a smile creeps onto her face."
    "I think I may have an idea who that is!"
    show kaori ske
    "She sends a reply before looking back up. As soon as she sees my wide grin, her smile falters."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_109.ogg"
    ki "What's with that look?"
    pf "Was that Eito?"
    show kaori cur b1 with dissolve
    "Her cheeks flare."
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_110.ogg"
    ki "How did you know?!"
    pf "I have a younger sister, remember? I know what that grin means."
    show kaori thi b2 with dissolve
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_111.ogg"
    ki "I-It's not like that!"
    pf "What did he ask you?"
    show kaori ann b2
    "She refuses to answer."
    pf "Oooh... I guess I'll have to make my own conclusions then..."
    show kaori thi b2
    voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_112.ogg"
    ki "What? Don't be so stupid. He just asked if we can go get some snacks for the daycare. We're meeting at the mall."

    menu:
        "Looks like I'll have to play cupid!":
            pf "You know he's interested in you, right? It's a mall date."
            "Her cheeks brighten in color."
            show kaori ann b2
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_113.ogg"
            ki "W-What are you saying?"
            pf "Come on, I saw the way you two look at each other. It's totally obvious."
            show kaori thi b2
            "I expected Kaori snap at me but she looks surprisingly meek."
            pf "What do you think of him?"
            show kaori cur b2
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_114.ogg"
            ki "Well, he's responsible, hardworking, and disciplined... and also really sweet with the kids..."
            "That's a better answer than I anticipated, but she didn't answer my question."
            pf "No, I mean, do you {i}like{/i} him?"
            show kaori neu b3 with dissolve
            "She remains silent, but her face somehow turns even redder. Under my unfaltering gaze, she reluctantly nods."
            pf "You need to let him know then!"
            show kaori ann b3
            "She looks unsure for a second, then shakes her head and glares at me."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_115.ogg"
            ki "I am not having this conversation with you!"
            "Looks like I'll need to take matters into my own hands. While Kaori starts to put the weights away, I grab her phone. She still has her text thread with Eito open."
            show kaori sur b3
            "Kaori freaks out and lunges for the phone! She grabs it from my hands, but not before I manage to send a text."
            "{i}Dinner after?{/i}"
            show kaori ang b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_116.ogg"
            ki "W-Why would you text him that?!"
            "Kaori punches me on the arm."
            show kaori win b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_117.ogg"
            ki "Now he'll think I'm so... so--Ugh! The daycare is going to be so weird when I see him again!"
            show kaori ann b3
            "She's about to hit me again when her phone vibrates."
            "She freezes and grabs her phone."
            pf "What did he say?"
            show kaori cur b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_118.ogg"
            ki "{i}I would love to, Kaori!{/i}"
            show kaori smi b3
            "Kaori's cheeks are still red and another smile plays on her lips as she continues to stare at the message."
            pf "Where's my thank you?"
            show kaori ang b3
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_119.ogg"
            ki "Shut up!"
            scene black with fade
            "I laugh. We continue our workout and I don't let up the teasing. Kaori scowls anytime I mention Eito's name, but she doesn't seem as perturbed by it now that she knows how he feels about her."

        "I shouldn't interfere in her business.":
            pf "Alright, whatever you say."
            show kaori neu
            "Kaori shakes her head."
            voice "audio/voice/E4/Kaori/Kaori Arc/Kaori_event_120.ogg"
            ki "Let's get back to our workout."
            pf "Yep."
            scene black with fade
            "The rest of the workout is very productive and I set a new personal record for myself! Kaori and I will definitely have to make this a more regular thing."

    "Once we wrap up, we say our goodbyes and head our separate ways."




scene black with fade
stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4KIS2_Completed = 1