import socket
import _thread

def main():
	host = '127.0.0.1'
	port = 5555
	un = input('Please pick a username: ')

	s = socket.socket()
	s.connect((host, port))

	def getMessages():
		while True:
			data = s.recv(1024).decode('utf-8')
			print(data)

	def sendMessage():
		while True:
			msg = input('')
			s.send((un + ': ' + msg).encode('utf-8'))

	_thread.start_new_thread(getMessages, ())
	_thread.start_new_thread(sendMessage, ())

	while True:
		pass

if __name__ == "__main__":
	main()