open("emails/Names.txt", "x").close()
open("emails/Message.txt", "x").close()

with open("emails/Names.txt", "w") as myfile:
    myfile.write("Sarah\nJim\nLogan\n")

with open("emails/Message.txt", "w") as myfile:
    myfile.write("Welcome to the party!\n")

with open("emails/Names.txt", "r") as mynames:
    with open("emails/Message.txt", "r") as mymessage:

        body = mymessage.read()
        for name in mynames:

            mail = F"Hello {name.strip()},\n\n  {body}"

            with open(F"emails/{name.strip()}.txt", "w") as myfile:
                myfile.write(mail)