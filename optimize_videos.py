import os
import subprocess

# Папка с видео
input_folder = "video"       # измени на свою
output_folder = "web_video"   # сюда будут сохраняться оптимизированные

# Создаем папку если нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходим по всем файлам
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".webm")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp4")

        # Команда ffmpeg для оптимизации
        command = [
            "ffmpeg",
            "-i", input_path,
            "-vcodec", "libx264",    # современный кодек h264
            "-crf", "28",            # качество (меньше число = лучше качество, больше = меньше размер)
            "-preset", "slow",       # баланс скорости/сжатия
            "-acodec", "aac",        # сжатие аудио
            "-b:a", "128k",
            output_path
        ]

        print(f"🎬 Оптимизация: {filename}")
        subprocess.run(command)

print("✅ Все видео оптимизированы!")
