import os
import shutil

import openai as openai
import pysrt as pysrt


def transcribe_single_audio(api_key, audio_file, new_file_path):
    audio_file = open(audio_file, "rb")
    openai.api_key = api_key
    transcript = openai.Audio.translate("whisper-1", audio_file, response_format="srt", language="en")
    f = open(new_file_path, "a+", encoding="utf-8")
    f.write(transcript)
    print(new_file_path + " finish")
    f.close()

def transcribe_all_audio(api_key, dir_path):
    for root, dirs, files in os.walk(dir_path):
        i = 0
        for file in files:

            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            if file_name.endswith(".mp3"):
                i = i + 1
            if file_name.endswith(".mp3") and i > 303:
                # print(file_name)
                # exit()
                transcribe_single_audio(api_key, file_path, os.path.join(root, file_name + ".srt"))

def extract_all_srt_text(folder_path, new_file_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 遍历所有文件
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)
        file_name = os.path.basename(file_path)
        # 检查文件是否为srt文件
        if file.endswith(".srt"):
            text = extract_srt_text(file_path)
            f = open(new_file_path + "\\" + file_name.replace(".srt","") + ".txt", "a+", encoding="utf-8")
            f.write(text)
            f.flush()
            f.close()
def extract_srt_text(file_path):
    # 打开srt文件
    subs = pysrt.open(file_path)

    # 提取文本内容
    text = ""
    for sub in subs:
        text += sub.text_without_tags + "\n"

    return text.strip()


if __name__ == '__main__':
    proxy = "http://127.0.0.1:7890"
    os.environ["http_proxy"] = proxy
    os.environ["https_proxy"] = proxy
    api_key = "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"
    # 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
    dir_path = "C:\\Users\\guagu\\Desktop\\english_pod_audio\\"
    # transcribe_single_audio(api_key, "C:\\Users\\guagu\\Desktop\\english_pod_audio\\englishpod_0001pb.mp3", "C:\\Users\\guagu\\Desktop\\english_pod_audio\\englishpod_0001pb.srt")
    # transcribe_all_audio(api_key, dir_path)

    extract_all_srt_text("C:\\Users\\guagu\\Desktop\\english_pod_audio\\srt", "C:\\Users\\guagu\\Desktop\\english_pod_audio\\txt")
