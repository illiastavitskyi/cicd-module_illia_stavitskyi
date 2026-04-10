def read_file(filename: str) -> str:
    file = open(filename)
    text = file.read()
    file.close()
    return text


def input_keyword(keyword: str) -> str:
    return keyword


def filter_text(text: str, keyword: str) -> str:
    parsed_text = ""
    for line in text.splitlines():
        if keyword in line.split():
            parsed_text += line + "\n"
    return parsed_text


def save_text(text: str, filename: str):
    with open(filename, 'w') as file:
        file.write(text)


def main():
    text = read_file('test.txt')
    user_keyword = input_keyword("ab")
    parsed_text = filter_text(text, user_keyword)
    print(parsed_text)
    save_text(parsed_text, 'filtered.txt')


if __name__ == "__main__":
    main()
