"""Submission for exercise sheet 1

SUBMIT this file as submission_<STUDENTID>.py where
you replace <STUDENTID> with your student ID, e.g.,
submission_1234567.py
"""
import torch
from einops import rearrange

# Exercise 1.1
def assignment_ex1() -> torch.Tensor:
    a = torch.arange(12)
    a = rearrange(a, '(h w) -> h w', h=3, w=4)
    return a
    
# Exercise 1.2
def assignment_ex2() -> torch.Tensor:
    T0 = torch.arange(16*3*3, dtype=torch.float32)
    T0 = rearrange(T0, '(c h w) -> c h w', c=16, h=3, w=3)
    T1 = T0 * 3
    T2 = torch.matmul(T0, T1).sum(dim=(-2,-1))
    return T2 # it wasnt correct


# Exercice 1.3
def assignment_ex3() -> torch.Tensor:
    a = torch.arange(36)
    a = rearrange(a, '(h w) -> h w', h=6, w=6)
    a = rearrange(a, '(h1 h2) (w1 w2) -> (h1 w1) h2 w2', h1=3, w1=3, h2=2, w2=2)
    return a