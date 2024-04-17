import os
import random

artist_list = [
    'ciloranko',
    'sho_(sho_lwlw)',
    'tianliang_duohe_fangdongye',
    'onineko',
    'rhasta',
    'suimya',
    'muririn',
    'ciloranko',
    'sho_(sho_lwlw)',
    'hoshi_(snacherubi)',
    'kase_daiki',
    'wlop',
    'eip_(pepai)',
    'rukako',
    'memmo',
    'memeno',
    'toosaka_asagi',
    'ask(askzy)'
    'kaede_(sayappa)',
    'jima',
    'sheya',
    'toosaka asagi'
]

def random_aritst():
    """随机画师串"""
    t_aritst_list = random.sample(artist_list, random.randint(5, 10))
    return "artist:" + ',artist:'.join(t_aritst_list)


def random_weight(artist: str):
    """给画师串增加随机的权重"""

    def add_brackets(word):
        num_brackets = random.randint(0, 4)
        t = random.randint(0, 1)
        if t == 1:
            num_brackets = int(num_brackets / 2)
        for _ in range(num_brackets):
            if t == 0:
                word = '[' + word + ']'
            else:
                word = '{' + word + '}'
        return word

    words = artist.split(',')
    words = [add_brackets(word) for word in words]
    return ','.join(words)

# def get_random_pic_prompt(prth: str):
#     def random_file(directory):
#         files = os.listdir(directory)
#         if not files:
#             print("文件夹为空。")
#             return None
#         return random.choice(files)
#
#     prompt = None
#     while not prompt:
#         selected_file = random_file(prth)
#         if
