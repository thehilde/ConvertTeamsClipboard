import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import Image
import base64
#import pyperclip as pc  # temp = pc.paste()

def GetText():
    # get the clipboard text
    clip.OpenClipboard()
    data = clip.GetClipboardData()
    clip.CloseClipboard()
    return data

def SendPilImageToClipboard(img):                
    output = BytesIO()
    img.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_DIB, data)
    clip.CloseClipboard()


if __name__ == '__main__':
    print("Convert Clipboard MS Teams BASE64 Picture to Clipboard Bitmap!")
    temp = GetText()
    #temp = pc.paste()
    if (type(temp) == str) and (';base64' in temp):
        print(type(temp))
        temp = temp.split(',')[1].split('"')[0]
        #print(temp)
        data = BytesIO(base64.b64decode(temp))
        #print(data)
        img = Image.open(data)
        SendPilImageToClipboard(img)
