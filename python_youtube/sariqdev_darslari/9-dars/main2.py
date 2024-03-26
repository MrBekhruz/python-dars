import threading
import time

def t_yillar(data):  
    t_yil = int(input('Assalom alaykum iltimos tug\'ilgan yilingizni kiriting: '))
    print(str(2024-t_yil) + ' '+ "siz shu yoshda ekansiz")
    print("yuklanmoqda..."  , data)

def register(data):
    name = input("Ismingiz nima? \n>>>: " )
    print("Assalom alaykum " + name.title())
    time.sleep(3)
    print("yuklanmoqda ...",data)

def shutdown():
    print("dastur tuxtatildi")


def main():
    tugilgan_yil_thread = threading.Thread(target=t_yillar, args=("tekis yul",))
    register_thread = threading.Thread(target=register, args=("save",))

    tugilgan_yil_thread.start()
    register_thread.start()

    tugilgan_yil_thread.join()
    register_thread.join()

    shutdown()
    print("Malumotlar saqlandi")
    
if __name__ == "__main__":
    main()

 