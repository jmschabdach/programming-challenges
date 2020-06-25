def rgbToHex(rgb):
    hexStr = ""
    for c in rgb:
        if c < 16:
            hexStr += "0"+hex(c)[-1]
        else:
            hexStr += hex(c)[-2:]
    return hexStr

if __name__ == "__main__":
    color1 = (51, 51, 255) # blue, should be 3333ff
    color2 = (102, 15, 102) # green, should be 66ff66
    color3 = (255, 0, 102) # pink, should be ff0066
    color4 = (255, 204, 102) # pale orange, should be ffcc66

    print(rgbToHex(color1))
    print(rgbToHex(color2))
    print(rgbToHex(color3))
    print(rgbToHex(color4))

