import os


all_videos = ('bkb',
              'eul',
              'glyph',
              'lose',
              'roshan',
              'shiva',
              'shrine',
              'teamFight',
              'teleport',
              'towerDestory')


def process_videos(video_list=all_videos):
    if not os.path.exists('./frames'):
        os.makedirs('./frames')

    for video in video_list:
        if os.path.exists('./' + video):
            for i in range(1, 11):
                video_name = './' + video + '/' + video + '_' + str(i) + '.mp4'
                destination = './frames/' + video + '_'
                get_frame(video_name, destination)


def get_frame(video, directory):
    """
    extract frames from videos with given FPS 15
    """

    fps = '30'
    dest = video[-5:-4]  # The folder that the frame images will end up in
    os.system('ffmpeg -i ' + video + ' -vf scale=720:720' + ' -r ' + fps + ' ' + directory + dest + '_%03d.png')


def main():
    process_videos()


if __name__ == '__main__':
    main()
