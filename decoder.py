import itertools

# This small program aims to decode the following text
# It is believed, the cipher type is "Permutation shift", 
# i.e. the text is divided into equal length units 
# and each unit is changed according to some static permutation.
# It is supposed, the text contains word (or part of a word) "Permutation"
# Program prints the text and the decoding permutation

text = "reK uzruPteminastoravhefnsrie  anedhi usfgo cdhnc ubrhselsosis chnunh ae rzkuenne,neae rdheu tbn azntmis edeu  fnrrkuue eTrez eoxdt  ne rimiKnobina totamni rnd eeraVhefn rMe. eimtduk oAfe mvmn eocnRenh nrdduen nArne yeamlsgiocelethekisnnd ii  Adeodnefrnernugnk ra tgyrpohsacpi ehreVhefnarxr eetgsmt egni.eeau eNtihrslcahpirc egxeT itnehihreece nLdrnea egenkeondrnc uHehu agefiikaatlsnedyes Bcrh uaesntbec hlietts nlecshul swetdne.rea  gDsihleecrf ftiacth uu  Bafhtuacsnabaep Drie(amgermoe)r dti p-r Terl(rmimga ue.)ze  SDrlecshulssoe t llleggaen gsneu ,uimn i  venltoalsdgeeniAssp uberroi lelna cehrSesleusumlo nlcehgium az e.c hnc Dioh ss tectn ihwnndoe,ailg  clheSesleusaslz urnuipoe.e rndmI nenbmea imsttmMset u ienre cehrSfsrpitcer ahsuatun,kzat  annnme  Sdnhauucrdumt ec leihshirncneanek  .   "

def decode(unit_length, permutation):
    result = ""
    text_units = [text[i:i+unit_length] for i in range(0, len(text), unit_length)]
    for unit in text_units:
        # means text was not split into equal parts and the last block is smaller
        # can be extended later, if no solution with exact permutations will be found 
        # would be better to check this condition before transforming text. TODO
        if (len(unit) != unit_length):
            break
            
        # Changing the symbol positions within each permutation
        # and instantly restoring the origin text
        for i in range (unit_length):
            result += unit[permutation[i]]

    # Supposed, the word "Permutation" is in the original text
    if "Permutation" in result:
        print(result)
        print()
        print()
        print("Successful permutation is ", permutation)

def main():

    # 798 symbols, which is 133 * 6 --> supposed permutation unit length is 6
    print("Text length is ", len(text))

    # Checking permutations 3-6, supposed optimal for the given text
    for i in range (3, 7):
        origin = list(range(i))
        for perm in list(itertools.permutations(origin)):
            decode(i, perm) 
    
    # successful permutation for the given text is
    # (2, 4, 0, 5, 1, 3) 

main()