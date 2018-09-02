#
label E4D1S4:
    
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    ### SFX - bike being parked / turned off?
    $renpy.pause(0.5)
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    
    "My stomach growls loudly as I park my bike in the garage. Nikki, please be home for once!"
    "I wonder what we're going to have to for dinner…"
    scene bg homekaito main night with fade
    "As I enter the kitchen, I see a dainty strawberry cake sitting on the kitchen table."
    "...Cake for dinner?"
    "I peer closely at the layered cake and use my finger to taste the whipped cream. It melts on my tongue in a cloud of sweetness. {w}Fresh whipped cream!"
    "That's the only kind of whipped cream I'll eat. Mom spoiled us. She never bought whipped cream because she'd always make it herself."
    "Wait a minute--"
    "{b}Mom's birthday!{/b}"
    pf "Nikki?"
    "Did Nikki bake this cake for Mom's birthday? I search the house but see no sign of her. There's no text from her on my phone either. Clearly she came home after school…which means there's only one place she can be."
    scene black with fade
    "I grab my keys and hop back on my bike to find Nikki."
    stop ambient fadeout 10
    "We lived next to a park back home and Nikki would often escape to there when she was upset. {w}Just as I expected, I find Nikki swinging forlornly in the park."
    play music "audio/music/Kaori Itami (GAME VERSION).ogg" fadein 6
    $ persistent.gpix[20][0] = 1
    show cg nikki park 1 with Dissolve(2.5):
        xzoom 0.5
        yzoom 0.5
    "Her head is bent as she gazes down at something in her hands."
    "I take a seat beside her. She glances at me but doesn't speak. Instead she cups the open locket in her hands, the one that usually hangs around her neck. Inside is a picture of Mom and Dad."
    #scene bg isokaze park night with fade
    #show nikki sad at cc with dissolve
    pf "You okay?"
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_101.ogg"
    sf "I don't know."
    pf "Mom would have loved the cake you made her."
    "Nikki snaps the locket shut and holds it to her chest."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_102.ogg"
    sf "I had to do something, you know? Today is Mom's birthday and I couldn't not celebrate it."
    pf "I know."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_103.ogg"
    sf "So I thought I'd make her a cake, like we used to do… but then…"
    # dots
    "Her voice trembles and she takes a minute to compose herself."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_104.ogg"
    sf "But then that cake… it was like it was taunting me. A reminder that Mom will never get a chance to eat it."
    #show nikki win
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_105.ogg"
    sf "It's not fair!"
    scene black with fade
    scene bg isokaze park night with fade
    $renpy.pause(.75)
    show nikki win at cc with dissolve
    $renpy.pause(.75)
    "Nikki's knuckles turn white as she clutches at the locket. Her hands begins to shake."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_106.ogg"
    sf "I barely got any time with her before she was taken away and I just want her back!"
    pf "Nikki…"
    show nikki sad with dissolve
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_107.ogg"
    sf "I know I'm being crazy, but… I just keep thinking it's my fault…"
    "Tears trickle down her cheeks and leave wet stains on her shirt. Instinctively, I pull her in for a hug and she leans against me."
    pf "This wasn't your fault, Nikki."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_108.ogg"
    sf "It is."
    pf "You had no control over this."
    # dots
    "She pulls away and falls silent. When she finally speaks her voice is thick."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_109.ogg"
    sf "I missed the bus that day."
    pf "What?"
    show nikki wor
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_110.ogg"
    sf "The reason they left the cafe is because I missed the bus and needed a ride home."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_111.ogg"
    sf "I keep thinking… what if I had just gotten on that bus as soon as class ended? I wasn't even doing anything important! I was just hanging out and lost track of time--"
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_112.ogg"
    sf "I remember being so annoyed when they didn't show up. I was so angry I had to walk home and all I could think about  was how much..."
    show nikki sad
    "Her voice falters."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_112_01.ogg"
    sf "How much I hated them."
    
    ### NOTE - verify variable usage and implementation in Variable.rpy and during the scene
    #if E3_5S?_TellNikki == 1:
        #"A twinge of guilt stabs at my heart. I had no idea Nikki was harbouring such deep guilt. A part of me wonders if telling her the accident might not have been an accident would help her. {w}Regardless, now wouldn't be the time to do that."
    
    #else:
        #"I had no idea Nikki was harbouring such deep guilt. It's definitely a good thing we didn't tell her what we found out about about Mom and Dad's accident. She's already dealing with a lot of feelings as it is."
    
    pf "You didn't mean that. You were angry."
    show nikki win
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_113.ogg"
    sf "What kind of daughter thinks like that? When I remember I feel so disgusted with myself!"
    pf "Be that as it may, what happened wasn't your fault, Nikki. You didn't tell that driver to hit them. You can't keep blaming yourself."
    show nikki sad
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_114.ogg"
    sf "Then why do I feel like I'm being punished?"
    pf "Because this sucks. Because it's so easy to think about all the years that have been stolen from you and to lament that loss."
    pf "But you can't keep thinking like that."
    
    menu:
        "Look on the positive side.":
            pf "Look at all the awesome stuff you're doing now. You have a lot of friends and your cooking club is a huge success. Mom and Dad could not be more proud of what you've accomplished."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_115.ogg"
            sf "But they aren't here to share in the success with me."
            pf "Maybe not physically, but they're still here. As long as we remember them, they'll always be here."
            show nikki neu
            "A ghost of a smile frames Nikki's lips."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_116.ogg"
            sf "You're so cheesy."
    
        "I didn't fair much better.":
            pf "I mean, I wasn't even home last year and I {i}forgot{/i} Mom's birthday. If I kept thinking about all the time I missed out on with them, I'd drive myself crazy too."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_117.ogg"
            sf "You were at college, though. It's not like you were avoiding them on purpose."
            pf "Exactly, but it still feels like I should have done more."
            show nikki neu
            "Nikki sighs, but a ghost of a smile graces her lips."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_118.ogg"
            sf "Why do you always make sense?"
    
        "Be happy for the time you did spend together.":
            pf "Focus on all the good times you had with them. The last thing Mom and Dad would want is for you to be sad because of them."
            pf "They want you to be happy."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_119.ogg"
            sf "I know… I just miss them so much."
            pf "I know, I miss them too."
            pf "But on the bright side, at least you've still got me!"
            show nikki ske
            "Nikki sighs."
            voice "audio/voice/E4/Nikki/Day 1/Nikki_04_120.ogg"
            sf "I thought you were trying to make me feel better, not worse."
            pf "Hey…"
            show nikki neu
            "She lets out a weak laugh."
            
    stop music fadeout 10
    "Her tears have stopped and some colour is returning to her face."
    play ambient "audio/ambience/Night Crickets.ogg" fadein 10
    pf "Remember Mom's cake from last year? It was completely inedible."
    #show nikki mis
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_121.ogg"
    sf "You mean the second cake--the one {i}you{/i} baked for Mom because you forgot her birthday?"
    pf "Oh yeah, whoops."
    show nikki smi
    "Nikki laughs."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_122.ogg"
    sf "Mom tried so hard to eat it but eventually she just gave up."
    pf "Not my finest moment, but at least it wasn't as bad as the one Dad baked the year before."
    #show nikki hap
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_123.ogg"
    sf "You mean when he almost burned our entire house down?"
    "Nikki laughs so hard she snorts, which only makes her laugh harder. Her laughter is infectious and I can't help but join in."
    pf "I think I got a lot more of Dad in me than you do."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_124.ogg"
    sf "Yeah, but it's not all bad. You got a lot of his good qualities too… like how you're always there for me when I need you."
    pf "It's a hard job but somebody has to do it."
    show nikki dis
    "Nikki bumps me playfully with her swing."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_125.ogg"
    sf "Rude!"
    pf "No, you know what's rude? Leaving a perfectly delicious cake untouched in the kitchen."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_126.ogg"
    sf "That's true. It was made for eating."
    pf "So let's go eat it."
    hide nikki with dissolve
    "Grinning from ear to ear, Nikki nods and stands up. Together, we head to my bike and I drive us back home."
    stop music fadeout 3
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    scene bg homekaito main night with fade
    show nikki cur at l2 with dissolve
    "As soon as I park, the two of us hop off my bike and eagerly rush into the kitchen, then freeze."
    play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
    show kaito neu at r2 with dissolve:
        xzoom -1
    "There is only 1/3 of the cake remaining, and a trail of crumbs starts from the kitchen table and ends at Uncle Kaito's face."
    show kaito cur
    "I can only stare in stunned silence at the scene."
    # shocked
    show nikki sur
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_127.ogg"
    sf "Uncle Kaito!"
    show kaito wor
    "He pauses, a fork full of moist yellow cake is halfway to his mouth."
    voice "audio/voice/E4/Nikki/Day 1/Nikki_04_128.ogg"
    show nikki ner
    sf "Did you eat all of the cake?!"
    # panic
    show kaito ner
    "Uncle Kaito looks from his fork to Nikki then back at the fork."
    voice "audio/voice/E4/Kaito/d01/Kaito_D1_01.ogg"
    hk "I want my lawyer."
    show nikki hap
    show kaito sad
    "Nikki and I burst out laughing as Uncle Kaito shoves the fork into his mouth. Nikki and I split the rest of the cake while Kaito looks on longingly."
    scene black with fade
    stop music fadeout 5
    "Nikki is all smiles for the rest of the night as Uncle Kaito asks us about our day. I tuck into bed early as I know I'll have a busy day of frolicking in the hot springs tomorrow."
    
    if valrelatonship == 1:
        "Soon I'm dreaming about Valerie steaming up the hot water..." 
    elif yuurelatonship == 1:
        "Soon I'm dreaming about Yuuna steaming up the hot water..."
    elif kaorelatonship == 1:
        "Soon I'm dreaming about Kaori steaming up the hot water..."
    elif mayrelatonship == 1:
        "Soon I'm dreaming about Mayu steaming up the hot water..."
    else: # Alone or Shou
        "Soon I'm dreaming about hot water and hot girls."
    
    jump E4D2S1
