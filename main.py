


def read_file(filename: str) -> str:
    file = open(filename)
    text = file.read()
    file.close()
    print(text)
    return text

def input_keyword(keyword: str) -> str:
    user_input = keyword 
    return keyword



def main():
    print("hi")
    text = read_file('test.txt')
    print(text)
    user_keyword =  input_keyword("fsjdfsj")
    print(user_keyword)

    



if __name__ =="__main__":
    main()