import numpy as np
import shutil

N_FRAMES = 200
YAW_ANGLE = 0
PITCH_ANGLE = 50
N_DOF = 12

def create_movement(angles, n_frames=N_FRAMES, symmetrical=True):
    """
    Create symmetrical movements
    Returns a vector of n_frames long
    """
    if symmetrical:
        output = [x*(angles/(n_frames/2)) for x in range(int(n_frames/2))]
        return output + output[::-1]
    else:
        return [x*(angles/n_frames) for x in range(int(n_frames))]



def construct_bvh(output_name):
    # Create a copy of the existing file
    output_filename = output_name[:-4] + 'v1.bvh'
    shutil.copyfile(output_name, output_filename)
    matrix = np.ones((N_FRAMES, N_DOF))
    yaw = create_movement(YAW_ANGLE, symmetrical=False)
    pitch = create_movement(PITCH_ANGLE, symmetrical=False)
    for col in range(len(matrix.T)):
        if col in range(10):
            matrix.T[col] *= 0
        else:
            if col == 10:
                matrix.T[col] *= yaw
            if col == 11:
                matrix.T[col] *= pitch
            
    try:
        with open(output_filename, 'a') as output_file:
            np.savetxt(output_file, matrix, delimiter=' ', fmt='%f')
        print(f"NumPy matrix has been written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    construct_bvh('gaze.bvh')