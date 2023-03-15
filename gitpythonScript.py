from git import Repo
import io

# Clone the repository
def clone_repo(repo_url):
    Repo.clone_from(repo_url, 'repo') # Clone the repository to a directory named 'repo'

# Change text in XML file
def change_xml_file(inputFileName, mapperFileName):
    input_dict = {}
    with open(r'C:\Users\91751\Desktop\script\input.txt', 'r') as file:
        
        for line in file.readlines():
            value = line.split("|")
            component = value[0]
            version = value[2]
            input_dict[component] = version

    print(input_dict)


    mapper_dict = {}
    with open(r'C:\Users\91751\Desktop\script\mapper.txt', 'r') as file:
        
        for line in file.readlines():
            value = line.split(":", 1)
            component = value[0]
            version = value[1]
            mapper_dict[component] = version

    print(mapper_dict)

    main_dict = {}
    for key in input_dict:
        element = mapper_dict[key].strip("\n")
        value = input_dict[key].strip("\n")
        main_dict[element] = value

    print(main_dict)
    

    with open(r'C:\Users\91751\Desktop\script\repo\citirisk-core\pomXML.txt', 'r') as file:
        lines = []
        for line in file.readlines():
            value = line.split(">", 1)
            new_value_1 = value[0].split("<",1)[1]
            new_value_2 = value[1].split("<", 1)[0]
            if main_dict.get(new_value_1) is not None:
                lines.append(line.replace(new_value_2, main_dict[new_value_1]))
            else:
                lines.append(line)

    with open(r'C:\Users\91751\Desktop\script\repo\citirisk-core\pomXML.txt', 'w') as file:
        for line in lines:
            file.write(line)

# Create new branch
def create_new_branch(repo, branch_name):
    repo.git.checkout('-b', branch_name)

# Commit and push changes
def commit_and_push_changes(repo, branch_name, commit_message):
    repo.git.add('.')
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push(branch_name)

# Main function
def main():
    # Clone the repository
    repo_url = 'https://github.com/divyamrai28/PythonScriptingForPomXMLchange.git'
    clone_repo(repo_url)
    
    # Open the cloned repository
    repo = Repo('repo')
    
    # Change text in XML file
    inputFileName = 'input.txt'
    mapperFileName = 'mapper.txt'
    change_xml_file(inputFileName, mapperFileName)
    
    # Create new branch
    branch_name = 'new-branch_1'
    create_new_branch(repo, branch_name)
    
    # Commit and push changes
    commit_message = 'Version Changed'
    commit_and_push_changes(repo, branch_name, commit_message)

if __name__ == '__main__':
    main()
