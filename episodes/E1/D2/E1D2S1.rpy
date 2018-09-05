label E1D2S1:
    
    $renpy.pause(2.0)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1.5)
    #BG Black background transition into daytime room background but hazy / unfocused.
    scene bg homekaito myroom blurry with Dissolve(2.5)
    scene black with fade
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    pf "Что…?"
    scene bg homekaito myroom blurry with fade
    "Мягкие солнечные лучи проходят через окно, грея мою щёку. Мелодичное пение птиц вдалеке почти утоплено в раздражающем звуке будильника."
    "Я отвернулся от окна и увидел \"7:00 AM\" на часах."
    pf Неужели уже утро?"
    
    menu:
        "Так и есть. Пора вставать":
            $ E1D2S1_timetogetup = 1
            $ E1D2S1_okaytimetogo = 0
            $ E1D2S1_almostup = 0
            stop sound
            play sound "audio/sfx/Technology/Button Click.ogg"
            "Я выключил будильник. Я никогда не был жаворонком, но вообще-то я не чувствую себя таким же уставшим как обычно… Я даже чувствую себя переполненным энергией. {w}Полагаю, джетлаги как-то странно работают. По крайней мере, я не опоздаю в свой первый день." 
            scene white with fade
            scene bg homekaito myroom day with Dissolve(2)
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
            
            "Встав с кровати, я на автомате начал свой утренний ритуал. Не раздумывая, я взял джинсы и почти надев их заметил форму, валяющуюся на стуле."
            pf "Чёрт…"
            "К этому придётся привыкнуть…"
            "Я снял джинсы и взял форму. Должен пирзнать, что касается формы, эта довольно-таки неплоха. Она немного яркая для моего вкуса и, совсем не то, чего я ожидал, но разрез льстит, а тиановые полосы выглядят довольно круто."
            "Я взглянул в зеркало, чтобы поправить галстук. {w}Узел мог бы быть лучше, но у меня не было много случаев, в которых мне нужно было одевать гастук {w}Я всё ещё выгляжу чертовски хорошо, это всё, что имеет значение."
            "После быстрой проверки, чтобы убедиться, что собрал все вещи, я спустился вниз." 
            scene black with fade
            play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
            $renpy.pause(3)
    
        "Ещё 5 минут...":
            stop sound
            play sound "audio/sfx/Technology/Button Click.ogg"
            "I smash the \"snooze\" button and am rewarded with blissful silence. {w}Just five more minutes and I'll be ready to face the world."
            scene black with fade
            "…"
            play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
            $renpy.pause(3)
            "That could {b}not{/b} have been five minutes.{w} Why do you hate me, clock?"
    
            menu:
                "Okay, time to go.":
                    $ E1D2S1_timetogetup = 0
                    $ E1D2S1_okaytimetogo = 1
                    $ E1D2S1_almostup = 0
                    stop sound
                    play sound "audio/sfx/Technology/Button Click.ogg"
                    "Fine, I'll get up now. {w}If I stay here any longer I might never leave."
                    scene bg homekaito myroom blurry with fade
                    scene white with fade
                    scene bg homekaito myroom day with Dissolve(2)
                    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
                
                    "Mustering willpower and determination, I heave myself out of my warm bed. {w}Mornings and I have never really seen eye-to-eye, and I stumble around my room as animated as a zombie. I automatically throw my things into my bag and hope that I've gotten everything I need. {w}I think I have. {w}If I haven't, I guess I'll find out at school."
                    "I finish dressing myself in jeans and a T-shirt and am about to go downstairs, when I notice the dark uniform laying over my chair."
                
                    "Whose idea was it to force everyone into uniforms anyway?"
                
                    "I sigh and slip into my uniform. {w}I can't even remember the last time I needed a tie or a suit jacket… or even slacks."
                    "Well, whatever. {w}Feeling a little more like a living person, I grab my bag and head downstairs."
                    scene black with fade
                    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
                    $renpy.pause(3)
            
                "I'm almost up… zzz...":
                    $ E1D2S1_timetogetup = 0
                    $ E1D2S1_okaytimetogo = 0
                    $ E1D2S1_almostup = 1
                    stop sound
                    play sound "audio/sfx/Technology/Button Click.ogg"
                    "I smash the \"snooze\" button again. {w}Mornings were not meant to be seen. {w}I can afford to stay here a little longer, right? {w}It won't take me that long to get ready. {w}I'll just sleep another five minutes… {w}maybe ten…"
                    $renpy.pause(3)
                    "…"
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                    "Something jabs my side."
                    
                    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
                    voice "audio/voice/E1/D2/S1/Nikki/1.ogg"
                    sf "Hey! Wake up! You’re going to be late!"
                
                    "Ugh, who is this harpy screeching in my ear? {w}Go away…"
                    voice "audio/voice/E1/D2/S1/Nikki/2.ogg"
                    sf "Do you really want to be late on your first day?"
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                
                    "Oh, right... {w}school. {w}I'll be fine. {w}There's still time."
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                
                    "But the jabs to my side are persistent. Over and over and {i}over{/i} again."
                    
                    play sound "audio/sfx/Human/Poke Noise.ogg"
                    $renpy.pause(1)
                
                    pf "Stop it… {w}Stop--Nikki!" 
                    stop music fadeout 3
                    scene bg homekaito myroom blurry
                    scene white with fade
                    scene bg homekaito myroom day with Dissolve(2)
                    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
                    show nikki smi at cc with dissolve
                
                    "I pull the blankets down and am greeted by my sister's face inches from my own."
                    show note:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E1/D2/S1/Nikki/3.ogg"
                    sf "Good morning, princess."
                    "I glare daggers at her, but she deflects them with a smile."
                
                    show nikki mis at cc
                    voice "audio/voice/E1/D2/S1/Nikki/4.ogg"
                    sf "How nice of you to finally join the world of the living. I almost thought you'd died in there with how long it took me to wake you."
                
                    pf "Ugh."
                    
                    show nikki hap at cc
                    voice "audio/voice/E1/D2/S1/Nikki/5.ogg"
                    sf "Aren't you glad I came in here and woke you?"
                
                    pf "I guess."
                    
                    show nikki smi at cc
                    voice "audio/voice/E1/D2/S1/Nikki/6.ogg"
                    sf "Mmhm. Now what would you do without me?"
                
                    pf "Sleep."
                    
                    show nikki ann at cc
                    $renpy.pause(.5)
                    show storm:
                        xoffset 720
                        yoffset 160
                        xzoom .75
                        yzoom .75
                    $renpy.pause(1)
                    "She crosses her arms and gives me a stern look."
                    voice "audio/voice/E1/D2/S1/Nikki/7.ogg"
                    sf "No more sleeping! You need to eat before we go. I know what you're like when you're hungry, and I wouldn't subject anyone to that kind of torture."
                
                    "She throws off my blankets and heads for the door."
                    show nikki dis at cc
                    voice "audio/voice/E1/D2/S1/Nikki/8.ogg"
                    sf "I'll go fix us breakfast. Don't you even think of falling back asleep!"
                    
                    hide nikki with dissolve
                
                    "Who, me? {w}Just who does she think she's talking… to..."
                
                    #FX: Maybe have a small black fade in and out here to simulate him nearly dozing off again?
                    scene black with Dissolve(2.5)
                    scene bg homekaito myroom day with fade
                
                    "Whoa--that was close."
                    "… {w}I really should get up now."
                
                    "Yawning, I let out a small groan as I stretch, and practically fall out of bed. {w}Once my legs remember how to work, I begin gathering all of my things. {w}While stumbling around the room, I bump into my chair and my uniform slides to the dusty floor."
                    pf "Great. Let's look like the new homeless student."
                    "I shake out my uniform and am successful in getting most of the dust off of it. Good enough."
                    "Nothing about this uniform feels natural. Nobody my age wears a suit and tie everyday--because that's basically what this is. {w}Plus, the material is pretty stiff, but I guess that's the price you pay for looking sharp."
                    "After successfully dressing myself, I run my hands through my hair, trying to flatten most of it down, before grabbing my bag and heading downstairs."
                    scene black with fade
                    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
                    $renpy.pause(3)
    
    stop ambient fadeout 2.0
    #BG kaito house day
    $renpy.pause(1)
    scene bg homekaito main day with fade
    $ nikOut = "sUniform"
        
    if (E1D2S1_timetogetup == 1) or (E1D2S1_okaytimetogo == 1):
        if (E1D2S1_timetogetup == 1):
            "I soon arrive in the kitchen, eager to begin my day. Waking up successfully at this hour feels kind of like a big accomplishment."
            show nikki smi at cc with dissolve
            "Nikki stifles a yawn as she sets down a plate of eggs and toast. {w}Suddenly, I don't feel so accomplished."
            pf "Did you make one for me too?"
            show nikki cur at cc with dissolve
            $renpy.pause(1)
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            $renpy.pause(2.5)
            "She blinks in surprise and it takes a moment for her to respond."
            show nikki hap at cc with dissolve
            voice "audio/voice/E1/D2/S1/Nikki/9.ogg"
            sf "As a matter of fact, I did!"
            "She grins, and places another plate down on the table."
            show nikki cur at cc
            voice "audio/voice/E1/D2/S1/Nikki/10.ogg"
            sf "Look at you, big bro, waking up bright and early. You're taking \"starting over\" to the next level."
            pf "Hey, I try."
            pf "Where's Uncle Kaito?"
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/11.ogg"
            sf "He already left for work so we'll have to lock up when we leave."
            "I nod, and she sidles over to me, wearing a playful look." 
    
        elif (E1D2S1_okaytimetogo == 1):
            show nikki neu at cc with dissolve
            "Stifling a yawn, I saunter into the kitchen and see Nikki at the table nibbling on some toast. She sees me enter and her face lights up."
            show nikki hap at cc
            voice "audio/voice/E1/D2/S1/Nikki/12.ogg"
            sf "Good, you're up! I was just about to go get you."
            pf "Well, I'm here."
            voice "audio/voice/E1/D2/S1/Nikki/13.ogg"
            sf "I made toast. Want some?"
            pf "Mmhm."
            "I sit down at the table but she just laughs."
            show nikki smi at cc
            voice "audio/voice/E1/D2/S1/Nikki/14.ogg"
            sf "It's in the toaster. Go get it yourself."
            "Grumbling, I pick up the toast from the toaster and take a bite."
            pf "No Uncle Kaito?"
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/15.ogg"
            sf "He already left for work."
            pf "Mm."
            "I'm enjoying the silence when Nikki sidles up to me wearing a playful grin." 
    
        show nikki smi at cc
        "In her white shirt and plaid skirt, she does a little twirl and looks expectantly at me."
        voice "audio/voice/E1/D2/S1/Nikki/16.ogg"
        sf "Sooo?"
    
        menu:
            "She does look cute... This is going to make my job hard.":
                "I cross my arms and scowl."
                show nikki ner at cc
                voice "audio/voice/E1/D2/S1/Nikki/17.ogg"
                sf "What?"
                pf "No."
                show panic:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/18.ogg"
                sf "No?"
                pf "No, that won't work."
                show nikki wor at cc
                voice "audio/voice/E1/D2/S1/Nikki/19.ogg"
                sf "What's wrong?"
                "Worry furrows her brow as Nikki starts fidgeting with her uniform."
                show nikki sad at cc
                pf "Oh, nothing. I was just trying to figure out the best way to bring my GEAR to your school."
                show nikki ske at cc
                "She raises her brow in question."
                pf "Well, how else am I going to keep all the boys away from you?"
                show nikki smi b1 at cc with dissolve
                show regBlush:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                "Nikki giggles, and a soft pink tinges her cheeks."
                voice "audio/voice/E1/D2/S1/Nikki/20.ogg"
                sf "You're being ridiculous."
                pf "I'm even considering writing your school a strongly worded letter."
                voice "audio/voice/E1/D2/S1/Nikki/21.ogg"
                sf "Oh no, let it not come to that!"
                "I smile, but Nikki sees the concern in my eyes."
                show nikki neu at cc
                voice "audio/voice/E1/D2/S1/Nikki/22.ogg"
                sf "I'll be fine. I'm a big girl now, I can handle myself."
                pf "Yeah, you're right."
                "But as an older brother, my instinct is to protect her, even if she doesn't really need that protection anymore."
        
            "What do you mean by \"sooo\"?":
                "..."
                "I stare blankly at her."
                pf "\"Sooo\" what?"
                show nikki mis at cc
                "She rolls her eyes, but her voice is still sickly sweet."
                voice "audio/voice/E1/D2/S1/Nikki/23.ogg"
                sf "Don't you notice anything {i}different{/i} about me today?"
                pf "Hmm…"
                "Did she get a haircut? {w}No. Dyed her hair? {w}No. New style? {w}Uh, maybe. Not sure. Should I go with that?"
                show nikki dis at cc
                "{i}tap, tap, tap.{/i}"
                "Nikki taps her foot, her smile faltering."
                "I need to say something soon."
                pf "I like what you did with your hair?"
                show storm:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/24.ogg"
                sf "No."
                "Shoot, okay. {w}What about her eyes? Coloured contacts? {w}Nope, still amber. Um…"
                
                #SFX Lightbulb
                play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
                
                pf "Ah…!"
                pf "It's your ridiculous clothes!"
                show nikki sur b1 at cc with dissolve
                "Nikki's eyes widen. She kind of looks like she got the wind knocked out of her."
                pf "I'm right, aren't I?"
                show nikki wor at cc
                show panic:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/25.ogg"
                sf "Ridiculous?! Oh my god, do I look just awful?"
                pf "Um, no, of course not. I mean, it's a weird choice, but if you're going for the \"naughty schoolgirl\" look then you've got it down."
                show nikki ann at cc
                show vein:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/26.ogg"
                sf "A weird choice? This is my uniform, you jerk! I didn't \"choose\" to wear this!"
                "Oh, that explains a lot. Uniforms. Like what I'm wearing now, except not at all. Suddenly, my uniform doesn't seem too bad."
                pf "Haha, did I say \"ridiculous\"? I meant \"great\". You look good!"
                show nikki dis at cc
                voice "audio/voice/E1/D2/S1/Nikki/27.ogg"
                sf "Ugh, forget it. Finish your cold toast. We're going to be late."
        
            "My little sister can't be this cute!":
                ##SFX: Poke Noise
                play sound "audio/sfx/Human/Poke Noise.ogg"
                show nikki win b1 at cc with dissolve
                "Too adorable! I pinch her cheek, ignoring her protests as she squirms."
                show crying:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/28.ogg"
                sf "Eeeeeep! S-Stop it!"
                pf "KYAAAAA~! Kawaii desu!"
                show nikki ann b1 at cc
                "Nikki puts on a sour expression as she wrenches free from my grasp. She gingerly pokes her cheek, as if to reassure herself it's still there."
                "I grin at her and pat her head."
                pf "D'awww, don't be mad."
                show nikki neu b1 at cc
                show tsuBlush:
                    xoffset 720
                    yoffset 160
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E1/D2/S1/Nikki/29.ogg"
                sf "Hmph!"
                "Despite her grumpy facade, I can see traces of a smile forming."
    
    elif (E1D2S1_almostup == 1):
        "Nikki frowns when I finally make it into the kitchen. I don't know what {i}she's{/i} so annoyed about. I'm the one who could have used at least another hour of sleep."
        show nikki ann at cc with dissolve
        voice "audio/voice/E1/D2/S1/Nikki/30.ogg"
        sf "Finally! I thought you'd fallen back asleep."
        "I grunt in response and sit at the table, yawning widely."
        #stomach growl
        play sound "audio/sfx/Human/Stomach Grumble.ogg"
        "Before me is a plate of eggs and toast, and my stomach growls at the promise of food. {w}I dig in with gusto, but grimace at the first bite."
        pf "This is cold."
        show nikki dis at cc
        voice "audio/voice/E1/D2/S1/Nikki/31.ogg"
        sf "That's what happens when you lounge around in bed all morning. Now eat faster. We're going to be late."
        "Geez, someone's crabby in the morning."
    
    stop music fadeout 3
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 2
    "We finish our meal in silence, with Nikki occasionally shooting hurried glances my way. {w}I wolf down my food and gather my stuff, then meet Nikki by the door."
    show nikki thi at cc with dissolve
    voice "audio/voice/E1/D2/S1/Nikki/32.ogg"
    sf "How are you going to get to the academy?"
    pf "My motorcycle, obviously."
    show nikki ske at cc
    show question:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D2/S1/Nikki/33.ogg"
    sf "Oh, you don't need a permit then? I remember you were worrying about that."
    "Permit? {w}I completely forgot! {w}I'll need a parking permit for my bike, but they should have visitor parking which I can use… If I can find a spot."
    "So, what should I do? {w}Should I take the motorcycle anyway and hope for the best, or should I take the bus today and take my bike once I've gotten my permit?" 
    
    menu:
        "Take the bus":
            $ E1D2S1_firstdaybus = 1
            pf "You're right, I'll take the bus today. I need to sort out my parking situation before taking my bike."
            show nikki neu at cc
            "Nikki nods in affirmation."
            voice "audio/voice/E1/D2/S1/Nikki/34.ogg"
            sf "Which bus will you be taking?"
            pf "The line that heads to the south side of the city."
            show nikki sad at cc
            "She pouts."
            voice "audio/voice/E1/D2/S1/Nikki/35.ogg"
            sf "Aww, I'm taking the one going west..."
            pf "That's not at the same intersection, is it?"
            show nikki thi at cc
            voice "audio/voice/E1/D2/S1/Nikki/36.ogg"
            sf "No, I don't think so."
            pf "Oh… Well, at least it'll help you get familiar with the city."
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/37.ogg"
            sf "Yeah, you're right."
            pf "I'll see you later then?"
            show nikki smi at cc
            voice "audio/voice/E1/D2/S1/Nikki/38.ogg"
            sf "Have a good time at school, 'kay?"
            "She beams at me."

            stop music fadeout 3
            scene black with fade
            jump E1D2S2
    
        "Take the motorcycle":
            $ E1D2S1_firstdaybike = 1
            "Eh. I'm sure it'll be fine if I take my bike. {w}There must be at least {i}some{/i} form of parking that doesn't require a permit."
            pf "Yeah… I'll take my bike."
            show nikki mis at cc
            voice "audio/voice/E1/D2/S1/Nikki/39.ogg"
            sf "Oh, right. Of course. I forgot how much you cried when it was taken for shipping."
            pf "Very funny… Now I might not offer you a ride."
            show nikki neu at cc
            voice "audio/voice/E1/D2/S1/Nikki/40.ogg"
            sf "Even if you did, I'd still have to pass. I need to figure out how to navigate around Isokaze sometime, right?"
            pf "Really? Being seen on a bike like mine would automatically make you the most popular girl in school. You sure you want to pass up such a great opportunity?"
            show nikki mis at cc
            voice "audio/voice/E1/D2/S1/Nikki/41.ogg"
            sf "Please, have you met me? With my winsome smile and ample charm, I won't need your bike to be popular."
            pf "Whatever you say."
            show nikki smi at cc
            "Nikki heads towards the bus stop and waves goodbye."
            voice "audio/voice/E1/D2/S1/Nikki/42.ogg"
            sf "Good luck on your first day!"
            pf "You too!"
    
    stop music fadeout 3
    scene black with fade
    jump E1D2S3

