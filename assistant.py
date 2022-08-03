# что будет включать голосовой ассистент
# обработка речи
# голосовой движок
# а что он будет делать?
import speech_recognition as sr
import subprocess, sys


name = 'василиса'


rec = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Говори')
        rec.adjust_for_ambient_noise(source)
        data = rec.record(source, duration=3)
        #text = rec.recognize_google(data, show_all=True, language='ru')
        text = rec.recognize_google(data, language='ru').lower()

        if name in text:
            print('Я тебя слышу')
            try:
                data = rec.record(source, duration=10)
                text = rec.recognize_google(data, language='ru').lower()
                if '=' in text:
                    print(eval(text[:-1]))
                elif 'привет' in text:
                    print('Здравствуйте')
                elif 'пуск' in text:
                    print('...запуск файла')
                    subprocess.Popen(['start', '/home/denis/1.odt'], shell = True)
                else:
                    print('Я тебя не понимаю!')
            except:
                print('Ошибка')

