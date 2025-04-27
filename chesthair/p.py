from PIL import Image
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# اسم المجلد اللي فيه الصور
input_folder = "."

# إنشاء مجلد للإخراج (اختياري)
output_folder = "converted_pngs"
os.makedirs(output_folder, exist_ok=True)

# فلترة كل الملفات بصيغة .webp
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        webp_path = os.path.join(input_folder, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(output_folder, png_filename)

        try:
            with Image.open(webp_path) as img:
                img.save(png_path, "PNG")
            print(f"✅ تم التحويل: {filename} -> {png_filename}")
        except Exception as e:
            print(f"❌ فشل التحويل: {filename}, السبب: {e}")
