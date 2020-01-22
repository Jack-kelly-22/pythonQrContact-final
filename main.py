from csv2vcard import csv2vcard
import qrcode


def main():
    print("welcome to the Contact info Qr encoder:")
    print("directions:")
    print("\t", "enter the prompts and an image called yourContactQR.png will be generated containing your contact info")
    print()
    print()

    firstName1= input("First name:")
    MiddleInitial1=input("middle Initial: ")
    lastName1=input("last Name:")
    title1=input("title: ")
    email1=input("email: ")
    url1= input("url: ")
    phone1= input("phone number: ")


    #print(csv2vcard.test_csv2vcard())
    st = csv2vcard.test_csv2vcard(lastName=lastName1,firstName=firstName1,title=title1,phone=phone1,email=email1,website=url1)
    #print(st["output"])
    #print("dddddd" + st.__str__())

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    #qr.add_data(st["output"])
    qr.add_data(st["output"])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")


    #print(img.type)
    img.save("yourContactQR.png")

if __name__ == "__main__":
    main()



