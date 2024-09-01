import math
from graph import Graph
from vertex import Vertex
from cow import Cow
from paintball import Paintball
import sys

"""
CSCI-603 Lab 9: Holi Cow!

This program is graph simulation where we need to find out in a field full of cows and paint balls that 
which paintball will color the most cows. Over here every object on the field will act a vertex of a graph

One paintball can trigger another paintball and can color the cow

author: Kapil Sharma ks4643
"""


class HoliCow:
    __slots__ = 'graph', 'color_list', 'cow_list'

    def __init__(self):
        self.graph = Graph()
        self.color_list = []
        self.cow_list = []

    def run_simulation(self, vertices):
        """
        This function is used to start the code simulation by passing down data to other functions
        :param vertices: takes vertices to perform the simulation on
        :return: None
        """
        index = -1
        for vertex in vertices:
            index += 1
            if vertex[0] == 'cow':
                cow = Cow(vertex[1], vertex[2], vertex[3])
                self.graph.add_vertex(index, cow)
                self.cow_list.append(index)
            elif vertex[0] == 'paintball':
                paintball = Paintball(vertex[1], vertex[2], vertex[3], vertex[4])
                self.graph.add_vertex(index, paintball)
                self.color_list.append(index)
        print("Field of Dreams")
        print("Number of vertices: ", (len(self.cow_list) + len(self.color_list)), ", cows: ", len(self.cow_list)
              , ", paint balls: ", len(self.color_list))
        print("------------------------------------------------------------------------------------------------")
        self.add_neighbors()
        max_list, max_color = self.traverse_the_graph()
        self.display_final_result(max_list, max_color)

    def find_distance_formaula(self, source_vertex, destination_vertex):
        """
        This takes source and destination vertex and applies distance formula between them to check whether
        the two vertex should be connected or not in the first place
        If the source vertex radius is less than the distance between them then the two vertex should be connected
        :param source_vertex: vertex whose radius needs to be checked with the distance, if so destination vertex is
        added in the source vertex
        :param destination_vertex: destination vertex to find the distance between them
        :return: the distance between the two
        """
        source_x = float(source_vertex.x_coordinate)
        source_y = float(source_vertex.y_coordinate)
        destination_x = float(destination_vertex.x_coordinate)
        destination_y = float(destination_vertex.y_coordinate)
        return math.sqrt(math.pow((destination_x - source_x),2) + math.pow((destination_y - source_y),2))

    def add_neighbors(self):
        """
        This function creates edges in the graph and connects all the vertices by adding neighbors in the vertex
        It also adds everything to the graph
        :return: None
        """
        graph = self.graph
        vert_dict_length = len(graph.get_vertices())
        for source in range(vert_dict_length):
            source_vertex = graph.get_vertex(source).get_id()
            if isinstance(source_vertex, Cow):
                continue
            for destination in range(vert_dict_length):
                destination_vertex = graph.get_vertex(destination).get_id()
                distance = self.find_distance_formaula(source_vertex, destination_vertex)
                if source_vertex == destination_vertex:
                    continue
                elif isinstance(destination_vertex, Cow) and isinstance(source_vertex, Paintball):
                    if distance <= float(source_vertex.radius):
                        graph.add_edge(source, source_vertex, destination, destination_vertex)
                elif isinstance(destination_vertex, Paintball) and isinstance(source_vertex, Paintball):
                    if distance <= float(source_vertex.radius):
                        graph.add_edge(source, source_vertex, destination, destination_vertex)
        print(graph)

    def traverse_the_graph(self):
        """
        This function sends colors one by one to test which has the optimal solution
        It also finds the optimal solution amongst all the solution recieved after ther traversal


        :return: color with the optimal solution and list of cows that it painted
        """
        graph = self.graph
        print("Beginning Simulation")
        max_count = 0
        max_list = []
        max_color = None
        for i in self.color_list:
            start_color = graph.get_vertex(i)
            print("Triggering ", start_color.get_id(), "paint ball...")
            cow_count = find_path_dfs(start_color)
            if max_count < len(cow_count):
                max_count = len(cow_count)
                max_list, max_color = cow_count, start_color
        return max_list, max_color

    def display_final_result(self, max_list, max_color):
        """
        This function is used to display results that is the optimal solution and the cows that are painted
        It also shows cows that are not painted with an empty set
        :param max_list: list of color with the optimal solution
        :param max_color: color itself
        :return: None
        """
        print("Results: ")
        if max_color is not None:
            print("Triggering the ", max_color.get_id(), " paint ball is the best choice with ", len(max_list),
                  " total paint on the cows")
            cows_dict = {}
            cow_keys = []

            for key in self.cow_list:
                cow_keys.append(self.graph.get_vertex(key).get_id())

            for keys in max_list:
                cows_dict[keys[1]] = []

            for keys in max_list:
                if keys[1] in cows_dict.keys():
                    cows_dict[keys[1]].append(keys[0])

            for cows_and_colors in cows_dict.keys():
                result = str(cows_and_colors) + "'s colors: { "
                for val in cows_dict[cows_and_colors]:
                    result += str(val) + ", "
                result += " }"
                print(result)

            for key in cow_keys:
                if key not in cows_dict:
                    print(key, "'s colors: {}")
        else:
            print("No cows were painted that is why there is no optimal solution")
            for key in self.cow_list:
                print(self.graph.get_vertex(key).get_id(),"'s colors: {}")



def __find_path_dfs(current: Vertex, visited: set[Vertex], cow_painted, paint_stack):
    """
    Private recursive helper function that finds the path, if one exists,
    from the current vertex to the end vertex
    :param current: The current vertex in the traversal
    :param end: The destination vertex
    :param visited: the vertices already visited
    :return: A list of Vertex objects from start to end, if a path exists, otherwise None
    """
    if paint_stack != current:
        if isinstance(paint_stack.get_id(), Paintball) and isinstance(current.get_id(), Cow):
            cow_painted.append([paint_stack.get_id(), current.get_id()])
            print("\t", current.get_id(), " is painted ", paint_stack.get_id())
        elif isinstance(paint_stack.get_id(), Paintball) and isinstance(current.get_id(), Paintball):
            print("\t", current.get_id(), " paint ball is getting triggered by ", paint_stack.get_id()," paint ball")
    paint_stack = current
    for neighbour in current.get_neighbors():
        if neighbour not in visited:
            visited.add(current)
            __find_path_dfs(neighbour, visited, cow_painted, paint_stack)
    return cow_painted

def find_path_dfs(start: Vertex) -> dict[Cow: Paintball]:
    """
    Find a path, if one exists, from a start to end vertex.
    :param start: the start vertex
    :param end: the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    visited = set()
    visited.add(start)
    cow_painted = []
    paint_stack = start
    return __find_path_dfs(start, visited, cow_painted, paint_stack)


def read_files_from_file(file_name: str) -> list:
    """
    This function reads file from the text file passed from the arguments
    :param file_name: name of the text file from where the file will be read
    :return: secret keyword
    """
    open_file = open(file_name)
    file_content = open_file.readlines()
    vertexes = []
    for line in file_content:
        vertexes.append(line.strip().split('\n')[0].split(" "))
    return vertexes


def main():
    if len(sys.argv) != 2:
        print("Usage: python holicow.py {filename}")
        return None
    try:
        holi_cow = HoliCow()
        vertexes = read_files_from_file(sys.argv[1])
        holi_cow.run_simulation(vertexes)

    except FileNotFoundError:
        print("File not found")
        return None


if __name__ == "__main__":
    main()