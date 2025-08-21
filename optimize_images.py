from PIL import Image
import os

# Папка, где лежат твои картинки
input_folder = "images"      # измени на свою
output_folder = "web_images"  # сюда будут сохраняться оптимизированные

# Создаем папку, если нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходим по всем файлам
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        filepath = os.path.join(input_folder, filename)
        img = Image.open(filepath)

        # Сжимаем и уменьшаем до макс ширины 1200px (если больше)
        max_width = 1200
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        # Сохраняем в новом виде (качество 80%)
        output_path = os.path.join(output_folder, filename)
        img.save(output_path, optimize=True, quality=80)

        print(f"✅ Оптимизировано: {filename}")

print("🎉 Все изображения обработаны!")
