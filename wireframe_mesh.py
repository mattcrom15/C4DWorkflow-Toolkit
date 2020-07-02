import c4d


##get selected object
objs = doc.GetOrderedActiveObjects()
#check  to see if display tag is enabled
for obj in objs:
    objtag =obj.GetTag(c4d.Tdisplay)
    
    ## if no tag
    if objtag == None:
    ## make tag
        tag = obj.MakeTag(c4d.Tdisplay)
        tag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE] = True
        tag[c4d.DISPLAYTAG_SDISPLAYMODE] = 6
    ## if tag and wireframe is enabled
    elif objtag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE] == True:
    ## disable wireframe
        objtag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE] = False
    
    else:
    ## enable wireframe
        objtag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE] = True
    
##add event
c4d.EventAdd()