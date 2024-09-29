#!/bin/bash
#

melt -progress2 -abort xml:lower-thirds.mlt -verbose -consumer avformat:lower-thirds.webm an=1 rc_lookahead=16 quality=good speed=3 vprofile=0 qmax=51 qmin=4 slices=4 tile-columns=6 frame-parallel=1 lag-in-frames=25 row-mt=1 auto-alt-ref=0 mlt_image_format=rgba pix_fmt=yuva420p
