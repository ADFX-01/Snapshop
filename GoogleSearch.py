try:
    from googlesearch import search
except ImportError:
    print("No mod found")

file = open("tags.txt", "r")
with open('tags.txt', 'r') as myfile:
    tags = myfile.read().replace('\n', '')

searchTerms = tags + " , shopping"

print("Top result(s) pertaining to your image search: ")
for j in search(searchTerms, tld="com", num=1, stop=1, pause=2):
    print(j)
