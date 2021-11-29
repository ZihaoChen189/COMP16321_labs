choice = input("Enter encrypt or decrypt: ")
if choice[0] == 'e' or choice[0] == 'E': shiftValue = -3
else: shiftValue = 3
inputText = input('Input text: ')
resultingText = ""
inputTextPosition = 0
while (inputTextPosition < len(inputText)):
inputTextChar = inputText[inputTextPosition]
ASCIIValue = ord(inputTextChar);
ASCIIValue += shiftValue
resultingText = resultingText + chr(ASCIIValue)
inputTextPosition+=1
print(resultingText)
def main():
def get_choice():
choice = input("Enter encrypt or decrypt: ")
if choice[0] == 'e' or choice[0] == 'E':
shift_value = -3
else:
shift_value = 3
def get_choice():
choice = input("Enter encrypt or decrypt: ")
if choice[0] == 'e' or choice[0] == 'E':
return -3
else:
return 3
def main():
shift_value = get_choice()
def main():
shift_value = get_choice()
input_text = input('Input text: ')
def do_conversion(input_text, shift_value):
resulting_text = ""
input_text_position = 0
while (input_text_position < len(input_text)):
input_text_char = input_text[input_text_position]
ascii_value = ord(input_text_char)
ascii_value += shift_value
resulting_text = resulting_text + chr(ascii_value)
input_text_position += 1
print(resulting_text)
def main():
shift_value = get_choice()
input_text = input('Input text: ')
do_conversion(input_text, shift_value)
print(resulting_text) to
return resulting_text.


