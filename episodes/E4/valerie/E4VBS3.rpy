#AFTERNOON EVENT (ROMANTIC ONLY)
label E4VBS3:

$ valHairF = "default"
$ valHairB = valHairF
$ valOut = "sCasual"

$ nikHairF = "default"
$ nikHairB = nikHairF
$ nikOut = "sCasual2"



"I dial Valerie's number… but she doesn't answer."
"Huh… I guess she's busy…"

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"I decide to study at home in the living room for a change."
scene bg homekaito main day with fade
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"When I arrive, Nikki's there!"

pf "What are you doing here?"
show nikki thi at cc with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie01.ogg"
sf "My school has an event so classes are cancelled. I wanted to get a head start on some of my essays, but…"
"She groans in frustration."
show nikki dis
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie02.ogg"
sf "None of this is making sense!"
pf "Scoot over on the couch. I'll help you."
hide nikki with dissolve
"She makes room as I begin to explain her assignment."
scene black with fade
"It doesn't take long for Nikki to understand the material and soon she's working on her own!"

"With her all set, I disappear to my room and have my own study session."
"After some time, I start losing focus. {w}I guess I'll go watch some TV or something."
scene bg homekaito main day with fade
"As I head downstairs, my steps slow as I smell the most magical scent. {w}Food, delicious food!"
"The coffee table in the living room has a beautiful bento. As I take a closer look, I can tell it was delicately made with much love. The rice is abundant with a layer of sliced meat and vegetables on the side."
"Nikki sits on the couch and beams."
show nikki neu at cc with dissolve
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie03.ogg"
sf "I made your favourite!"
pf "Not that I'm complaining, but to what do I owe this pleasure?"
show nikki smi
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie04.ogg"
sf "I just thought it'd be a nice \"thank you\" for taking your time out of your day to help me study."
pf "Please make food like this everyday."
stop music fadeout 5
"Before I can dig in, the doorbell rings. I blink at Nikki."
pf "Are you expecting anyone?"
show nikki cur
"She shakes her head."
hide nikki with dissolve
"I get up and open the door to see a smiling Valerie!"
pf "Valerie! What are you doing here?"
show valerie smi at l3 with dissolve:

voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL109.ogg"
vb "I was just in the neighborhood and thought I'd stop by."
pf "Uhh, don't you have to take a bus from campus?"
show valerie dis
play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
"She pouts."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL110.ogg"
vb "What's the matter? Can't a girl surprise her boyfriend?"

menu:
    "Yes, of course.":
        pf "Sorry, of course."
        show valerie mis
        "She winks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL111.ogg"
        vb "I'll forgive you this time."

    "I've got you in my sights.":
        "I raise an eyebrow."
        pf "Sure, but {i}this{/i} girl always has an ulterior motive."
        show valerie mis
        "Valerie smirks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL112.ogg"
        vb "You caught me."

show valerie hap
"She grins and holds up a bento box."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL113.ogg"
vb "I made a little too much food today so I thought I'd share it with a certain someone."
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL114.ogg"
vb "Knowing how you fare in the kitchen, I'm surprised you haven't starved by now."
pf "Really?"
show valerie dis
"Valerie frowns at my lack of enthusiasm."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL115.ogg"
vb "I thought you'd be a little more excited considering I made… your favourite!"
show valerie smi
"She opens the lid. Steam rises off a carefully prepared bed of rice with meat and vegetables."
pf "Seriously? You too?"
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL116.ogg"
vb "What do you mean \"too\"?"
pf "Well, Nikki actually already made me a bento. Valerie blinks when she sees Nikki."
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL117.ogg"
vb "Oh! Hi, Nikki. I didn't expect to see you here."
show nikki ske at r3 with dissolve:
    xzoom -1
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie05.ogg"
sf "Why not? This is my house too."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL118.ogg"
vb "I thought you'd be at school."
pf "They have some kind of activity today so she doesn't have classes."
"We both sit down on the couch as Nikki eyes Valerie's bento."
show nikki cur
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie06.ogg"
sf "What's that?"
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL119.ogg"
vb "Just a bento I made for my {i}boyfriend{/i}."
show nikki smi
"Nikki smiles widely."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie07.ogg"
sf "How thoughtful of you! It's a shame he won't get to taste it because he'll be eating the bento I made for my {i}brother{/i}."
show valerie hap
"Valerie matches Nikki's smile."
$ persistent.gpix[57][0] = 1
$ persistent.gpix[58][0] = 1
$ persistent.gpix[59][0] = 1

scene cg valerie dinner 1 with fade:
    xzoom .5
    yzoom .5
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL120.ogg"
vb "It does look good, but a little small. He might still be hungry afterwards! Looks like it's a good thing I brought food over after all."
"A sudden chill runs down my spine. {w}Whoa! Where did that come from?{w} I glance at Valerie and Nikki's smiles. Everyone seems to be getting along…"
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie08.ogg"
sf "Of course, I put in extra meat because I know that's his favourite part so it's very filling."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL121.ogg"
vb "Certainly not as filling as mine."
"Nikki looks at Valerie's open bento."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie09.ogg"
sf "You're right. With all that rice, mine wouldn't be able to compete."
scene cg valerie dinner 2 with dissolve:
    xzoom .5
    yzoom .5
"Valerie's smile twitches."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL122.ogg"
vb "There's just enough rice to complement the flavour of the meat."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie10.ogg"
sf "I'm sure it's very good, but I know my brother has an aversion to meat that is heavy on soy sauce, so I used my own special recipe… which he {i}loves{/i}."
scene cg valerie dinner 3 with dissolve:
    xzoom .5
    yzoom .5
"Am I imagining the electricity in the room?"
scene cg valerie dinner 2 with dissolve:
    xzoom .5
    yzoom .5
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL123.ogg"
vb "He's always enjoyed what I've made for him in the past so I know he'll love this too. Isn't that right?"

"Valerie turns to me, her smile still plastered on her face and her voice too sickly sweet. She holds up a piece of meat from her bento."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL124.ogg"
vb "Go ahead, try it!"
"Nikki's smile looks dangerous as she also holds up a piece of meat from her bento."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie11.ogg"
sf "No, you should eat mine!"
pf "Uhh…"
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie12.ogg"
sf "What's the matter? Don't you like my cooking?"
pf "Yeah, but--"
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie13.ogg"
sf "That's what I thought. I knew you'd like mine better."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL125.ogg"
vb "That's not what he said."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie14.ogg"
sf "That's what was implied."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL126.ogg"
vb "Maybe we should let him choose."
"They both turn towards me."
pf "Uhhhh…"
"I stare at the two women. Their smiles are still stuck on their faces but their eyes are staring daggers at each other."

menu:
    "Can't say no to my sister.":
        "If I go against Nikki, I will surely starve to death."
        scene bg homekaito main day with fade
        pf "Well, I think maybe I'll have Nikki's this time and I can have Valerie's later."
        show nikki hap at r3 with dissolve:
            xzoom -1
        show valerie sur at l3 with dissolve:
        "Nikki grins smugly as Valerie's smile drops."
        show nikki neu
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie15.ogg"
        sf "There's a reason why I'm working at a restaurant."
        show valerie sad
        "Valerie pouts."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL127.ogg"
        vb "I-Is that really how you feel?"
        "She turns her head away, and takes a shuddering breath."
        show valerie win
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL128.ogg"
        vb "I-I just wanted t-to do something nice for you!"
        "She hides her face in her hands as she begins to sniffle."
        show nikki cur
        pf "Whoa, wait!"
        "I pull her into a hug and she buries her face into my chest."
        pf "I didn't mean that at all!"
        show nikki ske
        "Nikki crosses her arms."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie16.ogg"
        sf "Oh please, what is this amateur hour?"
        pf "Nikki!"
        show nikki dis
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie17.ogg"
        sf "Come on, she's not even crying real tears!"
        "I glance at her as Valerie pulls away."
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL129.ogg"
        vb "Fine."
        show valerie mis
        "Valerie smirks, a mischievous twinkle in her eye."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL130.ogg"
        vb "You might have won this time, but I know one thing he'll always choose me for."
        jump E4VBS3_Kiss

    "No way am I going against my girlfriend.":
        "Even I'm smart enough to know that you always side with your girlfriend."
        scene bg homekaito main day with fade
        pf "Well, I think maybe I'll have Valerie's this time and I can have Nikki's later."
        stop music fadeout 5
        show nikki sur at r3 with dissolve:
            xzoom -1
        show valerie mis at l3 with dissolve:
        "Valerie grins smugly."

    "IT'S A TRAP!":
        "Why do I feel like this is a game where nobody wins?"
        scene bg homekaito main day with fade
        pf "They're both too good. I can't choose!"
        show nikki dis at r3 with dissolve:
            xzoom -1
        show valerie ann at l3 with dissolve:
        "Nikki frowns."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie18.ogg"
        sf "Nu uh, I'm not going to let you cop out like out."
        show valerie mis
        "Valerie smirks, a mischievous twinkle in her eye."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL131.ogg"
        vb "I know what will help him choose."

        label E4VBS3_Kiss:
        $ E4VBS3_Kissie = 1
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie19.ogg"
        sf "What?"
        show valerie hap b1 with dissolve
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL132.ogg"
        vb "This."
        "Valerie places her hands on my face and plants one long, lingering kiss on my lips."
        show nikki sur
        "As she slowly pulls away, I have to catch my breath."
        show nikki ann
        "Nikki fumes beside me. I can almost see the steam coming out of her ears."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie20.ogg"
        sf "That's not fair! You're cheating!"
        show valerie cur
        "Valerie looks innocent."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL133.ogg"
        vb "What do you mean?"
        stop music fadeout 10
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie21.ogg"
        sf "You know exactly what I mean!"
        "Nikki turns to me."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie22.ogg"
        sf "Tell her she's disqualified for cheating!"
        "I stare at Nikki in a daze, still remembering the taste of Valerie's lips."
        show valerie mis
        pf "...Come again?"

show nikki sad
"Nikki's eyes grow wide and she looks away."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie23.ogg"
sf "I see. Well, if that's how it is, then I guess you won't be needing this."
hide nikki
show valerie cur
with dissolve
"She grabs her bento and quickly heads into the kitchen."
pf "Wait! Nikki!"

menu:
    "Chase after her.":
        "I look apologetically at Valerie."
        show valerie neu
        pf "Sorry, but I need to talk to Nikki."
        "Valerie nods understandingly, looking slightly worried herself."
        hide valerie with dissolve
        "I follow Nikki into the kitchen. She quickly swipes at her eyes when she sees me."
        pf "Are you okay?"
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
        show nikki dis at r3 with dissolve:
            xzoom -1
        
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie24.ogg"
        sf "I'm fine. Shouldn't you be out there with your {i}girlfriend{/i}?"
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL134.ogg"
        vb "Hold on, Nikki."
        show valerie neu at l3 with dissolve:
        "Nikki frowns."

    "She'll get over it.":
        "Valerie and I sit in awkward silence."
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL135.ogg"
        vb "Are you going to go after her?"
        pf "No. She's just got to get used to the fact that it's not just the two of us anymore."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL136.ogg"
        vb "I don't want to be the one who comes between you two. I'm going to talk to her."
        hide valerie with dissolve
        pf "Hey, wait!"
        "Valerie gets up and heads into the kitchen. I follow after her."
        play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
        show nikki sad at r3 with dissolve:
            xzoom -1
        show valerie neu at l3 with dissolve
        "Nikki swipes at her eyes when she hears us enter. She spots Valerie and turns away."

voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie25.ogg"
sf "Come to gloat?"
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL137.ogg"
vb "No. I came to apologise."
show nikki cur
"Nikki blinks."

if E4VBS3_Kissie == 1:
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL138.ogg"
    vb "You're right, what I did was a cheap trick."

show valerie sad
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL139.ogg"
vb "To be honest, I'm jealous of you."
voice "audio/voice/MISSING/BATCH7/Nikki_final_missed15_01.ogg"
sf "Really?"
"Valerie smiles softly."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL140.ogg"
vb "You and your brother have a special bond that no one, not even I, can ever replace. I'm envious of how close you two are..."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL141.ogg"
vb "I'd like to get to know your brother better, but not if that's at the cost of your friendship."
show nikki cur b1 with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL142.ogg"
vb "He's really lucky to have such a caring sister who looks out for him. If I had a sister, I'd want for her to be like you too."
show nikki wor b1
"Nikki looks down and shuffles her feet as she thinks about Valerie's words."
show nikki sad b1
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie27.ogg"
sf "I suppose I overreacted a little bit."
show valerie mis
stop music fadeout 5
"Valerie grins."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL143.ogg"
vb "Your bento looked so good… do you think maybe I could try it?"
show nikki smi
"Nikki brightens up immediately."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Valerie28.ogg"
sf "Only if I get to try yours!"
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL144.ogg"
vb "Of course!"
pf "Hey wait--what about me?"
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"They both glance at me, then start giggling."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL145.ogg"
vb "You can have the leftovers."
hide valerie
hide nikki
with dissolve
"The girls walk out into the living room together."
pf "How did I go from two bentos to no bentos?"
"Shaking my head, I join them."

"Thankfully, the girls changed their minds and all three of us shared the bentos. I am so lucky to be surrounded by two amazing cooks."
"Once Valerie and Nikki found common ground, the two of them would not stop chatting about fashion, make-up, and all things \"girl\"!"
"I can't help but smile as I watch them."

"After a few hours, Valerie says she has to go back. We walk to the door."
show valerie smi at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL146.ogg"
vb "Exams are next week."
pf "I know."
show valerie cur
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL147.ogg"
vb "We should go out and do something fun before the stress gets to us."
pf "Like what?"
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL148.ogg"
vb "Like the amusement park!"
"I blink."
pf "There's an amusement park in Isokaze?"
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL149.ogg"
vb "It's a few hours away, but I hear it's worth it."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL150.ogg"
vb "Besides, what's a better way to let loose than to fly down a roller coaster?"

menu:
    "Those things are risky.":
        $ E4VBS3_Nofancoaster = 1
        pf "No way am I going to get on those death traps."
        show valerie mis
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL151.ogg"
        vb "Oooh, I had no idea you got scared so easily."
        pf "Hey! I have a valid reason to be \"concerned\"!"
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL152.ogg"
        vb "Maybe the kid's section would be more your level."
        pf "Very funny."
        "She pouts and touches my arm."
        show valerie sad
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL153.ogg"
        vb "Does that mean you don't want to go?"
        "A whole day alone with Valerie? I'd be crazy to pass that up!"
        pf "I didn't say that."
        show valerie smi
        "She smiles."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL154.ogg"
        vb "How about this weekend then?"
        pf "Let's do it."

    "Sign me up!":
        pf "Sounds like fun! How about this weekend?"
        show valerie mis
        "She winks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL155.ogg"
        vb "It's a date."

scene black with fade
"After a quick kiss goodbye, she leaves. Valerie's visit was unexpected, and for a while it was touch and go, but I'm glad my two best girls have found a way to get along."
"I head back inside, excited about my weekend plans."


stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4VBS3_Completed = 1