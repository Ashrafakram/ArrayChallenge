def ArrayChalenge(strArr):
    children = {}
    parents = set()
    all_nodes = set()
    for pair in strArr:
        child, parent = map(int, pair.strip('()').split(','))
        all_nodes.add(child)
        all_nodes.add(parent)
    if parent not in children:
        children[parent] = []
    if len(children[parent]) >= 2:
        return "false"
    children[parent].append(child)
    parents.add(child)
    root_candidates = all_nodes - parents
    if len(root_candidates) != 1:
        return "false"
    return "true"
print(ArrayChallenge(input()))
