#EVENING
label E4SSS1:
$ E4SSS1_Completed = 1


$ shoOut = "sCasual"

"Just as I decide what I want I to do, I get a phone call from Shou."
pf "What's up, broseph?"
voice "audio/voice/E4/Shou/Shou Arc/1 Copy.ogg"
ss "NO."
"Geez! I pull the phone away from my ear."
pf "What do you mean \"no\"?"
voice "audio/voice/E4/Shou/Shou Arc/2 Copy.ogg"
ss "You can't call me \"broseph\"! Broseph is your name, Broseph."
pf "Uhh… okay... {w}What's up?"
voice "audio/voice/E4/Shou/Shou Arc/3 Copy.ogg"
ss "What are you doing this fine evening?"
pf "I don't have any specific plans."
voice "audio/voice/E4/Shou/Shou Arc/4 Copy.ogg"
ss "Excellent! I'll meet you at the Isokaze park."
pf "What's going on at the park?"
voice "audio/voice/E4/Shou/Shou Arc/5 Copy.ogg"
ss "You'll see! See you in a few!"
"He hangs up before I can pry for more."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3
"Well, whatever it is, if Shou's excited then it has got to be fun! {w}I hop on my bike and drive to the park."


"Tantalising scents of food waft towards the street, enticing passersby. As I search for a parking space, the park is illuminated with hanging lanterns and packed full of stalls. Is this some type of festival?"

scene bg isokaze park day with fade

"Shou lingers on the outskirts of the park, and runs over to me."
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
show shou smi at cc with dissolve

voice "audio/voice/E4/Shou/Shou Arc/6 Copy.ogg"
ss "There you are, broseph!"
pf "What's all this?"
show shou hap
voice "audio/voice/E4/Shou/Shou Arc/7 Copy.ogg"
ss "It's a festival, of course!"
pf "Yeah, but which one?"
"He looks incredulous."
show shou cur
voice "audio/voice/E4/Shou/Shou Arc/8 Copy.ogg"
ss "Geez, you don't know?!"
pf "...No, should I?"
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/9 Copy.ogg"
ss "Of course! Everyone knows it's the festival of dangos!"
pf "...You have no idea, do you?"
voice "audio/voice/E4/Shou/Shou Arc/10 Copy.ogg"
ss "I just told you. They sell all kinds of dango here."
pf "But why is there even a festival where they can sell dango?"
"He blinks."
voice "audio/voice/E4/Shou/Shou Arc/11 Copy.ogg"
ss "Does it matter?"
show shou hap
voice "audio/voice/E4/Shou/Shou Arc/12 Copy.ogg"
ss "Now come on!"
pf "Wait, aren't we going to wait for the others?"
"Shou scratches the back of his head."
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/13 Copy.ogg"
ss "This might just be a two man operation..."


menu:
    "Sounds good to me!":
        "I nod."
        pf "Just us guys? I'm game."

    "...You have a girlfriend.":
        pf "Uh, wouldn't you prefer going with you know..."
        if mayrelatonship == 0:
            pf "...Mayu?"
        else:
            pf "...Hitomi?"
        jump E4SSS1_GFConverge

    "...I have a girlfriend." if valrelatonship == 1 or kaorelatonship == 1 or yuurelatonship == 1 or mayrelatonship == 1:
        pf "Umm, excuse me, I have a girlfriend."
        "Shou shakes his head."
        show shou thi
        voice "audio/voice/E4/Shou/Shou Arc/14 Copy.ogg"
        ss "And she won't let you hang out with your guy friends? That's a shame... I didn't think you'd get whipped so quickly."
        pf "Hey! I didn't say that."
        show shou mis
        voice "audio/voice/E4/Shou/Shou Arc/15 Copy.ogg"
        ss "You certainly implied it! I have a girlfriend too, remember? You don't see shackles on me!"
        pf "Is she not joining?"

        label E4SSS1_GFConverge:
        show shou sur
        voice "audio/voice/E4/Shou/Shou Arc/16 Copy.ogg"
        ss "You're joking right?"
        show shou dis
        voice "audio/voice/E4/Shou/Shou Arc/17 Copy.ogg"
        ss "It's reading week. She has me constantly studying and studying only!"
        show shou thi
        voice "audio/voice/E4/Shou/Shou Arc/18 Copy.ogg"
        ss "It's like being on house arrest, man. I barely managed to escape."
        "He waves his arms around for emphasis."
        pf "I mean, what she's doing isn't necessarily bad..."
        show shou smi
        voice "audio/voice/E4/Shou/Shou Arc/19 Copy.ogg"
        ss "I know. But sometimes it's good to just recharge the mental battery, y'know? I figured the others would get on my case but I can trust you, broseph."
        pf "Sounds more like you thought I wouldn't be studying."
        show shou hap
        voice "audio/voice/E4/Shou/Shou Arc/20 Copy.ogg"
        ss "Was I wrong?"
        pf "...I wouldn't say that."
        "He grins."

show shou smi
voice "audio/voice/E4/Shou/Shou Arc/21 Copy.ogg"
ss "Then let's get started! The adventures of Broseph and Shou!"
"I nod. Shou seems to be in an extra good mood."
"We enter the throng of people and browse the different stalls. This area sells all sorts of crafts and clothing. {w}A small doll dressed in a fitted kimono catches my attention. I stop Shou and inspect it further. The wooden doll has hair as black as night and a dainty face with blushing cheeks and red lips."

if valrelatonship == 1 or kaorelatonship == 1 or yuurelatonship == 1 or mayrelatonship == 1:
    if valrelatonship == 1:
        "Maybe Valerie would like this…"
    elif kaorelatonship == 1:
        "Maybe Kaori would like this…"
    elif yuurelatonship == 1:
        "Maybe Yuuna would like this…"
    elif mayrelatonship == 1:
        "Maybe Mayu would like this…"

    menu:
        "Buy it!":
            pf "How much for this?"
            "The vendor names his price and I pay it."
            "Shou cautiously watches the transaction."
            show shou cur
            voice "audio/voice/E4/Shou/Shou Arc/22 Copy.ogg"
            ss "Interesting choice… Is that a new thing you're into?"
            pf "It's a souvenir for my girlfriend."
            show shou sur
            "Shou's eyes go wide."
            voice "audio/voice/E4/Shou/Shou Arc/23 Copy.ogg"
            ss "What! You can't go buying souvenirs!"
            pf "Why not?"
            show shou thi
            voice "audio/voice/E4/Shou/Shou Arc/24 Copy.ogg"
            ss "Because now I'll have to buy one too!"
            pf "Sure, you can get one too."
            voice "audio/voice/E4/Shou/Shou Arc/25 Copy.ogg"
            ss "No, not this. I can't get the same one as you. She might find out and then she'd be upset."
            pf "Okay, then we'll look for something else."

        "Don't buy it.":
            "Hmm, this isn't really her style. I'll keep an eye out for something else."

else:
    pf "Hey, Shou!"
    show shou cur
    voice "audio/voice/E4/Shou/Shou Arc/26 Copy.ogg"
    ss "What?"
    pf "Look at this. What do you think?"
    "He glances at the doll and gives me a strange look."
    voice "audio/voice/E4/Shou/Shou Arc/27 Copy.ogg"
    ss "It's… fine?"
    pf "Do you think Mayu would like that?"
    voice "audio/voice/E4/Shou/Shou Arc/28 Copy.ogg"
    ss "Ohhhh…"
    "He looks thoughtful."
    show shou hap
    voice "audio/voice/E4/Shou/Shou Arc/29 Copy.ogg"
    ss "Hmm… actually… she might!"
    pf "I'm sure she'd be happy if you brought her back a souvenir."
    show shou smi
    voice "audio/voice/E4/Shou/Shou Arc/30 Copy.ogg"
    ss "Yeah!"
    show shou cur
    voice "audio/voice/E4/Shou/Shou Arc/31 Copy.ogg"
    ss "No, wait. Then she'll know I wasn't studying."
    pf "She's going to find out no matter what. At least this way you can say you were thinking about her."
    show shou hap
    voice "audio/voice/E4/Shou/Shou Arc/32 Copy.ogg"
    ss "You're right! Smart thinking, broseph."
    "Shou asks the vendor the price of the doll and pays it, then happily turns away."

show shou smi
stop music fadeout 5
voice "audio/voice/E4/Shou/Shou Arc/33 Copy.ogg"
ss "Ready for some food?"
pf "Always."
voice "audio/voice/E4/Shou/Shou Arc/34 Copy.ogg"
ss "That's what I like to hear!"
hide shou with dissolve
"We move away from the crafts area and straight into the sea of small eats. Shou can't decide on what to order to ends up ordering one of each item! His arms are full of more dango than one man can eat! I manage to stop him before he applies this same tactic to each vendor and convince him to eat what we have first."
"We sit down along the edge of the park at the picnic tables. As we settle in, a set of twins approaches us."

show shou cur at l3 with dissolve
show studentF extra at cc
show studentF2 extra at r3
with dissolve
play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
voice "audio/voice/E4/Shou_FlirtyGirl1/FlirtyGirl_01.ogg"
flirtyg1 "Hey boys, are these seats taken?"
"Although their faces are nearly identical, one girl has stick straight hair which flows in a glossy waterfall down her back and ends right above her ample bottom. The second girl plays with her curls and lets them bounce between her full bosom."
pf "Uh…"
"They flash us smiles, revealing cute dimples, then sit across from us and set down their drinks."
voice "audio/voice/E4/Flirty Girl 2/E4/Shou/1.ogg"
flirtyg2 "It's really nice of you to save us seats."
"They seem to be around our age. The girls look at Shou with interest as they play with the straw in their drinks."
voice "audio/voice/E4/Shou_FlirtyGirl1/FlirtyGirl_02.ogg"
flirtyg1 "Do you go to ACE?"
"Considering ACE is the only university around here, it's not an unusual guess."
show shou thi
voice "audio/voice/E4/Shou/Shou Arc/35 Copy.ogg"
ss "Um…"
"He seems dazed."
pf "Yeah, he's in the pilot program."
voice "audio/voice/E4/Flirty Girl 2/E4/Shou/2.ogg"
flirtyg2 "Pilots?!"
"Shou nods, still as confused as before. He shoots me questioning glances as if unsure whether or not this is actually happening. {w}He is so out of his element!"
"The girls look at each other then giggle."
voice "audio/voice/E4/Shou_FlirtyGirl1/FlirtyGirl_03.ogg"
flirtyg1 "What are you doing after the festival? Would you want to hang out?"
show shou sur
"Shou's eyes widen and he looks at me in astonishment. He looks like he's about to agree, when he quickly shakes his head."
show shou thi
voice "audio/voice/E4/Shou/Shou Arc/36 Copy.ogg"
ss "Actually, we have plans with our girlfriends later tonight."
voice "audio/voice/E4/Flirty Girl 2/E4/Shou/3.ogg"
flirtyg2 "Aw, really?"
show shou neu
"Shou nods, although more reluctantly this time."
voice "audio/voice/E4/Shou_FlirtyGirl1/FlirtyGirl_04.ogg"
flirtyg1 "Both of you are already taken? Oh well..."
"Shrugging, she scribbles something on a napkin then tucks it into Shou's hand. Her fingers lingers on Shou as she leans in close and speaks in a breathy voice."
voice "audio/voice/E4/Shou_FlirtyGirl1/FlirtyGirl_05.ogg"
flirtyg1 "Well, if you guys ever want to hang out, I'm sure we'll be available."
hide studentF
hide studentF2
with dissolve
"They slowly return to their feet and purposely give us an eyeful of their chest. As they walk away, they exaggerate the hypnotic sway of their hips."
show shou cur
voice "audio/voice/E4/Shou/Shou Arc/37 Copy.ogg"
ss "What just happened?"

menu:
    "They were just being nice.":
        pf "They probably just wanted to hang out and play Katan."
        show shou dis
        "Shou stares at me in disbelief."
        voice "audio/voice/E4/Shou/Shou Arc/38 Copy.ogg"
        ss "Broseph, please."
        pf "What?"
        voice "audio/voice/E4/Shou/Shou Arc/39 Copy.ogg"
        ss "Those were just {i}twins{/i}."
        pf "Twins don't play Katan?"
        show shou thi
        voice "audio/voice/E4/Shou/Shou Arc/40 Copy.ogg"
        ss "Twins who look like that don't."

    "The magic of not being single.":
        pf "You don't know?"
        "Shou looks at me with intrigue."
        pf "You're forbidden fruit now, Mr. Shinjirou."
        "He blinks."
        voice "audio/voice/E4/Shou/Shou Arc/41 Copy.ogg"
        ss "Huh? What do you mean?"
        pf "Now that you're spoken for, get ready for a lot more attention from girls, my friend."
        show shou thi
        voice "audio/voice/E4/Shou/Shou Arc/42 Copy.ogg"
        ss "That doesn't make any sense. How would they know I already have a girlfriend? We just met."
        pf "They've got a secret sense for these things."
        pf "You know how women are."
        show shou neu
        "Shou nods."
        voice "audio/voice/E4/Shou/Shou Arc/43 Copy.ogg"
        ss "They have a lot of secret senses…"
        "I remember reading that once you're in a relationship, you carry yourself with more confidence. You don't appear {i}desperate{/i} or {i}needy{/i} which makes you more appealing… but who wants to talk about that psychological mumbo jumbo?"

    "No idea.":
        "I shrug."
        pf "Beats me."
        show shou thi
        "Shou looks like he's still trying to process what happened but doesn't seem to be making much progress."

show shou thi
voice "audio/voice/E4/Shou/Shou Arc/44 Copy.ogg"
ss "I think that was a fluke."
pf "A fluke?"
show shou neu
voice "audio/voice/E4/Shou/Shou Arc/45 Copy.ogg"
ss "Yeah. I've tried so hard to get a girl's number before and was met with a 0\% success rate. This was just a random outlier."
pf "Hmm…"
voice "audio/voice/E4/Shou/Shou Arc/46 Copy.ogg"
ss "You don't sound convinced."
pf "You're not wrong."
voice "audio/voice/E4/Shou/Shou Arc/47 Copy.ogg"
ss "Okay, here watch."
hide shou with dissolve
"I watch as Shou stands. He spots another girl around our age waiting in line to get some food and approaches her."
"They chat for a while. When the girl pulls out her phone, Shou looks shocked. He furiously shakes his head and retreats back to me as the girl sadly looks on."
show shou cur b2 at cc with dissolve
pf "What was that all about?"
voice "audio/voice/E4/Shou/Shou Arc/48 Copy.ogg"
ss "I tried to get her number."
show shou sur b2
voice "audio/voice/E4/Shou/Shou Arc/49 Copy.ogg"
ss "AND THEN SHE WAS ABOUT TO GIVE IT TO ME."
show shou win b2
voice "audio/voice/E4/Shou/Shou Arc/50 Copy.ogg"
ss "WHAT IS HAPPENING?"
show shou ang b2
voice "audio/voice/E4/Shou/Shou Arc/51 Copy.ogg"
ss "THE YOUNGER ME WOULD HAVE KILLED FOR THIS POWER! THIS POWER THAT I CANNOT USEEEEEEEEEEEE!"
"I pat Shou on the back."
pf "I don't know what to tell you, man."
show shou sad b2
"Shou sinks into his chair and sniffles. I never thought I'd see the day when Shou would be sad that girls are into him!"
scene black with fade
"We spend the rest of the evening checking out the festival and fending off single girls, much to Shou's anguish."
"Once we've seen everything there is to see, we go our separate ways and I head home."



stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4SSS1_Completed = 1