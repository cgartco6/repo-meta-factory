import pytest
from canvas import AssetLayoutPipelineOptimizer

def test_canvas_optimizer_valid_cropping():
    optimizer = AssetLayoutPipelineOptimizer()
    # Mocking standard cloud asset url response
    mock_url = "https://replicate.delivery"
    
    result = optimizer.resize_and_crop_to_spec(mock_url, "16:9")
    
    assert result["source_asset_url"] == mock_url
    assert result["target_dimension_profile"] == "16:9"
    assert result["render_status"] == "PROCESSED_READY_FOR_HITL_GATEKEEPER"

def test_canvas_optimizer_invalid_ratio_fallback():
    optimizer = AssetLayoutPipelineOptimizer()
    mock_url = "https://replicate.delivery"
    
    # Passing an unsupported broken aspect ratio profile
    result = optimizer.resize_and_crop_to_spec(mock_url, "invalid_profile_dimensions")
    
    # Must fallback gracefully to baseline 1:1 format parameters
    assert result["target_dimension_profile"] == "1:1"
