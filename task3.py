good = r'''
"Demon in overalls"
    ,-----.
   ( <> <> )
    )_ W _(
     |||||    A A A
      |||     | | |
   __/)'(\__  `-+-'
  /\\     //\   |
 | |\\___//\ \  |
 | |/\\_//\ \ \ |
 | ||\\_//|  \ \|
 | ||/\_/\|   \ |
 | |/ /|\ \    \_)
 (_/  \_/  \    K
   |  | |  |    R
   |  | |  |    O
   |()| |()|    G
   |  | |  |    G
   |  | |  |    9
   |__| |__|    8
   \__/ \__/    V
'''
bad = r'''
(                      )
| \    _, --------._ / |
| `., '            `. /  |
`  '              ,-'   '
\ / _
_( /
(, -.`., ',-.`. `__,'
 | /  # \ ),-','#\`= ,'.` |
 `._ /) - '.\_,'   ) )) |
/ (_.)\   .   -'//
    ( /\____/\    ) )`'\
      \ |V----V|  ' , \
                      |`- -- -'   ,'   \  \      _____
___    |         .'    \ \  `._,-'     `-
` .__, ` ---^---'       \ ` -'
      -.______  \ . /  _ _____ ,-
`.     ,'            ap
Krogg
'''
guard_awake = False

if not guard_awake:
    outcome = "Shadow: You slip past unnoticed."
    print(good)
else:
    outcome = "Doom: The guard raises the alarm."
    print(bad)
print(outcome)

