# Importing necessary libraries
from github import Github
from textwrap import dedent

# Configuration
github_token = "..token.."
repo_name = "..path.."
readme_path = "README.md"

# Functions

def generate_info_scripted(points):
    return dedent(f"""
    ### Project Information

    - **Project Name:** LeetCode Solutions
    - **Description:** Collection of solutions to various LeetCode problems
    - **Features:** Python solutions, organized by problem categories
    - **Current Status:** Actively maintained

    Based on the points provided:
    {points}
    """)

def update_readme(content):
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    
    try:
        readme = repo.get_contents(readme_path)
        new_content = readme.decoded_content.decode() + "\n\n" + content
        repo.update_file(readme.path, "Update README", new_content, readme.sha)
        print(f"README updated successfully at {readme_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Creating a new README file...")
        repo.create_file(readme_path, "Create README", content)
        print(f"README created successfully at {readme_path}.")

def main():
    points = """
    - Project Name: LeetCode Solutions
    - Description: Collection of solutions to various LeetCode problems
    - Features: Python solutions, organized by problem categories
    - Current Status: Actively maintained
    """
    
    print("Generating information using the scripted method...")
    generated_info = generate_info_scripted(points)
    
    print("\nGenerated Information to Add:\n")
    print(generated_info)

    while True:
        user_input = input("Do you want to proceed with this information? (Y/N): ").strip().upper()
        
        if user_input == 'Y':
            update_readme(generated_info)
            break  # Exit the loop after successful update
        elif user_input == 'N':
            print("Regenerating information...")
            generated_info = generate_info_scripted(points)
            print("\nGenerated Information to Add:\n")
            print(generated_info)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()