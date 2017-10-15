import os
import time

width =79

text = raw_input("Enter the text: ").upper()

printedtext = [ "","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "A" : [ "  *  ",
                       " * * ",
                       "*   *",
                       "*****",
                       "*   *" ],

               "B" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*   *",
                       "**** " ],

               "C" : [ " ****",
                       "*    ",
                       "*    ",
                       "*    ",
                       " ****" ],

               "D" : [ "**** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "**** " ],

               "E" : [ "*****",
                       "*    ",
                       "*****",
                       "*    ",
                       "*****" ],

               "F" : [ "*****",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    " ],

               "G" : [ " ****",
                       "*    ",
                       "* ***",
                       "*   *",
                       " ****" ],

               "H" : [ "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *" ],

               "I" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "*****" ],

               "J" : [ "*****",
                       "   * ",
                       "   * ",
                       "*  * ",
                       "**** " ],

               "K" : [ "*   *",
                       "*  * ",
                       "***  ",
                       "*  * ",
                       "*   *"  ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "M" : [ "*   *",
                       "** **",
                       "* * *",
                       "*   *",
                       "*   *" ],

               "N" : [ "*   *",
                       "**  *",
                       "* * *",
                       "*  **",
                       "*   *" ],

               "O" : [ " *** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],

               "P" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*    ",
                       "*    " ],

               "Q" : [ " *** ",
                       "**  *",
                       "* * *",
                       " *** ",
                       "   * " ],

               "R" : [ "**** ",
                       "*   *",
                       "**** ",
                       "*  * ",
                       "*   *"  ],

               "S" : [ " ****",
                       "*    ",
                       " *** ",
                       "    *",
                       "**** " ],

               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "U" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],

               "V" : [ "*   *",
                       "*   *",
                       "*   *",
                       " * * ",
                       "  *  " ],

               "W" : [ "*   *",
                       "*   *",
                       "* * *",
                       "** **",
                       "*   *" ],

               "X" : [ "*   *",
                       " * * ",
                       "  *  ",
                       " * * ",
                       "*   *" ],

               "Y" : [ "*   *",
                       "*   *",
                       " * * ",
                       "  *  ",
                       "  *  " ],

               "Z" : [ "*****",
                       "   * ",
                       "  *  ",
                       " *   ",
                       "*****" ]

               }


for row in range(5):
    for char in text:
        printedtext[row] += (str(characters[char][row]) + "  ")

offset = width
while True:
    os.system("cls")
    for row in range(5):
        print(" " * offset + printedtext[row][max(0,offset*-1):width - offset])
    offset -=1

    if offset <= ((len(text)+2)*6) * -1:
        offset = width
    time.sleep(0.1)
