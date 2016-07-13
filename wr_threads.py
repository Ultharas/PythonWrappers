from wr_common import w,o
from threading import Thread
import threading
import itertools

def th_template(input_list, th_method_name):    
    full_result_dict_list = [] 
    while len(input_list) != 0:
        result_dict_list = [[]] * ThreadsNumber
        unknown_city_dict_list = [[]] * ThreadsNumber

        delay = 0

        urls = input_list[:ThreadsNumber]
        del input_list[:ThreadsNumber]

        threadlist = []

        WriteIndex = 0
        
        for u in urls:
            t = Thread(target=th_method_name, args=(u, delay, WriteIndex, result_dict_list))
            t.start()
            threadlist.append(t)   
            delay += DelayIncreaseLevel
            WriteIndex += 1

        for b in threadlist:
            b.join()  
            
        result_dict_list = [x for x in result_dict_list if x]
        full_result_dict_list += list(itertools.chain(*result_dict_list))

        Print('left in input_list', len(input_list))

    return full_result_dict_list

def get_this(field_dict_list_name, single=False, multi=False, mod='r'):

    if any((single, multi)):

        if single:
            field_dict_list = single
        elif multi:
            th_list, th_method = multi
            field_dict_list = th_template(th_list, th_method)

    if 'w' in mod:
        field_dict_list = json.dumps(field_dict_list)
        w(field_dict_list_name, field_dict_list)

    if 'r' in mod:
        field_dict_list = json.loads(o(field_dict_list_name))
        Print(field_dict_list_name, len(field_dict_list)) 

    return field_dict_list