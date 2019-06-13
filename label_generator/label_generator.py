import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

marker_dictionary = cv2.aruco.getPredefinedDictionary(3)

image_width = 1024
image_height = 512
top_bar_height = 128
bottom_bar_height = 128
fontpath = "./PORTAGO.TTF"     
marker_size = 60
marker_offset_x = 32
marker_offset_y = 32
marker_border_size = 10

def get_marker_for(id:int, size_in_pixels:int=256):
    return marker_dictionary.drawMarker(id, size_in_pixels)

def parse_color(code):
    if code.startswith("#"):
        pattern = "0x{}"
        r = int(pattern.format(code[1:3]),16)
        g = int(pattern.format(code[3:5]),16)
        b = int(pattern.format(code[5:7]),16)
        return b, g, r
    else:
        colors = {
            #name:     (  B  ,  G  ,  R ),
            "red":     (0x00, 0x00, 0xFF),
            "green":   (0x00, 0xFF, 0x00),
            "blue":    (0xFF, 0x00, 0x00),
            "yellow":  (0x00, 0xFF, 0xFF),
            "magenta": (0xFF, 0x00, 0xFF),
            "cyan":    (0xFF, 0xFF, 0x00),
            "white":   (0xFF, 0xFF, 0xFF),
            "black":   (0x00, 0x00, 0x00),
        }
        color = colors.get(code.lower())
        return color

def draw_bars(img, top_color, bottom_color):
    img = cv2.rectangle(img, (0,0), (image_width, top_bar_height), top_color, -1)
    img = cv2.rectangle(img, (0, image_height-1-bottom_bar_height), (image_width-1, image_height-1), bottom_color, -1)
    return img

def draw_markers(img, id1, id2, id3, id4):
    marker1 = get_marker_for(id1, marker_size)
    marker2 = get_marker_for(id2, marker_size)
    marker3 = get_marker_for(id3, marker_size)
    marker4 = get_marker_for(id4, marker_size)

    border_size = marker_size+2*marker_border_size

    border_x_offset_left = marker_offset_x - marker_border_size
    border_x_offset_right = image_width - (border_x_offset_left + border_size)
    border_y_offset_upper = marker_offset_y - marker_border_size
    border_y_offset_lower = image_height - (border_y_offset_upper + border_size)

    marker_x_offset_left = marker_offset_x
    marker_x_offset_right = image_width - (marker_offset_x + marker_size)
    marker_y_offset_upper = marker_offset_y
    marker_y_offset_lower = image_height - (marker_offset_y + marker_size)

    img[border_y_offset_upper+1:border_y_offset_upper+border_size+1, border_x_offset_left:border_x_offset_left+border_size, :] = np.ones((border_size,border_size,3)) * 255
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_left:marker_x_offset_left+marker_size, 0] = marker1
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_left:marker_x_offset_left+marker_size, 1] = marker1
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_left:marker_x_offset_left+marker_size, 2] = marker1

    img[border_y_offset_upper+1:border_y_offset_upper+border_size+1, border_x_offset_right:border_x_offset_right+border_size, :] = np.ones((border_size,border_size,3)) * 255
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_right:marker_x_offset_right+marker_size, 0] = marker2
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_right:marker_x_offset_right+marker_size, 1] = marker2
    img[marker_y_offset_upper+1:marker_y_offset_upper+marker_size+1, marker_x_offset_right:marker_x_offset_right+marker_size, 2] = marker2

    img[border_y_offset_lower:border_y_offset_lower+border_size, border_x_offset_right:border_x_offset_right+border_size, :] = np.ones((border_size, border_size,3)) * 255
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_right:marker_x_offset_right+marker_size, 0] = marker3
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_right:marker_x_offset_right+marker_size, 1] = marker3
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_right:marker_x_offset_right+marker_size, 2] = marker3

    img[border_y_offset_lower:border_y_offset_lower+border_size, border_x_offset_left:border_x_offset_left+border_size, :] = np.ones((border_size, border_size,3)) * 255
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_left:marker_x_offset_left+marker_size, 0] = marker4
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_left:marker_x_offset_left+marker_size, 1] = marker4
    img[marker_y_offset_lower:marker_y_offset_lower+marker_size, marker_x_offset_left:marker_x_offset_left+marker_size, 2] = marker4

    return img

def draw_text(img, number:int, scale:int=400, offset_x:int=325, offset_y:int=10):

    font = ImageFont.truetype(fontpath, scale)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    number_as_string = "{:03d}".format(number)
    draw.text((offset_x, offset_y),  number_as_string, font = font, fill = (0,0,0, 255))
    img = np.array(img_pil)

    return img

def main(*args):
    expected_types = [int, int, int, int, int, str, str, str, str]
    if len(args) != len(expected_types):
        print("usage: python label_generator.py id1 id2 id3 id4 starting_number image_path top_color bottom_color output_path")
        print("example: python label_generator.py 1 23 45 678 678 ./testimage.png #1256f3 #1256f3 ./test_output.png")
        exit(1)
    id1, id2, id3, id4, starting_number, image_path, top_color, bottom_color, output_path = [t(v) for t, v in zip(expected_types, args)]
    top_color = parse_color(top_color)
    bottom_color = parse_color(bottom_color)

    bg = cv2.imread(image_path, 0)

    img = np.ones((512, 1024, 3), np.uint8)*255
    img = draw_bars(img, top_color, bottom_color)
    img = draw_markers(img, id1, id2, id3, id4)
    img = draw_text(img, starting_number, 600, 180, -120)

    cv2.imwrite(output_path, img)

if __name__ == "__main__":
    from sys import argv
    main(*argv[1:])