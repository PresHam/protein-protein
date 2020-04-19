'''

Predict interactions between iDP and Protein:
PPARy x NCoR
Homo Sapiens


According to the paper by Pau Bernardó and cia:

Structural Bioinformatics on N-CoRNID
Local secondary structural features of N-CoRNID were predicted using the support vector machine-based PSIPRED3.2 server (Buchan
et al., 2013). Disorder propensity of N-CoRNID was assessed with IUPRED (Doszta´ nyi et al., 2005), PrDOS (Ishida and Kinoshita,
2007), PONDR-FIT (Xue et al., 2010) and DISOPRED3 (Jones and Cozzetto, 2015). The GREMLIN software (Kamisetty et al., 2013)
was fed with the N-CoRNID sequence to capture evolutionary conserved sequences by searching a pre-clustered Uniprot database
using the HHblits algorithm (Remmert et al., 2012). A Hidden Markov Model (HMM) multiple sequence alignment (MSA) was generated
excluding hits withR75%gaps. A final set of 61 sequences was used for detecting conservation and co-evolution signatures at
residue-level. Conservation profile was extracted from the HMM MSA using Skylign to compute the probability of observing for a
given position a specific residue above the background (Wheeler et al., 2014). Co-evolution analysis within the MSA was performed
using BIS2 (Oteri et al., 2017), which bypass the statistics requirements to estimate the background noise and the relevance of the coevolution
signal. BIS2 is a combinatorial method that allows identifying co-evolving blocks, instead of only residues, in a small number
of homologous sequences.

'''


# Find libraries, apply knowledge