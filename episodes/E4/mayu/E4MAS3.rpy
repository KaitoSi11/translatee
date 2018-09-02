##
label E4MAS3:
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "motel"
    
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    scene bg homekaito myroom day with fade
    
    "My alarm wakes me and I get out of bed feeling exhilarated. It's been a long time since I've gone paintballing and I could use the distraction!"
    "I get ready for the day and eat a hearty breakfast. I can't skimp on the most important meal of the day if I want to win!"
    "I hope Mayu is ready for me to get her. I better give her a call."
    "She picks up almost immediately."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-59.ogg"
    ma "Hello?"
    pf "Hey, Mayu. Are you ready?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-60.ogg"
    ma "As ready as I'll ever be."
    "Her voice betrays her confidence."
    pf "You okay?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-61.ogg"
    ma "Yeah… I just hope I'll be okay at it."
    
    menu:
        "You'll be great!":
            pf "Someone with as much tactical knowledge as you will be a natural!"
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-62.ogg"
            ma "I hope so!"
        
        "It takes some practice.":
            pf "It might take you a little while to get warmed up, but once you get the hang of it the rest just falls into place."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-63.ogg"
            ma "I suppose that makes sense."
        
        "Who cares? It's fun.":
            pf "So what if you're bad? The point is to have fun."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-64.ogg"
            ma "Y-Yeah! You're right."
    
    pf "So are you ready for me to come pick you up?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-65.ogg"
    ma "Yes!"
    "She sounds much more certain this time."
    pf "Okay, be there soon."
    
    scene black with fade
    
    "After we hang up, I hop on my bike and head to ACE."
    
    "Mayu waits for me outside her dorm and greets me with a smile. Once she's situated on my bike, we drive off."
    "I went online last night and was surprised to find that there was a paintballing range in Isokaze. It's a few hours away, but didn't look like too bad of a drive. I pre-programmed the GPS coordinates into my helmet, so once we hit the road, it was a smooth ride to the range."
    
    "We arrive at a wooded expanse."
    
    scene bg vacation nature day with fade
    "There are trees stretching as far as the eye can see and a cabin close to the parking lot. That must be where the registration desk is."
    "A good number of people exit the cabin and head towards the trees.{w} That's encouraging! It means a better game for us."
    "Mayu seems intimidated by all the people, so I throw a reassuring arm around her shoulders and squeeze gently. She glances up at me and smiles."
    pf "Let's go inside and get our gear."
    
    $ mayOut = "motel"
    
    show mayu neu at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-66.ogg"
    ma "Okay."
    hide mayu with dissolve
    "We speak with the clerk and receive our suits, glasses, vests, paintball guns, and ammo. We've been placed on the blue team and will be fighting against the red team."
    "Mayu looks wide-eyed at all the gear in her arms."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-67.ogg"
    ma "This seems way more intense than I thought."
    pf "It can be intense, but not as much as these items make it seem."
    "After getting changed, we meet up with the rest of our team. With the exception of one other girl, Mayu is the only girl on the team. The rest are guys who look to be in their 20's."
    "After introductions, we huddle to discuss plans."
    
    
    $ mayOut = "paintball no gloves"
    
    show mayu neu at l3
    show receptionist extra at r3:
        xzoom -1
    with dissolve
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/13.ogg"
    team1m "So the objective for this game is to capture the other team's flag, which means they're also going to go for our flag."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/14.ogg"
    team1m "Have any of you played before?"
    "There's a mixture of responses. It seems like most of the people on our team are newbies too."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/15.ogg"
    team1m "That's fine. It's not hard to pick up. We'll need some people defending and others on offense."
    "Mayu leans into me."
    show mayu cur
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-68.ogg"
    ma "Which side do you think we should be on?"
    pf "With your sharpshooting experience, I think we could be a huge benefit for the defensive team."
    show mayu neu
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-69.ogg"
    ma "I can do that."
    pf "If we see the offensive side needs help, we can hop in then too."
    stop music fadeout 5
    hide receptionist extra
    hide mayu
    with dissolve
    "The team lead starts getting everyone's preferences and splits people up."
    
    show mayu neu at cc with dissolve
    "Once everyone's been split up, we take a look at field. For the most part, we're all out in open space with sparse tree cover, which means our flags have no cover either. That makes it harder for us to defend, but also easier for us to spot enemy advancement."
    
    pf "If we see someone on the enemy team, we'll shoot them with our paintballs. If any paint gets on them it means they're out."
    "Mayu grins."
    show mayu smi
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-70.ogg"
    ma "That sounds pretty easy."
    pf "But that also means that if we get hit, we're out too."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-71.ogg"
    ma "Okay."
    pf "And don't shoot your own teammate or they're out too!"
    "Her eyes widen and she nods."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-72.ogg"
    ma "Got it!"
    pf "And that's basically how you play."
    "She giggles."
    show mayu hap
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-73.ogg"
    ma "Paintballing 101."
    hide mayu with dissolve
    
    "As we get into place, the game begins."
    play music "audio/music/Fight Song 1 (GAME VERSION).ogg" fadein 7
    "Mayu and I stake out an area a little further away from the flag, but which keeps the flag in plain view. If anyone tries to get close, they'll be an open target! We bank on the fact that we aren't directly in the line of sight and won't be spotted right away."
    "Other teammates crowd closer to the flag, hoping to be the one who shoots first instead of getting shot."
    "As expected, the other team begins trickling into view. They dart from cover to cover, hoping to stay hidden for as long as possible. It's easy to tell the more inexperienced people from the experienced as they get taken out almost immediately."
    
    $ mayOut = "paintball"
    
    show mayu neu at cc with dissolve
    "Mayu steadies her gun and focuses her aim. Every time she shoots, she hits her target square in the chest! Even before the rest of us have warmed up, she's already taken out every single attacker she sees! {w}If she keeps this up there won't be any players for the rest of us to attack."
    "I stare at her in awe… she's even more awesome out here on the field than in our GEAR matches!"
    "Once people figure out where her shots are coming from, we quickly abandon our posts and begin running. Mayu continually shoots a stream of paintballs, taking out multiple targets. She's even more lethal in motion!"
    "One of the attackers escapes her view though, and heads straight for the flag!"
    
    #QTE
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E4MAS3_Fumble")
    
    menu:
        "Trip...":
            jump E4MAS3_Fumble
        "Shoot!":
            jump E4MAS3_Steady
        "Stay...":
            jump E4MAS3_Fumble
        "Miss...":
            jump E4MAS3_Fumble
        "Aim!":
            jump E4MAS3_Steady
    
    label E4MAS3_Steady:
        $ renpy.hide_screen ("timer_scr")
        "I steady my weapon and pull the trigger. The attacker's red vest is stained with a large blue splat."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-74.ogg"
        ma "Nice one!"
        pf "Thanks!"
        jump E4MAS3_Continued
    
    label E4MAS3_Fumble:
        $ renpy.hide_screen ("timer_scr")
        "I fumble my weapon and the attacker continues advancing!"
        pf "Mayu!"
        "She whips around and spots him, then fires, but she's not the only one who's seen him. A torrent of paintballs splashes the poor guy as everyone shoots."
        jump E4MAS3_Continued
    
    label E4MAS3_Continued:
        "Mayu has this place on lockdown and the people coming to steal our flag are fewer and fewer as Mayu meticulously takes them out. I glance at the other side of the field and see most of our team members have paint splattered on them."
    
    pf "Mayu, it looks like our offense could use some help. What do you say?"
    "She nods."
    hide mayu with dissolve
    
    "We take off running towards the enemy base. We dart from cover to cover, hoping to stay hidden for as long possible. While under cover, Mayu aims her weapon and shoots at any defenders in sight."
    show mayu smi at l3 with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-75.ogg"
    ma "Let's take out as many as we can before we have to dive in."
    pf "Right!"
    "She expertly aims at her targets and hits them square in the chest. Like a machine, she fires shot after shot. Once the defenders realise where the shots are coming from, we quickly abandon our hiding spot and sprint towards the flag."
    hide mayu with dissolve
    "As a moving target we're harder to hit, and we use that to our advantage. My aim suffers a bit and there are a few times where I miss my mark, but Mayu doesn't seem affected. For every one of my misses, she has me covered."
    pf "I'm going to make a grab for the flag. You cover me!"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-76.ogg"
    ma "Got it!"
    "Trusting Mayu to have my back, I lower my weapon and make a break for it!"
    
    if MCStory != 1:
        menu:
            "Grab!":
                $ renpy.hide_screen ("timer_scr")
                jump E4MAS3_Athletic
            "Miss...":
                jump E4MAS3_Miss
            "Run...":
                jump E4MAS3_Miss
            "Swipe!":
                $ renpy.hide_screen ("timer_scr")
                jump E4MAS3_Athletic
            "Cover...":
                jump E4MAS3_Miss
    
    #if athletic jump to grab or swipe:
    
    else:
        label E4MAS3_Athletic:
            $ renpy.hide_screen ("timer_scr")
            "Weaving among the defenders, I zero in on the bright red flag. Without slowing my pace, I reach out my hand and grab it then make a wide turn and run towards the group."
            "My breath comes out in ragged gasps and my legs burn but I refuse to slow down. Suddenly, Mayu yells."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-77.ogg"
            ma "Look out!"
            "There's a paintball heading my way!"
            
            # QTE
            $ qtebase = 3
            $ qtetotal = qteath + qtebase
            $ t_var = qtetotal
            show screen timer_scr(place="E4MAS3_Derp")
            
            menu:
                "Freeze...":
                    jump E4MAS3_Derp
                "Dodge!":
                    jump E4MAS3_Dodge
                "Derp...":
                    jump E4MAS3_Derp
            
            label E4MAS3_Derp:
                $ renpy.hide_screen ("timer_scr")
                "The paintball comes barreling towards me and I can't move in time. As I brace for the impending impact, the team lead jumps in front of me and takes the shot instead."
                pf "I owe you one."
                "He shakes his head."
                voice "audio/voice/E4/HOT MALE 4!!!/Mayu/16.ogg"
                team1m "Go! Run!"
                pf "Right!"
                "Mayu takes out the attacker and stays a step behind me."
                jump E4MAS3_Chest
            
            label E4MAS3_Dodge:
                $ renpy.hide_screen ("timer_scr")
                "I skid out of the way, and Mayu takes out the attacker. Then I continue racing back to base, Mayu on my heels."
                jump E4MAS3_Chest
            
            label E4MAS3_Chest:
                "My chest feels like it's about to burst, but I refuse to lessen my pace. I can see our base in the distance and through sheer force of will, I increase my speed. Mayu continues to cover me. I focus on closing the distance between me and the base one step at a time. When my foot steps over the line, we make it safely back, signaling the end of the game."
                jump E4MAS3_Victory
    
    
    label E4MAS3_Miss:
        $ renpy.hide_screen ("timer_scr")
        "I zero in on the bright red flag and reach my out my hand. My fingers brush against the cloth, but ultimately it slips through my grasp."
        pf "No!"
        "Before I can turn back, the team lead darts up and grabs the flag."
        voice "audio/voice/E4/HOT MALE 4!!!/Mayu/17.ogg"
        team1m "I've got it!"
        pf "We'll cover you!"
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-78.ogg"
        ma "Right!"
        "We stay on his heels as he races back towards base. My chest feels like it's about to burst, but I don't lessen the pace."
        "Ignoring the burn in my legs, I focus on the space around us, alert for any enemy defenders. Mayu seems to effortlessly trail behind him as she continues firing shot after shot."
        "The team lead pumps his legs and uses his last few ounces of strength to make it back to base, signaling the end of the game."
        jump E4MAS3_Victory
    
    label E4MAS3_Victory:
        stop music fadeout 4
        "Everyone gathers around in high spirits and congratulates each other. Once the initial high of winning wears down, the focus turns to Mayu."
        
        $ mayOut = "paintball no gloves"
        
        show mayu ner at l3
        show receptionist extra at r3:
            xzoom -1
        with dissolve
        
        "She glances nervously around her."
        voice "audio/voice/E4/HOT MALE 4!!!/Mayu/18.ogg"
        team1m "What exactly was that out there?"
        "Her eyes grow wide."
        show mayu sad
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-79.ogg"
        
        ma "I-I'm sorry! I've never played before!"
        "Everyone wears a mixture of shock and awe."
        show mayu cur
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-80.ogg"
        ma "Did I do okay?"
        play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
        voice "audio/voice/E4/HOT MALE 4!!!/Mayu/19.ogg"
        team1m "\"Okay\"? You were incredible!"
        "Mayu blinks."
        show mayu sur
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-81.ogg"
        ma "O-Oh!"
        show mayu smi b2 with dissolve
        "She blushes as the compliment sinks in."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-82.ogg"
        ma "Thank you."
        "I pull her into a hug and grin."
        pf "You single-handedly demolished basically every enemy on that field."
        show mayu ner b2
        "She blushes deeply."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-83.ogg"
        ma "I'm not sure about that."
        pf "If it weren't for you, we never would have made it back! And you didn't let a single person get close to our flag!"
    
    show mayu smi b1 with dissolve
    "Mayu beams as the compliments keep flowing in. I knew she was dangerous during our GEAR matches, but I had no idea just how lethal a sharpshooter she really was. {w}She really is one of a kind."
    
    "Everyone gets ready to begin the next match."
    pf "Ready for round two?"
    "Mayu smiles and nods."
    
    scene black with fade
    "We play a few more rounds and try out a variety of modes. No matter what game type we choose, Mayu continues to demolish everyone on the field."
    "At one point, the enemy team was allowed more players in the hopes that it would balance out the teams, but all it did was provide more targets for Mayu to hit."
    
    stop music fadeout 5
    "The sun is beginning to set by the time we're done. After we get changed and return our gear, we go into the cafe next door."
    
    scene bg campus cafe dusk with fade
    $ mayOut = "motel"
    $renpy.pause(.5)
    pf "So, how was it today?"
    show mayu hap at cc with dissolve
    "Her face lights up."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-84.ogg"
    ma "That was so much fun! I can't believe I've never done it before."
    pf "Me neither. You rocked it."
    show mayu smi
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-85.ogg"
    ma "Next time, I'd like to try the one game where everyone is pit against each other."
    "I grin."
    pf "I don't know how I'd feel having to play against you. I think I like having you on my team better."
    show mayu b1 with dissolve
    "She blushes."
    
    scene black with dissolve
    "We finish eating and get back on my bike to make the drive back home."
    
    scene bg travel openroad dusk with fade
    "I turn the engine, but instead of starting, my bike makes a weird noise."
    "Mayu tenses against me."
    show mayu cur at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-86.ogg"
    ma "Um, what's that sound?"
    pf "I don't know…"
    "The noise grows louder as I try again, then I hop off. After an inspection, I still don't know what the damage is."
    pf "I need to take my bike to a garage. I'm not sure what the problem is and don't want to put us in danger by driving home."
    show mayu sad
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-87.ogg"
    ma "I understand."
    "I check my GPS for the nearest garage when one of our paintballing teammates waves."
    show mayu neu
    show receptionist extra at l3 with dissolve
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/20.ogg"
    team1m "Great game today, guys! You heading home now?"
    pf "We would, but I'm having trouble with my bike. Do you know if there's a place nearby I can go to get it fixed?"
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/21.ogg"
    team1m "There's one not too far away actually. I can take over if you like."
    "Mayu smiles."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-88.ogg"
    ma "I hope that won't be too much trouble!"
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/22.ogg"
    team1m "Not at all. We can hook it up to my truck."
    scene black with fade
    "I help him hook up my bike and then Mayu and I ride with him in his truck as he drops us off at the nearest garage."
    scene bg homekaito garage day with fade
    "When we arrive, the mechanic does a quick check and hands over an evaluation sheet."
    "Hm… it seems like it might be a transmission issue, which I think would be in line with the weird sounds."
    pf "Can you fix it now?"
    show bully2 extra at cc with dissolve
    voice "audio/voice/E4/Aludian Engineer/E4/Mayu/1.ogg"
    mech1 "We have a few cars ahead of you that we need to take care of first."
    pf "It's just that we're kind of in a rush…"
    voice "audio/voice/E4/Aludian Engineer/E4/Mayu/2.ogg"
    mech1 "Sorry, earliest I can get it back to you is tomorrow morning."
    "I sigh. I can either try to drive home, which would be a terrible idea, or spend the night here and go back tomorrow morning."
    pf "Alright then."
    hide bully2 extra with dissolve
    "I return to Mayu and relay what the mechanic said."
    show mayu neu at cc with dissolve
    pf "We're still over an hour away from home. I suppose technically we could taxi home, but I don't want to leave my bike here unattended…"
    "Mayu shakes her head."
    show mayu ner
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-89.ogg"
    ma "It doesn't make sense to taxi all the way home and then come back again in the morning. That'd be expensive too."
    "I nod."
    pf "I'm going to find a motel. You don't have to stay with me though. Maybe we can call someone to pick you up?"
    show mayu sad
    "Mayu looks worried."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-90.ogg"
    ma "I-I don't know… it's really late and I don't want to disturb anyone at this hour..."
    "Mayu keeps shooting glances at me. I think I understand what she's hinting at..."
    pf "Do... you want to stay here with me?"
    show mayu smi b1 with dissolve
    "She blushes and nods."
    pf "Alright."
    scene black with fade
    "I find a decent-looking motel within walking distance from the garage. There's weather damage on the bricks outside but otherwise it seems to be in good condition."
    "When we walk in, the lobby is small and conservatively decorated, but the front desk agent is helpful and the people who walk by the lobby seem to be normal."
    "I walk up to the front desk."
    
    menu:
        "Book one room.":
            pf "Do you have a room available for the night?"
            "The agent clicks through her system and nods."
            "I glance over at Mayu. {w}On second thought, I don't want to make her uncomfortable…"
            pf "Actually…"
            jump E4MAS3_2Rooms
        
        "Book two rooms.":
            label E4MAS3_2Rooms:
                pf "Do you have two rooms available for the night?"
                "The front desk agent clicks through her system and nods."
                recep "Let me get that taken care of for you."
                "We wait patiently as she finds us rooms and hands us our keys."
    
    "Mayu and I head upstairs to our rooms. Luckily, they're right next to each other!"
    
    scene bg vacation hotel night with fade
    show mayu ner at cc with dissolve
    "She glances at me and hovers in front of her door but doesn't go in."
    
    if MCStory == 3:
        "I don't think she's ready to go to bed yet."
        pf "Do you want to come in and chat?"
        show mayu smi
        "She smiles."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-91.ogg"
        ma "Sure!"
        
    else:
        show mayu cur
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-92.ogg"
        ma "Are you going to go to bed?"
        "...If Mayu's asking me this, does that mean she wants to hang out more?"
        pf "Not necessarily… are you?"
        "She shakes her head."
        pf "Want to come in and chat?"
        show mayu smi
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-93.ogg"
        ma "Yes!"
    
    hide mayu with dissolve
    "I open the door for her and she smiles her thanks as she walks into the room, then settles onto the bed. I sit beside her."
    pf "Sorry today didn't go quite as planned…"
    "She places a hand over my own."
    show mayu smi at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-94.ogg"
    ma "It's okay, I had a lot of fun."
    show mayu smi b2 with dissolve
    "She looks away and blushes."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-95.ogg"
    ma "I always have fun when I'm with you…"
    "I squeeze her hand."
    pf "Me too."
    stop music fadeout 20
    scene black with fade
    "We continue to chat about everything and nothing and the hours tick by. Soon, I'm stifling yawns."
    
    scene bg vacation hotel night with fade
    show mayu smi at cc with dissolve
    
    pf "We should probably get some rest since we'll be heading out early in the morning…"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-96.ogg"
    ma "Okay."
    show mayu ner
    "She looks worried and doesn't move."
    pf "Hey, are you alright?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-97.ogg"
    ma "Y-Yeah…"
    "But she looks far from alright. She sits on my bed with her eyes lowered."
    pf "Seriously, are you okay? What's wrong?"
    show mayu b1 with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-98.ogg"
    ma "I-It's really embarrassing…"
    pf "Hey, come on, it's me. You don't have to be embarrassed."
    "She shifts uncomfortably, then speaks."
    show mayu sad b1
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-99.ogg"
    ma "I'm scared of being alone."
    "I blink."
    pf "But don't you live alone?"
    show mayu ner
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-100.ogg"
    ma "It's not the same. I'm in a dorm with a lot of familiar people so I don't feel alone."
    show mayu sad
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-101.ogg"
    ma "...This place is a little scary…"
    pf "Do you want to stay here with me?"
    show mayu cur b2 with dissolve
    "Her cheeks turn pink and she looks away. Then she nods."
    pf "Alright."
    
    menu:
        "Time to sleep on the floor then!":
            "I grab a bunch of pillows from the bed and I'm about to throw them on the ground when Mayu stops me."
            show mayu sur b2 with dissolve
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-102.ogg"
            ma "W-Wait! What are you doing?"
            pf "You can have the bed. I'll take the floor."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-103.ogg"
            ma "The floor looks really uncomfortable though…"
            "I shrug."
            play music "audio/music/You and I (GAME VERSION).ogg" fadein 7
            show mayu ner b2 with dissolve
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-104.ogg"
            ma "Y-You can stay on the bed if you want."
            pf "So we'll be sharing the bed then. Is that okay?"
            "Her blush deepens but she meets my gaze."
        
        "We can share the bed.":
            "I lay down on my side of the bed."
            "Mayu's eyes widen."
            show mayu sur b2 with dissolve
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-105.ogg"
            ma "O-Oh! We're sharing the bed?"
            pf "Well, there's only one…"
            pf "I can sleep on the floor if it makes you more comfortable."
            "She blushes."
            show mayu ner b2 with dissolve
            play music "audio/music/You and I (GAME VERSION).ogg" fadein 7
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-106.ogg"
            ma "I-It's okay. We can share the bed."
            pf "Are you sure?"
    
    show mayu cur b2 with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-107.ogg"
    ma "It's okay for boyfriends and girlfriends to do that, right?"
    pf "Right."
    scene black with fade
    "I gently crawl beneath the covers as Mayu curls up on her side."
    $ persistent.gpix[47][0] = 1
    scene cg mayu motel 1 with Dissolve(2.0):
        xzoom .5
        yzoom .5
    $renpy.pause(.5)
    "She faces me with a smile, then shivers slightly."
    
    menu:
        "Warm her up with a cuddle.":
            "I scoot closer to her. Mayu tenses up as she senses my approach so I stop."
            "Instead, I gently rub her arm. Before I can pull way, Mayu takes my hand into hers and smiles."
        
        "Respect her personal space.":
            pf "Are you cold?"
            "Mayu nods, then to my surprise she reaches for my hand and holds it against her."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-108.ogg"
            ma "B-But this makes a little better... if you are okay with it..."
            "I smile and nod."
    
    "She's such a different person from when we first met, but also the same. She has the same qualities that I love but she's learned how to come out of her shell a little more and is beginning to embrace who she is."
    "She's smart, with a quiet strength that surrounds her like an invisible force, drawing me closer to her. The more time I spend with her, the more reluctant I am to leave."
    
    "I'm completely head over heels for her."
    
    "Mayu closes her eyes and uses my arm as her pillow."
    
    stop music fadeout 5
    "I can't help but grin, then close my eyes too and enjoy the peacefulness of her company. Mayu's breathing slows and steadies. I think she's fallen asleep and I drift off to the sleep with her."
    scene black with Dissolve(2.0)
    $renpy.pause(1.0)
    #
    "..."
    play ambient "audio/ambience/Morning.ogg" fadein 2
    "....."
    
    
    scene bg vacation hotel day with fade
    "A gentle shake jolts me awake. I blink open my eyes and am greeted by Mayu's kind smile."
    show mayu smi at cc with dissolve
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-109.ogg"
    ma "Time to wake up."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-110.ogg"
    ma "We have to go get your bike."
    pf "My bike?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-111.ogg"
    ma "Yup, it's at the garage, remember?"
    "As the thick fog of sleep slowly lifts, I remember… my bike!"
    pf "Right! Hopefully it's fixed by now."
    scene black with fade
    "I crawl out of bed and freshen up a bit in the bathroom. Once Mayu and I are ready, we walk over to the garage, where my bike is waiting for pickup. {w}I give it a quick once over. It seems okay..."
    stop ambient fadeout 2
    "After turning my engine, the bike roars to life. Satisfied, Mayu and I hop on and we make the drive back to ACE Academy."
    
    "I drop her off at her dorm, and Mayu carefully slides off my bike."
    scene bg campus building day with fade
    show mayu smi at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-112.ogg"
    ma "Thanks again for taking me out."
    pf "Thanks for putting up with me."
    show mayu hap
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-113.ogg"
    ma "It was a lot of fun… maybe we can do it again."
    pf "Of course!"
    show mayu smi b2 with dissolve
    "She smiles."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-114.ogg"
    ma "I'll see you later."
    hide mayu with dissolve
    "She waves goodbye, and I watch her disappear into her dorm."
    "Once she's out of sight, I drive home."
    
    scene black with fade
    stop music fadeout 3
    stop ambient fadeout 3
    $renpy.pause(2.5)
    $ E4MAS3_Completed = 1
    jump E4D7S1