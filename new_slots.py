from coordinates_generator import CoordinatesGenerator
from colors import *
import cv2
import glob

def read_name(name):
    global video_name
    video_name = name

    file_list = glob.glob('videos/*.*')
    for x in file_list:
        f = x.lstrip('videos\\\\').rstrip('.mp4')
        if f == video_name:
            video_file = 'videos/' + video_name + '.mp4'
            image_file = get_first_frame(video_name, video_file)
            data_file = 'data/' + video_name + '.yml'
            if image_file is not None:
                with open(data_file, "w+") as points:
                    generator = CoordinatesGenerator(image_file, points, COLOR_RED)
                    generator.generate()
            return 'success'
        return ''



def get_first_frame(_name, video_file):
    vid_cap = cv2.VideoCapture(video_file)
    success, image = vid_cap.read()
    if success:
        image_name = 'images/' + _name + '.png'
        cv2.imwrite(image_name, image)  # save frame as JPEG file
    return image_name


video_name = ''
