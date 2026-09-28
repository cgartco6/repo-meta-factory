from ..canvas import AssetLayoutPipelineOptimizer

def test_canvas_dimension_processing_rules():
    pipeline = AssetLayoutPipelineOptimizer()
    res = pipeline.resize_and_crop_to_spec("https://mock.com", "16:9")
    assert res["dimension_profile"] == "16:9"
    assert res["status"] == "PROCESSED_READY_FOR_HITL"
