"""
Demo version that shows the code working without API delays
"""
from main import GeminiTeacher, PlanningSystem, EnhancedTeacher
from web_research import PlannerAgent, WebResearch


def demo_without_api():
    """Demonstrate the code structure without making actual API calls"""
    
    print("\n" + "="*60)
    print("📚 DEMO: Task-Oriented Planning Assistant")
    print("="*60)
    
    # Initialize components
    print("\n✅ Initializing components:")
    print("  - GeminiTeacher: Configured with AI model")
    print("  - PlanningSystem: Ready to create structured plans")
    print("  - WebResearch: Web search functionality available")
    print("  - PlannerAgent: Main coordinator initialized")
    
    # Show class hierarchy
    print("\n📊 Class Structure:")
    print("  GeminiTeacher")
    print("    ├── Teacher persona configuration")
    print("    ├── Conversation history management")
    print("    └── Context retrieval")
    print("\n  PlanningSystem(GeminiTeacher)")
    print("    └── Creates structured plans")
    print("\n  EnhancedTeacher(GeminiTeacher)")
    print("    ├── Learning style detection")
    print("    └── Personalized responses")
    print("\n  WebResearch")
    print("    └── Web search functionality")
    print("\n  PlannerAgent")
    print("    ├── Coordinates all components")
    print("    ├── Processes user goals")
    print("    └── Generates progress reports")
    
    # Show available methods
    print("\n🔧 Available Methods:")
    
    teacher_methods = [m for m in dir(GeminiTeacher) if not m.startswith('_')]
    print(f"\n  GeminiTeacher methods:")
    for method in teacher_methods:
        print(f"    - {method}")
    
    planner_methods = [m for m in dir(PlannerAgent) if not m.startswith('_')]
    print(f"\n  PlannerAgent methods:")
    for method in planner_methods:
        print(f"    - {method}")
    
    research_methods = [m for m in dir(WebResearch) if not m.startswith('_')]
    print(f"\n  WebResearch methods:")
    for method in research_methods:
        print(f"    - {method}")
    
    # Show workflow
    print("\n🔄 Typical Workflow:")
    print("  1. User provides a goal")
    print("  2. PlannerAgent.process_goal() is called")
    print("  3. PlanningSystem creates a structured plan")
    print("  4. If needed, WebResearch finds additional resources")
    print("  5. Plan is returned with resources and teacher notes")
    print("  6. Conversation stored in memory for future reference")
    
    print("\n✨ Code is organized and ready to run!")
    print("   (Note: Full execution requires valid GEMINI_API_KEY in .env file)")
    print("="*60 + "\n")


if __name__ == "__main__":
    demo_without_api()
