import json
import pandas as pd

def load_data():
    try:
        with open('file.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def data_save(videos):
    with open('file.txt', 'w') as file:
        json.dump(videos, file)

def list_data(videos):
    print('\n')
    d_set = pd.DataFrame({'Name':[v["title"] for v in videos],'Time':[v["time"] for v in videos]},index=range(1, len(videos)+1))
    print(d_set)


def add(videos):
    title = input('Enter video title: ')
    time = input('Enter video time: ')
    videos.append({'title': title, 'time': time})
    data_save(videos)

def update(videos):
    list_data(videos)
    
    index = int(input('Enter the number of the video to update: '))
    if 1 <= index <= len(videos):
        title = input('Enter new video title: ')
        time = input('Enter new video time: ')
        videos[index - 1] = {'title': title, 'time': time}
        data_save(videos)
    else:
        print('Invalid choice')
    
def remove(videos):
    list_data(videos)
    
    index = int(input('Enter the number of the video to remove: '))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        data_save(videos)
    else:
        print('Invalid choice')


def main():
    videos = load_data()
    while True:
        print('\nWelcome to youtube video manager.........')
        print('Choose your Options')
        print('1. List all videos.')
        print('2. Add Videos.')
        print('3. Update Videos.')
        print('4. Remove Videos.')
        print('5. Exit')

        choice = int(input('\nEnter your choice: '))

        match choice:
            case 1:
                list_data(videos)
                if input('Press Enter to continue...') == '':
                    pass
            case 2:
                add(videos)
            case 3:
                update(videos)
            case 4:
                remove(videos)    
            case 5:
                break  
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()