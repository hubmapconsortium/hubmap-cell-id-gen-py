

def get_sequencing_cell_id(dataset_uuid:str, barcode:str)->str:
    """Takes a dataset uuid and a barcode of a cell within that dataset to produce a unique cell ID"""
    return "-".join([dataset_uuid, barcode])

def get_spatial_cell_id(dataset_uuid:str, tile_id:str, mask_index:int)->str:
    """Takes a dataset uuid, a tile_id within that dataset, and a mask_index number within that tile to prodduce a unique cell ID"""
    return "-".join([dataset_uuid, tile_id, str(mask_index)])