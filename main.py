# ============================================
# Smart Wildlife Identifier
# Introduction to AI Decision Trees
# ============================================

# --------------------------------------------
# Decision Tree Node
# --------------------------------------------
class DecisionNode:
    def __init__(self, text):
        self.text = text
        # TODO 1:
        # Create left and right child references
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.text)   



# --------------------------------------------
# Build the Initial Decision Tree
# --------------------------------------------

def build_tree():
    # Root question
    root = DecisionNode("Does it have feathers?")
    # TODO 2:
    # Create the remaining question nodes:
    #
    # "Can it fly?"
    # "Does it live in water?"
    can_fly = DecisionNode("Can it fly?")
    live_in_water = DecisionNode("Does it live in water?")

    # TODO 3:
    # Create the four classification nodes:
    #
    # Bird
    # Penguin
    # Fish
    # Mammal
    bird = DecisionNode("Bird")
    penguin = DecisionNode("Penguin")
    fish = DecisionNode("Fish")
    mammal = DecisionNode("Mammal")

    # TODO 4:
    # Connect the nodes using:
    #
    # left = YES
    # right = NO
    root.left = can_fly
    root.right = live_in_water
    can_fly.left = bird
    can_fly.right = penguin
    live_in_water.left = fish
    live_in_water.right = mammal

    return root

# --------------------------------------------
# Identify an Animal
# --------------------------------------------

def identify_animal(root):
    current = root
    # TODO 5:
    # Continue while current is not a leaf node.
    #
    # Ask the question stored in current.text.
    #
    # YES -> move left
    # NO  -> move right
    #
    # Reject invalid answers.
    while current.left is not None and current.right is not None: #current is not a leaf node; it has children
        answer = input(current.text + " (yes/no)" ).strip().lower() 
        if answer == "yes":
            current = current.left
        elif answer == "no":
            current = current.right
        else:
            print("Invalid answer. Please enter 'yes' or 'no'.")

    print("Animal identified:", current.text)

# --------------------------------------------
# Count Tree Nodes
# --------------------------------------------
def count_nodes(node):
    # TODO 6:
    # Use recursion to count every node.
    if node is None:
        return 0
    left_count = count_nodes(node.left)
    right_count = count_nodes(node.right)
    return 1 + left_count + right_count  # count the root node plus left and right subtrees


# --------------------------------------------
# Display All Animal Classifications
# --------------------------------------------

def show_animals(node):
    # TODO 7:
    # Use recursion.
    #
    # Print only leaf nodes.
    #
    # Do not print question nodes.
    if node is None:
        return
    if node.left is None and node.right is None: # node is a leaf node
        print(node.text)                         # p
        return
    show_animals(node.left)  # recursively show animals in the left subtree
    show_animals(node.right)  # recursively show animals in the right subtree

# --------------------------------------------
# Add a New Animal
# --------------------------------------------
def add_animal(root):
    print("\nAdd a New Animal")

    # TODO 8:
    #
    # Ask the researcher:
    #
    # 1. Which existing animal should be replaced
    #    by a new decision?
    #
    # 2. What is the new animal?
    #
    # 3. What YES/NO question distinguishes
    #    the new animal from the existing animal?
    #
    # 4. Does YES mean the new animal?
    #
    # Locate the existing animal leaf.
    #
    # Replace that leaf's text with the new question.
    #
    # Create two child nodes:
    # one for the existing animal and
    # one for the new animal.
    #
    # Use left = YES and right = NO.
    existing_animal = input("Which existing animal should be replaced? ").strip()
    
    def search_animal(node):
        if node is None:
            return None
        if node.left is None and node.right is None and node.text.lower() == existing_animal.lower():
            return node
        search_left = search_animal(node.left) 
        if search_left is not None: 
            return search_left
        search_right = search_animal(node.right)
        return search_right 
        
    found_animal = search_animal(root) # assigns the result of the search to found_animal
    if found_animal is None:            
        print("Animal not found in the tree.")
        return

    old_animal = found_animal.text # stores the text of the found animal in old_animal so that it can be used later when creating the new nodes

    new_animal = input("What is the new animal? ").strip()
    question = input("Enter a distinguishing yes/no question: ").strip()
    yes_meaning = input("Does YES mean the new animal? (yes/no) ").strip().lower()
    if yes_meaning != "yes" and yes_meaning != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    found_animal.text = question # updates the text of the found animal node to the new question

    old_node = DecisionNode(old_animal) # creates a new DecisionNode for the old animal
    new_node = DecisionNode(new_animal) # creates a new DecisionNode for the new animal

    # Connect the new nodes based on the user's input about which animal corresponds to a "yes" answer.
    if yes_meaning == "yes":
        found_animal.left = new_node
        found_animal.right = old_node
    else:
        found_animal.left = old_node
        found_animal.right = new_node

    print("New animal " + new_animal + " added successfully!")
 
# --------------------------------------------
# Main Menu
# --------------------------------------------
def main():
    root = build_tree()
    while True:
        print("\n==============================")
        print(" SMART WILDLIFE IDENTIFIER")
        print("==============================")
        print("1. Identify an Animal")
        print("2. Count Tree Nodes")
        print("3. Show Possible Animals")
        print("4. Add New Animal")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            identify_animal(root)
        elif choice == "2":
            print("Total nodes:", count_nodes(root))
        elif choice == "3":
            show_animals(root)
        elif choice == "4":
            add_animal(root)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid menu selection.")

# --------------------------------------------
# Start Program
# --------------------------------------------
if __name__ == "__main__":
    
    
    main()
    '''
    root = build_tree()
    print(root.text)
    print(root.left.text)
    print(root.right.text)
    print(root.left.left.text)
    '''
    