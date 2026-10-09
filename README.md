# AI Recommendation Logic

## Project 3 - DecodeLabs

## 📌 Project Overview

AI Recommendation Logic is a simple recommendation system that recommends movies based on the user's interests.

The user enters their preferences, such as `action`, `sci-fi`, or `romance`.

The program compares these preferences with the categories of available movies and calculates a simple match score.

Movies with matching preferences are displayed as recommendations.

## 🎯 Goal

The goal of this project is to create a simple recommendation system based on user preferences.

The system:

* Takes user choices or interests
* Matches preferences using logic
* Calculates a simple similarity/match score
* Displays recommended items

## 🔑 Key Skills

* Logic building
* Pattern matching
* User input handling
* Similarity concepts
* Recommendation system concepts
* Python programming

## ⚙️ How the System Works

The recommendation process has four main steps:

### 1. Take User Input

The user enters their interests.

Example:

```text
action, sci-fi
```

### 2. Match Preferences

The program compares the user's interests with the categories of each movie.

For example:

```text
User:
action, sci-fi

Avengers:
action, sci-fi
```

Both preferences match.

### 3. Calculate Match Score

Every matching preference increases the score by 1.

Example:

```text
Avengers
action → match
sci-fi → match

Match Score = 2
```

### 4. Display Recommendations

Movies are sorted according to their match score.

Movies with higher scores are displayed first.

## 🧠 Recommendation Logic

The project uses simple preference matching.

For every movie:

```text
If user preference matches movie category:
    Increase match score
```

For example:

```text
User preferences:
action, sci-fi

Avengers:
action + sci-fi = 2 matches

John Wick:
action = 1 match

Titanic:
no matching preference = 0
```

Therefore:

```text
Avengers → Match Score: 2
John Wick → Match Score: 1
```

## 🛠️ Technologies Used

* Python 3
* Conditional logic
* Loops
* Lists
* Dictionaries
* Functions
* String processing
* Basic similarity/matching logic

## 📂 Project Structure

```text
AI-Recommendation-Logic/
│
├── recommendation.py
├── README.md
└── requirements.txt
```

## 📋 Requirements

* Python 3.x
* VS Code or any Python-supported IDE
* No external Python libraries are required

## ▶️ How to Run

### Step 1

Open the project folder in VS Code.

### Step 2

Open the VS Code terminal.

### Step 3

Run:

```bash
python recommendation.py
```

### Step 4

Enter your interests.

Example:

```text
Enter your interests separated by commas: action, sci-fi
```

## 💻 Example Output

```text
===================================
     AI RECOMMENDATION SYSTEM
===================================
This system recommends items based
on your interests.

Enter your interests separated by commas: action, sci-fi

Your interests:
- action
- sci-fi

-----------------------------------
       RECOMMENDED ITEMS
-----------------------------------
Avengers - Match Score: 2
John Wick - Match Score: 1
Interstellar - Match Score: 1
The Dark Knight - Match Score: 1

Thank you for using the AI Recommendation System!
```

## 📊 Available Categories

You can enter interests such as:

```text
action
sci-fi
adventure
thriller
crime
romance
drama
```

## 🎓 Learning Outcome

Through this project, I learned how basic recommendation systems can use user preferences and similarity logic to provide personalized recommendations.

The project demonstrates basic logic building, pattern matching, and recommendation concepts.

## 🚀 Future Improvements

The basic version can later be extended with:

* More movies and categories
* User ratings
* Larger datasets
* Advanced similarity algorithms
* Machine learning-based recommendation systems

## 👨‍💻 Project Information

**Project:** AI Recommendation Logic
**Program:** Artificial Intelligence
**Training:** DecodeLabs
**Project Number:** 3

```
```
