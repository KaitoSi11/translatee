#
label E4Epilogue:

scene black with Dissolve(1.75)
$renpy.pause(.5)
scene white with Dissolve(1.5)

image creditscroll:
    Text("{b}{size=32}Producers{/size}{/b}\n  Dishu Khan\n  Rishu Khan\n  Donnie Roos\n  Ex Zee\n  Mahkcloud\n\n\n{b}{size=32}Director{/size}{/b}\n  Dishu Khan\n\n\n{b}{size=32}Artists{/size}{/b}\n  Sunimu\n  Keith Chan Xeikth\n  Teagirl-vn\n  Shoji\n\n\n{b}{size=32}Writers{/size}{/b}\n  Alisia Faust\n  Dishu Khan\n\n\n{b}{size=32}Programmers{/size}{/b}\n  Austin Bryant\n  Dishu Khan\n\n\n{b}{size=32}Composer{/size}{/b}\n  Christopher Escalante\n\n\n{b}{size=32}Audio Production{/size}{/b}\n  Dishu Khan\n\n\n{b}{size=32}Voice Talent{/size}{/b}\n  Tina \"Pickle131\" Kim - {i}Nikki{/i}\n  Sydney \"Sydsnap\" Poniewaz - {i}Kaori Itami{/i}\n  Samantha Chan - {i}Yuuna Misaki{/i}\n  Angela Lorenzana - {i}Valerie Belle{/i}\n  Alexandra Boodram - {i}Mayu Akemi{/i}\n  Kim Morton - {i}Shou Shinjirou{/i}\n  Bradley Petyak - {i}Kaito Hikari{/i}\n  Amanda Lee - {i}Mei Satomi // AmaLee{/i}\n  Miguel Moran - {i}Akira Masata // Various Roles{/i}\n  James Brown Jr. - {i}Eagle // Various Roles{/i}\n  Olivia Steele - {i}Yuki Hikari // Various Roles{/i}\n  Kyle Lumash - {i}Ken Kokan // Various Roles{/i}\n  Christopher Escalante - {i}Various Roles{/i}\n  Lee Turner - {i}Various Roles{/i}\n  Peter Colon - {i}Various Roles{/i}\n  Luci W. - {i}Various Roles{/i}\n  Alexandria B. - {i}Various Roles{/i}\n  Arthur Romeo - {i}Various Roles{/i}\n\n\n{b}{size=32}PixelFaders - KS{/size}{/b}\n  Jorgen Robertson\n  Daniel Kruse\n  Gilbert\n  Aaron - Exiled WereSheep in Torment\n  Anthony\n  Jambles\n  Phoenix\n  Matthew Spreeman\n  RUI CHENG\n  Kingz\n  Kyle Abeyta\n  Wade Clemons\n  First Mate Shou\n  Daniel Evans\n  ZeroGamer\n  Mr_Enigma\n  KennyJ\n  Hubert Volecek\n  Erwin Sutrisno\n  Alec Greenbank\n  Bryan\n  Luke Harrison\n  Erde\n  Alexander John Aristotle Kimball\n  BuffAnimeScientist\n  Bryan Tsang\n  Cap'n Kaori\n  Redcomet\n  YP Lim\n  Rei Aoki\n  William Taylor Lashbrook\n  Alen Wong\n  Lukasz Pawlus\n  Simon W. Steen\n  LordRevan\n  Océane Gulini\n  Iikka Yli-Kuivila\n  Solomatin Mikhail\n  Erwin Matthew Patalinghug\n  Annatalonstv\n\n\n{b}{size=32}{color=#5f497a}PixelFaders - LVL3{/color}{/size}{/b}\n  Matthew Harper\n  Konrad Michalek\n  Daniel Evans\n  James Ryan Sisk\n  Aegeta \n  Duc \n  Christopher Oates\n  Austin McCoy\n  Mikhail Solomatin\n  Liam Poole\n  Gin \n  Sean Jewett\n  Tristan Medina\n  IIIllIIl \n  Jacob Harmon\n  Thomas Richard Wall\n  Butlee \n  jimmylamtk \n  terrman \n  Toh Xin Tian\n  Vox Chaotica\n  technocat \n  Alexander Adler\n  Ocacane Gulini\n  Tomi Arola\n  Steinar Hagen\n  Daniel Needs\n\n\n{b}{size=32}{color=#1f497d}PixelFaders - LVL2{/color}{/size}{/b}\n  BitFaze \n  BlaÅz \n  Callum Horton\n  mccallam21\n\n\n{b}{size=32}{color=#4f6128}PixelFaders - LVL1{/color}{/size}{/b}\n  Juho Kainulainen\n  James  Connally\n  Daniel Chung\n  Candy-Sama \n  David Manuel Sousa Carvalho\n  CrashRocks1419\n  The Crushor\n  Ben Goldstein\n  Peter Villumsen\n\n{size=20}For complete credits, please see Extra > Credits!{/size}", size=24, color="#000000")
    anchor (1, 0)
    pos (0.05, 1.0)
    linear 140 ypos 0.0 yanchor 1.0


image epilogue1 = "i/epilogue/1.png"

image epilogue2:
    "i/sprites/empty.png"
    pause 3
    "i/epilogue/17.jpg"
    alpha 0
    ypos 0.6
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/15.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/32.jpg"
    alpha 0
    ypos 0.5
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/5.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/23.jpg"
    alpha 0
    ypos 0.6
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/4.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/11.jpg"
    alpha 0
    ypos 0.5
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/7.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/27.jpg"
    alpha 0
    ypos 0.6
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/28.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/30.jpg"
    alpha 0
    ypos 0.5
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/18.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/10.jpg"
    alpha 0
    ypos 0.6
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/20.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/19.jpg"
    alpha 0
    ypos 0.5
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/25.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/24.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .25
    yzoom .25
    parallel:
        easein 3.0 yoffset 50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/6.jpg"
    alpha 0
    ypos 0.6
    xpos 0.5
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 yoffset -50
    parallel:
        easein 2 alpha 1
    pause 3
    easeout 1 alpha 0
    xoffset 0
    yoffset 0
    "i/epilogue/26.jpg"
    alpha 0
    ypos 0.4
    xpos 0.6
    yanchor .5
    xanchor .5
    xzoom .3
    yzoom .3
    parallel:
        easein 3.0 xoffset -50
    parallel:
        easein 2 alpha 1
    pause 4.5
    easeout 1 alpha 0
    xoffset 0
    yoffset 0


    
    
    
    

show epilogue1 with Dissolve(1.25):
    xzoom .8
    yzoom .8
    yalign .5
    xalign .5
    

$renpy.pause(2.5,hard="True")
show epilogue2
show creditscroll
hide epilogue1 with Dissolve(1.5)


$renpy.pause(6, hard="True")  
$renpy.pause(106)
stop music fadeout 26
$renpy.pause(25)

scene black with Dissolve(2.0)
    
$renpy.pause(1.5)


jump E4END

return