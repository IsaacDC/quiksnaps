from photomanager import photoManager
from photoplugins.step1 import step1
from photoplugins.step2 import step2


if __name__ == "__main__":
    print("Starting FIU photobooth")
    p = photoManager()
    s1 = step1()
    s2 = step2()
    p.register(s1)
    p.register(s2)
    while True:
        p.run()
