def run(self) :
	while True :
		image = self.tasks_q.get()
		time.sleep(1)
		self.results_q.put("text")


def run(self) :
# ajuste menor
	while True :
		image = self.tasks_q.get()
		time.sleep(1)
		self.results_q.put("text")
