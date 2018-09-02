#AFTERNOON
label E4YMS1:

$ yuuHairF = "pony"
$ yuuHairB = yuuHairF
$ yuuOut = "sTennis"


"I wonder if Yuuna's still trying out different clubs. The last couple of times I went with her it was pretty fun. {w}Let's see what she's up to."
"I dial Yuuna's number. She seems out of breath when she answers."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/1.ogg"
ym "Hello?"
pf "Hey, Yuuna. Checking out any new clubs today?"
"She chuckles."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/2.ogg"
ym "Nope, I've decided on what I want to do."
pf "Oh really? What did you choose?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/3.ogg"
ym "Tennis!"
"I grin."

if MCStory == 3:
    "I had a feeling she'd come back to that."
    
pf "Is that what you're doing now?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/4.ogg"
ym "Actually, I decided to participate in the tennis open league today."
pf "Does that mean you're going to try out for the school league next year?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/5.ogg"
ym "Maybe… I'm not sure yet. It's still a huge time commitment… but I can always drop in on club matches."

if yuurelatonship == 0:
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/6.ogg"
    ym "Want to come watch?"
    "I recall how Yuuna schooled me in tennis the last time we played."
    "There's no chance this will be a boring event!"
    pf "Sure. I'll meet you at the courts."

                
elif yuurelatonship == 1:
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/8.ogg"
    ym "You're coming, right?"
    "She tries to keep her tone light, but a hint of worry sneaks into her voice. I know that my being there to support her would mean a lot."
    "Plus, there's no way I'm going to turn down another opportunity to see her in that cute tennis outfit!"
    pf "Of course! I'll be that loud voice in the stands cheering you on."
    "She giggles."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/9.ogg"
    ym "I'll be disappointed if I don't hear you."
    pf "I'll be sure to yell extra loud. {w}Meet you at the courts."

    
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/10.ogg"
ym "Okay, see you soon!"
"We hang up the phone and I make my way to the rec center."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3


"The event has a strong turnout, and while the spectator space is not as large as our other venues, more than half of the seats are filled."

scene bg campus gym day with fade

"I scan the crowd of students lining the tennis courts in search of Yuuna. She's off on her own, leaning into a runner's stretch."
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
pf "Hey, Yuuna."
show yuuna smi at cc with dissolve
"Her face lights up when she sees me."
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/11.ogg"
ym "You're here! Thanks for coming."
pf "I wasn't going to miss out on another chance to watch you wipe the floor with your opponents."
show yuuna smi
"She laughs."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/12.ogg"
ym "It won't be so easy this time. I recognise some of the students from the ACE tennis league. There's a good chance I'll have to play against them."
"I take another look at the students holding tennis rackets. Most of them keep to themselves. They wear solemn faces and quietly stretch. A small group of students are gathered in a circle. Those must be the league members."
pf "I don't think I know who any of them are."
"Yuuna pauses and points out the ones she recognises."
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/13.ogg"
ym "That girl with short hair is also a second year and a pretty strong player on the team. She's actually from my hometown. We trained together in high school."
"The girl is one of the only students with a smile on her face. She rolls her wrist and lets her racket hang loosely by her side."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/14.ogg"
ym "The guy to her left is a first year. He just made it onto the team so he's still in training."
"As Yuuna gives me the stats on her opponents, her demeanor changes. Her posture relaxes and her eyes glance alertly around the court. She'd fit right in with the rest of us in the pre-combat room if she were a pilot."
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/15.ogg"
ym "And that small guy beside them is actually their star player."
pf "Really?"
"I glance skeptically at him. He looks like a high schooler who's still waiting to go through puberty."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/16.ogg"
ym "Yeah, he's a third year and captain of the tennis team. In fact, she--"
"Yuuna points again to the first girl."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/17.ogg"
ym "--will probably take his place as captain next year."
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/18.ogg"
ym "He's also left handed."
pf "And that means?"
show yuuna neu
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/19.ogg"
ym "I should have worked harder on my backhand."
pf "So it sounds like those few are the only real challenge here."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/20.ogg"
ym "That's only as far as I know. There may be some hidden diamonds nobody knows about!"

menu:
    "You'll do great anyway.":
        pf "Well, even if they are, you don't have to worry about them. I've seen first hand what you can do and I know you'll win this thing!"
        show yuuna smi b1 with dissolve
        "She blushes."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/21.ogg"
        ym "Thanks."

    "I doubt there will be any surprises.":
        pf "Eh, probably not. I bet you're the only worthwhile player who's not already in the tennis league."
        "She smiles."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/22.ogg"
        ym "I appreciate your confidence, but I'm not going to let my guard down."

    "Just keep your head in the game.":
        pf "Regardless, as long as you stay focused on the game you'll be fine."
        show yuuna mis
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/23.ogg"
        ym "Thanks, coach."
        "She sticks her tongue out at me."

"Spectators are being ushered to their seats as the organisers announce the first match up."
pf "I better go so I can claim a good seat."
show yuuna smi
"Yuuna nods."

if yuurelatonship == 0:
    hide yuuna with dissolve
    
if yuurelatonship == 1:
    show yuuna cur b1 with dissolve
    "Before I go, I wrap my arms around her and pull her into a hug. Then I kiss her cheek."
    pf "Good luck! I'll be rooting for you."
    show yuuna hap b1
    "Her cheeks are flushed but she grins."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/24.ogg"
    ym "Thanks!"
    hide yuuna with dissolve
    "As I leave, she fidgets with the edge of her racket as she looks out into the crowd. I guess she is nervous afterall."

"The first few rounds are between students I don't know. I half-heartedly watch the matches, as they all kind of bleed together."
"Finally, Yuuna's first match is up! I sit up in my seat and wave as she walks onto the court. She smiles in acknowledgment. Her opponent is a random student I don't recognise. I settle back into my seat. This will probably be a quick match."
"As I predicted, Yuuna demolished the poor guy."
"Soon, the second round of matches begins and Yuuna is pit against the first year team league player. He scowls at Yuuna but she seems undisturbed. {w}In the end, Yuuna demolished him too. He stomps off the stage as I cheer along with the rest of the crowd for Yuuna."
"When she's matched with the girl from the tennis team, the two of them nod in respect for each other. Yuuna grips her racket tightly. A look of concentration replaces the smile on her opponent's face."
"They're more evenly matched--I assume because they're used to each other's styles and know each other's strengths and weaknesses. Although Yuuna claims to be out of practice, she still comes out victorious with a 2 point lead."

"Finally, the two remaining contenders are Yuuna and the third year captain of the ACE tennis league. Even from my seats Yuuna seems to tower over him, but he is unfazed."
"They ready their rackets as Yuuna gives the first serve. Just like when I played against her, her racket connects with the ball in a resounding crack."
"It speeds across the net in a blur, but her opponent seems to be waiting for the ball and easily returns her serve. They continue to volley the ball back and forth. I lean forward in my seat, holding my breath."
"He strikes towards Yuuna's left and her backhand misses. The audience lets out a collective gasp."
"Their match is the most engaging as the two of them dart across the court. They are tied and this last point wins the match. Ultimately, Yuuna misses another backhanded strike and her opponent is named the victor."
"I race back down to the courts. Yuuna and the captain are speaking, and as I approach I catch the tail end of their conversation."

show receptionist extra at r2 with dissolve:
    xzoom -1
    yoffset 120
    
show yuuna smi at l2 with dissolve

voice "audio/voice/E4/Tennis Captain/Yuuna/1.ogg"
tc "Did you try out for the league this year?"
"Yuuna shakes her head."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/25.ogg"
ym "No, I was focused on my studies and was worried the league might be too much of a time commitment."
voice "audio/voice/E4/Tennis Captain/Yuuna/2.ogg"
tc "No wonder I haven't seen you play before. I'll admit, I was really impressed by your skills."
voice "audio/voice/E4/Tennis Captain/Yuuna/3.ogg"
tc "You should try out for the league next year. I'm positive you'll make it onto the team."
"Yuuna smiles politely."
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/26.ogg"
ym "Thank you for the offer! I'll definitely keep that in mind."
voice "audio/voice/E4/Tennis Captain/Yuuna/4.ogg"
tc "I hope you do."
show yuuna smi
"He glances my way, then politely excuses himself."

hide yuuna
hide receptionist
with dissolve

show yuuna neu at cc with dissolve

if yuurelatonship == 1:
    "As he walks away, I sneak up behind Yuuna and attack her with a hug from behind!"
    show yuuna sur b2 with dissolve
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/27.ogg"
    ym "Ah!"
    show yuuna hap b1 with dissolve
    "She whirls to face me and smiles."
    pf "You were so awesome out there!"
    
else:
    pf "Hey Yuuna."
    show yuuna smi
    "She whirls around to face me."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/28.ogg"
    ym "Oh hey."
    pf "You were great out there!"

show yuuna dis with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/29.ogg"
ym "Thanks… but I didn't win."
pf "No, but you and the freaking {i}captain{/i} of the tennis league were neck and neck for the majority of the match!"
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/30.ogg"
ym "I know!"
"I thought she would finally realise just how impressive that was and crack a smile, but she frowns instead."
show yuuna ann
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/31.ogg"
ym "Ugh, if only I'd practiced my backhand! I know I could have beaten him and his smug face!"
"Uh… wow… I knew Yuuna was competitive, but I had no idea she was {i}this{/i} competitive."

menu:
    "Try to calm her down.":
        pf "You've been out of the game for a while, but you still managed to clobber the rest of the team. If tennis is what you've decided to take up as your extra curricular, then I'm positive you'll have a chance to play against him again."
        show yuuna mis
        "Yuuna perks up."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/32.ogg"
        ym "You're right! Let's see how he likes a taste of my backhand!"
        pf "I wouldn't word it like that…"

    "I've never seen this side of you before.":
        pf "I didn't know you had it in you."
        show yuuna cur
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/33.ogg"
        ym "Had what?"
        pf "Salty Yuuna."
        show yuuna ann
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/34.ogg"
        ym "I'm not salty!"
        pf "You're so salty you're giving me high blood pressure."
        if yuurelatonship == 1:
            show yuuna smi
            "Yuuna blinks, then laughs."
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/35.ogg"
            ym "I guess I am overreacting a bit, aren't I?"
            pf "A little."
            "She sighs and buries her face in my chest."
            show yuuna dis
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/36.ogg"
            ym "But I was so close…"
            "I stroke her hair."
            pf "I know."
        else:
            "Yuuna raises an eyebrow."
            show yuuna ske
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/37.ogg"
            ym "How long did it take you to think that up?"
            pf "Too long."

    "Let her vent.":
        show yuuna ann
        "This was a hard loss, and if I were in her shoes I'd be just as upset. Better that she gets it out of her system now than later."
        "Yuuna continues to mumble to herself until she naturally begins to calm down."
        pf "Feel better?"
        show yuuna neu
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/38.ogg"
        ym "A bit."

show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/39.ogg"
ym "Well, it looks like everyone is leaving."
pf "Yeah, we should probably leave too."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/40.ogg"
ym "I'm going to go to the lockers and shower. Thanks for coming out again."
pf "This was fun."
"She smiles."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/41.ogg"
ym "I'll see you later."

hide yuuna with dissolve
"I say my goodbyes and we head our separate ways."

stop music fadeout 3
stop ambient fadeout 3
scene black with fade
$renpy.pause(2.5)
$ E4YMS1_Completed = 1