#!/usr/bin/env python3
"""
Test script for the PosterAgent functionality
"""

from agents import PosterAgent
import json

def test_poster_agent():
    """Test the PosterAgent class functionality"""

    # Initialize the agent
    poster_agent = PosterAgent()

    # Test data - sample campaign data
    campaign_data = {
        "Campaign Name": "AI Ad Optimization Test",
        "Product/Service Description": "AI-powered ad optimization platform",
        "USPs": "Automated testing, higher CTR, time savings",
        "Objective": "Lead Generation",
        "Platforms": ["Facebook", "Google Ads"]
    }

    # Sample top variations
    top_variations = [
        {
            "id": "ADC-001",
            "headline": "Transform Your Ad Performance",
            "body": "Stop manual testing. Our AI creates 50 variations automatically for better results.",
            "cta": "Start Optimizing Now"
        }
    ]

    # Sample insights
    insights = {
        "key_findings": [
            "Pain-point headlines outperform by 47%",
            "Urgency CTAs drive higher conversions",
            "Facebook outperforms other platforms"
        ],
        "recommendations": [
            "Allocate more budget to top variations",
            "Retire bottom performers",
            "Generate new hybrid variations"
        ]
    }

    print("Testing PosterAgent functionality...")
    print("=" * 50)

    # Test 1: Prompt generation
    print("Test 1: Prompt generation")
    try:
        prompt = poster_agent.generate_poster_prompt(campaign_data, top_variations, insights)
        print("✓ Prompt generated successfully")
        print(f"Prompt length: {len(prompt)} characters")
        print(f"First 200 characters: {prompt[:200]}...")
    except Exception as e:
        print(f"✗ Prompt generation failed: {e}")
        return False

    # Test 2: Poster generation (this will make actual API call)
    print("\nTest 2: Poster generation (API call)")
    try:
        result = poster_agent.generate_poster(campaign_data, top_variations, insights)
        if result.get('success'):
            print("✓ Poster generated successfully")
            print(f"Image URL: {result.get('image_url')}")
            print(f"Generated at: {result.get('generated_at')}")
        else:
            print(f"✗ Poster generation failed: {result.get('error')}")
            print(f"Prompt used: {result.get('prompt_used')[:100]}...")
    except Exception as e:
        print(f"✗ Poster generation exception: {e}")
        return False

    # Test 3: Error handling - missing data
    print("\nTest 3: Error handling - missing data")
    try:
        result = poster_agent.generate_poster({}, [], {})
        if not result.get('success'):
            print("✓ Error handling works correctly for missing data")
        else:
            print("✗ Error handling failed - should have failed with empty data")
    except Exception as e:
        print(f"✗ Unexpected exception in error handling: {e}")

    print("\n" + "=" * 50)
    print("PosterAgent testing completed!")
    return True

if __name__ == "__main__":
    test_poster_agent()
