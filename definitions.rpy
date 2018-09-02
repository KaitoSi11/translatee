###################################################################### ~ GUI
transform quickmenufade:

    on idle:
        ypos 1040
    on hover:
        ypos 1040
        easein 0.3 ypos 1035
    on selected_hover:
        ypos 1040

transform menutransition:
    on idle:
        xpos 0
    on hover:
        easein 0.3 xpos 10
    on selected_hover:
        xpos 10
    on selected_idle:
        xpos 10
transform navigationfade:
    on idle:
        xpos 0
    on hover:
        easein 0.3 xpos 10
    on selected:
        xpos 10
    on selected_hover:
        xpos 10
    on selected_idle:
        xpos 10

transform buttonfade:

    on idle:
        alpha 1.0
    on hover:
            linear 0.2 alpha 1.0


###################################################################### ~ Shake

#init:

init python:

    import math

    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)



transform shaketrain:
    ease 0.3 xoffset -.1 yoffset .3
    ease 0.35 xoffset .7 yoffset .6
    ease 0.3 xoffset -.2 yoffset .5
    ease 0.3 xoffset -.8 yoffset .7
    ease 0.3 xoffset 0 yoffset .8
    ease 0.35 xoffset .3 yoffset 1
    ease 0.3 xoffset .6 yoffset .4
    ease 0.35 xoffset .5 yoffset 1
    ease 0.3 xoffset -.3 yoffset 0
    ease 0.35 xoffset 0 yoffset 1.1
    ease 0.3 xoffset .7 yoffset .5
    ease 0.3 xoffset .55 yoffset 1.5
    ease 0.3 xoffset 0 yoffset 0
    repeat
