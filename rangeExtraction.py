def rangeExtraction(nums):
    output = ""
    rangeStart = None
    
    for i in range(len(nums)):
        # last el edge case
        if i+1 == len(nums):
            if rangeStart is not None:
                if nums[i] - rangeStart > 1:
                    output += f'{rangeStart}-{nums[i]}'
                else:
                    output += f'{nums[i-1]},{nums[i]}'
            else:
                output += f'{nums[i]}'
        else:        
            if (nums[i+1] == (nums[i] + 1)):
                if rangeStart is None:
                    rangeStart = nums[i]
            else:
                if rangeStart is None:
                    output += f'{nums[i]},'
                else:
                    if nums[i] - rangeStart > 1:
                        output += f'{rangeStart}-{nums[i]},'
                    else:
                        output += f'{nums[i-1]},{nums[i]},'
                    rangeStart = None
    return output

#print(rangeExtraction([15, 17, 18, 19, 20]))

# 2
print(rangeExtraction([-87, -84, -82, -79, -77, -76, -73, -72, -69, -66, -63, -62]))
# '-6,-3-1,3-5,7-11,14,15,17-20'

# 3
#print(rangeExtraction([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
          #-10--8,-6,-3-1,3-5,7-11,14-15,17-20


'''ERRORS:
It should work for random inputs too: 
'-99,-97,-94,-93,-90,-88,-86,-85,-82,-79,-77,-74,-72--70,-68,-67,-65,-63,-62,-59,-57--56' 
'-99,-97,-94,-93,-90,-88,-86,-85,-82,-79,-77,-74,-72--70,-68,-67,-65,-63,-62,-59,-57,-56'

'-58--56,-54,-51,-50,-48--45,-42,-40,-37,-35,-32,-29,-27--26' 
'-58--56,-54,-51,-50,-48--45,-42,-40,-37,-35,-32,-29,-27,-26'

Testing for [-87, -84, -82, -79, -77, -76, -73, -72, -69, -66, -63, -62]
'-87,-84,-82,-79,-77,-76,-73,-72,-69,-66,-63--62' 
'-87,-84,-82,-79,-77,-76,-73,-72,-69,-66,-63,-62'
 -87,-84,-82,-79,-77,-76,-73,-72,-69,-66,-63,-62
'''
'''
output = -10--8,-6,-3-1,3-5
pocetakRangea = 3
pocetni el: 5
    ako je iduci +1 => 
        ako je iduci +1 i ako postoji pocetakRange-a=> 
            predji na iduci el
        ako je iduci +1 i ako NE postoji pocetakRange-a=> 
            detect pocetak potencijalnog range-a, postavi pocetakRange-a na [el] ako je trenutno None, ,predji na iduci el

    ako nije iduci +1 => 
        nije postajao PocetakRangea=>
            dodaj ga u output string, RESET pocetkaRangea na None

    ako nije iduci +1 i ako postoji pocetakRange-a=> 
        da li je trenutni el - pocetakRangea > 1 =>  
            da: DETEKTOVAN RANGE [unesi pocetakRangea-trenutnoEl u string], RESET pocetkaRangea na None
            ne: premal opseg [unesi (trenutniEl-1)-trenutnoEl u string], RESET pocetkaRangea na None]
   
'''