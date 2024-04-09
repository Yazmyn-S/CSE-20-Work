# assignment: programming assignment 4
# author: Yazmyn Sims
# date: 11/21/2022
# file: cipher.py is a program that encodes or decodes a user provided message.
# input: user will select if they want to encode or decode a message then they will choose a file for reading and another file for writing.
# output: the program will output the plaintext and the ciphertext.

def readfile():
   message = ""
   file = input("Please enter a file for reading:\n")
   try :
      file1 = open (file, "r")
      #for line in file1 :
         #message.append(line.strip())
   except IOError :
      print ("The selected file cannot be open for reading!")
      return readfile()
   else:
      message = file1.read()
      file1.close()    
   return message

def writefile(message):
   file = input("Please enter a file for writing:\n")
   try:
      file1 = open(file, "w")
      file1.writelines(message)
   except IOError:
      print("Cannot write to a file!")
   else:
      file1.close()   

def make_alphabet():
   alphabet = ()
   for i in range(26):
      char = i + 65
      alphabet += (chr(char),)
      #print (alphabet)
   return alphabet

def encode(plaintext, shift = 3):
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for line in plaintext:
      s = ""
      for char in line:
         if char in alphabet:
            i = alphabet.index(char)
            letter = alphabet[(i + shift) % length]
            s += letter
         else:
            s += char
      ciphertext.append(s)  
   return ciphertext 

# decode ciphertext letter by letter using a Caesar cipher
def decode(ciphertext, shift = -3):
   plaintext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for line in ciphertext:
      s = ""
      for char in line:
         if char in alphabet:
            i = alphabet.index(char)
            letter = alphabet[(i + shift) % length]
            s += letter
         else:
            s += char
      plaintext.append(s)
   return plaintext
   
# convert a list into a string
def to_string(text):
   s = ""
   s = s.upper()
   for element in text:
      s = s + element
   return s

# main program
if __name__ == '__main__':
   choice = "a"

   while choice != "q" or choice != "Q" or choice != "e" or choice != "E" or choice != "d" or choice != "D":
      choice = input("Would you like to encode or decode the message?\n" \
                     "Type E to encode, D to decode, or Q to quit:\n")

      #Encode
      if choice == "e" or choice == "E":
         
         message = readfile()
                  
         encoded = encode(message)
         writefile(encoded)
         encoded = to_string(encoded)

         print("Plaintext:")
         print(to_string(message))
         print("Ciphertext:")
         print(encoded)
         
      #Decode
      elif choice == "d" or choice == "D":
         encoded1 = readfile()
         
         decoded = decode(encoded1)
         writefile(decoded)
         decoded = to_string(decoded)

         print ("Ciphertext: ")
         print(to_string(encoded1))
         
         print("Plaintext: ")
         print(decoded)
      #Bad Choice
      elif choice == "q" or choice == "Q":
         print("Goodbye!")
         break
