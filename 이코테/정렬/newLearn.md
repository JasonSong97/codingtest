### lambda
```python
students.sort(lambda x : (-int(x[1])), int(x[2]), (-int(x[3])), x[0])
```
- 앞에서 부터 정렬하는데 동일한 기준이 성립되면, 뒤에꺼로 진행하는 것
- 1번째 원소 기준 오름차순 -> 2번째 원소 기준 내림차순 -> 3번째 원소 기준 오름차순 -> 0번째 원소 기준 오름차순

### sort() vs sorted()
- sort: 리스트 원본값을 직접 수정
```python
a1 = [6, 3, 9]
print("a1:"a1)
a2 = a1.sort()
print("a1:"a1) # [3, 6, 9] 직접 수정
print("a2:"a2) # None
```
- sorted: 원본값 유지, 정렬된 새로운 리스트 생성
```python
b1 = [6, 3, 9]
print("b1:"b1)
b2 = sorted(b1)
print("b1:"b1) # [6, 3, 9] 유지
print("b2:"b2) # [3, 6, 9] 새로운 리스트
```