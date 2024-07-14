meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek",
            "GG" : "iyi oyundu",
            "ALT+F4" : "uygulamadan çıkartan kısayol",
            "SKIBIDI" : "tuvalet kafalı mem",
            "RIZZ" : "karşı konulamaz havalılık",
            "SIGMA" : "Psikolojik olarak bağımsız ve özgür ruhlu kişilere verilen unvan",
            "GIGACHAD" : "Güçlü, çekici erkek idolü",
            "OHIO" : "Amerika'da garip olaylarla ilişkilendirilen eyalet.",
            "W" : "Kazanmak ya da kazanan kişi",
            "L" : "kaybetmek ya da kaybeden kişi",
            "GYATT" : "Çekici kadın",
            "FANUM TAX" : "Arkadaşın yemek yerken ondan aldığın vergi",
            "ALPHA" : "Alfa kişi",
            "NIGGA" : "siyahi kişi",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Girdiğiniz kelime sözlükte yok!")
