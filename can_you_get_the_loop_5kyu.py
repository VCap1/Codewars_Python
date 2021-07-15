def loop_size(node):
    res = []
    while node:
        if node not in res:
            res.append(node)
            node = node.next
        else:
            return len(res) - res.index(node)
