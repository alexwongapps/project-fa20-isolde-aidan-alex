from utils import *
from simanneal import Annealer
from random import *
class BreakoutProblem(Annealer):

    def __init__(self, graph, stress_budget):
        self.graph = graph
        self.state = Zoom(graph, graph.number_of_nodes())
        self.stress_budget = stress_budget


    def move(self):
        self.state.move_random_student()


    def energy(self):
        dic = {}
        for i in range(len(self.state.rooms)):
            dic[i] = self.state.rooms[i].students
        if is_valid_solution(convert_dictionary(dic), self.graph, self.stress_budget, len(self.state.rooms)):
            return -1 * calculate_happiness(convert_dictionary(dic), self.graph)
        else:
            return 1
        
        

class Zoom:
    def __init__(self, graph, num_students, rooms=[]):
        self.rooms = rooms
        self.graph = graph
        self.num_students = num_students
        self.add_random_students()
        
    def add_random_students(self):
        lst = self.partition([i for i in range(self.num_students)], randint(1, self.num_students - 1))
        for element in lst:
            self.rooms.append(Room(self.graph, element.copy()))

    def add_all_students(self):
        for i in range(self.num_students):
            self.rooms.append(Room(self.graph, [i]))

    def partition(self, lst, n):
        division = len(lst) / float(n)
        return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]

    def move_from_avg_least_happy(self):
        rand1, rand2 = self.two_heuristic_rooms() 
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
            


    def two_random_rooms(self):
        rand1 = 0
        rand2 = 0
        while rand1 == rand2:
            rand1 = randint(0, self.num_rooms() - 1)
            rand2 = randint(0, self.num_students - 1)
            
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
    
    def __repr__(self):
        return str(self.students)