import os
import requests

def download_file(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 发送 GET 请求
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 检查请求是否成功

    # 将内容写入文件
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def handler(event, context):
    try:
        region = os.getenv("FC_REGION")
        root = os.getenv("NAS_ROOT")
        download_file("https://dipper-cache-%s.oss-%s-internal.aliyuncs.com/huggingface/city96/FLUX.1-dev-gguf/flux1-dev-Q8_0.gguf" % (region, region), "%s/models/unet/flux1-dev-Q8_0.gguf" % root)
    except Exception as e:
        print(e)
        raise e
        
    return 'initial done'