import torchvision.transforms as T
import torch
from zjwocr.model import LightCNN
from zjwocr.img_utils import to_rgb, loadimg
from zjwocr.model_utils import credit_customs_gov_cn_label_map, credit_customs_gov_cn_num
from zjwocr.user_utils import is_user_data_type, is_user_model


DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = LightCNN(output=len(credit_customs_gov_cn_label_map) * credit_customs_gov_cn_num)
if torch.cuda.is_available():
    model = model.to(DEVICE)
    model.load_state_dict(torch.load("./models/credit_customs_gov_cn.model"))
    model.eval()
else:
    model = model.to(DEVICE)
    model.load_state_dict(torch.load("./models/credit_customs_gov_cn.model", map_location=DEVICE))
    model.eval()


def ocr_api(data):
    """
    :param data: data = {'图片': '','网站': '中国海关企业进出口信用信息公示平台'}
    :return: 返回值：识别出的数字或者英文字母
    """
    data = is_user_data_type(data)
    data = is_user_model(data)
    binary = data["图片"]
    try:
        im = loadimg(binary, None)
        im = T.Compose([
            to_rgb,
            T.ToPILImage(),
            T.Resize((128, 128)),
            T.ToTensor(),
        ])(im)
        im = im.to(DEVICE)
        im = im.unsqueeze(0)
        result = model(im).view(credit_customs_gov_cn_num, len(credit_customs_gov_cn_label_map))
        predict = ''.join([credit_customs_gov_cn_label_map[i] for i in list(torch.argmax(result.cpu(), dim=1))])
    except:
        predict = ""
        raise TypeError('这是一个意外，报错。')
        
    return {"code": predict}





