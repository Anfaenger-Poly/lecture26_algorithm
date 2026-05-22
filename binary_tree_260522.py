# Tree.get(node.[]) 리프 노드 KeyError 방지
# len(children) > 1 오른쪽 자식 없을 때 None 처리
# print 위치 -> 순회 종류 결정

Tree = {}
Tree['A'] = ['B', 'C']
Tree['B'] = ['D'] # B의 오른쪽 자식이 없음 -> None 생략
Tree['C'] = ['E', 'F']
Tree['D'] = [None, None] # D는 리프 노드 -> 자식이 없음
Tree['E'] = [None, None] # E는 리프 노드 -> 자식이 없음
Tree['F'] = [None, 'G'] # 왼쪽 자식이 없을 땐 None 써야함
Tree['G'] = [None, None] # G는 리프 노드 -> 자식이 없음


def preorder(node):
    if node is None: # 기저 조건 -> 노드가 없으면 더 이상 탐색 할 필요 없음
        return
    print(node, end='')
    children = Tree.get(node, []) # 자식 목록 가져옴, 없으면 빈 리스트
    preorder(children[0] if len(children) > 0 else None) # 왼쪽 재귀
    preorder(children[1] if len(children) > 1 else None) # 오른쪽 재귀

def inorder(node):
    if node is  None: # 기저 조건 -> 노드가 없으면 더 이상 탐색 할 필요 없음
        return
    children = Tree.get(node, [])
    inorder(children[0] if len(children) > 0 else None) # 왼쪽 먼저 재귀
    print(node, end='') # 현재 노드 출력
    inorder(children[1] if len(children) > 1 else None) # 오른쪽 재귀

def postorder(node):
    if node is None: # 기저 조건 -> 노드가 없으면 더 이상 탐색 할 필요 없음
        return
    children = Tree.get(node, [])
    postorder(children[0] if len(children) > 0 else None) # 왼쪽 먼저 재귀
    postorder(children[1] if len(children) > 1 else None) # 오른쪽 재귀
    print(node, end='') # 현재 노드 출력

print('전위 순회: ', end='')
preorder('A') # A부터 전위 순회 시작
print() # 순회 후 줄바꿈

print('중위 순회: ', end='')
inorder('A')
print()

print('후위 순회: ', end='')
postorder('A')
print()