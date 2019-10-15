from core.utils.threads_manager import use_threads
from core.custom_global_manager import CustomGlobalManager

class RunTimeEngine:
    __instance = None

    def __init__(self):
        if RunTimeEngine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.nodes = []
            self.nodes_ids_mapping = {}
            self.is_simulator_in_running = False
            self.rounds = 0
            self.current_id = 0
            self.is_engine_active = False
            RunTimeEngine.__instance = self

    @staticmethod
    def getInstance():
        if RunTimeEngine.__instance == None:
            RunTimeEngine()
        return RunTimeEngine.__instance

    def run_simulator(self):
        self.is_simulator_in_running = True
        while (self.is_simulator_in_running):
            self.run_simulator_step()

    def stop_simulator(self):
        self.is_simulator_in_running = False

    def run_simulator_step(self):
        self.next_round()

    def next_round(self):
        CustomGlobalManager.get_custom_global().pre_round()
        self.rounds += 1
        self.execute_nodes(self.nodes)
        CustomGlobalManager.get_custom_global().post_round()

    @staticmethod
    @use_threads
    def execute_nodes(nodes):
        for node in nodes:
            node.handle_messages()

    def get_nodes(self):
        return self.nodes

    def get_rounds(self):
        return self.rounds

    def get_node_by_id(self, id):
        if self.nodes_ids_mapping.get(id) is not None:
            return self.nodes_ids_mapping[id]
        for node in self.nodes:
            if(node.ID == id):
                return node

    def init_node(self, node):
        self.nodes_ids_mapping[node.ID] = node;
        self.nodes.append(node)

    def generate_node_id(self):
        curr_id = self.current_id
        self.current_id += 1
        return curr_id

    def clean_nodes(self):
        self.nodes = []
        self.current_id = 0
