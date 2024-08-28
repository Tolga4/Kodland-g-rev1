meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH":"onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": " agresifleşmek/sinirlenmek",
            }
secim = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if secim in meme_dict.keys():
    print(meme_dict[secim])
else:
    print("bunu bilmiyorum")
