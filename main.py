import time
from utils.noval_ai import NovelAI

from utils import tools

prompt = '1girl'
negative_prompt = '"nsfw, lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], nsfw, lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], nsfw, lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract], lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract],{{weibo_username}},female_pubic_hair,{{weibo_logo}},low quality,@_@,chibi"'

novel_ai = NovelAI()
for i in range(1000):  # 执行次数
    novel_ai.generate(prompt, negative_prompt)

    if i % 10 == 0 and i != 0:
        tools.random_sleep(30, 35)
    else:
        tools.random_sleep(5, 8)
