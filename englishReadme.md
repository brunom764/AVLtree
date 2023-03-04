# AVLtree

Implementation of an AVL tree using Python with functions to insert, rotate, balance, remove, and display in order.

## Problem Statement
After exercising your programming skills so much in the first semester of Computer Science, it's time to take the dreaded Algorithms and Data Structures course. In this sieve, you know that you must do your best to understand the subjects taught by the professor and still perform the practical activities within the stipulated deadline. However, everyone knows that life is a collaborative experience, and for students, it's no different.

To ensure that you and your friends have the most profitable experience possible, you decide to create a mutual aid network in which members help each other through the challenges that the semester proposes. To do this, you develop a system to register each of the participants in this organization to manage their position in the social tree and which other students each should help.

The system, affectionately called JUPAL, has three basic functions: search, insert, and remove the name of a member. At the beginning of the system's implementation, you realize that the situation of some "top" students quickly becomes unsustainable because many people begin to depend on them, and the system becomes unbalanced. To expedite these processes and ensure the emotional stability of everyone involved, you decide to use a famous software engineering structure that is perfect for this situation: the balanced AVL tree.

As you well know, AVL trees automatically balance their leaves every time an insertion or removal is made to always keep the height of all approximately equal. Following this reasoning, the system is capable of keeping all members happy, without overloads happening on one side or the other of the tree.

## DESCRIPTION OF IMPLEMENTATION
You must implement a balanced AVL tree with a stable balance factor, such that, for all nodes in the tree: -1 <= f.b. <= 1. For this, it is stipulated that the balance factor of each given node is defined as: f.b(Node) = height(Node->right) - height(Node->left). Some important points:

The height of a null node is given as 0;
The height of a leaf is 1;
The height of any node is the maximum value between the height of the node to its right and the node to its left, plus 1.
Each student in your tree must be represented by a string corresponding to their name, and the ordering of nodes should follow the standard string priority (alphabetical, lexicographic).

WARNING: Since we are dealing with an AVL tree, insertion and removal will be done in a similar way to inserting and removing from a regular binary search tree, but after each operation, the program must check if that node is balanced according to the relationship required by the definition of the structure. If not, a rotation should be made for it to occur.

CHALLENGE: Insert into the code a function that prints to the user the complete tree when the VER command is entered (very similar to what happens with FIM). If you want to go further, make a VER <name> command that prints the tree starting from a certain node (i.e., prints a node and its descendants). The way the printing is done is up to each one, but I suggest something that indicates the node and its (up to) two children, like "Nx helps Ny and Nz." or "Nx helps Ny" or "Nx doesn't help anyone." And do this recursively for each child. The code lines related to this may be commented out or not, as the function will not be called by the Dikastis inputs.
  
 ## Input
Your program should read inputs repeatedly until the command FIM (END in English) is called. The possible commands list is as follows:

• INSERIR <name>: Inserts a node with the value <name>
  
• DELETAR <name>: Deletes a node with the value <name>
  
• MINIMO: Returns the string with the lowest lexicographic value
  
• MAXIMO: Returns the string with the highest lexicographic value
  
• ALTURA: Returns the total height of the tree, starting from the root
  
• FIM: Ends the program
  
  
## Output
Each command from the previous list will have a specific return, as follows:

• INSERIR <name>:
If <name> does not exist in the tree: <name> INSERIDO

If <name> already exists in the tree: <name> JA EXISTE

• DELETAR <name>:
If <name> exists in the tree: <name> DELETADO

If <name> does not exist in the tree: <name> NAO ENCONTRADO

• MINIMO:
If the tree is not empty: MENOR: <name>

If the tree is empty: ARVORE VAZIA

• MAXIMO:
If the tree is not empty: MAIOR: <name>

If the tree is empty: ARVORE VAZIA

• ALTURA:
ALTURA: <treeheight>

• FIM:
If the tree is not empty: <list of remaining nodes in the tree, in order>

If the tree is empty: ARVORE VAZIA
