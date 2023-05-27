translationdict = {
  "apa": "what",
  "saya" : "I",
  "kamu" : "you",
  "dia": "he/she",
  "kami" : "we",
  "mereka" : "they",
  "termina kasih" : "thank you",
  "ya" : "yes",
  "tidak" : "no",
  "rumah" : "house",
  "makan" : "eat",
  "minum" : "drink",
  "belajar" : "study",
  "buku" : "book",
  "sekolah" : "school",
  "teman" : "friend",
  "tanggal" : "date",
  "waktu" : "time",
  "kerja" : "work",
}


def translate_word(word, dictionary):
  if word in dictionary:
    return dictionary[word]
  else:
    return "Translation not available."
  
  
while True:
  print("Translation Options:")
  print("1. Indonesian to English")
  print("2. English to Indonesian")
  print("3. Exit")

  choice = input("Enter your choice (1, 2, or 3): ")

  if choice == "1":
    indonesian_word = input("Enter an Indonesian word: ")
    translation = translate_word(indonesian_word, translation_dict)
    print("English translation:", translation)

  elif choice == "2":
    english_word = input("Enter an English word: ")
    reverse_dict = {value: key for key, value in translation_dict.items()}
    translation = translate_word(english_word, reverse_dict)
    print("Indonesian Translation:", translation)

  elif choice == "3":
    print("Exiting...")
    break

  else:
    print("Invalid choice. Please try again.")
          
         
    
    
