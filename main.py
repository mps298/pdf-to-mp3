
from gtts import gTTS 
from art import tprint
import pdfplumber
import pathlib 
from pathlib import Path
import easygui

def pdf_to_mp3(file_path = 'the gift of the magi.pdf', language = 'en'):
    
    print(f'[+] Original file: {Path(file_path).name}')
    print('[+] Processiing...')
    
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        text = ''
        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as pdf:
            for page in pdf.pages:
                text += page.extract_text()

        #text = text.replace('\n', '  ')

        my_audio = gTTS(text= text, lang= language, slow= False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
      
        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'
    else:
        return "File doesn't exist, check the file"
    
def main():
    tprint('PDF_TO_MP3')
    
    file_path = ''
    language = ''
    
    try:
        while file_path == '':
            file_path = easygui.fileopenbox('Enter a PDF file:', '', '', '*.pdf', )     #input("Enter a PDF file's path:\n")
            if not (Path(file_path).is_file() and Path(file_path).suffix == '.pdf'):
                print(f"{file_path} isn't a correct PDF file's path, try again")
                file_path = ''
        
        while language == '':
            language = easygui.choicebox('Enter a PDF file:', 'Enter a PDF file', ['English', 'Russian']) #input ("Choose a language:\nEn for English\nRu for Russian:\n")
            if language == 'English':
                language = 'en'
            elif language == 'Russian':
                language = 'ru'
            else:
                print(f"{language} isn't a correct name of a language, try again")
                language = ''
    except:
        easygui.msgbox("Something went wrong")

    print(pdf_to_mp3(file_path, language))

if __name__ == '__main__':
    main()
