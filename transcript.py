import whisper
import os


def main():
    try:
        print("Модель Whisper загружается")
        model = whisper.load_model("large")
        print("Модель успешно загружена")
    except Exception as e:
        print(f"Ошибка загрузки модели: {e}")
        return

    audio_folder = "audio"
    output_folder = "output"

    if not os.path.exists(audio_folder):
        print(f"Ошибка: папка с аудиофайлами '{audio_folder}' не найдена")
        return

    os.makedirs(output_folder, exist_ok=True)

    processed_files = 0
    for audio_file in os.listdir(audio_folder):
        if audio_file.lower().endswith(('.mp3', '.wav', '.mp4')):
            try:
                audio_path = os.path.join(audio_folder, audio_file)
                print(f"\nОбрабатывается файл: {audio_file}")

                result = model.transcribe(audio_path, language="ru", beam_size=5)

                output_file = os.path.splitext(audio_file)[0] + ".txt"
                output_path = os.path.join(output_folder, output_file)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result["text"])

                print(f"Результат транскрипции сохранен в: {output_path}")
                processed_files += 1

            except Exception as e:
                print(f"Ошибка обработки файла {audio_file}: {e}")

    if processed_files > 0:
        print(f"\nТранскрипция успешно завершена. Обработано файлов: {processed_files}")
    else:
        print("\nАудиофайлы не найдены")

if __name__ == "__main__":
    main()
