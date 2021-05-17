"""30. WAP to remove duplicat characters from given string """

def removeDuplicates(string):
    uniqs = ''
    for x in string:
        if not(x in uniqs):
            uniqs = uniqs + x
    print(uniqs)


removeDuplicates("aaabbcccc")
