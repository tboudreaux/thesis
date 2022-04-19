#!/bin/bash
text=${1?Text Goes Here}
angle=45 # in degrees counterclockwise from horizontal
grey=0.75 # 0 is black 1 is white

ps2pdf - - <<!
%!PS
/cm { 28.4 mul } bind def
/draft-Bigfont /Helvetica-Bold findfont 72 scalefont def
/draft-copy { 
        gsave initgraphics $grey setgray 
        5 cm 10 cm moveto  
        $angle rotate 
        draft-Bigfont setfont
        ($text) show grestore
 } def
draft-copy showpage
!
# FROM https://unix.stackexchange.com/questions/295514/pdf-stamp-with-angle-using-cli
