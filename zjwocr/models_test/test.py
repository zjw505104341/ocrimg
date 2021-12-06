import os

import numpy
import torch, io
from PIL import Image

# fake data
from model import LightCNN
from model_utils import credit_customs_gov_cn_label_map, credit_customs_gov_cn_num

model = LightCNN(output=len(credit_customs_gov_cn_label_map) * credit_customs_gov_cn_num)
model.load_state_dict(torch.load("../models/credit_customs_gov_cn.model", map_location='cpu'))




# dummy_input1 = torch.randn(1, 3, 64, 64)
# input_names = ["actual_input_1"]
# output_names = ["output1"]
# # torch.onnx.export(model, (dummy_input1, dummy_input2, dummy_input3), "C3AE.onnx", verbose=True, input_names=input_names, output_names=output_names)
# torch.onnx.export(model, dummy_input1, "C3AE_emotion.onnx", verbose=True, input_names=input_names,
#                   output_names=output_names)




