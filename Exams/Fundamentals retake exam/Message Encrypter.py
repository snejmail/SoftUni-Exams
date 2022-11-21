import re
n = int(input())
for _ in range(n):
    message = input()
    pattern = r"(\*|@)([A-Z][a-z]{2,})\1(: )(\[[A-Za-z]\]\|\[[A-Za-z]\]\|\[[A-Za-z]\]\|)$"
    result = re.search(pattern, message)

    if not result:
        print("Valid message not found!")
    else:
        tag = result.group(2)
        valid_message = result.group(4)
        numbers = ""

        for symbol in valid_message:
            if symbol.isalpha():
                symbol = ord(symbol)
                numbers += " " + str(symbol)

        print(f"{tag}:{numbers}")

