def SE_RemoveSuffix(str):
    edits = str.split('_')
    
    if len(edits) < 2:
        return str

    suffix = '_' + edits[-1]
    strNoSuffix = str[:-len(suffix)]

    return strNoSuffix
