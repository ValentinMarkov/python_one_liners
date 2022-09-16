# Filtering out words that don’t contribute a lot of meaning is common practice when
# implementing search engines. A simple heuristic is to filter out all words with three characters or less.

text = "Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, " \
       "and nothing particular to interest me on shore, I thought I would sail about a little and see the watery" \
       " part of the world. It is a way I have of driving off the spleen, and regulating the circulation. - Moby Dick"

lst_bigger_than_3 = [word for line in text.split('\\') for word in line.split() if len(word) > 3]
lst_bigger_than_3_1 = [[word for word in line.split() if len(word) > 3] for line in text.split('\\')]


print(lst_bigger_than_3)
print(lst_bigger_than_3_1)