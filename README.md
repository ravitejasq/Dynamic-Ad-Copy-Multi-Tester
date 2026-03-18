# 🚀 Dynamic Ad-Copy Multi-Tester

## 🎯 Project Overview

**Dynamic Ad-Copy Multi-Tester** is an AI-powered platform that automates the entire ad copy optimization workflow. Built for the **Gen AI Hackathon**, it uses multi-agent AI systems to generate 20-50 ad variations, simulate A/B testing across platforms (Facebook, Google Ads, etc.), analyze performance metrics (CTR, CPC, conversions), and create professional DALL-E generated advertisement posters.

### ✨ Key Features
- **7 Specialized AI Agents**: Research, Creative, Deployment, Monitoring, Analysis, Optimization, PosterAgent
- **End-to-End Workflow**: Input → Intelligence → Variations → Testing → Insights → Optimization → Poster
- **Real-time Simulation**: Generates realistic performance data (CTR 1-5%, CPC, conversions)
- **DALL-E Poster Generation**: Creates professional ad posters from optimized campaigns
- **Modern UI/UX**: Gradient animations, 3D cards, shimmer effects, responsive design
- **Multi-Platform**: Facebook, Google Ads, LinkedIn, Twitter/X, TikTok support
- **Vercel Deploy Ready**: Production-ready deployment configuration

## 🛠️ Tech Stack
```
Frontend: Streamlit + Custom CSS (Animations, Gradients, 3D Transforms)
Backend: Python + OpenAI GPT-3.5/DALL-E 3
Data: Pandas + Plotly Express
Deployment: Vercel
APIs: OpenAI API
```
**Dependencies**: `streamlit openai pandas plotly requests numpy matplotlib`

## 🚀 Quick Start

### Prerequisites
```bash
# Clone & Navigate
cd gen-ai-hackathon

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo 'OPENAI_API_KEY="your-key-here"' > config.py
```

### Run Locally
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501)

### Deploy to Vercel
```bash
# Already configured with vercel.json
vercel --prod
```

## 📋 How It Works (9-Step Workflow)

1. **Initial Setup**: Enter campaign details, audience demographics, budget, platforms
2. **Research Agent**: Generates market intelligence & micro-personas  
3. **Creative Agent**: Creates 20-50 unique ad copy variations (headlines, body, CTAs)
4. **Deployment Agent**: Simulates multi-platform campaign launch
5. **Monitoring Agent**: Tracks real-time performance (CTR, CPC, conversions)
6. **Analysis Agent**: Statistical evaluation & insights generation
7. **Optimization Agent**: Budget reallocation & variation recommendations
8. **Dashboard**: Performance overview & top performers
9. **PosterAgent**: DALL·E 3 generates professional ad posters

## 📊 Sample Results
```
Generated Variations: 20-50 per run
CTR Range: 1.0-5.0% (realistic simulation)
Top Performers: Identified automatically
Poster Output: Downloadable PNG (1024x1024)
```

## 🎨 UI Highlights
- Animated gradient backgrounds (5-color shift)
- 3D hover cards with backdrop blur
- Shimmer progress bars & loading animations
- Metric cards with rotating orbs & pulse effects
- Glassmorphism design with custom Inter font

## 🏆 Hackathon Innovation
- **Multi-Agent Architecture**: 7 specialized AI agents collaborating
- **Full Automation**: Manual → Fully automated A/B testing pipeline
- **Production Ready**: Deployed UI with real OpenAI integration
- **Visual Output**: DALL-E posters as tangible deliverables

## 📁 Project Structure
```
gen-ai-hackathon/
├── app.py              # Main Streamlit app (900+ lines UI + logic)
├── agents.py           # 7 AI Agent classes (OpenAI integration)
├── config.py           # API keys
├── requirements.txt    # Dependencies
├── vercel.json         # Deployment config
├── test_poster.py      # Poster testing
└── README.md          # You're reading it!
```

## 🔮 Future Enhancements
- [ ] Real ad platform APIs (Meta, Google Ads)
- [ ] Live A/B testing integration  
- [ ] Multi-language support
- [ ] Advanced ML models for prediction
- [ ] Team collaboration features

## 🤝 Contributing
```
1. Fork the repo
2. Create feature branch
3. Submit PR with tests
```

## 📄 License
MIT License - Feel free to use & adapt!

---

**Built with ❤️ for Gen AI Hackathon** | **Streamlit + OpenAI + Modern UI**
