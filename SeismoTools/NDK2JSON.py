import json

def NDK2JSON(filename_in, i, filename_out):
    
    filelines = get_NDK_lines(filename_in)
    n_events = len(filelines) // 5
    raw_events = [filelines[(j*5):((j*5)+5)] for j in range(n_events)]
    data = parse_lines(raw_events[i])
    
    with open(filename_out, 'w') as f:
        json.dump(data, f, indent=4)
    return data
        
def get_NDK_lines(filename_in):
    with open(filename_in, mode='r') as f:
        filecontent = f.read()
    filelines = filecontent.splitlines()
    return filelines

def parse_lines(raw_lines):
    data = {
        **parse_line1(raw_lines[0]),
        **parse_line2(raw_lines[1]),
        **parse_line3(raw_lines[2]),
        **parse_line4(raw_lines[3]),
        **parse_line5(raw_lines[4]),
    }
    return data

def irange(istart, iend):
    return slice(istart-1,iend)
def parse_line1(raw_line):
    data = {
        'hypocenter_reference_catalog' : raw_line[irange(1,4)],
        'date' : raw_line[irange(6,15)],
        'time' : raw_line[irange(17,26)],
        'latitude' : raw_line[irange(28,33)],
        'longitude' : raw_line[irange(35,41)],
        'depth' : raw_line[irange(43,47)],
        'magnitudes' : raw_line[irange(49,55)],
        'location' : raw_line[irange(57,80)],
    }
    return data
def parse_line2(raw_line):
    data = {
        'CMT_event_name' : raw_line[irange(1,16)],
        'inversion_info' : parse_inversion_info(raw_line[irange(18,61)]),
        'inversion_source_type' : raw_line[irange(63,68)],
        'moment_rate_function' : parse_inversion_source_type(raw_line[irange(70,80)]),
    }
    return data
def parse_line3(raw_line):
    data = {
        'centroid_parameters' : raw_line[irange(1,58)],
        'depth_type' : raw_line[irange(60,63)],
        'timestamp' : raw_line[irange(66,80)],
    }
    return data
def parse_line4(raw_line):
    data = {
        'CMT_exponent' : raw_line[irange(1,2)],
        'moment_tensor' : raw_line[irange(3,80)],
    }
    return data
def parse_line5(raw_line):
    data = {
        'code_version' : raw_line[irange(1,3)],
        'moment_tensor_principal_axis' : raw_line[irange(4,48)],
        'scalar_moment' : raw_line[irange(50,56)],
        'sdr_1st_nodal_plane_dc' : raw_line[irange(58,80)],
    }
    return data

def parse_inversion_info(raw_line_string):
    data = {
        'B_data' : parse_inversion_info_B(raw_line_string),
        'S_data' : parse_inversion_info_S(raw_line_string),
        'M_data' : parse_inversion_info_M(raw_line_string),
    }
    return data
def parse_inversion_info_B(raw_line_string):
    if 'B:' in raw_line_string:
        istart = raw_line_string.find('B:') + 2
        iend = raw_line_string.find('S')
        B_string = raw_line_string[istart:iend]
        B_string_split = B_string.split()
        n_stations = B_string_split[0]
        n_components = B_string_split[1]
        shortest_period = B_string_split[2]
    else:
        n_stations = ''
        n_components = ''
        shortest_period = ''
    data = {
        'n_stations' : n_stations,
        'n_components' : n_components,
        'shortest_period' : shortest_period,
    }
    return data
def parse_inversion_info_S(raw_line_string):
    if 'S:' in raw_line_string:
        istart = raw_line_string.find('S:') + 2
        iend = raw_line_string.find('M')
        S_string = raw_line_string[istart:iend]
        S_string_split = S_string.split()
        n_stations = S_string_split[0]
        n_components = S_string_split[1]
        shortest_period = S_string_split[2]
    else:
        n_stations = ''
        n_components = ''
        shortest_period = ''
    data = {
        'n_stations' : n_stations,
        'n_components' : n_components,
        'shortest_period' : shortest_period,
    }
    return data
def parse_inversion_info_M(raw_line_string):
    if 'M:' in raw_line_string:
        istart = raw_line_string.find('M:') + 2
        iend = len(raw_line_string)
        M_string = raw_line_string[istart:iend]
        M_string_split = M_string.split()
        n_stations = M_string_split[0]
        n_components = M_string_split[1]
        shortest_period = M_string_split[2]
    else:
        n_stations = ''
        n_components = ''
        shortest_period = ''
    data = {
        'n_stations' : n_stations,
        'n_components' : n_components,
        'shortest_period' : shortest_period,
    }
    return data
def parse_inversion_source_type(raw_line_string):
    colon_loc = raw_line_string.find(':')
    type_string = raw_line_string[0:colon_loc]
    value_string = raw_line_string[(colon_loc+1):len(raw_line_string)]
    data = {
        'type' : type_string,
        'value' : value_string,
    }
    return data

