def postupdate(post,residence,phone,email):
    with open('input.txt') as fo:
        postindex = -1
        for rec in fo:
            content = fo.readlines()

            for line in content:
                words = line.split()

                for word in words:
                    if "promoted" in word:
                        postindex = words.index(word)
                        index = postindex + 2
                        while index < len(words):
                            post.append(words[index])
                            index = index + 1


                    if "shift" in word or "move" in word:
                        postindex = words.index(word)
                        index=postindex+2
                        while index < len(words):
                            residence.append(words[index])
                            index = index +1

                    if "phone" in word or "mobile" in word:
                        postindex = words.index(word)
                        phone.append(words[postindex+3])

                    if "@gmail.com" in word or "@iitg.ernet.in" in word:
                        email.append(word)