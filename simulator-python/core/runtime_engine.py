
class RunTimeEngine:
    __instance = None

    def __init__(self):
        if RunTimeEngine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.nodes = []
            self.simulator_activation = False
            self.rounds = 0
            self.current_id = 1
            self.is_engine_active = False
            RunTimeEngine.__instance = self

    @staticmethod
    def getInstance():
        if RunTimeEngine.__instance == None:
            RunTimeEngine()
        return RunTimeEngine.__instance

    def run_simulator(self):
        self.is_engine_active = True
        self.simulator_activation = True
        while (self.simulator_activation):
            self.next_round()

    def stop_simulator(self):
        self.simulator_activation = False

    def run_simulator_step(self):
        self.is_engine_active = True
        self.next_round()

    def next_round(self):
        self.rounds += 1
        for node in self.nodes:
            node.handle_messages()

    def get_nodes(self):
        return self.nodes

    def get_rounds(self):
        return self.rounds

    def get_node_by_id(self, id):
        for node in self.nodes:
            if(node.ID == id):
                return node

    def init_node(self, node):
        self.nodes.append(node)

    def get_node_id(self):
        curr_id = self.current_id
        self.current_id += 1
        return curr_id