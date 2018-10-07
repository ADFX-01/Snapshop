def gSearch(tags):
    try:
        from googlesearch import search
    except ImportError:
        print("No mod found")
        
    searchTerms = tags + " , shopping"

    print("Top result(s) pertaining to your image search: ")
    for j in search(searchTerms, tld="com", num=1, stop=1, pause=2):
        print(j)