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
        input()
        exit()
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


def safe_exit():
    if os.path.isfile(audio_name):
        os.remove(audio_name)
    input()
    exit()
#--------------------

words_name = 'st.txt'
language = 'en'
audio_name = 'st.mp3'
count_corr = 0
count_wrong = 0

words_file_banner = '\
Write the words and expressions in a file called "st.txt". Write each item in one row. Save the file next to the program and run the program again.'

intro_guide_banner = '\
---------------------------------\n\
Powered by Google Text to Speech.\n\
---------------------------------\n\
Write the word you hear, then press \
Enter. Capitalization is not checked.\n\
---------------------------------'

# Loading words list and cleaning
try:
    with open(words_name) as words_file:
        words_lst = words_file.read().split('\n')
except FileNotFoundError:
    print(words_file_banner)
    input()
    exit()

words_lst = list(map(lambda s: s.strip(), words_lst))
words_lst = [item for item in words_lst if item]
#--------------------

print(intro_guide_banner)

for word in words_lst:
    read_word(word)
    user_input = input().lower()
    if check_word(user_input, word):
        count_corr += 1
    else:
        print('Correct answer:', word)
        count_wrong += 1
    print('---------------------------------')

print('Correct:', count_corr, 'Wrong:', count_wrong)
safe_exit()

