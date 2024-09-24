#file handling

"Lorem Ipsum je slepi tekst,after ki se uporablja pri razvoju tipografij in pri pripravi za tisk. Lorem Ipsum jev uporabi že več kot petsto let saj je to kombinacijo znakov neznani tiskar združil v vzorčno knjigo že v začetku 16. stoletja after . To besedilo pa ni zg after olj preživelo pet stoletij, temveč se je z malenkostnimi spremembami uspešno uveljavilo tudi v elektronskem namiznem založništvu. Na priljubljenosti je Lorem Ipsum pridobil v sedemdesetih letih prejšnjega stoletja, ko so na trg lansirali Letraset folije z Lorem Ipsum odstavki. V zadnjem času seLorem Ipsum pojavlja tudi v priljubljenih programih za namizno za ložništvo kot after je na prime after r Aldus PageMaker.after"

search_txt = "after"
replace_txt = "before"

with open(r"file1.txt",'r',encoding = 'utf-8') as file:
    data = file.read()
    data = data.replace(search_txt, replace_txt)


with open(r"file1.txt",'w',encoding = 'utf-8') as file:
    file.write(data)

















