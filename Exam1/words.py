def main():
    number_of_words = dict()
    with open("read_words") as f:
        data = f.readlines()
        str=""
        print("Number of words:", len(data))
        for i in data:
           str+=i
        for i in str:
            number_of_words[i]=str.count(i)
    print("Number of occurrences:",number_of_words)


if __name__ == "__main__":
    main()