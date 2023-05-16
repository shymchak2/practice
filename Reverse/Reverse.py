def main():
    while(1):
        filename=input("Enter filename: ")
        try:
            f = open(filename, "r")
            txt=f.read()
            reverse=''.join(reversed(txt))
            f.close()
            break
        except:
            print("Your file does not exist.")
    format=filename[filename.find('.'):]
    filename=filename[:filename.find('.')]+'-out'+format
    f=open(filename,"w")
    f.write(reverse)
    print("Result is saved in ",filename)
    f.close()

if __name__=="__main__":
    main()
