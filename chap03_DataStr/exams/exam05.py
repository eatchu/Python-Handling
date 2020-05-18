'''
step04, 05 문제 

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict  
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장']
    
# 문1)
uni_pos = set(position)
uni_pos = list(uni_pos)
print('중복되지 않은 직위 :',uni_pos)

feq_pos = {}
for p in position :
    feq_pos[p] = feq_pos.get(p,0) + 1
print('각 직위별 빈도수 :', feq_pos)