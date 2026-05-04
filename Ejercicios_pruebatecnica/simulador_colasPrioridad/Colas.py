class CustomerQueue:
    def __init__(self):
        # Usamos una lista normal para guardar diccionarios o tuplas
        self.queue = []

    def enqueue(self, name: str, priority: int) -> None:
        # Simplemente agregamos al final de la lista
        # O(1) - Muy rápido para insertar
        self.queue.append({
            "name": name, 
            "priority": priority
        })

    def dequeue(self) -> str:
        if not self.queue:
            return None
        
        # 1. Encontrar el cliente con la prioridad más baja (número menor)
        # En caso de empate, al usar min() con la lista original, 
        # Python mantendrá el orden de llegada (el primero que encuentre).
        best_customer = self.queue[0]
        best_index = 0
        
        for i in range(1, len(self.queue)):
            # Si encontramos alguien con número de prioridad menor (más VIP)
            if self.queue[i]["priority"] < best_customer["priority"]:
                best_customer = self.queue[i]
                best_index = i
        
        # 2. Remover al cliente de la lista para que no se repita
        # O(n) - Un poco más lento porque debe reordenar la lista interna
        self.queue.pop(best_index)
        
        return best_customer["name"]

# --- Prueba del código ---
cq = CustomerQueue()
cq.enqueue("Alice", 3)
cq.enqueue("Bob", 2)
cq.enqueue("Charlie", 1)
cq.enqueue("Dave", 2)

print(cq.dequeue())  # Charlie (1)
print(cq.dequeue())  # Bob (2, llegó antes que Dave)
print(cq.dequeue())  # Dave (2)
print(cq.dequeue())  # Alice (3)
print(cq.dequeue())  # None