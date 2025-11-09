import heapq


def huffman_encoding(s):
    freq = {ch: s.count(ch) for ch in set(s)}
    heap = [[wt, [ch, ""]] for ch, wt in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low1, low2 = heapq.heappop(heap), heapq.heappop(heap)
        for p in low1[1:]:
            p[1] = "0" + p[1]
        for p in low2[1:]:
            p[1] = "1" + p[1]
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    return sorted(heap[0][1:], key=lambda x: (len(x[1]), x[0]))


text = input("Enter text: ")
for ch, code in huffman_encoding(text):
    print(f"{ch}\t{code}")
