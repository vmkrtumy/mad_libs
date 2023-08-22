def temp1():
	v = ['a,', 'e', 'i', 'i', 'u']
	number = input('input a number: ')
	time_mes = input('input a mesure of time: ')
	transport = input('input a mode of transportation: ')
	adjective = input('input an adjective: ')
	an = []
	if adjective[0] in v:
    		an.append("an")
	else:
    		an.append("a")
	a = ''.join(an)
	adjective2 = input('input another adjective: ')
	noun = input('input a plural noun: ')
	color = input('input a color: ')
	body_part = input('input a part of the body: ')
	verb = input('input a verb: ')
	number2 = input('input another number: ')
	noun2 = input('input another noun: ')
	noun3 = input('input another noun: ')
	body_part2 = input('input another part of the body: ')
	noun4 = input('input another noun: ')
	adjective3 = input('input another adjective: ')
	silly_word = input('input a silly word: ')
	l1 = ["It was about ", number, " ", time_mes, " ago when I arrived at the hospital in a ", transport, ". The hospital is ", a, " ", adjective, " place, there are a lot of ", adjective2, " ",  noun, " here. There are nurses here who have ", color, " ", body_part, ". If someone wants to come into my room I told them that they have to ", verb, " first. I’ve decorated my room with ",  number2, " ", noun2, ". Today I talked to a doctor and they were wearing a ", noun3, " on their ", body_part2, ". I heard that all doctors ", verb, " ", noun4, " every day for breakfast. The most ", adjective3, " thing about being in the hospital is the ", silly_word, " ", noun, "!"]
	print(''.join(l1))

def temp2():
	v = ['a,', 'e', 'i', 'i', 'u']
	person = input("input a person's name: ")
	noun = input('input a noun: ')
	ad_feeling = input('input an adjective feeling: ')
	verb = input('input a verb: ')
	ad_feeling2 = input('input another adjective feeling: ')
	an = []
	if ad_feeling2[0] in v:
		an.append("an")
	else:
		an.append("a")
	a = ''.join(an)
	animal = input('input an animal: ')
	verb2 = input('input another verb: ')
	color = input('input a color: ')
	v_ing = input('input a verb ending in ing: ')
	adverb_ly = input('input an adverb ending in ly: ')
	number = input('input a number ')
	mes_time = input('input a mesure of time: ')
	number2 = input('input another number: ')
	silly_wrd = input('input a silly word: ')
	noun2 = input('input another noun: ')
	l2 = ["This weekend I am going camping with ", person, ". I packed my lantern, sleeping bag, and ", noun, ". I am so ", ad_feeling, " to ", verb, " in a tent. I am ", ad_feeling2, " we might see ", a, ' ', animal, ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and ", verb2, ". I have heard that the ", color, " lake is great for ", v_ing, ". Then we will ", adverb_ly, " hike through the forest for ", number, " ", mes_time, " If I see a ", color, " ", animal, " while hiking, I am going to bring it home as a pet! At night we will tell ", number2, " ", silly_wrd, " stories and roast ", noun2, " around the campfire!!"]
	print(''.join(l2))	

def temp3():
	v = ['a,', 'e', 'i', 'i', 'u']
	person = input("input a person's name: ")
	adjective = input('input an adjective: ')
	color = input('input a color: ')
	animal = input('input an animal: ')
	place = input('input a place: ')
	adjective2 = input('another adjective: ')
	creatures = input('input a magical creature(plural): ')
	adjective3 = input('input another adjective: ')
	creatures2 = input('input another magical creature(plural): ')
	room = input('input a room in a house: ')
	noun = input('input a noun: ')
	noun2 = input('input another noun: ')
	nouns3 = input('input another noun(plural): ')
	adjective4 = input('input another adjective: ')
	nouns4 = input('input another noun(plural): ')
	number = input('input a number: ')
	mes_time = input('input a mesurement of time: ')
	v_ing = input('input a verb ending in ing: ')
	adjective5 = input('input another adjective: ')
	noun5 = input('input another noun: ')
	an = []
	if adjective[0] in v:
		an.append("an")
	else:
		an.append("a")
	a = ''.join(an)
	l3 = ["Dear", person, ", I am writing to you from ", a, " ", adjective, " castle in an enchanted forest. I found myself here one day after going for a ride on a ", color, " ", animal, " ", place, ". There are ", adjective2, " ", creatures, " and ", adjective3, " ", creatures2, " here! In the ", room, " there is a pool full of ", noun, ". I fall asleep each night on a ", noun2, " of ", nouns3, " and dream of ", adjective4, " ", nouns4, ". It feels as though I have lived here for ", number, " ", mes_time, ". I hope one day you can visit, although the only way to get here now is ", v_ing, " on a ", adjective5, " ", noun5]
	print(''.join(l3))

t = int(input("Choose a template: 1, 2 or 3: "))
if t == 1:
	temp1()
elif t == 2:
	temp2()
else:
	temp3()
