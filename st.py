# Initiating packages
import os
try:
    from gtts import gTTS
    from playsound import playsound
except:
    print('Installing the required packages...')
    try:
        os.system('pip install gtts')
        os.system('pip install playsound==1.2.2')
    except:
        print('Check the internet connection.')
    finally:
        print('Run the program again.')
        safe_exit()
#--------------------


# Reader and checker functions
def read_word(text):
    # Generate, save, and play audio file
    if os.path.isfile(audio_name):
        os.remove(audio_name)

    try:
        audio_file = gTTS(text=text, lang=language, slow=False)
        audio_file.save(audio_name)
        if not os.stat('./' + audio_name).st_size > 0:
            raise Exception
    except:
        print('Check the internet connection.')
        print('Run the program again.')
        safe_exit()
        
    playsound(audio_name)


def check_word(text, correct_text):
    # Check whether the answer is right
    return True if text == correct_text else False


def overwrite_new_words(text):
    # Overwrite wrong words in 
    new_words_file = open(words_name, 'w')
    new_words_file.write(text)
    new_words_file.close()


def load_settings():
    
    settings_dict = {}
    with open(settings_name) as settings_file:
        settings_lines = settings_file.read().split('\n')
    for line in settings_lines:
        if 'repeat_wrong=' in line:
            settings_dict['repeat_wrong'] = \
            True if line[len('repeat_wrong='):] == '1' else False
    
    return settings_dict
            


def safe_exit():
    if os.path.isfile(audio_name):
        os.remove(audio_name)
    input('Press Enter to exit...')
    exit()
#--------------------


words_name = 'st.txt'
language = 'en'
audio_name = 'st.mp3'
settings_name = 'settings.txt'
count_corr = 0
count_wrong = 0
wrong_words = ''

words_file_banner = '\
---------------------------------\n\
        Spelling Trainer         \n\
---------------------------------\n\
Powered by Google Text to Speech.\n\
---------------------------------\n\
1. Write the words/expressions in\n\
   a file. Write each item in one\n\
   row.                          \n\
2. Save the file as "st.txt".    \n\
3. Put the file next to the app. \n\
4. Run the app again.            \n\
---------------------------------'

intro_guide_banner = '\
---------------------------------\n\
         Spelling Trainer        \n\
---------------------------------\n\
Powered by Google Text to Speech.\n\
---------------------------------\n\
Write the word you hear, then    \n\
press Enter.                     \n\
* The app needs internet connec- \n\
  tion.                          \n\
* Capitalization is not checked. \n\
---------------------------------'


# Loading words list and cleaning
try:
    with open(words_name) as words_file:
        words_lst = words_file.read().split('\n')
except FileNotFoundError:
    print(words_file_banner)
    safe_exit()

words_lst = list(map(lambda s: s.strip(), words_lst))
words_lst = [item for item in words_lst if item]
#--------------------


# Loading settings
settings = load_settings()
#--------------------

print(intro_guide_banner)

for word in words_lst:
    read_word(word)
    user_input = input().lower()
    if check_word(user_input, word):
        count_corr += 1
    else:
        print('Correct answer:', word)
        if settings['repeat_wrong']:
            words_lst.append(word)
        wrong_words += word + '\n'
        count_wrong += 1
    print('---------------------------------')

print('Correct:', count_corr, 'Wrong:', count_wrong)
print('---------------------------------')

new_words_bool = True if input('Do you want to keep \
only the mistakes? [Y/n]: ').lower() == 'y' else False
if new_words_bool:
    overwrite_new_words(wrong_words)

safe_exit()

