
from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co


class MyData(Dataset):

    def __getitem__(self, index):
        print(1)
        return 2

    def __init__(self) -> None:
        print(2)
        super().__init__()

    def __len__(self):
        print(3)
        pass



obj = MyData()
obj[1]

pass