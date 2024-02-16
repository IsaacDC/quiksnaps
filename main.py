from photomanager import photoManager
from photoplugins.step1 import step1
from photoplugins.flash import flash
from photoplugins.end import laststep
from photoplugins.preview import previewCamera
from photoplugins.email import emailPicture



if __name__ == "__main__":
    print("Starting FIU photobooth")
    p = photoManager()
    s1 = step1()
    s2 = previewCamera()
    s3 = flash()
    s4 = laststep()
    email = emailPicture()
    p.register(s1)
    p.register(s2)
    p.register(s3)
    p.register(email)
    p.register(s4)

    while True:
        p.run()
