import io
import json
import zipfile
import random
from datetime import datetime
import requests
from utils import flogger


class NovelAI:
    log = flogger.Flogger().get_logger(__name__)

    num_error = 0

    def __init__(self, output_folder='./output'):
        with open("./token.txt", "r") as file:
            self.token = file.read()
        self.output_folder = output_folder

    def _request_data(self, prompt: str, negative_prompt: str):
        url = "https://image.novelai.net/ai/generate-image"

        payload = json.dumps({
            "input": prompt,
            "model": "nai-diffusion-3",
            "action": "generate",
            "parameters": {
                "params_version": 1,
                "width": 832,
                "height": 1216,
                "scale": 5,
                "sampler": "k_euler",
                "steps": 28,
                "n_samples": 1,
                "ucPreset": 0,
                "qualityToggle": True,
                "sm": False,
                "sm_dyn": False,
                "dynamic_thresholding": False,
                "controlnet_strength": 1,
                "legacy": False,
                "add_original_image": True,
                "uncond_scale": 1,
                "cfg_rescale": 0,
                "noise_schedule": "native",
                "legacy_v3_extend": False,
                "seed": random.randint(0, 9999999999),
                "negative_prompt": negative_prompt,
                "reference_image_multiple": [],
                "reference_information_extracted_multiple": [],
                "reference_strength_multiple": []
            }
        })
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'authorization': f'Bearer {self.token}',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://novelai.net',
            'referer': 'https://novelai.net/',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            return response
        except Exception as e:
            print("请求失败")
            return None

    def _parse_data(self, response: requests.models.Response):
        if response == None or response.status_code != 200:
            raise Exception("请求失败")

        zip_data = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_data, 'r') as zip_file:
            file_list = zip_file.namelist()
            if file_list:
                image_data = zip_file.read(file_list[0])
                with open(rf'{self.output_folder}/{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.jpg', 'wb') as f:
                    f.write(image_data)
        print("图片保存成功")

    def generate(self, prompt: str, negative_prompt: str):
        try:
            response = self._request_data(prompt, negative_prompt)
            self._parse_data(response)
            self.num_error = 0
        except Exception as e:
            self.num_error += 1
            if self.num_error > 5:
                raise Exception("请求失败次数过多，为了保护账号，终止程序")

            print(f"第{self.num_error}次请求失败")
