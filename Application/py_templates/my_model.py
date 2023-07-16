import os
import torch
from torchvision import transforms
from PIL import Image
import numpy as np




model_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'py_templates/Models/data/model.pth')

image_path=os.path.dirname(os.path.dirname(__file__))


device = torch.device('cpu')
model = torch.load(model_path, map_location=device)
model.eval()

#image -> tensor
    
transform = transforms.Compose([transforms.Resize((150,150)),
                                     transforms.ToTensor(),
                                     transforms.Normalize(mean = [0.5175, 0.4244, 0.4595], std= [0.3344, 0.2769, 0.2959]),
                                     ])
    

#predict
def get_prediction(url):
    #images = image_tensor.reshape(-1, 150*150)
    new_url = image_path+url
    image = Image.open(new_url)
    image = image.convert(mode='RGB')
    image = transform(image)
    image = image.unsqueeze(0)
    outputs = model(image)
    #print(outputs)
    #outputs = outputs.detach().numpy()
    #outputs = np.argmax(outputs)
    #return outputs
    _, predicted = torch.max(outputs.data, 1)
    return predicted




