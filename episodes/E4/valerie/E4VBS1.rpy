#EVENING EVENT
label E4VBS1:

$ valHairF = "default"
$ valHairB = valHairF
$ valOut = "sFashion"




"I bet Valerie would want to hang out. I decide to give her a call."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL1.ogg"
vb "Hey there, I was just thinking about you."
pf "Oh really?"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL2.ogg"
vb "Yup. I was just thinking how fun it would be to go dancing… but I need a partner. You in?"

menu:
    "I was born to dance.":
        $ E4VBS1_DanceMachine = 1
        pf "Definitely! I've got some sick moves on the dancefloor."
        "Valerie laughs."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL3.ogg"
        vb "I'll have to see it to believe it."
        pf "Trust me, you'll be impressed."

    "Eh, I'm not much of a dancer.":
        pf "I don't think I'd make a good dance partner."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL4.ogg"
        vb "So? It doesn't matter if you're good or not as long as you have fun."
        pf "If you need someone to stand on the sideline and watch everyone else dance, I can do that."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL5.ogg"
        vb "Alright, but I bet I can get you dancing before the night's done."
        pf "Good luck."

pf "Is this going to be on campus?"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL6.ogg"
vb "Haha! You're funny. I'll text you the address. See you soon!"
"She hangs up, and a few seconds later my phone buzzes with a text."

scene black with fade
stop ambient fadeout 3
stop music fadeout 3

"I get changed into something more comfortable which I can still move in, then drive to the address."
scene bg nightclub with fade
"As I get close, I see a line of people waiting out front as a bouncer checks everyone's ID. This is not what I expected…"
if valrelatonship == 1:
    "Valerie stands right out front and greets me with a kiss."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    show valerie hap at l3 with dissolve:
        xzoom -1
    
    pf "Looks like someone's happy to see me."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL7.ogg"
    vb "Took you long enough to get here."
else:
    "Valerie stands right out front and waves me over."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    show valerie hap at l3 with dissolve:
        xzoom -1
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL8.ogg"
    vb "Finally you're here! I almost thought you weren't coming."

pf "Are we at a club?"
show valerie dis
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL9.ogg"
vb "Obviously. Where do you think people go dancing?"
pf "I thought you were talking about a dance class."
show valerie hap
"Valerie laughs."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL10.ogg"
vb "Nope."
"I glance at the bouncer up ahead as he turns away a couple of underage girls."
pf "How do you expect to get in?"
show valerie smi
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL11.ogg"
vb "With my ID, of course."
"She pulls out her ID, which labels her as 20."
pf "Where did you get that?!"
show valerie mis
"She smirks."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL12.ogg"
vb "I have my ways."

menu:
    "You should be careful.":
        pf "Maybe this isn't a good idea. He might know it's a fake."
        if valrelatonship == 1:
            "Valerie places her hand on my arm and gives me a reassuring smile."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL13.ogg"
            vb "Hey, don't worry. It's always worked in the past."
            pf "Uh, how many times have you done this before?"
            "She grins and kisses my cheek."
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL14.ogg"
            vb "Don't worry!"
        else:
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL15.ogg"
            vb "He won't know. Trust me, I've done this before."
            pf "That isn't very reassuring."
        "I hope Valerie knows what she's doing…"

    "It's better than my old fake.":
        pf "Whoa! That's way better than my old fake."
        show valerie cur
        "Valerie looks intrigued."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL16.ogg"
        vb "You had a fake too?"
        pf "Sure, how else would I get into bars back in the States?"
        show valerie mis
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL17.ogg"
        vb "Oh yeah, now who's the underaged one?"
        pf "Says the girl holding a fake."
        show valerie sur
        "Valerie puts a finger to my lips."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL18.ogg"
        vb "Not so loud!"

    "Let me take a closer look.":
        pf "Let me see that."
        show valerie cur
        "I snatch the ID out of Valerie's hand and bring it close to my face. {w}Huh… this is actually very realistic."
        show valerie smi
        "Valerie smirks."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL19.ogg"
        vb "Pretty good, right?"
        pf "You might be able to get away with it."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL20.ogg"
        vb "May I have it back now?"
        "I hand it over."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL21.ogg"
        vb "Thank you."

pf "Aren't we going to get in line?"
show valerie hap
"Valerie laughs."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL22.ogg"
vb "Who stands in line?"
hide valerie with dissolve
"She strides right up to the bouncer and flashes him an irresistible smile. Then she slips her ID into his hands."
"He grins appreciatively at her and waves her in, but stops me as I try to follow."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL23.ogg"
vb "He's with me."
"Valerie touches the bouncer's arm, and gives him a sultry look."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL24.ogg"
vb "It would make me really happy if you let him in too."
"He sighs, and checks my ID, then waves me in."
if valrelatonship == 1:
    "I'm not thrilled about the way she looked at the bouncer, but it beats standing in line."
"Valerie winks as we slip past the bouncer and into the club. I squint in the dim bar as my heart pulses in time with the bass. The place has a decent crowd for this time of night."
show valerie smi at cc with dissolve
"I migrate towards the bar and order a drink and something age appropriate for Valerie. She accepts the drink with an amused glint in her eyes."
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL25.ogg"
vb "Come on, let's dance!"
"She grabs my hands and pulls me to the dance floor."

if E4VBS1_DanceMachine == 1:
    "Valerie swings her hips in time to the beat and bounces in rhythm to the music. She smiles at me."

else:
    "I pull back."
    pf "Hey! I don't dance remember?"
    show valerie dis
    "She pouts."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL26.ogg"
    vb "Are you really going to make me dance alone?"
    pf "You knew what you were getting into when you asked me to come."
    if valrelatonship == 0:
        show valerie hap
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL27.ogg"
        vb "Too bad. You don't get a choice."
        "She grabs my hand and pulls me onto the dance floor, then she swings her hips in time to the beat and bounces in rhythm to the music."
        "I sigh in defeat and begin tapping my toes. Once I feel more confident, I join Valerie in moving my hips."
        show valerie mis
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL28.ogg"
        vb "I told you I'd get you to dance."
        pf "You win."
        "She smirks."

    if valrelatonship == 1:
        show valerie sad
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL29.ogg"
        vb "Are you sure you want your cute girlfriend dancing alone… essentially up for grabs for any other guy…?"

        menu:
            "I won't let her dance alone!":
                pf "On second thought, maybe I will dance."
                show valerie smi
                "Valerie smiles, then swings her hips in time to the beat and bounces in rhythm to the music."
                "I meet her gaze and grin as I appreciate the way her body moves, then join in."

            "Nope, not happening.":
                "I scoff."
                pf "That's not going to happen."
                show valerie mis
                "Valerie grins."
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL30.ogg"
                vb "That's what you think!"
                "She grabs my hand and pulls me onto the dance floor, then she swings her hips in time to the beat and bounces in rhythm to the music."
                "I sigh in defeat and begin tapping my toes. Once I feel more confident I join Valerie in moving my hips."
                "Alright, time to bust a move!"

                
menu:
    "Do what seems fun!":
        "Who cares if I'm good or not? I'm just going to do what feels right!"
        show valerie cur
        "I sway my body in whichever way the music takes me. Sometimes my limbs don't respond quite the way I thought they would and my movements seem a little jerky and uncoordinated."
        "Valerie giggles."
        if E4VBS1_DanceMachine == 1:
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL31.ogg"
            vb "Are these your \"sick\" moves?"
            pf "That depends. Are you impressed yet?"
            "She giggles again."
            if valrelatonship == 1:
                show valerie mis
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL32.ogg"
                vb "Hmm, it's a good thing you're cute."
            else:
                show valerie smi
                voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL33.ogg"
                vb "It's very original."
                
        else:
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL34.ogg"
            vb "Are we having fun yet?"
            "I nod. This wasn't so bad afterall!"

    "Bust out the hip hop skills!":
        show valerie cur
        "That one hip hop class I accidentally took is finally going to pay off! I throw out my best moves and show her I can dougie, whip, nae nae, and wrap things up nicely with the shuffle."
        "Valerie pauses her dancing to admire me."
        if E4VBS1_DanceMachine == 1:
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL35.ogg"
            vb "Whoa! You weren't kidding when you said you had moves!"
            pf "I tell it like it is."
        else:
            show valerie hap
            voice "audio/voice/MISSING/BATCH4/Valerie/ValE4Redos/ValE4Redo4.ogg"
            vb "Hey! You're really good! What were you so shy about?"
            pf "I said I don't dance, not that I don't know how to."

    "Just rock back and forth.":
        "Everyone knows the only way to dance in clubs is to just step from side to side. Valerie watches me and grins."
        show valerie smi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL36.ogg"
        vb "Ah, the good old side step."
        pf "Yup."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL37.ogg"
        vb "Classic."

    "Chicken dance!":
        "I decide to wow Valerie with the one dance I know. I cluck my hand-beaks, flap my arm-wings, and wiggle my \"tail feathers\"."
        show valerie ske
        "Valerie laughs nervously and stops me."
        show valerie thi
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL38.ogg"
        vb "Oookay! Unless you're a sandwich, a club is no place for a chicken."
        pf "Aw, but that's my signature move."
        if valrelatonship == 1:
            "She pulls me close and moves my hips to rock with her own."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL39.ogg"
            vb "Let me show you how it's done."
        else:
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL40.ogg"
            vb "I can show you some new ones."

show valerie smi
"After dancing together for a while, I feel thirsty."
pf "I'm going to get another drink. You want anything?"
"Valerie shakes her head."
pf "Okay, I'll be right back."
show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL42.ogg"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL41.ogg"
vb "I'll be here."
hide valerie with dissolve
stop music fadeout 4
"I return to the bar and order a water, then chug it in one long gulp. {w}Dancing is hard work. I feel like I'm getting a workout!"
"As I go find Valerie, some random guy corners her."
show valerie neu at r3 with dissolve
show bully extra at l3 with dissolve
voice "audio/voice/E4/Creep/E4/Valerie/1.ogg"
creep "What's a pretty thing like you doing in a place like this?"
"Valerie forces a smile and steps away from him."
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL43.ogg"
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL42.ogg"
vb "Sorry, but I have a boyfriend."
voice "audio/voice/E4/Creep/E4/Valerie/2.ogg"
creep "Aw, I'm just talking to you. That's not a crime, is it? How about I buy you a drink?"
"What a vulture! I step away for one minute…"

if valrelatonship == 1:
    menu:
        "Confront the guy directly.":
            "I step up to him and tap him on the shoulder."
            show valerie cur
            pf "Back off. She just said she's not interested."
            voice "audio/voice/E4/Creep/E4/Valerie/3.ogg"
            creep "This doesn't concern you."
            pf "Yes, it does, considering I'm the boyfriend."
            "He looks skeptically at Valerie."
            voice "audio/voice/E4/Creep/E4/Valerie/4.ogg"
            creep "{i}This{/i} guy?"
            show valerie mis
            "My hands ball into fists, but Valerie snakes her hands around my arm and leans her head on my shoulder."
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL43.ogg"
            vb "Yup, this guy."
            hide bully extra with dissolve
            "He mumbles something unintelligible then slinks back into the crowd."

        "Use his own strategy against him.":
            show valerie cur
            pf "Hey there, what's a pretty thing like you doing in a place like this?"
            "The guy whirls around and glares at me."
            voice "audio/voice/E4/Creep/E4/Valerie/5.ogg"
            creep "Go away. I'm not interested."
            show valerie mis
            pf "Aw, don't be like that. It's not a crime to talk, is it? How about I buy you a drink?"
            voice "audio/voice/E4/Creep/E4/Valerie/6.ogg"
            creep "Back off, I'm here with someone."
            "Valerie suddenly looks intrigued."
            show valerie cur
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL44.ogg"
            vb "You are?"
            voice "audio/voice/E4/Creep/E4/Valerie/7.ogg"
            creep "Uh… yeah… you, of course."
            "Valerie points at me."
            show valerie thi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL45.ogg"
            vb "That's so strange because I'm here with him."
            voice "audio/voice/E4/Creep/E4/Valerie/8.ogg"
            creep "What?"
            "I sling my arm around Valerie and she places her hand on my chest."
            show valerie hap
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL46.ogg"
            vb "Meet my boyfriend."
            voice "audio/voice/E4/Creep/E4/Valerie/9.ogg"
            creep "Forget it."
            hide bully extra with dissolve
            "He slinks back into the crowd."

        "Let Valerie handle it.":
            "I'm positive Valerie gets unwanted attention all the time. I stand behind the guy, but don't say anything, curious to see how she handles it."
            show valerie smi
            "Valerie glances at me and smirks. She refocuses her attention on the guy."
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL47.ogg"
            vb "When you put it that way how can I refuse?"
            voice "audio/voice/E4/Creep/E4/Valerie/10.ogg"
            creep "Great! What are you drinking?"
            show valerie mis
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL48.ogg"
            vb "Surprise me."
            hide bully extra with dissolve
            "As the guy heads towards the bar, Valerie grabs my hand and drags me away."
            show valerie smi
            voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL49.ogg"
            vb "Let's move before he comes back."
            "I let out a laugh at Valerie's mischievous grin."

    hide valerie with dissolve
    "We sit down and rest for a few more minutes. That guy sure knows how to ruin a mood. Still, I'm surprised Valerie let him off the hook so easily…" 
    show valerie cur at cc with dissolve
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL50.ogg"
    vb "Hello...?"
    "Her voice jolts me out of my thoughts."
    pf "Oh, sorry, I was still annoyed by that dude from earlier."
    show valerie neu
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    "Valerie frowns."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL51.ogg"
    vb "Don't even waste your time thinking about someone like that. Besides, we have more fun things to do!"
    show valerie hap
    "I smile and nod. She's right. She grins and interlaces her fingers with mine."


else:
    "I stand behind the guy, about to say something when Valerie glances at me and smirks. Then she refocuses on the guy."
    show valerie neu
    voice "audio/voice/MISSING/BATCH4/Valerie/ValE4Redos/ValE4Redo5.ogg"
    vb "Just one drink?"
    voice "audio/voice/E4/Creep/E4/Valerie/11.ogg"
    creep "That's right. Just one drink."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL52.ogg"
    vb "Mmm, okay. Surprise me."
    hide bully extra with dissolve
    "As the guy heads to the bar, Valerie darts towards me and leads me away."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL53.ogg"
    vb "Come on! Before he comes back."
    hide valerie with dissolve
    "I laugh as Valerie leads me to the far end of the club. We sit on a couple of free stools and rest."
    show valerie dis at cc with dissolve
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL54.ogg"
    vb "What a creep, right?"
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    pf "Yeah… nice strategy telling him you have a boyfriend. Too bad it didn't work."
    show valerie cur
    "Valerie gives me a strange look."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL55.ogg"
    vb "What do you mean \"strategy\"?"
    pf "Well, you don't have one, do you?"
    show valerie neu
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL56.ogg"
    vb "Of course I do."
    show valerie smi
    "She's joking, right? Valerie makes all kinds of jokes… {w}But her face holds no hint of a teasing smile."
    pf "Wait, seriously? How come I'm only finding out about this now?!"
    show valerie thi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL57.ogg"
    vb "You never asked before."
    pf "If you have a boyfriend, then why did you invite me to clubbing instead of him?"
    show valerie mis
    "Valerie's teasing smirk appears."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL58.ogg"
    vb "To make him jealous."
    "I frown."
    pf "Valerie…"
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL59.ogg"
    vb "I'm just kidding! No need to look so serious."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL60.ogg"
    vb "I did invite him, but he's out of town."
    pf "How convenient…"
    show valerie dis
    "She pouts."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL61.ogg"
    vb "Aw, that sounds like you don't believe me. I'm hurt!"
    "She pulls out her phone and shows me a text message string."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL62.ogg"
    vb "See for yourself."
    "The first text is from Valerie."
    "{i}Aww, since you won't be here, I'm going out with [pfirst] tonight. I miss you! xoxo{/i}"
    "He replied…"
    "{i}I miss you too! Be safe and have fun but not too much fun ;){/i}"
    "{i}Don't worry, the real fun won't start until you get back ;) I've got a special treat for--{/i}"
    show valerie mis
    "Valerie snatches the phone out of my hands."
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL63.ogg"
    vb "The rest is a private conversation."
    pf "Okay, I'm convinced you're telling the truth."
    show valerie smi
    "Valerie grins and stands."

show valerie hap
voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL64.ogg"
vb "Break's over, mister. Let's dance some more!"

hide valerie with dissolve
"We dance until our feet grow tired and we can't dance anymore. As we walk out of the club, Valerie leans into me to ease her aching feet."

if valrelatonship == 1:
    "Reminiscent of our first outing together, I scoop her up into my arms."
    show valerie sur b1 at cc with dissolve
    "She gasps in surprise, then laughs and throws her arms around my neck as I carry her back to my bike."
    show valerie cur b1
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL65.ogg"
    vb "I'm getting a strong feeling of deja vu."
    pf "Oh?"
    
    "I kiss her on the lips. When I pull away, her cheeks are pink."
    show valerie smi b2 with dissolve
    voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL66.ogg"
    vb "Okay, that was new."
    
else:
    "Valerie pauses and slips her heels off. She pulls out a pair of comfortable shoes from her bag."
    show valerie smi at cc with dissolve
    if E2VBS4_Completed == 1:
        "She grins at me."
        voice "audio/voice/E4/Valerie/ValE4ValerieArc/ValE4ValerieArcL67.ogg"
        vb "I learned my lesson from my shoe mishap at the park."
        "I laugh while she puts on her shoes. Then we walk to my bike."
        
    else:
        "She seems overly prepared for this. How often does she go out dancing?"

scene black with fade

"When we arrive at my bike, Valerie and I both climb on. After I drop Valerie off at ACE, I head home. Although tonight wasn't at all what I expected, I still ended up having a good time."


stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4VBS1_Completed = 1