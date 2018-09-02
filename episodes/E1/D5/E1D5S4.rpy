label E1D5S4:
stop music fadeout 3.0

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    $renpy.pause(1.5)
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg" 
    $renpy.pause(1.5)
    "Just as I reach for my phone, I'm startled by a loud buzzing sound. Kaori's name flashes across the screen."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "... That's weird."
    pf "Hey Kaori. I was just about to call--"
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E1/D5/S4/Kaori/1.ogg"
    ki "You broke my tablet!" 
    pf "U-Uh, what?"
    voice "audio/voice/E1/D5/S4/Kaori/2.ogg"
    ki "You broke my tablet so you owe me a working one." 

    menu: 
        "When did I do that?":
            pf "When have I even gone near your tablet?"
            voice "audio/voice/E1/D5/S4/Kaori/3.ogg"
            ki "When you nearly mowed me down with your bike."
            "I pause."
            pf "Ohhh…"
            voice "audio/voice/E1/D5/S4/Kaori/4.ogg"
            ki "Exactly. Anyway, it's broken now because of you."

        "I don't give gifts until the second or third date.":
            pf "At least wait until we've gone on a date before you start asking for gifts."
            voice "audio/voice/E1/D5/S4/Kaori/5.ogg"
            ki "It's not a present if you're the reason I need a replacement!"
            pf "You want me to buy it, don't you?"
            voice "audio/voice/E1/D5/S4/Kaori/6.ogg"
            ki "Of course! You broke it!"
            pf "Sounds like a gift to me."
            voice "audio/voice/E1/D5/S4/Kaori/7.ogg"
            ki "It's not!"
            pf "Hey, I get it--"
            voice "audio/voice/E1/D5/S4/Kaori/8.ogg"
            ki "I don't have time for this. You owe me a replacement."

        "I've never gone near your tablet.":
            pf "No, I didn't."
            voice "audio/voice/E1/D5/S4/Kaori/9.ogg"
            ki "Yes, you did!"
            pf "How could I have broken it when I've never used it?"
            voice "audio/voice/E1/D5/S4/Kaori/10.ogg"
            ki "When you nearly killed me, you actually killed my tablet instead."
            pf "What?"
            voice "audio/voice/E1/D5/S4/Kaori/11.ogg"
            ki "You shattered the screen when my bag was thrown across the pavement, and now it won't even turn on."
            pf "That still sounds like it's {i}your{/i} problem."
            "There's a pause before Kaori's rage breaks loose."
            voice "audio/voice/E1/D5/S4/Kaori/12.ogg"
            ki "{i}My{/i} problem? Idiot! {i}You{/i} were the one who ran the red light. {i}You{/i} were the one who almost ran me down. And {i}you{/i} were the one who caused my bag--a bag with valuable things, I might add--to fly across the pavement, thereby completely shattering said valuable things. And if it weren't for you, I'd--"
            pf "God, this {i}again{/i}? What will it take for you to shut up about this?"
            voice "audio/voice/E1/D5/S4/Kaori/13.ogg"
            ki "The tablet."

    pf "Fine."
    pf "What model did you have? I'll replace it with the same. You won't notice a difference." 
    voice "audio/voice/E1/D5/S4/Kaori/14.ogg"
    ki "I had an EN85…"
    pf "No, really, what did you have?"
    voice "audio/voice/E1/D5/S4/Kaori/15.ogg"
    ki "That's what I had!"
    pf "I would have thought you'd had a newer model."
    voice "audio/voice/E1/D5/S4/Kaori/16.ogg"
    ki "Why? It worked fine until you broke it."
    pf "Well, okay. How long did you have it for?"
    voice "audio/voice/E1/D5/S4/Kaori/17.ogg"
    ki "Two years."
    pf "That's kind of a long time… How much for the replacement?"
    voice "audio/voice/E1/D5/S4/Kaori/18.ogg"
    ki "399.99 credits, plus tax."
    pf "399.99 credits?{w} {i}Plus{/i} tax?!"
    voice "audio/voice/E1/D5/S4/Kaori/19.ogg"
    ki "It's how much that cost."
    pf "It's used. Do you not know what depreciation is? I'll give you 150 credits and that's being generous."
    voice "audio/voice/E1/D5/S4/Kaori/20.ogg"
    ki "What?! That's not even close to how much I paid for it!"
    pf "Of course not, it's an old model, but that's about how much it'd be worth now."
    voice "audio/voice/E1/D5/S4/Kaori/21.ogg"
    ki "I paid more than double that price when I bought it so that's how much it's worth."
    pf "That's not how it works."
    voice "audio/voice/E1/D5/S4/Kaori/22.ogg"
    ki "That's how much it was worth to me!"
    pf "Maybe I can get you a used one then."
    voice "audio/voice/E1/D5/S4/Kaori/23.ogg"
    ki "No! People don't take care of their things. Knowing your luck you'll buy me a faulty tablet and I'll have to replace it again almost immediately."
    pf "I know how to pick out electronics. I'm not so stupid that I'd buy you a damaged one."
    voice "audio/voice/E1/D5/S4/Kaori/24.ogg"
    ki "Debatable."
    "She is making this really difficult." 
    pf "Look, I'm not going to pay the original cost, {i}plus tax{/i}, of something that is no longer worth that amount." 
    voice "audio/voice/E1/D5/S4/Kaori/25.ogg"
    ki "Fine, but you should at least get me something comparable to my old one--like the YX140." 

else:
    "Hmm, Kaori never sent over the strategies she wanted me to look over before our meeting on Monday. {w}What time is that meeting anyway? May as well ask her."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    "I grab my phone and dial her number."
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    "The phone rings a few times before Kaori answers." 
    voice "audio/voice/E1/D5/S4/Kaori/26.ogg"
    ki "Hello?" 
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    pf "Hey, Kaori, it's [pfirst]." 
    voice "audio/voice/E1/D5/S4/Kaori/27.ogg"
    ki "Oh, hi." 
    pf "Hey, you never sent me the strategies you wanted me to learn." 
    voice "audio/voice/E1/D5/S4/Kaori/28.ogg"
    ki "Of course I sent them. Check your email again."
    "I flip through my emails, and as expected, do not see one from Kaori."
    pf "Well, it's not sitting in my inbox so if you sent it I don't know who you sent it to."
    voice "audio/voice/E1/D5/S4/Kaori/29.ogg"
    ki "Isn't this your email?"
    "She reads me an incorrect address."
    pf "No, there's no \"7\" in my email."
    voice "audio/voice/E1/D5/S4/Kaori/30.ogg"
    ki "Ugh, idiot! Why did you give me the wrong email?"
    pf "I didn't give you the wrong--"
    voice "audio/voice/E1/D5/S4/Kaori/31.ogg"
    ki "Wait, I'll send it again."
    "I hear a commotion on the other end of the phone and something that sounds like a frustrated groan." 
    voice "audio/voice/E1/D5/S4/Kaori/32.ogg"
    ki "Ugh, my tablet still isn't working so I have to grab my laptop. Hold on."
     
    if (E1D2S3_EncounteredKaori == 0):
        menu: 
            "What did you do to it?":
                pf "What happened to your tablet?" 
                voice "audio/voice/E1/D5/S4/Kaori/33.ogg"
                ki "I don't know. It's been weird for a while but ever since yesterday it won't even turn on." 
                pf "That sucks." 
                voice "audio/voice/E1/D5/S4/Kaori/34.ogg"
                ki "I'm so fed up with it. I'm heading to the mall later to grab the YX140 to replace it."

            "Sounds like you need a man to fix it.":
                pf "I could come by to fix it for you." 
                voice "audio/voice/E1/D5/S4/Kaori/35.ogg"
                ki "You can't fix this. It's completely dead." 
                pf "I can, I have very skilled hands…" 
                voice "audio/voice/E1/D5/S4/Kaori/36.ogg"
                ki "Skilled enough to bring it back to life?" 
                pf "Skilled enough to make you forget about the damage." 
                voice "audio/voice/E1/D5/S4/Kaori/37.ogg"
                ki "What? Whatever--I'm just going to head to the mall and get the YX140 to replace it." 

            "I still haven't gotten an email…":  
                pf "Have you resent it yet?" 
                voice "audio/voice/E1/D5/S4/Kaori/38.ogg"
                ki "No, my computer is slow. That's why I always use my tablet." 
                pf "Then get a new tablet." 
                voice "audio/voice/E1/D5/S4/Kaori/39.ogg"
                ki "Like I didn't think of that! I'm heading to the mall today to get the YX140."

    if (E1D2S3_MetKaoriWasRudeYesHelmet == 1):
        pf "What happened? Did you break it?" 
        voice "audio/voice/E1/D5/S4/Kaori/40.ogg"
        ki "No, {i}I{/i} didn't break it." 
        pf "Someone else did?" 
        voice "audio/voice/E1/D5/S4/Kaori/41.ogg"
        ki "Some idiot ran me over on the first day of school and it hasn't been working since!"
        "Oops…" 
        pf "Wow, what a jerk!" 
        voice "audio/voice/E1/D5/S4/Kaori/42.ogg"
        ki "I know! I'm heading to the mall later to grab the YX140 to replace it, but I wish I knew who it was so I could make them get me a new one."
            
pf "What about the Z90 model? It has better specs and it's cheaper." 
voice "audio/voice/E1/D5/S4/Kaori/43.ogg"
ki "No, it doesn't! The YX140 is the model that replaced the EN85. It offers more GB than the Z90 and has better connectivity options."
pf "What are you talking about? Everything else is comparable and you can get it with a higher GB. Plus, the Z90 is made by Macrohard which we all know is better than Pineapple." 
voice "audio/voice/E1/D5/S4/Kaori/44.ogg"
ki "Are you kidding me? Pineapple is the better choice. It runs faster and it doesn't get viruses either so it has a better shelf-life."
pf "Is this a joke? Meet me at the store. I'll show you that the Z90 is just as good--if not better--than the YX140. If after that you still don't believe me then I'll concede." 
voice "audio/voice/E1/D5/S4/Kaori/45.ogg"
ki "Fine, but only because I know you're wrong! Meet you there in half an hour." 
"The phone clicks without another word. {w}Well goodbye to you too! {w}I grab my jacket and head for the door." 


stop ambient fadeout 3.0
stop music fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Mall.ogg" fadein 3
scene bg mall main day with fade

$renpy.pause(1.0)


"I arrive at the mall before Kaori and wait by the front south entrance."
"It's only a minute or two before I see her walking up to me dressed in a hoodie and jeans. It's weird to see her out of uniform." 

$ kaoOut = "sCasual"
$ kaoHairF = "long"
$ kaoHairB = "long"

show kaori neu at cc with dissolve

menu: 
    "You look nice.":
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "I like your outfit."
        show kaori dis
        voice "audio/voice/E1/D5/S4/Kaori/46.ogg"
        ki "Why? It's nothing special."
        pf "It's just nice to see what you like to wear."
        show kaori thi
        voice "audio/voice/E1/D5/S4/Kaori/47.ogg"
        ki "I-I suppose…"

    "Do you meet all your dates in a hoodie?": 
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "A little casual for a date, but I can dig it."
        show vein:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori dis 
        voice "audio/voice/E1/D5/S4/Kaori/48.ogg"
        ki "This isn't a date!"
        pf "Don't get me wrong, I'm not complaining! You still look good."
        show kaori ann with dissolve
        voice "audio/voice/E1/D5/S4/Kaori/49.ogg"
        ki "Shut up! I wouldn't wear this on a date."
        pf "What would you wear?"
        show tsuBlush:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori dis b1 with dissolve
        voice "audio/voice/E1/D5/S4/Kaori/50.ogg"
        ki "I-It doesn't matter!"

    "What are you wearing?!": 
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        pf "You could have picked anything in your closet and you chose that?" 
        show kaori dis
        voice "audio/voice/E1/D5/S4/Kaori/51.ogg"
        ki "What's that supposed to mean?" 
        pf "That you could look better."
        show kaori ann
        voice "audio/voice/E1/D5/S4/Kaori/52.ogg"
        ki "What's wrong with how I look now?" 
        pf "It's like you aren't even trying." 
        "Kaori clenches her jaw." 
        show vein:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D5/S4/Kaori/53.ogg"
        ki "I don't dress for you. I dress for me."

    "Don't say anything.":
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
        "Who cares about what she's wearing? I'm not wearing a uniform either. It's Saturday."

show kaori neu with dissolve
voice "audio/voice/E1/D5/S4/Kaori/54.ogg"
ki "Let's just go in." 
pf "You're the boss!" 

stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Electronics Store.ogg" fadein 3
scene bg store electronics day with fade

$renpy.pause(1.0)

"I follow Kaori into the electronics store."


"She heads straight for the aisle of tablets and points to the XY140."

show kaori neu at cc with dissolve
voice "audio/voice/E1/D5/S4/Kaori/55.ogg"
ki "There it is." 
pf "And there's mine." 
"I point to the Z90 and read the details." 
pf "Optic display with Hexa-HD resolution at 750 ppi with a V9Z chip and 256 bit architecture. It even has an antireflective coating on the screen. You must admit this is an amazing tablet. And…" 
"I point to the price on the XY140."
pf "... It's cheaper." 
"Kaori crosses her arms." 
show kaori ske with dissolve
voice "audio/voice/E1/D5/S4/Kaori/56.ogg"
ki "So? The XY140 costs a bit more because you get more. Look, it holds three times the number of files and even though the displays match, the XY140 has amazing video stabilization and built in data connection options." 

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    pf "Nothing you just said makes me believe it's worth the extra money." 
    show kaori ann
    voice "audio/voice/E1/D5/S4/Kaori/57.ogg"
    ki "I can't believe you want to get me an inferior model to {i}make up{/i} for breaking my stuff in the first place." 
    pf "It's not inferior! It's a great tablet." 
    voice "audio/voice/E1/D5/S4/Kaori/58.ogg"
    ki "But not comparable to my E85." 
    pf "Why are you so difficult?" 
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/59.ogg"
    ki "Why did you have to break my tablet?"
    pf "You're killing me."
    voice "audio/voice/E1/D5/S4/Kaori/60.ogg"
    ki "Serves you right for trying to kill me."

else:
    pf "The Z90 is still better." 
    show kaori ann
    voice "audio/voice/E1/D5/S4/Kaori/61.ogg"
    ki "It isn't, and since it's my tablet, I'm getting the XY140."
    pf "You're impossible." 
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/62.ogg"
    ki "And you're still wrong."

stop music fadeout 1.0
voice "audio/voice/E1/D5/S4/GosuElectronics/1.ogg"
rn "Just so you know, you're {i}both{/i} wrong." 
show exclamation:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori cur with dissolve
$renpy.pause(.5)
"Kaori and I turn to face the voice."

hide kaori with dissolve


show gosunerd extra at l2 with dissolve:
    xzoom -1

show kaori cur at r3 with dissolve
    
"Standing behind us is a stubby guy with round glasses. He reaches between us and grabs another model off the shelf." 
play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
voice "audio/voice/E1/D5/S4/GosuElectronics/2.ogg"
rn "This is the IB760 by Bensang. It's the fastest on the market with a vector core CPU at 6.00 GHz, redtooth technologies, and a fingerprint identity sensor in the screen. Not to mention the superior resolution with advanced multi-touch technology." 
"He reaches by and grabs something else."
voice "audio/voice/E1/D5/S4/GosuElectronics/3.ogg"
rn "Plus, it comes with the cover built in so you don't have to pay more to buy accessories." 

show gosunerd extra:
    xzoom 1

"He glances over at Kaori." 
voice "audio/voice/E1/D5/S4/GosuElectronics/4.ogg"
rn "Which, from what I heard, you could really use." 
"Kaori and I exchange a look." 

show kaori dis

voice "audio/voice/E1/D5/S4/Kaori/63.ogg"
ki "Nobody asked for your opinion." 
voice "audio/voice/E1/D5/S4/GosuElectronics/5.ogg"
rn "Clearly you need it if you're considering the XY140 like some sort of technological pleb."
show kaori ang
show vein:
    xoffset 1175
    yoffset 110
    xzoom .75
    yzoom .75
voice "audio/voice/E1/D5/S4/Kaori/64.ogg"
ki "Why you--!"
show kaori ann
pf "That's what I was saying all along! I told you the XY140 was no good."

show gosunerd extra:
    xzoom -1

voice "audio/voice/E1/D5/S4/GosuElectronics/6.ogg"
rn "Woah, calm down \"Mr. High and Mighty\", the Z90 is an even {i}worse{/i} choice!"
pf "What?"
voice "audio/voice/E1/D5/S4/GosuElectronics/7.ogg"
rn "Who would want to use a machine built on the Frame operating system? The last time that piece of junk worked was Frame XP!"
pf "Frame 7 was good!"
"He snickers loudly."
voice "audio/voice/E1/D5/S4/GosuElectronics/8.ogg"
rn "How cute. No wonder you're together, you both have a taste for inferior tablets."

show kaori sur b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/65.ogg"
ki "Together?!"

show kaori ang b1:
    xzoom -1
    easein .5 xoffset -150
    
$renpy.pause(.15)
    
show gosunerd extra:
    xzoom 1
    easein .33 xoffset -70

$renpy.pause(.5)
"Kaori stomps a foot forward as her hands clench into fists. The nerd is clearly shaken but tries to keep his cool."
voice "audio/voice/E1/D5/S4/Kaori/66.ogg"
ki "You have no idea what you're talking about!"
show kaori ann b1
pf "No kidding! Macrohard has the entire business market."
voice "audio/voice/E1/D5/S4/Kaori/67.ogg"
ki "And Pineapple makes premium, cutting edge devices!"
pf "Also, nowadays, all models come with Redtooth 3.0 built in!"
voice "audio/voice/E1/D5/S4/Kaori/68.ogg"
ki "And fingerprint ID sensors, and advanced multi-touch technologies!"
"He opens his mouth to speak again but Kaori interrupts him." 
show kaori ang b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/69.ogg"
ki "And we are not together!"
show kaori dis b1 with dissolve
pf "Yeah, go mind your own business!"
voice "audio/voice/E1/D5/S4/GosuElectronics/9.ogg"
rn "You n00bs! Your vision is too clouded to see the light! Otherwise you'd understand that Andzoid is the best hardware, software, {i}and{/i} value for your money!"

hide gosunerd extra with dissolve
$renpy.pause(.5)

"Before either of us can say another word, he turns around and confidently waddles away. A bag of cheese puffs seem to materialise in his hand."
hide kaori with dissolve
show vein:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori ann at cc with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S4/Kaori/70.ogg"
ki "Idiot! Sticking his nose where it doesn't belong." 
pf "I know, right?"
$renpy.pause(.5)
show kaori thi with dissolve
stop music fadeout 3.0
"We fall silent as I look over the IB760 demo model."

$renpy.pause(1.0)
"..."
pf "Actually Kaori…"
show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/71.ogg"
ki "What?" 
pf "I think he might have been onto something." 
voice "audio/voice/E1/D5/S4/Kaori/72.ogg"
ki "Let me see." 
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
"We both review the \"specifications\" card next to the tablet."
show kaori cur
voice "audio/voice/E1/D5/S4/Kaori/73.ogg"
ki "Huh, the features here definitely outweigh the XY140…" 
pf "And hardware-wise it blows the Z90 out of the water."
"I watch as Kaori swipes the tablet screen and tweaks the settings and configuration. A moment later, she grabs an IB760 box off the shelf and looks it over."
pf "So... Do you want this one then?" 
show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/74.ogg"
ki "As much as I hate to admit it, it makes the most sense."
pf "Just don't let {i}him{/i} hear you saying that."

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    hide kaori with dissolve
    "I take the tablet from her and head to the counter." 
    pf "Glad we got that sorted out." 
    show kaori neu at l3 with dissolve
    "As I go to pay, Kaori cuts me off from the cashier and pulls out her wallet."
    pf "Uh?" 
    voice "audio/voice/E1/D5/S4/Kaori/75.ogg"
    ki "Whatever, I don't need you to pay for it."

    menu:
        "I still need to take responsibility.":
            "I shake my head."
            pf "No, but it's still my fault you need to buy a new one in the first place."
            show kaori sur with dissolve
            "Before she has a chance to reply, I tap my card against the register. An \"Approved\"! notification displays on the machine."
            show kaori ske
            show exclamation:
                xoffset 230
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D5/S4/Kaori/76.ogg"
            ki "Y-You idiot! I just let you off the hook and you paid anyways…"
            "I flash her a smile."
            pf "Oh well, too late now."
            show kaori cur b1 with dissolve
            "Kaori appears flustered. I offer the bag to her."
            pf "Here."
            show kaori neu b1
            "She blinks at the bag a few times before reluctantly accepting it. I'm glad after that whole choosing a tablet ordeal she doesn't fight me on this too. I guess she understands that we're both equally stubborn."
            voice "audio/voice/E1/D5/S4/Kaori/77.ogg"
            ki "... Thanks."

        "I won't argue against that!":
            pf "A strong independent woman who don't need no man! I like it."
            show kaori dis
            voice "audio/voice/E1/D5/S4/Kaori/78.ogg"
            ki "Wow, I try to do something nice and you still manage to be a complete ass."
            pf "What? I didn't mean it sarcastically!"
            show kaori ann
            "She glares at me, then pays for the tablet and grabs the bag."

        "I'll pay for part of it.":
            pf "Let me cover half. You might be getting an upgrade but it's my fault you have to make the purchase sooner rather than later."
            show kaori thi
            "She mulls the thought over."
            pf "At least that way we can call it even and you won't hold this over my head."
            show kaori neu
            voice "audio/voice/E1/D5/S4/Kaori/79.ogg"
            ki "Fine."
            "The cashier sets up the bill and we both tap our respective cards. Kaori grabs the bag shortly after."
            voice "audio/voice/E1/D5/S4/Kaori/80.ogg"
            ki "Thanks, I guess."
            pf "No problem."

else:
    hide kaori with dissolve
    "She takes the tablet and heads to the counter." 
    show kaori neu at l3 with dissolve
    
    pf "Glad we got that sorted out."
    voice "audio/voice/E1/D5/S4/Kaori/81.ogg"
    ki "Me too."
    "Kaori pulls out her wallet and pays for it."

"We exit the store."
    
stop ambient fadeout 3.0
scene black with fade
$renpy.pause(1.5)
play ambient "audio/ambience/Mall.ogg" fadein 3
scene bg mall main day with fade

$renpy.pause(1.0)

show kaori neu at cc with dissolve
$renpy.pause(.25)

"Kaori turns towards me outside the store."
show kaori thi at cc with dissolve
$renpy.pause(.5)
voice "audio/voice/E1/D5/S4/Kaori/82.ogg"
ki "Thanks for coming out, I guess… I mean, some of the stuff you said was helpful, but mostly you just gave me a headache."
"I grin at her."
pf "You're really bad at giving compliments."
show tsuBlush:
    xoffset 720
    yoffset 110
    xzoom .75
    yzoom .75
show kaori ann b1 with dissolve
voice "audio/voice/E1/D5/S4/Kaori/83.ogg"
ki "It wasn't a compliment!"
"But I can see a blush creeping up her cheeks."
pf "Anyway, don't worry about it. We're teammates which means we look out for each other, right?"
show kaori neu b1
voice "audio/voice/E1/D5/S4/Kaori/84.ogg"
ki "Yeah, that's how we were able to defeat that loser when he came by."
pf "Ha! Did you see how he left in a huff?"
show kaori mis b1
voice "audio/voice/E1/D5/S4/Kaori/85.ogg"
ki "Maybe that'll teach him to stop butting in where he doesn't belong."
"I laugh, and I think I see Kaori crack a smile."

if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S3_MetKaoriWasNice == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
    pf "So, are we good?"
    show kaori neu at cc with dissolve
    voice "audio/voice/E1/D5/S4/Kaori/86.ogg"
    ki "Huh?"
    pf "You know--about that whole almost running you over thing."
    show kaori cur
    voice "audio/voice/E1/D5/S4/Kaori/87.ogg"
    ki "Oh."
    "She glances at her bag and nods."
    show kaori neu
    voice "audio/voice/E1/D5/S4/Kaori/88.ogg"
    ki "Yeah, we're good."
    pf "Cool, because I don't want to start this friendship on a sour note."
    "She blinks at the mention of \"friendship\" and waves off what I said."

else:
    pf "At least now you can email me those strategies."
    show kaori neu with dissolve
    voice "audio/voice/E1/D5/S4/Kaori/89.ogg"
    ki "Heh, yeah. I'll send them over once I get this thing set up."
    pf "You gonna need advice on how to do that too?"
    "She puts a hand on her hip."
    show kaori dis
    voice "audio/voice/E1/D5/S4/Kaori/90.ogg"
    ki "No."
    "I smile at her stern expression."
    pf "It was a joke, Kaori. That's what friends do. They joke around with each other."
    show kaori neu with dissolve
    "She blinks at the mention of \"friends\" and the frown eases off her face."

show kaori neu
voice "audio/voice/E1/D5/S4/Kaori/91.ogg"
ki "Whatever, I better get going. See you on Monday."
pf "Yeah, see you."
hide kaori with dissolve
"With a nod, she turns away and disappears into the crowd of people."



stop music fadeout 3.0
stop ambient fadeout 3.0
scene black with fade
"I head in the opposite direction towards a GEAR equipment store I've been meaning to check out. "
"Once it gets late, I head home."

        
        
$renpy.pause(2.0)   



jump E1D5S7