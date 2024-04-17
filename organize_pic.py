from PIL import Image
import os
import shutil
from tqdm import tqdm


def read_image_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            try:
                # 获取图像的元数据
                metadata = img.info
                return metadata
            except Exception as e:
                return None
    except:
        return None


def move_files_based_on_content(src_folder, dest_folder1, keywords):
    for root, dirs, files in os.walk(src_folder):
        for file in tqdm(files, desc="Processing"):
            if (
                    file.endswith(".jpg")
                    or file.endswith(".JPG")
                    or file.endswith(".png")
                    or file.endswith(".PNG")
            ):
                # 移动原图
                file_path = os.path.join(root, file)
                content = read_image_metadata(file_path)
                if content is not None and any(
                        keyword in content for keyword in keywords
                ):
                    if os.path.exists(f"{dest_folder1}\\{file}"):
                        os.remove(file_path)
                    else:
                        shutil.move(file_path, dest_folder1)


src_folder = r"D:\OneDrive\AI Paint\筛选原图"
dest_folder1 = r"D:\OneDrive\AI Paint\原图nai3"
keywords = ["Description", "parameters"]
# keywords = ["Description"]
# keywords = ["parameters"]

move_files_based_on_content(src_folder, dest_folder1, keywords)
