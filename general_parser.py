def raw_data_parse(file_dir, delimiter, line_stride, delete_line):
    raw = open(file_dir, 'r')
    raw_str_list = raw.read().split('\n')
    delete_line.sort()
    delete_line.reverse()
    for i in delete_line:
        del raw_str_list[i]
    while raw_str_list[-1] == '':
        del raw_str_list[-1]
    data_str_list = [ [] for _ in range(line_stride) ]
    for i in range(len(raw_str_list)):
        data_str_list[i%line_stride].append(raw_str_list[i])
    data_list = [ [] for _ in range(line_stride) ]
    for i in range(line_stride):
        data_str_mat = data_str_list[i]
        for line in data_str_mat:
            local = line.split(delimiter)
            while local[-1] == '':
                del local[-1]
            for j in range(len(local)):
                local[j] = float(local[j])
            data_list[i].append(local)
    return data_list