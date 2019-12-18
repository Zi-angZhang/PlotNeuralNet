import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
	to_head('..'),
	to_cor(),
	to_begin(),
	to_input('01-TD-face.jpg', to='(-1,0,0)', width=13, height=13, name='temp'),
	to_Conv('conv0', 64, 16, offset='(0,0,0)', to='(-1,0,0)', height=64, depth=64, width=1),
	to_Conv('conv1', 64, 16, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2),
	to_Conv('conv2', 64, 16, offset='(1,0,0)', to='(conv1-east)', height=64, depth=64, width=2),
	to_Conv('conv3', 32, 64, offset='(2,-5,0)', to='(conv2-east)', height=32, depth=32, width=8),
	to_Conv('conv4', 32, 64, offset='(1,0,0)', to='(conv3-east)', height=32, depth=32, width=8),
	to_Conv('conv5', 16, 256, offset='(2,-5,0)', to='(conv4-east)', height=16, depth=16, width=32),
	to_Conv('conv6', 16, 256, offset='(1,0,0)', to='(conv5-east)', height=16, depth=16, width=32),
	to_Conv('conv7', 32, 64, offset='(2,5,0)', to='(conv6-east)', height=32, depth=32, width=8),
	to_Conv('conv8', 32, 64, offset='(1,0,0)', to='(conv7-east)', height=32, depth=32, width=8),
	to_Conv('conv9', 64, 16, offset='(2,5,0)', to='(conv8-east)', height=64, depth=64, width=2),
	to_Conv('conv10', 64, 16, offset='(1,0,0)', to='(conv9-east)', height=64, depth=64, width=2),
	to_Conv('conv11', 64, 16, offset='(1,0,0)', to='(conv10-east)', height=64, depth=64, width=1),
	to_input('01-TD-face.jpg', to='(conv11-east)', width=13, height=13, name='temp'),
	to_connection(of='conv2', to='conv9'),
	to_connection(of='conv4', to='conv7'),
	to_skip(of='conv0', to='conv11'),
	to_end()]

def main():
	namefile = str(sys.argv[0]).split('.')[0]
	to_generate(arch, namefile+'.tex')
if __name__ == '__main__':
	main()
