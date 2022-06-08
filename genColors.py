rgb_values = [[122, 123, 100], [11, 55, 12], [220, 100, 200]]

def genColors():
    from PIL import Image
    import numpy as np

    im = Image.open('traits/HOOPAZ-base.png')
    im = im.convert('RGBA')

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    #

    print(green[1020][355])

    # Replace white with red... (leaves alpha values alone...)
    for i in range(0,3):
        white_areas = (red == red[1020][355]) & (green == green[1020][355]) & (blue == blue[1020][355])
        data[..., :-1][white_areas.T] = (rgb_values[i]) # Transpose back needed

        im2 = Image.fromarray(data)
        im2.save(str(i) + "base.png")


genColors()