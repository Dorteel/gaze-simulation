class BVH_Writer():
    def __init__(self, input_file):
        self.file = None
        self.input = input_file
        self.motion_line_index = -1
        self.read_bvh()
        self.output = None

    def read_bvh(self):
        try:
            with open(self.input, 'r') as input_file:
                self.file = input_file.readlines()

                for i, line in enumerate(self.file):
                    if line.strip() == "MOTION":
                        self.motion_line_index = i
                        self.output = self.file[:self.motion_line_index+3]
                        break
            print(self.output)

        except FileNotFoundError:
            print(f"File '{self.input}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def construct_bvh(self, output_name):
        pass


if __name__ == "__main__":
    bvh_writer = BVH_Writer('walk.bvh')