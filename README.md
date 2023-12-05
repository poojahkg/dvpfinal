


# Zero-Shot Text-to-Video Generation: Leveraging Efficient Text-to-Image Synthesis for Dynamic and Context-Preserving Video Synthesis


## Setup

1. Set up Sol Working directory 

- Create an account to access ASU's super computer 
- Download Cisco Secure Client
- Establish VPN connection to using ```ssh <username>@sol.asu.edu``` in the terminal and type in your password. 
- Request for a GPU session to access the resources

2. Clone this repository and enter:

Login to the remote desktop and carry out these commands in the terminal.
``` shell
git clone https://github.com/Picsart-AI-Research/Text2Video-Zero.git
cd Text2Video-Zero/
```
2. Install requirements using Python 3.9 and CUDA
``` shell
virtualenv --system-site-packages -p python3.9 venv
source venv/bin/activate
pip install -r requirements.txt
pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio -f https://download.pytorch.org/whl/cu102/torch_stable.html
pip install setuptools==59.5.0

```




--- 



## Inference API


To run inferences create an instance of `Model` class use the script ```inference.py```

``` python
import torch
from model import Model

model = Model(device = "cuda", dtype = torch.float16)
```


This repository is an extention of the implementation of [Text2Video-Zero](https://arxiv.org/abs/2303.13439).
