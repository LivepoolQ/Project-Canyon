from qpid.constant import INPUT_TYPES
from qpid.model import Model, layers
from qpid.training import Structure

from .__args import KayakArgs

import torch


class KayakModel(Model):
    def __init__(self, structure=None, *args, **kwargs):
        super().__init__(structure, *args, **kwargs)

        # Init args
        self.args._set_default('K', 1)
        self.args._set_default('K_train', 1)
        self.kk_args = self.args.register_subargs(
            KayakArgs, 'kk_args')
        self.k = self.kk_args
        
        # Set model inputs
        self.set_inputs(INPUT_TYPES.OBSERVED_TRAJ,
                        INPUT_TYPES.NEIGHBOR_TRAJ)
        
        # MLP network
        self.direct_pred = layers.Dense(self.args.obs_frames * self.dim,
                                        self.args.pred_frames * self.dim * self.k.generation_num)
        
    def forward(self, inputs, training=None, mask=None, *args, **kwargs):
        # --------------------
        # MARK: - Preprocesses
        # --------------------
        x_ego = self.get_input(inputs, INPUT_TYPES.OBSERVED_TRAJ)
        x_nei = self.get_input(inputs, INPUT_TYPES.NEIGHBOR_TRAJ)

        # ----------------
        # MARK: - Backbone
        # ----------------
        Y = self.direct_pred(torch.reshape(x_ego, [-1, self.args.obs_frames * self.dim]))
        Y = torch.reshape(Y, [-1, self.k.generation_num, self.args.pred_frames, self.dim])

        return Y
    
    
class Kayak(Structure):
    MODEL_TYPE = KayakModel
