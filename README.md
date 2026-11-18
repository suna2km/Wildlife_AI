# Wildlife_AI
# Smart Wildlife Identifier
 
A Python program that uses a binary decision tree to identify animals by asking yes/no questions. Researchers can also teach it new animals while it runs.

 <b>Table of Content</b>
- [How it works](#how-it-works)
- [Author](#author)
- [Requirements](#requirements)
- [Running the programd](#running-the-program)
- [Menu options](#menu-options)
- [Code overview](#code-overview)
- [Concepts Demonstrated](#concepts-demonstrated)

## How It Works
 
The program stores its knowledge as a tree of `DecisionNode` objects. Each node holds some text and two links:
 
- **Question nodes** hold a yes/no question and have two children.
- **Leaf nodes** hold an animal classification and have no children.
- **Left = YES, Right = NO** throughout the tree.
### Starting Tree
 
```
                 Does it have feathers?
                /                      \
              YES                      NO
              /                          \
        Can it fly?              Does it live in water?
        /        \                  /             \
      YES        NO               YES             NO
      /            \              /                 \
    Bird        Penguin        Fish              Mammal
```
 
The tree has 7 nodes: 3 questions and 4 animals.
 
## Requirements
 
- Python 3.8 or newer
- No external libraries
## Running the Program
 
```
python main.py
```
 
## Menu Options
 
| Option | Name | What it does |
|--------|------|--------------|
| 1 | Identify an Animal | Asks yes/no questions, following the tree until it reaches an animal. Invalid answers are rejected. |
| 2 | Count Tree Nodes | Uses recursion to count every node in the tree. |
| 3 | Show Possible Animals | Uses recursion to print only the leaf nodes (animals), not questions. |
| 4 | Add New Animal | Teaches the tree a new animal (see below). |
| 5 | Exit | Ends the program. |
 
## Adding a New Animal
 
Option 4 converts an existing animal (a leaf) into a question node with two new leaves. For example, to separate dolphins from fish:
 
1. Enter the existing animal: `Fish`
2. Enter the new animal: `Dolphin`
3. Enter a distinguishing question: `Does it breathe air?`
4. Does YES mean the new animal? `yes`
Before:
 
```
Does it live in water?
        |
       YES
        |
      Fish
```
 
After:
 
```
Does it live in water?
        |
       YES
        |
  Does it breathe air?
      /        \
    YES         NO
    /             \
 Dolphin          Fish
```
 
The existing Fish node is edited in place: its text becomes the new question, and two new nodes are attached under it. Nothing above it in the tree needs to change. If the animal isn't found, or the yes/no answer is invalid, the tree is left unchanged.
 
After adding the dolphin, the tree has 9 nodes.
 
## Code Overview
 
| Part | Purpose |
|------|---------|
| `DecisionNode` | Class for one node: `text`, `left` (YES), `right` (NO) |
| `build_tree()` | Builds and connects the starting tree, returns the root |
| `identify_animal(root)` | Walks the tree from the root based on user answers |
| `count_nodes(node)` | Recursively counts all nodes |
| `show_animals(node)` | Recursively prints leaf nodes only |
| `add_animal(root)` | Searches for a leaf and converts it into a question with two new leaves |
| `main()` | Displays the menu and runs the program loop |
 
## Concepts Demonstrated
 
- Binary trees and node references
- Recursion (counting, searching, and displaying)
- Modifying a tree by changing node references, similar to BST insert and delete
- Input validation

 ## Author
 **Suna Aregay**  
GitHub: [@suna2km](https://github.com/suna2km)

