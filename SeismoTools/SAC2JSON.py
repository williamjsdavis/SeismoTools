from struct import unpack
import json

def SAC2JSON(filename_in, filename_out):
    body, metadata_small = get_data(filename_in)
    data = {
        'header' : metadata_small,
        'body' : body,
    }
    
    #new_filename = filename + '.json'
    with open(filename_out, 'w') as f:
        json.dump(data, f, indent=4)
        
def SAC3JSON(filenames_in, filename_out):
    assert len(filenames_in) == 3
    body0, metadata0_small = get_data(filenames_in[0])
    body1, metadata1_small = get_data(filenames_in[1])
    body2, metadata2_small = get_data(filenames_in[2])
    
    body = {
        'body0' : {
            'component' : metadata0_small.pop('component'),
            'body' : body0,
        },
        'body1' : {
            'component' : metadata1_small.pop('component'),
            'body' : body1,
        },
        'body2' : {
            'component' : metadata2_small.pop('component'),
            'body' : body2,
        },
    }
    
    data = {
        'header' : metadata0_small,
        'body' : body
    }
    
    with open(filename_out, 'w') as f:
        json.dump(data, f, indent=4)

def get_data(filename):
    with open(filename, mode='rb') as f:
        filecontent = f.read()
    
    # Number of words in header
    header1_nwords = 70 # 4 bytes each
    header2_nwords = 40 # 4 bytes each
    header3_nwords = 24 # 8 bytes each

    # Byte locations
    i = 4 * header1_nwords
    j = i + (4 * header2_nwords)
    k = j + (8 * header3_nwords)
    iend = len(filecontent)

    # Number of words in body
    body_nwords = (iend - k) // 4

    # Unpack
    header1 = unpack("f" * header1_nwords, filecontent[:i])
    header2 = unpack("i" * header2_nwords, filecontent[i:j])
    header3 = unpack("8s" * header3_nwords, filecontent[j:k])
    body = unpack("f" * body_nwords, filecontent[k:iend])
    metadata_small = {
        'network name' : header3[21].decode("utf-8").strip(),
        'station name' : header3[0].decode("utf-8").strip(),
        'component' : header3[20].decode("utf-8").strip(),
        'year' : header2[0],
        'day' : header2[1],
        'hour' : header2[2],
        'minute' : header2[3],
        'second' : header2[4],
        'millisecond' : header2[5],
        'delta t' : header1[0],
        'no. points' : header2[9],
        'station lat.' : header1[31],
        'station lon.' : header1[32],
        'station az.' : header1[57],
        'station inc.' : header1[58],
    }
    return body, metadata_small

if __name__ == "__main__":
    import sys

    filename = str(sys.argv[1])

    new_filename = filename.replace('.','_') + ".json"
    
    SAC2JSON(filename, new_filename)
    print("Success!")
