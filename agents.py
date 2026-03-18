from openai import OpenAI
from config import OPENAI_API_KEY
import json
import random
import time
import requests
import os

client = OpenAI(api_key=OPENAI_API_KEY)

class ResearchAgent:
    def __init__(self):
        pass

    def generate_intelligence_report(self, campaign_data, audience_data):
        # Simulate AI response for demo
        report = {
            "micro_personas": ["Persona 1: Tech-savvy entrepreneur, motivated by efficiency, pain point: time waste"],
            "keywords": ["AI testing", "ad optimization", "CTR improvement"],
            "competitive_analysis": "Competitors focus on manual testing; opportunity for automation",
            "platform_recommendations": "Use Facebook for targeting, Google for search",
            "emotional_triggers": "Relief from manual work, aspiration for better results",
            "sentiment_summary": "Positive towards automation, frustrated with manual processes"
        }
        return report

class CreativeAgent:
    def __init__(self):
        pass

    def generate_ad_variations(self, intelligence_report, campaign_data, num_variations=20):
        platforms = campaign_data.get("Platforms", ["Facebook"])
        product = campaign_data.get("Product/Service Description", "AI-powered ad optimization tool")
        usps = campaign_data.get("USPs", "Automated testing, higher CTR, time savings")
        tone = campaign_data.get("Tone", "Professional")

        prompt = f"""
        As a Creative Agent, generate {num_variations} unique ad copy variations for a campaign about: {product}

        Key selling points: {usps}
        Tone: {tone}
        Platforms to target: {platforms}
        Intelligence insights: {intelligence_report}

        Create realistic ad copy variations. For each variation:
        - Use a unique ID like ADC-001, ADC-002, etc.
        - Assign to one of the platforms: {platforms}
        - Create compelling headlines (25-50 characters)
        - Write engaging body copy (100-150 characters)
        - Add strong CTAs
        - Specify what element is being tested (Headline, Body, CTA, etc.)
        - Choose emotional trigger (Relief, Aspiration, Urgency, Fear, Trust, etc.)
        - Give confidence score (80-95)

        Output ONLY a valid JSON array with no additional text. Format:
        [
          {{
            "id": "ADC-001",
            "platform": "Facebook",
            "headline": "Transform Your Ad Performance",
            "body": "Stop manual testing. Our AI creates 50 variations automatically for better results.",
            "cta": "Start Optimizing Now",
            "testing_element": "Headline",
            "emotional_trigger": "Aspiration",
            "confidence_score": 92
          }},
          ...
        ]
        """
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative ad copy generator. Generate realistic ad copy variations based on the provided data."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            content = response.choices[0].message.content
            # Try to parse JSON
            try:
                variations = json.loads(content.strip('```json\n').strip('```'))
            except json.JSONDecodeError:
                # If not JSON, try to extract from text
                variations = self.parse_variations_from_text(content, num_variations, campaign_data.get("Platforms", ["Facebook"]))
        except Exception as e:
            print(f"OpenAI API error: {e}")
            variations = self.generate_fallback_variations(num_variations, campaign_data.get("Platforms", ["Facebook"]))
        return variations

    def parse_variations_from_text(self, text, num_variations, platforms):
        # Simple parsing for demo - in real implementation, use better NLP
        variations = []
        for i in range(1, num_variations + 1):
            platform = platforms[i % len(platforms)] if platforms else "Facebook"
            variations.append({
                "id": f"ADC-{i:03d}",
                "platform": platform,
                "headline": f"Transform Your Ad Performance with AI",
                "body": f"Stop wasting time on manual testing. Our AI generates {num_variations} variations automatically.",
                "cta": "Start Optimizing Now",
                "testing_element": "Headline",
                "emotional_trigger": "Aspiration",
                "confidence_score": random.randint(80, 95)
            })
        return variations

    def generate_fallback_variations(self, num_variations, platforms):
        # Use campaign data if available
        campaign_data = getattr(self, 'campaign_data', {})
        product = campaign_data.get("Product/Service Description", "AI-powered ad optimization tool")
        usps = campaign_data.get("USPs", "Automated testing, higher CTR, time savings").split(", ")
        tone = campaign_data.get("Tone", "Professional")

        headlines = [
            f"Transform Your {product} Results Today",
            f"Stop Manual Work: Automate {product}",
            f"Boost Performance with Smart {product}",
            f"Discover the Future of {product} Optimization",
            f"Scale Your {product} Success Instantly",
            f"Unlock Hidden Potential in {product}",
            f"Revolutionize Your {product} Strategy",
            f"Maximize ROI with Advanced {product}",
            f"Streamline Your {product} Workflow",
            f"Accelerate Growth with {product} AI",
            f"Dominate the Market with {product}",
            f"Simplify Complex {product} Tasks",
            f"Enhance Efficiency in {product}",
            f"Break Through {product} Limitations",
            f"Empower Your {product} Decisions",
            f"Optimize Everything with {product}",
            f"Future-Proof Your {product} Approach",
            f"Master {product} Performance Metrics",
            f"Elevate Your {product} Game",
            f"Conquer {product} Challenges Easily"
        ]

        bodies = [
            f"Experience the power of automated {product} that handles {num_variations} variations simultaneously. Save time and boost results.",
            f"Our intelligent {product} system analyzes data in real-time to optimize your campaigns automatically.",
            f"Say goodbye to manual testing. Our {product} creates diverse variations for maximum impact.",
            f"Harness the potential of AI-driven {product} to achieve unprecedented performance improvements.",
            f"Streamline your workflow with {product} that adapts and learns from every campaign iteration.",
            f"Unlock new levels of efficiency with {product} designed for modern marketing challenges.",
            f"Transform your approach to {product} with cutting-edge automation and intelligent insights.",
            f"Scale your success with {product} that delivers consistent, measurable improvements.",
            f"Experience the difference with {product} that combines speed, accuracy, and innovation.",
            f"Take control of your {product} destiny with tools that work smarter, not harder.",
            f"Discover the competitive edge with {product} that stays ahead of market trends.",
            f"Simplify complexity with {product} that makes advanced optimization accessible.",
            f"Maximize your potential with {product} that learns and adapts to your unique needs.",
            f"Break free from limitations with {product} that pushes the boundaries of what's possible.",
            f"Empower your strategy with {product} that provides actionable insights instantly.",
            f"Optimize every aspect with {product} that covers all bases comprehensively.",
            f"Future-proof your campaigns with {product} built for tomorrow's challenges.",
            f"Master performance metrics with {product} that provides deep analytical capabilities.",
            f"Elevate your results with {product} that consistently delivers exceptional outcomes.",
            f"Conquer any challenge with {product} that provides reliable, proven solutions."
        ]

        ctas = [
            "Start Optimizing Now",
            "Get Started Today",
            "Try It Free",
            "Learn More",
            "See Results",
            "Boost Performance",
            "Scale Up",
            "Discover Now",
            "Transform Today",
            "Accelerate Growth",
            "Maximize ROI",
            "Unlock Potential",
            "Experience Power",
            "Take Control",
            "Break Through",
            "Empower Success",
            "Optimize Everything",
            "Future-Proof Now",
            "Master Performance",
            "Conquer Challenges"
        ]

        testing_elements = ["Headline", "Body", "CTA", "Tone", "Length", "Structure"]
        emotional_triggers = ["Aspiration", "Relief", "Urgency", "Trust", "Fear", "Excitement", "Curiosity", "Authority"]

        variations = []
        for i in range(1, num_variations + 1):
            platform = platforms[(i-1) % len(platforms)] if platforms else "Facebook"
            usp = usps[(i-1) % len(usps)] if usps else "automation"

            variation = {
                "id": f"ADC-{i:03d}",
                "platform": platform,
                "headline": headlines[(i-1) % len(headlines)],
                "body": bodies[(i-1) % len(bodies)],
                "cta": ctas[(i-1) % len(ctas)],
                "testing_element": testing_elements[(i-1) % len(testing_elements)],
                "emotional_trigger": emotional_triggers[(i-1) % len(emotional_triggers)],
                "confidence_score": random.randint(80, 95)
            }
            variations.append(variation)
        return variations

class DeploymentAgent:
    def __init__(self):
        pass

    def deploy_campaign(self, variations, platforms):
        # Simulate deployment
        manifest = {
            "campaign_ids": {platform: f"CAMP-{platform.upper()}-{random.randint(1000,9999)}" for platform in platforms},
            "variation_ids": [v["id"] for v in variations],
            "tracking_params": "UTM codes set",
            "budget_allocation": "Equal split initially",
            "launch_status": "Launched",
            "api_status": "Connected"
        }
        return manifest

class MonitoringAgent:
    def __init__(self):
        pass

    def monitor_performance(self, variations, duration_hours=72):
        # Simulate monitoring
        performance_data = []
        for v in variations:
            metrics = {
                "variation_id": v["id"],
                "impressions": random.randint(1000, 10000),
                "clicks": random.randint(50, 500),
                "ctr": round(random.uniform(1.0, 5.0), 2),
                "cpc": round(random.uniform(0.5, 2.0), 2),
                "conversions": random.randint(5, 50),
                "conversion_rate": round(random.uniform(5.0, 20.0), 2),
                "engagement": random.randint(10, 100)
            }
            performance_data.append(metrics)
        return performance_data

class AnalysisAgent:
    def __init__(self):
        pass

    def analyze_performance(self, performance_data):
        # Simulate analysis
        top_performers = sorted(performance_data, key=lambda x: x["ctr"], reverse=True)[:5]
        insights = {
            "top_performers": top_performers,
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
        return insights

class OptimizationAgent:
    def __init__(self):
        pass

    def optimize_campaign(self, insights, variations):
        # Simulate optimization
        actions = {
            "budget_reallocations": "Increase budget for top 5 variations by 50%",
            "variation_status": "Pause bottom 5 variations",
            "new_variations": "Generate 10 new hybrid variations",
            "platform_adjustments": "Shift 25% budget to Facebook",
            "expected_impact": "Projected CTR +38%, CPC -22%"
        }
        return actions

class PosterAgent:
    def __init__(self):
        pass

    def generate_poster_prompt(self, campaign_data, top_variations, insights):
        """Generate a detailed prompt for DALL-E to create an advertisement poster"""
        campaign_name = campaign_data.get("Campaign Name", "AI Ad Optimization")
        product_desc = campaign_data.get("Product/Service Description", "AI-powered ad optimization tool")
        usps = campaign_data.get("USPs", "Automated testing, higher CTR, time savings")
        objective = campaign_data.get("Objective", "Lead Generation")
        platforms = campaign_data.get("Platforms", ["Facebook"])

        # Get top performing variation
        if top_variations:
            top_variation = top_variations[0]  # Assuming sorted by performance
            headline = top_variation.get("headline", "Transform Your Ad Performance")
            cta = top_variation.get("cta", "Start Optimizing Now")
        else:
            headline = "Transform Your Ad Performance"
            cta = "Start Optimizing Now"

        # Get key insights
        key_findings = insights.get("key_findings", ["AI-powered optimization", "Higher CTR", "Time savings"])
        recommendations = insights.get("recommendations", ["Automate your testing", "Scale performance"])

        # Craft detailed prompt for poster
        prompt = f"""
        Create a professional, eye-catching advertisement poster for: {campaign_name}

        Key elements to include:
        - Main headline: "{headline}"
        - Product: {product_desc}
        - Key benefits: {usps}
        - Call to action: "{cta}"
        - Campaign objective: {objective}
        - Target platforms: {', '.join(platforms)}

        Visual style:
        - Modern, clean design with gradient backgrounds
        - Professional color scheme (blues, purples, whites)
        - Include icons representing AI, optimization, growth, performance
        - Text should be bold and readable
        - Include subtle geometric patterns or tech-inspired elements
        - High contrast for visibility

        Layout:
        - Top: Eye-catching headline
        - Center: Key benefits and product description
        - Bottom: Strong call-to-action button
        - Include performance metrics or success indicators
        - Add subtle background elements representing data/analytics

        Make it look like a digital advertisement poster, professional and compelling, suitable for {', '.join(platforms)} platforms.
        """

        return prompt.strip()

    def generate_poster(self, campaign_data, top_variations, insights):
        """Generate poster using DALL-E API and download the image"""
        prompt = self.generate_poster_prompt(campaign_data, top_variations, insights)

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url

            # Download the image
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            image_data = image_response.content

            return {
                "success": True,
                "image_url": image_url,
                "image_data": image_data,
                "prompt_used": prompt,
                "generated_at": time.time()
            }
        except Exception as e:
            error_str = str(e)
            print(f"DALL-E API error: {error_str}")

            # Check for specific billing limit error
            if "billing_hard_limit_reached" in error_str or "billing hard limit" in error_str.lower():
                user_friendly_error = (
                    "Billing limit reached for DALL-E image generation. "
                    "Please check your OpenAI account billing settings and ensure you have sufficient credits. "
                    "You can also try using DALL-E 2 (which has lower costs) or contact OpenAI support for assistance."
                )
            else:
                user_friendly_error = f"Failed to generate poster: {error_str}"

            return {
                "success": False,
                "error": user_friendly_error,
                "prompt_used": prompt
            }
