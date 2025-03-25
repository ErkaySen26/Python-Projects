import requests
def send_message(text_str):

    text_str = text_str
    chat_id = "-869810256"
    bot_id = "6511149354:AAFyJDE_-V90SNLYqelEktPsuS2TNCNOX7g"
    try:
        send = requests.get(
            f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text=' + str(
                text_str), timeout=2)

        if send.status_code > 299:
            print('TELEGRAM_ALARM_PUSH_ERROR: ', send.text)

    except Exception as exc:
        print('telegram push error: ' + str(exc))


message = "günaydın deneme"
send_message(message)
