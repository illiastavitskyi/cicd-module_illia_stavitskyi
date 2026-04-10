


def read_file(filename: str) -> str:
    file = open(filename)
    text = file.read()
    file.close()
    
    return text

def input_keyword(keyword: str) -> str:
    user_input = keyword 
    return keyword


def filter_text(text: str, keyword: str) -> str:
    parsed_text = ""
    for line in text.splitlines():
        if keyword in line:
            parsed_text += line + "\n"
    
    return parsed_text



def main():
   # print("hi")
    text = read_file('test.txt')
   # print(text)
    user_keyword =  input_keyword("ab")
   # print(user_keyword)

    parsed_text = filter_text(text, user_keyword)
    print(parsed_text)

    



if __name__ =="__main__":
    main()