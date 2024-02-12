from photomanager import photoManager
from photoplugins.step1 import step1
from photoplugins.flash import flash
from photoplugins.end import laststep



if __name__ == "__main__":
    print("Starting FIU photobooth")
    p = photoManager()
    s1 = step1()
    s2 = flash()
    s3 = laststep()
    p.register(s1)
    p.register(s2)
    p.register(s3)
    while True:
        p.run()
