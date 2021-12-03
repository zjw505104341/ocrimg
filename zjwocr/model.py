# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/3 14:39
import torch

class CNNBlock(torch.nn.Module):
    def __init__(self, in_features, out_features, kernel, strides):
        super(CNNBlock, self).__init__()
        self.conv = torch.nn.Conv2d(in_features, out_features, kernel, strides[0])
        self.bn = torch.nn.BatchNorm2d(out_features, momentum=0.9)
        self.relu = torch.nn.LeakyReLU(0.01)
        self.pool = torch.nn.MaxPool2d(2, strides[1])

        torch.nn.init.xavier_uniform_(self.conv.weight, gain=1)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        x = self.pool(x)

        return x


class LightCNN(torch.nn.Module):

    def __init__(self, image_shape=(128, 128), output=100):
        super(LightCNN, self).__init__()
        self.image_shape = image_shape

        self.cnn = torch.nn.Sequential(
            CNNBlock(3, 32, 7, (1, 1)),
            CNNBlock(32, 64, 5, (1, 2)),
            CNNBlock(64, 128, 3, (1, 2)),
            CNNBlock(128, 128, 3, (1, 2)),
            CNNBlock(128, 64, 3, (1, 2))
        )

        self.linear = torch.nn.Sequential(
            torch.nn.Linear(self._cal_shape(), output)
        )

    def _cal_shape(self):
        x = torch.zeros((1, 3) + self.image_shape)
        return self.cnn(x).flatten().shape[0]

    def forward(self, x):
        batch_size = x.shape[0]

        x = self.cnn(x)
        x = x.view(batch_size, -1)
        x = self.linear(x)
        return x
