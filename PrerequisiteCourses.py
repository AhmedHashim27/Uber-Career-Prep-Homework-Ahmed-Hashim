"""
Time Complexity: O(V + E) => must visit every course (vertex) and its prereq (edge) 
Space Complexity: O(V + E) => must store visited courses in set
Technique: Depth-first search
Time Spent:60 mins

"""
def prerequisite_courses(courses, prerequisites):
    for course in courses:
        if course not in prerequisites:
            prerequisites[course] = []

    order = []
    visited = set()
    
    def dfs(course):
        if course in visited:  # already visited course
            return 
        
        visited.add(course)

        # visit all prerequisites before adding current course to order[]
        for prerequisite in prerequisites[course]:
            dfs(prerequisite)
        
        order.append(course)
        
    for course in courses:
        dfs(course)

    print(order)
    return order

# Test Cases  
prerequisite_courses(
    ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"],
    {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"]
    }
)
prerequisite_courses(
    ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"],
    {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"]
    }
)
