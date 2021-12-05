import os

import numpy
import torch, io
from PIL import Image

# fake data
from model import LightCNN
from model_utils import credit_customs_gov_cn_label_map, credit_customs_gov_cn_num

# DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model = LightCNN(output=len(credit_customs_gov_cn_label_map) * credit_customs_gov_cn_num)
# model = model.to(DEVICE)
# model.load_state_dict(torch.load("../models/credit_customs_gov_cn.onnx"))
# model.eval()


# model.save(net1.state_dict(), 'net_params.pkl')

# print(model)


import onnxruntime as ort
__graph_path = os.path.join(os.path.dirname(__file__), 'credit_customs_gov_cn.onnx')
ort_session = ort.InferenceSession(__graph_path, providers=[
                ('CUDAExecutionProvider', {
                    'device_id': 0,
                    'arena_extend_strategy': 'kNextPowerOfTwo',
                    'cuda_mem_limit': 2 * 1024 * 1024 * 1024,
                    'cudnn_conv_algo_search': 'EXHAUSTIVE',
                    'do_copy_in_default_stream': True,
                }),
            ])

# outputs = ort_session.run(None,{"actual_input_1": np.random.randn(10, 3, 224, 224).astype(numpy.float32)},)
# print(outputs[0])
