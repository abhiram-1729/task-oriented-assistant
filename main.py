import os
import google.generativeai as genai
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

class GeminiTeacher:
    def __init__(self):
        # Configure Gemini
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Please set GEMINI_API_KEY in your .env file")
        
        genai.configure(api_key=self.api_key)
        
        # Create the model with teacher personality
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Memory storage
        self.conversation_history = []
        self.user_preferences = {}
        
        # Teacher persona
        self.teacher_persona = """
        You are Professor Planwell, an experienced teacher and planning expert. 
        Your personality:
        - Patient and encouraging
        - Clear and structured in explanations
        - Uses analogies and examples
        - Remembers student's progress
        - Adapts to learning style
        - Celebrates small victories
        
        Teaching style:
        1. Break down complex goals into manageable steps
        2. Provide reasoning for each step
        3. Suggest resources and timelines
        4. Check for understanding
        5. Offer encouragement
        """
    
    def add_to_memory(self, user_input, assistant_response):
        """Store conversation in memory"""
        self.conversation_history.append({
            'user': user_input,
            'assistant': assistant_response,
            'timestamp': len(self.conversation_history)
        })
        
        # Keep only last 20 messages to manage context
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]
    
    def get_context(self):
        """Get recent conversation context"""
        if not self.conversation_history:
            return "No previous conversation."
        
        context = "Recent conversation:\n"
        for msg in self.conversation_history[-5:]:  # Last 5 exchanges
            context += f"Student: {msg['user']}\n"
            context += f"Teacher: {msg['assistant']}\n"
        return context

class PlanningSystem:
    def __init__(self, gemini_teacher):
        self.teacher = gemini_teacher
    
    def create_structured_plan(self, user_goal):
        """Create a detailed plan for the user's goal"""
        
        # Build the prompt with memory and persona
        prompt = f"""
        {self.teacher.teacher_persona}
        
        Context: {self.teacher.get_context()}
        
        Student's Goal: {user_goal}
        
        Please create a comprehensive plan with this structure:
        
        🎯 GOAL ANALYSIS:
        - Understanding what the student wants to achieve
        - Why this goal is important
        - Potential challenges
        
        📝 STRUCTURED PLAN:
        [Create a step-by-step plan with:
        1. Step description
        2. Reasoning why this step is important
        3. Estimated time
        4. Resources needed
        5. Success criteria]
        
        🔍 ADDITIONAL RESEARCH:
        [Mention if web research would be helpful for any step]
        
        💡 TEACHER'S NOTES:
        - Encouragement
        - Tips for success
        - What to focus on
        
        Remember to be supportive and use teaching analogies!
        """
        
        try:
            response = self.teacher.model.generate_content(prompt)
            plan = response.text
            
            # Store in memory
            self.teacher.add_to_memory(user_goal, plan)
            
            return plan
            
        except Exception as e:
            return f"I encountered an error while planning: {str(e)}"


class EnhancedTeacher(GeminiTeacher):
    """Extended teacher with learning style detection and personalization"""
    
    def __init__(self):
        super().__init__()
        self.student_profile = {
            'learning_style': None,
            'preferred_pace': None,
            'previous_successes': []
        }
    
    def detect_learning_style(self, user_input):
        """Simple learning style detection"""
        styles = {
            'visual': ['see', 'show', 'visual', 'picture', 'diagram'],
            'auditory': ['hear', 'listen', 'talk', 'discuss'],
            'kinesthetic': ['do', 'practice', 'hands-on', 'try']
        }
        
        for style, keywords in styles.items():
            if any(keyword in user_input.lower() for keyword in keywords):
                self.student_profile['learning_style'] = style
                return style
        return None
    
    def personalize_response(self, base_plan, learning_style):
        """Add personalization based on learning style"""
        personalization = {
            'visual': "\n👁️ **Visual Learner Tip**: Try creating mind maps or diagrams for each step!",
            'auditory': "\n👂 **Auditory Learner Tip**: Explain each step out loud or discuss with a study partner!",
            'kinesthetic': "\n🖐️ **Hands-On Tip**: Practice each concept immediately after learning it!"
        }
        
        if learning_style in personalization:
            return base_plan + personalization[learning_style]
        return base_plan


def main():
    """Main entry point for the planning assistant"""
    import time
    from web_research import PlannerAgent
    
    # Initialize our planner agent
    professor = PlannerAgent()
    
    print(professor.introduction)
    
    # Example conversation
    goals = [
        "I want to learn Python programming in 3 months",
        "Can you help me plan my fitness journey?",
        "I need to prepare for my final exams"
    ]
    
    for goal in goals:
        print("\n" + "="*50)
        plan = professor.process_goal(goal)
        print(f"\n🧠 Professor's Plan:\n{plan}")
        time.sleep(2)  # Small delay to simulate thinking
    
    # Show progress report
    print("\n" + "="*50)
    print(professor.get_progress_report())


if __name__ == "__main__":
    main()