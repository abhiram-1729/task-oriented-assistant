import requests
from bs4 import BeautifulSoup
from main import GeminiTeacher, PlanningSystem


class WebResearch:
    """Web search functionality for research and resource discovery"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_web(self, query):
        """Simple web search (you can enhance this with proper search API)"""
        try:
            # This is a basic example - consider using Google Search API for production
            url = f"https://www.google.com/search?q={requests.utils.quote(query)}"
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic information (simplified)
            results = []
            for g in soup.find_all('div', class_='g')[:3]:  # First 3 results
                anchor = g.find('a')
                if anchor:
                    link = anchor.get('href')
                    title = g.find('h3')
                    if title:
                        results.append({
                            'title': title.text,
                            'link': link
                        })
            return results[:3]  # Return top 3 results
            
        except Exception as e:
            return f"Web search unavailable: {str(e)}"


class PlannerAgent:
    """Main agent coordinating planning, teaching, and web research"""
    
    def __init__(self):
        self.teacher = GeminiTeacher()
        self.planner = PlanningSystem(self.teacher)
        self.researcher = WebResearch()
        
        # Teacher's introduction
        self.introduction = """
        👋 Hello! I'm Professor Planwell, your personal planning assistant!
        
        I'm here to help you:
        • Break down big goals into manageable steps
        • Create structured plans with clear reasoning
        • Remember your progress and preferences
        • Provide teacher-style guidance and encouragement
        
        What goal would you like to work on today? 🎯
        """
    
    def process_goal(self, user_goal):
        """Main method to process user goals"""
        
        print(f"\n📚 Student's Goal: {user_goal}")
        print("🤔 Professor is thinking...")
        
        # Check if this relates to previous conversations
        context = self.teacher.get_context()
        if "No previous conversation" not in context:
            print("📖 Professor is reviewing your progress...")
        
        # Create the main plan
        plan = self.planner.create_structured_plan(user_goal)
        
        # Check if web research would help
        if any(keyword in user_goal.lower() for keyword in ['learn', 'research', 'study', 'find']):
            print("🔍 Professor is checking for additional resources...")
            web_results = self.researcher.search_web(user_goal)
            if web_results and not isinstance(web_results, str):
                plan += "\n\n🌐 **Additional Resources I Found:**\n"
                for result in web_results:
                    plan += f"• {result['title']}\n"
        
        return plan
    
    def get_progress_report(self):
        """Generate a progress report based on memory"""
        if not self.teacher.conversation_history:
            return "We haven't started working on any goals yet!"
        
        total_goals = len(self.teacher.conversation_history)
        recent_goal = self.teacher.conversation_history[-1]['user']
        
        report = f"""
        📊 **Progress Report**
        
        Total goals we've worked on: {total_goals}
        Most recent goal: {recent_goal}
        
        I remember all our conversations and can see how you're growing!
        Keep up the great work! 🌟
        """
        return report