try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

tags = "samsung, s8, technology, phone"
query = tags + " , shopping"

print("Top result(s) pertaining to your image search: ")
for j in search(query, tld="com", num=1, stop=1, pause=2):
    print(j)
