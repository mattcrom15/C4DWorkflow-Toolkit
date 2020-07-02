### solo and frame selected objects
### unsolo and frame all objects


import c4d


def main():
    if c4d.IsCommandChecked(431000058):
        c4d.CallCommand(100004768, 100004768) # Select Children
        c4d.CallCommand(431000059, 431000059) # Viewport Solo Single 
        c4d.CallCommand(13038) # Frame Selected Elements
    
    elif c4d.IsCommandChecked(431000059):
        c4d.CallCommand(100004768, 100004768) # Select Children
        c4d.CallCommand(431000058) # turn off solo
        c4d.CallCommand(12288, 12288) # Frame All
    
    else:
        pass
    
    return


if __name__=='__main__':
    main()
