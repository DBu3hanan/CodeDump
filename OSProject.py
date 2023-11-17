import os

# Define the file system size and block size
FILE_SYSTEM_SIZE = 30
BLOCK_SIZE = 8

# Define the file names and their contents
files = {
    'A': 'The Power to Be Your Best.',
    'B': 'This program has performed an illegal operation and will be shut down.',
    'C': 'From tiny ACORNS mighty UNIX trees grow.'
}

# Initialize the file system with empty blocks
file_system = [''] * FILE_SYSTEM_SIZE


# Function to allocate blocks for a file's content
def allocate_blocks(content):
  allocated_blocks = []
  remaining_content = content

  while remaining_content:
    block = find_empty_block()
    if block is None:
      print("Error: File system is full.")
      return None

    allocated_blocks.append(block)

    # Fill the block with content (up to BLOCK_SIZE characters)
    file_system[block] = remaining_content[:BLOCK_SIZE]

    # Remove the filled characters from the remaining content
    remaining_content = remaining_content[BLOCK_SIZE:]

  return allocated_blocks


def total_blocks_used_in_system():
  stat = os.statvfs('/')
  block_size = stat.f_frsize
  total_blocks = stat.f_blocks
  total_size_bytes = total_blocks * block_size
  print(f'Total blocks used in the system: {total_size_bytes} bytes')


# Function to append a word at the front, middle, or back of a file's content
def append_word(file_name, position, word):
  if file_name not in files:
    print(f"Error: File '{file_name}' does not exist.")
    return

  content = files[file_name]

  if position == 'front' or 'f':
    content = word + content
  elif position == 'middle' or 'm':
    middle = len(content) // 2
    content = content[:middle] + word + content[middle:]
  elif position == 'back' or 'b':
    content = content + word
  else:
    print("Invalid position. Use 'front', 'middle', or 'back'.")
    return

  files[file_name] = content

  print(f"File {file_name} after appending at {position}: {content}")

  print()
  display_file_in_blocks(file_name, content)


def display_file_in_blocks(file_name, content):
  block_count = (len(content) + BLOCK_SIZE - 1) // BLOCK_SIZE

  print(f"File {file_name} after appending:")
  for i in range(block_count):
    start = i * BLOCK_SIZE
    end = (i + 1) * BLOCK_SIZE
    block_content = content[start:end]
    print(f"Block {i + 1}: {block_content}")


# Function to find an empty block in the file system
def find_empty_block():
  for i, block in enumerate(file_system):
    if not block:
      return i

  return None


# Function to read a file's content from allocated blocks
def read_file(file_name, position):
  if file_name not in files:
    print(f"Error: File '{file_name}' does not exist.")
    return

  content = files[file_name]

  if position == 'front' or 'r':
    result = content[:50]  # Read first 50 characters
  elif position == 'middle' or 'm':
    middle = len(content) // 2
    result = content[middle - 25:middle +
                     25]  # Read 50 characters around the middle
  elif position == 'back' or 'b':
    result = content[-50:]  # Read last 50 characters
  else:
    print("Invalid position. Use 'front', 'middle', or 'back'.")
    return

  print(f"File {file_name} content at {position}: {result}")
  # IF END IS CHOSEN , IT STILL PRINTS WITH END AS A POSITION


# def save_file(file_name):


# Function to write a file's content to allocated blocks
def write_file(file_name, content):

  files[file_name] = content
  print(f"File '{file_name}' created with content: {content}")


# Function to delete a file's content from allocated blocks
def delete_file(file_name, position, word):
  if file_name not in files:
    print(f"Error: File '{file_name}' does not exist.")
    return

  content = files[file_name]

  if position == 'front':
    if content.startswith(word):
      content = content[len(word):]
    else:
      print(f"Error: Word '{word}' not found at the front.")
      return
  elif position == 'middle':
    if word in content:
      content = content.replace(word, '', 1)
    else:
      print(f"Error: Word '{word}' not found in the middle.")
      return
  elif position == 'back':
    if content.endswith(word):
      content = content[:len(content) - len(word)]
    else:
      print(f"Error: Word '{word}' not found at the back.")
      return
  else:
    print("Invalid position. Use 'front', 'middle', or 'back'.")
    return

  # Update the file's content
  files[file_name] = content

  # Display the updated file content
  print(f"File {file_name} after deleting '{word}': {content}")


def size_command(file_name):
  # Implement SIZE command to display the size of a file
  if file_name in files:
    char_count, block_count = get_file_size(files[file_name])
    print(
        f"File {file_name} size: {char_count} characters, {block_count} blocks"
    )


# Define a function to get the size of a file in characters and blocks
def get_file_size(file_content):
  if file_content is None:
    return 0, 0
  char_count = len(file_content)
  block_count = (char_count + 7) // 8
  return char_count, block_count


# Function to display the current state of the file system
def display_file_system():
  print()

  print("\nFiles:")

  #for file_name, allocated_blocks in files.items():
  #print(f"{file_name}: {allocated_blocks}")
  for file_name, block in files.items():
    print(f"{file_name}: {block}")

  print()

# Main loop
while True:
  command = input(
      "\nChoose a command: \nHelp | Size | Create (C) | Read (R) | Write (W) | Delete (D) | Exit | Append (A) \n\n:- "
  )

  if command.lower() == 'create' or  command.lower() == 'c' :  #ALLOW TO DO DIFFERENT CASES

    file_name = input("Enter the name of the file to create: ")

    if file_name in files:
      print(f"Error: File '{file_name}' already exists.")
      continue

    content = input("Enter the content of the file: ")

    allocate_blocks(content)

    write_file(file_name, content)

    display_file_system()


  elif command.lower() == 'read' or command.lower() == 'r':
    file_name = input("Enter the name of the file to read: ")
    position = input("Enter the position (front, middle, or back): ")
    read_file(file_name, position)



  elif command.lower() == 'write' or command.lower() == 'w':
    file_name = input("Enter the name of the file to write: ")

    if file_name not in files:
      print(f"Error: File '{file_name}' does not exist.")
      continue

    content = input("Enter the new content of the file: ")

    print(file_name)

    write_file(file_name, content)

    display_file_system()

  elif command.lower() == 'delete' or command.lower() == 'd':
    file_name = input("Enter the name of the file to delete: ")

    position = input(
        "Enter the position (front or f), (middle or m), or (back or b)): ")
    word = input("Enter the word to delete: ")

    delete_file(file_name, position, word)

    display_file_system()

  elif command.lower() == 'append' or command.lower() == 'a':
    file_name = input("Enter the name of the file to be appended : ")
    position = input(
        "Enter the position (front or f), (middle or m), or (back or b)): ")
    allocate_blocks(file_name)
    word = input("Enter the word to append: ")

    append_word(file_name, position, word)
    display_file_in_blocks(file_name, word)

  elif command.upper() == "HELP":
    available_commands = input(
        "Available Commands: APPEND, DELETE, READ, WRITE, CREATE, EXIT. Choose one"
    )
    if (available_commands == "HELP APP"):
      print("APPEND - Appends a word to a file.")
    elif (available_commands == "HELP DEL"):
      print("DEL - Deletes a word from a file")
    elif (available_commands == "HELP READ"):
      print("READ - Reads a file")
    elif (available_commands == "HELP WRITE"):
      print("WRITE - Writes a file")
    elif (available_commands == "HELP CREATE"):
      print("CREATE - Creates a file")
    elif (available_commands == "Size"):
      choice = input(
          "SIZE - Displays the total blocks used in the system(A)or the number of characters in the given file (B)"
      )
      if (choice.upper() == "A"):
        print("The total number of blocks used in the system is: ", end="")
        total_blocks_used_in_system()
      elif (choice.upper == "B"):
        file_name = input("Enter the name of the file: ")
        char_count = size_command(file_name)
        print("The number of characters in the given file is: ", end="")
        print(char_count)

  elif command.lower() == 'exit':
    print("File manager terminated.")
    exit()

  else:
    print("Invalid command. Please try again.")
