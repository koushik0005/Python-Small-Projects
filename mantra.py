import time
import pyautogui
count = 5
print('T minus')
for i in range(5):
    print(count)
    time.sleep(1)
    count = count - 1

for i in range(100):
    pyautogui.typewrite('chu mantar chu, kala kutter ghu')
    pyautogui.press('enter')
    time.sleep(0.3)