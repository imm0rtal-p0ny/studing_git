def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    result = []
    if lng * 2 == wdth:
        result.append(lng)
        result.append(lng)
    elif wdth * 2 == lng:
        result.append(wdth)
        result.append(wdth)
    elif lng < wdth:
        result.append(lng)
        wdth = wdth - lng
        result = result + sq_in_rect(lng, wdth)
    elif wdth < lng:
        result.append(wdth)
        lng = lng - wdth
        result = result + sq_in_rect(lng, wdth)
    return result

print(sq_in_rect(5, 3))
