import sysimport pyodbc#Variable Definitions cnstring = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\DB.accdb;"cfgname = ''#Devo is awesome//this defines reading data from filesdef readin(filenames):    ret = {}    chunk = {}    chunknum = 0    for filename in filenames:        with open(filename, 'r') as cfgfile:            for line in cfgfile:                line = line.strip()                if not line or line.startswith('#') or line.startswith('define'): continue                if line.startswith('}'):                    ret[chunknum] = chunk                    chunknum += 1                    chunk = {}                    continue                bits = line.split(None, 1)                if len(bits) > 1:                    k, v = bits                    chunk[k] = v    return ret 