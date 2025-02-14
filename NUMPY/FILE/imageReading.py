with open('aniket.jpg','rb')as fp:
    with open("A.jpg",'wb')as f:
        imgdata=fp.read()
        f.write(imgdata)
        print("Your operatin successfully Perform")
