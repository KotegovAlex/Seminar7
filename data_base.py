from datetime import datetime as dt

def get_storage(data):
    time = dt.now().strftime('%H:%M')
    with open('bd.csv', 'a') as file:
        file.write('{};value;{}\n'
                    .format(time, data))