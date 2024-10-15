def ArrayChalenge(strArr):
    #This initializes an empty dictinary called children to store each parent node key 
    
    children = {}
    #Intializes an empty set called parent and all_nodes to keep track of all nodes and to store every nodes that appear in the input
    
    parents = set()
    all_nodes = set()
    #To process each parent child relationship in strarr each pair represents a relationship 
    
    for pair in strArr:
        #Extracts the child and parents pair.strip to remove the parentheses and separates the child and parent the map function is to ensure both values are integer
        
        child, parent = map(int, pair.strip('()').split(','))
        #keep track of unique nodes
        
        all_nodes.add(child)
        all_nodes.add(parent)
    #It will check whether parent have an empty children and to store an empty list to store a children 
    
    if parent not in children:
        children[parent] = []
    #Checks if the parent has two children if it does it returns false since it's a binary tree node can't have more than two
    
    if len(children[parent]) >= 2:
        return "false"
    #add the current child and add the child nodes to the parents set, making it as node
    
    children[parent].append(child)
    parents.add(child)
    #subtract all known children from all nodes to find the root nodes a root node is a node that is not child of any other node
    
    root_candidates = all_nodes - parents
    if len(root_candidates) != 1:
        return "false"
    return "true"
print(ArrayChallenge(input()))
