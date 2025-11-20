"""
Streamlit UI for Task-Oriented Planning Assistant
Creative & Interactive Version
"""
import streamlit as st
from main import GeminiTeacher, PlanningSystem, EnhancedTeacher
from web_research import PlannerAgent
import time
import random

# Page configuration
st.set_page_config(
    page_title="Professor Planwell - AI Planning Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for creative styling
st.markdown("""
    <style>
    /* Global Styles */
    :root {
        --primary-color: #6366F1;
        --secondary-color: #EC4899;
        --accent-color: #F59E0B;
        --success-color: #10B981;
        --danger-color: #EF4444;
    }
    
    /* Main Header with Gradient */
    .main-header {
        # background: linear-gradient(135deg, #6366F1 0%, #EC4899 50%, #F59E0B 100%);
        # padding: 1px;
        # border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
        # box-shadow: 0 5px 15px rgba(99, 102, 241, 0.3);
    }
    
    .main-header h1 {
        font-size: 1.8em;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header h3 {
        margin: -20px 0 0 0;
        opacity: 0.95;
        font-size: 1em;
    }
    
    .main-header p {
        margin: -10px 0 0 0;
        font-size: 0.9em;
        opacity: 0.9;
    }
    
    /* Goal Section */
    .goal-section {
        background: linear-gradient(135deg, #E0E7FF 0%, #FCE7F3 100%);
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 10px;
        border: 2px solid #6366F1;
        border-left: 6px solid #EC4899;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.15);
        transition: all 0.3s ease;
    }
    
    .goal-section:hover {
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.25);
        transform: translateY(-2px);
    }
    
    .goal-section h3 {
        color: #4F46E5;
        margin-top: 0;
        font-size: 1.3em;
    }
    
    .goal-section p {
        color: #6B7280;
        line-height: 1.6;
    }
    
    /* Plan Section */
    .plan-section {
        background: linear-gradient(135deg, #F0F9FF 0%, #F5F3FF 50%, #FEF3C7 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 2px dashed #6366F1;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.1);
    }
    
    .plan-section h3 {
        color: #10B981;
        margin-top: 0;
        font-size: 1.3em;
    }
    
    /* Success Box */
    .success-box {
        background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #10B981;
        color: #065F46;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    }
    
    .success-box h3 {
        color: #047857;
        margin-top: 0;
    }
    
    .success-box p {
        color: #065F46;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #FEF3C7 0%, #FCD34D 100%);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #F59E0B;
        color: #92400E;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
    }
    
    .info-box h4 {
        color: #D97706;
        margin-top: 0;
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, #F3E8FF 0%, #FEE2E2 100%);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #EC4899;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .feature-card h4 {
        color: #9F1239;
        margin-top: 0;
    }
    
    .feature-card p {
        color: #6B7280;
    }
    
    .feature-card:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.2);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #EC4899 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
    }
    
    /* Text Area */
    .stTextArea textarea {
        border: 2px solid #6366F1 !important;
        border-radius: 10px !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #6366F1 0%, #EC4899 100%);
    }
    
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'professor' not in st.session_state:
    try:
        st.session_state.professor = PlannerAgent()
        st.session_state.initialized = True
    except ValueError as e:
        st.session_state.initialized = False
        st.session_state.error_msg = str(e)

# Creative Header
st.markdown("""
    <div class='main-header'>
        <h1>🎓 Professor Planwell</h1>
        <h3>✨ Your AI-Powered Planning Assistant ✨</h3>
        <p>Transform your wildest dreams into actionable step-by-step plans</p>
    </div>
""", unsafe_allow_html=True)

# Error handling
if not st.session_state.initialized:
    st.error(f"⚠️ {st.session_state.error_msg}")
    st.info("🔑 Please ensure you have a valid `GEMINI_API_KEY` in your `.env` file")
else:
    # Sidebar with creative elements
    with st.sidebar:
        st.markdown("### 📊 Your Planning Dashboard")
        
        professor = st.session_state.professor
        conversation_count = len(professor.teacher.conversation_history)
        
        # Metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎯 Goals", conversation_count)
        with col2:
            st.metric("📋 Plans", conversation_count)
        
        st.divider()
        
        # Learning streak
        if conversation_count > 0:
            st.success(f"🔥 {conversation_count} {'goal' if conversation_count == 1 else 'goals'} on your journey!")
        
        st.divider()
        
        # Features
        st.markdown("### ⚡ Amazing Features")
        features = [
            "🤖 AI-Powered Planning",
            "📚 Structured Guidance",
            "🔍 Web Research",
            "💾 Memory & Progress",
            "🎓 Personalized Learning"
        ]
        for feature in features:
            st.markdown(f"✓ {feature}")
        
        st.divider()
        
        # Quick tips
        st.markdown("### 💡 Quick Tips")
        tips = [
            "Be specific with goals",
            "Break into small steps",
            "Track progress daily",
            "Celebrate small wins"
        ]
        for i, tip in enumerate(tips, 1):
            st.caption(f"{i}. {tip}")
    
    # Main content with tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 Create Plan", "📈 Progress", "📚 Guide", "🎨 About"])
    
    with tab1:
        st.header("🚀 Create Your Perfect Plan")
        
        # Goal input section
        # st.markdown("""
        #     <div class='goal-section'>
        #         <h3>🎯 What goal would you like to work on today?</h3>
        #         <p>Share your objective, and Professor Planwell will create a comprehensive, personalized plan just for you.</p>
        #     </div>
        # """, unsafe_allow_html=True)
        
        # Input
        goal_input = st.text_area(
            "Your Goal:",
            placeholder="e.g., I want to learn Python programming in 3 months...",
            height=100,
            label_visibility="collapsed"
        )
        
        # Suggestions below input
        # st.write("**Quick Suggestions:**")
        # cols = st.columns(5)
        # suggestions = ["🐍 Python", "💪 Fitness", "📚 Study", "🎨 Creative", "💼 Career"]
        # for col, sugg in zip(cols, suggestions):
        #     with col:
        #         st.caption(sugg)
        
        # st.divider()
        
        # Buttons
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submit_button = st.button("🎯 Create Plan", use_container_width=True)
        with col2:
            clear_button = st.button("🔄 Clear", use_container_width=True)
        
        if clear_button:
            st.rerun()
        
        # Process goal
        if submit_button and goal_input.strip():
            loading_messages = [
                "🧠 Thinking deeply...",
                "✍️ Crafting your plan...",
                "🔍 Researching resources...",
                "🎯 Structuring pathway...",
                "⚡ Adding final touches..."
            ]
            placeholder = st.empty()
            
            try:
                progress_bar = st.progress(0)
                
                for i in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
                    if i % 20 == 0:
                        placeholder.info(random.choice(loading_messages))
                
                placeholder.empty()
                
                # Create plan
                plan = st.session_state.professor.process_goal(goal_input)
                
                # Success message
                st.markdown("""
                    <div class='success-box'>
                        <h3>🎉 Plan Created Successfully!</h3>
                        <p>Your personalized roadmap is ready. Follow these steps to achieve your goal!</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Display plan
                st.markdown('<div class="plan-section">', unsafe_allow_html=True)
                st.markdown(plan)
                st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        elif submit_button and not goal_input.strip():
            st.warning("⚠️ Please enter a goal to create a plan.")
    
    with tab2:
        st.header("📈 Your Progress Hub")
        
        professor = st.session_state.professor
        history = professor.teacher.conversation_history
        
        if history:
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #DBEAFE 0%, #E9D5FF 100%); padding: 25px; border-radius: 15px; margin-bottom: 25px;'>
                    <h2 style='color: #1E40AF; margin-top: 0;'>🏆 You're On Fire!</h2>
                    <p style='color: #1E3A8A; font-size: 1.2em;'><strong>{len(history)}</strong> goal{'s' if len(history) > 1 else ''} completed</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            st.subheader("📜 Your Goal Journey")
            
            for i, entry in enumerate(reversed(history[-10:]), 1):
                with st.expander(f"🎯 Goal {len(history) - i + 1}: {entry['user'][:60]}..."):
                    st.markdown(f"> **{entry['user']}**")
                    summary = entry['assistant'][:300] + "..." if len(entry['assistant']) > 300 else entry['assistant']
                    st.markdown(summary)
        else:
            st.markdown("""
                <div style='background: linear-gradient(135deg, #E0E7FF 0%, #FCE7F3 100%); padding: 40px; border-radius: 15px; text-align: center;'>
                    <h2 style='color: #4F46E5;'>🌟 Start Your Journey</h2>
                    <p style='color: #6B7280;'>No goals yet. Go to <strong>Create Plan</strong> tab to begin!</p>
                </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.header("📚 Success Guide")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div class='feature-card'>
                    <h4>🎯 Be Specific</h4>
                    <p>Clear goals = Better plans. Include timelines and metrics.</p>
                </div>
                
                <div class='feature-card'>
                    <h4>⏰ Realistic Timelines</h4>
                    <p>Break down goals into monthly and weekly targets.</p>
                </div>
                
                <div class='feature-card'>
                    <h4>📚 Stay Flexible</h4>
                    <p>Adjust your plan as you learn and grow.</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class='feature-card'>
                    <h4>💪 Consistency Wins</h4>
                    <p>Small daily steps create massive results.</p>
                </div>
                
                <div class='feature-card'>
                    <h4>🎉 Celebrate Wins</h4>
                    <p>Acknowledge every milestone!</p>
                </div>
                
                <div class='feature-card'>
                    <h4>🤝 Get Support</h4>
                    <p>Share goals & ask for help.</p>
                </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.header("🎨 About Professor Planwell")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🤖 Your AI Planning Partner
            
            Professor Planwell combines AI intelligence with teaching wisdom to create personalized plans for your goals.
            
            ✨ **Key Features:**
            - Patient & encouraging guidance
            - Structured step-by-step plans
            - Memory of your progress
            - Adaptive to your learning style
            - Resource recommendations
            
            **Mission:** Empower you to achieve anything with the right plan and support.
            """)
        
        with col2:
            st.image("https://img.icons8.com/nolan/256/teacher.png", use_column_width=True)
        
        st.divider()
        
        st.markdown("""
            <div class='info-box'>
                <h4>🚀 Ready to Begin?</h4>
                <p>Go to the <strong>Create Plan</strong> tab and start your transformation today!</p>
            </div>
        """, unsafe_allow_html=True)
