#AFTERNOON EVENT (PLATONIC ONLY)
label E4VBS2:

$ valHairF = "default"
$ valHairB = valHairF
$ valOut = "sCasual"


"Valerie pops up in my mind, but before I can call her, she calls me."
pf "Hey, what's going on?"
stop music fadeout 4
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL68.ogg"
vb "Hey… Are you busy?"
"There no playfulness in her voice. She seems unusually serious…"
pf "Is something wrong?"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL69.ogg"
vb "Yes--I mean, I don't know."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL70.ogg"
vb "Do you think we could talk?"
pf "Sure."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL71.ogg"
vb "Meet me at the usual spot?"

menu:
    "The Hangar?":
        pf "You mean the Hangar?"
        "Valerie laughs."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL72.ogg"
        vb "All work and no play makes Valerie a dull girl. Is that really where you think we hang out?"
        pf "I mean, the last few times you called me out of the blue it was to talk about my GEAR."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL73.ogg"
        vb "Mm, that's fair, but I had someplace else in mind."

    "The cafe?":
        pf "You mean the cafe?"
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL74.ogg"
        vb "Aw, you remembered."
        pf "My other guess would have been the Hangar."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL75.ogg"
        vb "I wouldn't say we hang out there. That's business."
        pf "And this is pleasure?"
        "She sighs."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL76.ogg"
        vb "No, this is more like torture."
        pf "I think someone's blowing things out of proportion…"

    "Your room?" if valrelatonship == 0 and kaorelatonship == 0 and mayrelatonship == 0 and yuurelatonship == 0:
        pf "Valerie, are you inviting me up to your room?"
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL77.ogg"
        vb "Nice try, mister. That place is out of bounds."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL78.ogg"
        vb "I was thinking of somewhere a little more public."

voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL79.ogg"
vb "So, will you meet me at the cafe?"
pf "I'll be there."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL80.ogg"
vb "Thanks. See you soon."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"Wow, it must be serious if I actually get a goodbye! {w}I hurry to the cafe."

scene bg campus cafe day with fade

"Valerie waits for me in a booth by the corner of the restaurant. She looks up and smiles as I slip into the seat across from her."
play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
show valerie smi at cc with dissolve
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL81.ogg"
vb "I bet you're wondering why I called you."
pf "It might have crossed my mind."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL82.ogg"
vb "I need some advice."
"I grin."
pf "Oh no, trouble in paradise?"
show valerie smi
"She rolls her eyes but smiles."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL83.ogg"
vb "Paradise is better than ever, thank you very much."
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL84.ogg"
vb "Which unfortunately, is why I need advice."
pf "Okay, well, now I'm thoroughly confused."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL85.ogg"
vb "It's my mom."

if E3VBS3_Completed == 1:
    pf "Oh…"
    "I hope she didn't break her promises again. I don't know if I can take another girl's day…"

elif E3VBS2_Completed == 1:
    pf "Oh…"
    "I hope she didn't break her promises again. I can't take a beating the same way her punching bags can."

else:
    pf "What about your mom?"
    show valerie ann
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL86.ogg"
    vb "She's adding even more drama to my life!"

voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL87.ogg"
vb "I was talking to her last night because she actually remembered to call me for our weekly call this time, and I might have accidentally mentioned my boyfriend…"
show valerie sad
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL88.ogg"
vb "And now she wants to meet him."
pf "That's good, isn't it?"
show valerie ann
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL89.ogg"
vb "No! It's terrible!"
pf "Why? You don't think she'll like him?"
show valerie neu
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL90.ogg"
vb "Oh, no, she'll love him. That's not the problem."
show valerie ann
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL91.ogg"
vb "The problem is that she's crazy and will scare him away!"
pf "I'm sure that's not true."
show valerie neu
"Valerie sighs and leans back in her chair."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL92.ogg"
vb "You don't understand. Me finally getting a boyfriend is a huge deal for her!"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL93.ogg"
vb "She already lectured me about how I shouldn't \"screw this up\". As if she isn't already the queen of screwing up relationships."
pf "So, did you tell her she can't meet him?"
show valerie sur
"Valerie stares at me as if I'm the crazy one."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL94.ogg"
vb "I can't do that! She's my mom!"
show valerie neu

menu:
    "It's nice that your mom is taking an interest.":
        pf "It seems like your mom really cares and wants you to be happy. I think that's why she wants to meet him."
        "Valerie scoffs."
        show valerie ann
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL95.ogg"
        vb "If my mom really cared about what I wanted then she wouldn't push so hard to meet him."
        pf "That's just what parents do."
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL96.ogg"
        vb "Mmm, well, I still think it's too early to let him see the crazy in my family."

    "It's way too early to meet the parents!":
        pf "You need to shut that down before it begins!"
        show valerie cur
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL97.ogg"
        vb "What?"
        pf "You guys started dating recently, right?"
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL98.ogg"
        vb "Yeah…"
        pf "Meeting the parents now will definitely scare him off. It's too serious, too fast."
        show valerie smi
        "Valerie looks amused."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL99.ogg"
        vb "I agree that I don't want him to meet my mom, but when I told him about it he didn't freak out or anything."
        pf "You already told him about it?!"
        show valerie mis
        "She smirks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL100.ogg"
        vb "Honesty is the best policy in a relationship."
        pf "Ugh, okay, Kosmo."
        show valerie hap
        "Valerie laughs."

    "She'll probably just cancel anyway." if E3VBS2_Completed == 1:
        pf "Does it really matter if your mom plans to meet him?"
        show valerie ann
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL101.ogg"
        vb "Didn't you just hear everything I told you?"
        pf "Right, but how many times has your mom planned on coming to see you?"
        show valerie neu
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL102.ogg"
        vb "Um, about 6 I think."
        pf "And how many times has she actually shown up?"
        "She remains silent."
        pf "Therefore, you have nothing to worry about."
        "Valerie crosses her arms, then smirks."
        show valerie thi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL103.ogg"
        vb "That was mean, but oddly accurate."

pf "So, what are you going to do then?"
show valerie neu
"She shrugs."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL104.ogg"
vb "I'll probably just leave it alone for a while and see if she brings it up again. Chances are she'll have met her new love and \"he'll be the one\" and she'll have forgotten all about this."
pf "What if she doesn't forget?"
show valerie smi
"Valerie smirks."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL105.ogg"
vb "We'll see. This isn't the first time I've disagreed with my mom."
"She stands."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL106.ogg"
vb "Anyway, thanks for letting me vent, but I should probably head out now."
pf "Aww, are you missing your boyfriend?"
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL107.ogg"
vb "More like he's the one missing me."
"She winks."
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL108.ogg"
vb "I'll see you later then."
pf "Bye."

scene black with fade
"We walk out of the cafe together, then head our separate ways."


stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4VBS2_Completed = 1