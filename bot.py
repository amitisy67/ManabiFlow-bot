import telebot
import studysesstion

user_states = {}

studysesstion.load_users()
user_sessions = studysesstion.user_sessions

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        'Welcome 🎀📚\n 🌸 Hey there! Im ManabiFlow!\n\n'
        "📚 Your little study companion who helps you turn goals into progress.\n\n"
        "✨ Add your study sessions,\n🍅 focus with Pomodoro,\n"
        "🌱 and build your learning journey one step at a time.\n\n"
        "Let's make studying feel like an adventure! 🚀\n\n"
        "💡 Not sure what I can do?\n"
        "Type /menu to see all my features!🎀"
    )


@bot.message_handler(commands=['menu'])
def menu(msg):
    bot.send_message(
        msg.chat.id,
        ' ✨ /add session\n📚 /view sessions\n🗑️ /remove session\n🍅 run /pomodoro'
    )


@bot.message_handler(commands=["view"])
def view_sessions(message):

    print("========== VIEW ==========")
    print("CHAT ID:", message.chat.id)
    print("USER SESSIONS:", user_sessions)
    print("FOUND:", message.chat.id in user_sessions)

    if message.chat.id in user_sessions:

        text = "📚 Your study sessions:\n\n"

        for subject, minutes in user_sessions[message.chat.id].items():
            text += f"📌 {subject}: {minutes} minutes\n"

        print("SENDING:", text)

        bot.send_message(message.chat.id, text)

    else:
        print("NO SESSION FOUND")

        bot.send_message(
            message.chat.id,
            "You don't have any study sessions yet 🎀"
        )
        
@bot.message_handler(commands=["add"])
def add(message):
    user_states[message.chat.id] = "adding"

    bot.send_message(
        message.chat.id,
        "What do you want to study today 📚✨\n"
        "Send subject name and minutes to me like this 🎀✨:\n\n"
        "Python 30"
    )


@bot.message_handler(
    func=lambda message: user_states.get(message.chat.id) == "adding"
)
def add_receive(message):

    data = message.text.split()

    subject = data[0]
    minutes = int(data[1])

    if message.chat.id not in user_sessions:
        user_sessions[message.chat.id] = {}

    user_sessions[message.chat.id][subject] = minutes

    studysesstion.save_users()

    bot.send_message(
        message.chat.id,
        f"🎉 Yay! Your {subject} session is ready!\n\n"
        f"⏰ Study time: {minutes} minutes\n"
        f"🌸 Small steps today = future achievements!"
    )


@bot.message_handler(commands=["remove"])
def remove(message):
    user_states[message.chat.id] = "removing"

    bot.send_message(
        message.chat.id,
        "🗑️ Which study session do you want to remove? 📚"
    )


@bot.message_handler(
    func=lambda message: user_states.get(message.chat.id) == "removing"
)
def remove_receive(message):

    user_states[message.chat.id] = None
    subject = message.text

    if message.chat.id in user_sessions and subject in user_sessions[message.chat.id]:

        del user_sessions[message.chat.id][subject]

        studysesstion.save_users()

        bot.send_message(
            message.chat.id,
            f"🗑️ {subject} has been removed! ✨"
        )

    else:
        bot.send_message(
            message.chat.id,
            f"❌ I couldn't find {subject} in your sessions."
        )


import time
import threading


def run_pomodoro(chat_id, minutes):

    seconds = minutes * 60

    timer_message = bot.send_message(
        chat_id,
        f"🍅 Pomodoro\n\n⏳ {minutes:02d}:00"
    )

    while seconds > 0:
        time.sleep(1)
        seconds -= 1

        mins = seconds // 60
        secs = seconds % 60

        bot.edit_message_text(
            f"🍅 Pomodoro\n\n⏳ {mins:02d}:{secs:02d}",
            chat_id=chat_id,
            message_id=timer_message.message_id
        )

    bot.edit_message_text(
        "🎉 Pomodoro finished! Great job! 🍅✨",
        chat_id=chat_id,
        message_id=timer_message.message_id
    )


@bot.message_handler(commands=["pomodoro"])
def pomodoro(message):

    print("Pomodoro received")

    bot.send_message(
        message.chat.id,
        "🍅 Pomodoro started!"
    )

    threading.Thread(
        target=run_pomodoro,
        args=(message.chat.id, 25)
    ).start()


bot.infinity_polling()