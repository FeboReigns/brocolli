import torch
import torch.nn.functional as F
import pytest
import warnings

from brocolli.testing.common_utils import OnnxBaseTester as Tester


class TestNormalizationClass:
    def test_L2Norm(
        self,
        request,
        shape=(1, 3, 32, 32),
    ):
        class L2Norm(torch.nn.Module):
            def __init__(
                self,
            ):
                super(L2Norm, self).__init__()

            def forward(self, x):
                return F.normalize(x, p=2, dim=1)

        model = L2Norm()
        x = torch.rand(shape)
        Tester(request.node.name, model, x)

    def test_Layernorm(
        self,
        request,
        shape=(20, 5, 10),
    ):
        class LayerNorm(torch.nn.Module):
            def __init__(
                self,
            ):
                super(LayerNorm, self).__init__()
                self.layer_norm = torch.nn.LayerNorm(10)

            def forward(self, x):
                return self.layer_norm(x)

        model = LayerNorm()
        x = torch.rand(shape)
        Tester(request.node.name, model, x)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    pytest.main(
        [
            "-p",
            "no:warnings",
            "-v",
            "test/converter/op_test/onnx/normalization/test_normalization.py",
        ]
    )
