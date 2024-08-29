# Small Projects

Welcome to the **Small Projects** repository! This is a collection of small yet useful projects and scripts that I have created to solve everyday problems or explore new ideas in programming. Each project is unique and showcases different skills and concepts, primarily using Python.

## Table of Contents


- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Projects](#projects)

## How to Use

Each project will have its folder containing the source code and a `README.md` file explaining the project, its purpose, and how to use it. To use any of the projects, clone this repository and navigate to the desired project folder:

```bash
git clone https://github.com/jit-mukherjee/small-projects.git
cd small-projects/project-folder
```

## Contributing
If you'd like to contribute to any of these projects or have suggestions for improvement, feel free to open an issue or create a pull request. Your contributions are always welcome!

## License
This repository is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.

## Contact
Feel free to reach out if you have any questions, or suggestions, or want to connect:

- **Email**: jitmukherjee.dev@gmail.com
- **LinkedIn**: [Jit Mukherjee](https://www.linkedin.com/in/jit-mukherjee)
- **Facebook Page**: [CodesByJit]([https://www.linkedin.com/in/jit-mukherjee](https://www.facebook.com/profile.php?id=61564525307391))
- **Instagram Page**: [CodesByJit](https://www.linkedin.com/in/jit-mukherjee)

## Projects

Here is a list of some of the projects included in this repository:

- **[FileFlow_Organizer.py](https://github.com/GTAJIT/Small-Projects/blob/main/FileFlow_Organizer.py)**: A Python script designed to rename files in a directory based on their creation time. This helps in organizing files chronologically, making them easier to manage and find. The script sorts files by their creation dates and renames them sequentially.
  - **Technologies Used**: Python, `os`, and `time` modules.
  - **Features**:
    - **File Listing**: Retrieves a list of files with a specified format in a given directory.
    - **Sorting**: Sorts files based on their creation times.
    - **Renaming**: Renames files sequentially according to their sorted order.
  - **Usage**: Useful for organizing directories that contain a large number of files, especially when files are added at different times and need to be arranged chronologically. This can be applied to photo collections, document archives, and other file-based datasets.
  - **Example**: The script prompts the user for the directory path and file format, then renames the files in the directory based on their creation timestamps.

- **[Blockchain-Encryption-Decryption.py](https://github.com/GTAJIT/Small-Projects/blob/main/Blockchain-Encryption-Decryption.py)**: A Python script that demonstrates basic encryption and decryption techniques using RSA-like methods. This script illustrates how to encrypt and decrypt messages, providing a simple example of cryptographic techniques used to secure and decipher data.
  - **Technologies Used**: Python.
  - **Features**:
    - **Encryption**: Encrypts a given message using a public key.
    - **Decryption**: Decrypts the encrypted message using a private key.
  - **Usage**: Ideal for learning the fundamentals of encryption and decryption processes. It provides a basic framework for understanding how public and private keys are used in cryptographic systems.
  - **Example**: The script prompts the user to input a value for the public key `E` and demonstrates encryption and decryption with predefined values for `p` and `q`.

- **[Ephemeral_Library.py](https://github.com/GTAJIT/Small-Projects/blob/main/Ephemeral_Library.py)**: A Python class-based library management system that allows users to add books, view the number of books, and print a list of all books. This script manages a dynamic list of books with interactive user input.
  - **Technologies Used**: Python.
  - **Features**:
    - **Add Books**: Adds new books to the library with user input. Ensures no duplicate entries.
    - **View Number of Books**: Displays the total number of books currently in the library.
    - **Print Books**: Lists all the books in the library.
  - **Usage**: Ideal for learning how to manage and manipulate lists in Python through a user interface. Provides a practical example of object-oriented programming.
  - **Example**: The script features a looped menu that lets users choose between adding books, viewing the count, printing the list, or exiting the program.

- **[Math-KBC.py](https://github.com/GTAJIT/Small-Projects/blob/main/Math-KBC.py)**: A Python script simulating a quiz game inspired by the "Kaun Banega Crorepati" (KBC) format with random mathematical questions. Players answer questions to earn virtual money based on their correct answers, with a simple game loop that provides feedback on their performance.
  - **Technologies Used**: Python, `random` module.
  - **Features**:
    - **Random Questions**: Generates random mathematical questions including addition, subtraction, multiplication, and division.
    - **Scoring System**: Awards virtual money based on the number of correct answers. The money increases with each correct answer.
    - **Game Loop**: Continues to ask questions until the player either provides an incorrect answer or completes all questions.
  - **Usage**: Engaging for users interested in simple game development and quiz applications. Demonstrates random number generation and basic game logic.
  - **Example**: The script randomly selects a type of mathematical question and asks the user to input their answer, providing immediate feedback on correctness and updating their virtual earnings.

- **[Name-Guessing-Game.py](https://github.com/GTAJIT/Small-Projects/blob/main/Name-Guessing-Game.py)**: A Python script for a guessing game where users attempt to guess a name from a predefined list. The game provides feedback on correct guesses and tracks the number of remaining attempts.
  - **Technologies Used**: Python.
  - **Features**:
    - **Name Selection**: Randomly selects a name from a predefined list.
    - **User Input**: Accepts user guesses and provides feedback on whether the guess is correct or not.
    - **Attempt Tracking**: Tracks and displays the number of remaining attempts.
    - **Win/Loss Conditions**: Announces the result based on whether the player guesses the name correctly within the allowed number of attempts.
  - **Usage**: Great for understanding how to handle user input, manage game state, and provide interactive feedback. Useful for learning about basic game development and loop control in Python.
  - **Example**: The script starts by asking for the user's name, then challenges the player to guess a randomly chosen name, and provides updates on their progress throughout the game.

- **[Roman_To_Int.py](https://github.com/GTAJIT/Small-Projects/blob/main/Roman_To_Int.py)**: A Python script that converts Roman numerals into their integer equivalents. This script provides a straightforward method to translate Roman numeral strings into integers, useful for understanding numeral systems and basic parsing logic.
  - **Technologies Used**: Python.
  - **Features**:
    - **Conversion**: Translates Roman numeral strings (e.g., "XIV") to their integer values (e.g., 14).
    - **Validation**: Handles invalid Roman numeral inputs by returning an appropriate message.
  - **Usage**: Useful for applications that require numeral system conversions, such as educational tools or parsing Roman numerals in various contexts.
  - **Example**: The script accepts a Roman numeral string as input and outputs the corresponding integer. For instance, inputting "MCMXCIV" will return 1994.

- **[Secret-Code-Maker.py](https://github.com/GTAJIT/Small-Projects/blob/main/Secret-Code-Maker.py)**: A Python script designed to generate secret codes or messages using a simple encoding scheme. The script allows users to create encoded messages that can be decoded later using the same script or a corresponding decoding function.
  - **Technologies Used**: Python.
  - **Features**:
    - **Encoding**: Converts a plain text message into a secret code using a predefined algorithm.
    - **Decoding**: Converts the secret code back into plain text to retrieve the original message.
  - **Usage**: Useful for understanding basic encoding and decoding techniques. Demonstrates how simple algorithms can be used to create and decipher coded messages.
  - **Example**: The script prompts the user to enter a message to encode and then displays the encoded version. It also allows decoding of the encoded message back to its original form.

- **[Snake_Water_Gun.py](https://github.com/GTAJIT/Small-Projects/blob/main/Snake_Water_Gun.py)**: A Python script for a simple command-line game where players choose between "Snake," "Water," or "Gun" to compete against a computer's random choice. The game is a variation of "Rock, Paper, Scissors" and demonstrates basic game logic and random number generation.
  - **Technologies Used**: Python, `random` module.
  - **Features**:
    - **Player Input**: Allows the player to choose between "Snake," "Water," or "Gun."
    - **Computer Choice**: The computer randomly selects one of the three options.
    - **Game Logic**: Determines the winner based on predefined rules (e.g., Snake beats Water, Water beats Gun, Gun beats Snake).
    - **Score Tracking**: Keeps track of the number of wins, losses, and draws.
  - **Usage**: Fun and educational for understanding basic game development principles, including user input handling and random number generation. Provides an example of how to implement simple game rules and logic in Python.
  - **Example**: The script prompts the player to make a choice and displays the result of each round, along with the current score.

- **[Number-Guessing-Game.py](https://github.com/GTAJIT/Small-Projects/blob/main/Number-Guessing-Game.py)**: A Python script that implements a simple number-guessing game. The player attempts to guess a randomly generated number within a specified range. The game provides feedback on whether the guess is correct and tracks the number of attempts.
  - **Technologies Used**: Python, `random` module.
  - **Features**:
    - **Random Number Generation**: Generates a random number within a given range.
    - **User Input**: Prompts the player to guess the number and provides feedback on the guess.
    - **Attempt Tracking**: Counts the number of attempts made by the player.
  - **Usage**: Great for learning about user input handling, random number generation, and basic game logic. It offers a simple example of how to create interactive applications with Python.
  - **Example**: The script allows players to guess a number between 1 and 100, providing hints as to whether their guesses are too high or


*(Adding more projects as I'm create them!)*
