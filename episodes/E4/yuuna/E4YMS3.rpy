#WEEKEND
label E4YMS3:

$ yuuHairF = "default"
$ yuuHairB = yuuHairF
$ yuuOut = "Camp Bag"

scene bg homekaito myroom day with fade
play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 10
"I wake up with a yawn and stretch. Then I get ready for the day and eat a hearty breakfast. {w}I hope Yuuna didn't forget our plans for the day! I'll give her a quick call to make sure she's ready for me to pick her up."
"The phone rings a couple of times before she answers."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/94.ogg"
ym "Hi, ready for our nature excursion?"
"I grin."
pf "And here I was worried you'd forgotten."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/95.ogg"
ym "No way! I meant it when I said I wanted to get away this weekend. I've even got my friend watching Mochi for the night."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/96.ogg"
ym "Studying for exams next week is really stressing me out. I think spending a day outside, enjoying the fresh air, seeing the wildlife is exactly what I need to rejuvenate the soul."
pf "Awesome, because I already got permission from Uncle Kaito to borrow his car."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/97.ogg"
ym "And I found a tent in our attic, so we have no excuse not to go."
pf "In that case, I'll come by and pick you up now?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/98.ogg"
ym "Okay, I'll be ready."
scene black with fade

"I've already prepared everything I want to bring, so once we hang up, I load it into the car. Then I drive to Yuuna's house."
"She's waiting for me with a rolled up tent in one hand and a large bag in the other."

scene bg isokaze neighborhood day with fade

show yuuna smi at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/99.ogg"
ym "I brought some water and food which should be easy to cook over a fire."
pf "Perfect, I brought some snacks too."

scene black with fade

"I help her load everything into the car and we get driving. Yuuna acts as my navigator and tells me where to go. There's an area between the mountain ranges and lake which is a popular camping and hiking destination. Although this island isn't that big, it's still a couple of hours drive before we arrive."


"There aren't very many people around, which is fortunate for us. We select a more secluded area to set up camp. I grab the tent out of the car."

scene bg vacation nature day with fade

if E4YMS2_Indoors == 0:
    "Although it's been a few years since I've gone camping, I still remember the basics of how to put up a tent. Yuuna's tent is actually a lot larger than the ones I've used and way more stable!"

else:
    "Yuuna's tent is a lot larger than I remember most tents to be and I struggle getting it open and upright. Is this the tent flap? Wait, no, that doesn't open…"
    show yuuna hap at cc with dissolve
    "Yuuna looks on with amusement and giggles."
    show yuuna mis
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/100.ogg"
    ym "Let me help you with that."
    "Yuuna grabs another end of the tent, and as we are able to stretch it open, it's easy to find which way is which."
    "Together, we put the tent up with no trouble."

pf "This is a nice tent!"
show yuuna smi at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/101.ogg"
ym "Thanks, my mom picked it out when I was in high school. She said Yuudai and I had outgrown our old tent."
"I glance at her in surprise when she mentions her brother's name, but Yuuna's face no longer holds a shadow of sadness. Instead, she looks on fondly."
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/102.ogg"
ym "Yuudai used to compete with Dad to see who could put up the tent the fastest. Usually Dad won."
pf "They always do."
show yuuna smi
"After getting the tent set up, we pull out the sleeping bags and blankets and set them up inside the tent."
pf "Should we unpack anything else or should we go do something?"
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/103.ogg"
ym "I vote we unpack later and do something first."
"I grin."
pf "Me too."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/104.ogg"
ym "I had a few ideas planned. The nice thing about this location is that we've got a lot of options available."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/105.ogg"
ym "I was thinking we could go hiking, go swimming, or go on a scavenger hunt."

menu:
    "Let's go hiking.":
        $ E4YMS3_hiking = 1
        pf "I've got my outdoor boots on and I'm ready to tackle the wilderness. Let's go for a hike."
        "Yuuna points to her boots."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/106.ogg"
        ym "We were thinking the same thing."
        pf "Nice!"
        "She grabs a couple of water bottles from her bag in the car and a few bags of trail mix. Then she puts them in a cute little doggy backpack."
        pf "Nice backpack."
        show yuuna cur b1
        "She blushes."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/107.ogg"
        ym "Oh! Um, I got this when I was little but it's still useful so…"
        pf "No, I actually mean it's cute."
        show yuuna smi
        "She smiles."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/108.ogg"
        ym "I think so too. Plus, it looks a little like Mochi."
        "After shouldering the pack, she points towards the trail."
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/109.ogg"
        ym "Come on, the trail starts here."
        show yuuna smi
        "She starts to lead me away from camp."
        jump E4MYS3_hikejump

    "I'm basically a fish in the water.":
        $ E4YMS3_swimming = 1
        pf "Is there anything better than swimming?"
        show yuuna mis
        "Yuuna grins."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/111.ogg"
        ym "I brought a sturdier swimsuit this time."
        pf "Good thinking."
        show yuuna smi
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/112.ogg"
        ym "Do you need to change?"
        pf "Um, yeah, I have my trunks in the car."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/113.ogg"
        ym "Okay, you can take the tent."
        pf "What about you?"
        hide yuuna with dissolve
        "She smirks playfully, then pulls off her shirt--"
        pf "Whoa! I like where this is going!"
        
        $ yuuOut = "sSwimsuit"
        
        show yuuna smi b2 at cc with dissolve
        "--and reveals the exact same swimsuit she wore to the beach."
        show yuuna mis b2
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/114.ogg"
        ym "I came prepared."
        pf "I thought you said you chose a different suit."
        show yuuna cur b2
        "She blinks."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/115.ogg"
        ym "I did!"
        pf "Uh…"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/116.ogg"
        ym "These straps are a little bit thicker than the other. See?"
        pf "Sure…"
        "They look exactly the same to me. {w}Women…"
        "I grab my suit from the car and get changed in the tent."
        "Yuuna leads me towards the lake."
        show yuuna hap b2
        #voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/117.ogg"
        voice "audio/voice/MISSING/BATCH6/Redo 1.ogg"
        ym "Come on!"
        jump E4MYS3_swimjump

    "Scavenging is in my nature.":
        $ E4YMS3_scavenge = 1
        pf "A scavenger hunt sounds cool, but how would that work?"
        show yuuna hap
        
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/118.ogg"
        ym "I found a list online! It's kind of interactive so once we find the item, we have to take a picture and upload it before it'll move onto the next item."
        show yuuna smi
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/119.ogg"
        ym "What do you think?"
        pf "Sounds fun! My only regret is that I didn't bring my explorer hat."
        "Yuuna grins, then rummages in one of her bags and pulls out… {w}a hat! She puts it on her head."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/120.ogg"
        ym "Luckily, I did."
        pf "Whoa, you came prepared."

        menu:
            "Steal her hat!":
                "When Yuuna isn't paying attention, I swipe the hat off her head and put it on myself. It fits really snugly."
                show yuuna sur
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/121.ogg"
                ym "Hey!"
                pf "My hat now!"
                show yuuna smi
                "Yuuna looks at me then giggles."
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/122.ogg"
                ym "Looks a little small."
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/123.ogg"
                ym "Are you sure you wouldn't rather have…"
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/124.ogg"
                ym "This one?"
                "She pulls out a larger but otherwise identical hat from behind her back and offers it to me."
                pf "Wow, you really did prepare for anything!"
                "Yuuna laughs as we swap hats."

            "Guess I'm hatless...":
                "Yuuna hides a laugh at my pout."
                show yuuna hap
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/125.ogg"
                ym "Aw, don't look so sad."
                show yuuna smi
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/126.ogg"
                ym "Maybe this will cheer you up."
                "She pulls out a larger but otherwise identical hat from behind her back and offers it to me."
                pf "No way!"
                "I accept the hat and prop it on my head with a wide grin."
                pf "How do I look?"
                show yuuna mis
                voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/127.ogg"
                ym "Like you're ready to get to business."

                "She opens up her phone and looks for the first object."
                
        jump E4MYS3_scavjump

label E4MYS3_hikejump:
$ E4YMS3_hiking = 1
hide yuuna with dissolve
"At first, the trail leading up the mountain is easy, but soon it starts to get rockier and we have to be careful about where we step."
if MCStory == 1:
    "Although my breaths come out in short pants, my footing is solid and I navigate the trail without difficulty."
    "Yuuna and I continue to keep pace with each other. She's so naturally graceful and maneuvers around the rocks with ease."
    show yuuna smi at cc with dissolve
    
else:
    "My footing is unsteady and I lag slightly behind Yuuna as I watch very closely where I step."
    show yuuna cur at cc with dissolve
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/128.ogg"
    ym "You okay?"
    pf "Yeah, I'm fine."
    "She smiles, but slows her pace to match mine anyway."

"As we continue to climb, I enjoy the peacefulness of our surroundings. The trees shield us from the hot rays of the sun, and the only sounds are the scurrying of animals and our breathing."
"I barely register the squirrels jumping to and from the trees, but a weird animal that looks kind of like a dog and a raccoon darts behind a tree off the path."
pf "Hey! Did you see that?"
show yuuna cur
"Yuuna stops."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/129.ogg"
ym "Hm?"
pf "That… raccoon dog?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/130.ogg"
ym "What?"
pf "Let's go chase it!"
"I start to drift off the trail when Yuuna stops me."
show yuuna sur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/131.ogg"
ym "Hey, wait! That's not a good idea. We could get really lost."

menu:
    "The raccoon dog is more important!":
        pf "We have to go after it!"
        hide yuuna with dissolve
        "Before Yuuna can protest, I slip off the trail and go into the trees."
        "Yuuna stays rooted to the spot and doesn't come after me. Probably for the best."

    "Good point. You wait here.":
        pf "Ah, you're right. The last thing we want to do is get lost and die in the wilderness."
        show yuuna thi
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/132.ogg"
        ym "No, that wouldn't be good."
        pf "Okay, stay here, while I look!"
        show yuuna sur
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/133.ogg"
        ym "What?!"
        hide yuuna with dissolve
        "Before she can protest, I dart off into the trees."
        
"I spot the furry fellow gnawing on something and I approach it cautiously. A twig snaps beneath my feet, alerting the creature."
"It sits up and stares straight at me, then runs away. I immediately give chase!"
"We speed through the trees, my focus entirely on keeping the creature in my sight. Suddenly, I crash into someone!"
pf "Ow!"
show yuuna win at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/134.ogg"
ym "Hey!"
"I blink."
pf "Yuuna?"
"Scrambling to my feet, I help her back onto hers."
pf "What are you doing here?"
show yuuna wor
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/135.ogg"
ym "I've been waiting for you to come back. I was so scared you'd get lost!"
"Yuuna's eyes glitter and her voice wavers. I didn't realise I worried her so much! {w}I brush the stray leaves out of her hair, and gently caress her cheek."
pf "I'm sorry, I shouldn't have done that."
"I pull her close to me and she buries her face in my chest."
show yuuna smi b1 with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/136.ogg"
ym "I-It's okay… as long as you're safe."
"Slowly, we pull apart and I lean in to kiss her."
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/137.ogg"
ym "By the way, that animal you saw is a Tanuki."
pf "A Tanuki?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/138.ogg"
ym "They're all over Japan. I'm surprised you haven't seen one before now."
pf "Uhh, are those the spirit animals with the huuuuuuge balls--"
show yuuna win b2 with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/139.ogg"
ym "We should be heading back now!"
hide yuuna with dissolve
"Yuuna's cheek are bright red and she quickly heads back down the trail."
pf "Hey! Wait for me!"
"As Yuuna slows her pace, she looks back at me."
show yuuna smi at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/140.ogg"
ym "Do you want to just hang out at camp or do something else?"

menu:
    "Let's go on the scavenger hunt." if E4YMS3_scavenge == 0:
        pf "How does the scavenger hunt work?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/141.ogg"
        ym "I found a list earlier and put it on my phone. It's kind of a game, so when we find the item, we take a picture of it and then it'll tell us the next item."
        pf "That sounds fun!"
        "She grins, and pulls out her phone."
        jump E4MYS3_scavjump

    "Let's go swimming." if E4YMS3_swimming == 0:
        pf "Swimming sounds perfect right about now."
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/142.ogg"
        ym "Great! Since we're headed back to camp anyway, we can go get changed first."
        hide yuuna with dissolve
        "I nod, as Yuuna leads the way. Once we're done changing, I follow Yuuna again."
        jump E4MYS3_swimjump

    "Let's go back to camp.":
        pf "I'm pooped. Let's take a rest back at camp."
        show yuuna smi
        "She nods and we make our way back."
        hide yuuna with dissolve
        jump E4MYS3_campjump


label E4MYS3_swimjump:
$ E4YMS3_swimming = 1
hide yuuna with dissolve
"It takes a few minutes as Yuuna guides us."

$ yuuOut = "sSwimsuit"

scene bg isokaze park2 day with fade

"Finally, we come to the end of the path."
pf "Where's the lake?"
show yuuna smi b1 at cc with dissolve
"Yuuna points downwards. I stand beside her at the edge and glance down to see pristine waters."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/143.ogg"
ym "That's the fastest way to the lake, otherwise we'll have to take the long way to go down."
pf "Are you sure this is safe?"
show yuuna hap b1
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/144.ogg"
ym "Of course! There are no hidden rocks below if that's what you're worried about. We're not that far up either."
pf "Um…"
"Yuuna wears a sly grin."
show yuuna mis b1
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/145.ogg"
ym "If you're afraid, we can just walk down."

menu:
    "Cannonball!":
        "Afraid?! I live for the adrenaline!"
        show yuuna cur
        "Instead of responding, I step away from the ledge. Yuuna watches with a mixture of amusement and surprise as I take a running start and leap off the edge. I tuck my arms and legs into a ball as I slice through the air."
        "With barely enough time to suck in a deep breath, I crash into the water."
        "I pump my legs and break through the surface of the water to suck in more air. Squinting at the sun, I spot Yuuna peering down at me and flash her a thumbs up."
        pf "Come on in! The water's great!"
        hide yuuna with dissolve
        "She disappears, and for a minute I wonder if she's going to walk, when I see a flash of pink gracefully arcs off the edge into a beautiful swan dive. She barely makes a splash as she enters the water."
        show yuuna mis b1 at cc with dissolve
        "After a few seconds, she breaks the surface and grins at me."
        pf "I give that a 10/10."
        show yuuna sur b1
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/146.ogg"
        ym "Oh wow, a perfect score!"
        pf "For a perfect girl."
        show yuuna smi b2 with dissolve
        "I swim over and kiss her, my heart still pounding from the adrenaline."

    "Yuuna should go first.":
        pf "Me? Afraid? Please, but how do I know if it's really safe?"
        show yuuna smi
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/147.ogg"
        ym "I wouldn't suggest it if it weren't."
        pf "Alright, then ladies first."
        "Yuuna blinks, then grins."
        show yuuna mis
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/148.ogg"
        ym "As you wish!"
        hide yuuna with dissolve
        "She takes a few steps back, then after a running start, she gracefully arcs off the ledge into a beautiful swan dive. She barely makes a splash as she enters the water."
        "When she breaks the surface, she waves at me."
        show yuuna hap at cc with dissolve
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/149.ogg"
        ym "Your turn!"
        show yuuna smi
        "Well, she took my challenge, so there's no turning back now!"
        "After a running start, I jump off the ledge, then tuck my arms and legs into a ball as I crash into the water."
        show yuuna hap
        "Yuuna laughs as I resurface."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/150.ogg"
        ym "That was a huge splash!"
        pf "I know! Pretty good, right?"
        show yuuna mis
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/151.ogg"
        ym "I think I'll have to dock you a lot of points for your form. 5/10."
        pf "What!"
        pf "That was definitely a 10/10."
        show yuuna smi
        "I pout. Yuuna kisses me gently."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/152.ogg"
        ym "Alright, you win. It was a 10/10 splash."
        pf "Thank you."

    "Let's take the long way.":
        pf "Yeah, heights and I don't really get along…"
        show yuuna smi
        "Yuuna smiles gently."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/153.ogg"
        ym "Okay, we'll walk around."
        hide yuuna with dissolve
        "She leads me back down the path and it's another 10 minutes before we arrive at the bank of the lake."
        "Without hesitation, Yuuna wades into the water."
        show yuuna cur at cc with dissolve
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/154.ogg"
        ym "Ooh, the water's nice!"
        "She dives under, then resurfaces a few paces away."
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/155.ogg"
        ym "Come on!"
        "I gingerly dip a toe in. Huh, the water's pretty warm. Then I follow her lead and splash my way to her."

show yuuna smi
"We continue to laugh and splash in the water, when a colourful fish catches my eye."
pf "Hey! Did you see that?"
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/156.ogg"
ym "See what?"
pf "The rainbow fish!"
"Yuuna gives me a weird look."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/157.ogg"
ym "There's no such thing as a rainbow fish."
pf "I swear I just saw it…"
"We both squint at the water. I spot a lot of trout and other plain looking fish… when a glint of bright white and orange swims past."
pf "There!"
show yuuna sur
"Yuuna looks surprised."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/158.ogg"
ym "Hey! That's a carp! What's it doing here?"
pf "I don't know. Let's catch it!"
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/159.ogg"
ym "With what?"
"As the fish swims past again, I snatch at it with my bare hands but only grab a handful of water."
pf "Aw…"
show yuuna hap
"Yuuna laughs."
show yuuna mis
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/160.ogg"
ym "That's why fishing rods were invented."
pf "Bears can do it."
"The carp swims by again and I lunge for it, but again come back empty handed."
pf "Stop swimming, you sly fishy!"
"Suddenly, Yuuna darts forward."
show yuuna sur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/161.ogg"
ym "Oh! I touched it!"
pf "Really?"
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/162.ogg"
ym "Yeah!"
"She grins proudly and her eyes sparkle."
show yuuna mis
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/163.ogg"
ym "I'm going to catch that fish!"
"No matter how often we called and waited for the carp to return, it didn't appear again. I guess it learned its lesson and was staying far, far away from the grabby hands."
show yuuna smi
"Once our fingers and toes started to prune, we decided to get out of the water and dry off."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/164.ogg"
ym "Is there something else you want to do or do you want to head back to camp?"

menu:
    "Let's go hiking." if E4YMS3_hiking == 0:
        pf "Why don't we take that hike now?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/165.ogg"
        ym "Okay! I guess we have to go back to camp first anyway to change."
        pf "No worries."
        hide yuuna with dissolve
        $ yuuOut = "Camp Bag"
        scene black with fade
        "Yuuna nods, then leads the way back to camp. Once we're done changing, I follow Yuuna again."
        scene bg vacation nature day with fade
        jump E4MYS3_hikejump

    "Let's go on a scavenger hunt." if E4YMS3_scavenge == 0:
        pf "How does the scavenger hunt work?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/166.ogg"
        ym "I have a list on my phone! We take a picture of it and upload it, then the list will tell us what to take next."
        pf "That sounds fun!"
        show yuuna hap
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/167.ogg"
        ym "Okay, let's go get changed and then we can start."
        hide yuuna with dissolve
        $ yuuOut = "Camp Bag"
        scene black with fade
        "She leads the way back to camp. Once we're done changing, I follow Yuuna again."
        scene bg vacation nature day with fade
        jump E4MYS3_scavjump

    "Let's go back to camp.":
        pf "I'm pooped. Let's take a rest back at camp."
        show yuuna smi
        "Yuuna nods."
        hide yuuna with dissolve
        $ yuuOut = "Camp Bag"
        scene black with fade
        "We change back into our clothes."
        scene bg vacation nature day with fade
        jump E4MYS3_campjump

label E4MYS3_scavjump:
$ E4YMS3_scavenge = 1
hide yuuna with dissolve
"We double check the app."
show yuuna cur at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/168.ogg"
ym "Okay, so the first object we have to find is sunlight through the trees."
pf "That's oddly specific, but not hard."
"I point to any one of the myriad of trees surrounding us. Yuuna shrugs, and arbitrarily picks a tree to take a picture."
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/169.ogg"
ym "Done! The next thing we have to find is a fish."
pf "Also not hard."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/170.ogg"
ym "Come on, let's go to the lake."
"I follow Yuuna down to the lake and we snap a photo of the fish swimming beneath the clear waters."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/171.ogg"
ym "Next one is to find a lizard."
pf "Okay, that's a little harder… they like water, right? Good thing we're already by the lake."
"We scour the bank but are unsuccessful. Just as we're about to give up, Yuuna jumps excitedly."
show yuuna sur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/172.ogg"
ym "Oh! I found one! Look!"
show yuuna smi
"I rush over and spot a little brown gecko. It blended in so well with the ground, that I would have missed it if Yuuna hadn't said something."
pf "Nice! What's next?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/173.ogg"
ym "Find an intact spider web."
pf "That'll probably be easy to spot on the trees…"
"We continue to run down the list, enjoying the challenge. The further down the list we go, the harder the requests. The items range from really specific, such as an ant moving something, to really general, like a butterfly, to kind of weird, like a dead tree."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/174.ogg"
ym "Next we have to find a four leaf clover."
pf "Those don't exist."
show yuuna cur
"Yuuna blinks."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/175.ogg"
ym "Sure they do."
pf "No, clovers are three leaves."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/176.ogg"
ym "Yeah, the four leafed ones are really rare but they do exist."
pf "I've never seen one before."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/177.ogg"
ym "Well, now you will!"
"Still skeptical, we get to searching…"
"...and searching…"
pf "Are you sure about this? I can't find one anywhere."
"Yuuna frowns."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/178.ogg"
ym "They do exist! They're just super hard to find."
pf "Okay, well, can we skip this one and move onto the next? My neck is starting to cramp from staring at the ground for so long."
show yuuna dis
"Yuuna tries to skip but frowns."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/179.ogg"
ym "It won't let us skip without uploading a pic."

menu:
    "Upload a pic of something random.":
        pf "Does it matter what the pic is?"
        show yuuna cur
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/180.ogg"
        ym "Um, I think so?"
        pf "I mean, does this thing actually know if we've uploaded a picture of the requested item, or is it just triggered by a picture upload?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/181.ogg"
        ym "I'm not sure. This is the first time I've used it."
        pf "What if we just took a random pic and uploaded it?"
        show yuuna dis
        "She looks disappointed."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/182.ogg"
        ym "That defeats the purpose of the game though…"

    "Take a pic of a four leaf clover.":
        pf "Okay, we'll take a picture of a four leaf clover then."
        show yuuna cur
        "Yuuna blinks."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/183.ogg"
        ym "Did you find one?"
        pf "Nope."
        "I pluck a three leaf clover and another leaf from another clover, then hold them together to make a four leaf clover."
        pf "Ta-da! There's our four leaf clover."
        show yuuna dis
        "Yuuna looks uneasy."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/184.ogg"
        ym "That's definitely cheating."
        
    "Keep looking.":
        pf "Let's keep trying."
        show yuuna neu
        "Yuuna nods."
        "Our search continues!"
        "After some time, it looks like we won't be finding a four leaf clover anytime soon."

show yuuna thi 
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/185.ogg"
ym "Maybe we should take a break for now."
"Yuuna smiles, but I can tell she's disappointed. She probably wanted this game to go smoothly and my complaining certainly didn't help."
pf "Hey, I have one last thing for us to find."
show yuuna cur
"Yuuna glances up at me."
pf "One amazing girlfriend."
show yuuna smi b2 with dissolve
"She blushes as I pull her close and kiss her."
pf "Time to take a picture, right?"
show yuuna hap b2
"She nods, and takes out her camera so we can pose in a picture together."
show yuuna smi with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/186.ogg"
ym "Okay, now I'm really ready for a break though. Is there something else you want to do or should we just go back to camp?"

menu:
    "Let's go hiking." if E4YMS3_hiking == 0:
        pf "Why don't we take that hike now?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/187.ogg"
        ym "Okay!"
        hide yuuna with dissolve
        "Yuuna leads the way again."
        jump E4MYS3_hikejump

    "Let's go swimming." if E4YMS3_swimming == 0:
        pf "Swimming sounds perfect right about now."
        "She grins."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/188.ogg"
        ym "Okay, let's go get changed first."
        hide yuuna with dissolve
        "I nod, as Yuuna leads the way. Once we're done changing, I follow Yuuna again."
        jump E4MYS3_swimjump

    "Let's go back to camp.":
        pf "I'm pooped. Let's take a rest back at camp."
        show yuuna smi
        "She nods and we make our way back."
        hide yuuna with dissolve
        jump E4MYS3_campjump


label E4MYS3_campjump:
stop music fadeout 6
hide yuuna with dissolve
pf "Lead on!"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/189.ogg"
ym "Sounds good!"
scene black with fade
"Yuuna leads the way back to camp. The sun slowly dips in the sky. I glance again at Yuuna, and smile."
"The day just flies by when I'm with her!"

scene bg vacation camp dusk with fade
$ yuuOut = "Camp No Bag"
"Once we spot our tent, Yuuna turns to me."
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
show yuuna cur at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/190.ogg"
ym "What now?"
pf "Now it's time for the best part… the campfire!"
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/191.ogg"
ym "I'll go collect some wood."
hide yuuna with dissolve
"I nod, and the two of us get to work building the fire. I packed a lighter with me so we wouldn't have to fiddle with stones like cavemen. {w}Soon, a bright fire chases away the shadows as the sun sets."
"Yuuna's face glows from the flame as the sun shines a halo behind her. I grab a couple of skewers and pass one to her. I know traditionally people use sticks but that always seemed kind of gross and unhygienic to me. {w}Yuuna looks at me, confused."
show yuuna cur at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/192.ogg"
ym "What's this for?"
pf "S'mores, of course!"
show yuuna sur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/193.ogg"
ym "S'mores?"
pf "Don't tell me you've never had s'mores before!"
show yuuna thi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/194.ogg"
ym "Umm…"
"I grab the graham crackers, chocolate, and marshmallows."
pf "It is heaven in your mouth. First you put your marshmallow on your skewer to toast it over the fire."
show yuuna cur
"I hold my skewer above the flames to demonstrate. Yuuna hesitantly copies me."
pf "Then you take the graham crackers, chocolate, and marshmallow and combine it into one warm, melty sandwich!"
show yuuna smi
"Yuuna hides a giggle as she looks at my skewer."
pf "What?"
show yuuna mis
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/195.ogg"
ym "Is the marshmallow supposed to be charcoal?"
"I lift my skewer out of the fire and see that one side of my marshmallow is completely blackened."
pf "Dang! Why does that happen every time?!"
show yuuna hap
"Yuuna removes her skewer and bursts out laughing. Her marshmallow did not fare much better than mine."
pf "Let's try that again."
show yuuna smi
"We place fresh marshmallows on the skewers and successfully toast them. After completing our s'mores, Yuuna takes a big bite and her face lights up."
show yuuna sur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/196.ogg"
ym "This is delicious!"
pf "I know!"
show yuuna cur
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/197.ogg"
ym "This is something you do in America a lot?"
pf "It's a must for every campsite."
show yuuna smi
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/198.ogg"
ym "Ahh! I wish I'd had one sooner!"
show yuuna hap
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/199.ogg"
ym "Let's make another!"
pf "Okay."
show yuuna smi
"I grin as I pass Yuuna the items and watch as she eagerly puts the pieces together. I guess she really does love American stuff!"
"I think I see her shiver and notice the cool breeze as the sun disappears below the horizon."
if MCStory == 3:
    "The campfire burns even brighter as darkness settles in. Are those clouds in the sky?"
"Scooting closer, I wrap my arms around her as she focuses on her marshmallow. She blinks at my touch, then our gazes lock."
show yuuna smi b2 with dissolve
"She meets me in a kiss, her forgotten marshmallow burning on the skewer."
"Suddenly, a droplet hits my head. I break away in surprise and glance at the sky."
pf "Did you just feel a raindrop?"
show yuuna cur b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/200.ogg"
ym "No…"
"She gasps as a droplet falls on her nose."
show yuuna thi b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/201.ogg"
ym "I mean, yes."
show yuuna sad b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/202.ogg"
ym "It wasn't supposed to rain today!"
show yuuna sur b2
"As if those were the magic words which unlocked the sky, the rain pours down in a thick sheet of water. Yuuna's hair sticks to her face and neck as we are drenched within minutes!"
pf "Quickly! To the tent!"
hide yuuna with dissolve
stop music fadeout 5
scene black with fade
"I grab Yuuna's hand and we race into the dry safety of the tent, zipping it up behind us. I can hear Yuuna's teeth chattering in the darkness."
pf "We've got to get out of these clothes."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/203.ogg"
ym "W-What?!"
"My cheeks burn."
pf "We'll catch a cold if we stay in these wet clothes."
"She hesitates."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/204.ogg"
ym "Y-You're right… but we left the spare clothes in the car…"
"Suddenly, she pulls her top off."
pf "W-Wait!"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/205.ogg"
ym "Just turn around, okay?"
"I do as she obliges and strip down to my boxers."

$ persistent.gpix[75][0] = 1
$ persistent.gpix[76][0] = 1
$ persistent.gpix[77][0] = 1

scene cg yuuna tent 1 with fade:
    xzoom .5
    yzoom .5
"I glance over my shoulder and see Yuuna stripped down to her underclothes."
scene cg yuuna tent 2 with dissolve:
    xzoom .5
    yzoom .5
"She looks back at me over her shoulder and her cheeks turn pink."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/206.ogg"
ym "Stop peeking!"
pf "S-Sorry!"
scene cg yuuna tent 1 with dissolve:
    xzoom .5
    yzoom .5
play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 7
"There's a small lantern hanging on the top of the tent which provides a tiny bit of light in the darkness. We sit quietly as the rain patters against the tent. {w}I try not to think about Yuuna sitting half-naked behind me, but my mind keeps wandering back to it. Think about something else! Maybe I should ask her a question."
"Yuuna speaks before I can think of something to ask her."

scene cg yuuna tent 3 with dissolve:
    xzoom .5
    yzoom .5
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/207.ogg"
ym "So, um, have you ever played that game where you write a word on someone's back and they have to guess what it is?"
pf "Yeah…"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/208.ogg"
ym "...Want to play?"
pf "Sure."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/209.ogg"
ym "Okay! I-I'll go first."
"Yuuna's trying to ease the tension and pretend like nothing unusual is happening, but I can hear the anxiety in her voice."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/210.ogg"
ym "Don't look, okay?"
"She gently traces her finger along my back. My skin tingles where she touches."
pf "Oh, we're playing in English?"
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/211.ogg"
ym "Yes!"
"She continues to trace letters on my back one after another."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/212.ogg"
ym "Okay, done. What did I write?"
"Hmm… It felt like something that started with an \"h\" and ended with a \"y\"."

menu:
    "Healthy!":
        pf "Was it \"healthy\"?"
        "She giggles."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/213.ogg"
        ym "Kind of close? But no."
        pf "Darn."
        "I guess that wouldn't make as much sense for Yuuna. Kaori's the health nut."
        jump E4YMS3_wrongguess

    "Happy!":
        pf "It felt like \"happy\"."
        "Yuuna claps."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/214.ogg"
        ym "Yes, that was it!"
        pf "Is that how you feel right now?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/215.ogg"
        ym "Yes…"
        "Her voice is soft and I can imagine the blush on her cheeks."
        pf "I feel that way too."

    "History!":
        pf "Hm… is it \"history\"?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/216.ogg"
        ym "No, but good guess!"
        pf "I thought that might be it since we have that class together."
        label E4YMS3_wrongguess:
            pf "What was it?"
            voice "audio/voice/MISSING/BATCH6/Redo 2.ogg"
            ym "\"Happy\"!"
            pf "Aw, that's a good one."
            voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/217.ogg"
            ym "It's how I feel when I'm with you."
            "I'm glad we have our backs facing each other. I don't want her to see how red my face is."

voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/218.ogg"
ym "Okay, your turn."
scene cg yuuna tent 1 with dissolve:
    xzoom .5
    yzoom .5
"I hear her settle into place and then I turn to face her back. Her skin is porcelain smooth. As I gently brush her hair out of the way, I wonder what I should write…"

menu:
    "Love.":
        $ E4YMS3_love = 1
        "I trace the word \"love\" on her back, acutely aware of the warmth of her skin."
        pf "Okay, what is it?"
        "Her cheeks turn pink and I think she knows what it is."
        
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/219.ogg"
        ym "Is it \"love\"?"
        pf "You got it."
        "Her blush deepens."

    "ORAL!":
        $ E4YMS3_oral = 1
        "Hehehe, I know just the word! I trace \"oral\" on her back, trying not to giggle as I write."
        "Judging from Yuuna's bright cheeks, I think she's guessed it."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/220.ogg"
        ym "\"Oral\"?"
        "I can't hold back my grin."
        pf "Yeah."
        "Yuuna's blush deepens and she doesn't say anything for a while. I'm a little worried I've offended her…"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/221.ogg"
        ym "...Okay."
        "Maybe that wasn't the best choice to make… at least now we can move on."
        pf "Okay."
        "I get back into position so she can write on my back, but she doesn't move."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/222.ogg"
        ym "...So, me or you?"
        pf "It's you now."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/223.ogg"
        ym "Okay."
        "She still doesn't move…"
        scene cg yuuna tent 3 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/224.ogg"
        ym "A-Aren't you going to turn around?"
        pf "Wait, what?"
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/225.ogg"
        ym "What?"
        "I twist to look at her. She's facing me with lowered eyes."
        pf "It's your turn for the game."
        "Not only does her face turn red, but her blush creeps down her neck and chest too."
        scene cg yuuna tent 1 with dissolve:
            xzoom .5
            yzoom .5
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/226.ogg"
        ym "N-Nevermind! Yes! The game!"
        "All I can do is stare. Did she really--was she going to--?!"
        "I shake the thought away. There's {i}no{/i} way she meant what's on my mind right now!"
        "...I think."

    "Pretty.":
        "I trace \"pretty\" on her back. The best way to describe her."
        "She blushes and I can tell she's guessed it."
        pf "Okay, done."
        voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/227.ogg"
        ym "Is it \"pretty\"?"
        pf "It sure is."
        "She blushes even further."

scene black with fade
"We play a few more rounds then chat for a few hours. Times goes by in flash as we enjoy each others company and it looks like the rain has stopped. I peek outside, and sure enough, the only rain is from dripping leaves."
pf "I'll go to the car and get our clothes. You stay here."
"Yuuna nods."
$renpy.pause(1.0)
"Once I come back with the rest of our supplies, we quickly get changed and tuck ourselves into our sleeping bags after turning off the lantern."
"It's pitch black inside, only the subtle noise of shuffling creates a sense of space."

voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/228.ogg"
ym "I'm a little cold..."
"Her voice is muffled from the sleeping bag."
pf "Maybe I can fix that…"
"I scoot my bag even closer to hers and sling my arm around her. She smiles as she leans against me."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/229.ogg"
ym "This is nice."

if E4YMS3_love == 1:
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/230.ogg"
    ym "Earlier, when we were playing that game… how did you choose which word to write?"
    pf "I just wrote what I feel."
    "She gasps slightly and looks up at me, then looks away as a blush stains her cheeks."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/231.ogg"
    ym "I think that's what I feel too."
    "When she makes eye contact again, I hug her even closer to me as my lips meet her own. I take a sharp breath and breathe in her familiar scent. Her arms slip out of the sleeping bag and wrap around my neck."
    "My lips linger as she gently pulls away and cuddles into me."

if E4YMS3_oral == 1:
    "I can't stop thinking about our game earlier and how Yuuna… I need to know!"
    pf "Yuuna…"
    voice "audio/voice/MISSING/BATCH6/Redo 3.ogg"
    ym "Hm?"
    pf "About earlier, when we were playing the writing game…"
    "I'm not sure how to ask this. Yuuna blushes deeply."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/232.ogg"
    ym "Um, what about it?"
    pf "Were you really going to--I mean--"
    "Her face is redder than a tomato."
    voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/233.ogg"
    ym "I think it's time to go to sleep now!"
    "She burrows into my chest, trying to hide her face."
    "Was she just teasing me earlier then…? Now I'm even more unsure!"
stop music fadeout 3.0
"We stay this way and enjoy the fullness of each other's company. I listen to the soft sound of her breathing and the stillness of the night, before drifting to sleep."

$renpy.pause(2.5)
play ambient "audio/ambience/Morning.ogg" fadein 3
"When I awake, Yuuna is still cuddled up against me. I smile at her sleeping form. She looks so peaceful, and the sunlight filtering through the cracks of the tent frame her like an angel."
play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
scene bg vacation camp dusk with fade
"I brush a stray hair away from her face and she blinks her eyes open."
show yuuna smi b2 at cc with dissolve
"She smiles as her gaze fixes on me."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/234.ogg"
ym "Good morning."
pf "Morning."
"She stretches lazily and yawns."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/235.ogg"
ym "Did you sleep well?"
pf "Very well, actually. How about you?"
show yuuna hap b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/236.ogg"
ym "Very well too."
"We stay where we are for a while longer before Yuuna reluctantly sighs."
show yuuna thi b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/237.ogg"
ym "I think it's time for us to pack up."
pf "Are you sure?"
show yuuna smi b2
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/238.ogg"
ym "Yeah…"
hide yuuna with dissolve
scene black with fade
stop ambient fadeout 1.5
"I sigh, then nod. We crawl out of our sleeping bags and get to work cleaning up the camp. After heating up some of the food Yuuna brought, we pack everything up into the car and drive back."
scene bg isokaze neighborhood day with fade
"I drop her off in front of her house and help carry her things to her door."
show yuuna smi b1 at cc with dissolve
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/239.ogg"
ym "Thanks so much for taking me on this trip. I had a great time."
pf "Me too."
voice "audio/voice/E4/Yuuna/E4/Yuuna Arc/240.ogg"
ym "I'll see you on Monday?"
pf "Yup."
scene black with fade

"Our lips meet for one last kiss. Yuuna smiles and heads into her house while I get back into my car and drive home."



stop music fadeout 3
stop ambient fadeout 3
$renpy.pause(2.5)
$ E4YMS3_Completed = 1
jump E4D7S1