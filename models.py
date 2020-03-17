import os
from pathlib import Path
import pandas as pd

class TrackfieldModel():
    def __init__(self, dir, actif_id=0):
        super().__init__()
        self.set_paths(dir)
        self.load(actif_id)

    def set_paths(self, dir):
        self.paths = []
        for dp, dns, fns in os.walk(dir):
            for fn in fns:
                path = Path('%s/%s'%(dp, fn))
                if path.suffix == '.csv':
                    self.paths.append(Path('%s/%s'%(dp, fn)))
    def get_path(self, id):
        return self.paths[id]

    def load(self, id):
        self.actif = pd.read_csv(self.get_path(0))


def get_first_of_each(tfm, by, filter): # .loc[1].at[filter]
    return [(name) for name, group in tfm.actif.groupby(by)]
