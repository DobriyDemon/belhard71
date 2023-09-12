# text = "python" #string
# text = r"python/" #raw string? without escape commands for strings
# print(text[1:6:2]) #start, stop, step

# print(text + " " + text) #concatenate
# print(text * 3) #replication, if 0 then empty string

text = "python is more awesome than java"
a = text.split(sep=" ", maxsplit=2) #split by space and maxsplit 2 times, also have a right split(rsplit)

# LISTS