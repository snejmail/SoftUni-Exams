def words_sorting(*args):
    words_dict = {}
    total_ascii_sum = 0

    for word in args:
        ascii_sum = sum(ord(symbol) for symbol in word)
        total_ascii_sum += ascii_sum
        words_dict[word] = ascii_sum

    if total_ascii_sum % 2 != 0:
        sorted_words_dict = sorted(words_dict.items(), key=lambda kvtp: -kvtp[1])
    else:
        sorted_words_dict = sorted(words_dict.items(), key=lambda kvtp: kvtp[0])

    result = ""
    for key, value in sorted_words_dict:
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))
#
