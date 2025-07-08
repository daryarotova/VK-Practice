import whisper
import os


model = whisper.load_model("large")

audio_folder = "audio"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

for audio_file in os.listdir(audio_folder):
    if audio_file.endswith(('.mp3', '.wav', '.mp4')):
        audio_path = os.path.join(audio_folder, audio_file)
        print(f"Обрабатывается файл: {audio_file}")

        result = model.transcribe(audio_path, language="ru")

        output_file = os.path.splitext(audio_file)[0] + ".txt"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Транскрипт сохранен в: {output_path}")

print("Транскрипция успешно проведена.")
