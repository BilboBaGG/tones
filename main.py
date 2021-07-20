notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"] # Знаки нот
lengthes = [2,2,1,2,2,2] # Количества полутонов меду нотами

notesInStrings = ['До', "До диез", 'Ре', "Ми бемоль", "Ми", "Фа", "Фа диез", 'Соль', 'Соль диез', "Ля", "Си бемоль", "Си"] # Ноты прописью

allTheTones = []

# Функция, звписывающая все возможные тональности в один большой List
def MakeAllTheTones():
	for majNote in notes:
		index = notes.index(majNote)

		tone = []

		tone.append(notes[index].lower())

		for length in lengthes:
			index += length
			index %= 12
			tone.append(notes[index].lower())

		allTheTones.append(tone)

# Определение тональностей, в которых присутствует введённая нота
def SearchInTone(searchNote):
	tonesWithSearchNote = []

	for tone in allTheTones:
		if searchNote in tone:
			tonesWithSearchNote.append(tone)

	return tonesWithSearchNote

# Переменная для ввода данных
inputString = "nothing"

# Создание тональностей
MakeAllTheTones()


while True:

	inputString = str(input("\nВведите ноту, которую хотите найти в тональностях или пустую строку, если хотите увидеть все тональности : ")).lower().strip()
	print()

	while inputString != "" and inputString not in notes and inputString != "end":

		inputString = str(input("Не удовлетворяет условию, попробуйте ещё раз : ")).lower().strip()
		print()

	# Остановка программы
	if inputString == "end":
		break

	# Пересоздание 
	elif inputString == "":
		allTheTones = []
		MakeAllTheTones()

	# Если введена конкретная нота, то отсеить тональности, в которых ее нет
	else :
		allTheTones = SearchInTone(inputString)

	# Красивый вывод
	for tone in allTheTones:
	
		majNote = notesInStrings[notes.index(tone[0])]

		string = majNote + " мажор "
		string += " " * (16 - len(string)) + ":  "
		print(string, end = "")
	
		for everyNote in tone:
			if len(everyNote) == 1:
				print(everyNote.upper(), end = "   ")
			else:
				print(everyNote.upper(), end = "  ")
		print()