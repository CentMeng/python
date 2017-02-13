# -*- coding: utf-8 -*-
from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

# StastModels来进行ADF平稳性检验
result = ADF(np.random.rand(100))
print(result)