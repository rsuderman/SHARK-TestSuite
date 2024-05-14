# Copyright 2024 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import sys
import torch
import torch.nn as nn

# import from e2eshark/tools to allow running in current dir, for run through
# run.pl, commutils is symbolically linked to allow any rundir to work
sys.path.insert(0, "../../../tools/stubs")
from commonutils import E2ESHARK_CHECK_DEF

# Create an instance of it for this test
E2ESHARK_CHECK = dict(E2ESHARK_CHECK_DEF)

class op_gridsampler(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, g):
        interpolation_mode=0,
        padding_mode=0,
        align_corners=False,
        z = nn.functional.grid_sample(x, g, mode="bilinear", padding_mode="zeros", align_corners=False)
        return z

model = op_gridsampler()
# torch.manual_seed(42)
X = torch.rand(7, 8, 12, 4)
Y = torch.rand(7, 11, 13, 2)*2.0-1.0
Z = model(X, Y)

E2ESHARK_CHECK["input"] = [X, Y]
E2ESHARK_CHECK["output"] =  Z
print("Input:", X)
print("Grid:", Y)
print("Output:", Z)
