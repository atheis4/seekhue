from PIL import Image

def open_image(source):
    return Image.open(source)

def resize_img(image):
    ratio = image.size[0] / image.size[1]
    width = 1080
    height = int(width / ratio)
    return image.resize((width, height))

def get_data_from_im(image):
    return image.getdata()

def rearrange_data(data):
    return list(sorted(data))

def create_new_img_for_sort(image):
    return Image.new('RGB', (image.size[0], image.size[1]))

def put_data_into_new_image(new_im, sorted_data):
    return new_im.putdata(sorted_data)

def sort_rgb_to_grb(image):
    grb_values = []

    for r, g, b in image.getdata():
        reverse_data.append((b, g, r))




def main():
    im = open_image('test_imgs/van_gogh_6.jpg')

    if im.size[0] > 1080:
        im = resize_img(im)

    data = get_data_from_im(im)
    sorted_data = rearrange_data(data)

    new_im = create_new_img_for_sort(im)
    new_im.putdata(sorted_data)

    new_im.show()




if __name__=="__main__":
    main()
