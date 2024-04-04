from dwave.system import EmbeddingComposite, DWaveSampler

linear = {('a', 'a'): -5, ('b', 'b'): -5, ('c', 'c'): -5}
quadratic = {('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}
Q = {**linear, **quadratic}

sampler = EmbeddingComposite(DWaveSampler())

sampleset = sampler.sample_qubo(Q, num_reads=5000)

print(sampleset)