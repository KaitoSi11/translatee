########################
###### Usage Code #######
########################

#X axis sprite offsets are as follows:
    
    #L3 ~ xoffset 230
    #L2 ~ xoffset 365
    #L1 ~ xoffset 515
    #CC ~ xoffset 720
    #R1 ~ xoffset 890
    #R2 ~ xoffset 1040
    #R3 ~ xoffset 1175
 
    #show confused
    
    #show exclamation
    
    #show question
    
    #show frightful
    
    #show drooling
    
    #show shiny
    
    #show crying
    
    #show shocked
    
    #show panic
    
    #show storm
    
    #show bulb
    
    #show shoBlush
    
    #show tsuBlush
    
    #show regBlush
    
    #show dots
    
    #show vein
    
    #show drop
    
    #show heart
    
    #show note
    
    
########################
###### Character y Axis ####
########################

# In general, 150 for short characters and 50 for tall characters works good. These are probably also the range limits.

##### Akira #####
#show ?:
    #xoffset 720
    #yoffset 5
    #xzoom .75
    #yzoom .75

##### Kaito #####
#show ?:
    #xoffset 720
    #yoffset 5
    #xzoom .75
    #yzoom .75

##### Kaori #####
#show ?:
    #xoffset 720
    #yoffset 110
    #xzoom .75
    #yzoom .75

##### Mayu #####
#show ?:
    #xoffset 720
    #yoffset 135
    #xzoom .75
    #yzoom .75
    
##### Mei #####
#show ?:
    #xoffset 720
    #yoffset 100
    #xzoom .75
    #yzoom .75

##### Nikki #####
#show ?:
    #xoffset 720
    #yoffset 160
    #xzoom .75
    #yzoom .75

##### Shou #####
#show ?:
    #xoffset 720
    #yoffset 20
    #xzoom .75
    #yzoom .75

##### Valerie #####
#show ?:
    #xoffset 720
    #yoffset 125
    #xzoom .75
    #yzoom .75

##### Yuuna #####
#show ?:
    #xoffset 720
    #yoffset 100
    #xzoom .75
    #yzoom .75



########################
###### Emoticons Code ##
########################

image bubble:
        ycenter 100
        xcenter 100
        "emoticons/Bubble.png"
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0
        #repeat

image bubbleflip:
        ycenter 100
        xcenter 100
        im.Flip("emoticons/Bubble.png", horizontal=True)
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0
        #repeat
        
image note:
    alpha 0
    contains:
        "bubble"
    contains:
        xcenter 20 ycenter 30
        "emoticons/note/1.png"
        alpha 0
        xzoom 0.6
        yzoom 0.6
        easein 0.3 xzoom 0.8 yzoom 0.5 xcenter 80 ycenter 130 alpha 1.0
        easeout 0.3 yzoom 0.8 xcenter 110 ycenter 80
        linear 0.3 xcenter 150 ycenter 110
        easein 0.4 xcenter 200 ycenter 90 alpha 0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image heart:
    alpha 0
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/heart/1.png"
        alpha 0
        xzoom 0.3
        yzoom 0.3
        easeout 0.4 xzoom 1.2 yzoom 1.1 alpha 1.0
        easein 0.3 xzoom 0.8 yzoom 0.7
        parallel:
            easeout 0.4 xzoom 1.0 yzoom 0.9
            easein 0.3 xzoom 0.8 yzoom 0.7
        parallel:
            pause 0.3
            easeout 0.4 alpha 0.5
            easein 0.3  alpha 0.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0
    
image heart2:
    alpha 0
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/heart/1.png"
        alpha 0
        xzoom 0.3
        yzoom 0.3
        easeout 0.4 xzoom 1.2 yzoom 1.1 alpha 1.0
        easein 0.3 xzoom 0.8 yzoom 0.7
        parallel:
            easeout 0.4 xzoom 1.0 yzoom 0.9
            easein 0.3 xzoom 0.8 yzoom 0.7
        parallel:
            pause 0.3
            easeout 0.4 alpha 0.5
            easein 0.3  alpha 0.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image drop:
    alpha 0
    contains:
        "bubble"
    contains:
        xcenter 100 ycenter 20
        "emoticons/drop/1.png"
        alpha 0
        xzoom 0.5
        yzoom 0.4
        easeout 0.4 xzoom 0.7 yzoom 0.6 xcenter 100 ycenter 60 alpha 1.0
        linear 0.5 xzoom 0.7 yzoom 0.8 xcenter 100 ycenter 90
        parallel:
            easein 0.5 xzoom 0.7 yzoom 0.7 xcenter 100 ycenter 130
        parallel:
            pause 0.3
            easein 0.5 alpha 0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image vein:
    alpha 0
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/vein/1.png"
        alpha 0
        xzoom 0.3
        yzoom 0.3
        easeout 0.3 xzoom 1.1 yzoom 1.1 alpha 1.0
        easein 0.4 xzoom 0.6 yzoom 0.6
        easeout 0.3 xzoom 0.9 yzoom 0.9
        easein 0.4 xzoom 0.6 yzoom 0.6 alpha 0  
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image dots:
    alpha 0
    contains:
        "bubble"
    contains:
        xcenter 100
        ycenter 100
        xoffset 10
        alpha 0
        "emoticons/dots/1.png"
        time 0.25
        linear 0.4 alpha 1.0
    contains:
        xcenter 100
        ycenter 100
        xoffset 80
        alpha 0
        "emoticons/dots/1.png"
        time 0.50
        linear 0.4 alpha 1.0
    contains:
        xcenter 100
        ycenter 100
        xoffset 150
        alpha 0
        "emoticons/dots/1.png"
        time 0.75
        linear 0.4 alpha 1.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0
    
image dots2:
    alpha 0
    contains:
        "bubble"
    contains:
        xcenter 100
        ycenter 100
        xoffset 10
        alpha 0
        "emoticons/dots/1.png"
        time 0.25
        linear 0.4 alpha 1.0
    contains:
        xcenter 100
        ycenter 100
        xoffset 80
        alpha 0
        "emoticons/dots/1.png"
        time 0.50
        linear 0.4 alpha 1.0
    contains:
        xcenter 100
        ycenter 100
        xoffset 150
        alpha 0
        "emoticons/dots/1.png"
        time 0.75
        linear 0.4 alpha 1.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0
    
image regBlush:
    alpha 0
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "blush_eyes"
        linear 0.4 xcenter 103 
        linear 0.4 xcenter 97
        linear 0.4 xcenter 103
        linear 0.4 xcenter 97
    contains:
        ycenter 100
        xcenter 100
        "blush_face"
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8 
        easein 0.2 xzoom 1.0 yzoom 1.0   
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image tsuBlush:
    alpha 0
    contains:
        "bubble"
    contains:
        "emoticons/tsuBlush/1.png"
        ycenter 100
        xcenter 100
        xzoom 0.5 yoffset -5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1 yoffset 5
        easeout 0.25 xzoom 0.9 yzoom 0.8 yoffset -5
        easein 0.2 xzoom 1.0 yzoom 1.0 yoffset 5
        easeout 0.2 yoffset -3
        easeout 0.2 yoffset 3
        easeout 0.2 yoffset -3
        easeout 0.2 yoffset 3
    contains:
        "emoticons/tsuBlush/2.png"
        ycenter 100
        xcenter 100
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1 
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0 
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0
    
image shoBlush:
    alpha 0
    contains:
        "bubble"
    contains:
        ycenter 90
        xcenter 100
        ycenter 100
        xcenter 100
        xzoom 0.5
        yzoom 0.3
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
            easein 0.2 xzoom 1.0 yzoom 1.0
        parallel:
            pause 0.45
            "emoticons/shoBlush/2.png"
            pause 0.10
            Null()
            pause 0.10
            repeat
    contains:
        ycenter 100
        xcenter 100
        "emoticons/shoBlush/1.png"
        alpha 0.6
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8 
        easein 0.2 xzoom 1.0 yzoom 1.0 
    contains:
        "emoticons/shoBlush/3.png"
        ycenter 100
        xcenter 100
        xzoom 0.5
        yzoom 0.3
        easein 0.35 xzoom 1.2 yzoom 1.8 
        easeout 0.25 xzoom 1.1 yzoom 1.2
        easein 0.2 xzoom 1.0 yzoom 1.0 
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image exclamation:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        yoffset -100
        "emoticons/exclamation/1.png"
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            easein 0.38 yoffset 0
            easein 0.28 yoffset 20
            easeout 0.12 yoffset 0
        parallel:
            pause 0.4
            easein 0.28 yzoom 0.6
            easeout 0.28 yzoom 0.9
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image question:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        yoffset 15
        "emoticons/question/1.png"
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            easein 0.15 rotate -30
            easein 0.30 rotate +30
            easein 0.20 rotate -15
            easein 0.15 rotate +15
            easein 0.10 rotate 0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image bulb:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        yoffset 15
        "emoticons/bulb/1.png"
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            time 0.72
            "emoticons/bulb/2.png"
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image storm:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            pause 0.15
            "emoticons/storm/1.png"
            pause 0.15
            "emoticons/storm/2.png"
            pause 0.15
            "emoticons/storm/3.png"
            repeat
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0
    
image panic:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/panic/2.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
    contains:
        ycenter 100
        xcenter 100
        "emoticons/panic/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
    contains:
        ycenter 100
        xcenter 100
        parallel:
            "emoticons/panic/3.png"
            pause 0.15
            "emoticons/panic/4.png"
            pause 0.15
            "emoticons/panic/5.png"
            pause 0.15
            repeat
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image shocked:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        #yoffset 15
        "emoticons/shocked/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
    contains:
        ycenter 100
        xcenter 100
        xoffset 18
        yoffset -10
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            pause 0.45
            "emoticons/shocked/2.png"
            pause 0.10
            Null()
            pause 0.10
            repeat
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image crying:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        yoffset 12
        "emoticons/crying/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
    contains:
        ycenter 100
        xcenter 100
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            pause 0.75
            yoffset 17
            "emoticons/crying/2.png"
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image shiny:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/shiny/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0
    contains:
        ycenter 100
        xcenter 100
        parallel:
            "emoticons/shiny/2.png"
            pause 0.12
            "emoticons/shiny/3.png"
            pause 0.12
            "emoticons/shiny/4.png"
            pause 0.12
            "emoticons/shiny/3.png"
            pause 0.12
            "emoticons/shiny/2.png"
            pause 0.12
            repeat
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
            easein 0.2 xzoom 1.0 yzoom 1.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image drooling:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/drooling/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image frightful:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/frightful/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
    contains:
        ycenter 100
        xcenter 100
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
        parallel:
            pause 0.1
            yoffset -40
            "emoticons/frightful/2.png"
            linear 0.5 yoffset -10
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

image confused:
    contains:
        "bubble"
    contains:
        ycenter 100
        xcenter 100
        "emoticons/confused/1.png"
        easein 0.35 xzoom 1.2 yzoom 1.1
        easeout 0.25 xzoom 0.9 yzoom 0.8
        easein 0.2 xzoom 1.0 yzoom 1.0
    contains:
        ycenter 100
        xcenter 100
        alpha 0
        parallel:
            rotate 0
            xoffset -55
            yoffset -28
            "emoticons/confused/4.png"
            linear 1.0 rotate 359
            repeat
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
            easein 0.2 xzoom 1.0 yzoom 1.0
        parallel:
            easein 0.5 alpha 1
            time 1.0
            easeout 0.5 alpha 0
    contains:
        ycenter 100
        xcenter 100
        parallel:
            rotate 0
            xoffset +55
            yoffset -28
            "emoticons/confused/4.png"
            linear 1.0 rotate 359
            repeat
        parallel:
            easein 0.35 xzoom 1.2 yzoom 1.1
            easeout 0.25 xzoom 0.9 yzoom 0.8
            easein 0.2 xzoom 1.0 yzoom 1.0
        parallel:
            easein 0.5 alpha 1
            time 1.0
            easeout 0.5 alpha 0
    linear 0.4 alpha 1.0
    pause 0.9
    linear 0.4 alpha 0

#######################
## Common Image Defines
#######################

image blush_eyes:
    "emoticons/regBlush/2.png"
    ycenter 100
    xcenter 100
    xzoom 0.5
    yzoom 0.3
    easein 0.35 xzoom 1.2 yzoom 1.1 
    easeout 0.25 xzoom 0.9 yzoom 0.8
    easein 0.2 xzoom 1.0 yzoom 1.0
        
image blush_face:
    "emoticons/regBlush/1.png"
    alpha 1.0
    linear 0.4 alpha 1.2
    linear 0.4 alpha 0.8
    linear 0.4 alpha 1.3
    linear 0.4 alpha 0.8
        
image blush_eyes_shock:

###########################################################################################
## Spare Define. Maybe a different beating heart animation. Was already in the sample code.
###########################################################################################

image heart_2:
        ycenter 100
        xcenter 100
        "emoticons/heart/1.png"
        alpha 0
        xzoom 0.3
        yzoom 0.3
        alpha 1.0
        easeout 0.4 xzoom 1.3 yzoom 1.2 alpha 0.6
        easein 0.3 xzoom 1.5 yzoom 1.4 alpha 0
        xzoom 0.4 yzoom 0.4
        alpha 1.0
        easeout 0.4 xzoom 1.4 yzoom 1.3 alpha 0