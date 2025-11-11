from collections import deque

def solution(n, computers):
    """
    네트워크의 개수를 BFS를 사용하여 계산하는 함수
    :param n: 컴퓨터의 개수
    :param computers: 컴퓨터 연결 정보 (인접 행렬)
    :return: 네트워크의 개수
    """
    
    # 방문 여부를 기록하는 리스트 초기화
    visited = [False] * n
    
    # 네트워크 개수 카운트 변수
    network_count = 0

    # 0번 컴퓨터부터 n-1번 컴퓨터까지 순차적으로 확인
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터를 발견하면
        if not visited[i]:
            # 새로운 네트워크의 시작점으로 간주
            network_count += 1
            
            # BFS 탐색 시작: 큐에 시작 노드 추가
            queue = deque([i])
            visited[i] = True  # 시작 노드 방문 처리

            while queue:
                # 큐에서 노드를 하나 꺼냄
                current_node = queue.popleft()
                
                # 현재 노드와 연결된 다른 모든 노드(neighbor)를 확인
                for neighbor in range(n):
                    # 1. 연결되어 있고 (computers[current_node][neighbor] == 1),
                    # 2. 아직 방문하지 않은 노드라면 (not visited[neighbor])
                    if computers[current_node][neighbor] == 1 and not visited[neighbor]:
                        # 방문 처리 후 큐에 추가하여 다음 탐색 대상으로 지정 (같은 네트워크에 속함)
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
    return network_count