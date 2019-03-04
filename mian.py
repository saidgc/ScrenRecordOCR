import csv
import threading
import time

import pytesseract
from PIL import Image
from mss import mss


def capture_screenshot():
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')


def record(image, time):
    cp_image = image.crop(box=(2800, 350, 3100, 1690))
    y = 0
    for y in range(1340):
        r, g, b = cp_image.getpixel((150, y))
        if r > 100 and g > 100 and b > 100:
            break
    value_image = cp_image.crop(box=(95, y, 290, y + 60))
    text = pytesseract.image_to_string(value_image)
    row = [str(text), str(time.strftime('%Y,%m,%d,%H:%M:%S'))]
    print(text)
    with open('read1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()


if __name__ == "__main__":
    last_time = time.time()
    while 1:
        img = capture_screenshot()
        # print('took {} seconds'.format(time.time() - last_time))
        # last_time = time.time()
        asinc = threading.Thread(name='session', target=record, args=(img, time,))
        asinc.start()
