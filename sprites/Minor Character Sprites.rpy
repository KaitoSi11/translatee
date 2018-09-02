################################################# ~ Miguel ~ #################################################

image migGlasses = ConditionSwitch (
        "migGlasses == 0", "i/sprites/empty.png",
        "migGlasses == 1", "i/sprites/miguel/accessories/glasses.png"
        )

image miguel hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/miguel/outfits/base.png",
    ( 0, 0 ), "mighap",
    ( 0, 0 ), "i/sprites/miguel/hairstyles/default/front.png",
    ( 0, 0 ), "migGlasses"
    )

image miguel mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/miguel/outfits/base.png",
    ( 0, 0 ), "migmis",
    ( 0, 0 ), "i/sprites/miguel/hairstyles/default/front.png",
    ( 0, 0 ), "migGlasses"
    )

image miguel neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/miguel/outfits/base.png",
    ( 0, 0 ), "migneu",
    ( 0, 0 ), "i/sprites/miguel/hairstyles/default/front.png",
    ( 0, 0 ), "migGlasses"
    )

image miguel smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/miguel/outfits/base.png",
    ( 0, 0 ), "migsmi",
    ( 0, 0 ), "i/sprites/miguel/hairstyles/default/front.png",
    ( 0, 0 ), "migGlasses"
    )

image miguel sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/miguel/outfits/base.png",
    ( 0, 0 ), "migsur",
    ( 0, 0 ), "i/sprites/miguel/hairstyles/default/front.png",
    ( 0, 0 ), "migGlasses"
    )


image mighap:
    "i/sprites/miguel/expressions/happy/1.png"

image migmis:
    "i/sprites/miguel/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/miguel/expressions/mischievous/2.png"
    .05
    "i/sprites/miguel/expressions/mischievous/3.png"
    .05
    "i/sprites/miguel/expressions/mischievous/4.png"
    .05
    "i/sprites/miguel/expressions/mischievous/3.png"
    .05
    "i/sprites/miguel/expressions/mischievous/2.png"
    .05
    repeat
    
image migneu:
    "i/sprites/miguel/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/miguel/expressions/neutral/2.png"
    .05
    "i/sprites/miguel/expressions/neutral/3.png"
    .05
    "i/sprites/miguel/expressions/neutral/4.png"
    .05
    "i/sprites/miguel/expressions/neutral/3.png"
    .05
    "i/sprites/miguel/expressions/neutral/2.png"
    .05
    repeat
    
image migsmi:
    "i/sprites/miguel/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/miguel/expressions/smiling/2.png"
    .05
    "i/sprites/miguel/expressions/smiling/3.png"
    .05
    "i/sprites/miguel/expressions/smiling/4.png"
    .05
    "i/sprites/miguel/expressions/smiling/3.png"
    .05
    "i/sprites/miguel/expressions/smiling/2.png"
    .05
    repeat
    
image migsur:
    "i/sprites/miguel/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/miguel/expressions/surprised/2.png"
    .05
    "i/sprites/miguel/expressions/surprised/3.png"
    .05
    "i/sprites/miguel/expressions/surprised/4.png"
    .05
    "i/sprites/miguel/expressions/surprised/3.png"
    .05
    "i/sprites/miguel/expressions/surprised/2.png"
    .05
    repeat
    
# end Miguel

################################################# ~ boyfriend ~ #################################################

image boyOut = ConditionSwitch (
        "boyOut == 'default'", "i/sprites/boyfriend/outfits/base.png"
        )

image boyfriend ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyang",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyann",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boycur",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boydis",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyhap",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boymis",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyner",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyneu",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boysad",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boyske",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boysmi",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boysur",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boythi",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boywin",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyfriend wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "boyOut",
    ( 0, 0 ), "boywor",
    ( 0, 0 ), "i/sprites/boyfriend/hairstyles/default/front.png"
    )

image boyang:
    "i/sprites/boyfriend/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/angry/2.png"
    .05
    "i/sprites/boyfriend/expressions/angry/3.png"
    .05
    "i/sprites/boyfriend/expressions/angry/4.png"
    .05
    "i/sprites/boyfriend/expressions/angry/3.png"
    .05
    "i/sprites/boyfriend/expressions/angry/2.png"
    .05
    repeat

image boyann:
    "i/sprites/boyfriend/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/annoyed/2.png"
    .05
    "i/sprites/boyfriend/expressions/annoyed/3.png"
    .05
    "i/sprites/boyfriend/expressions/annoyed/4.png"
    .05
    "i/sprites/boyfriend/expressions/annoyed/3.png"
    .05
    "i/sprites/boyfriend/expressions/annoyed/2.png"
    .05
    repeat


image boycur:
    "i/sprites/boyfriend/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/curious/2.png"
    .05
    "i/sprites/boyfriend/expressions/curious/3.png"
    .05
    "i/sprites/boyfriend/expressions/curious/4.png"
    .05
    "i/sprites/boyfriend/expressions/curious/3.png"
    .05
    "i/sprites/boyfriend/expressions/curious/2.png"
    .05
    repeat

image boydis:
    "i/sprites/boyfriend/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/disappointed/2.png"
    .05
    "i/sprites/boyfriend/expressions/disappointed/3.png"
    .05
    "i/sprites/boyfriend/expressions/disappointed/4.png"
    .05
    "i/sprites/boyfriend/expressions/disappointed/3.png"
    .05
    "i/sprites/boyfriend/expressions/disappointed/2.png"
    .05
    repeat
    
image boyhap:
    "i/sprites/boyfriend/expressions/happy/1.png"

image boymis:
    "i/sprites/boyfriend/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/mischievous/2.png"
    .05
    "i/sprites/boyfriend/expressions/mischievous/3.png"
    .05
    "i/sprites/boyfriend/expressions/mischievous/4.png"
    .05
    "i/sprites/boyfriend/expressions/mischievous/3.png"
    .05
    "i/sprites/boyfriend/expressions/mischievous/2.png"
    .05
    repeat
    
image boyner:
    "i/sprites/boyfriend/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/nervous/2.png"
    .05
    "i/sprites/boyfriend/expressions/nervous/3.png"
    .05
    "i/sprites/boyfriend/expressions/nervous/4.png"
    .05
    "i/sprites/boyfriend/expressions/nervous/3.png"
    .05
    "i/sprites/boyfriend/expressions/nervous/2.png"
    .05
    repeat

image boyneu:
    "i/sprites/boyfriend/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/neutral/2.png"
    .05
    "i/sprites/boyfriend/expressions/neutral/3.png"
    .05
    "i/sprites/boyfriend/expressions/neutral/4.png"
    .05
    "i/sprites/boyfriend/expressions/neutral/3.png"
    .05
    "i/sprites/boyfriend/expressions/neutral/2.png"
    .05
    repeat
    
image boysad:
    "i/sprites/boyfriend/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/sad/2.png"
    .05
    "i/sprites/boyfriend/expressions/sad/3.png"
    .05
    "i/sprites/boyfriend/expressions/sad/4.png"
    .05
    "i/sprites/boyfriend/expressions/sad/3.png"
    .05
    "i/sprites/boyfriend/expressions/sad/2.png"
    .05
    repeat
    
image boyske:
    "i/sprites/boyfriend/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/skeptical/2.png"
    .05
    "i/sprites/boyfriend/expressions/skeptical/3.png"
    .05
    "i/sprites/boyfriend/expressions/skeptical/4.png"
    .05
    "i/sprites/boyfriend/expressions/skeptical/3.png"
    .05
    "i/sprites/boyfriend/expressions/skeptical/2.png"
    .05
    repeat
    
image boysmi:
    "i/sprites/boyfriend/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/smiling/2.png"
    .05
    "i/sprites/boyfriend/expressions/smiling/3.png"
    .05
    "i/sprites/boyfriend/expressions/smiling/4.png"
    .05
    "i/sprites/boyfriend/expressions/smiling/3.png"
    .05
    "i/sprites/boyfriend/expressions/smiling/2.png"
    .05
    repeat
    
image boysur:
    "i/sprites/boyfriend/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/surprised/2.png"
    .05
    "i/sprites/boyfriend/expressions/surprised/3.png"
    .05
    "i/sprites/boyfriend/expressions/surprised/4.png"
    .05
    "i/sprites/boyfriend/expressions/surprised/3.png"
    .05
    "i/sprites/boyfriend/expressions/surprised/2.png"
    .05
    repeat
    
image boythi:
    "i/sprites/boyfriend/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/thinking/2.png"
    .05
    "i/sprites/boyfriend/expressions/thinking/3.png"
    .05
    "i/sprites/boyfriend/expressions/thinking/4.png"
    .05
    "i/sprites/boyfriend/expressions/thinking/3.png"
    .05
    "i/sprites/boyfriend/expressions/thinking/2.png"
    .05
    repeat
    
image boywin:
    "i/sprites/boyfriend/expressions/wincing/1.png"
    
image boywor:
    "i/sprites/boyfriend/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/boyfriend/expressions/worried/2.png"
    .05
    "i/sprites/boyfriend/expressions/worried/3.png"
    .05
    "i/sprites/boyfriend/expressions/worried/4.png"
    .05
    "i/sprites/boyfriend/expressions/worried/3.png"
    .05
    "i/sprites/boyfriend/expressions/worried/2.png"
    .05
    repeat
    
    
# end boyfriend

################################################# ~ donnie ~ #################################################

image donScanner = ConditionSwitch (
        "donScanner == 0", "i/sprites/empty.png",
        "donScanner == 1", "i/sprites/donnie/accessories/scanner.png"
        )

image donTie = ConditionSwitch (
        "donTie == 0", "i/sprites/donnie/accessories/no tie.png",
        "donTie == 1", "i/sprites/empty.png"
        )

image donnie ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donang",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donann",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "doncur",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "dondis",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donhap",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donmis",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donner",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donneu",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donsad",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donske",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donsmi",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donsur",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donthi",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donwin",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donnie wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/donnie/outfits/base.png",
    ( 0, 0 ), "donwor",
    ( 0, 0 ), "i/sprites/donnie/hairstyles/default/front.png",
    ( 0, 0 ), "donTie",
    ( 0, 0 ), "donScanner"
    )

image donang:
    "i/sprites/donnie/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/angry/2.png"
    .05
    "i/sprites/donnie/expressions/angry/3.png"
    .05
    "i/sprites/donnie/expressions/angry/4.png"
    .05
    "i/sprites/donnie/expressions/angry/3.png"
    .05
    "i/sprites/donnie/expressions/angry/2.png"
    .05
    repeat

image donann:
    "i/sprites/donnie/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/annoyed/2.png"
    .05
    "i/sprites/donnie/expressions/annoyed/3.png"
    .05
    "i/sprites/donnie/expressions/annoyed/4.png"
    .05
    "i/sprites/donnie/expressions/annoyed/3.png"
    .05
    "i/sprites/donnie/expressions/annoyed/2.png"
    .05
    repeat


image doncur:
    "i/sprites/donnie/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/curious/2.png"
    .05
    "i/sprites/donnie/expressions/curious/3.png"
    .05
    "i/sprites/donnie/expressions/curious/4.png"
    .05
    "i/sprites/donnie/expressions/curious/3.png"
    .05
    "i/sprites/donnie/expressions/curious/2.png"
    .05
    repeat

image dondis:
    "i/sprites/donnie/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/disappointed/2.png"
    .05
    "i/sprites/donnie/expressions/disappointed/3.png"
    .05
    "i/sprites/donnie/expressions/disappointed/4.png"
    .05
    "i/sprites/donnie/expressions/disappointed/3.png"
    .05
    "i/sprites/donnie/expressions/disappointed/2.png"
    .05
    repeat
    
image donhap:
    "i/sprites/donnie/expressions/happy/1.png"

image donmis:
    "i/sprites/donnie/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/mischievous/2.png"
    .05
    "i/sprites/donnie/expressions/mischievous/3.png"
    .05
    "i/sprites/donnie/expressions/mischievous/4.png"
    .05
    "i/sprites/donnie/expressions/mischievous/3.png"
    .05
    "i/sprites/donnie/expressions/mischievous/2.png"
    .05
    repeat
    
image donner:
    "i/sprites/donnie/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/nervous/2.png"
    .05
    "i/sprites/donnie/expressions/nervous/3.png"
    .05
    "i/sprites/donnie/expressions/nervous/4.png"
    .05
    "i/sprites/donnie/expressions/nervous/3.png"
    .05
    "i/sprites/donnie/expressions/nervous/2.png"
    .05
    repeat

image donneu:
    "i/sprites/donnie/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/neutral/2.png"
    .05
    "i/sprites/donnie/expressions/neutral/3.png"
    .05
    "i/sprites/donnie/expressions/neutral/4.png"
    .05
    "i/sprites/donnie/expressions/neutral/3.png"
    .05
    "i/sprites/donnie/expressions/neutral/2.png"
    .05
    repeat
    
image donsad:
    "i/sprites/donnie/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/sad/2.png"
    .05
    "i/sprites/donnie/expressions/sad/3.png"
    .05
    "i/sprites/donnie/expressions/sad/4.png"
    .05
    "i/sprites/donnie/expressions/sad/3.png"
    .05
    "i/sprites/donnie/expressions/sad/2.png"
    .05
    repeat
    
image donske:
    "i/sprites/donnie/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/skeptical/2.png"
    .05
    "i/sprites/donnie/expressions/skeptical/3.png"
    .05
    "i/sprites/donnie/expressions/skeptical/4.png"
    .05
    "i/sprites/donnie/expressions/skeptical/3.png"
    .05
    "i/sprites/donnie/expressions/skeptical/2.png"
    .05
    repeat
    
image donsmi:
    "i/sprites/donnie/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/smiling/2.png"
    .05
    "i/sprites/donnie/expressions/smiling/3.png"
    .05
    "i/sprites/donnie/expressions/smiling/4.png"
    .05
    "i/sprites/donnie/expressions/smiling/3.png"
    .05
    "i/sprites/donnie/expressions/smiling/2.png"
    .05
    repeat
    
image donsur:
    "i/sprites/donnie/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/surprised/2.png"
    .05
    "i/sprites/donnie/expressions/surprised/3.png"
    .05
    "i/sprites/donnie/expressions/surprised/4.png"
    .05
    "i/sprites/donnie/expressions/surprised/3.png"
    .05
    "i/sprites/donnie/expressions/surprised/2.png"
    .05
    repeat
    
image donthi:
    "i/sprites/donnie/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/thinking/2.png"
    .05
    "i/sprites/donnie/expressions/thinking/3.png"
    .05
    "i/sprites/donnie/expressions/thinking/4.png"
    .05
    "i/sprites/donnie/expressions/thinking/3.png"
    .05
    "i/sprites/donnie/expressions/thinking/2.png"
    .05
    repeat
    
image donwin:
    "i/sprites/donnie/expressions/wincing/1.png"
    
image donwor:
    "i/sprites/donnie/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/donnie/expressions/worried/2.png"
    .05
    "i/sprites/donnie/expressions/worried/3.png"
    .05
    "i/sprites/donnie/expressions/worried/4.png"
    .05
    "i/sprites/donnie/expressions/worried/3.png"
    .05
    "i/sprites/donnie/expressions/worried/2.png"
    .05
    repeat
    
    
# end donnie

################################################# ~ ivan ~ #################################################

image ivaHelmet = ConditionSwitch (
        "ivaHelmet == '0'", "i/sprites/empty.png",
        "ivaHelmet == '1'", "i/sprites/ivan/accessories/helmet.png"
        )

image ivaOut = ConditionSwitch (
        "ivaOut == 'default'", "i/sprites/ivan/outfits/base.png",
        "ivaOut == 'open'", "i/sprites/ivan/outfits/open.png"
        )

image ivan ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivaang",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivaann",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivacur",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivadis",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivahap",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivamis",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivaner",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivaneu",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivasad",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivaske",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivasmi",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivasur",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivathi",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivawin",
    ( 0, 0 ), "ivaHelmet"
    )

image ivan wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "ivaOut",
    ( 0, 0 ), "ivawor",
    ( 0, 0 ), "ivaHelmet"
    )

image ivaang:
    "i/sprites/ivan/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/angry/2.png"
    .05
    "i/sprites/ivan/expressions/angry/3.png"
    .05
    "i/sprites/ivan/expressions/angry/4.png"
    .05
    "i/sprites/ivan/expressions/angry/3.png"
    .05
    "i/sprites/ivan/expressions/angry/2.png"
    .05
    repeat

image ivaann:
    "i/sprites/ivan/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/annoyed/2.png"
    .05
    "i/sprites/ivan/expressions/annoyed/3.png"
    .05
    "i/sprites/ivan/expressions/annoyed/4.png"
    .05
    "i/sprites/ivan/expressions/annoyed/3.png"
    .05
    "i/sprites/ivan/expressions/annoyed/2.png"
    .05
    repeat


image ivacur:
    "i/sprites/ivan/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/curious/2.png"
    .05
    "i/sprites/ivan/expressions/curious/3.png"
    .05
    "i/sprites/ivan/expressions/curious/4.png"
    .05
    "i/sprites/ivan/expressions/curious/3.png"
    .05
    "i/sprites/ivan/expressions/curious/2.png"
    .05
    repeat

image ivadis:
    "i/sprites/ivan/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/disappointed/2.png"
    .05
    "i/sprites/ivan/expressions/disappointed/3.png"
    .05
    "i/sprites/ivan/expressions/disappointed/4.png"
    .05
    "i/sprites/ivan/expressions/disappointed/3.png"
    .05
    "i/sprites/ivan/expressions/disappointed/2.png"
    .05
    repeat
    
image ivahap:
    "i/sprites/ivan/expressions/happy/1.png"

image ivamis:
    "i/sprites/ivan/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/mischievous/2.png"
    .05
    "i/sprites/ivan/expressions/mischievous/3.png"
    .05
    "i/sprites/ivan/expressions/mischievous/4.png"
    .05
    "i/sprites/ivan/expressions/mischievous/3.png"
    .05
    "i/sprites/ivan/expressions/mischievous/2.png"
    .05
    repeat
    
image ivaner:
    "i/sprites/ivan/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/nervous/2.png"
    .05
    "i/sprites/ivan/expressions/nervous/3.png"
    .05
    "i/sprites/ivan/expressions/nervous/4.png"
    .05
    "i/sprites/ivan/expressions/nervous/3.png"
    .05
    "i/sprites/ivan/expressions/nervous/2.png"
    .05
    repeat

image ivaneu:
    "i/sprites/ivan/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/neutral/2.png"
    .05
    "i/sprites/ivan/expressions/neutral/3.png"
    .05
    "i/sprites/ivan/expressions/neutral/4.png"
    .05
    "i/sprites/ivan/expressions/neutral/3.png"
    .05
    "i/sprites/ivan/expressions/neutral/2.png"
    .05
    repeat
    
image ivasad:
    "i/sprites/ivan/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/sad/2.png"
    .05
    "i/sprites/ivan/expressions/sad/3.png"
    .05
    "i/sprites/ivan/expressions/sad/4.png"
    .05
    "i/sprites/ivan/expressions/sad/3.png"
    .05
    "i/sprites/ivan/expressions/sad/2.png"
    .05
    repeat
    
image ivaske:
    "i/sprites/ivan/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/skeptical/2.png"
    .05
    "i/sprites/ivan/expressions/skeptical/3.png"
    .05
    "i/sprites/ivan/expressions/skeptical/4.png"
    .05
    "i/sprites/ivan/expressions/skeptical/3.png"
    .05
    "i/sprites/ivan/expressions/skeptical/2.png"
    .05
    repeat
    
image ivasmi:
    "i/sprites/ivan/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/smiling/2.png"
    .05
    "i/sprites/ivan/expressions/smiling/3.png"
    .05
    "i/sprites/ivan/expressions/smiling/4.png"
    .05
    "i/sprites/ivan/expressions/smiling/3.png"
    .05
    "i/sprites/ivan/expressions/smiling/2.png"
    .05
    repeat
    
image ivasur:
    "i/sprites/ivan/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/surprised/2.png"
    .05
    "i/sprites/ivan/expressions/surprised/3.png"
    .05
    "i/sprites/ivan/expressions/surprised/4.png"
    .05
    "i/sprites/ivan/expressions/surprised/3.png"
    .05
    "i/sprites/ivan/expressions/surprised/2.png"
    .05
    repeat
    
image ivathi:
    "i/sprites/ivan/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/thinking/2.png"
    .05
    "i/sprites/ivan/expressions/thinking/3.png"
    .05
    "i/sprites/ivan/expressions/thinking/4.png"
    .05
    "i/sprites/ivan/expressions/thinking/3.png"
    .05
    "i/sprites/ivan/expressions/thinking/2.png"
    .05
    repeat
    
image ivawin:
    "i/sprites/ivan/expressions/wincing/1.png"
    
image ivawor:
    "i/sprites/ivan/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ivan/expressions/worried/2.png"
    .05
    "i/sprites/ivan/expressions/worried/3.png"
    .05
    "i/sprites/ivan/expressions/worried/4.png"
    .05
    "i/sprites/ivan/expressions/worried/3.png"
    .05
    "i/sprites/ivan/expressions/worried/2.png"
    .05
    repeat
    
    
# end ivan

################################################# ~ ken ~ #################################################

image kendirt = ConditionSwitch (
        "kenDirt == 0", "i/sprites/empty.png",
        "kenDirt == 1", "i/sprites/ken/accessories/dirt.png"
        )

image kenOut = ConditionSwitch (
        "kenOut == 'default'", "i/sprites/ken/outfits/summer - uniform.png",
        "kenOut == 'barista'", "i/sprites/ken/outfits/barista.png"
        )

image ken ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenang",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenann",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kencur",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kendis",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenhap",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenmis",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenner",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenneu",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kensad",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenske",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kensmi",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kensur",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenthi",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenwin",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image ken wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/ken/outfits/base.png",
    ( 0, 0 ), "kenOut",
    ( 0, 0 ), "kenwor",
    ( 0, 0 ), "i/sprites/ken/hairstyles/default/front.png",
    ( 0, 0 ), "kendirt"
    )

image kenang:
    "i/sprites/ken/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/angry/2.png"
    .05
    "i/sprites/ken/expressions/angry/3.png"
    .05
    "i/sprites/ken/expressions/angry/4.png"
    .05
    "i/sprites/ken/expressions/angry/3.png"
    .05
    "i/sprites/ken/expressions/angry/2.png"
    .05
    repeat

image kenann:
    "i/sprites/ken/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/annoyed/2.png"
    .05
    "i/sprites/ken/expressions/annoyed/3.png"
    .05
    "i/sprites/ken/expressions/annoyed/4.png"
    .05
    "i/sprites/ken/expressions/annoyed/3.png"
    .05
    "i/sprites/ken/expressions/annoyed/2.png"
    .05
    repeat


image kencur:
    "i/sprites/ken/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/curious/2.png"
    .05
    "i/sprites/ken/expressions/curious/3.png"
    .05
    "i/sprites/ken/expressions/curious/4.png"
    .05
    "i/sprites/ken/expressions/curious/3.png"
    .05
    "i/sprites/ken/expressions/curious/2.png"
    .05
    repeat

image kendis:
    "i/sprites/ken/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/disappointed/2.png"
    .05
    "i/sprites/ken/expressions/disappointed/3.png"
    .05
    "i/sprites/ken/expressions/disappointed/4.png"
    .05
    "i/sprites/ken/expressions/disappointed/3.png"
    .05
    "i/sprites/ken/expressions/disappointed/2.png"
    .05
    repeat
    
image kenhap:
    "i/sprites/ken/expressions/happy/1.png"

image kenmis:
    "i/sprites/ken/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/mischievous/2.png"
    .05
    "i/sprites/ken/expressions/mischievous/3.png"
    .05
    "i/sprites/ken/expressions/mischievous/4.png"
    .05
    "i/sprites/ken/expressions/mischievous/3.png"
    .05
    "i/sprites/ken/expressions/mischievous/2.png"
    .05
    repeat
    
image kenner:
    "i/sprites/ken/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/nervous/2.png"
    .05
    "i/sprites/ken/expressions/nervous/3.png"
    .05
    "i/sprites/ken/expressions/nervous/4.png"
    .05
    "i/sprites/ken/expressions/nervous/3.png"
    .05
    "i/sprites/ken/expressions/nervous/2.png"
    .05
    repeat

image kenneu:
    "i/sprites/ken/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/neutral/2.png"
    .05
    "i/sprites/ken/expressions/neutral/3.png"
    .05
    "i/sprites/ken/expressions/neutral/4.png"
    .05
    "i/sprites/ken/expressions/neutral/3.png"
    .05
    "i/sprites/ken/expressions/neutral/2.png"
    .05
    repeat
    
image kensad:
    "i/sprites/ken/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/sad/2.png"
    .05
    "i/sprites/ken/expressions/sad/3.png"
    .05
    "i/sprites/ken/expressions/sad/4.png"
    .05
    "i/sprites/ken/expressions/sad/3.png"
    .05
    "i/sprites/ken/expressions/sad/2.png"
    .05
    repeat
    
image kenske:
    "i/sprites/ken/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/skeptical/2.png"
    .05
    "i/sprites/ken/expressions/skeptical/3.png"
    .05
    "i/sprites/ken/expressions/skeptical/4.png"
    .05
    "i/sprites/ken/expressions/skeptical/3.png"
    .05
    "i/sprites/ken/expressions/skeptical/2.png"
    .05
    repeat
    
image kensmi:
    "i/sprites/ken/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/smiling/2.png"
    .05
    "i/sprites/ken/expressions/smiling/3.png"
    .05
    "i/sprites/ken/expressions/smiling/4.png"
    .05
    "i/sprites/ken/expressions/smiling/3.png"
    .05
    "i/sprites/ken/expressions/smiling/2.png"
    .05
    repeat
    
image kensur:
    "i/sprites/ken/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/surprised/2.png"
    .05
    "i/sprites/ken/expressions/surprised/3.png"
    .05
    "i/sprites/ken/expressions/surprised/4.png"
    .05
    "i/sprites/ken/expressions/surprised/3.png"
    .05
    "i/sprites/ken/expressions/surprised/2.png"
    .05
    repeat
    
image kenthi:
    "i/sprites/ken/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/thinking/2.png"
    .05
    "i/sprites/ken/expressions/thinking/3.png"
    .05
    "i/sprites/ken/expressions/thinking/4.png"
    .05
    "i/sprites/ken/expressions/thinking/3.png"
    .05
    "i/sprites/ken/expressions/thinking/2.png"
    .05
    repeat
    
image kenwin:
    "i/sprites/ken/expressions/wincing/1.png"
    
image kenwor:
    "i/sprites/ken/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/ken/expressions/worried/2.png"
    .05
    "i/sprites/ken/expressions/worried/3.png"
    .05
    "i/sprites/ken/expressions/worried/4.png"
    .05
    "i/sprites/ken/expressions/worried/3.png"
    .05
    "i/sprites/ken/expressions/worried/2.png"
    .05
    repeat
    
    
# end ken

################################################# ~ xz ~ #################################################

image xzNecklace = ConditionSwitch (
        "xzNecklace == 0", "i/sprites/xz/outfits/noNecklace.png",
        "xzNecklace == 1", "i/sprites/xz/outfits/withNecklace.png"
        )

image xz ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzann",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzcur",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzhap",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzmis",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzneu",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzsmi",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xz sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "xzNecklace",
    ( 0, 0 ), "xzsur",
    ( 0, 0 ), "i/sprites/xz/hairstyles/default/front.png"
    )

image xzann:
    "i/sprites/xz/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/xz/expressions/annoyed/2.png"
    .05
    "i/sprites/xz/expressions/annoyed/3.png"
    .05
    "i/sprites/xz/expressions/annoyed/4.png"
    .05
    "i/sprites/xz/expressions/annoyed/3.png"
    .05
    "i/sprites/xz/expressions/annoyed/2.png"
    .05
    repeat


image xzcur:
    "i/sprites/xz/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/xz/expressions/curious/2.png"
    .05
    "i/sprites/xz/expressions/curious/3.png"
    .05
    "i/sprites/xz/expressions/curious/4.png"
    .05
    "i/sprites/xz/expressions/curious/3.png"
    .05
    "i/sprites/xz/expressions/curious/2.png"
    .05
    repeat

image xzhap:
    "i/sprites/xz/expressions/happy/1.png"

image xzmis:
    "i/sprites/xz/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/xz/expressions/mischievous/2.png"
    .05
    "i/sprites/xz/expressions/mischievous/3.png"
    .05
    "i/sprites/xz/expressions/mischievous/4.png"
    .05
    "i/sprites/xz/expressions/mischievous/3.png"
    .05
    "i/sprites/xz/expressions/mischievous/2.png"
    .05
    repeat
    
image xzneu:
    "i/sprites/xz/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/xz/expressions/neutral/2.png"
    .05
    "i/sprites/xz/expressions/neutral/3.png"
    .05
    "i/sprites/xz/expressions/neutral/4.png"
    .05
    "i/sprites/xz/expressions/neutral/3.png"
    .05
    "i/sprites/xz/expressions/neutral/2.png"
    .05
    repeat
    
image xzsmi:
    "i/sprites/xz/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/xz/expressions/smiling/2.png"
    .05
    "i/sprites/xz/expressions/smiling/3.png"
    .05
    "i/sprites/xz/expressions/smiling/4.png"
    .05
    "i/sprites/xz/expressions/smiling/3.png"
    .05
    "i/sprites/xz/expressions/smiling/2.png"
    .05
    repeat
    
    
# end xz

################################################# ~ Yuri ~ #################################################

image yurGlasses = ConditionSwitch (
        "yurGlasses == 0", "i/sprites/empty.png",
        "yurGlasses == 1", "i/sprites/yuri/accessories/glasses.png"
        )

image yuri ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yurann",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yurcur",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yurhap",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yurmis",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yurneu",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yursmi",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yuri sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "i/sprites/yuri/outfits/base.png",
    ( 0, 0 ), "yursur",
    ( 0, 0 ), "i/sprites/yuri/hairstyles/default/front.png",
    ( 0, 0 ), "yurGlasses"
    )

image yurann:
    "i/sprites/yuri/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuri/expressions/annoyed/2.png"
    .05
    "i/sprites/yuri/expressions/annoyed/3.png"
    .05
    "i/sprites/yuri/expressions/annoyed/4.png"
    .05
    "i/sprites/yuri/expressions/annoyed/3.png"
    .05
    "i/sprites/yuri/expressions/annoyed/2.png"
    .05
    repeat


image yurcur:
    "i/sprites/yuri/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuri/expressions/curious/2.png"
    .05
    "i/sprites/yuri/expressions/curious/3.png"
    .05
    "i/sprites/yuri/expressions/curious/4.png"
    .05
    "i/sprites/yuri/expressions/curious/3.png"
    .05
    "i/sprites/yuri/expressions/curious/2.png"
    .05
    repeat

image yurhap:
    "i/sprites/yuri/expressions/happy/1.png"

image yurmis:
    "i/sprites/yuri/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuri/expressions/mischievous/2.png"
    .05
    "i/sprites/yuri/expressions/mischievous/3.png"
    .05
    "i/sprites/yuri/expressions/mischievous/4.png"
    .05
    "i/sprites/yuri/expressions/mischievous/3.png"
    .05
    "i/sprites/yuri/expressions/mischievous/2.png"
    .05
    repeat
    
image yurneu:
    "i/sprites/yuri/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuri/expressions/neutral/2.png"
    .05
    "i/sprites/yuri/expressions/neutral/3.png"
    .05
    "i/sprites/yuri/expressions/neutral/4.png"
    .05
    "i/sprites/yuri/expressions/neutral/3.png"
    .05
    "i/sprites/yuri/expressions/neutral/2.png"
    .05
    repeat
    
image yursmi:
    "i/sprites/yuri/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuri/expressions/smiling/2.png"
    .05
    "i/sprites/yuri/expressions/smiling/3.png"
    .05
    "i/sprites/yuri/expressions/smiling/4.png"
    .05
    "i/sprites/yuri/expressions/smiling/3.png"
    .05
    "i/sprites/yuri/expressions/smiling/2.png"
    .05
    repeat
    
    
# end yuri
