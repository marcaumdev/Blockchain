from blockchain import Blockchain

# Uso do Blockchain
blockchain = Blockchain()

# Adicionando blocos
blockchain.add_block("Transação 1: Alice paga Bob 10 BTC")
blockchain.add_block("Transação 2: Bob paga Charlie 5 BTC")

# Validando a cadeia
print("Blockchain válido?", blockchain.is_chain_valid())

# Exibindo o Blockchain
for block in blockchain.chain:
    print(f"Índice: {block.index}")
    print(f"Hash Anterior: {block.previous_hash}")
    print(f"Hash Atual: {block.hash}")
    print(f"Dados: {block.data}")
    print("-" * 30)