#
label E3MAS2:
    $ mayOut = renpy.random.choice(['sFashion'])
    $ meiHairB = "default"
    $ meiOut = "sCasual"
    $ meiHairF = "default"
    
    #Afternoon
    play sound [ "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg", "audio/sfx/Technology/Phone Vibration Once.ogg" ]
    play sound2 "audio/sfx/Technology/Phone Alarm.ogg"
    "I receive an incoming call from Mayu."
    stop sound
    stop sound2
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(.5)
    pf "Hey, Mayu."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-21.ogg"
    ma "Hi! Um, I hope you don't think this is weird, but would you want to go to the comic book store with me?"
    pf "Oh, is there one on campus?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-22.ogg"
    ma "N-No, it's in town. My next class was canceled so I'm done for the day. Do you have class?"
    pf "No, I'm done too." 
    "She seems relieved."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-23.ogg"
    ma "Great! I pre-ordered the new series of {i}Boundless Stratus{/i} and it's ready for pick-up. I don't like going alone because the guys there are... umm…"
    pf "Ummm...?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-24.ogg"
    ma "A bit overbearing. They're always trying to chat and they keep asking me to play games and stuff... but it feels weird... Shou's not into comics and he also thinks I'm overreacting."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-25.ogg"
    ma "I would just feel more comfortable having you there with me…"
    pf "Sure, I'll go with you. How were you planning to get there?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-26.ogg"
    ma "Um, by bus…"
    pf "I can drive us."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-27.ogg"
    ma "Are you sure? I don't want to be any trouble."
    pf "It's no trouble. How about I meet you at your dorm and we can go together?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-28.ogg"
    ma "Okay, see you soon."
    
    stop ambient fadeout 3
    scene black with fade
    "We hang up and I head to her dorm. After I pick her up, I drive us to the comic book store in town."
    
    "When we arrive, Mayu hesitates before she hops off my bike."
    pf "You okay?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-29.ogg"
    ma "Yeah…"
    "She takes a deep breath then gives me a nod. I follow her into the store."
    play ambient "audio/ambience/Mall.ogg" fadein 3
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    scene bg mall main day with fade
    "As soon as we walk in my mouth falls agape in wonder. Every staff member in the store is beyond attractive. Is that a prerequisite to working here?"
    "As I continue to look around, the patrons are all on the same level as the staff. The women have beautiful smiles and shapely curves which turn into legs that go on for days. They smile at me as we walk past."
    "The men are all tall with broad shoulders, and I can see the faint outlines of muscles underneath their shirts."
    
    if MCStory == 1:
        "I train pretty hard myself so I don't feel so out of place among the patrons here."
    
    else:
        "I am not in bad shape, but I still feel a little out of place. I wish I'd spent some more time on my training."
    
    "What is this place?!"
    show mayu neu at l2 with dissolve
    "Mayu doesn't even pause and heads straight to the counter. When we walk past, the staff members greet us, but Mayu keeps her head down and refuses to make eye contact."
    show receptionist extra at r2 with dissolve:
        xzoom -1
    "As we approach the counter, an equally attractive and friendly man greets us."
    voice "audio/voice/E3/Free/MA/S2/hotm1/1.ogg"
    hotm1 "Good to see you again, Mayu! Is there anything I can help you with?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-30.ogg"
    ma "Hi, I got an email saying my pre-order for {i}Boundless Stratus{/i} has arrived."
    voice "audio/voice/E3/Free/MA/S2/hotm1/2.ogg"
    hotm1 "Hmm, I didn't think we had any copies yet, but I'll double check the back stockroom for you."
    voice "audio/voice/E3/Free/MA/S2/hotm1/3.ogg"
    hotm1 "In the meantime, you and your friend should have a look around."
    hide receptionist
    hide mayu
    with dissolve
    
    show mayu smi at cc
    with dissolve
    "After flashing us a handsome smile, he heads into the backroom."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-31.ogg"
    ma "Do you want to take a look at their manga?"
    pf "Yeah, sounds good."
    
    "Mayu leads me through the section and I browse the titles."
    
    if E2KIS3_Completed == 1:
        "Hey, they even have copies of {i}Ninja Ranger{/i}! I wonder if Kaori's ever read the mangas or just watched the anime."
    
    pf "Are you a big manga fan?"
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-32.ogg"
    ma "I read some."
    "A title catches my eye and I enthusiastically grab the book off the shelf."
    pf "Oh hey, I remember this! Did you ever read this one?"
    show mayu neu
    "I hold the book out to Mayu while she examines the cover. She furrows her brows and slowly shakes her head."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-33.ogg"
    ma "No…"
    pf "Really? It was super popular when we were in middle school, at least it was in the States."
    show mayu cur
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-34.ogg"
    ma "What's it about?"
    show mayu neu
    pf "The main character and his family had to return home to take care of his sick grandfather, who passes on a protective charm for the main character. At his first day in his new high school, he gets into a fight and accidentally activates the charm, which turns out to be a cat-spirit-demon-girl."
    show mayu ske
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-35.ogg"
    ma "Umm…"
    pf "Once activated, the cat-girl swears to protect the main character and disguises herself as another student at his school. This causes all sorts of hilarious scenarios between her and the other girls in his class."
    show mayu thi
    ### VOICE - line read "That… That sounds… uh, that doesn't sound very familiar." but voice gave difference
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-36.ogg"
    ma "That... doesn't sound very familiar..."
    "I shrug."
    pf "It's really silly, but it was fun at the time."
    show mayu neu
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-37.ogg"
    ma "Which character was your favourite?"
    
    menu:
        "The shy girl." if MCStory != 3:
            jump E3MAS2_ShyGirl
            
        "{color=#00ff00}{b}The shy girl.{/b}{/color}" if MCStory == 3:
            label E3MAS2_ShyGirl:
                pf "I always liked the quiet girl. She's really nice and understanding and she's so cute when she gets embarrassed."
                show mayu smi b2
                "Mayu grins and her cheeks turn pink."
                voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-38.ogg"
                ma "I think I would like her too."
                show mayu smi b1
    
        "The fiery girl.":
            pf "I like the girl who is very outspoken and knows what she wants. Seeing her flustered is even more satisfying when you get past her hard shell."
            show mayu ner
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-39.ogg"
            ma "Sounds a little scary…"
    
        "The nice girl.":
            pf "I like the girl who is always nice and polite. She's always trying to help because she's very caring."
            show mayu smi
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-40.ogg"
            ma "You're right, she does sound nice."
    
        "The flirty girl.":
            pf "I like the girl who isn\'t afraid to flaunt what she\'s got. She\'s a tease and likes to stir up trouble. She always keeps the main character on his toes!"
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-41.ogg"
            ma "Hm... "
    
    pf "Anyway, I can't believe they still have it!"
    "I put the book back on the shelf."
    show mayu smi
    pf "What else do you read besides \"Boundless Stratus\"?"
    show mayu hap
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-42.ogg"
    ma "Oh! I like \"Evangelium\" and \"Gumdan\" too."
    pf "I'm beginning to see a trend here…"
    show mayu cur
    "She blinks."
    show question:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-43.ogg"
    ma "What do you mean?"
    pf "Well, all of the mangas you mentioned have giant robot battles."
    show mayu cur b1
    "Mayu's cheeks tinge pink."
    show mayu thi b1
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-44.ogg"
    ma "I mean, I do come from a long line of pilots. It's only natural that I gravitate towards those type of manga too."
    pf "You haven't read {i}any{/i} other types?"
    show mayu ner b1
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-45.ogg"
    ma "N-No… Father wasn't very fond of mangas to begin with. The only reason he let me read the ones I did was because they were sort of relevant to my studies."
    "Her voice lowers to a mumble."
    show drop:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-46.ogg"
    ma "{size=16}And because he didn't know about most of them.{/size}"
    "She stares at the ground and shuffles her feet when she catches my grin. Who knew Mayu had a rebellious side!"
    pf "Let's find a manga that you'd like. That's {i}not{/i} GEAR related."
    show mayu neu b1
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-47.ogg"
    ma "O-Okay…"
    "As we both peruse the shelves, one of the gorgeous men nearby politely greets us."
    $ persistent.gpix[41][0] = 1
    show cg mayu shopping 1 with dissolve:
        xzoom 0.5
        yzoom 0.5
    voice "audio/voice/E3/Free/MA/S2/hotm2/1.ogg"
    hotm2 "Excuse me, I couldn't help but overhear you're looking for a new manga. My sister just finished this one and she loved it."
    "He hands Mayu a book with a girl and a flute."
    voice "audio/voice/E3/Free/MA/S2/hotm2/2.ogg"
    hotm2 "Maybe you'd like it."
    "Mayu shifts from one foot to the other."
    pf "Thanks man, that's really nice of you."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-48.ogg"
    ma "Ah! Um, t-thanks…"
    voice "audio/voice/E3/Free/MA/S2/hotm2/3.ogg"
    hotm2 "No problem!"
    "Another man interjects."
    voice "audio/voice/E3/Free/MA/S2/hotm3/1.ogg"
    hotm3 "I highly recommend that one too. Although, there are some parts later on that... that deal with some \"heavy\" subjects."
    voice "audio/voice/E3/Free/MA/S2/hotm2/4.ogg"
    hotm2 "That's true."
    voice "audio/voice/E3/Free/MA/S2/hotm3/2.ogg"
    hotm3 "If you want something more lighthearted, you might want to check out that author's second title."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-49.ogg"
    ma "O-Oh...um…"
    "A third man joins in the conversation."
    voice "audio/voice/E3/Free/MA/S2/hotm4/1.ogg"
    hotm4 "Oh! I've read that one! You're talking about the boy and alien pet, right?"
    voice "audio/voice/E3/Free/MA/S2/hotm3/3.ogg"
    hotm3 "Yeah, that's the one."
    voice "audio/voice/E3/Free/MA/S2/hotm4/2.ogg"
    hotm4 "That one is really funny! The two of them get into all sorts of shenanigans."
    voice "audio/voice/E3/Free/MA/S2/hotm2/5.ogg"
    hotm2 "Huh, I'll have to check that out too."
    "Mayu stares helplessly at the crowd surrounding her as they continue to chat. I gently pull her aside and point to the book still clutched tightly in her hand."
    hide cg mayu shopping 1
    show mayu wor b1 at cc
    with dissolve
    pf "So, what do you think?"
    show mayu neu
    "She takes a deep breath to relax, then scans the synopsis."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-50.ogg"
    ma "It's about a girl who lands her dream role as the solo flutist in a symphony, but when her mother gets sick she has to decide between her family and her passion."
    show mayu cur
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-51.ogg"
    ma "Actually, I think this would be very interesting."
    "I grin."
    show mayu smi
    pf "Mission accomplished."
    "The man who originally suggested the title notices Mayu's interest in the book."
    voice "audio/voice/E3/Free/MA/S2/hotm2/6.ogg"
    hotm2 "I hope you enjoy it."
    show mayu sur
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-52.ogg"
    ma "T-Thanks!"
    show mayu neu
    "We part from the group, who are still deep in discussion. {w}Mayu breathes a sigh of relief."
    show mayu smi
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-53.ogg"
    ma "I'm glad you came with me."
    pf "Hm?"
    show mayu ner
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-54.ogg"
    ma "Didn't you see what happened back there? That happens all the time!"
    "That's what Mayu meant by \"overbearing\"? They seemed like really cool guys to me."
    pf "At least you got a new book out of it."
    show mayu smi
    "She smiles at the title in her hands."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-55.ogg"
    ma "True…"
    "After selecting a couple of titles for myself, I glance at Mayu."
    pf "Let's go check on your pre-order."
    "She nods happily."
    hide mayu with dissolve
    
    show mayu smi at l2
    show receptionist extra at r2
    with dissolve
    "We head to the counter where the clerk is waiting for us."
    voice "audio/voice/E3/Free/MA/S2/hotm1/4.ogg"
    hotm1 "Here is your pre-order."
    show mayu hap
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-56.ogg"
    ma "Thanks!"
    "I place the books I picked up on the counter and hand over my card."
    pf "I'd like to check these out, please."
    show mayu cur
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-57.ogg"
    ma "Oh yeah…"
    "I think she'd forgotten about the manga in her hand. {w}She puts it on the counter."
    $ E3MAS2_Paid = 0
    
    menu:
        "Offer to pay for her.":
            $ E3MAS2_Paid = 1
            pf "Include that one in my purchases too."
            show mayu sur
            "She blinks at me in surprise."
            show panic:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-58.ogg"
            ma "You don't have to do that!"
            pf "I know, I want to."
            show mayu sur b2
            "I smile at her and she blushes."
            show mayu wor b2
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-59.ogg"
            ma "But you've already done enough just by agreeing to come here with me."
            pf "That's not much. Any good friend would do that."
            show mayu ner b2
            "She's still hesitant."
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-60.ogg"
            ma "I-I appreciate it, but--"
            voice "audio/voice/E3/Free/MA/S2/hotm1/5.ogg"
            hotm1 "Here you go, sir."
            "The cashier returns my card and hands me a receipt and a bag with all of my books, including Mayu's."
            show mayu sur b2
            pf "Wha…?"
            show dots:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            "Mayu's eyes are wide as she stares at the bag."
            "The cashier winks at me."
            show mayu cur b2
            voice "audio/voice/E3/Free/MA/S2/hotm1/6.ogg"
            hotm1 "Have a nice day."
            pf "Thanks."
            hide receptionist extra with dissolve
            "I grin at Mayu."
            pf "Consider this an early birthday present."
            show mayu smi b2
            "Mayu blushes deeply."
            show regBlush:
                xoffset 365
                yoffset 135
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-61.ogg"
            ma "Thanks…"

        "Let her pay for her own book.":
            hide mayu
            hide receptionist
            with dissolve
            "I pay for my purchases and Mayu pays for her manga."
    
    "As we head towards the door, Mayu bumps into someone."
    show mayu wor at l2 with dissolve
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-62.ogg"
    ma "I'm sorry!"
    show mayu sur
    "She looks up in surprise."
    show mei neu at r2 with dissolve:
        xzoom -1
    ### VOICE - line is misread
    #voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-63.ogg"
    voice "audio/voice/MISSING/BATCH8/Missing Mayu-01.ogg"
    ma "Mei?"
    show mei hap
    voice "audio/voice/E3/Free/MA/S2/mei/MeiEp3_Line_69.ogg"
    ms "Hi guys!"
    show mayu cur
    pf "I didn't know you liked to read manga."
    show mei smi
    voice "audio/voice/E3/Free/MA/S2/mei/MeiEp3_Line_70.ogg"
    ms "Oh yeah! It's a secret pleasure of mine."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-64.ogg"
    ma "Really?"
    show mei mis
    "Mei grins appreciatively as one of the men walks past. So that's what she means by \"secret pleasure\". {w}At least I'm not the only one who sees this!"
    show heart:
        xoffset 1040
        yoffset 100
        xzoom .75
        yzoom .75
    ### VOICE - line missing?
    #ms "The view here is amazing."
    show mayu ske
    "Mayu furrows her brow."
    show question:
        xoffset 365
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-65.ogg"
    ma "View? It's inside a mall plaza..."
    show drop:
        xoffset 1040
        yoffset 100
        xzoom .75
        yzoom .75
    show mei ske
    "Mei raises an eyebrow. I understand her look all too well. How is Mayu not seeing this?"
    show mei hap with dissolve
    voice "audio/voice/E3/Free/MA/S2/mei/MeiEp3_Line_71.ogg"
    ms "Anyway, I've got some... \"things\" to check out so I'll see you later."
    hide mei with dissolve
    "She heads deeper into the shop while Mayu and I walk outside."
    show mayu smi
    pf "Ready to head back?"
    
    scene black with fade
    stop ambient fadeout 3
    "She nods. {w}We hop on my bike and I drive us back to campus."
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    show mayu smi at cc with dissolve
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-66.ogg"
    ma "Thanks for taking me to the comic book store."
    pf "Thanks for introducing it to me. Now I know where to go to catch up on my series."
    show mayu hap
    "She smiles."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-67.ogg"
    ma "I'm really happy you like to read manga too. Shou doesn't really care for it."
    pf "You think he'd like it more since there are pictures..."
    show mayu mis
    "Mayu giggles."
    show note:
        xoffset 720
        yoffset 135
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-68.ogg"
    ma "Be nice."
    show mayu smi
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-69.ogg"
    ma "Anyway, Father will be here soon and I still need to clean."
    pf "By \"clean\" do you mean \"hide your new books\"?"
    show mayu ner b1
    "She blushes."
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-70.ogg"
    ma "It would be best if he didn't know."
    show mayu smi b1
    voice "audio/voice/E3/Free/MA/S2/mayu/Mayu Arc-71.ogg"
    ma "Anyway, I'll see you later."
    hide mayu with dissolve
    "I wave goodbye and watch her disappear into her dorm."
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 3
    $ meiOut = "sUniform"
    
    $ E3MAS2_Completed = 1
    #end

