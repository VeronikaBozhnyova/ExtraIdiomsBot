import json


correct_answers_data = {'correctanswers': []}
correct_answers_data['correctanswers'].append({
    0: 'The correct answers are:\n',
    1: 'B)',
    2: 'C)',
    3: 'A)',
    4: 'D)',
    5: 'C)',
    6: 'B)',
    7: 'A)',
    8: 'D)',
    9: 'B)',
    10: 'C)',
    11: 'B)',
    12: 'C)',
    13: 'A)',
    14: 'A)',
    15: 'D)',
    16: 'B)',
    17: 'C)',
    18: 'B)',
    19: 'A)',
    20: 'B)'
})


with open(r'C:\Texts\correctanswers.txt', 'w') as outfile:
    json.dump(correct_answers_data, outfile, indent=4)