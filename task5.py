good = r'''

                     _ /\.'|_
                 _.-| |\ | / |_
                / \ _>-"""-._.'|_
               >`-.'         `./ \
              /`./             \-<
              `-|               |_/
              /_|               |_\
              ) |               | |
              -<|               |\/
              `'_\             /`<
               |_/`.         .'\_/
                \_/ >-.._..-'\_|
                  `-`_| \_\|_/
                   |   `' |  |
                   |      |  |
                   |      |  |
                   |      |  |
                   |      |  |
                   |  /\  |  |
                   | /| \ |\ |
                   |/ |/ \| \|

VK
'''
bad = r'''
  __
 /    \
| STOP |
 \ __ /
   ||
   ||
   ||
   ||
   ||
 ~~~~~~~
unknown
'''
escaped = True

if escaped:
    outcome = "Legend: Your tale will be told for generations."
    print(good)
else:
    outcome = "Doom: The dugeon claims another soul"
    print(bad)
print(outcome)