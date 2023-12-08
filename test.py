import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torch.autograd import Variable
from network import C3D_model
from dataloaders.dataset import VideoDataset

model = C3D_model.C3D(num_classes=101, pretrained=False)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.load_state_dict(torch.load('/workspace/pytorch-video-recognition/pretrained/c3d-pretrained.pth'))
train_dataloader = DataLoader(VideoDataset(dataset='ucf101', split='train',clip_len=16), batch_size=20, shuffle=True, num_workers=0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
running_corrects = 0.0
model = model.to(device)
model.eval()
for inputs, labels in train_dataloader:
    inputs = Variable(inputs, requires_grad=True).to(device)
    labels = Variable(labels).to(device)
    with torch.no_grad():
        outputs = model(inputs)
    probs = nn.Softmax(dim=1)(outputs)
    preds = torch.max(probs, 1)[1]
    running_corrects += torch.sum(preds == labels.data)
epoch_acc = running_corrects.double() / len(train_dataloader.dataset)
print('Acc :', epoch_acc)
