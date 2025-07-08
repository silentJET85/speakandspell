import sys
import pyttsx3
import random
import time
from getkey import getkey, keys



level_a_words = (
	"ABOVE", "ANGEL", "ANSWER", "CALF", "DOES", "EARTH", "ECHO", "EXTRA",
	"FIVE", "FOR", "FOUR", "GUESS", "HALF", "HEALTH", "IRON", "LEARN", "NINE",
	"OCEAN", "ONCE", "ONE", "OVEN", "PINT", "PULL", "RANGE", "SAYS", "SIX",
	"SKI", "SURE", "SWAP", "TALK", "TEN", "THREE", "TO", "TOUCH", "TWO",
	"VIEW", "WARM", "WAS", "WASH", "WORD", "ZERO"
	)

level_b_words = (
	"ANOTHER", "BEAUTY", "BEIGE", "BLOOD", "BULLET", "CARRY", "CHALK",
	"CHILD", "DANGER", "EARLY", "EIGHT", "FLOOD", "FLOOR", "FRONT", "GUIDE",
	"HASTE", "HEAVEN", "LINGER", "MIRROR", "OTHER", "PRIEST", "READY",
	"RURAL", "SCHOOL", "SEVEN", "SQUAD", "SQUAT", "SUGAR", "TODAY", "UNION",
	"WATCH", "WATER", "YIELD"
	)

level_c_words = (
	"ALREADY", "BELIEVE", "BUILT", "BUSHEL", "COMFORT", "COMING", "COUPLE",
	"COUSIN", "ENOUGH", "FINGER", "GUARD", "HEALTHY", "HEAVY", "INSTEAD",
	"LAUGH", "MEASURE", "MOTHER", "NIECE", "OUTDOOR", "PERIOD", "PLAGUE",
	"POLICE", "PROMISE", "QUIET", "RANGER", "RELIEF", "REMOVE", "SEARCH",
	"SHIELD", "SHOULD", "SHOVEL", "SOMEONE", "SOURCE", "STATUE", "TERROR",
	"TROUBLE", "WELCOME", "WOLVES", "WOMAN", "WONDER", "WORTH"
	)

level_d_words = (
	"ABSCESS", "ANCIENT", "ANYTHING", "BROTHER", "BUREAU", "BUTCHER",
	"CARAVAN", "CIRCUIT", "CORSAGE", "COULDN'T", "COURAGE", "DISCOVER",
	"DUNGEON", "EARNEST", "FEATHER", "GREATER", "JEALOUS", "JOURNEY",
	"LANGUAGE", "LAUGHTER", "LEISURE", "LETTUCE", "MACHINE", "MINUTE",
	"PIERCE", "PLEASURE", "PLUNGER", "POULTRY", "QUOTIENT", "RHYTHM",
	"SCHEDULE", "SCISSORS", "SHOULDER", "SERIOUS", "STOMACH", "STRANGER",
	"SURGEON", "TOMORROW", "TREASURE", "WORKMAN", "YACHT"
	)

all_letters = (
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
	"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
	)

instructions = ("Spell.", "Now spell.", "Next, spell.", "Now try.", "Try.")
congrats = ("That is correct.", "You are correct.", "That is right", "You are right")


def display(words=""):
	if current_mode in ("spell", "say"):
		option2 = "(2:Go)"
	else:
		option2 = "      "
	if current_mode in ("spell", "say") and game_state != "diffsel":
		option3 = "(3:Replay)"
	else:
		option3 = "          "
	if current_mode in ("spell", "say")	and game_state == "active":
		option4 = "(4:Repeat)"
	else:
		option4 = "          "
	if current_mode == "mystery":
		option5 = "(5:Clue)"
		arrow6 = "^"
	else:
		option5 = "        "
		arrow6 = " "
	if current_mode == "secret":
		arrow7 = "^"
	else:
		arrow7 = " "
	if current_mode == "letter":
		arrow8 = "^"
	else:
		arrow8 = " "
	if current_mode == "say":
		arrow9 = "^"
	else:
		arrow9 = " "
	if current_mode == "spell":
		arrow0 = "^"
	else:
		arrow0 = " "

	print("\033[H\033[J") # clear the screen
	#print("
	print(
		"\n                           Speak and Spell"
		"\n|====================================================================|"
		"\n|                                                                    |"
		f"\n|           (1:Off) {option2} {option3} {option4} {option5}            |"
		"\n|  (6:Mystery Word) (7:Secret Code) (8:Letter) (9:Say It) (0:Spell)  |"
		f"\n|          {arrow6}                {arrow7}            {arrow8}          {arrow9}          {arrow0}     |"
		"\n|====================================================================|"
		"\n"
		"\n"
		)
	print(" ".join(words), flush=True, end="")
	return


def speak(words):
	engine.say(words)
	engine.runAndWait()
	return


def get_letter():
	global current_mode
	letter = getkey()
	match letter:
		case "1":
			print()
			sys.exit()
		case "2" | "3" | "4" | "5":
			return letter
		case "6":
			#Mystery Word
			current_mode = "mystery"
			return "6"
		case "7":
			#Secret Code
			current_mode = "secret"
			return "7"
		case "8":
			#Letter Mode
			current_mode = "letter"
			return "8"
		case "9":
			#Say It
			current_mode = "say"
			return "9"
		case "0":
			#Spell Mode (default)
			current_mode = "spell"
			return "0"
		case _:
			return letter.upper().replace("`", "'")


def get_sentence(word):
	sentence_words = {
		"ONE":"One. As in one word.",
		"TO":"To. As in. To Pull.",
		"TWO":"Two. As in two wolves.",
		"FOR":"For. As in for someone.",
		"FOUR":"Four. As in four wolves.",
		"EIGHT":"Eight. As in eight reindeer"
		}

	if word in sentence_words:
		return sentence_words[word]
	else:
		return word


def get_clue(word, found):
			remaining_letters = []
			for letter in word:
				if letter not in found:
					remaining_letters.append(letter)
			return random.sample(remaining_letters, 1)[0]


def convert_code(code):
	letters_a_to_c = ("A", "B", "C")
	letters_f_to_d = ("F", "E", "D")
	letters_g_to_p = ("G", "H", "I", "J", "K", "L", "M", "N", "O", "P")
	letters_z_to_q = ("Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q")
	new_text = ""

	for letter in code:
		if letter in letters_a_to_c:
			letter_index = letters_a_to_c.index(letter)
			new_letter = letters_f_to_d[letter_index]
			new_text += new_letter
		elif letter in letters_f_to_d:
			letter_index = letters_f_to_d.index(letter)
			new_letter = letters_a_to_c[letter_index]
			new_text += new_letter
		elif letter in letters_g_to_p:
			letter_index = letters_g_to_p.index(letter)
			new_letter = letters_z_to_q[letter_index]
			new_text += new_letter
		elif letter in letters_z_to_q:
			letter_index = letters_z_to_q.index(letter)
			new_letter = letters_g_to_p[letter_index]
			new_text += new_letter
		elif letter == "'":
			new_text += "'"
	return new_text


def choose_diff(mode, skip=False):
	global game_state
	game_state = "diffsel"
	if not skip:
		global difficulty_level
		difficulty_level = "A"
		entered_letter = ""
		while entered_letter != "2":
			display(f"{mode.upper()} {difficulty_level}")
			entered_letter = get_letter()
			if entered_letter in ("6", "7", "8", "9", "0"):
				return
			if entered_letter in ("A", "B", "C", "D"):
				difficulty_level = entered_letter
			if entered_letter.isalpha():
				speak(entered_letter)
			elif entered_letter == "'":
				speak("apostrophe")

	match difficulty_level:
		case "A":
			word_list = random.sample(level_a_words, 10)
		case "B":
			word_list = random.sample(level_b_words, 10)
		case "C":
			word_list = random.sample(level_c_words, 10)
		case "D":
			word_list = random.sample(level_d_words, 10)
	return word_list


def spell_mode(word_list):
	global game_state
	game_state = "active"
	num_correct = 0
	num_wrong = 0
	instruction = 0
	congrat = 0
	if word_list is None:
		return
	for word in word_list:
		tries = 2
		display()
		speak(f"{instructions[instruction]}, {get_sentence(word)}")
		if instruction == 4:
			instruction = 0
		else:
			instruction += 1

		while True:
			tries -= 1
			submit_text = False
			entered_text = ""
			display(entered_text)

			while not submit_text:
				display(entered_text)
				entered_letter = get_letter()
				if (entered_letter.isalpha() or entered_letter == "'") and len(entered_text) < 8:
					entered_text += entered_letter
					display(entered_text)
					speak(entered_letter)
				elif entered_letter == "2":
					return "Go"
				elif entered_letter == "3":
					return "Replay"
				elif entered_letter == "4":
					display(entered_text)
					speak(word)
				elif entered_letter in ("6", "7", "8", "9", "0"):
					return
				elif entered_letter == keys.BACKSPACE:
					entered_text = ""
					display(entered_text)
				elif entered_letter == keys.ENTER:
					submit_text = True

			if entered_text.strip() == word:
				speak(congrats[congrat])
				if tries > 0:
					num_correct += 1
				break
			elif tries > 0:
				speak("Wrong. Try again.")
				speak(get_sentence(word))
				num_wrong += 1
			else:
				speak(f"That is incorrect. The correct spelling of. {word}")
				word_spelling = ""
				time.sleep(0.25)
				speak("is.")
				for letter in word:
					speak(f"{letter}.")
					word_spelling += letter
					display(word_spelling)
					time.sleep(0.5)
				speak(word)
				break
		if congrat == 3:
			congrat = 0
		else:
			congrat += 1
	game_state = "postgame"
	display(f"+{num_correct}  -{num_wrong}")
	if num_wrong == 0:
		speak("Perfect score.")
	else:
		speak(f"Here is your score. {num_correct} correct. {num_wrong} wrong.")
	entered_letter = ""
	while True:
		entered_letter = get_letter()
		if entered_letter == "3":
			return "Replay"
		elif entered_letter == "2":
			return "Go"
		elif entered_letter.isalpha():
			speak(entered_letter)
			return
		elif entered_letter in ("6", "7", "8", "9", "0"):
			return


def say_it_mode(word_list):
	#say the word list
	if word_list is None:
		return
	for word in word_list:
		display(word)
		speak("Say it.")
		time.sleep(0.75)
		speak(word)
		time.sleep(0.5)
		display()
		time.sleep(0.5)
	return spell_mode(word_list)


def letter_mode():
	random_letter = random.sample(all_letters, 1)
	entered_text = ""
	entered_text += random_letter[0]
	display(entered_text)
	speak(random_letter)
	return entered_text


def secret_code_mode(text=""):
	entered_text = text
	while True:
		display(entered_text)
		entered_letter = get_letter()
		if (entered_letter.isalpha() or entered_letter == "'") and len(entered_text) < 8:
			entered_text += entered_letter
			display(entered_text)
			speak(entered_letter)
		elif entered_letter == keys.BACKSPACE:
			entered_text = ""
		elif entered_letter == keys.ENTER:
			entered_text = convert_code(entered_text)
		elif entered_letter in ("6", "7", "8", "9", "0"):
			return


def mystery_word_mode():
	combined_word_list = []
	combined_word_list = level_c_words + level_d_words
	chosen_word = random.sample(combined_word_list, 1)[0]
	word_to_guess = []
	found_letters = []
	for letter in chosen_word:
		word_to_guess += letter
		found_letters += "_"
	attempts = 7
	display("".join(found_letters))
	while attempts > 0 and found_letters != word_to_guess:
		entered_letter = get_letter()
		if entered_letter == "5" and attempts >= 2:
			attempts -= 2
			entered_letter = get_clue(word_to_guess, found_letters)
		if entered_letter.isalpha():
			speak(entered_letter)
			if entered_letter in word_to_guess and entered_letter not in found_letters:
				for letter_index, letter in enumerate(word_to_guess):
					if entered_letter == letter:
						found_letters[letter_index] = letter
			else:
				attempts -= 1
		elif entered_letter in ("6", "7", "8", "9", "0"):
			return
		display("".join(found_letters))
	if found_letters == word_to_guess:
		speak("You win!")
	else:
		display("".join(word_to_guess))
		speak("I win!")
	while True:
		entered_letter = get_letter()
		display("".join(word_to_guess))
		if entered_letter.isalpha():
			speak(entered_letter)
		elif entered_letter in ("6", "7", "8", "9", "0"):
			return


def main():
	global engine
	engine = pyttsx3.init()
	engine.setProperty('voice', 'english-us')

	global current_mode
	current_mode = "spell"
	spell_return = ""
	say_return = ""

	while True:
		match current_mode:
			case "spell":
				if spell_return == "Go":
					#skip difficulty select when "Go" pressed in spell func
					word_list = choose_diff(current_mode, skip=True)
					spell_return == ""
				else:
					word_list = choose_diff(current_mode)
				while True:
					spell_return = spell_mode(word_list)
					if spell_return != "Replay":
						break
			case "say":
				if say_return == "Go":
					#skip difficulty select when "Go" pressed in spell func
					word_list = choose_diff(current_mode, skip=True)
					say_return = ""
				else:
					word_list = choose_diff(current_mode)
				while True:
					say_return = say_it_mode(word_list)
					if say_return != "Replay":
						break
			case "letter":
				secret_code_mode(letter_mode())
			case "secret":
				secret_code_mode()
			case "mystery":
				mystery_word_mode()




if __name__ == "__main__":
	main()

