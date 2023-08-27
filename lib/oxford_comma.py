def oxford_comma(items):
    if(len(items)==1):
        return items[0]
    elif(len(items)==2):
        return items[0]+' and '+items[1]
    else:
        without_end = [item for item in items if items.index(item)!=len(items)-1]
        return ', '.join(without_end)+', and '+items[-1]

oxford_comma(['hello', 'bye', 'goodbye'])