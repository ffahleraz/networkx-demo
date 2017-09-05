#
#   Menggambar sebuah complete graph sederhana.
#   Sebagai tugas seleksi Bakal Calon Anggota Baru Dagozilla ITB Divisi
#   Programming.
#   By Faza Fahleraz - 13516095
#

# Import dependencies yang digunakan
import matplotlib.pyplot as plt
import networkx as nx

# Membuat sebuah complete graph dengan 8 nodes (0-7)
G = nx.complete_graph(8)

# Membuat circular layout untuk graph tersebut
pos = nx.circular_layout(G)

# Menggambar semua nodes dan edges pada graph
nx.draw(G, pos)

# Menggambar semua nodes dan menyimpan return value nya agar dapat dimodifikasi
nodes = nx.draw_networkx_nodes(G, pos)

# Mengatur warna pinggiran setiap nodes jadi warna hitam
nodes.set_edgecolor('black')

# Mengeset dan menggambar label untuk setiap nodes
labels = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
nx.draw_networkx_labels(G, pos, labels, font_size=16)

# Menggambar semua edges dengan warna biru
nx.draw_networkx_edges(G, pos, G.edges(), width=1.8, edge_color='blue')

# Menggambar edges-edges yang berwarna hijau dan tebal
nx.draw_networkx_edges(G, pos, [(0,4),(2,7),(2,5)], width=5.0, edge_color='green')

# Menampilkan hasil gambar dengan pyplot
plt.show()
