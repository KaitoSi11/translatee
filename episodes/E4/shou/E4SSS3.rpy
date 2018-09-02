#
label E4SSS3:
$ E4SSS3_Completed = 1

$ shoOut = "sCasual"

"Shou and I made plans this weekend to play in the beta of WatchOver, a multiplayer co-op game!"
"Better not keep him waiting. Nikki is working at the restaurant, and I have no idea where Kaito and Yuki went. {w}Someplace where they can be {i}alone{/i}."
scene black with fade
"After I get ready and wolf down some leftover food, I get on my bike and head to Shou's dorm."
stop ambient fadeout 3

scene bg campus dorm day with fade
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"As an honorary \"broseph\", Shou's brothers greet me warmly and let me roam around the dorm freely. I've even been granted access to their well-stocked fridge of alcohol and pizza."

scene bg campus dormroom day with fade
"I make my way to Shou's room. He grins when he sees me."
show shou hap at cc with dissolve
voice "audio/voice/E4/Shou/Shou Arc/81 Copy.ogg"
ss "Broseph! Are you ready?!"
pf "I was born ready!"
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/82 Copy.ogg"
ss "I got the second TV hooked up, junk food to last us for the next eight hours, and bottles in case we need power washroom breaks."

menu:
    "Uh, I think I'll stick with the actual washroom.":
        pf "Er, I'm pretty sure we can afford a few minutes to use a proper facility."
        show shou cur
        voice "audio/voice/E4/Shou/Shou Arc/83 Copy.ogg"
        ss "We'll lose precious leveling time!"
        pf "That's a sacrifice I'm willing to make."
        show shou hap
        "Shou laughs."
        voice "audio/voice/E4/Shou/Shou Arc/84 Copy.ogg"
        ss "I was just kidding anyway."
        "Yeaaah, I'm not sure about that."

    "Good work!":
        "I nod."
        pf "Excellent work, especially the extra bottles to maximize leveling and minimize wasted time."
        show shou cur
        voice "audio/voice/E4/Shou/Shou Arc/85 Copy.ogg"
        ss "Woah, wait a minute, I was just kidding about the last one."
        pf "This is no joking matter."
        show shou thi
        voice "audio/voice/E4/Shou/Shou Arc/86 Copy.ogg"
        ss "Geez, I didn't know you were this hardcore a gamer."

    "Enough talk, let's game.":
        pf "Let's get started. We're already falling behind on levels."
        "Shou nods."
        voice "audio/voice/E4/Shou/Shou Arc/87 Copy.ogg"
        ss "You're right!"

hide shou with dissolve
"After we get everything set up, we boot up the game and play some solid matches."
"It's fun for the most part, but everytime I see an enemy McGee, I start fuming at his \"E\" and right click shenanigans. I hope they end up nerfing this soon!"
"Shou seems to be doing very well with Tracee, a character who is very similar to his GEAR in most ways. Even down to the gender!"
"Meanwhile, I've really been enjoying the skillfulness of pressing \"Q\" as the Grim-Reaper and always getting the \"Play of the Match\" screen!"

show shou hap at cc with dissolve
voice "audio/voice/E4/Shou/Shou Arc/88 Copy.ogg"
ss "Ahh, this is the life."
"I lean back in the bean bag chair."
pf "You can say that again."
show shou smi
"Shou gets up and opens his mini-fridge. He throws me a drink and grabs one for himself. The chilled drink feels extra refreshing after such an intense gaming session. I think we were both overdue for a quick break."

menu:
    "How'd the month-a-versary go with your girl?" if E4D1S3_Suggestion != "None":
        pf "So... what were the results of all of my hard work?"
        show shou cur
        voice "audio/voice/E4/Shou/Shou Arc/89 Copy.ogg"
        ss "Huh?"
        pf "I spent an afternoon helping you pick out a gift for your month-a-versary! I expect a status report."
        "Shou grins."
        show shou smi
        voice "audio/voice/E4/Shou/Shou Arc/90 Copy.ogg"
        ss "Oh right! Well, broseph, I'll just say you have some solid taste."
        "I nod, he does speak the truth afterall."
        pf "Does that mean Mayu liked it?"

        if E4D1S3_Suggestion == "Jewelry":
            "Shou scratches the back of his head. He grins like an idiot and his cheeks flush."
            show shou smi
            voice "audio/voice/E4/Shou/Shou Arc/91 Copy.ogg"
            ss "Hehe, about that... I surprised her by putting the gold chain around her neck."
            pf "Wow, I didn't know you were a romantic."
            show shou cur b1 with dissolve
            voice "audio/voice/E4/Shou/Shou Arc/92 Copy.ogg"
            ss "H-Hey!"
            "I chuckle as he fake coughs to clear his throat."
            show shou smi b1
            voice "audio/voice/E4/Shou/Shou Arc/93 Copy.ogg"
            ss "Anyway, she was really happy… but then started feeling guilty I spent so much money on it \"just for her\"."
            pf "That sounds like Mayu alright."
            voice "audio/voice/E4/Shou/Shou Arc/94 Copy.ogg"
            ss "Exactly! But the next couple of times we met, she was still wearing it. It actually made me kind of happy too."
            pf "Awww, you're going soft on me, Shou."
            "Shou stammers out his response."
            show shou sur b1
            voice "audio/voice/E4/Shou/Shou Arc/95 Copy.ogg"
            ss "I-It was just unexpected, okay?"
            pf "A good unexpected thing though."
            show shou smi with dissolve
            voice "audio/voice/E4/Shou/Shou Arc/96 Copy.ogg"
            ss "I can't argue with that."

        elif E4D1S3_Suggestion == "Animal":
            "Shou's face lights up."
            show shou hap
            voice "audio/voice/E4/Shou/Shou Arc/97 Copy.ogg"
            ss "The stuffed teddy bear!"
            voice "audio/voice/E4/Shou/Shou Arc/98 Copy.ogg"
            ss "She loved it! Actually, the first time I gave it to her, she squeezed it so hard I thought it was going to explode."
            "I cough. I hope we are still talking about the teddy bear!"
            show shou cur
            "Shou looks at me strangely."
            voice "audio/voice/E4/Shou/Shou Arc/99 Copy.ogg"
            ss "Something up broseph?"
            pf "Nope, just glad she liked it."
            show shou smi
            "He smiles."
            voice "audio/voice/E4/Shou/Shou Arc/100 Copy.ogg"
            ss "Me too!"

        elif E4D1S3_Suggestion == "Chocolate":
            voice "audio/voice/E4/Shou/Shou Arc/101 Copy.ogg"
            ss "You mean the chocolate?"
            pf "Yeah."
            show shou hap
            voice "audio/voice/E4/Shou/Shou Arc/102 Copy.ogg"
            ss "Oh, it was delicious."
            pf "...You were suppose to give it as a gift, not eat it yourself."
            "Shou laughs then shakes his head."
            show shou smi
            voice "audio/voice/E4/Shou/Shou Arc/103 Copy.ogg"
            ss "When I gave it to her, she said she would only eat it if I shared it with her."
            "He blushes as he recalls the memory. {w}I'm not sure I want to know what he's thinking..."

        elif E4D1S3_Suggestion == "Books":
            show shou thi
            voice "audio/voice/E4/Shou/Shou Arc/104 Copy.ogg"
            ss "The best seller book? Yeah about that..."
            voice "audio/voice/E4/Shou/Shou Arc/105 Copy.ogg"
            ss "Apparently she already read it."
            pf "Damn, Mayu's fast! That just came out a few weeks before you bought it."
            show shou smi
            voice "audio/voice/E4/Shou/Shou Arc/106 Copy.ogg"
            ss "It's okay! Since it ended up being an extra, I borrowed it and read it."
            show shou cur
            voice "audio/voice/E4/Shou/Shou Arc/107 Copy.ogg"
            ss "Did you know books are pretty cool? It's like a manuscript to a movie that plays in your brain."
            pf "Focus..."
            voice "audio/voice/E4/Shou/Shou Arc/108 Copy.ogg"
            ss "Right! Sorry! So yeah, after I read it, we ended up talking about the story's world and characters... and she was so excited! We'd never been able to talk about books before, but I could tell Mayu really enjoyed sharing her interest with me."
            show shou hap
            voice "audio/voice/E4/Shou/Shou Arc/109 Copy.ogg"
            ss "And I found out reading isn't super boring if you read the right book!"
            pf "Sounds like a win-win."
            show shou smi
            voice "audio/voice/E4/Shou/Shou Arc/110 Copy.ogg"
            ss "You got that right."

        "Shou's smile is genuine, and he seems happier than I've seen him before. I've noticed Mayu has been more outgoing lately, and Shou has been more calm and grounded. They complement each other."
        if E3MAS3_RealCompleted == 1:
            "Despite my feelings for Mayu, I'm glad things worked out for them."

    "What's the status update on the Moosetang?":
        pf "How are things at the garage?"
        show shou smi
        voice "audio/voice/E4/Shou/Shou Arc/111 Copy.ogg"
        ss "You mean, how's the American muscle doing?"
        pf "Obviously."
        "Shou grins."
        voice "audio/voice/E4/Shou/Shou Arc/112 Copy.ogg"
        ss "It's going pretty well. I managed to find a replacement for the defective part, but it looks like a few other pieces might have gotten damaged. I'm looking extra hard for the authentic stuff this time around."
        voice "audio/voice/E4/Shou/Shou Arc/113 Copy.ogg"
        ss "I already know what to expect if I get knock-offs!"
        "I nod."
        pf "Got to stick with the originals."
        voice "audio/voice/E4/Shou/Shou Arc/114 Copy.ogg"
        ss "You got that right, broseph!"

    "Skip the small talk, I'm ready to game again.":
        "I'm not one for pointless conversation. I eat my snacks and chug my drink. If I keep my mouth full, I can't chat!"
        "It seems Shou is also enjoying all the grub and is in no mood for chit-chat. Good!"

stop music fadeout 5
"We hear a knock on Shou's door."
hide shou with dissolve
"He shakes his head, but stands up and cracks the door open. Suddenly, his body stiffens as he flings the door wide open." 
show shou neu at l3 with dissolve
pf "You expecting someone?"
"I lean over to see who it is..."
show akio neu at r3 with dissolve:
    xzoom -1
play music "audio/music/Stress (GAME VERSION).ogg" fadein 7
"...Akio?!"

show shou dis
voice "audio/voice/E4/Shou/Shou Arc/115 Copy.ogg"
ss "What are you doing here?"
show akio ann
voice "audio/voice/E4/Akio/1.ogg"
aks "You haven't answered any of my calls or emails in the past few weeks."
voice "audio/voice/E4/Shou/Shou Arc/116 Copy.ogg"
ss "Yeah, I thought you would have gotten the hint, but evidently not."
show akio neu
voice "audio/voice/E4/Akio/2.ogg"
aks "I have to talk to you."
voice "audio/voice/E4/Shou/Shou Arc/117 Copy.ogg"
ss "What a surprise."
voice "audio/voice/E4/Akio/3.ogg"
aks "This is important--"
show shou ann
voice "audio/voice/E4/Shou/Shou Arc/118 Copy.ogg"
ss "Are you going to pretend like you're a brother again before steering the conversation towards the family business, or are you going to go directly into it?"
"Even I'm surprised by Shou's sharp tongue. I know their last conversation didn't end so well… I guess Shou's been harboring even more anger than before."
show akio ann
voice "audio/voice/E4/Akio/4.ogg"
aks "Can you just listen--"
voice "audio/voice/E4/Shou/Shou Arc/119 Copy.ogg"
ss "I'm not sure I want to hear what you have to say."
show akio neu
voice "audio/voice/E4/Akio/5.ogg"
aks "Shou--"
voice "audio/voice/E4/Shou/Shou Arc/120 Copy.ogg"
ss "I know, I'm such a disappointment and so selfish because I'm not putting the family first--"
show akio dis
voice "audio/voice/E4/Akio/6.ogg"
aks "Shou!"
stop music fadeout 1.0
show akio ann
voice "audio/voice/E4/Akio/7.ogg"
aks "I'm dying."
show shou sur with dissolve
"Time seems to freeze. Shou stands motionless with his mouth hanging open. Akira faces him, stone-faced."
"Finally, Shou chokes out a word."
show shou neu
voice "audio/voice/E4/Shou/Shou Arc/121 Copy.ogg"
ss "What?"
voice "audio/voice/E4/Akio/8.ogg"
aks "I have a terminal illness, Shou."
show shou dis
voice "audio/voice/E4/Shou/Shou Arc/122 Copy.ogg"
ss "This is a joke, right? You're just saying that to make me listen… That's a cheap trick..."
show shou neu
"Akio shakes his head."
show akio thi
show shou ner
voice "audio/voice/E4/Akio/9.ogg"
aks "The doctors predict that I have a year max."
show akio neu
voice "audio/voice/E4/Akio/10.ogg"
aks "That's why Mom and Dad went back on their promise."
voice "audio/voice/E4/Akio/11.ogg"
aks "They want you to take over the family business because I can't."
voice "audio/voice/E4/Shou/Shou Arc/123 Copy.ogg"
ss "I don't… but why didn't they tell me?"
voice "audio/voice/E4/Akio/12.ogg"
aks "Mom and Dad wanted to come here themselves and tell you, but I thought the news should come from me. We both know how overbearing they can be. I wanted you to be able to make up your own mind."
show shou neu
voice "audio/voice/E4/Shou/Shou Arc/124 Copy.ogg"
ss "I see…"
"Akio nods."
voice "audio/voice/E4/Akio/13.ogg"
aks "I wish I could have approached it differently, but my condition has gotten worse… and the parents are getting restless. They want an answer right away, and that's why I pushed you to talk about it before you were ready."
voice "audio/voice/E4/Akio/14.ogg"
aks "I just wanted to see if there was any interest now that you've had a chance to be on your own for a while."
voice "audio/voice/E4/Akio/15.ogg"
aks "The business is important, but you're my little brother and your happiness is even more important. I don't want you to be forced to live a life you hate."
voice "audio/voice/E4/Akio/16.ogg"
aks "If being a pilot is what you truly want, then I will respect that."
"Shou looks more serious than I've ever seen him. After a pause, he nods."
voice "audio/voice/E4/Shou/Shou Arc/125 Copy.ogg"
ss "Okay, let's talk."
"He steps aside, and Akio is surprised to see me."
show akio cur
voice "audio/voice/E4/Akio/17.ogg"
aks "Oh, you had a guest. I didn't know."
show akio neu
"And that's my cue to leave. {w}I probably should have left earlier, but that might have been even more awkward considering they were blocking the only exit."
"I scramble to my feet." 
pf "Sorry, I didn't mean to overhear."
voice "audio/voice/E4/Shou/Shou Arc/126 Copy.ogg"
ss "It's okay. we'll catch up later, broseph."
pf "Alright."

hide shou
hide akio
with dissolve

scene bg campus dorm day with fade

"I head head past the two of them and take a seat in the common room. Maybe I should go home… but more than likely, Shou will need a friend after that conversation."
"Some of Shou's dorm mates are battling it out over consoles. Despite their welcoming invitations to join in, I politely decline. There's no way I'll be able to concentrate on anything else after that bombshell!"
"I'm not sure how much time passed, but eventually, I spot Akio come downstairs. He smiles weakly as I stand up to greet him."
show akio neu at cc with dissolve
pf "How's he doing?"
show akio thi
voice "audio/voice/E4/Akio/18.ogg"
aks "He'll need some time to process everything… but I'm confident he'll make the choice that's best for him."
"I nod."
pf "And you...?"
show akio smi
voice "audio/voice/E4/Akio/19.ogg"
aks "Doing as well as expected."
"For a guy carrying such heavy burdens, he seems to be fairly optimistic. I guess that's a Shinjirou family trait."
pf "I know we don't know each other well, but if there's anything I can do to help, please let me know."
"His smile becomes warm."
voice "audio/voice/E4/Akio/20.ogg"
aks "Thank you very much."
"Akio's phone beeps."
show akio neu
voice "audio/voice/E4/Akio/21.ogg"
aks "My apologies, I have a plane to catch."
pf "Of course, safe travels."
hide akio with dissolve
"He offers me one last smile and heads out. I return to Shou's room and see the door is partly open. He's sitting in his chair, deep in thought."
scene bg campus dormroom day with fade
"I tentatively knock and he looks up at me, then nods."
pf "You okay?"
play music "audio/music/Kaori Itami (GAME VERSION).ogg" fadein 5
show shou sad at cc with dissolve
"For the first time, he doesn't try to hide his feelings behind a smile. Instead, he shakes his head."
voice "audio/voice/E4/Shou/Shou Arc/127 Copy.ogg"
ss "He's only ever had my best interest at heart. I should have given him a chance… should have known that of course he was on my side. He always has been."
show shou ann
voice "audio/voice/E4/Shou/Shou Arc/128 Copy.ogg"
ss "Instead, I acted like such a jerk!"

menu:
    "You didn't know.":
        pf "You can't beat yourself up over something you didn't even know."
        show shou neu
        voice "audio/voice/E4/Shou/Shou Arc/129 Copy.ogg"
        ss "Maybe, but it doesn't excuse my behaviour."
        pf "You can't change what you did. At least you two were able to move past it. That's more than can be said for some."
        "Shou nods half-heartedly."

    "Family is there to cover for each other's shortcomings.":
        pf "He's your brother. I'm sure he understood."
        show shou ner
        "Shou sighs."
        voice "audio/voice/E4/Shou/Shou Arc/130 Copy.ogg"
        ss "I'm also his brother. I should have understood as well."
        pf "Regardless, what matters is that you were both able to move past all that and come together."
        voice "audio/voice/E4/Shou/Shou Arc/131 Copy.ogg"
        ss "That's true..."

    "Wallowing in self pity is not the answer.":
        pf "Hindsight is always 2020. There's no point in dwelling on what you did. You and Akio were able to discuss what needed to be said. That's the only thing that matters."
        "Shou sighs."
        voice "audio/voice/E4/Shou/Shou Arc/132 Copy.ogg"
        ss "You're right."

pf "What's your plan now?"
show shou thi
voice "audio/voice/E4/Shou/Shou Arc/133 Copy.ogg"
ss "Reading week is done, all our pre-season matches are complete, and we won't be entering the actual playoffs until next semester."
show shou neu
voice "audio/voice/E4/Shou/Shou Arc/134 Copy.ogg"
ss "Once exams are over, I'm going to London to be with Akio and learn how he runs his business."
voice "audio/voice/E4/Shou/Shou Arc/135 Copy.ogg"
ss "And from there, I'll decide if I want to go home and get involved with the main family business."
pf "You're leaving ACE?"
"Shou's eyes widen."
voice "audio/voice/E4/Shou/Shou Arc/136 Copy.ogg"
ss "Of course not! I'll be back before the next semester starts, and I'll definitely be finishing my piloting program."
voice "audio/voice/E4/Shou/Shou Arc/137 Copy.ogg"
ss "I'm just trying to give this a chance before completely writing it off."
stop music fadeout 10
"He cracks a smile. Looks like having some sort of plan helps."
pf "Aw damn, and here I thought we'd finally get some peace and quiet."
show shou smi
voice "audio/voice/E4/Shou/Shou Arc/138 Copy.ogg"
ss "Sorry broseph, you aren't getting rid of me that easily."
"We both grin. Shou is finally starting to act more normal."
show shou neu
voice "audio/voice/E4/Shou/Shou Arc/139 Copy.ogg"
ss "I'd love to stay and keep gaming, but I have to start taking care of some stuff."
pf "Of course, I'll chat with you later?"
voice "audio/voice/E4/Shou/Shou Arc/140 Copy.ogg"
ss "You bet you will. Have a good one, broseph."
stop music fadeout 3
pf "You too."
"I pack up my stuff and head out. I'm still a little worried about Shou, but he's more resilient than anyone gives him credit for."

scene black with fade
"Now that he's finally starting to patch things up with his family, I think he'll be okay."
"Still, I can't stop picturing the look on Akio's face as I drive home. The moment when Shou refused to listen, there was an instant when Akio looked hurt and scared. I think Shou's anger rattled him more than he let show."
"If it had been me and Nikki in a rocky relationship and I knew I didn't have much time left… my biggest fear would be that we'd never mend our differences."
"I quickly banish the thought from my head as my stomach feels uneasy. Hopefully that's not a situation I will have to deal with!"

scene bg homekaito main dusk with fade

$ nikOut = renpy.random.choice(['sCasual'])
$ nikHairF = renpy.random.choice(['default'])
$ nikHairB = renpy.random.choice(['default'])

"As I return home, Nikki is lounging on the couch, but she stands when she sees me." 
show nikki sur at cc with dissolve
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou01.ogg"
sf "Oh hey! You're home!"
"Seeing her makes me wonder again about what if we were like Shou and Akio..."
show nikki smi

menu:
    "Give her a hug.":
        "Wordlessly, I step forward and envelop her into a hug so tight I lift her up to the tips of her toes."
        show nikki sur b2 with dissolve
        "At first, she's too surprised to move, then she wraps her arms around me and hugs me back." 
        show nikki neu with dissolve
        "Once my uneasiness passes and I feel reassured, I let go. Nikki looks amused yet curious."
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou02.ogg"
        sf "What was that all about…?"
        pf "I'm just really glad you're my sister."
        show nikki smi
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou03.ogg"
        sf "Well, it took you long enough."
        "I blink, then laugh."
        show nikki neu
        voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou04.ogg"
        sf "But for what it's worth, you're not a bad brother either."
        pf "Thanks."

    "I'm thinking too much...":
        "I shake the thought away again."
        pf "Hey Nikki. What's up?"

show nikki hap
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou05.ogg"
sf "I was actually going to watch a movie."
"She points to the popcorn on the table then flops back onto the couch and pats the spot beside her."
show nikki smi
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou06.ogg"
sf "Care to join me, pillow?"
"I chuckle."
pf "I don't think I have a choice."
show nikki mis
"She grins."
voice "audio/voice/E4/Nikki/Nikki Arcs/Nikki_04_Shou07.ogg"
sf "Not unless you want to learn how to cook for yourself!"
show nikki smi
"Oh god no! I quickly sit down. Nikki grabs the remote."

scene black with fade

"We end up watching some romantic comedy of her choice. As the movie progresses, we add our own snide commentary, which frankly, is the only thing that made the movie bearable."
"We continue watching movies until the two of us are stifling yawns. After shutting off the TV, I get ready for sleep and go to bed."



stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4SSS3_Completed = 1
jump E4D7S1