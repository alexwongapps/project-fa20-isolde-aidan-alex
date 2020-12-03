from utils import *
from simanneal import Annealer
from random import *
from parse import *
import time

def true_random(graph, stress_budget, start_greedy_at=None):
    size = graph.number_of_nodes()
    if start_greedy_at is None:
        start_greedy_at = size
    students = [i for i in range(size)]
    #origorig = students.copy()
    max_happiness = (None, -1)
    start_time = int(time.time())
    iters = 0
    while int(time.time()) - start_time < 10:
        iters += 1
        #orig = origorig.copy()
        #shuffle(orig)
        shuffle(students)
        for num_rooms in range(1, size + 1):
            #students = orig.copy()
            rooms = [[] for i in range(num_rooms)]
            #for i in range(num_rooms):
            #    rooms[i].append(students.pop(0))
            good = True
            for i in range(start_greedy_at):
                student = students[i]
                valid = False
                to_try = [i for i in range(num_rooms)]
                try_this = -1
                while not valid and len(to_try) > 0:
                    try_this = choice(to_try)
                    if calculate_stress_for_room(rooms[try_this] + [student], graph) <= stress_budget / num_rooms:
                        valid = True
                    to_try.remove(try_this)
                if valid:
                    rooms[try_this] += [student]
                else:
                    good = False
                    break
            for i in range(start_greedy_at, size):
                student = students[i]
                to_place = (-1, -1)
                for room in range(num_rooms):
                    to_gain = calculate_happiness_for_room(rooms[room] + [student], graph) - calculate_happiness_for_room(rooms[room], graph)
                    if to_gain > to_place[1] and calculate_stress_for_room(rooms[room] + [student], graph) <= stress_budget / num_rooms:
                        to_place = (room, to_gain)
                if to_place[0] > -1:
                    rooms[to_place[0]] += [student]
                else:
                    good = False
                    break
            if good:
                rooms = [room for room in rooms if len(room) > 0]
                dic = {}
                for i in range(len(rooms)):
                    dic[i] = rooms[i]
                if is_valid_solution(convert_dictionary(dic), graph, stress_budget, len(rooms)):
                    hap = calculate_happiness(convert_dictionary(dic), graph) 
                    if hap > max_happiness[1]:
                        max_happiness = (rooms, hap)
    print(max_happiness)
    return max_happiness[0] if max_happiness[0] is not None else [[i] for i in range(size)]



def greedy_happiness(graph, stress_budget):
    size = graph.number_of_nodes()
    students = [i for i in range(size)]
    shuffle(students)
    original_students = students.copy()
    max_happiness = (None, -1)
    for num_rooms in range(1, size + 1):
        rooms = [[] for i in range(num_rooms)]
        finish = True
        students = original_students.copy()
        # add first num_rooms students, one per room
        for i in range(num_rooms):
            rooms[i].append(students.pop(0))
        for student in students:
            to_place = (-1, -1)
            for room in range(num_rooms):
                to_gain = calculate_happiness_for_room(rooms[room] + [student], graph) - calculate_happiness_for_room(rooms[room], graph)
                if to_gain > to_place[1] and calculate_stress_for_room(rooms[room] + [student], graph) <= stress_budget / num_rooms:
                    to_place = (room, to_gain)
            if to_place[0] > -1:
                rooms[to_place[0]] += [student]
            else:
                finish = False
                break
        if finish:
            dic = {}
            for i in range(num_rooms):
                dic[i] = rooms[i]
            hap = calculate_happiness(convert_dictionary(dic), graph) 
            if hap > max_happiness[1]:
                max_happiness = (rooms, hap)
    return max_happiness[0]

# greedy alg, half random
def greedy_happiness_half_random(graph, stress_budget):
    size = graph.number_of_nodes()
    students = [i for i in range(size)]
    shuffle(students)
    max_happiness = (None, -1)
    for num_rooms in range(1, size + 1):
        rooms = [[] for i in range(num_rooms)]
        finish = True

        i = 0

        for student in students:
            to_place = (-1, -1)
            can_place = []
            for room in range(num_rooms):
                to_gain = calculate_happiness_for_room(rooms[room] + [student], graph) - calculate_happiness_for_room(rooms[room], graph)
                if calculate_stress_for_room(rooms[room] + [student], graph) <= stress_budget / num_rooms:
                    if to_gain > to_place[1]:
                        to_place = (room, to_gain)
                    can_place.append(room)
            if to_place[0] > -1:
                if i % 2 == 0:
                    rooms[to_place[0]] += [student]
                else:
                    rooms[choice(can_place)] += [student]
            else:
                finish = False
                break
            i += 1

        if finish:
            dic = {}
            for i in range(num_rooms):
                dic[i] = rooms[i]
            hap = calculate_happiness(convert_dictionary(dic), graph) 
            if hap > max_happiness[1]:
                max_happiness = (rooms, hap)
    return max_happiness[0]

class BreakoutProblem(Annealer):

    def __init__(self, graph, stress_budget):
        self.graph = graph
        self.state = Zoom(graph, graph.number_of_nodes(), stress_budget)
        self.stress_budget = stress_budget


    def move(self):
        #dic = {}
        """for i in range(len(self.state.rooms)):
            dic[i] = self.state.rooms[i].students
        if is_valid_solution(convert_dictionary(dic), self.graph, self.stress_budget, len(self.state.rooms)):
           // self.state.move_random_student()
        else:"""
        #self.state.shuffle()
        self.state.move_random_student()
        #self.state.move_from_least_strappiness()
        


        
        #measure stress levels, if the highest avg stress is too large then take a random thing from that and place it in (random/(least stress/happiness score))
        # -a*stress + b*happiness
        # if the stress is too large then we give that a really big stress level -> stress budget 

    def energy(self):
        dic = {}
        for i in range(len(self.state.rooms)):
            dic[i] = self.state.rooms[i].students
        if is_valid_solution(convert_dictionary(dic), self.graph, self.stress_budget, len(self.state.rooms)):
            return -1 * calculate_happiness(convert_dictionary(dic), self.graph)
        else: # does not meet stress requirement
            # return 1
            return max(0, (-1 * self.state.stress_happiness_score()) / 100)
        

class Zoom:
    def __init__(self, graph, num_students, stress_budget, rooms=[]):
        self.rooms = rooms
        self.graph = graph
        self.stress_budget = stress_budget
        self.num_students = num_students
        self.add_all_students()
        #self.add_random_students()
        #self.add_current_sol("outputs/small-65.out")

    def shuffle(self):
        self.rooms.clear()
        self.add_random_students()

    def add_random_students(self):
        lst = self.partition(sample([i for i in range(self.num_students)], self.num_students), randint(1, (self.num_students)/2))
        for element in lst:
            self.rooms.append(Room(self.graph, element.copy()))

    def add_all_students(self):
        for i in range(self.num_students):
            self.rooms.append(Room(self.graph, [i]))

    def add_greedily(self):
        rooms = greedy_happiness(self.graph, self.stress_budget)
        for room in rooms:
            if len(room) > 0:
                self.rooms.append(Room(self.graph, room))

    def add_current_sol(self, path):
        dic = read_output_file(path, self.graph, self.stress_budget)
        rooms = [[] for i in range(self.num_students)]
        for i in range(len(dic)):
            rooms[dic[i]].append(i)
        for room in rooms:
            if len(room) > 0:
                self.rooms.append(Room(self.graph, room))

    def partition(self, lst, n):
        division = len(lst) / float(n)
        return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n)]

    def move_from_avg_least_happy(self):
        rand1, rand2 = self.two_heuristic_rooms() 
        cur_r = self.rooms[rand1]
        new_r = self.rooms[rand2]
        ran_student = choice(cur_r.students)
        cur_r.remove_student(ran_student)
        new_r.add_student(ran_student)

        if cur_r.num_students() == 0:
            self.remove_room(rand1)

    def move_from_least_strappiness(self):
        rand1, rand2 = self.two_heuristic_strappiness_rooms() 
        cur_r = self.rooms[rand1]
        new_r = self.rooms[rand2]
        ran_student = choice(cur_r.students)
        cur_r.remove_student(ran_student)
        new_r.add_student(ran_student)

        if cur_r.num_students() == 0:
            self.remove_room(rand1)

    def move_random_student(self):
        rand1, rand2 = self.two_random_rooms()
        cur_r = self.rooms[rand1]
        new_r = self.rooms[rand2]
        ran_student = choice(cur_r.students)
        cur_r.remove_student(ran_student)
        new_r.add_student(ran_student)

        if cur_r.num_students() == 0:
            self.remove_room(rand1)

    def two_heuristic_rooms(self):
        room1 = min(self.rooms, key=lambda r: r.average_happiness())
        index1 = self.rooms.index(room1)
        index2 = index1

        while index1 == index2:
            index2 = randint(0, self.num_students - 1)
            
            if index2 >= self.num_rooms():
                new_room = Room(self.graph, [])
                self.rooms.append(new_room)
                index2 = self.num_rooms() - 1
            else:
                new_room = self.rooms[index2]
        
        return index1, index2
            
    def two_heuristic_strappiness_rooms(self):
        room1 = min(self.rooms, key=(lambda k: k.stress_happiness_score()))
        index1 = self.rooms.index(room1)
        index2 = index1

        while index1 == index2:
            index2 = randint(0, self.num_rooms())
            
            if index2 >= self.num_rooms():
                new_room = Room(self.graph, [])
                self.rooms.append(new_room)
                index2 = self.num_rooms() - 1
            else:
                new_room = self.rooms[index2]
        
        return index1, index2


    def two_random_rooms(self):
        rand1 = 0
        rand2 = 0
        while rand1 == rand2:
            rand1 = randint(0, self.num_rooms() - 1)
            rand2 = randint(0, self.num_rooms())
            
            if rand2 >= self.num_rooms():
                new_room = Room(self.graph, [])
                self.rooms.append(new_room)
                rand2 = self.num_rooms() - 1
            else:
                new_room = self.rooms[rand2]
        
        return rand1, rand2

    def num_rooms(self):
        return len(self.rooms)

    def remove_room(self, index):
        del self.rooms[index]

    def stress_happiness_score(self):
        return sum([room.stress_happiness_score() for room in self.rooms])
    
    def stress_bound(self, stress_level):
        return stress_level <= self.stress_budget/self.num_rooms()
        
    def __repr__(self):
        return str(self.rooms)



class Room:
    def __init__(self, graph, students=[]):
        self.graph = graph
        self.students = students
    
    def happiness_score(self):
        return calculate_happiness_for_room(self.students, self.graph)

    def add_student(self, student):
        self.students.append(student)
    
    def stress_score(self):
        return calculate_stress_for_room(self.students, self.graph)
        
    def num_students(self):
        return len(self.students)
    
    def random_student(self):    
        return choice(self.students)
        
    def remove_student(self, student):
        self.students.remove(student)
    
    def average_happiness(self):
        return (calculate_happiness_for_room(self.students, self.graph))/(self.num_students())

    def stress_happiness_score(self):
        stress = -1 * STRESS_CONSTANT * calculate_stress_for_room(self.students, self.graph)
        happiness = HAPPINESS_CONSTANT * calculate_happiness_for_room(self.students, self.graph)
        return stress + happiness + ADD_CONSTANT
    
    def __repr__(self):
        return str(self.students)