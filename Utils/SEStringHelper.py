#-----------------------------------------------------------------------------
def SE_RemoveSuffix(str):
    edits = str.split('_')
    
    if len(edits) < 2:
        return str

    suffix = '_' + edits[-1]
    strNoSuffix = str[:-len(suffix)]

    return strNoSuffix
#-----------------------------------------------------------------------------
def getSuffix(str):
    edits = str.split('_')
    
    if len(edits) < 2:
        return None

    return edits[-1]
#-----------------------------------------------------------------------------
def SE_RemovePrefix(str):
    edits = str.split('_')
    
    if len(edits) < 2:
        return str

    prefix = edits[0] + '_'
    strNoPrefix = str[len(prefix):]

    return strNoPrefix
#-----------------------------------------------------------------------------