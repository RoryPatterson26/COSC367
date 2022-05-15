from search import *


import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        

def forward_deduce(kb):
    C = set()
    knowledge_base = list(clauses(kb))
    flag = True
    while flag:
        flag = False
        for clause in knowledge_base:
            if len(clause[1]) == 0:
                C.add(clause[0])
                knowledge_base.remove(clause)
                flag = True
        
        for clause in knowledge_base:
            if all(elem in C  for elem in clause[1]):
                C.add(clause[0])
                knowledge_base.remove(clause)
                flag = True
    return C

