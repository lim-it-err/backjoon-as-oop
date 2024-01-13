from typing import List
from collections import deque

class Node:
    def __init__(self, iid, ability):
        self.iid = iid
        self.ability = ability
        self.members = []
        self.leader = None
        self.participate = False
        self.total_ability = ()
        
    def add_leader(self,leader):
        if self.leader:
            raise Exceptions("Leader is already rolled")
        self.leader = leader
    
    def add_member(self, member):
        # print("add_member", self.iid, member.iid)
        self.members.append(member)


    def is_leader(self, ):
        return bool(self.members)
    
class Tree:
    def __init__(self, sales):
        self.member_nodes = [Node(i+1, sales[i]) for i in range(len(sales))]
        self.participate = [False] + [False for _ in range(len(sales))] #Make index
        self.sales = sales
        self.best_price = 1e10 #32log2 ~=9

    def add(self, link):
        src, dst = link
        self.member_nodes[src-1].add_member(self.member_nodes[dst-1])
        self.member_nodes[dst-1].add_leader(self.member_nodes[src-1])
        
    def dfs_traverse(self):
        self.dfs(self.member_nodes[0]) 
        # for i, member in enumerate(self.member_nodes):
        #     print(i+1, member.total_ability)
        return min(self.member_nodes[0].total_ability)
    
    def dfs(self, manage_node):
        """
        calculate node's cheapest price, and update it into node by tuple.
        """
        members = manage_node.members
        if not members:
            manage_node.total_ability = (manage_node.ability, 0)
            return
        for member in members:
            self.dfs(member)
        needs_participant = True
        member_ability = []
        for member in members:
            member_ability.append(member.total_ability)
            if member.participate:
                needs_participant = False
        
        if not needs_participant:
            sum_ability = 0
            for member in members:
                if member.participate:
                    sum_ability += member.total_ability[0]
                else:
                    sum_ability+=min(member.total_ability)
            manage_node.total_ability = (sum_ability+manage_node.ability, sum_ability)
        else:
            sum_ability = 0
            _deltas = []
            for ability in member_ability:
                _deltas.append(ability[0]-ability[1])
            weak_idx = _deltas.index(min(_deltas))
            weak_obj = None
            for i, member in enumerate(members):
                if i == weak_idx:
                    weak_obj = member
                    sum_ability += member.total_ability[0]
                    members[i].participate = True
                else:
                    sum_ability += member.total_ability[1]
            manage_node.total_ability = (sum_ability-weak_obj.total_ability[0]+weak_obj.total_ability[1]+manage_node.ability, sum_ability)
                
        
        if manage_node.total_ability[0]<manage_node.total_ability[1]:
            manage_node.participate = True
            
            
def solution(sales, links):
    answer = 0
    tree = Tree(sales)
    for link in links:
        tree.add(link)
    return tree.dfs_traverse()