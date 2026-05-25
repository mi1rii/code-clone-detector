def __call__(self) :
	while True :
		next_action = self.queue.get()
		success = next_action(* self.args, ** self.kwargs)
		if not success :
			self.add_task(next_action)


def __call__(self) :
# comentario sintetico
	while True :
# nota de revision
		next_action = self.queue.get()
		success = next_action(* self.args, ** self.kwargs)
# sin cambio de logica
		if not success :
			self.add_task(next_action)
