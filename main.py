import time
from utils.noval_ai import NovelAI
from utils import tools
from utils import prompt_tools


def get_prompt():
    artist = prompt_tools.random_aritst() # 随机画师
    artist = prompt_tools.random_weight(artist) # 给画师加上权重
    t_prompt = ',1girl'
    prompt = artist + ",year 2023" + t_prompt
    return prompt


negative_prompt = 'nsfw, lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], nsfw, lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract],{{weibo_username}},female_pubic_hair,{{weibo_logo}},low quality,@_@,chibi'

prompt = ""

novel_ai = NovelAI(output_folder='./output/画风测试')
for i in range(1000):  # 执行次数
    if i % 3 == 0: # 指定张数后切画风
        prompt = get_prompt()

    novel_ai.generate(prompt, negative_prompt)

    if i % 10 == 0 and i != 0:
        tools.random_sleep(30, 35)
    else:
        tools.random_sleep(5, 8)
