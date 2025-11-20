# Professor Planwell - AI Planning Assistant 🤖🎓

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-AI-blue?style=for-the-badge&logo=google&logoColor=white)

A professional **AI-powered planning and goal achievement** web application built with Streamlit that transforms your ambitions into actionable, step-by-step plans powered by Google's Gemini API, with memory persistence and personalized teaching methodology.

## ✨ Features

### 🎯 **Intelligent Planning**
- Break down complex goals into manageable steps
- Structured planning with clear reasoning and timelines
- Adaptive to your learning style and preferences

### 📚 **Teaching Methodology**
- Patient, encouraging teacher persona (Professor Planwell)
- Uses analogies and examples for better understanding
- Celebrates small victories and progress milestones

### 🔍 **Enhanced Research**
- Web research integration for learning and study goals
- Automatic resource discovery and recommendations
- Context-aware planning based on your needs

### 💾 **Memory & Personalization**
- Conversation history tracking (last 20 conversations)
- Learning style detection (visual, auditory, kinesthetic)
- Progress analytics and achievement tracking
- Personalized encouragement and guidance

## 🚀 How Professor Planwell Works
User Goal
↓

ANALYSIS: Understand goal importance and challenges
↓

STRUCTURING: Create step-by-step plan with reasoning
↓

ENHANCEMENT: Add resources and personalized tips
↓

DELIVERY: Provide encouraging, teacher-style guidance
↓
Personalized Plan (With timelines & resources)


## Installation

### Requirements
- Python 3.8+
- Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/professor-planwell.git
cd professor-planwell
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

Get your free API key from: [Google AI Studio](https://aistudio.google.com/app/apikey)

4. **Add .env to .gitignore** (important for security!)
```bash
echo ".env" >> .gitignore
```

### Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Step-by-Step Guide

1. **Access the Dashboard** - Open the app and explore the intuitive interface
2. **Create Your Plan** - Navigate to "🚀 Create Plan" tab and enter your goal
3. **Get Personalized Roadmap** - Click "🎯 Create Plan" for your structured plan
4. **Track Progress** - Monitor your achievements in "📈 Progress" tab
5. **Learn Strategies** - Access success tips in "📚 Guide" tab

### Example Goals

- "I want to learn Python programming in 3 months"
- "Plan my fitness journey for the next 6 months"
- "Prepare for my final exams effectively"
- "Start a small business while working full-time"
- "Learn web development and build a portfolio"

## 🏗️ Architecture

### Components

| Component | Purpose |
|-----------|---------|
| `GeminiTeacher` | AI teaching persona with memory and context |
| `PlanningSystem` | Structured plan generation engine |
| `WebResearch` | Resource discovery and web search integration |
| `PlannerAgent` | Main coordination agent orchestrating workflow |
| `EnhancedTeacher` | Extended teacher with learning style detection |

### Core Pipeline

```python
# Example usage
professor = PlannerAgent()
plan = professor.process_goal("Your goal here")
```

### Technology Stack

- **Streamlit** - Interactive web interface with custom CSS
- **Google Generative AI** - Gemini 2.0 Flash model
- **BeautifulSoup4** - Web research and content extraction
- **Requests** - HTTP requests for web search functionality
- **python-dotenv** - Environment variable management

## ⚙️ Configuration

### Environment Variables

```env
GEMINI_API_KEY=your_api_key_here  # Required for Gemini integration
```

### Tunable Parameters

Edit these in the code to customize behavior:

```python
# In GeminiTeacher class
self.conversation_history = []  # Stores last 20 conversations

# In PlanningSystem
context_window = 5  # Number of previous conversations to consider

# Learning style detection keywords
styles = {
    'visual': ['see', 'show', 'visual', 'picture', 'diagram'],
    'auditory': ['hear', 'listen', 'talk', 'discuss'],
    'kinesthetic': ['do', 'practice', 'hands-on', 'try']
}
```

## 💡 Performance Tips

1. **For complex goals** - Be specific about timelines and desired outcomes
2. **Learning preferences** - Use keywords that match your learning style
3. **Progress tracking** - Regularly check the Progress tab for motivation
4. **API costs** - Monitor usage at [Google AI Studio Billing](https://aistudio.google.com/billing)

## ⚠️ Limitations & Future Improvements

### Current Limitations

- ⚠️ Web search functionality is basic (uses Google search scraping)
- ⚠️ No persistent storage between sessions (memory resets)
- ⚠️ Learning style detection relies on keyword matching
- ⚠️ Limited to text-based goals and planning

### Planned Improvements

- [ ] Persistent storage with database integration
- [ ] Advanced web search with proper API integration
- [ ] Multi-format goal input (voice, image analysis)
- [ ] Collaborative planning features
- [ ] Export plans to PDF/calendar formats
- [ ] Advanced progress analytics with charts
- [ ] Integration with productivity tools

## 🛠️ Troubleshooting

### Issue: "GEMINI_API_KEY not found in .env file"
**Solution**: Ensure your `.env` file has `GEMINI_API_KEY=your_key_here` and is in the same directory as `app.py`

### Issue: "Please set GEMINI_API_KEY in your .env file"
**Solution**: Create a `.env` file in the project root with your valid Gemini API key

### Issue: Web search not returning results
**Solution**: This may be due to Google blocking automated requests. Consider implementing a proper search API

### Issue: Streamlit app not loading
**Solution**: Ensure all dependencies are installed and port 8501 is available

## 🔒 Security Considerations

**API Key Safety**
- Never commit `.env` to version control
- Always use `.gitignore` to exclude `.env`
- Rotate your API key regularly
- Use environment variables in production deployments

## 💰 API Costs

- **Gemini 2.0 Flash** - Free tier available (limited requests)
- **Web Research** - Free (basic Google search scraping)
- **Streamlit** - Free for local deployment

Monitor your Gemini API usage: [Google AI Studio Billing](https://aistudio.google.com/billing)

## 📄 License

MIT License - feel free to use this project for personal and commercial use.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request for:
- Bug fixes
- New features
- Documentation improvements
- UI/UX enhancements

## 🆘 Support

For issues, questions, or suggestions, please open a GitHub issue or contact the development team.

---

**Built with ❤️ using:**
- 🎨 **[Streamlit](https://streamlit.io/)** - Interactive web framework
- 🧠 **[Google Gemini](https://ai.google.dev/)** - Generative AI model
- 🌐 **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** - Web scraping
- 📚 **[Requests](https://docs.python-requests.org/)** - HTTP library

---

**Start transforming your goals into achievements today with Professor Planwell!** 🌟

*"The expert in anything was once a beginner. Let's build your roadmap to success together!" - Professor Planwell*
```
