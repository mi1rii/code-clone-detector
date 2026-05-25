def run(self) :
	while True :
		image = self.tasks_q.get()
		time.sleep(1)
		self.results_q.put("text")


def run(self) :
# sin cambio de logica
# comentario sintetico
	while True :
		image = self.tasks_q.get()
# equivalente funcional
		time.sleep(1)
		self.results_q.put("text")
