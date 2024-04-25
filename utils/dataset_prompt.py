import random


def colors():
    color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "grey", "silver", "gold", "cyan",
             "black", "white", "blonde", ]
    random.shuffle(color)
    return color


pantyhose_list = ["white pantyhose", "black pantyhose", "striped pantyhose"]

hair = {f'{color} hair': 0 for color in colors()}
hair.update({f'light {color} hair': 0 for color in colors()})
hair_type = {key: 0 for key in
             ["long hair", "short hair", "very long hair", "short hair"]}
hair_type_2 = {key: 0 for key in
               ["double bun", "twintails", "curly hair", "straight hair", "ponytail", "single side bun",
                "side ponytail"]}
hair_type_3 = {key: 0 for key in
               ["bangs", "ahoge", "hair between eyes", "blunt bangs"]}
hair_append = {key: 0 for key in
               ["hair ornaments", "hair ribbon", "crescent hair ornaments", "hair flower", "hairband", "hair bow"]}
eyes = {f'{color} eyes': 0 for color in colors()}
expression = {key: 0 for key in [":)", ":d", ":b", ":(", ":3", ";)", "blush", "smile", ]}
clothes = {key: 0 for key in
           ["swimsuit", "dress", 'pajamas', 'hoodie', 'maid', 'school uniform', 'bikini', 'nude', 'wendding dress',
            'lolita dress', 'maid dress']}
foot = {key: 0 for key in pantyhose_list}
foot.update({f'{color},panties under pantyhose': 0 for color in pantyhose_list})
foot.update({f'{color},no panties': 0 for color in pantyhose_list})
background = {key: 0 for key in ["simple background", "white background", "floral background", "blurry background"]}

view_type = {key: 0 for key in
             ["close-up", "upper body", "full body"]}
view_location = {key: 0 for key in
             ["from above", "from below"]}


def find_min_value_key(data):
    key = min(data, key=data.get)
    data[key] = data.get(key) + 1
    return key


def get_prompt():
    prompt_list = []
    prompt_list.append(find_min_value_key(hair))
    if random.choice([True, False]):
        prompt_list.append(find_min_value_key(hair_type))
        prompt_list.append(find_min_value_key(hair_type_2))
        prompt_list.append(find_min_value_key(hair_type_3))
        prompt_list.append(find_min_value_key(hair_append))
    prompt_list.append(find_min_value_key(eyes))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(expression))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(clothes))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(foot))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(background))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(view_type))
    if random.choice([True, False]): prompt_list.append(find_min_value_key(view_location))
    return ','.join(prompt_list)
