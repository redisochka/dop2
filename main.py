from pydub import AudioSegment
# Импортирует модуль pydub, который позволяет работать с аудиофайлами в Python.
wav_file = AudioSegment.from_wav("music.wav")
# Загружает аудиофайл в переменную wav_file из файла "music.wav" в формате wav.

def speed_change(sound, speed=1.0):
# Определяет функцию speed_change, которая принимает аудиофайл и коэффициент скорости в качестве аргументов, по умолчанию используется значение 1.0.
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    # Создает новый аудиофайл sound_with_altered_frame_rate, у которого изменена частота кадров.
    # Строка использует метод _spawn библиотеки pydub для создания нового аудиофайла на основе исходного. Значение overrides используется для изменения частоты кадров
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    # Возвращает новый аудиофайл со скорректированной частотой кадров, которая была установлена в предыдущей строке.
    # Метод set_frame_rate устанавливает исходную частоту кадров для нового аудиофайла.

print('Замедлить или Ускорить? \nКоэффициенты ускорения: (1.5; 2; 3 и тп ) \nКоэффициенты замедления:( 0.5; 0.7; 0.8 и тп )')

user_input = input('Введите коэффициент: ')

fast_sound = speed_change(wav_file, float(user_input))
#  Вызывает функцию speed_change с аргументами wav_file и user_input, и сохраняет результат в переменную fast_sound.
fast_sound.export("output.wav", format="wav")
#  Экспортирует новый аудиофайл