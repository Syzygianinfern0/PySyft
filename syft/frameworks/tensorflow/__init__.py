import syft

if syft.dependency_check.tensorflow_available:
    from syft_tensorflow.hook import TensorFlowHook

    setattr(syft, "TensorFlowHook", TensorFlowHook)
