import json


tasks_data = {'tasks': []}
tasks_data['tasks'].append({
    1: 'COUCH POTATO refers to:\n\nA) A person who eats food while '
                                     'watching TV \nB) A lazy individual\nC) Old people\nD) Food left '
                                     'on a couch\n',
    2: 'What are PINK ELEPHANTS?\n\nA) Your closest friends\nB) Your '
                                     'enemies that lurk at every corner \nC) Hallucinations caused by '
                                     'drunkenness\nD) Dreams\n',
    3: 'What is a PIECE OF CAKE?\n\nA) Some easy task\nB) Participation in something\n'
                                     'C) Something complimental\nD) A helping of dessert\n',
    4: 'What does to HIT THE SACK mean?\n\nA) To prepare your backpack\nB) To get '
                                     'ready for a trip\nC) To boot a bag\nD) To go to bed\n',
    5: 'What does to LET THE CAT OUT OF THE BAG stand for?\n\nA) To lose your pet\nB) '
                                     'To leave the door opened\nC) To reveal a secret\nD) To turn your pockets '
                                     'inside out\n',
    6: 'What does to SIT ON THE FENCE mean?\n\nA) To lounge\nB) To be hesitant \nC) '
                                     'To watch the fight\nD) To risk\n',
    7: "Where is FROM HORSE'S MOUTH from?\n\nA) An authoritative source\nB) A liar "
                                     "or gossip\nC) Miles from nowhere\nD) A shady source\n",
    8: 'What does to PEPPER SOMEONE WITH SOMETHING mean?\n\nA) To improve \nB) To '
                                     'annoy\nC) To cause pain\nD) To attack\n',
    9: 'To CATCH WIND refers to: \n\nA) To tune up\nB) To hear about something\nC) '
                                     'To get ill\nD) To be swept off feet\n',
    10: 'What does to SPLIT HAIRS mean?\n\nA) To harm your health\nB) To annoy '
                                      'someone\nC) To argue about very small details \nD) To devide\n',
    11: 'What does to FACE MUSIC mean?\n\nA) To enroll in a conservatory\nB) To accept results of your actions\n'
          'C) To hide from reality\nD) To listen to the loud music\n',
    12: 'What is a SLIP OF THE TONGUE?\n\nA) A lick\nB) A deliberate insult\nC) A speaking mistake\n'
          'D) An imitation of a sound\n',
    13: 'The idiom LOOSE LIPS SINK SHIPS means you should not:\n\nA) Talk carelessly\nB) Eat a lot\n'
          'C) Yawn loudly\nD) Lie\n',
    14: 'What does to SCRATCH AN ITCH mean?\n\nA) To satisfy a desire\nB) To exhaust yourself\n'
          'C) To forget a bad memory\nD) To annoy someone\n',
    15: 'What does to SHOOT FROM THE HIP mean?\n\nA) To surprise someone\nB) To tell a joke\n'
          'C) To run very fast\nD) To speak directly\n',
    16: 'BY HOOK OR BY CROOK means you do it:\n\nA) Bravely\nB) Any way possible\nC) Without any meaning\n'
          'D) Using no permission\n',
    17: 'NO BRAINER refers to:\n\nA) A silly individual\nB) An action  without thinking\nC) A very easy choice\n'
          'D) An animal without grey matter\n',
    18: 'If someone FREAKS OUT he:\n\nA) Shows off\nB) Gets angry\nC) Gets upset\nD) Overuses makeup\n',
    19: 'If you STICK TO YOUR GUNS, you:\n\nA) Refuse to change your mind\nB) Accept no help\nC) Deny obvious truth\n'
          'D) Start improving\n',
    20: 'What does a RAT RACE mean?\n\nA) Hustle and bustle\nB) Struggle for success\n'
         'C) Something you do in a little time\nD) A pointless competition\n'
})


with open(r'C:\Texts\tasks.txt', 'w') as outfile:
    json.dump(tasks_data, outfile, indent=4)

