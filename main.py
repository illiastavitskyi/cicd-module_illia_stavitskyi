


def read_file(filename: str) -> str:
    file = open(filename)
    text = file.read()
    file.close()
    print(text)
    return text



def main():
    print("hi")
    text = read_file('test.txt')
    print(text)

    



if __name__ =="__main__":
    main()