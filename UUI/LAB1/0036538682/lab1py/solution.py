import sys, argparse
import time
import heapq

class Heuristic:
    algorytham=None
    file_path_heuristic=None
    file_path_states=None
    opti=False
    consistent=False
    start_state=None
    end_state=None
    state_graf=None
    heuristic_weight=None
    p_time=None
    def __init__(self):
        self.state_graf={}
        self.heuristic_weight={}
        self.p_time=time.time()
    def main(self, args):
        parser=argparse.ArgumentParser()
        parser.add_argument("--alg", nargs="?", choices=["bfs","ucs","astar"], help="Algoritam pretrage")
        parser.add_argument("--ss",nargs="?", help="opisnik prostora stanja")
        parser.add_argument("--h", nargs="?", help="opisnik heuristike")
        parser.add_argument("--check-optimistic", action="store_true", help="zastavica za provjeru optimisticnosti")
        parser.add_argument("--check-consistent", action="store_true", help="zastavica za provjeru konzistentnosti")
        pars_args = parser.parse_args(args)
        self.file_path_heuristic=pars_args.h
        self.file_path_states=pars_args.ss
        self.opti=getattr(pars_args,"check_optimistic")
        self.consistent=getattr(pars_args,"check_consistent")
        self.algorytham = pars_args.alg
        # print(f"finished Load in: {time.time()-self.p_time}")
        # print(pars_args.alg)
        # print(self.consistent)
        # print(self.opti)
        # print(self.file_path_heuristic)
        # print(self.file_path_states)
        if self.file_path_states != None :
            self.load_states()
        if self.file_path_heuristic != None:
            self.load_heuristics()

        if(not self.opti and not self.consistent):
            if(self.algorytham=="bfs"):
                resault_tree, vs_len=self.bfs()
                if(resault_tree!=None):
                    path,vs_len,cost=self.bfs_clean(resault_tree,vs_len)
                    self.format_print(path,vs_len,cost)
                else:
                    self.format_print_fale()

            if(self.algorytham=="ucs"):
                    resault, vs_len, cost=self.ucs()
                    if(resault!=None):
                        self.format_print(resault, vs_len, cost)
                    else:
                        self.format_print_fale()

            if(self.algorytham=="astar"):
                resault, vs_len, cost=self.a_star()
                if(resault!=None):
                    self.format_print(resault, vs_len, cost)
                else:
                    self.format_print_fale()
        elif(self.opti):
            self.check_optimistic()
        elif(self.consistent):
            self.check_consistent()
        return
    

    def load_states(self):
        with open (self.file_path_states,"r") as r:
            all_lines = r.readlines()

        lines=[] # remove coments
        for line in all_lines:
            if '#' not in line:
                lines.append(line)

        self.start_state=lines[0].replace("\n","")
        self.end_state=set(lines[1].replace("\n","").split(" "))
        entry :str
        for entry in lines[2:]:
            line=entry.split(" ")
            state=line[0].rstrip(":\n")
            next_states=[]
            for x in line[1:]:
                next_state=tuple(x.replace("\n","").split(","))
                next_states.append(next_state)
            if(self.algorytham=="bfs"):
                next_states=sorted(next_states)
            elif(self.algorytham=="ucs"):
                next_states=sorted(next_states,key = lambda x: float(x[1]))
            self.state_graf[state]=next_states
        # print(self.state_graf)
        return

    def load_heuristics(self):
        with open (self.file_path_heuristic,"r") as r:
            all_lines = r.readlines()

        lines=[] # remove coments
        for line in all_lines:
            if '#' not in line:
                lines.append(line)
        entry :str
        for entry in lines:
            x=entry.split(" ")
            self.heuristic_weight[x[0].rstrip(":")]=x[1].replace("\n","")
        # print(self.heuristic_weight)
        return
    
    def bfs(self):# pretrazivanje u sirinu
        visited=set()
        start=self.start_state
        target=self.end_state
        paths=self.state_graf
        visited.add(start)
        tree_depth=0
        current_lvl={}
        current_lvl[0]={start:(None,0)}
        if(target==start):
            return current_lvl,0
        while(tree_depth<=len(paths)):
            # print(f"level {tree_depth+1} start: {time.time()-self.p_time}")
            current_lvl[tree_depth+1]={}
            for sts in current_lvl[tree_depth]:
                try:
                    for x in paths[sts]:
                        if(x[0] in target):
                            current_lvl[tree_depth+1][x[0]]=(sts,x[1])
                            return current_lvl, len(visited)+1
                        else:
                            if(x[0] not in visited):
                                visited.add(x[0])
                                current_lvl[tree_depth+1][x[0]]=(sts,x[1])    
                except:
                    return None, None
            tree_depth=tree_depth+1
        return None,None
    def bfs_clean(self, resault_tree, visited):
        path=[]
        next_p=None
        cost=0
        # for x in resault_tree:
        #     print(f"{x}: {resault_tree[x]}")
        for i,x in enumerate(reversed(resault_tree)):
            if(i==0):
                path.append(list(reversed(resault_tree[x].keys()))[0])
                next_p=resault_tree[x][path[i]][0]
                cost=cost+float(resault_tree[x][path[i]][1])
            else:
                path.append(next_p)
                next_p=resault_tree[x][path[i]][0]
                cost=cost+float(resault_tree[x][path[i]][1])
        return path, visited, cost

    def ucs(self):
        visited=set()
        start=self.start_state
        target=self.end_state
        paths=self.state_graf
        visited.add(start)
        nodes=[]
        passed_nodes={}
        path=[]
        if(target==start):
            return start,1,0 #path, visited, cost
        else:
            heapq.heappush(nodes,(0,(start,None))) #cost node, parent
            while(len(visited)<=len(paths)):
                cost, lowest=heapq.heappop(nodes)
                passed_nodes[lowest[0]]=lowest[1]
                visited.add(lowest[0])
                if(lowest[0] in target):
                    path.append(lowest[0])
                    prev=lowest[1]
                    while(prev!=None):
                        prev_p=passed_nodes[prev]
                        path.append(prev)
                        prev=prev_p
                    # print(f"ended ucs:{time.time()-self.p_time}")
                    return path, len(passed_nodes), cost
                else:
                    try:
                        for x in paths[lowest[0]]:
                            if(x[0] not in visited):
                                # visited.add(x[0])
                                next_cost=cost+float(x[1])
                                heapq.heappush(nodes, (next_cost,(x[0],lowest[0])))
                    except:
                        return None,None,None
        return None,None,None
    

    def a_star(self):
        visited=set()
        start=self.start_state
        target=self.end_state
        paths=self.state_graf
        heuristic=self.heuristic_weight
        visited.add(start)
        nodes=[]
        passed_nodes={}
        path=[]
        if(target==start):
            return start,1,0 #path, visited, cost
        else:
            heapq.heappush(nodes,(0,(start,None,0))) #cost node, parent, path_cost
            while(len(visited)<=len(paths)):
                cost, lowest=heapq.heappop(nodes)
                passed_nodes[lowest[0]]=lowest[1]
                visited.add(lowest[0])
                if(lowest[0] in target):
                    path.append(lowest[0])
                    # print(lowest[1])
                    prev=lowest[1]
                    while(prev!=None):
                        prev_p=passed_nodes[prev]
                        path.append(prev)
                        # print(path)
                        prev=prev_p
                    # print(f"ended astar:{time.time()-self.p_time}")
                    return path, len(passed_nodes), lowest[2]
                else:
                    try:
                        for x in paths[lowest[0]]:
                            if(x[0] not in visited):
                                # visited.add(x[0])
                                p_cost_next=float(lowest[2])+float(x[1])
                                # print(p_cost_next)
                                next_cost=float(p_cost_next) #+ float(x[1])
                                next_prio=next_cost+float(heuristic[x[0]])
                                heapq.heappush(nodes, (next_prio,(x[0],lowest[0],p_cost_next)))
                        # print("visited:", visited)
                        # print(nodes[:4])
                    except:
                        return None,None,None
        return None,None,None
    
    def check_optimistic(self):
        paths=self.state_graf
        heuristics=self.heuristic_weight
        true_cost={}
        optimistic=True
        for x in paths:#sorted(paths.keys(), reverse=True):
            self.start_state=x
            path,visited,cost=self.ucs()
            # print(x,":",path, ":",cost)
            if cost == None:
                cost=0
            true_cost[x]=cost
        for x in reversed(true_cost):
            if(true_cost[x]>=float(heuristics[x])):
                print(f"[CONDITION]: [OK] h({x}) <= h*: {float(heuristics[x])} <= {float(true_cost[x])}")
            else:
                print(f"[CONDITION]: [ERR] h({x}) <= h*: {float(heuristics[x])} <= {float(true_cost[x])}")
                optimistic=False
        if(optimistic):
            print("[CONCLUSION]: Heuristic is optimistic.")
        else:
            print("[CONCLUSION]: Heuristic is not optimistic.")
        return
        

    def check_consistent(self):
        paths=self.state_graf
        heuristics=self.heuristic_weight
        consistent=True
        for x in sorted(paths.keys(), reverse=True):
            sorted_next=sorted(paths[x])
            for next_node in sorted_next:
                c=float(next_node[1])
                heu_cur=float(heuristics[x])
                heu_next=float(heuristics[next_node[0]])
                if(heu_cur<=heu_next+c):
                    print(f"[CONDITION]: [OK] h({x}) <= h({next_node[0]}) + c: {heu_cur} <= {heu_next} + {c}")
                else:
                    print(f"[CONDITION]: [ERR] h({x}) <= h({next_node[0]}) + c: {heu_cur} <= {heu_next} + {c}")
                    consistent=False
        if(consistent):
            print("[CONCLUSION]: Heuristic is consistent.")
        else:
            print("[CONCLUSION]: Heuristic is not consistent.")
        return
    


    def format_print(self, path, visited, cost):
        if(self.algorytham=="astar"):
            alg_str=str(self.algorytham).upper()[0]+"-"+str(self.algorytham).upper()[1:]
            print(f"# {alg_str} {self.file_path_heuristic}")
        else:
            print(f"# {str(self.algorytham).upper()}")
        print("[FOUND_SOLUTION]: yes")
        print(f"[STATES_VISITED]: {visited}")
        print(f"[PATH_LENGTH]: {len(path)}")
        print(f"[TOTAL_COST]: {float(cost)}")
        str_path=""
        for x in reversed(path):
            str_path=str_path + str(x) +" => "
        str_path=str_path.rstrip(" => ")
        print(f"[PATH]: {str_path}")
        return

    def format_print_fale(self):
        if(self.algorytham=="astar"):
            alg_str=str(self.algorytham).upper()[0]+"-"+str(self.algorytham).upper()[1:]
            print(f"# {alg_str} {self.file_path_heuristic}")
        else:
            print(f"# {str(self.algorytham).upper()}")
        print("[FOUND_SOLUTION]: no")  
        return           


if __name__== "__main__":
    x=Heuristic()
    x.main(sys.argv[1:])