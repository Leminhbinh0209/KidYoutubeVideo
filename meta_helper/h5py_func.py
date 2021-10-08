import os
import h5py
from tqdm import tqdm
def save_dict(data_dict, filename):
    """
    Implemetation of Two-level dictionary wrting
    """
    f = h5py.File(filename, 'w')
    for grp_name in data_dict:
        grp = f.create_group(grp_name)
        for dset_name in data_dict[grp_name]:
            dset = grp.create_dataset(dset_name, data = data_dict[grp_name][dset_name])
    f.close()
    print(f"Successfully saved to {filename}")

def read_dict(filename, intance_keys):
    """
    Two-level dictionary reading from h5py 
        {
            key1: {
                intance_keys[0]: data,
                intance_keys[1]: data,
                ...}
        ...}
    output:
        data-frame style dictionary
    """
    # Create an empty datadiction 
    data_dict = dict({'video_id': []})
    for k in intance_keys:
        data_dict[k] = []

    f = h5py.File(filename, 'r')
    list_keys = f.keys()
    for grp_name in tqdm(list_keys):
        # data_dict[grp_name] = dict()
        data_dict['video_id'].append(grp_name)
        for dset_name in intance_keys:
            if dset_name != 'y':
                data_dict[dset_name].append(f[grp_name][dset_name][:]) 
            else:
                data_dict[dset_name].append(f[grp_name][dset_name][()])
    f.close()
    return data_dict
