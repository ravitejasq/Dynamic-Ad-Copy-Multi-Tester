import streamlit as st
import pandas as pd
import plotly.express as px
import time
import os
from agents import ResearchAgent, CreativeAgent, DeploymentAgent, MonitoringAgent, AnalysisAgent, OptimizationAgent, PosterAgent

# Initialize agents
research_agent = ResearchAgent()
creative_agent = CreativeAgent()
deployment_agent = DeploymentAgent()
monitoring_agent = MonitoringAgent()
analysis_agent = AnalysisAgent()
optimization_agent = OptimizationAgent()

# Page configuration
st.set_page_config(
    page_title="Dynamic Ad-Copy Multi-Tester",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ultra-modern, shocking UI with advanced effects and interactions
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-attachment: fixed;
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        color: white;
        padding: 4rem 3rem;
        border-radius: 25px;
        margin-bottom: 3rem;
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4), 0 0 0 1px rgba(255,255,255,0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: headerFloat 6s ease-in-out infinite;
        backdrop-filter: blur(20px);
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);
        animation: headerGlow 4s ease-in-out infinite alternate;
    }

    .main-header::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="stars" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.3)"/><circle cx="5" cy="15" r="0.5" fill="rgba(255,255,255,0.2)"/></pattern></defs><rect width="100" height="100" fill="url(%23stars)"/></svg>');
        opacity: 0.1;
        animation: twinkle 3s linear infinite;
    }

    @keyframes headerFloat {
        0%, 100% { transform: translateY(0px) rotateX(0deg); }
        25% { transform: translateY(-10px) rotateX(1deg); }
        50% { transform: translateY(-5px) rotateX(0deg); }
        75% { transform: translateY(-15px) rotateX(-1deg); }
    }

    @keyframes headerGlow {
        0% { opacity: 0.3; transform: scale(1); }
        100% { opacity: 0.6; transform: scale(1.1); }
    }

    @keyframes twinkle {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-20px); }
    }

    .step-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.95) 0%, rgba(248,249,255,0.9) 100%);
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.05), 0 0 0 1px rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(20px);
    }

    .step-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.15), transparent);
        transition: left 0.8s cubic-bezier(0.23, 1, 0.320, 1);
    }

    .step-card:hover::before {
        left: 100%;
    }

    .step-card:hover {
        transform: translateY(-12px) rotateX(3deg) scale(1.02);
        box-shadow: 0 25px 65px rgba(102, 126, 234, 0.25), 0 10px 25px rgba(0,0,0,0.1), 0 0 0 1px rgba(102, 126, 234, 0.2);
        border-color: rgba(102, 126, 234, 0.4);
    }

    .step-card h2 {
        color: #667eea;
        margin-bottom: 1.5rem;
        font-weight: 800;
        text-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
        position: relative;
    }

    .step-card h2::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 2px;
        animation: lineGrow 2s ease-out;
    }

    @keyframes lineGrow {
        0% { width: 0; }
        100% { width: 60px; }
    }

    .btn-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        color: white;
        border: none;
        padding: 18px 36px;
        border-radius: 15px;
        font-weight: 800;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5), 0 0 0 1px rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        backdrop-filter: blur(10px);
    }

    .btn-primary::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.6s cubic-bezier(0.23, 1, 0.320, 1);
    }

    .btn-primary:hover::before {
        left: 100%;
    }

    .btn-primary:hover {
        transform: translateY(-5px) scale(1.08);
        box-shadow: 0 20px 45px rgba(102, 126, 234, 0.7), 0 0 0 1px rgba(255,255,255,0.2);
        background: linear-gradient(135deg, #764ba2 0%, #f093fb 25%, #f5576c 50%, #4facfe 75%, #667eea 100%);
    }

    .btn-primary:active {
        transform: translateY(-2px) scale(1.05);
    }

    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 25%, #ff9a9e 50%, #fecfef 75%, #fa709a 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(245, 87, 108, 0.4), 0 0 0 1px rgba(255,255,255,0.1);
        transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(20px);
        animation: metricPulse 3s ease-in-out infinite;
    }

    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05), rgba(255,255,255,0.1));
        animation: metricRotate 8s linear infinite;
    }

    .metric-card::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: metricOrb 4s ease-in-out infinite alternate;
    }

    @keyframes metricPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 15px 35px rgba(245, 87, 108, 0.4); }
        50% { transform: scale(1.05); box-shadow: 0 20px 45px rgba(245, 87, 108, 0.6); }
    }

    @keyframes metricRotate {
        0% { transform: translate(-50%, -50%) rotate(0deg); }
        100% { transform: translate(-50%, -50%) rotate(360deg); }
    }

    @keyframes metricOrb {
        0% { opacity: 0.3; transform: translate(-50%, -50%) scale(0.8); }
        100% { opacity: 0.7; transform: translate(-50%, -50%) scale(1.2); }
    }

    .metric-card:hover {
        transform: scale(1.1) rotateY(10deg) translateY(-10px);
        box-shadow: 0 25px 65px rgba(245, 87, 108, 0.6), 0 0 0 1px rgba(255,255,255,0.2);
    }

    .sidebar-nav {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4), 0 0 0 1px rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(20px);
    }

    .sidebar-nav::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 50%, rgba(255,255,255,0.05) 100%);
        animation: navShimmer 5s linear infinite;
    }

    @keyframes navShimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    .nav-item {
        color: white;
        padding: 15px 20px;
        margin: 8px 0;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
        font-weight: 700;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(15px);
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }

    .nav-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.6s cubic-bezier(0.23, 1, 0.320, 1);
    }

    .nav-item:hover::before {
        left: 100%;
    }

    .nav-item:hover {
        background: rgba(255,255,255,0.3);
        transform: translateX(10px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255,255,255,0.3), 0 0 0 1px rgba(255,255,255,0.2);
    }

    .nav-item.active {
        background: rgba(255,255,255,0.4);
        font-weight: 800;
        box-shadow: 0 8px 25px rgba(255,255,255,0.4), 0 0 0 1px rgba(255,255,255,0.3);
        transform: translateX(8px) scale(1.03);
        animation: activePulse 2s ease-in-out infinite;
    }

    @keyframes activePulse {
        0%, 100% { box-shadow: 0 8px 25px rgba(255,255,255,0.4); }
        50% { box-shadow: 0 12px 35px rgba(255,255,255,0.6); }
    }

    .progress-container {
        margin: 2rem 0;
        position: relative;
    }

    .progress-label {
        color: white;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }

    .progress-bar {
        width: 100%;
        height: 12px;
        background: rgba(255,255,255,0.2);
        border-radius: 6px;
        overflow: hidden;
        position: relative;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #ffffff 0%, rgba(255,255,255,0.9) 50%, #ffffff 100%);
        border-radius: 6px;
        transition: width 1s cubic-bezier(0.23, 1, 0.320, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(255,255,255,0.5);
    }

    .progress-fill::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
        animation: progressShine 2s linear infinite;
    }

    @keyframes progressShine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
</style>
""", unsafe_allow_html=True)

# Initialize agents
poster_agent = PosterAgent()

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'campaign_data' not in st.session_state:
    st.session_state.campaign_data = {}
if 'intelligence_report' not in st.session_state:
    st.session_state.intelligence_report = {}
if 'variations' not in st.session_state:
    st.session_state.variations = []
if 'deployment_manifest' not in st.session_state:
    st.session_state.deployment_manifest = {}
if 'performance_data' not in st.session_state:
    st.session_state.performance_data = []
if 'insights' not in st.session_state:
    st.session_state.insights = {}
if 'optimization_actions' not in st.session_state:
    st.session_state.optimization_actions = {}

def validate_inputs(inputs):
    for key, value in inputs.items():
        if not value or value == "":
            st.error(f"{key} is mandatory. Please fill it in.")
            return False
    return True

def step_1_initial_setup():
    st.markdown('<div class="main-header"><h1>🚀 Dynamic Ad-Copy Multi-Tester</h1><p>AI-Powered Ad Optimization Platform</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="step-card fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #667eea; margin-bottom: 1rem;">📋 Step 1: Initial Setup & User Input Collection</h2>', unsafe_allow_html=True)
    st.write("Provide campaign details, audience information, platforms, and testing parameters. All fields are mandatory.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        campaign_name = st.text_input("🎯 Campaign Name", key="campaign_name", placeholder="Enter campaign name...")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        objective = st.selectbox("🎯 Campaign Objective", ["Brand Awareness", "Lead Generation", "Sales", "Engagement"], key="objective")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        product_desc = st.text_area("📦 Product/Service Description", key="product_desc", placeholder="Describe your product/service...")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        usps = st.text_area("✨ Unique Selling Propositions (USPs)", key="usps", placeholder="What makes you unique?")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        budget = st.number_input("💰 Budget (USD)", min_value=0.0, key="budget", step=100.0)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        timeline = st.text_input("⏰ Timeline/Deadlines", key="timeline", placeholder="e.g., Q4 2024, 3 months...")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        demographics = st.text_area("👥 Demographics (Age, Gender, Location, Income)", key="demographics", placeholder="Target audience demographics...")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        psychographics = st.text_area("🧠 Psychographics (Interests, Values, Lifestyle)", key="psychographics", placeholder="Audience interests and values...")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        pain_points = st.text_area("🎯 Pain Points & Challenges", key="pain_points", placeholder="What problems do they face?")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        communication_style = st.selectbox("💬 Preferred Communication Style", ["Professional", "Casual", "Humorous", "Authoritative", "Empathetic"], key="communication_style")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    platforms = st.multiselect("🌐 Platforms", ["Facebook", "Google Ads", "LinkedIn", "Twitter/X", "TikTok"], key="platforms")
    st.markdown('</div>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        num_variations = st.slider("🔢 Number of Ad Variations", 20, 50, 20, key="num_variations")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        test_duration = st.slider("⏱️ Test Duration (Hours)", 24, 168, 72, key="test_duration")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        success_metrics = st.multiselect("📊 Success Metrics Priority", ["CTR", "CPC", "Conversions", "Engagement"], key="success_metrics")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        tone = st.selectbox("🎭 Tone of Voice", ["Professional", "Casual", "Humorous", "Authoritative", "Empathetic"], key="tone")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
    brand_guidelines = st.text_area("📋 Brand Guidelines", key="brand_guidelines", placeholder="Brand voice, prohibited words, compliance...")
    st.markdown('</div>', unsafe_allow_html=True)

    inputs = {
        "Campaign Name": campaign_name,
        "Objective": objective,
        "Product/Service Description": product_desc,
        "USPs": usps,
        "Budget": budget,
        "Timeline": timeline,
        "Demographics": demographics,
        "Psychographics": psychographics,
        "Pain Points": pain_points,
        "Communication Style": communication_style,
        "Platforms": platforms,
        "Number of Variations": num_variations,
        "Test Duration": test_duration,
        "Success Metrics": success_metrics,
        "Tone": tone,
        "Brand Guidelines": brand_guidelines
    }

    st.markdown('<div style="text-align: center; margin-top: 2rem;">', unsafe_allow_html=True)
    if st.button("Next ➡️", key="next_research"):
        if validate_inputs(inputs):
            st.session_state.campaign_data = inputs
            st.session_state.step = 2
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def step_2_research_agent():
    st.header("Step 2: Research Agent - Market Intelligence & Audience Profiling")
    st.write("Generating audience intelligence report based on your inputs.")

    if st.button("Generate Intelligence Report"):
        with st.spinner("Researching..."):
            time.sleep(2)  # Simulate processing
            report = research_agent.generate_intelligence_report(st.session_state.campaign_data, st.session_state.campaign_data)
            st.session_state.intelligence_report = report

    if st.session_state.intelligence_report:
        st.subheader("Audience Intelligence Report")
        st.json(st.session_state.intelligence_report)

        if st.button("Next: Creative Agent"):
            st.session_state.step = 3
            st.rerun()

def step_3_creative_agent():
    st.header("Step 3: Creative Agent - Ad Copy Generation & Variation Creation")
    st.write("Generating ad copy variations.")

    if st.button("Generate Ad Variations"):
        with st.spinner("Creating variations..."):
            time.sleep(3)
            variations = creative_agent.generate_ad_variations(
                st.session_state.intelligence_report,
                st.session_state.campaign_data,
                st.session_state.campaign_data.get("Number of Variations", 20)
            )
            st.session_state.variations = variations

    if st.session_state.variations:
        st.subheader("Ad Copy Variations")
        df = pd.DataFrame(st.session_state.variations)
        st.dataframe(df)

        if st.button("Next: Deployment Agent"):
            st.session_state.step = 4
            st.rerun()

def step_4_deployment_agent():
    st.header("Step 4: Deployment Agent - Platform Configuration & Campaign Launch")
    st.write("Simulating campaign deployment.")

    if st.button("Deploy Campaign"):
        with st.spinner("Deploying..."):
            time.sleep(2)
            manifest = deployment_agent.deploy_campaign(st.session_state.variations, st.session_state.campaign_data["Platforms"])
            st.session_state.deployment_manifest = manifest

    if st.session_state.deployment_manifest:
        st.subheader("Deployment Manifest")
        st.json(st.session_state.deployment_manifest)

        if st.button("Next: Monitoring Agent"):
            st.session_state.step = 5
            st.rerun()

def step_5_monitoring_agent():
    st.header("Step 5: Monitoring Agent - Real-Time Performance Tracking")
    st.write("Monitoring performance data.")

    if st.button("Start Monitoring"):
        with st.spinner("Monitoring..."):
            time.sleep(2)
            data = monitoring_agent.monitor_performance(st.session_state.variations, st.session_state.campaign_data["Test Duration"])
            st.session_state.performance_data = data

    if st.session_state.performance_data:
        st.subheader("Performance Data")
        df = pd.DataFrame(st.session_state.performance_data)
        st.dataframe(df)

        fig = px.bar(df, x="variation_id", y="ctr", title="CTR by Variation")
        st.plotly_chart(fig)

        if st.button("Next: Analysis Agent"):
            st.session_state.step = 6
            st.rerun()

def step_6_analysis_agent():
    st.header("Step 6: Analysis Agent - Statistical Evaluation & Insights Generation")
    st.write("Analyzing performance data.")

    if st.button("Analyze Performance"):
        with st.spinner("Analyzing..."):
            time.sleep(2)
            insights = analysis_agent.analyze_performance(st.session_state.performance_data)
            st.session_state.insights = insights

    if st.session_state.insights:
        st.subheader("Insights & Recommendations")
        st.json(st.session_state.insights)

        if st.button("Next: Optimization Agent"):
            st.session_state.step = 7
            st.rerun()

def step_7_optimization_agent():
    st.header("Step 7: Optimization Agent - Continuous Improvement & Iteration")
    st.write("Optimizing campaign based on insights.")

    if st.button("Optimize Campaign"):
        with st.spinner("Optimizing..."):
            time.sleep(2)
            actions = optimization_agent.optimize_campaign(st.session_state.insights, st.session_state.variations)
            st.session_state.optimization_actions = actions

    if st.session_state.optimization_actions:
        st.subheader("Optimization Actions")
        st.json(st.session_state.optimization_actions)

        if st.button("Next: Dashboard"):
            st.session_state.step = 8
            st.rerun()

def step_8_dashboard():
    st.header("Step 8: Continuous Feedback Loop & Dashboard")
    st.write("Campaign overview and results.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Campaign Summary")
        st.write(f"**Campaign Name:** {st.session_state.campaign_data.get('Campaign Name', 'N/A')}")
        st.write(f"**Objective:** {st.session_state.campaign_data.get('Objective', 'N/A')}")
        st.write(f"**Platforms:** {', '.join(st.session_state.campaign_data.get('Platforms', []))}")
        st.write(f"**Variations Generated:** {len(st.session_state.variations)}")

    with col2:
        if st.session_state.performance_data:
            df = pd.DataFrame(st.session_state.performance_data)
            avg_ctr = df["ctr"].mean()
            st.metric("Average CTR", f"{avg_ctr:.2f}%")
            top_variation = df.loc[df["ctr"].idxmax()]
            st.write(f"**Top Variation:** {top_variation['variation_id']} (CTR: {top_variation['ctr']}%)")

    if st.button("Restart Campaign"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

def step_9_poster_generation():
    st.header("Step 9: Poster Generation - AI-Powered Advertisement Creation")
    st.write("Generate a professional advertisement poster using optimized campaign data and DALL-E.")

    # Check if we have the required data
    if not st.session_state.campaign_data or not st.session_state.variations or not st.session_state.insights:
        st.error("Please complete the previous steps first to generate a poster.")
        return

    # Get top performing variations
    if st.session_state.performance_data:
        df = pd.DataFrame(st.session_state.performance_data)
        top_variations = sorted(st.session_state.variations,
                               key=lambda x: next((p['ctr'] for p in st.session_state.performance_data if p['variation_id'] == x['id']), 0),
                               reverse=True)[:3]
    else:
        top_variations = st.session_state.variations[:3]

    st.markdown('<div class="step-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #667eea; margin-bottom: 1rem;">🎨 Generate Advertisement Poster</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Campaign Overview")
        st.write(f"**Campaign:** {st.session_state.campaign_data.get('Campaign Name', 'N/A')}")
        st.write(f"**Product:** {st.session_state.campaign_data.get('Product/Service Description', 'N/A')}")
        st.write(f"**Top Headline:** {top_variations[0]['headline'] if top_variations else 'N/A'}")
        st.write(f"**Call to Action:** {top_variations[0]['cta'] if top_variations else 'N/A'}")

        st.subheader("Key Insights")
        insights = st.session_state.insights
        if insights.get('key_findings'):
            for finding in insights['key_findings'][:3]:
                st.write(f"• {finding}")

    with col2:
        st.subheader("Poster Preview")
        if st.button("🎨 Generate Poster", key="generate_poster"):
            with st.spinner("Creating your advertisement poster..."):
                result = poster_agent.generate_poster(
                    st.session_state.campaign_data,
                    top_variations,
                    st.session_state.insights
                )

                if result.get('success'):
                    st.success("Poster generated successfully!")

                    # Display the poster image
                    st.image(result['image_data'], caption="Generated Advertisement Poster", use_column_width=True)

                    # Display generation details
                    with st.expander("Generation Details"):
                        st.write(f"**Prompt Used:** {result['prompt_used']}")
                        st.write(f"**Generated At:** {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result['generated_at']))}")

                    # Download button with actual image data
                    campaign_name = st.session_state.campaign_data.get('Campaign Name', 'campaign').replace(' ', '_')
                    file_name = f"{campaign_name}_poster.png"

                    st.download_button(
                        label="📥 Download Poster",
                        data=result['image_data'],
                        file_name=file_name,
                        mime="image/png",
                        key="download_poster"
                    )
                else:
                    st.error(f"Failed to generate poster: {result.get('error', 'Unknown error')}")

    st.markdown('</div>', unsafe_allow_html=True)

# Main app logic
st.sidebar.title("Dynamic Ad-Copy Multi-Tester")
st.sidebar.write("Navigate through the steps:")

steps = [
    "1. Initial Setup",
    "2. Research Agent",
    "3. Creative Agent",
    "4. Deployment Agent",
    "5. Monitoring Agent",
    "6. Analysis Agent",
    "7. Optimization Agent",
    "8. Dashboard",
    "9. Poster Generation"
]

for i, step_name in enumerate(steps, 1):
    if st.sidebar.button(step_name, key=f"nav_{i}"):
        st.session_state.step = i
        st.rerun()

current_step = st.session_state.step

if current_step == 1:
    step_1_initial_setup()
elif current_step == 2:
    step_2_research_agent()
elif current_step == 3:
    step_3_creative_agent()
elif current_step == 4:
    step_4_deployment_agent()
elif current_step == 5:
    step_5_monitoring_agent()
elif current_step == 6:
    step_6_analysis_agent()
elif current_step == 7:
    step_7_optimization_agent()
elif current_step == 8:
    step_8_dashboard()
elif current_step == 9:
    step_9_poster_generation()

st.sidebar.progress((current_step - 1) / 8)
