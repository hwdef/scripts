from moviepy.editor import AudioFileClip
import argparse,os,platform,sys

if platform.system().lower() == 'windows':
    print('Windows is not supported, the program terminates.')
    sys.exit(1)

parser = argparse.ArgumentParser('Extract audio from video')
parser.add_argument('--video','-v',help='Path to the directory where the video is located.',default='video')
parser.add_argument('--audio','-a',help='Path to the audio output directory.',default='audio')
parser.add_argument('--suffix','-s',help='video file suffix.',default='mp4')
args = parser.parse_args()

os.makedirs(args.audio)

files = os.listdir(args.video)
for file in files:
    if file.endswith(args.suffix):
        audio_clip = AudioFileClip(args.video+'/'+file)
        audio_clip.write_audiofile(args.audio+'/'+file[:-len(args.suffix)]+'.mp3')