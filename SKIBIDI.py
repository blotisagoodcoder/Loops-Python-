class StringReverse:
    def __init__(self, text):
        self.__text = text

    def reverse_words(self):
        words = self.__text.split()
        reversed_list = words[::-1]
        return " ".join(reversed_list)

if __name__ == "__main__":
    input_string = "BUILDING A OFF FALL"
    reverser = StringReverse(input_string)
    result = reverser.reverse_words()
    
    print(f"Original: {input_string}")
    print(f"Reversed: {result}")