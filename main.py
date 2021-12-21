from PIL import Image
import cv2
import re 
import pytesseract
import pyautogui
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import time
import random

import winsound
frequency = 1000  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second



# # Screenshot de la base entera
# myScreenshot = pyautogui.screenshot()
# myScreenshot.save(r'D:\Proyects\cocAutoFind\images\base.png')

# # Cut
# image = Image.open('images/base.png')
# image_gold = image.crop((144,157,286,191))
# image_gold.save('images/gold.png')


# # Apply open cv
# image = cv2.imread("images/gold.png")
# imageWithFilter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply pytesseract
# gold = pytesseract.image_to_string(imageWithFilter)
# print(gold)

while True:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'D:\Proyects\cocAutoFind\images\base.png')
    image = Image.open('images/base.png')
    image_gold = image.crop((144,157,286,191))
    image_gold.save('images/gold.png')
    image = cv2.imread("images/gold.png")
    imageWithFilter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gold = pytesseract.image_to_string(imageWithFilter, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    list_of_numbers = re.findall(r'\d+', gold)
    result_number = ''.join(list_of_numbers)
    print("Oro encontrado: ", result_number)
    
    if result_number != '':
        if (int(result_number) < 300000):
            print("Oro insuficiente, siguiente base")
            x = random.randint(1560,1800)
            y = random.randint(700,800)
            pyautogui.click(x, y)
            time.sleep(random.randrange(5,8))
        else:
            print("oro suficiente")
            winsound.Beep(frequency, duration)
    else:
        print("error tesseract")

    




# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')