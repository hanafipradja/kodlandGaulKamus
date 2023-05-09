meme_dict = {'CRINGE':'sesuatu yang alay atau menjijikan',
             'LOL':'Ketawa sangat kencang',
             'BTW':'omong omong'
            }
            

word = input('Ketik kata yang ingin dicari tahu:')

if word in meme.dict.keys():
    # apa yang harus ditampilkan ketika kata nya ada di dalam kamus
    print(meme_dict[word])
else:
    # apa yang harus ditampilkan ketika kata nya tidak ada di dalam kamus
    print('Kata yang dicari tidak tersedia')
