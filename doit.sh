#!/bin/bash
#

#/Applications/Shotcut.app/Contents/MacOS/melt -verbose -progress2 -abort xml:lower-thirds.mlt
#/Applications/Shotcut.app/Contents/MacOS/melt xml:lower-thirds.mlt -consumer avformat:output.mp4
#/Applications/Shotcut.app/Contents/MacOS/melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=qtrle pix_fmt=argb an=1
#/Applications/Shotcut.app/Contents/MacOS/melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=qtrle pix_fmt=argb an=1
melt -progress2 -abort xml:lower-thirds.mlt -consumer avformat:output.mov vcodec=qtrle pix_fmt=argb an=1

