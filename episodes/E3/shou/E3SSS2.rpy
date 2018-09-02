#
label E3SSS2:
$ shoOut = "sUniform"

scene black with fade

"I'm in the mood for a sweet latte so I decide to make my way across the campus quad towards the cafe."

play ambient "audio/ambience/Campus.ogg" fadein 5
scene bg campus main day with dissolve

$renpy.pause(.75)
voice "audio/voice/E3/Free/SS/S2/stu6m/1.ogg"
stu6m "Watch out!"

$ qtebase = 3
$ qtetotal = qteintel + qtebase
$ t_var = qtetotal
show screen timer_scr(place="E3SSS2_NoDodge")
menu:
    "Ninja reflex!":
        $ renpy.hide_screen ("timer_scr")
        jump E3SSS2_Dodged
    "Dodge!":
        $ renpy.hide_screen ("timer_scr")
        jump E3SSS2_Dodged
    "Get smoked...":
        $ renpy.hide_screen ("timer_scr")
        jump E3SSS2_NoDodge
    "Stand still...":
        $ renpy.hide_screen ("timer_scr")
        jump E3SSS2_NoDodge
    "Juke!":
        $ renpy.hide_screen ("timer_scr")
        jump E3SSS2_Dodged

label E3SSS2_Dodged:
    "I instinctively sidestep and watch a frisbee fly past my head!"
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    "Three guys approach me, and I recognise Shou as one of them."
    
    show shou cur at r2:
        xzoom -1
    show studentM extra at l3:
        xoffset -225
    show studentM2 extra at l1
    with dissolve
    show exclamation:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    $renpy.pause(.75)
    voice "audio/voice/E3/Free/SS/S2/shou/56.ogg"
    ss "Broseph! Sorry about that."
    jump E3SSS2_Convergence1

label E3SSS2_NoDodge:
    "Before I can react, something smacks the back of my head. I lose my balance and tumble forward."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    "As I roll onto my back, I see Shou standing over me with two other people."
    
    show shou cur at r2:
        xzoom -1
    show studentM extra at l3:
        xoffset -225
    show studentM2 extra at l1
    with dissolve
    show exclamation:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    $renpy.pause(.75)
    voice "audio/voice/E3/Free/SS/S2/shou/57.ogg"
    ss "Broseph! Are you alive? Speak to me!"
    pf "Dude."
    "He extends a hand and helps me up. I climb back to my feet."
    jump E3SSS2_Convergence1

label E3SSS2_Convergence1:
voice "audio/voice/E3/Free/SS/S2/stu5m/1.ogg"
stu5m "Excellent work, Shou. I especially like the part where you did the mid-air twirl and completely whiffed your throw."
show shou ske
voice "audio/voice/E3/Free/SS/S2/shou/58.ogg"
ss "That was going to be a legendary move! It just so happens that my fingers were a little sweaty."
voice "audio/voice/E3/Free/SS/S2/stu6m/2.ogg"
stu6m "Suuuuuuure."
"The two guys glance at each other other then laugh. {w}Wait, don't I have class with these guys? {w}One of them turns towards me."
voice "audio/voice/E3/Free/SS/S2/stu5m/2.ogg"
stu5m "Anyway, you okay--"
"His eyes widen when he recognises me."
show shou cur
voice "audio/voice/E3/Free/SS/S2/stu5m/3.ogg"
stu5m" It's the chick magnet!"
"Yup, I have class with them."
voice "audio/voice/E3/Free/SS/S2/stu6m/3.ogg"
stu6m "You're right!"
voice "audio/voice/E3/Free/SS/S2/shou/59.ogg"
ss "Wait, what, where?"
"They both point to me."
voice "audio/voice/E3/Free/SS/S2/stu5m/4.ogg"
stu5m "This guy."
show question:
    xoffset 1040
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/SS/S2/shou/60.ogg"
ss "This guy?"
voice "audio/voice/E3/Free/SS/S2/stu6m/4.ogg"
stu6m "This guy!"
"I'm pretty sure they're referring to the first time I met Valerie in class."
pf "Hey, guys."
voice "audio/voice/E3/Free/SS/S2/shou/61.ogg"
ss "You know each other?"
show shou smi
voice "audio/voice/E3/Free/SS/S2/stu5m/5.ogg"
stu5m "Yeah, he's been teaching us how to pick up the ladies."
pf "...What?"
voice "audio/voice/E3/Free/SS/S2/stu6m/5.ogg"
stu6m "Don't deny your talents! We've seen you hanging around campus with that blonde bombshell!"
pf "Well, yeah, she's our team engineer."
play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
show bulb:
    xoffset 1040
    yoffset 20
    xzoom .75
    yzoom .75
"Shou perks up."
show shou cur
voice "audio/voice/E3/Free/SS/S2/shou/62.ogg"
ss "Oh, you guys mean Valerie?"
voice "audio/voice/E3/Free/SS/S2/stu5m/6.ogg"
stu5m "You know her too?!"
"They both stare at Shou with awe."

if (E2MAS4_Completed == 0):
    voice "audio/voice/E3/Free/SS/S2/stu5m/7.ogg"
    stu5m "Your childhood friend, the girl from gymnastics, and now the engineer chick too?"
    voice "audio/voice/E3/Free/SS/S2/stu6m/6.ogg"
    stu6m "Damn Shou!"
    show shou ske
    "Shou looks just as perplexed as I do."
    ### VOICE - missing line
    voice "audio/voice/MISSING/BATCH2/5.ogg"
    ss "What are you guys rambling about?!"

else:
    voice "audio/voice/E3/Free/SS/S2/shou/63.ogg"
    ss "Umm... yeah, Valerie takes care of our GEARs."
    voice "audio/voice/E3/Free/SS/S2/stu6m/7.ogg"
    stu6m "\"Takes care\"..."
    voice "audio/voice/E3/Free/SS/S2/stu5m/8.ogg"
    stu5m "Of their \"GEARs\"."
    show shou ske
    "Shou and I blink. These guys have a really overactive imagination."

"The pair share a knowing look with each other, then cross their arms and nod."
voice "audio/voice/E3/Free/SS/S2/stu6m/8.ogg"
stu6m "We have a ways to go."
voice "audio/voice/E3/Free/SS/S2/stu5m/9.ogg"
stu5m "But one day we'll reach your level!"
show shou smi
"Shou shrugs."
voice "audio/voice/E3/Free/SS/S2/shou/65.ogg"
ss "Anyway..."
"He looks at me."
voice "audio/voice/E3/Free/SS/S2/shou/66.ogg"
ss "What brings you here, broseph?"
pf "Just heading to the cafe, you?"
show shou hap
voice "audio/voice/E3/Free/SS/S2/shou/67.ogg"
ss "I was just showing these guys an awesome frisbee throw I saw on MeTube."
voice "audio/voice/E3/Free/SS/S2/stu5m/10.ogg"
stu5m "\"Awesome\" he says."
"They laugh again."
show shou ann
voice "audio/voice/E3/Free/SS/S2/shou/68.ogg"
ss "Oh! I'll show you! Watch!"
hide shou with dissolve
"Shou grabs the frisbee and takes a few steps back to give himself space. Then he takes a running start to build momentum, jump-spins in the air, and whips the frisbee free."
"It goes flying! {w}That actually looked pretty cool! Even the two other guys are impressed!"
"The Frisbee curves back like a boomerang… but instead of coming back to us, it heads straight for a well-dressed older man in a blazer!"

show shou sur at r2 with dissolve:
    xzoom -1
show frightful:
    xoffset 1040
    yoffset 20
    xzoom .75
    yzoom .75
voice "audio/voice/E3/Free/SS/S2/shou/69.ogg"
ss "Crap! Not again! Watch out!"
"The man catches the frisbee mid-air. He looks around and makes a beeline towards us when he spots us. {w}Uh oh."
show shou cur
voice "audio/voice/E3/Free/SS/S2/stu5m/11.ogg"
stu5m "Uh, it was nice hanging out with you, but, uh, we've got class."
hide studentM extra with dissolve
voice "audio/voice/E3/Free/SS/S2/stu6m/9.ogg"
stu6m "Yeah... we'll talk to you guys later!"
hide studentM2 extra with dissolve
show shou sur with dissolve
voice "audio/voice/E3/Free/SS/S2/shou/70.ogg"
ss "W-Wait! Where are you going? What about your frisbee?"
voice "audio/voice/E3/Free/SS/S2/stu5m/12.ogg"
stu5m "Keep it!"
"The two \"friends\" speed walk away into the distance."
show shou ang
voice "audio/voice/E3/Free/SS/S2/shou/71.ogg"
ss "Cowards!"
show shou ner
"Shou looks at me, then gulps."
stop music fadeout 6
"As the man approaches, his eyes widen in surprise..."
show shou sur with dissolve
"...but not nearly as wide as Shou's."

stop ambient fadeout 10
hide shou with dissolve

show shou sur at l2
show akio neu at r2:
    xzoom -1
with dissolve
### VOICE - missing line
voice "audio/voice/MISSING/BATCH2/6.ogg"
ss "Akio?"
show shou neu
voice "audio/voice/E3/Free/SS/S2/aks/1.ogg"
aks "Hello, Shou."
"They look eerily similar."
pf "You two know each other?"
"Shou nods."
play music "audio/music/Stress (GAME VERSION).ogg" fadein 6
voice "audio/voice/E3/Free/SS/S2/shou/72.ogg"
ss "This is my brother."
"All trace of laughter is gone from his voice. He's strangely stiff and formal. It's obvious he's not very comfortable around his brother."
voice "audio/voice/E3/Free/SS/S2/aks/2.ogg"
aks "I'm Akio Shinjirou."
pf "[pfull]."
show akio smi
"He smiles politely."
voice "audio/voice/E3/Free/SS/S2/shou/73.ogg"
ss "What are you doing here?"
voice "audio/voice/E3/Free/SS/S2/aks/3.ogg"
aks "I'm the guest lecturer for Cenorobotics and the Modern Business World."
show shou dis
voice "audio/voice/E3/Free/SS/S2/shou/74.ogg"
ss "Why didn't you tell me you were coming?"
"Although Shou's careful to keep any sense of bitterness or disapproval from his voice, it's clear he's not pleased by this surprise. They don't act very brotherly..."
show akio neu
voice "audio/voice/E3/Free/SS/S2/aks/4.ogg"
aks "I only arrived a few hours ago. I was going to text you after the first lecture."
show akio smi
"He smiles."
voice "audio/voice/E3/Free/SS/S2/aks/5.ogg"
aks "But since you're here, let's pencil in something for the weekend."
show shou neu
"Shou shrugs."
voice "audio/voice/E3/Free/SS/S2/shou/75.ogg"
ss "I'll have to check my schedule first."
"Akio nods."
voice "audio/voice/E3/Free/SS/S2/aks/6.ogg"
aks "Of course. Let's say tentative for Saturday."
voice "audio/voice/E3/Free/SS/S2/shou/76.ogg"
ss "Sure, but I might be busy."
voice "audio/voice/E3/Free/SS/S2/aks/7.ogg"
aks "Then let me know when you can."
"Akio looks at me."
show akio hap
voice "audio/voice/E3/Free/SS/S2/aks/8.ogg"
aks "You're welcome to join us. I'd like to get to know Shou's friends. He doesn't share much about--"
show shou dis
voice "audio/voice/E3/Free/SS/S2/shou/77.ogg"
ss "Don't you have a lecture to go to?"
show akio dis with dissolve
"Akio sighs. He checks his watch."
show akio neu
voice "audio/voice/E3/Free/SS/S2/aks/9.ogg"
aks "Correct. Let's continue this conversation over the weekend."
show shou neu
voice "audio/voice/E3/Free/SS/S2/shou/78.ogg"
ss "Bye."
voice "audio/voice/E3/Free/SS/S2/aks/10.ogg"
aks "Goodbye."

hide akio with dissolve
"As Akio disappears into a nearby building, I look at Shou."

hide shou with dissolve

show shou neu at cc with dissolve
show dots:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
"His jaw is set and his eyes are clouded. This is really out of character for him..."

menu:
    "What was that all about?":
        pf "Your brother seems nice."
        "Shou just shrugs."
        "He rarely ever talks about his family, and I guess his family being here still isn't enough to get him to open up about them."
        pf "You're not exactly yourself around him."

    "Why are you being a jackass?":
        pf "You were a bit of a dick to your bro."
        show shou dis
        "Shou glares at me."

    "I'm not getting involved.":
        "I'll pass on getting swept into this drama llama business."
        "Although, I was invited to join them on Saturday… Should I take him up on the invite? Is it rude to say no?"
        pf "So, uh..."
        jump E3SSS2_NotInvolved

show shou dis
voice "audio/voice/E3/Free/SS/S2/shou/79.ogg"
ss "You don't know him like I do."
pf "What do you mean?"
show shou neu
voice "audio/voice/E3/Free/SS/S2/shou/80.ogg"
ss "He's not as he seems. I don't trust him just showing up out of the blue."
"I'm sure he knows his brother best, but I didn't get that feeling."
voice "audio/voice/E3/Free/SS/S2/shou/81.ogg"
ss "He lives and works in London so the fact that he's here is very suspicious."
pf "Well, he said he was invited to lecture for a class."
"Shou doesn't seem convinced."
show shou ske
voice "audio/voice/E3/Free/SS/S2/shou/82.ogg"
ss "It's too convenient. And why now?"
pf "Regardless, he did come all this way… Aren't you going to at least see him this weekend?"
show shou neu
show storm:
    xoffset 720
    yoffset 20
    xzoom .75
    yzoom .75
"Shou sighs."
voice "audio/voice/E3/Free/SS/S2/shou/83.ogg"
ss "Yes, but only because he'll be a nuisance if I don't."

label E3SSS2_NotInvolved:
pf "...Do you want me to come on Saturday?"
show shou neu
voice "audio/voice/E3/Free/SS/S2/shou/84.ogg"
ss "If you want to."
pf "I don't want to intrude."
voice "audio/voice/E3/Free/SS/S2/shou/85.ogg"
ss "No, it's fine."
voice "audio/voice/MISSING/BATCH2/7.ogg"
ss "Actually, I think I prefer you coming. Maybe then he'll be on his best behaviour."
pf "Uh... okay."
"This is getting really awkward. Part of me thinks it would be a bad idea to go, but maybe I can help mediate and smooth things over between them."
### VOICE - needs editting
#voice "audio/voice/E3/Free/SS/S2/shou/86.ogg"
ss "Anyway, I'm going to head off."
pf "Alright, have a good one."
"Shou nods and heads towards his dorm."
hide shou with dissolve
"I can't help but feel a bit uneasy from that entire exchange…"

scene black with fade
stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E3SSS2_Completed = 1