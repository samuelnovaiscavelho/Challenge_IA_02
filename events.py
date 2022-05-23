import datetime


def save_event(event):
    se = open('event.txt', 'a', encoding='utf-8')
    data = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
    se.write(f"{data} | {event};\n")