# with open("/Letters/starting_letter.docx") as s:
#     l=s.read()
# with open("Input/Names/invited_names.txt") as i:
#     m=i.read()

# def genw():
#     w=""
#     ww=[]
#     for i in l:
#         w+=i
#         if i==" ":
#             ww.append(w)
#             w=""
#     return ww
def genn():
    n=""
    nn=[]
    for i in m:
        if i!="\n":
            n+=i
        else:
            nn.append(n)
            n=""
    return nn


# ww=genw()
# nn=genn()

# def letter(name):
#     l=[]
#     ll=""
#     for i in ww:
#         if i=="[name], ":
#             i=name+", "
#         l.append(i)
#     for i in l:
#         ll+=i
#     return ll
# for z in nn:
#     letter(z)
# for z in nn:
#     with open(f"/letter_for_{z}.doxc","w") as y:
#         y.write(letter(z))
#OR
with open("/letter generator 1.0/Input/Letters/starting_letter.docx") as s:
    l=s.read()
with open("../letter generator 1.0/Input/Names/invited_names.txt") as i:
    m=i.read()
nn=genn()
for z in nn:
    with open(f"../letter generator 1.0/Output/ReadyToSend/letter_for_{z}.docx","w") as y:
        text=l.replace("[name]",z)
        y.write(text)


#readline(): helps you to generate a list of text
#replace(): helps you to switch words
#strip(): helps you to take away spaces at the end and beginning of string