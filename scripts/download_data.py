import squidpy as sq
import os

def load_spatial_data(dataset_name="visium_hne_adata"):
    """
    :param dataset_name: squidpy.datasets 
    :return: anndata object
    default is "visium_hne_adata", which is a human breast cancer dataset from 10x Genomics Visium platform.
    """
    print(f"Downloading squidpy dataset: {dataset_name} ...")

    # get the dataset function from squidpy.datasets and call it to get the AnnData object
    try:
        data_func = getattr(sq.datasets, dataset_name)
        adata = data_func()

        print(f"Success")
        print(f"Data shape: {adata.shape[0]} spots, {adata.shape[1]} genes")
        return adata
        
    except AttributeError:
        print(f"Error: Dataset '{dataset_name}' not found in squidpy.datasets.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    target_dataset = "visium_hne_adata"
    load_spatial_data(target_dataset)