# 🌸 ManabiFlow

A simple Telegram study companion built with Python.

## 📚 About the Project

ManabiFlow is a Telegram bot created to make studying more organized and focused.

It allows users to manage their study sessions and use a Pomodoro timer directly from Telegram, while keeping each user's study data separate and saved between restarts.

## ✨ What Does It Do?

ManabiFlow provides a simple study workflow:

1. Add the subject you want to study and its duration.
2. View your saved study sessions.
3. Remove sessions you no longer need.
4. Start a 25-minute Pomodoro when you're ready to focus.
5. Your study sessions are automatically saved for the next time you run the bot.

## 🚀 Features

- ➕ Add study sessions
- 📚 View saved sessions
- 🗑️ Remove sessions
- 🍅 25-minute Pomodoro timer
- 👤 Separate data for each Telegram user
- 💾 Persistent storage using JSON
- 🧵 Non-blocking Pomodoro timer using threading

## 🛠️ Technologies Used

- **Python** — Main programming language
- **pyTelegramBotAPI (Telebot)** — Telegram bot development
- **Telegram Bot API** — Communication with Telegram
- **JSON** — Saving study-session data
- **Threading** — Running the Pomodoro timer without blocking the bot

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ManabiFlow
