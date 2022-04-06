### Step-1 Import Libraries required
import torch as T
import torch.nn as nn
import torch.nn.functional as F # relu, tanh
import torch.optim as optim

from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms
