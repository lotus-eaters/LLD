"""
COMMAND DESIGN PATTERN
=======================
Problem (from the doc):
    Need to:
        - execute actions
        - support UNDO
        - decouple the "requester" (who wants an action done) from the
          "receiver" (the object that actually knows how to do it)
        - treat actions themselves as objects (so they can be queued,
          logged, retried, or stacked into an undo history)
 
Fix:
    Every action becomes a `Command` object with execute()/undo().
    A `CommandInvoker` runs commands and keeps a history STACK, so
    undo() always reverses the MOST RECENT action -- classic undo/redo
    mechanics, same idea as Ctrl+Z in any editor.
"""
from abc import ABC,abstractmethod
from typing import List

class Command(ABC):
	@abstractmethod
	def execute(self)->None:
		pass
	@abstractmethod
	def undo(self)->None:
		pass

class OrderProcessor:
	def place_order(self,order_id:str)->None:
		print(f"Order placed for order_id : {order_id}")

	def cancel_order(self,order_id:str)->None:
		print(f"Order Cancelled for order_id : {order_id}")

class OrderCommander(Command):
	def __init__(self,order_processor:OrderProcessor,order_id:str):
		self._order_processor=order_processor
		self._order_id=order_id

	def execute(self)->None:
		self._order_processor.place_order(self._order_id)

	def undo(self)->None:
		self._order_processor.cancel_order(self._order_id)

class CommandInvoker:
	def __init__(self):
		self._history : List[Command]=[]

	def execute(self,command:Command)->None:
		command.execute()
		self._history.append(command)

	def undo(self)->None:
		if self._history:
			self._history.pop().undo()
		else:
			print("Nothing to undo")

if __name__=="__main__":
	process_order=OrderProcessor()
	invoker=CommandInvoker()

	place_ord1=OrderCommander(process_order,"ORD_1")
	place_ord2=OrderCommander(process_order,"ORD_2")
	place_ord3=OrderCommander(process_order,"ORD_3")

	print("Execute Commands")

	invoker.execute(place_ord1)
	invoker.execute(place_ord2)
	invoker.execute(place_ord3)

	invoker.undo()
	invoker.undo()

	invoker.execute(OrderCommander(process_order,"ORD_4"))
	invoker.undo()

	invoker.undo()
	invoker.undo()