#!/bin/bash
#Code determines if a word has more vowels than consonants and if the word is a palindrome
if [ $# -eq 0 ]; then
  read -p "Enter your name: " name #Correction: changed 'user_name' to 'name'.
else
  name="$1"
fi

lowercase_name="${name,,}" # Convert to lowercase 

vowels="aeiou"
countvow=0

for ((i = 0; i < ${#lowercase_name}; i++)); do
  char="${lowercase_name:i:1}"

  if [[ "$vowels" == *"$char"* ]]; then
    ((countvow++))
  fi
done

num_consonants=$(( ${#name} - countvow )) #Correction: "$" symbol was missing from in front of curly brace in this line.

#add function named is_palindrome
is_palindrome() {
  
  str="$1"
  reversed_str=$(echo "$str" | rev)
  
  if [ "${str,,}" == "${reversed_str,,}" ]; then
    return 0  # It's a palindrome
  else
    return 1  # It's not a palindrome
  fi
}

if ((countvow > num_consonants )); then
  echo "Hello $name, your name has more vowels! Vowels are awesome!"
else
  echo "Hi $name, your name has more consonants! Consonants give a strong sound!" #Correction: closing quotation mark was missing here.
fi

# Check if the entered name is a palindrome
if is_palindrome "$name"; then
  echo "$name is a palindrome!"
else
  echo "$name is not a palindrome."
fi

