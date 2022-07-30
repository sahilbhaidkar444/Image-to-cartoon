from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import cv2

myfont=('inter',12)

def convert():
    location = filedialog.askopenfilename()
    print(location)
    img = cv2.imread(location)
    Gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    Blur_image = cv2.GaussianBlur(Gray_image, (3, 3), 0)
    detect_edge = cv2.adaptiveThreshold(Blur_image, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    # cartoonize :
    output = cv2.bitwise_and(img, img, mask=detect_edge)

    #cv2.imshow("Original picture", img)
    cv2.imshow("Cartoon Effect", output)
    cv2.waitKey(0)

    # save image :
    cv2.imwrite("converted.jpg",output)
    l1 =Label(w,text='Image Saved',width=50,height=2,bg = "#FFFDF9",fg='#121212',font = myfont).pack()


w = Tk()
w.resizable(False, False)
w.geometry('350x500')
photo = PhotoImage(file = "layers.png")
w.iconphoto(False, photo)
w.configure(bg = '#FFFDF9')
w.title('Image to cartoon')
l =Label(w,text='Choose an image',width=50,height=2,bg = "#FFFDF9",fg='#121212',font = myfont).pack()
b =Button(w,text='O P E N  F I L E  A N D  C O N V E R T',width=50,height=2,bg='#ffcc66',fg ='white',command=convert).pack()

w.mainloop()
